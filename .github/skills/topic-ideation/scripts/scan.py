# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx>=0.27"]
# ///
"""Scan candidate research areas across OpenAlex and arXiv for topic ideation.

API-only companion to the publications-search skill: no browser and no
institutional session, so it is safe to run unattended. For each area it
collects publication volume by year, top venues, top-cited and most-recent
works, and fresh arXiv submissions, then renders one comparison card per area
for the agent to rubric-score in Stage 2.
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
import unicodedata
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

OPENALEX_WORKS = "https://api.openalex.org/works"
ARXIV_API = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}

# H2 headings in the seed file double as area queries; the rationale text
# under each heading is for the agent, not the scanner.
DEFAULT_AREAS_FILE = Path(__file__).resolve().parent.parent / "references" / "SEED-AREAS.md"

# arXiv asks automated clients for roughly 3 s between requests, which can
# exceed --delay when one area retries with a broader query.
ARXIV_MIN_DELAY = 3.0

VENUE_LIMIT = 8

# Deliberately standalone: these helpers are duplicated from the sibling
# publications-search skill so ideation runs without it on sys.path.
STOPWORDS = frozenset(
    ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "have", "how", "in", "is", "it", "its", "of", "on", "or", "that", "the", "to", "was", "were", "what", "when", "where", "which", "who", "why", "with", "using", "use", "can", "could", "do", "does"]
)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--areas",
        default=None,
        help="Semicolon-separated area queries; overrides --areas-file.",
    )
    parser.add_argument(
        "--areas-file",
        type=Path,
        default=DEFAULT_AREAS_FILE,
        help="Markdown file whose H2 headings name the areas (default: references/SEED-AREAS.md).",
    )
    parser.add_argument("--from-year", type=int, default=2022)
    parser.add_argument(
        "--per-area",
        type=int,
        default=15,
        help="Top-cited and most-recent works fetched per area.",
    )
    parser.add_argument("--out", type=Path, default=Path("results"))
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between API calls.")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def _mailto() -> str:
    return os.getenv("CONTACT_EMAIL", "").strip()


def _polite_sleep(delay: float) -> None:
    time.sleep(delay + random.uniform(0, delay * 0.4))


def tokenize(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", (text or "").lower()) if t not in STOPWORDS]


def slugify(text: str, max_len: int = 60) -> str:
    """Filesystem-safe slug used for the ideation run folder."""
    norm = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    norm = re.sub(r"[^\w\s-]", "", norm).strip().lower()
    return re.sub(r"[-\s]+", "-", norm)[:max_len].strip("-") or "untitled"


def _content_terms(area: str, max_terms: int) -> list[str]:
    """First few unique content-bearing terms, in original order."""
    seen: list[str] = []
    for token in tokenize(area):
        if token not in seen:
            seen.append(token)
        if len(seen) >= max_terms:
            break
    return seen


def parse_areas_md(path: Path) -> list[str]:
    """H2 headings are area names; everything else is agent-facing rationale."""
    areas: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            name = line[3:].strip()
            if name:
                areas.append(name)
    return areas


def run_slug(areas: list[str]) -> str:
    # Single-area smoke tests keep a readable folder name; sweeps use a count.
    return slugify(areas[0], 40) if len(areas) == 1 else f"{len(areas)}-areas"


def _openalex(params: dict[str, Any]) -> dict[str, Any]:
    if _mailto():
        params["mailto"] = _mailto()
    resp = httpx.get(OPENALEX_WORKS, params=params, timeout=60.0)
    resp.raise_for_status()
    return resp.json()


def _year_filter(from_year: int) -> str:
    return f"from_publication_date:{from_year}-01-01"


def volume_by_year(area: str, from_year: int) -> dict[str, int]:
    """Publication counts per year; keys are strings for JSON stability."""
    data = _openalex(
        {"search": area, "filter": _year_filter(from_year), "group_by": "publication_year"}
    )
    counts: dict[str, int] = {}
    for group in data.get("group_by", []):
        key = str(group.get("key") or "")
        if key.isdigit():
            counts[key] = group.get("count", 0)
    return dict(sorted(counts.items()))


def top_venues(area: str, from_year: int, limit: int = VENUE_LIMIT) -> list[dict[str, Any]]:
    data = _openalex(
        {
            "search": area,
            "filter": _year_filter(from_year),
            "group_by": "primary_location.source.id",
        }
    )
    venues: list[dict[str, Any]] = []
    for group in data.get("group_by", []):
        # OpenAlex reports works with no source under the literal key "unknown".
        name = group.get("key_display_name")
        if not name or name.lower() == "unknown":
            continue
        venues.append({"venue": name, "count": group.get("count", 0)})
        if len(venues) >= limit:
            break
    return venues


# select= trims each work to the fields the landscape actually uses.
_WORK_FIELDS = "id,doi,display_name,publication_year,publication_date,cited_by_count,primary_location,authorships"


def _work(item: dict[str, Any]) -> dict[str, Any]:
    location = item.get("primary_location") or {}
    doi = (item.get("doi") or "").replace("https://doi.org/", "") or None
    return {
        "title": item.get("display_name") or "",
        "authors": [
            authorship["author"]["display_name"]
            for authorship in (item.get("authorships") or [])[:3]
            if authorship.get("author", {}).get("display_name")
        ],
        "year": item.get("publication_year"),
        "date": item.get("publication_date"),
        "venue": (location.get("source") or {}).get("display_name"),
        "doi": doi,
        "cited_by": item.get("cited_by_count", 0),
        "url": item.get("doi") or location.get("landing_page_url"),
    }


def fetch_works(area: str, from_year: int, limit: int, sort: str) -> list[dict[str, Any]]:
    data = _openalex(
        {
            "search": area,
            "filter": _year_filter(from_year),
            "sort": sort,
            "per-page": min(limit, 200),
            "select": _WORK_FIELDS,
        }
    )
    return [_work(item) for item in data.get("results", [])]


def _parse_atom(xml_text: str) -> list[dict[str, Any]]:
    root = ET.fromstring(xml_text)
    entries: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        title = re.sub(r"\s+", " ", entry.findtext("atom:title", "", ATOM_NS) or "").strip()
        if not title:
            continue
        url = (entry.findtext("atom:id", "", ATOM_NS) or "").strip().replace("http://", "https://")
        entries.append(
            {
                "title": title,
                "published": (entry.findtext("atom:published", "", ATOM_NS) or "")[:10],
                "url": url,
                "arxiv_id": url.rsplit("/abs/", 1)[-1] if "/abs/" in url else None,
                "authors": [
                    name.text.strip()
                    for name in entry.findall("atom:author/atom:name", ATOM_NS)
                    if name.text and name.text.strip()
                ],
            }
        )
    return entries


def arxiv_recent(area: str, limit: int, delay: float) -> list[dict[str, Any]]:
    """Most-recent arXiv submissions matching the area's content terms.

    arXiv's API treats a quoted multi-word area as an exact phrase and returns
    nothing for natural-language headings, so terms are ANDed instead; when a
    strict conjunction finds nothing, the query backs off to the two leading
    terms.
    """
    terms = _content_terms(area, max_terms=4)
    attempts = [terms] if len(terms) <= 2 else [terms, terms[:2]]
    entries: list[dict[str, Any]] = []
    for index, attempt in enumerate(attempts):
        if not attempt:
            break
        if index:
            _polite_sleep(max(delay, ARXIV_MIN_DELAY))
        resp = httpx.get(
            ARXIV_API,
            params={
                "search_query": " AND ".join(f"all:{term}" for term in attempt),
                "sortBy": "submittedDate",
                "sortOrder": "descending",
                "max_results": limit,
            },
            timeout=60.0,
            follow_redirects=True,
        )
        resp.raise_for_status()
        entries = _parse_atom(resp.text)
        if entries:
            break
    return entries


def momentum(counts: dict[str, int]) -> dict[str, Any]:
    """Compare the last full year against the year before it.

    The current year is always partial, so it never enters the ratio; the
    per-year table still shows it, flagged as partial, for eyeballing.
    """
    last_full = datetime.now(UTC).year - 1
    prior = last_full - 1
    last_count = counts.get(str(last_full), 0)
    prior_count = counts.get(str(prior), 0)
    return {
        "last_full_year": last_full,
        "prior_year": prior,
        "last_full_year_works": last_count,
        "prior_year_works": prior_count,
        "ratio": round(last_count / prior_count, 2) if prior_count else None,
    }


def scan_area(area: str, from_year: int, per_area: int, delay: float) -> dict[str, Any]:
    """Collect one area's landscape, degrading per step instead of aborting."""
    record: dict[str, Any] = {
        "area": area,
        "volume_by_year": {},
        "momentum": {},
        "top_venues": [],
        "top_cited": [],
        "most_recent": [],
        "arxiv_recent": [],
        "errors": [],
    }
    steps: tuple[tuple[str, Any], ...] = (
        ("volume_by_year", lambda: volume_by_year(area, from_year)),
        ("top_venues", lambda: top_venues(area, from_year)),
        ("top_cited", lambda: fetch_works(area, from_year, per_area, "cited_by_count:desc")),
        ("most_recent", lambda: fetch_works(area, from_year, per_area, "publication_date:desc")),
        ("arxiv_recent", lambda: arxiv_recent(area, per_area, delay)),
    )
    for name, fetch in steps:
        try:
            record[name] = fetch()
        except (httpx.HTTPError, ET.ParseError, ValueError) as exc:
            # One flaky endpoint degrades this area; other areas keep going.
            logger.warning("%s: %s failed: %s", area, name, exc)
            record["errors"].append({"step": name, "error": str(exc)})
        _polite_sleep(delay)
    record["momentum"] = momentum(record["volume_by_year"])
    return record


def _empty(record: dict[str, Any]) -> bool:
    return not (
        record["volume_by_year"]
        or record["top_cited"]
        or record["most_recent"]
        or record["arxiv_recent"]
    )


def _md_escape(text: str) -> str:
    return text.replace("|", "\\|")


def _momentum_label(mom: dict[str, Any]) -> str:
    return f"{mom['ratio']}x" if mom.get("ratio") is not None else "n/a"


def _area_card(record: dict[str, Any], from_year: int, current_year: int) -> list[str]:
    lines = [f"## {record['area']}", ""]
    mom = record["momentum"]
    if mom.get("ratio") is not None:
        lines.append(
            f"Momentum: {mom['last_full_year_works']:,} works in {mom['last_full_year']} "
            f"vs {mom['prior_year_works']:,} in {mom['prior_year']} "
            f"({_momentum_label(mom)})."
        )
    else:
        lines.append(
            f"Momentum: {mom['last_full_year_works']:,} works in {mom['last_full_year']}; "
            f"no {mom['prior_year']} baseline to compare."
        )
    lines.append("")
    if record["volume_by_year"]:
        lines += ["| Year | Works |", "|---|---:|"]
        for year, count in record["volume_by_year"].items():
            partial = " (partial)" if int(year) == current_year else ""
            lines.append(f"| {year}{partial} | {count:,} |")
        lines.append("")
    if record["top_venues"]:
        lines.append(
            "Top venues: "
            + " · ".join(f"{v['venue']} ({v['count']})" for v in record["top_venues"])
        )
        lines.append("")
    if record["top_cited"]:
        lines += [
            f"### Key papers (top-cited since {from_year})",
            "",
            "| Year | Cites | Paper | DOI |",
            "|---|---:|---|---|",
        ]
        for work in record["top_cited"][:10]:
            lines.append(
                f"| {work['year'] or '----'} | {work['cited_by']:,} "
                f"| {_md_escape(work['title'])} | {work['doi'] or '—'} |"
            )
        lines.append("")
    if record["arxiv_recent"]:
        lines += ["### Fresh arXiv submissions", ""]
        for entry in record["arxiv_recent"][:5]:
            lines.append(f"- {entry['published']} — {_md_escape(entry['title'])} ({entry['url']})")
        lines.append("")
    if record["errors"]:
        failed = ", ".join(err["step"] for err in record["errors"])
        lines += [f"> Scan degraded: {failed} unavailable for this area.", ""]
    return lines


def render_markdown(payload: dict[str, Any]) -> str:
    current_year = datetime.now(UTC).year
    areas = payload["areas"]
    last_full, prior = current_year - 1, current_year - 2
    lines = [
        "# Landscape Scan — Topic Ideation",
        "",
        (
            f"Generated {payload['generated']} · window from {payload['from_year']} "
            f"· {payload['per_area']} works per list per area."
        ),
        "",
        "## Momentum overview",
        "",
        (
            f"Ranked by {last_full}-vs-{prior} volume growth. "
            f"{current_year} is partial and never enters the ratio."
        ),
        "",
        f"| Area | {prior} | {last_full} | Momentum |",
        "|---|---:|---:|---|",
    ]
    ranked = sorted(
        areas,
        key=lambda r: (r["momentum"].get("ratio") is not None, r["momentum"].get("ratio") or 0.0),
        reverse=True,
    )
    for record in ranked:
        mom = record["momentum"]
        lines.append(
            f"| {_md_escape(record['area'])} | {mom['prior_year_works']:,} "
            f"| {mom['last_full_year_works']:,} | {_momentum_label(mom)} |"
        )
    lines.append("")
    for record in areas:
        lines += _area_card(record, payload["from_year"], current_year)
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    if args.areas:
        areas = [a.strip() for a in args.areas.split(";") if a.strip()]
    else:
        if not args.areas_file.is_file():
            logger.error("Areas file not found: %s", args.areas_file)
            return EXIT_ERROR
        areas = parse_areas_md(args.areas_file)
    if not areas:
        logger.error("No areas to scan.")
        return EXIT_ERROR
    if args.per_area < 1:
        logger.error("--per-area must be at least 1.")
        return EXIT_ERROR

    results: list[dict[str, Any]] = []
    for index, area in enumerate(areas, 1):
        logger.info("[%d/%d] %s", index, len(areas), area)
        results.append(scan_area(area, args.from_year, args.per_area, args.delay))

    if all(_empty(record) for record in results):
        logger.error("Every area came back empty. Check network access and try again.")
        return EXIT_ERROR

    payload = {
        "generated": datetime.now(UTC).date().isoformat(),
        "from_year": args.from_year,
        "per_area": args.per_area,
        "areas_file": None if args.areas else str(args.areas_file),
        "areas": results,
    }
    root = args.out / f"{datetime.now(UTC):%Y%m%d}-ideation-{run_slug(areas)}"
    root.mkdir(parents=True, exist_ok=True)
    (root / "landscape.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (root / "landscape.md").write_text(render_markdown(payload), encoding="utf-8")

    degraded = sum(1 for record in results if record["errors"])
    logger.info(
        "%d areas scanned (%d degraded) -> %s", len(results), degraded, root / "landscape.md"
    )
    print(root)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
