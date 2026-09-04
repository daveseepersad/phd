# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx>=0.27", "playwright>=1.47"]
# ///
"""Search academic sources, merge results, and rank them for a review topic.

API sources (OpenAlex, Crossref, arXiv) need no browser. Google Scholar, ACM
DL, and IEEE Xplore are read through a Playwright profile; ACM and IEEE
additionally need the institutional session created by auth_setup.py.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import random
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx

sys.path.insert(0, str(Path(__file__).parent))
from _common import (
    DEFAULT_PROFILE_DIR,
    RANKING_PROFILES,
    Paper,
    check_access,
    clean_authors,
    launch_context,
    looks_preprint,
    merge,
    paper_from_openalex,
    reconstruct_abstract,
    run_dir,
    save_papers,
    save_storage_state,
    score_papers,
    seed_library_access,
    tokenize,
    wait_past_challenge,
    write_json_atomic,
)

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

API_SOURCES = {"openalex", "crossref", "arxiv"}
BROWSER_SOURCES = {"scholar", "acm", "ieee"}
AUTH_SOURCES = {"acm", "ieee"}


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic", help="Research question or topic in plain language.")
    parser.add_argument(
        "--sources",
        default="openalex,crossref,scholar",
        help="Comma-separated: openalex, crossref, arxiv, scholar, acm, ieee.",
    )
    parser.add_argument("--per-source", type=int, default=50)
    parser.add_argument("--from-year", type=int, default=None)
    parser.add_argument(
        "--keywords",
        default=None,
        help="Query used for ACM and IEEE, which reject long questions. Auto-condensed when omitted.",
    )
    parser.add_argument(
        "--enrich-limit",
        type=int,
        default=200,
        help="Max records to backfill from OpenAlex; skipped targets are logged.",
    )
    parser.add_argument("--out", type=Path, default=Path("results"))
    parser.add_argument("--profile-dir", type=Path, default=DEFAULT_PROFILE_DIR)
    parser.add_argument(
        "--ranking-profile",
        choices=sorted(RANKING_PROFILES),
        default="frontier",
        help="Named weighting strategy; frontier favors recent work (default).",
    )
    parser.add_argument("--w-relevance", type=float, default=None)
    parser.add_argument("--w-citations", type=float, default=None)
    parser.add_argument("--w-recency", type=float, default=None)
    parser.add_argument("--half-life", type=float, default=None)
    parser.add_argument("--delay", type=float, default=3.0, help="Seconds between browser requests.")
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run the browser headless. ACM and Scholar detect and block this; use xvfb-run instead.",
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def _mailto() -> str:
    return os.getenv("CONTACT_EMAIL", "").strip()


def search_openalex(topic: str, limit: int, from_year: int | None) -> list[Paper]:
    params: dict[str, str | int] = {"search": topic, "per-page": min(limit, 200)}
    if from_year:
        params["filter"] = f"from_publication_date:{from_year}-01-01"
    if _mailto():
        params["mailto"] = _mailto()
    resp = httpx.get("https://api.openalex.org/works", params=params, timeout=60.0)
    resp.raise_for_status()
    return [paper_from_openalex(item) for item in resp.json().get("results", [])]


def search_crossref(topic: str, limit: int, from_year: int | None) -> list[Paper]:
    params: dict[str, str | int] = {"query": topic, "rows": min(limit, 100)}
    if from_year:
        params["filter"] = f"from-pub-date:{from_year}-01-01"
    if _mailto():
        params["mailto"] = _mailto()
    resp = httpx.get("https://api.crossref.org/works", params=params, timeout=60.0)
    resp.raise_for_status()
    papers: list[Paper] = []
    for item in resp.json().get("message", {}).get("items", []):
        titles = item.get("title") or []
        if not titles:
            continue
        container = item.get("container-title") or []
        year = None
        for key in ("published-print", "published-online", "issued"):
            parts = (item.get(key) or {}).get("date-parts") or []
            if parts and parts[0] and isinstance(parts[0][0], int):
                year = parts[0][0]
                break
        authors = [
            " ".join(filter(None, [a.get("given"), a.get("family")])).strip()
            for a in item.get("author", [])
            if a.get("family") or a.get("given")
        ]
        paper = Paper(
            title=titles[0],
            authors=authors,
            year=year,
            venue=container[0] if container else None,
            doi=item.get("DOI"),
            url=item.get("URL"),
            cited_by=item.get("is-referenced-by-count", 0),
            sources=["crossref"],
            discovery_methods=["keyword"],
            work_type=item.get("type"),
            volume=item.get("volume"),
            issue=item.get("issue"),
            pages=item.get("page"),
            publisher=item.get("publisher"),
            authors_source="api" if authors else None,
        )
        # Crossref registers preprints as posted-content; DOI/venue markers
        # catch preprints deposited under other types.
        paper.is_preprint = item.get("type") == "posted-content" or looks_preprint(paper)
        papers.append(paper)
    return papers


ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def parse_arxiv_atom(xml_text: str, from_year: int | None) -> list[Paper]:
    """Map arXiv Atom entries onto Papers.

    The query API has no publication-date filter, so from_year is applied
    here against each entry's published date.
    """
    papers: list[Paper] = []
    for entry in ET.fromstring(xml_text).findall("atom:entry", ATOM_NS):
        title = re.sub(r"\s+", " ", entry.findtext("atom:title", "", ATOM_NS)).strip()
        if not title:
            continue
        published = entry.findtext("atom:published", "", ATOM_NS)
        year = int(published[:4]) if published[:4].isdigit() else None
        if from_year and year and year < from_year:
            continue
        pdf_url = None
        for link in entry.findall("atom:link", ATOM_NS):
            if link.get("title") == "pdf" or link.get("type") == "application/pdf":
                pdf_url = link.get("href")
        abstract = re.sub(r"\s+", " ", entry.findtext("atom:summary", "", ATOM_NS)).strip()
        authors = [
            name.strip()
            for name in (
                author.findtext("atom:name", "", ATOM_NS)
                for author in entry.findall("atom:author", ATOM_NS)
            )
            if name.strip()
        ]
        papers.append(
            Paper(
                title=title,
                authors=authors,
                year=year,
                venue="arXiv preprint",
                doi=entry.findtext("arxiv:doi", None, ATOM_NS),
                url=entry.findtext("atom:id", None, ATOM_NS),
                pdf_url=pdf_url,
                abstract=abstract or None,
                sources=["arxiv"],
                discovery_methods=["keyword"],
                work_type="preprint",
                is_preprint=True,
                authors_source="api" if authors else None,
            )
        )
    return papers


def search_arxiv(topic: str, limit: int, from_year: int | None) -> list[Paper]:
    """arXiv covers the grey literature the publisher databases miss (REVIEW.md B)."""
    params: dict[str, str | int] = {
        "search_query": f"all:{topic}",
        "max_results": min(limit, 200),
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    resp = httpx.get(
        "https://export.arxiv.org/api/query", params=params, timeout=60.0, follow_redirects=True
    )
    resp.raise_for_status()
    return parse_arxiv_atom(resp.text, from_year)


def _polite_sleep(delay: float) -> None:
    time.sleep(delay + random.uniform(0, delay * 0.4))


def condense(topic: str, max_terms: int = 6) -> str:
    """Publisher search engines return nothing for long natural-language questions.

    Keep the first few content-bearing terms in their original order.
    """
    seen: list[str] = []
    for token in tokenize(topic):
        if token not in seen:
            seen.append(token)
        if len(seen) >= max_terms:
            break
    return " ".join(seen)


def _scrape(context, url: str, wait_selector: str, delay: float):
    page = context.new_page()
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=90_000)
        if not wait_past_challenge(page):
            logger.warning("Bot challenge did not clear at %s", url)
        try:
            page.wait_for_selector(wait_selector, timeout=45_000)
        except Exception:  # noqa: BLE001
            logger.warning("No results matched %s at %s", wait_selector, url)
        html_page = page.content()
        _polite_sleep(delay)
        return page, html_page
    except Exception:
        page.close()
        raise


def search_scholar(context, topic: str, limit: int, from_year: int | None, delay: float) -> list[Paper]:
    """Scholar supplies citation counts and coverage the APIs miss."""
    papers: list[Paper] = []
    for start in range(0, min(limit, 40), 10):
        params = {"q": topic, "start": start, "hl": "en"}
        if from_year:
            params["as_ylo"] = from_year
        url = "https://scholar.google.com/scholar?" + urllib.parse.urlencode(params)
        page, _ = _scrape(context, url, "div.gs_ri", delay)
        for block in page.query_selector_all("div.gs_ri"):
            title_el = block.query_selector("h3.gs_rt a")
            if not title_el:
                continue
            meta = block.query_selector("div.gs_a")
            year = None
            if meta:
                for chunk in meta.inner_text().split("-"):
                    for token in chunk.split():
                        if token.strip(",.").isdigit() and 1900 < int(token.strip(",.")) < 2100:
                            year = int(token.strip(",."))
            cited = 0
            for link in block.query_selector_all("div.gs_fl a"):
                text = link.inner_text()
                if text.startswith("Cited by"):
                    cited = int(text.replace("Cited by", "").strip() or 0)
            snippet = block.query_selector("div.gs_rs")
            papers.append(
                Paper(
                    title=title_el.inner_text().strip(),
                    year=year,
                    url=title_el.get_attribute("href"),
                    abstract=snippet.inner_text().strip() if snippet else None,
                    cited_by=cited,
                    sources=["scholar"],
                    discovery_methods=["keyword"],
                )
            )
        page.close()
        if len(papers) < start + 5:
            break
    return papers


def search_acm(context, topic: str, limit: int, from_year: int | None, delay: float) -> list[Paper]:
    params = {"AllField": topic, "pageSize": min(limit, 50)}
    if from_year:
        params["AfterYear"] = from_year
    url = "https://dl.acm.org/action/doSearch?" + urllib.parse.urlencode(params)
    page, _ = _scrape(context, url, "li.search__item", delay)
    papers: list[Paper] = []
    for item in page.query_selector_all("li.search__item"):
        link = item.query_selector("h5.issue-item__title a, .issue-item__title a")
        if not link:
            continue
        href = link.get_attribute("href") or ""
        doi = href.split("/doi/")[-1] if "/doi/" in href else None
        if doi and doi.startswith(("abs/", "full/", "pdf/")):
            doi = doi.split("/", 1)[1]
        venue = item.query_selector(".issue-item__detail a, .epub-section__title")
        abstract = item.query_selector(".issue-item__abstract")
        cited = 0
        # Bare digits under .issue-item__detail include the publication year,
        # so counts come only from ACM's citation-specific markup.
        for span in item.query_selector_all("span.citation, span.citation span"):
            text = span.inner_text().strip().replace(",", "")
            if text.isdigit():
                cited = max(cited, int(text))
        # .loa scopes to the author list; the bare ul.rlist--inline also
        # matches the result-item toolbar (REVIEW.md A1). Profile links are
        # the fallback when ACM renames the class again.
        author_links = item.query_selector_all("ul.rlist--inline.loa li a") or item.query_selector_all(
            'a[href*="/profile/"]'
        )
        authors = clean_authors(a.inner_text().strip() for a in author_links)
        papers.append(
            Paper(
                title=link.inner_text().strip(),
                authors=authors,
                venue=venue.inner_text().strip() if venue else None,
                doi=doi,
                url=urllib.parse.urljoin("https://dl.acm.org", href),
                abstract=abstract.inner_text().strip() if abstract else None,
                cited_by=cited,
                sources=["acm"],
                discovery_methods=["keyword"],
                authors_source="scraped" if authors else None,
            )
        )
    page.close()
    return papers


def search_ieee(context, topic: str, limit: int, from_year: int | None, delay: float) -> list[Paper]:
    params = {"queryText": topic, "rowsPerPage": min(limit, 50)}
    if from_year:
        params["ranges"] = f"{from_year}_{2100}_Year"
    url = "https://ieeexplore.ieee.org/search/searchresult.jsp?" + urllib.parse.urlencode(params)
    page, _ = _scrape(context, url, ".result-item", delay)
    papers: list[Paper] = []
    for item in page.query_selector_all(".List-results-items"):
        link = item.query_selector("h3.result-item-title a, h3 a")
        if not link:
            continue
        href = link.get_attribute("href") or ""
        desc = item.query_selector(".description, .js-displayer-content")
        venue = item.query_selector(".description a, .publisher-info-container")
        authors = clean_authors(
            a.inner_text().strip() for a in item.query_selector_all("xpl-authors-name-list a, .author a")
        )
        papers.append(
            Paper(
                title=link.inner_text().strip(),
                authors=authors,
                venue=venue.inner_text().strip() if venue else None,
                url=urllib.parse.urljoin("https://ieeexplore.ieee.org", href),
                abstract=desc.inner_text().strip() if desc else None,
                sources=["ieee"],
                discovery_methods=["keyword"],
                authors_source="scraped" if authors else None,
            )
        )
    page.close()
    return papers


def enrich_missing(papers: list[Paper], limit: int = 200) -> tuple[int, int]:
    """Backfill authors, year, citations, venue, and DOI from OpenAlex by title match.

    Scholar supplies neither authors nor DOIs, and IEEE often omits the year.
    Without this, citations are unusable and ranking is distorted. API
    authorship also replaces scraped DOM lists outright (REVIEW.md A1).

    Returns (enriched, truncated), where truncated counts targets skipped by
    the limit.
    """
    enriched = 0
    targets = [p for p in papers if not p.year or not p.cited_by or not p.authors or not p.doi]
    truncated = max(len(targets) - limit, 0)
    if truncated:
        logger.warning(
            "enrichment capped: %d of %d targets skipped; raise --enrich-limit to cover them",
            truncated,
            len(targets),
        )
    for paper in targets[:limit]:
        try:
            params = {"filter": f"title.search:{paper.title[:180]}", "per-page": 1}
            if _mailto():
                params["mailto"] = _mailto()
            resp = httpx.get("https://api.openalex.org/works", params=params, timeout=30.0)
            if resp.status_code != 200:
                continue
            hits = resp.json().get("results") or []
            if not hits:
                continue
            hit = hits[0]
            if not _titles_match(paper.title, hit.get("display_name") or ""):
                continue
            location = hit.get("primary_location") or {}
            biblio = hit.get("biblio") or {}
            paper.year = paper.year or hit.get("publication_year")
            paper.cited_by = paper.cited_by or hit.get("cited_by_count", 0)
            paper.doi = paper.doi or (hit.get("doi") or "").replace("https://doi.org/", "") or None
            paper.abstract = paper.abstract or reconstruct_abstract(hit.get("abstract_inverted_index"))
            paper.venue = paper.venue or (location.get("source") or {}).get("display_name")
            paper.openalex_id = paper.openalex_id or (hit.get("id") or "").rsplit("/", 1)[-1] or None
            hit_authors = [
                a["author"]["display_name"]
                for a in hit.get("authorships", [])
                if a.get("author", {}).get("display_name")
            ]
            if hit_authors and paper.authors_source != "api":
                paper.authors = hit_authors
                paper.authors_source = "api"
            paper.work_type = paper.work_type or hit.get("type")
            paper.volume = paper.volume or biblio.get("volume")
            paper.issue = paper.issue or biblio.get("issue")
            first_page, last_page = biblio.get("first_page"), biblio.get("last_page")
            paper.pages = paper.pages or (
                f"{first_page}-{last_page}" if first_page and last_page else first_page
            )
            paper.publisher = paper.publisher or (location.get("source") or {}).get(
                "host_organization_name"
            )
            paper.is_preprint = (
                paper.is_preprint
                or location.get("version") == "submittedVersion"
                or looks_preprint(paper)
            )
            if not paper.pdf_url:
                paper.pdf_url = (hit.get("best_oa_location") or {}).get("pdf_url")
            paper.is_oa = paper.is_oa or (hit.get("open_access") or {}).get("is_oa", False)
            enriched += 1
        except Exception as exc:  # noqa: BLE001
            logger.debug("enrich failed for %r: %s", paper.title[:50], exc)
    return enriched, truncated


def enrich_from_source(papers: list[Paper]) -> int:
    """Fill authors and venue from arXiv or Crossref using the record's own URL.

    Google Scholar returns no structured authors, and OpenAlex title matching
    misses very recent preprints. Going straight to the hosting service is
    authoritative, so citations are never guessed. API authorship replaces
    scraped DOM lists, never the reverse (REVIEW.md A1).
    """
    fixed = 0
    for paper in papers:
        if paper.authors and paper.authors_source == "api":
            continue
        source = f"{paper.url or ''} {paper.pdf_url or ''}"
        arxiv_id = re.search(r"arxiv\.org/(?:abs|pdf)/([\w.]+?)(?:v\d+)?(?:\s|$)", source)
        doi = paper.doi or (
            re.search(r"(?:dl\.acm\.org|doi\.org)/(?:doi/)?(?:abs/|full/|pdf/)?(10\.\d{4,}/[^\s?]+)", source)
            or type("", (), {"group": lambda _s, _n: None})()
        ).group(1)
        try:
            if arxiv_id:
                resp = httpx.get(
                    "https://export.arxiv.org/api/query",
                    params={"id_list": arxiv_id.group(1), "max_results": 1},
                    timeout=30.0,
                    follow_redirects=True,
                )
                names = re.findall(r"<author>\s*<name>([^<]+)</name>", resp.text)
                if names:
                    paper.authors = names
                    paper.authors_source = "api"
                    paper.venue = paper.venue or "arXiv preprint"
                    paper.is_preprint = True
                    fixed += 1
            elif doi:
                resp = httpx.get(f"https://api.crossref.org/works/{doi}", timeout=30.0)
                if resp.status_code == 200:
                    msg = resp.json()["message"]
                    names = [
                        " ".join(filter(None, [a.get("given"), a.get("family")])).strip()
                        for a in msg.get("author", [])
                        if a.get("family") or a.get("given")
                    ]
                    if names:
                        paper.authors = names
                        paper.authors_source = "api"
                        fixed += 1
                    container = msg.get("container-title") or []
                    paper.venue = paper.venue or (container[0] if container else None)
                    paper.doi = paper.doi or msg.get("DOI")
        except Exception as exc:  # noqa: BLE001
            logger.debug("source enrich failed for %r: %s", paper.title[:50], exc)
    return fixed


def _titles_match(a: str, b: str) -> bool:
    """Guard against OpenAlex returning a loosely related paper."""
    ta, tb = set(tokenize(a)), set(tokenize(b))
    if not ta or not tb:
        return False
    return len(ta & tb) / min(len(ta), len(tb)) >= 0.75


def resolve_ranking(args: argparse.Namespace) -> dict[str, float]:
    """Combine a named profile with optional explicit weight overrides."""
    profile = RANKING_PROFILES[args.ranking_profile]
    weights = {
        "relevance": args.w_relevance if args.w_relevance is not None else profile.relevance,
        "citations": args.w_citations if args.w_citations is not None else profile.citations,
        "recency": args.w_recency if args.w_recency is not None else profile.recency,
        "half_life_years": (
            args.half_life if args.half_life is not None else profile.half_life_years
        ),
    }
    if any(weights[name] < 0 for name in ("relevance", "citations", "recency")):
        raise ValueError("ranking weights cannot be negative")
    if abs(sum(weights[name] for name in ("relevance", "citations", "recency")) - 1.0) > 1e-9:
        raise ValueError("relevance, citation, and recency weights must sum to 1.0")
    if weights["half_life_years"] <= 0:
        raise ValueError("half-life must be positive")
    return weights


def append_search_log(root: Path, run_entry: dict[str, Any]) -> None:
    """Persist per-run search evidence for the PRISMA flow diagram (REVIEW.md A4).

    A refresh or re-search appends to the runs list so earlier counts survive.
    """
    path = root / "search-log.json"
    runs: list[dict[str, Any]] = []
    if path.is_file():
        try:
            runs = json.loads(path.read_text(encoding="utf-8")).get("runs") or []
        except (json.JSONDecodeError, OSError):
            logger.warning("Existing %s was unreadable; starting a fresh log", path)
    runs.append(run_entry)
    write_json_atomic(path, {"runs": runs})
    logger.info("Search log -> %s", path)


def append_dedup_log(root: Path, run_entry: dict[str, Any]) -> None:
    """Persist per-run dedup events with the same append shape as the search
    log, so a refresh adds to earlier duplicate counts instead of erasing them.
    """
    path = root / "dedup-log.json"
    runs: list[dict[str, Any]] = []
    if path.is_file():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            logger.warning("Existing %s was unreadable; starting a fresh log", path)
        else:
            if isinstance(existing, dict) and isinstance(existing.get("runs"), list):
                runs = existing["runs"]
            elif isinstance(existing, dict):
                # Legacy flat {generated, event_count, events}: absorb it as
                # the first run.
                runs = [existing]
            elif isinstance(existing, list):
                runs = [{"event_count": len(existing), "events": existing}]
    runs.append(run_entry)
    write_json_atomic(path, {"runs": runs})
    logger.info("Dedup log -> %s", path)


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    requested = [s.strip().lower() for s in args.sources.split(",") if s.strip()]
    unknown = set(requested) - API_SOURCES - BROWSER_SOURCES
    if unknown:
        logger.error("Unknown source(s): %s", ", ".join(sorted(unknown)))
        return EXIT_ERROR

    try:
        weights = resolve_ranking(args)
    except ValueError as exc:
        logger.error("Invalid ranking configuration: %s", exc)
        return EXIT_ERROR

    needs_auth = set(requested) & AUTH_SOURCES
    if needs_auth and not (args.profile_dir / "Default").exists():
        logger.error(
            "%s need an institutional session. Run auth_setup.py first.",
            ", ".join(sorted(needs_auth)),
        )
        return EXIT_ERROR

    groups: list[list[Paper]] = []
    source_log: list[dict[str, Any]] = []
    for name, fn in (
        ("openalex", search_openalex),
        ("crossref", search_crossref),
        ("arxiv", search_arxiv),
    ):
        if name in requested:
            entry: dict[str, Any] = {
                "source": name,
                "interface": "api",
                "query_as_sent": args.topic,
                "requested": args.per_source,
                "returned": 0,
            }
            try:
                found = fn(args.topic, args.per_source, args.from_year)
                logger.info("%-9s %d results", name, len(found))
                groups.append(found)
                entry["returned"] = len(found)
            except Exception as exc:  # noqa: BLE001
                logger.warning("%s failed: %s", name, exc)
                entry["error"] = str(exc)
            source_log.append(entry)

    browser_requested = [s for s in requested if s in BROWSER_SOURCES]
    if browser_requested:
        from playwright.sync_api import sync_playwright

        keywords = args.keywords or condense(args.topic)
        logger.info("ACM/IEEE query: %r", keywords)

        with sync_playwright() as p:
            context = launch_context(p, args.profile_dir, headless=args.headless)
            try:
                if needs_auth:
                    seed_library_access(context, log=logger)
                    check_access(context, log=logger)
                for name, fn in (
                    ("scholar", search_scholar),
                    ("acm", search_acm),
                    ("ieee", search_ieee),
                ):
                    if name not in browser_requested:
                        continue
                    query = args.topic if name == "scholar" else keywords
                    entry = {
                        "source": name,
                        "interface": "browser",
                        "query_as_sent": query,
                        "requested": args.per_source,
                        "returned": 0,
                    }
                    try:
                        found = fn(context, query, args.per_source, args.from_year, args.delay)
                        logger.info("%-9s %d results", name, len(found))
                        groups.append(found)
                        entry["returned"] = len(found)
                    except Exception as exc:  # noqa: BLE001
                        logger.warning("%s failed: %s", name, exc)
                        entry["error"] = str(exc)
                    source_log.append(entry)
            finally:
                save_storage_state(context, args.profile_dir)
                context.close()

    if not groups:
        logger.error("No source returned results.")
        return EXIT_ERROR

    dedup_events: list[dict[str, Any]] = []
    merged = merge(*groups, events=dedup_events)
    source_fixed = enrich_from_source(merged)
    filled, truncated = enrich_missing(merged, limit=args.enrich_limit)
    if filled:
        logger.info("enriched %d records with OpenAlex metadata", filled)
    scoring_meta: dict[str, Any] = {}
    ranked = score_papers(
        merged,
        tokenize(args.topic),
        w_relevance=weights["relevance"],
        w_citations=weights["citations"],
        w_recency=weights["recency"],
        half_life_years=weights["half_life_years"],
        scoring_meta=scoring_meta,
    )

    root = run_dir(args.out, args.topic)
    out_path = root / "candidates.json"
    save_papers(
        out_path,
        args.topic,
        ranked,
        sources=requested,
        ranking_profile=args.ranking_profile,
        weights=weights,
        scoring=scoring_meta,
    )
    logger.info("%d unique papers -> %s", len(ranked), out_path)

    append_search_log(
        root,
        {
            "generated": datetime.now(UTC).isoformat(timespec="seconds"),
            "topic": args.topic,
            "parameters": {
                "sources": requested,
                "per_source": args.per_source,
                "from_year": args.from_year,
                "delay": args.delay,
                "ranking_profile": args.ranking_profile,
                "weights": weights,
            },
            "per_source": source_log,
            "merged_unique": len(merged),
            "enrichment": {
                "openalex_backfilled": filled,
                "source_backfilled": source_fixed,
                "truncated": truncated,
            },
            "scoring": scoring_meta,
        },
    )
    append_dedup_log(
        root,
        {
            "generated": datetime.now(UTC).isoformat(timespec="seconds"),
            "event_count": len(dedup_events),
            "events": dedup_events,
        },
    )
    for paper in ranked[:10]:
        logger.info("  %.3f  %-4s  %s", paper.score, paper.year or "----", paper.title[:88])
    print(root)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
