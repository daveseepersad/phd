# /// script
# requires-python = ">=3.12"
# dependencies = ["beautifulsoup4>=4.12", "httpx>=0.27", "playwright>=1.47"]
# ///
"""Recover missing abstracts from DOI landing pages and publisher metadata.

Direct HTML is attempted first. An authenticated Playwright browser handles
JavaScript-rendered and institution-gated pages. Every attempt is recorded;
blocked pages remain unresolved and are never silently excluded.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent))
from _common import (
    DEFAULT_PROFILE_DIR,
    Paper,
    launch_context,
    save_storage_state,
    score_papers,
    seed_library_access,
    tokenize,
    wait_past_challenge,
    write_json_atomic,
)
from search import _polite_sleep
from snowball import ranking_metadata

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

META_FIELDS = (
    ("name", "citation_abstract"),
    ("name", "dc.description"),
    ("name", "DC.Description"),
    ("property", "og:description"),
    ("name", "description"),
)
VISIBLE_SELECTORS = (
    "div.abstract-text",
    ".c-article-section__content",
    ".abstractSection.abstractInFull",
    ".abstractSection",
    ".article__abstract",
    "section.Abstract",
    "div.abstract",
    "#abstract .html-p",
)
REJECT_PHRASES = (
    "just a moment",
    "checking your browser",
    "enable javascript and cookies",
    "access denied",
    "cookie policy",
    "we use cookies",
    "the doi system",
)

# Generic social/SEO meta tags often carry a site-wide publisher blurb rather
# than the paper's abstract, so text taken from them must also look like it
# belongs to this paper.
GENERIC_META_SOURCES = (
    "meta[name=description]",
    "meta[property=og:description]",
    "json-ld.description",
)
STOPWORDS = frozenset(
    ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "into", "is", "it", "its", "of", "on", "or", "the", "to", "with", "using", "toward", "towards", "via", "based", "multi", "single", "new", "study", "paper", "approach"]
)


def looks_like_own_abstract(text: str, title: str) -> bool:
    """A real abstract restates its own subject; publisher boilerplate does not.

    Deliberately language-agnostic: one landing page returned Polish marketing
    copy for the publishing house, which no English phrase list would catch.
    """
    terms = {t for t in re.findall(r"[a-z0-9]{4,}", title.lower()) if t not in STOPWORDS}
    if len(terms) < 3:
        return True
    lowered = text.lower()
    return sum(1 for term in terms if term in lowered) / len(terms) >= 0.2


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--profile-dir", type=Path, default=DEFAULT_PROFILE_DIR)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--delay", type=float, default=1.5)
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def clean_abstract(value: str | None) -> str | None:
    if not value:
        return None
    text = BeautifulSoup(value, "html.parser").get_text(" ", strip=True)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^abstract\s*[:.\-—]?\s*", "", text, flags=re.IGNORECASE)
    lowered = text.lower()
    if len(text) < 120 or len(text) > 12_000:
        return None
    if any(phrase in lowered for phrase in REJECT_PHRASES):
        return None
    return text


def abstract_from_html(html: str) -> tuple[str | None, str | None]:
    soup = BeautifulSoup(html, "html.parser")
    for attribute, value in META_FIELDS:
        tag = soup.find("meta", attrs={attribute: value})
        abstract = clean_abstract(tag.get("content") if tag else None)
        if abstract:
            return abstract, f"meta[{attribute}={value}]"

    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        try:
            payload = json.loads(script.get_text())
        except (json.JSONDecodeError, TypeError):
            continue
        objects = payload if isinstance(payload, list) else [payload]
        for item in objects:
            if not isinstance(item, dict):
                continue
            abstract = clean_abstract(item.get("description"))
            if abstract:
                return abstract, "json-ld.description"
    return None, None


def direct_abstract(url: str) -> tuple[str | None, str | None, str | None]:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126 Safari/537.36"
        )
    }
    try:
        response = httpx.get(url, headers=headers, follow_redirects=True, timeout=40.0)
        content_type = response.headers.get("content-type", "")
        if response.status_code == 200 and "html" in content_type:
            abstract, method = abstract_from_html(response.text)
            return abstract, method, str(response.url)
        return None, f"http-{response.status_code}", str(response.url)
    except httpx.HTTPError as exc:
        return None, type(exc).__name__, None


def browser_abstract(page, url: str) -> tuple[str | None, str | None, str | None]:
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=90_000)
        if not wait_past_challenge(page, timeout_s=10.0):
            return None, "browser-challenge", page.url
        page.wait_for_timeout(2500)
        abstract, method = abstract_from_html(page.content())
        if abstract:
            return abstract, method, page.url
        for selector in VISIBLE_SELECTORS:
            element = page.query_selector(selector)
            abstract = clean_abstract(element.inner_text() if element else None)
            if abstract:
                return abstract, f"visible:{selector}", page.url
        return None, "browser-no-abstract", page.url
    except Exception as exc:  # noqa: BLE001
        return None, type(exc).__name__, page.url


def paper_url(paper: Paper) -> str | None:
    if paper.doi:
        return f"https://doi.org/{paper.doi}"
    if paper.key().startswith("10."):
        return f"https://doi.org/{paper.key()}"
    return paper.url


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def write_candidates(path: Path, payload: dict[str, Any], papers: list[Paper]) -> None:
    payload["papers"] = [paper.to_dict() for paper in papers]
    write_json_atomic(path, payload)


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    candidate_path = args.run_dir / "candidates.json"
    screening_path = args.run_dir / "screening.json"
    if not candidate_path.is_file() or not screening_path.is_file():
        logger.error("Run search.py and screen.py init before abstract recovery.")
        return EXIT_ERROR

    candidates = json.loads(candidate_path.read_text(encoding="utf-8"))
    papers = [Paper.from_dict(item) for item in candidates.get("papers", [])]
    screening = json.loads(screening_path.read_text(encoding="utf-8"))
    by_key = {paper.key(): paper for paper in papers}
    by_title = {normalized_title(paper.title): paper for paper in papers}

    # Bind unresolved records to candidates by identity, never by position:
    # ranks freeze at the last screen.py init while every snowball round
    # re-ranks candidates.json (REVIEW.md A3).
    targets: list[tuple[dict[str, Any], Paper]] = []
    for record in screening.get("records", []):
        if record.get("decision") != "unresolved":
            continue
        paper = by_key.get(record["key"])
        if paper is not None and normalized_title(paper.title) != normalized_title(record["title"]):
            logger.error(
                'Key %s binds to a different title: screening "%s" vs candidates "%s".',
                record["key"], record["title"], paper.title,
            )
            return EXIT_ERROR
        if paper is None:
            # A backfilled DOI turns a title-derived key into a DOI key; the
            # normalized title still identifies the record.
            paper = by_title.get(normalized_title(record["title"]))
        if paper is None:
            logger.error(
                'Unresolved record missing from candidates.json: key=%s "%s".',
                record["key"], record["title"],
            )
            return EXIT_ERROR
        targets.append((record, paper))
    stop = args.offset + args.limit if args.limit is not None else None
    targets = targets[args.offset:stop]

    from playwright.sync_api import sync_playwright

    attempts: list[dict[str, Any]] = []
    recovered = 0
    try:
        with sync_playwright() as playwright:
            context = launch_context(playwright, args.profile_dir, headless=args.headless)
            seed_library_access(context, log=logger)
            page = context.new_page()
            try:
                for position, (record, paper) in enumerate(targets, start=1):
                    url = paper_url(paper)
                    result: dict[str, Any] = {
                        "key": record["key"],
                        "rank": record.get("rank"),
                        "title": paper.title,
                        "requested_url": url,
                        "status": "missing",
                        "method": None,
                        "resolved_url": None,
                    }
                    if not url:
                        result["method"] = "no-url"
                        attempts.append(result)
                        continue

                    try:
                        abstract, method, resolved = direct_abstract(url)
                        if not abstract:
                            abstract, method, resolved = browser_abstract(page, url)
                    except Exception as exc:  # noqa: BLE001
                        # httpx.InvalidURL and other non-HTTPError failures
                        # (e.g. a malformed scraped DOI) must not abort the
                        # remaining targets.
                        abstract, method, resolved = None, type(exc).__name__, None
                        result["error"] = str(exc)
                        logger.warning("%s fetch failed: %s: %s", record["key"], type(exc).__name__, exc)
                    if abstract and method in GENERIC_META_SOURCES and not looks_like_own_abstract(
                        abstract, paper.title
                    ):
                        logger.info(
                            "[%s] discarding %s: text shares no terms with the title (publisher boilerplate)",
                            record["key"],
                            method,
                        )
                        abstract, method = None, f"{method}-boilerplate"
                    if abstract:
                        paper.abstract = abstract
                        paper.url = resolved or paper.url
                        result["status"] = "recovered"
                        recovered += 1
                        # Persist immediately so an interrupt cannot discard an
                        # abstract that already cost a page fetch.
                        write_candidates(candidate_path, candidates, papers)
                    result["method"] = method
                    result["resolved_url"] = resolved
                    result["characters"] = len(abstract) if abstract else 0
                    attempts.append(result)
                    logger.info(
                        "[%d/%d %s] %s via %s",
                        position,
                        len(targets),
                        record["key"],
                        result["status"],
                        method,
                    )
                    _polite_sleep(args.delay)
            finally:
                page.close()
                save_storage_state(context, args.profile_dir)
                context.close()
    finally:
        # Runs on every exit path, so an abort after a recovery can never
        # leave a persisted abstract sitting at its no-abstract score.
        if recovered:
            # A recovered abstract changes the relevance component, so the
            # corpus is re-ranked with the run's stored weights instead of
            # leaving the record at its no-abstract score (REVIEW.md medium
            # finding).
            profile_name, weights = ranking_metadata(candidates)
            before = {paper.key(): index for index, paper in enumerate(papers)}
            scoring_meta: dict[str, Any] = {}
            papers = score_papers(
                papers,
                tokenize(candidates["topic"]),
                weights["relevance"],
                weights["citations"],
                weights["recency"],
                weights["half_life_years"],
                scoring_meta=scoring_meta,
            )
            moved = sum(1 for index, paper in enumerate(papers) if before[paper.key()] != index)
            candidates["ranking_profile"] = profile_name
            candidates["weights"] = weights
            candidates["scoring"] = scoring_meta
            write_candidates(candidate_path, candidates, papers)
            logger.info("Re-ranked %d candidates after recovery; %d moved position.", len(papers), moved)

        report = {
            "generated": datetime.now(UTC).isoformat(),
            "attempted": len(targets),
            "recovered": recovered,
            "offset": args.offset,
            "limit": args.limit,
            "attempts": attempts,
        }
        report_path = args.run_dir / "abstract-recovery.json"
        write_json_atomic(report_path, report)
        logger.info("Recovered %d/%d abstracts -> %s", recovered, len(targets), report_path)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())