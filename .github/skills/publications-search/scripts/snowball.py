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
import os
import re
import sys
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx

sys.path.insert(0, str(Path(__file__).parent))
from _common import (
    RANKING_PROFILES,
    Paper,
    merge,
    paper_from_openalex,
    save_papers,
    score_papers,
    tokenize,
)

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

OPENALEX_API = "https://api.openalex.org"


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
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


class OpenAlexClient:
    """Small polite-pool client for the OpenAlex endpoints used here."""

    def __init__(self) -> None:
        headers = {"User-Agent": "publications-search/0.2"}
        self.client = httpx.Client(base_url=OPENALEX_API, headers=headers, timeout=60.0)
        self.mailto = os.getenv("CONTACT_EMAIL", "").strip()

    def close(self) -> None:
        self.client.close()

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        request_params = dict(params or {})
        if self.mailto:
            request_params["mailto"] = self.mailto
        response = self.client.get(path, params=request_params)
        response.raise_for_status()
        return response.json()

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
    ) -> list[dict[str, Any]]:
        filters = [f"cites:{openalex_id}"]
        if from_year:
            filters.append(f"from_publication_date:{from_year}-01-01")
        works: list[dict[str, Any]] = []
        cursor = "*"
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
            page = payload.get("results", [])
            works.extend(page)
            cursor = (payload.get("meta") or {}).get("next_cursor")
            if not page or not cursor:
                break
        return works[:limit]


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


def anchors_from_screening(path: Path, papers: list[Paper], limit: int) -> list[Paper]:
    data = json.loads(path.read_text(encoding="utf-8"))
    keys = [
        item["key"]
        for item in data.get("records", [])
        if item.get("decision") == "core"
    ][:limit]
    by_key = {paper.key(): paper for paper in papers}
    return [by_key[key] for key in keys if key in by_key]


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
    papers = [Paper(**item) for item in payload.get("papers", [])]
    anchors: list[Paper] = []
    for spec in args.anchor:
        paper = resolve_candidate(spec, papers)
        if paper is None:
            logger.error("Anchor did not match a candidate: %s", spec)
            return EXIT_ERROR
        anchors.append(paper)
    if args.anchors_from:
        anchors.extend(anchors_from_screening(args.anchors_from, papers, args.anchor_count))
    anchors = merge(anchors)[: args.anchor_count]
    if not anchors:
        logger.error("Choose anchors with --anchor or --anchors-from; none were resolved.")
        return EXIT_ERROR

    client = OpenAlexClient()
    discovered: list[Paper] = []
    edges: list[dict[str, str]] = []
    anchor_records: list[dict[str, Any]] = []
    try:
        for anchor in anchors:
            work = client.resolve(anchor)
            if work is None:
                logger.warning("OpenAlex could not resolve anchor: %s", anchor.title)
                continue
            anchor_id = work["id"].rsplit("/", 1)[-1]
            anchor.openalex_id = anchor_id
            anchor.discovery_methods = sorted(set(anchor.discovery_methods) | {"anchor"})
            anchor_records.append(
                {
                    "openalex_id": anchor_id,
                    "doi": anchor.doi,
                    "title": anchor.title,
                }
            )

            references = client.works_by_ids(
                work.get("referenced_works", []), args.backward_limit
            )
            for item in references:
                paper = paper_from_openalex(item, "snowball-backward", 1)
                paper.backward_reference_of = [anchor_id]
                discovered.append(paper)
                edges.append(
                    {
                        "anchor": anchor_id,
                        "work": paper.openalex_id or paper.key(),
                        "direction": "backward-reference",
                    }
                )

            forward = client.citing_works(
                anchor_id, args.forward_limit, args.forward_from_year
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
    finally:
        client.close()

    profile_name, weights = ranking_metadata(payload)
    expanded = merge(papers, discovered)
    ranked = score_papers(
        expanded,
        tokenize(payload["topic"]),
        weights["relevance"],
        weights["citations"],
        weights["recency"],
        weights["half_life_years"],
    )
    prior_runs = payload.get("snowball_runs", 0)
    save_papers(
        candidate_path,
        payload["topic"],
        ranked,
        sources=payload.get("sources", []),
        ranking_profile=profile_name,
        weights=weights,
        snowball_runs=prior_runs + 1,
    )

    graph_path = args.run_dir / "snowball.json"
    round_path = args.run_dir / f"snowball-round-{prior_runs + 1:02d}.json"
    graph = {
        "generated": datetime.now(UTC).date().isoformat(),
        "round": prior_runs + 1,
        "anchors": anchor_records,
        "forward_from_year": args.forward_from_year,
        "limits": {
            "backward_per_anchor": args.backward_limit,
            "forward_per_anchor": args.forward_limit,
        },
        "edges": edges,
        "unique_discovered": len(merge(discovered)),
        "corpus_before": len(papers),
        "corpus_after": len(ranked),
    }
    graph_text = json.dumps(graph, indent=2, ensure_ascii=False)
    graph_path.write_text(graph_text, encoding="utf-8")
    round_path.write_text(graph_text, encoding="utf-8")
    logger.info(
        "%d unique candidates (%+d) -> %s",
        len(ranked),
        len(ranked) - len(papers),
        candidate_path,
    )
    logger.info("Citation graph -> %s", round_path)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())