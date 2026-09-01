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
    seed_library_access,
    wait_past_challenge,
)
from search import _polite_sleep

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
    papers = [Paper(**item) for item in candidates.get("papers", [])]
    screening = json.loads(screening_path.read_text(encoding="utf-8"))
    unresolved_ranks = [
        item["rank"] for item in screening.get("records", []) if item.get("decision") == "unresolved"
    ]
    stop = args.offset + args.limit if args.limit is not None else None
    ranks = unresolved_ranks[args.offset:stop]
    by_rank = {rank: papers[rank - 1] for rank in ranks}

    from playwright.sync_api import sync_playwright

    attempts: list[dict[str, Any]] = []
    recovered = 0
    with sync_playwright() as playwright:
        context = launch_context(playwright, args.profile_dir, headless=args.headless)
        seed_library_access(context, log=logger)
        page = context.new_page()
        try:
            for position, rank in enumerate(ranks, start=1):
                paper = by_rank[rank]
                url = paper_url(paper)
                result: dict[str, Any] = {
                    "rank": rank,
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

                abstract, method, resolved = direct_abstract(url)
                if not abstract:
                    abstract, method, resolved = browser_abstract(page, url)
                if abstract:
                    paper.abstract = abstract
                    paper.url = resolved or paper.url
                    result["status"] = "recovered"
                    recovered += 1
                result["method"] = method
                result["resolved_url"] = resolved
                result["characters"] = len(abstract) if abstract else 0
                attempts.append(result)
                logger.info(
                    "[%d/%d rank %d] %s via %s",
                    position,
                    len(ranks),
                    rank,
                    result["status"],
                    method,
                )
                _polite_sleep(args.delay)
        finally:
            page.close()
            save_storage_state(context, args.profile_dir)
            context.close()

    candidates["papers"] = [paper.to_dict() for paper in papers]
    candidate_path.write_text(
        json.dumps(candidates, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    report = {
        "generated": datetime.now(UTC).isoformat(),
        "attempted": len(ranks),
        "recovered": recovered,
        "offset": args.offset,
        "limit": args.limit,
        "attempts": attempts,
    }
    report_path = args.run_dir / "abstract-recovery.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("Recovered %d/%d abstracts -> %s", recovered, len(ranks), report_path)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())