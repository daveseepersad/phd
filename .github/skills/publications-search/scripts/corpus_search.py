# /// script
# requires-python = ">=3.12"
# ///
"""Search the extracted full-text corpus with page-anchored BM25 ranking.

Every hit carries the paper stem and the exact page from the [[page N]]
markers, so evidence found here can be cited without re-opening the PDF.
`--quote` verifies a quotation instead: exact substring first, then a
normalized fallback that forgives PDF extraction artifacts (line-break
hyphenation, dropped or collapsed spaces, curly quotes) — the anti-fabrication
check the synthesis rules require before any quote enters review.md.
"""
from __future__ import annotations

import argparse
import json
import logging
import math
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from itertools import pairwise
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _common import tokenize

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

PAGE_MARKER = re.compile(r"\[\[page (\d+)\]\]")
# Standard Okapi constants; the corpus is small enough that tuning them per
# run would just overfit to one paper's length distribution.
BM25_K1 = 1.5
BM25_B = 0.75
SNIPPET_RADIUS = 40
CLUSTER_WINDOW = 30

CURLY_QUOTES = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "‚": "'", "„": '"'})


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Run folder containing text/.")
    parser.add_argument("query", nargs="?", default=None, help="Search terms (BM25 mode).")
    parser.add_argument("--top", type=int, default=10, help="Hits to print (default 10).")
    parser.add_argument(
        "--decision",
        default=None,
        help="Comma-separated screening decisions to search, e.g. core,supporting.",
    )
    parser.add_argument(
        "--all-pages",
        action="store_true",
        help="Rank every matching page instead of only each paper's best page.",
    )
    parser.add_argument(
        "--expect-page",
        type=int,
        default=None,
        help=(
            "Assert the page a document cites for this quotation. Without it a "
            "verbatim quote passes while carrying the wrong page, which is how a "
            "bad page citation reaches a submitted document."
        ),
    )
    parser.add_argument(
        "--quote",
        default=None,
        help="Verify this passage exists in the corpus instead of searching.",
    )
    return parser


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


@dataclass
class PageUnit:
    stem: str
    page: int
    body: str
    tokens: list[str]


def load_pages(run_root: Path) -> list[PageUnit]:
    pages: list[PageUnit] = []
    text_dir = run_root / "text"
    for path in sorted(text_dir.glob("*.txt")):
        text = path.read_text(encoding="utf-8")
        parts = PAGE_MARKER.split(text)
        # split() yields [preamble, n1, body1, n2, body2, ...].
        for number, body in zip(parts[1::2], parts[2::2], strict=True):
            pages.append(PageUnit(path.stem, int(number), body, tokenize(body)))
    return pages


def load_context(run_root: Path) -> tuple[dict[str, str], dict[str, dict[str, Any]]]:
    """Map text-file stem -> title, and normalized title -> decision/concepts."""
    stem_to_title: dict[str, str] = {}
    manifest_path = run_root / "manifest.json"
    if manifest_path.is_file():
        for record in json.loads(manifest_path.read_text(encoding="utf-8")):
            if record.get("text_file"):
                stem_to_title[Path(record["text_file"]).stem] = record["title"]

    info: dict[str, dict[str, Any]] = {}
    screening_path = run_root / "screening.json"
    if screening_path.is_file():
        payload = json.loads(screening_path.read_text(encoding="utf-8"))
        for record in payload.get("records", []):
            info[normalized_title(record["title"])] = {
                "decision": record.get("decision"),
                "concepts": record.get("concepts", []),
            }
    ledger_path = run_root / "evidence-ledger.json"
    if ledger_path.is_file():
        payload = json.loads(ledger_path.read_text(encoding="utf-8"))
        for record in payload.get("records", []):
            entry = info.setdefault(normalized_title(record["title"]), {"decision": None})
            # Ledger concepts come from full-text reading and supersede the
            # coarser abstract-screening concepts.
            if record.get("concepts"):
                entry["concepts"] = record["concepts"]
    return stem_to_title, info


def paper_context(stem: str, stem_to_title: dict[str, str], info: dict[str, dict[str, Any]]) -> dict[str, Any]:
    title = stem_to_title.get(stem)
    if title is None:
        return {"title": None, "decision": None, "concepts": []}
    entry = info.get(normalized_title(title), {})
    return {
        "title": title,
        "decision": entry.get("decision"),
        "concepts": entry.get("concepts", []),
    }


def bm25_scores(pages: list[PageUnit], terms: list[str]) -> list[float]:
    doc_count = len(pages)
    avgdl = (sum(len(page.tokens) for page in pages) / doc_count if doc_count else 1.0) or 1.0
    term_set = set(terms)
    df = Counter(term for page in pages for term in set(page.tokens) if term in term_set)
    idf = {
        term: math.log((doc_count - df[term] + 0.5) / (df[term] + 0.5) + 1.0)
        for term in terms
    }
    scores: list[float] = []
    for page in pages:
        tf = Counter(page.tokens)
        length_norm = BM25_K1 * (1 - BM25_B + BM25_B * len(page.tokens) / avgdl)
        scores.append(
            sum(
                idf[term] * tf[term] * (BM25_K1 + 1) / (tf[term] + length_norm)
                for term in terms
                if tf[term]
            )
        )
    return scores


def snippet(body: str, terms: list[str]) -> str:
    """~40 words each side of the densest cluster of query terms."""
    words = body.split()
    if not words:
        return ""
    term_set = set(terms)

    def is_hit(word: str) -> bool:
        norm = re.sub(r"[^a-z0-9]", "", word.lower())
        return any(norm == term or norm.startswith(term) for term in term_set)

    hits = [i for i, word in enumerate(words) if is_hit(word)]
    if not hits:
        center = 0
    else:
        best_start, best_count = hits[0], 1
        for anchor in hits:
            in_window = [i for i in hits if anchor <= i < anchor + CLUSTER_WINDOW]
            if len(in_window) > best_count:
                best_start, best_count = anchor, len(in_window)
        window = [i for i in hits if best_start <= i < best_start + CLUSTER_WINDOW]
        center = (window[0] + window[-1]) // 2
    start = max(center - SNIPPET_RADIUS, 0)
    end = min(center + SNIPPET_RADIUS, len(words))
    prefix = "… " if start > 0 else ""
    suffix = " …" if end < len(words) else ""
    return prefix + " ".join(words[start:end]) + suffix


def search(run_root: Path, query: str, top: int, decisions: set[str] | None, all_pages: bool) -> int:
    pages = load_pages(run_root)
    if not pages:
        logger.error("No page-marked text under %s; run extract.py first.", run_root / "text")
        return EXIT_ERROR
    stem_to_title, info = load_context(run_root)
    if decisions:
        before = {page.stem for page in pages}
        pages = [
            page
            for page in pages
            if paper_context(page.stem, stem_to_title, info)["decision"] in decisions
        ]
        dropped = before - {page.stem for page in pages}
        if dropped:
            logger.info("Decision filter %s excluded %d papers.", sorted(decisions), len(dropped))
        if not pages:
            logger.error("No pages left after the decision filter.")
            return EXIT_ERROR

    terms = tokenize(query)
    if not terms:
        logger.error("Query reduced to stopwords only; nothing to search.")
        return EXIT_ERROR
    scores = bm25_scores(pages, terms)
    ranked = sorted(
        (pair for pair in zip(scores, pages, strict=True) if pair[0] > 0),
        key=lambda pair: pair[0],
        reverse=True,
    )
    if not all_pages:
        # One hit per paper: its best page.
        seen: set[str] = set()
        ranked = [pair for pair in ranked if not (pair[1].stem in seen or seen.add(pair[1].stem))]

    if not ranked:
        logger.info("No pages match %r.", query)
        return EXIT_SUCCESS
    print(f"{min(top, len(ranked))} of {len(ranked)} matching pages for: {query}\n")
    for position, (score, page) in enumerate(ranked[:top], start=1):
        context = paper_context(page.stem, stem_to_title, info)
        decision = context["decision"] or "?"
        print(f"{position:2d}. {page.stem}  p.{page.page}  score={score:.2f}  [{decision}]")
        if context["concepts"]:
            print(f"    concepts: {', '.join(context['concepts'][:8])}")
        print(f"    {snippet(page.body, terms)}\n")
    return EXIT_SUCCESS


def normalize_for_quote(text: str) -> str:
    """Neutralize the PDF artifacts that break exact substring matching."""
    text = unicodedata.normalize("NFKC", text).translate(CURLY_QUOTES)
    text = text.replace("­", "")  # soft hyphen
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)
    # Removing all whitespace also forgives the dropped/joined spaces common
    # in two-column extraction ("systemsenable").
    return re.sub(r"\s+", "", text).casefold()


def verify_quote(
    run_root: Path, quote: str, decisions: set[str] | None, expect_page: int | None = None
) -> int:
    pages = load_pages(run_root)
    if not pages:
        logger.error("No page-marked text under %s; run extract.py first.", run_root / "text")
        return EXIT_ERROR
    stem_to_title, info = load_context(run_root)
    # Quote verification always scans every extracted page: filtering first
    # would let --decision turn "present, but in an excluded paper" into a
    # false "not found" verdict. The filter only annotates the result below.
    needle_norm = normalize_for_quote(quote)
    if not needle_norm:
        logger.error("Quote is empty after normalization.")
        return EXIT_ERROR

    matches: list[tuple[str, int, str]] = []
    by_stem: dict[str, list[PageUnit]] = {}
    for page in pages:
        by_stem.setdefault(page.stem, []).append(page)
    for stem, stem_pages in by_stem.items():
        stem_pages.sort(key=lambda page: page.page)
        for page in stem_pages:
            if quote in page.body:
                matches.append((stem, page.page, "exact"))
            elif needle_norm in normalize_for_quote(page.body):
                matches.append((stem, page.page, "normalized"))
        # A quotation can straddle a page break; scan adjacent pairs and
        # attribute the match to the page where it starts.
        for first, second in pairwise(stem_pages):
            if second.page != first.page + 1:
                continue
            joined = f"{first.body}\n{second.body}"
            already = {(stem, first.page), (stem, second.page)}
            if already & {(m[0], m[1]) for m in matches}:
                continue
            if quote in joined:
                matches.append((stem, first.page, "exact (spans page break)"))
            elif needle_norm in normalize_for_quote(joined):
                matches.append((stem, first.page, "normalized (spans page break)"))

    shown = quote if len(quote) <= 80 else quote[:77] + "..."
    if not matches:
        print(f'NOT FOUND: "{shown}"')
        print("Do not use this quotation: it could not be located in any extracted text.")
        return EXIT_ERROR
    print(f'FOUND ({len(matches)} location{"s" if len(matches) > 1 else ""}): "{shown}"\n')
    for stem, page_number, kind in matches:
        context = paper_context(stem, stem_to_title, info)
        decision = context["decision"] or "?"
        print(f"  {stem}  p.{page_number}  match={kind}  [{decision}]")
    if expect_page is not None and all(page != expect_page for _, page, _ in matches):
        found = ", ".join(f"p.{page}" for _, page, _ in matches)
        print(
            f"\nPAGE MISMATCH: cited as p.{expect_page} but the text is at {found}. "
            "Correct the citation before this quotation enters any document."
        )
        return EXIT_ERROR
    if decisions and not any(
        paper_context(stem, stem_to_title, info)["decision"] in decisions
        for stem, _, _ in matches
    ):
        print(
            f"\nEvery match is outside the requested --decision filter "
            f"({', '.join(sorted(decisions))}): the passage exists, but only in "
            "papers screened to other decisions."
        )
    if all("normalized" in kind for _, _, kind in matches):
        print("\nMatch is normalized, not exact: re-check wording against the PDF before citing.")
    return EXIT_SUCCESS


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    if not args.query and not args.quote:
        logger.error("Provide a query, or --quote to verify a passage.")
        return EXIT_ERROR
    decisions = (
        {value.strip() for value in args.decision.split(",") if value.strip()}
        if args.decision
        else None
    )
    try:
        if args.quote:
            return verify_quote(args.run_dir, args.quote, decisions, args.expect_page)
        return search(args.run_dir, args.query, args.top, decisions, args.all_pages)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        logger.error("%s", exc)
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())
