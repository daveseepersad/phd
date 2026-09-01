# /// script
# requires-python = ">=3.12"
# ///
"""Initialize and validate abstract screening for a literature-review run.

The top 20 remain marked as a quality baseline, but every candidate with an
abstract is screened. Apply writes selected.json from all core and supporting
decisions, so full-text retrieval is bounded by relevance rather than rank.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _common import Paper, save_papers

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

DECISIONS = {"pending", "core", "supporting", "context", "exclude", "unresolved"}


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="Create or refresh screening.json.")
    init.add_argument("run_dir", type=Path)
    init.add_argument("--baseline", type=int, default=20)

    merge = subparsers.add_parser("merge", help="Merge agent-reviewed decision chunks.")
    merge.add_argument("run_dir", type=Path)
    merge.add_argument("chunks", type=Path, nargs="+")

    apply = subparsers.add_parser("apply", help="Validate decisions and write selected.json.")
    apply.add_argument("run_dir", type=Path)
    apply.add_argument("--allow-pending", action="store_true")
    apply.add_argument("--include-context", action="store_true")
    apply.add_argument("--include-unresolved", action="store_true")
    return parser


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def load_candidates(run_dir: Path) -> tuple[dict[str, Any], list[Paper]]:
    path = run_dir / "candidates.json"
    if not path.is_file():
        raise FileNotFoundError(f"No candidates.json in {run_dir}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload, [Paper(**item) for item in payload.get("papers", [])]


def initialize(run_dir: Path, baseline: int) -> int:
    payload, papers = load_candidates(run_dir)
    screening_path = run_dir / "screening.json"
    previous: dict[str, dict[str, Any]] = {}
    previous_titles: dict[str, dict[str, Any]] = {}
    if screening_path.is_file():
        old = json.loads(screening_path.read_text(encoding="utf-8"))
        previous = {item["key"]: item for item in old.get("records", [])}
        previous_titles = {
            normalized_title(item["title"]): item for item in old.get("records", [])
        }

    records: list[dict[str, Any]] = []
    for rank, paper in enumerate(papers, start=1):
        prior = previous.get(paper.key()) or previous_titles.get(normalized_title(paper.title), {})
        prior_decision = prior.get("decision")
        if prior_decision == "unresolved" and paper.abstract:
            decision = "pending"
        else:
            decision = prior_decision or ("pending" if paper.abstract else "unresolved")
        records.append(
            {
                "rank": rank,
                "key": paper.key(),
                "baseline": rank <= baseline,
                "title": paper.title,
                "year": paper.year,
                "cited_by": paper.cited_by,
                "score": paper.score,
                "score_parts": paper.score_parts,
                "abstract": paper.abstract,
                "sources": paper.sources,
                "discovery_methods": paper.discovery_methods,
                "forward_citation_of": paper.forward_citation_of,
                "backward_reference_of": paper.backward_reference_of,
                "decision": decision,
                "rationale": prior.get("rationale", ""),
                "concepts": prior.get("concepts", []),
            }
        )

    screening = {
        "topic": payload["topic"],
        "generated": datetime.now(UTC).date().isoformat(),
        "baseline_size": baseline,
        "criteria": {
            "core": "Directly answers the research question and warrants full text.",
            "supporting": "Contributes a method, limitation, benchmark, or combinable solution.",
            "context": "Useful background that does not require full-text synthesis.",
            "exclude": "Keyword collision, wrong field, duplicate, or out of scope.",
            "unresolved": "No usable abstract; inspect the landing page before exclusion.",
        },
        "records": records,
    }
    screening_path.write_text(json.dumps(screening, indent=2, ensure_ascii=False), encoding="utf-8")
    initial_baseline = run_dir / "baseline.json"
    if not initial_baseline.exists():
        save_papers(
            initial_baseline,
            payload["topic"],
            papers[:baseline],
            baseline_size=baseline,
            snapshot="initial-keyword-search",
        )
    save_papers(
        run_dir / "baseline-current.json",
        payload["topic"],
        papers[:baseline],
        baseline_size=baseline,
        snapshot="current-expanded-corpus",
    )
    counts = Counter(item["decision"] for item in records)
    logger.info("%d records -> %s", len(records), screening_path)
    logger.info("baseline=%d decisions=%s", min(baseline, len(records)), dict(counts))
    return EXIT_SUCCESS


def apply_decisions(
    run_dir: Path,
    allow_pending: bool,
    include_context: bool,
    include_unresolved: bool,
) -> int:
    payload, papers = load_candidates(run_dir)
    screening_path = run_dir / "screening.json"
    if not screening_path.is_file():
        logger.error("No screening.json in %s; run screen.py init first.", run_dir)
        return EXIT_ERROR
    screening = json.loads(screening_path.read_text(encoding="utf-8"))
    records = screening.get("records", [])

    invalid = [item for item in records if item.get("decision") not in DECISIONS]
    if invalid:
        logger.error("%d records have invalid decisions.", len(invalid))
        return EXIT_ERROR
    pending = [item for item in records if item.get("decision") == "pending"]
    if pending and not allow_pending:
        logger.error(
            "%d abstracts remain pending. Screen the complete queue or pass --allow-pending.",
            len(pending),
        )
        return EXIT_ERROR

    include = {"core", "supporting"}
    if include_context:
        include.add("context")
    if include_unresolved:
        include.add("unresolved")
    priority = {"core": 0, "supporting": 1, "context": 2, "unresolved": 3}
    chosen_records = sorted(
        (item for item in records if item["decision"] in include),
        key=lambda item: (priority[item["decision"]], item["rank"]),
    )
    chosen_keys = [item["key"] for item in chosen_records]
    chosen_titles = {
        normalized_title(item["title"])
        for item in records
        if item["decision"] in include
    }
    by_key = {paper.key(): paper for paper in papers}
    selected: list[Paper] = []
    seen: set[str] = set()
    for key in chosen_keys:
        paper = by_key.get(key)
        if paper and paper.key() not in seen:
            selected.append(paper)
            seen.add(paper.key())
    for paper in papers:
        if normalized_title(paper.title) in chosen_titles and paper.key() not in seen:
            selected.append(paper)
            seen.add(paper.key())

    counts = Counter(item["decision"] for item in records)
    save_papers(
        run_dir / "selected.json",
        payload["topic"],
        selected,
        screening_counts=dict(counts),
        baseline_size=screening.get("baseline_size", 20),
        selection_decisions=sorted(include),
    )
    logger.info("%d selected from %d screened -> %s", len(selected), len(records), run_dir / "selected.json")
    return EXIT_SUCCESS


def merge_chunks(run_dir: Path, chunk_paths: list[Path]) -> int:
    screening_path = run_dir / "screening.json"
    if not screening_path.is_file():
        logger.error("No screening.json in %s; run screen.py init first.", run_dir)
        return EXIT_ERROR
    screening = json.loads(screening_path.read_text(encoding="utf-8"))
    records = screening.get("records", [])
    by_rank = {item["rank"]: item for item in records}
    reviewed: dict[int, dict[str, Any]] = {}
    valid_review_decisions = DECISIONS - {"pending"}

    for path in chunk_paths:
        chunk = json.loads(path.read_text(encoding="utf-8"))
        for item in chunk.get("records", []):
            rank = item.get("rank")
            decision = item.get("decision")
            if rank not in by_rank:
                logger.error("%s contains unknown candidate rank: %s", path, rank)
                return EXIT_ERROR
            if rank in reviewed:
                logger.error("Candidate rank %s appears in multiple chunks.", rank)
                return EXIT_ERROR
            if decision not in valid_review_decisions:
                logger.error("Rank %s has invalid reviewed decision: %s", rank, decision)
                return EXIT_ERROR
            if not isinstance(item.get("rationale"), str) or not item["rationale"].strip():
                logger.error("Rank %s has no screening rationale.", rank)
                return EXIT_ERROR
            if not isinstance(item.get("concepts"), list):
                logger.error("Rank %s concepts must be a list.", rank)
                return EXIT_ERROR
            reviewed[rank] = item

    for rank, item in reviewed.items():
        target = by_rank[rank]
        target["decision"] = item["decision"]
        target["rationale"] = item["rationale"].strip()
        target["concepts"] = sorted(set(item["concepts"]))

    screening_path.write_text(
        json.dumps(screening, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    counts = Counter(item["decision"] for item in records)
    logger.info("Merged %d reviewed abstracts from %d chunks.", len(reviewed), len(chunk_paths))
    logger.info("decisions=%s", dict(counts))
    return EXIT_SUCCESS


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        if args.command == "init":
            return initialize(args.run_dir, args.baseline)
        if args.command == "merge":
            return merge_chunks(args.run_dir, args.chunks)
        return apply_decisions(
            args.run_dir,
            args.allow_pending,
            args.include_context,
            args.include_unresolved,
        )
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        logger.error("%s", exc)
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())