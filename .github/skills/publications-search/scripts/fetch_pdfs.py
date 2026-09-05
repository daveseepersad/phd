# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx>=0.27", "playwright>=1.47", "pypdf>=4.3"]
# ///
"""Download the top-ranked PDFs for a review run.

Open-access copies come straight over HTTP. Paywalled ACM and IEEE items reuse
the institutional cookies stored by auth_setup.py, which is the same access you
have in the browser.

Requests are deliberately serial and throttled. Publisher terms prohibit
systematic or bulk downloading, and libraries suspend access for traffic that
looks automated. Screen the corpus before downloading and leave --delay at or
above the default.
"""
from __future__ import annotations

import argparse
import io
import json
import logging
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import httpx
from pypdf import PdfReader

sys.path.insert(0, str(Path(__file__).parent))
from _common import (
    DEFAULT_PROFILE_DIR,
    Paper,
    check_access,
    launch_context,
    load_papers,
    openalex_headers,
    save_papers,
    save_storage_state,
    seed_library_access,
    slugify,
)
from search import _polite_sleep

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

PDF_MAGIC = b"%PDF"
MAX_BYTES = 80 * 1024 * 1024
DOWNLOAD_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126 Safari/537.36"
    )
}
PDF_META_SELECTORS = (
    'meta[name="citation_pdf_url"]',
    'meta[name="wkhealth_pdf_url"]',
    'meta[property="og:pdf"]',
)
PDF_LINK_SELECTORS = (
    'a[href$=".pdf"]',
    'a[href*="/pdf?"]',
    'a[href*="download_pub"]',
    'a[data-track-action*="download"]',
    'a.c-pdf-download__link',
)

# Landing pages advertise recommended and related articles, so a generic
# "first .pdf link" can return someone else's paper. Every download is checked
# against its own title before it is saved.
TITLE_STOPWORDS = frozenset(
    ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "into", "is", "it", "its", "of", "on", "or", "the", "to", "with", "using", "via", "toward", "towards", "based", "llm", "llms", "large", "language", "model", "models", "study", "paper", "approach", "towards", "how", "what", "when", "where", "does", "do"]
)
TITLE_MATCH_RATIO = 0.34


def pdf_matches_title(body: bytes, title: str) -> bool:
    """True when the PDF's opening pages actually mention the requested title."""
    terms = {
        word
        for word in re.findall(r"[a-z0-9]{4,}", title.lower())
        if word not in TITLE_STOPWORDS
    }
    if len(terms) < 3:
        return True
    try:
        reader = PdfReader(io.BytesIO(body))
        head = " ".join((page.extract_text() or "") for page in reader.pages[:3])
    except Exception:  # noqa: BLE001
        return True
    if not head.strip():
        return True
    head = re.sub(r"[^a-z0-9]+", " ", head.lower())
    return sum(1 for term in terms if term in head) / len(terms) >= TITLE_MATCH_RATIO


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Run folder containing candidates.json.")
    parser.add_argument(
        "--input",
        type=Path,
        default=None,
        help="Paper JSON to fetch. Defaults to selected.json when present.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional cap. By default every paper in selected.json is fetched.",
    )
    parser.add_argument(
        "--offset",
        type=int,
        default=0,
        help="Zero-based start within the selected corpus for batched retrieval.",
    )
    parser.add_argument("--delay", type=float, default=5.0, help="Seconds between downloads.")
    parser.add_argument("--profile-dir", type=Path, default=DEFAULT_PROFILE_DIR)
    parser.add_argument("--skip-paywalled", action="store_true", help="Open access only.")
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run the browser headless. ACM blocks this; use xvfb-run instead.",
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def candidate_urls(paper: Paper) -> list[str]:
    """Ordered PDF locations to try, cheapest and most permissive first.

    Landing pages are rewritten to their PDF equivalents where the pattern is
    known, so an arXiv abstract link or an ACM /doi/abs/ link still resolves.
    """
    urls: list[str] = []

    def add(url: str | None) -> None:
        # pdf_url is rewritten to the saved local path after a successful
        # download, so a re-run would otherwise hand that path to urllib.
        if url and url.split(":", 1)[0] in ("http", "https") and url not in urls:
            urls.append(url)

    add(paper.pdf_url)

    for source in (paper.url, f"https://doi.org/{paper.doi}" if paper.doi else None):
        if not source:
            continue
        match = re.search(r"arxiv\.org/(?:abs|pdf)/([\w.\-/]+?)(?:v\d+)?$", source)
        if match:
            add(f"https://arxiv.org/pdf/{match.group(1)}")

    doi = paper.doi
    if doi and doi.lower().startswith("10.48550/arxiv."):
        add(f"https://arxiv.org/pdf/{doi.split('arxiv.', 1)[1]}")
    if doi and doi.startswith("10.1145"):
        add(f"https://dl.acm.org/doi/pdf/{doi}")
    if paper.url and "dl.acm.org/doi" in paper.url:
        add(re.sub(r"/doi/(abs/|full/)?", "/doi/pdf/", paper.url))
    if doi and doi.startswith("10.1109"):
        add(f"https://doi.org/{doi}")
    if doi and doi.startswith("10.1007"):
        add(f"https://link.springer.com/content/pdf/{doi}.pdf")
    if doi and doi.lower().startswith("10.2139/ssrn."):
        abstract_id = doi.rsplit(".", 1)[-1]
        add(f"https://papers.ssrn.com/sol3/Delivery.cfm?abstractid={abstract_id}")

    add(paper.url)
    return urls


def refreshed_open_urls(paper: Paper) -> list[str]:
    """Refresh OA locations because indexes often add PDFs after publication."""
    identifier = paper.openalex_id or (f"doi:{paper.doi}" if paper.doi else None)
    if not identifier:
        return []
    try:
        response = httpx.get(
            f"https://api.openalex.org/works/{identifier}",
            timeout=30.0,
            headers=openalex_headers(),
        )
        response.raise_for_status()
        work = response.json()
    except (httpx.HTTPError, ValueError):
        return []

    urls: list[str] = []
    locations = [work.get("best_oa_location") or {}, *(work.get("locations") or [])]
    for location in locations:
        pdf_url = location.get("pdf_url")
        landing = location.get("landing_page_url")
        if pdf_url and pdf_url not in urls:
            urls.append(pdf_url)
        arxiv = re.search(
            r"(?:arxiv\.org/(?:abs|pdf)/|doi\.org/10\.48550/arxiv\.)([\w.]+)",
            landing or "",
            re.IGNORECASE,
        )
        if arxiv:
            url = f"https://arxiv.org/pdf/{arxiv.group(1)}"
            if url not in urls:
                urls.append(url)
    return urls


def looks_like_pdf(body: bytes) -> bool:
    return body[:4] == PDF_MAGIC


def fetch_open(url: str) -> bytes | None:
    try:
        with httpx.Client(
            follow_redirects=True, timeout=90.0, headers=DOWNLOAD_HEADERS
        ) as client:
            resp = client.get(url)
        if resp.status_code == 200 and looks_like_pdf(resp.content):
            return resp.content
        logger.debug("OA fetch %s -> %s", url, resp.status_code)
    except httpx.HTTPError as exc:
        logger.debug("OA fetch failed %s: %s", url, exc)
    try:
        request = urllib.request.Request(url, headers=DOWNLOAD_HEADERS)
        with urllib.request.urlopen(request, timeout=90.0) as response:
            body = response.read(MAX_BYTES + 1)
        if len(body) <= MAX_BYTES and looks_like_pdf(body):
            return body
    except OSError as exc:
        logger.debug("urllib fetch failed %s: %s", url, exc)
    return None


def fetch_authenticated(context, url: str) -> bytes | None:
    """Reuse browser cookies via Playwright's request context."""
    try:
        resp = context.request.get(url, timeout=120_000)
        body = resp.body()
        if resp.ok and looks_like_pdf(body):
            return body
        logger.debug("Auth fetch %s -> %s", url, resp.status)
    except Exception as exc:  # noqa: BLE001
        logger.debug("Auth fetch failed %s: %s", url, exc)
    return None


def resolve_ieee_pdf(context, article_url: str) -> str | None:
    """Resolve an IEEE article or DOI link to its real PDF URL.

    The stamp viewer embeds the PDF in an iframe whose src points at the actual
    file; that iframe is only populated when the session is entitled, so a miss
    here usually means the subscription does not cover the item.
    """
    page = context.new_page()
    try:
        page.goto(article_url, wait_until="domcontentloaded", timeout=90_000)
        page.wait_for_timeout(5000)
        if "ieeexplore.ieee.org" not in page.url:
            return None
        match = re.search(r"/document/(\d+)", page.url)
        if not match:
            return None
        arnumber = match.group(1)

        page.goto(
            f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={arnumber}",
            wait_until="domcontentloaded",
            timeout=90_000,
        )
        page.wait_for_timeout(5000)
        for frame in page.query_selector_all("iframe, embed, object"):
            src = frame.get_attribute("src") or frame.get_attribute("data") or ""
            if ".pdf" in src or "ielx" in src or "getPDF" in src:
                return src if src.startswith("http") else f"https://ieeexplore.ieee.org{src}"
        return f"https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber={arnumber}&ref="
    except Exception as exc:  # noqa: BLE001
        logger.debug("IEEE resolve failed %s: %s", article_url, exc)
        return None
    finally:
        page.close()


def resolve_page_pdf(context, article_url: str) -> str | None:
    """Read standard citation metadata or download links from a landing page."""
    page = context.new_page()
    try:
        page.goto(article_url, wait_until="domcontentloaded", timeout=90_000)
        page.wait_for_timeout(2500)
        for selector in PDF_META_SELECTORS:
            element = page.query_selector(selector)
            url = element.get_attribute("content") if element else None
            if url:
                return url if url.startswith("http") else urllib.parse.urljoin(page.url, url)
        for selector in PDF_LINK_SELECTORS:
            element = page.query_selector(selector)
            url = element.get_attribute("href") if element else None
            if url:
                return url if url.startswith("http") else urllib.parse.urljoin(page.url, url)
        return None
    except Exception as exc:  # noqa: BLE001
        logger.debug("Page PDF resolve failed %s: %s", article_url, exc)
        return None
    finally:
        page.close()


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    candidates = args.run_dir / "candidates.json"
    selected = args.run_dir / "selected.json"
    input_path = args.input or (selected if selected.is_file() else candidates)
    if not input_path.is_file():
        logger.error("No paper input in %s. Run search.py and screen.py first.", args.run_dir)
        return EXIT_ERROR

    # The unscreened-pool guard below is pointless if --input can smuggle in
    # an arbitrary corpus; downloads only ever run against this run's files.
    run_root = args.run_dir.resolve()
    input_resolved = input_path.resolve()
    if not input_resolved.is_relative_to(run_root):
        logger.error("--input must resolve inside %s (got %s).", run_root, input_resolved)
        return EXIT_ERROR
    if input_resolved == candidates.resolve() and args.limit is None:
        logger.error(
            "Refusing to download the unscreened candidate pool. Run screen.py apply "
            "or provide an explicit --limit."
        )
        return EXIT_ERROR
    if args.offset < 0 or (args.limit is not None and args.limit < 1):
        logger.error("--offset must be non-negative and --limit must be positive.")
        return EXIT_ERROR
    input_payload = json.loads(input_path.read_text(encoding="utf-8"))
    all_papers = load_papers(input_path)
    retrieved_path = args.run_dir / "retrieved.json"
    if retrieved_path.is_file():
        prior = {paper.key(): paper for paper in load_papers(retrieved_path)}
        for paper in all_papers:
            cached = prior.get(paper.key())
            if cached and cached.pdf_url and Path(cached.pdf_url).is_file():
                paper.pdf_url = cached.pdf_url
    stop = args.offset + args.limit if args.limit is not None else None
    papers = all_papers[args.offset:stop]
    pdf_dir = args.run_dir / "pdfs"
    pdf_dir.mkdir(parents=True, exist_ok=True)

    def persist(attempted_through: int) -> int:
        """Rewrite retrieved.json so a crash or interrupt cannot lose state."""
        total = sum(
            1 for paper in all_papers if paper.pdf_url and Path(paper.pdf_url).is_file()
        )
        save_papers(
            retrieved_path,
            input_payload.get("topic", ""),
            all_papers,
            fetched=total,
            attempted_through=attempted_through,
            screening_counts=input_payload.get("screening_counts", {}),
            baseline_size=input_payload.get("baseline_size", 20),
        )
        return total
    logger.info(
        "Fetching screened papers %d-%d of %d at %.1fs intervals",
        args.offset + 1,
        args.offset + len(papers),
        len(all_papers),
        args.delay,
    )

    context = None
    playwright = None
    if not args.skip_paywalled:
        if not (args.profile_dir / "Default").exists():
            logger.warning("No institutional profile; open access only. Run auth_setup.py.")
        else:
            from playwright.sync_api import sync_playwright

            playwright = sync_playwright().start()
            context = launch_context(playwright, args.profile_dir, headless=args.headless)
            seed_library_access(context, log=logger)
            expired = [name for name, ok in check_access(context, log=logger).items() if not ok]
            if expired:
                logger.warning(
                    "Session expired for: %s. Paywalled items will be skipped. "
                    "Re-run auth_setup.py to restore access.",
                    ", ".join(expired),
                )

    fetched = 0
    try:
        for index, paper in enumerate(papers, start=args.offset + 1):
            name = f"{index:02d}-{slugify(paper.title, 70)}.pdf"
            target = pdf_dir / name
            if target.exists():
                logger.info("[%02d] cached  %s", index, name)
                paper.pdf_url = str(target)
                fetched += 1
                persist(index)
                continue

            body = None
            open_urls = refreshed_open_urls(paper)
            urls: list[str] = []
            for url in [*open_urls, *candidate_urls(paper)]:
                if url not in urls:
                    urls.append(url)
            for url in urls:
                if url in open_urls or "arxiv.org/pdf" in url:
                    body = fetch_open(url)
                elif ("10.1109" in url or "ieeexplore" in url) and context:
                    resolved = resolve_ieee_pdf(context, url)
                    if resolved:
                        body = fetch_authenticated(context, resolved)
                if body is None and context:
                    body = fetch_authenticated(context, url)
                if body is None and context and not url.lower().endswith(".pdf"):
                    resolved = resolve_page_pdf(context, url)
                    if resolved:
                        body = fetch_authenticated(context, resolved)
                if body is None and paper.is_oa:
                    body = fetch_open(url)
                if body and not pdf_matches_title(body, paper.title):
                    logger.warning(
                        "[%02d] discarded PDF from %s: content does not match the title",
                        index,
                        url[:80],
                    )
                    body = None
                    continue
                if body:
                    logger.debug("[%02d] hit via %s", index, url)
                    break

            if body and len(body) <= MAX_BYTES:
                target.write_bytes(body)
                paper.pdf_url = str(target)
                fetched += 1
                logger.info("[%02d] saved   %s (%d KB)", index, name, len(body) // 1024)
            else:
                paper.pdf_url = None
                logger.warning("[%02d] MISSING %s", index, paper.title[:70])
            persist(index)
            _polite_sleep(args.delay)
    except KeyboardInterrupt:
        logger.warning("Interrupted; retrieved.json reflects every completed attempt.")
        return 130
    finally:
        if context:
            save_storage_state(context, args.profile_dir)
            context.close()
        if playwright:
            playwright.stop()

    total_fetched = persist(args.offset + len(papers))
    logger.info(
        "Retrieved %d/%d total (%d in this batch) -> %s",
        total_fetched,
        len(all_papers),
        fetched,
        retrieved_path,
    )
    return EXIT_SUCCESS if fetched else EXIT_FAILURE


if __name__ == "__main__":
    sys.exit(main())
