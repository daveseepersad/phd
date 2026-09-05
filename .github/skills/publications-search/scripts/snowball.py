# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx>=0.27"]
# ///
"""Expand a literature search through backward and forward citation snowballing.

Anchors can be candidate ranks, DOIs, OpenAlex IDs, URLs, or exact titles. The
command adds cited references and citing works to candidates.json, records every
discovery edge in snowball.json, and re-ranks the expanded corpus using the
search run's original ranking weights.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import time
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx

sys.path.insert(0, str(Path(__file__).parent))
from _common import (
    RANKING_PROFILES,
    Paper,
    contact_email,
    merge,
    openalex_headers,
    paper_from_openalex,
    save_papers,
    score_papers,
    tokenize,
    write_json_atomic,
)

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

OPENALEX_API = "https://api.openalex.org"
RETRY_ATTEMPTS = 3
RETRY_BASE_DELAY_S = 2.0


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Run folder containing candidates.json.")
    parser.add_argument(
        "--anchor",
        action="append",
        default=[],
        help="Candidate rank, DOI, OpenAlex ID, URL, or exact title. Repeatable.",
    )
    parser.add_argument(
        "--anchors-from",
        type=Path,
        default=None,
        help="Screening JSON whose core papers should be used as anchors.",
    )
    parser.add_argument("--anchor-count", type=int, default=4)
    parser.add_argument("--forward-limit", type=int, default=100)
    parser.add_argument("--backward-limit", type=int, default=100)
    parser.add_argument(
        "--forward-from-year",
        type=int,
        default=None,
        help="Optional earliest year for forward citations; references remain unrestricted.",
    )
    parser.add_argument(
        "--backward-from-year",
        type=int,
        default=None,
        help=(
            "Optional earliest year for backward references. Deep reference tails are "
            "mostly pre-LLM textbooks and proceedings front matter; set this to the "
            "protocol's earliest eligible year to keep them out of the screening queue."
        ),
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


class OpenAlexClient:
    """Small polite-pool client for the OpenAlex endpoints used here."""

    def __init__(self) -> None:
        self.client = httpx.Client(
            base_url=OPENALEX_API, headers=openalex_headers(), timeout=60.0
        )
        self.mailto = contact_email()

    def close(self) -> None:
        self.client.close()

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        request_params = dict(params or {})
        if self.mailto:
            request_params["mailto"] = self.mailto
        # OpenAlex intermittently returns 429/5xx under load; without retries a
        # single transient failure used to discard every anchor's fetched data.
        for attempt in range(1, RETRY_ATTEMPTS + 1):
            try:
                response = self.client.get(path, params=request_params)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as exc:
                status = getattr(getattr(exc, "response", None), "status_code", None)
                retryable = status is None or status == 429 or status >= 500
                if not retryable or attempt == RETRY_ATTEMPTS:
                    raise
                delay = RETRY_BASE_DELAY_S * 2 ** (attempt - 1)
                logger.warning(
                    "OpenAlex %s attempt %d/%d failed (%s); retrying in %.0fs",
                    path, attempt, RETRY_ATTEMPTS, exc, delay,
                )
                time.sleep(delay)
        raise AssertionError("unreachable")  # loop always returns or raises

    def resolve(self, paper: Paper) -> dict[str, Any] | None:
        identifiers: list[str] = []
        if paper.openalex_id:
            identifiers.append(paper.openalex_id)
        if paper.doi:
            identifiers.append(f"doi:{paper.doi}")
        source = f"{paper.url or ''} {paper.pdf_url or ''}"
        arxiv = re.search(r"arxiv\.org/(?:abs|pdf)/([\w.]+)", source)
        if arxiv:
            identifiers.append(f"arxiv:{arxiv.group(1)}")

        for identifier in identifiers:
            try:
                return self.get(f"/works/{identifier}")
            except httpx.HTTPStatusError as exc:
                if exc.response.status_code != 404:
                    raise

        payload = self.get("/works", {"search": paper.title, "per-page": 5})
        for hit in payload.get("results", []):
            if titles_match(paper.title, hit.get("display_name") or ""):
                return hit
        return None

    def works_by_ids(self, ids: Iterable[str], limit: int) -> list[dict[str, Any]]:
        clean = [identifier.rsplit("/", 1)[-1] for identifier in ids][:limit]
        works: list[dict[str, Any]] = []
        for offset in range(0, len(clean), 50):
            batch = clean[offset : offset + 50]
            if not batch:
                continue
            payload = self.get(
                "/works",
                {
                    "filter": "openalex_id:" + "|".join(batch),
                    "per-page": len(batch),
                },
            )
            works.extend(payload.get("results", []))
        return works[:limit]

    def citing_works(
        self, openalex_id: str, limit: int, from_year: int | None
    ) -> tuple[list[dict[str, Any]], bool]:
        """Return citing works plus whether the limit cut off known results.

        Truncation must be reported, not silent: capping forward citations is a
        deviation from Wohlin closure that the round file has to make auditable.
        """
        filters = [f"cites:{openalex_id}"]
        if from_year:
            filters.append(f"from_publication_date:{from_year}-01-01")
        works: list[dict[str, Any]] = []
        cursor = "*"
        total: int | None = None
        while len(works) < limit:
            page_size = min(200, limit - len(works))
            payload = self.get(
                "/works",
                {
                    "filter": ",".join(filters),
                    "per-page": page_size,
                    "cursor": cursor,
                },
            )
            if total is None:
                total = (payload.get("meta") or {}).get("count")
            page = payload.get("results", [])
            works.extend(page)
            cursor = (payload.get("meta") or {}).get("next_cursor")
            if not page or not cursor:
                break
        return works[:limit], total is not None and total > limit


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def titles_match(left: str, right: str) -> bool:
    left_tokens = set(tokenize(left))
    right_tokens = set(tokenize(right))
    if not left_tokens or not right_tokens:
        return False
    return len(left_tokens & right_tokens) / min(len(left_tokens), len(right_tokens)) >= 0.8


def resolve_candidate(spec: str, papers: list[Paper]) -> Paper | None:
    spec = spec.strip()
    if spec.isdigit():
        rank = int(spec)
        return papers[rank - 1] if 1 <= rank <= len(papers) else None

    bare_doi = spec.lower().removeprefix("https://doi.org/").removeprefix("doi:")
    for paper in papers:
        if paper.doi and paper.doi.lower() == bare_doi:
            return paper
        if paper.openalex_id and paper.openalex_id.lower() == spec.lower().rsplit("/", 1)[-1]:
            return paper
        if paper.url and paper.url == spec:
            return paper
        if normalized_title(paper.title) == normalized_title(spec):
            return paper
    return None


def used_anchor_keys(run_dir: Path) -> set[str]:
    """Anchors already expanded in earlier rounds, by OpenAlex ID, DOI, and title."""
    used: set[str] = set()
    for round_file in sorted(run_dir.glob("snowball-round-*.json")):
        try:
            data = json.loads(round_file.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for record in data.get("anchors", []):
            for field in ("openalex_id", "doi", "title"):
                value = record.get(field)
                if value:
                    used.add(str(value).rsplit("/", 1)[-1].lower())
    return used


def anchors_from_screening(
    path: Path, papers: list[Paper], limit: int, exclude: set[str] | None = None
) -> list[Paper]:
    """Pick unexpanded core papers.

    Without the exclusion set every round re-selects the same highest-ranked
    core papers, so round 2 onward discovers nothing.
    """
    exclude = exclude or set()
    data = json.loads(path.read_text(encoding="utf-8"))
    by_key = {paper.key(): paper for paper in papers}
    chosen: list[Paper] = []
    for item in data.get("records", []):
        if item.get("decision") != "core":
            continue
        paper = by_key.get(item["key"])
        if paper is None:
            continue
        identifiers = {
            str(value).rsplit("/", 1)[-1].lower()
            for value in (paper.openalex_id, paper.doi, paper.title)
            if value
        }
        if identifiers & exclude:
            continue
        chosen.append(paper)
        if len(chosen) >= limit:
            break
    return chosen


def ranking_metadata(payload: dict[str, Any]) -> tuple[str, dict[str, float]]:
    profile_name = payload.get("ranking_profile", "frontier")
    fallback = RANKING_PROFILES.get(profile_name, RANKING_PROFILES["frontier"])
    weights = payload.get("weights") or {
        "relevance": fallback.relevance,
        "citations": fallback.citations,
        "recency": fallback.recency,
        "half_life_years": fallback.half_life_years,
    }
    return profile_name, weights


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    candidate_path = args.run_dir / "candidates.json"
    if not candidate_path.is_file():
        logger.error("No candidates.json in %s", args.run_dir)
        return EXIT_ERROR

    payload = json.loads(candidate_path.read_text(encoding="utf-8"))
    papers = [Paper.from_dict(item) for item in payload.get("papers", [])]
    anchors: list[Paper] = []
    for spec in args.anchor:
        paper = resolve_candidate(spec, papers)
        if paper is None:
            logger.error("Anchor did not match a candidate: %s", spec)
            return EXIT_ERROR
        anchors.append(paper)
    if args.anchors_from:
        already = used_anchor_keys(args.run_dir)
        fresh = anchors_from_screening(args.anchors_from, papers, args.anchor_count, already)
        if already:
            logger.info("skipping %d anchor(s) expanded in earlier rounds", len(already))
        if not fresh and not anchors:
            logger.warning(
                "Every core paper has already been expanded; screen more abstracts or "
                "pass --anchor explicitly to re-expand one."
            )
        anchors.extend(fresh)
    anchors = merge(anchors)[: args.anchor_count]
    if not anchors:
        logger.error("Choose anchors with --anchor or --anchors-from; none were resolved.")
        return EXIT_ERROR

    client = OpenAlexClient()
    discovered: list[Paper] = []
    edges: list[dict[str, str]] = []
    anchor_records: list[dict[str, Any]] = []
    anchor_errors: list[dict[str, str]] = []
    skipped_backward = 0
    try:
        for anchor in anchors:
            # One dead anchor must not discard the expansion already fetched
            # for the others; record the failure and keep the partial round.
            try:
                work = client.resolve(anchor)
            except (httpx.HTTPError, ValueError) as exc:
                logger.warning("Anchor resolution failed for %s: %s", anchor.title[:64], exc)
                anchor_errors.append({"title": anchor.title, "error": f"resolve: {exc}"})
                continue
            if work is None:
                logger.warning("OpenAlex could not resolve anchor: %s", anchor.title)
                continue
            anchor_id = work["id"].rsplit("/", 1)[-1]
            anchor.openalex_id = anchor_id
            anchor.discovery_methods = sorted(set(anchor.discovery_methods) | {"anchor"})
            record = {
                "openalex_id": anchor_id,
                "doi": anchor.doi,
                "title": anchor.title,
                "truncated": False,
            }
            anchor_records.append(record)

            try:
                references = client.works_by_ids(
                    work.get("referenced_works", []), args.backward_limit
                )
                for item in references:
                    paper = paper_from_openalex(item, "snowball-backward", 1)
                    if args.backward_from_year and (paper.year or 0) < args.backward_from_year:
                        skipped_backward += 1
                        continue
                    paper.backward_reference_of = [anchor_id]
                    discovered.append(paper)
                    edges.append(
                        {
                            "anchor": anchor_id,
                            "work": paper.openalex_id or paper.key(),
                            "direction": "backward-reference",
                        }
                    )

                forward, truncated = client.citing_works(
                    anchor_id, args.forward_limit, args.forward_from_year
                )
                if truncated:
                    # Capped forward snowballing deviates from Wohlin closure;
                    # the flag keeps the deviation auditable per anchor.
                    record["truncated"] = True
                    logger.warning(
                        "Forward citations truncated at --forward-limit=%d for %s "
                        "(Wohlin deviation recorded in round file)",
                        args.forward_limit,
                        anchor.title[:64],
                    )
                for item in forward:
                    paper = paper_from_openalex(item, "snowball-forward", 1)
                    paper.forward_citation_of = [anchor_id]
                    discovered.append(paper)
                    edges.append(
                        {
                            "anchor": anchor_id,
                            "work": paper.openalex_id or paper.key(),
                            "direction": "forward-citation",
                        }
                    )
                logger.info(
                    "%s: %d references, %d forward citations",
                    anchor.title[:64],
                    len(references),
                    len(forward),
                )
            except (httpx.HTTPError, ValueError) as exc:
                record["error"] = str(exc)
                anchor_errors.append(
                    {"title": anchor.title, "openalex_id": anchor_id, "error": str(exc)}
                )
                logger.warning(
                    "Anchor expansion failed for %s: %s (keeping partial results)",
                    anchor.title[:64],
                    exc,
                )
    finally:
        client.close()

    if anchor_errors and not anchor_records and not discovered:
        logger.error("Every anchor failed before any expansion; nothing to save.")
        for failure in anchor_errors:
            logger.error("  %s: %s", failure["title"][:64], failure["error"])
        return EXIT_ERROR

    profile_name, weights = ranking_metadata(payload)
    expanded = merge(papers, discovered)
    scoring_meta: dict[str, Any] = {}
    ranked = score_papers(
        expanded,
        tokenize(payload["topic"]),
        weights["relevance"],
        weights["citations"],
        weights["recency"],
        weights["half_life_years"],
        scoring_meta=scoring_meta,
    )
    prior_runs = payload.get("snowball_runs", 0)
    save_papers(
        candidate_path,
        payload["topic"],
        ranked,
        sources=payload.get("sources", []),
        ranking_profile=profile_name,
        weights=weights,
        scoring=scoring_meta,
        snowball_runs=prior_runs + 1,
    )

    graph_path = args.run_dir / "snowball.json"
    round_path = args.run_dir / f"snowball-round-{prior_runs + 1:02d}.json"
    graph = {
        "generated": datetime.now(UTC).date().isoformat(),
        "round": prior_runs + 1,
        "anchors": anchor_records,
        "anchor_errors": anchor_errors,
        "forward_from_year": args.forward_from_year,
        "backward_from_year": args.backward_from_year,
        "backward_skipped_by_year": skipped_backward,
        "limits": {
            "backward_per_anchor": args.backward_limit,
            "forward_per_anchor": args.forward_limit,
        },
        "edges": edges,
        "unique_discovered": len(merge(discovered)),
        "corpus_before": len(papers),
        "corpus_after": len(ranked),
    }
    write_json_atomic(graph_path, graph)
    write_json_atomic(round_path, graph)
    logger.info(
        "%d unique candidates (%+d) -> %s",
        len(ranked),
        len(ranked) - len(papers),
        candidate_path,
    )
    logger.info("Citation graph -> %s", round_path)
    if anchor_errors:
        logger.warning(
            "%d of %d anchors failed; partial round saved, errors recorded in %s",
            len(anchor_errors),
            len(anchors),
            round_path,
        )
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())