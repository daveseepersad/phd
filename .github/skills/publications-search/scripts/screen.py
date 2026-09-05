# /// script
# requires-python = ">=3.12"
# ///
"""Initialize and validate abstract screening for a literature-review run.

The top 20 remain marked as a quality baseline, but every candidate with an
abstract is screened. Apply writes selected.json from all core and supporting
decisions, so full-text retrieval is bounded by relevance rather than rank.
Sample and kappa support the AI-assist disclosure: a decision-blind stratified
sample for independent human screening, then Cohen's kappa against the agent.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
import random
import re
import sys
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _common import Paper, save_papers, write_json_atomic

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

DECISIONS = {"pending", "core", "supporting", "context", "exclude", "unresolved"}
# Abstract judgments a blind human validator can reproduce; pending and
# unresolved are queue states, not screening decisions.
SCREENED_DECISIONS = ("core", "supporting", "context", "exclude")


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

    sample = subparsers.add_parser("sample", help="Draw a decision-blind human-validation sample.")
    sample.add_argument("run_dir", type=Path)
    sample.add_argument("--fraction", type=float, default=0.15)
    sample.add_argument("--seed", type=int, default=0)

    kappa = subparsers.add_parser("kappa", help="Score the filled human sample with Cohen's kappa.")
    kappa.add_argument("run_dir", type=Path)
    return parser


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def load_candidates(run_dir: Path) -> tuple[dict[str, Any], list[Paper]]:
    path = run_dir / "candidates.json"
    if not path.is_file():
        raise FileNotFoundError(f"No candidates.json in {run_dir}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload, [Paper.from_dict(item) for item in payload.get("papers", [])]


def append_history(run_dir: Path, events: list[dict[str, Any]]) -> None:
    """Archive superseded decision states; nothing is ever silently dropped."""
    if not events:
        return
    path = run_dir / "screening-history.json"
    history: dict[str, Any] = {"events": []}
    if path.is_file():
        history = json.loads(path.read_text(encoding="utf-8"))
    history.setdefault("events", []).extend(events)
    write_json_atomic(path, history)
    logger.info("%d superseded decision(s) archived -> %s", len(events), path)


def initialize(run_dir: Path, baseline: int) -> int:
    payload, papers = load_candidates(run_dir)
    screening_path = run_dir / "screening.json"
    prior_screening: dict[str, Any] = {}
    if screening_path.is_file():
        prior_screening = json.loads(screening_path.read_text(encoding="utf-8"))
    prior_records: list[dict[str, Any]] = prior_screening.get("records", [])
    previous = {item["key"]: item for item in prior_records}
    previous_titles = {normalized_title(item["title"]): item for item in prior_records}

    now = datetime.now(UTC).isoformat()
    history: list[dict[str, Any]] = []
    carried: set[int] = set()
    records: list[dict[str, Any]] = []
    for rank, paper in enumerate(papers, start=1):
        prior = previous.get(paper.key()) or previous_titles.get(normalized_title(paper.title)) or {}
        if prior:
            carried.add(id(prior))
        prior_decision = prior.get("decision")
        if prior_decision == "unresolved" and paper.abstract:
            # A recovered abstract reopens the record; the unresolved state is
            # archived rather than silently overwritten.
            decision, decided_at = "pending", now
            history.append({"when": now, "reason": "unresolved-superseded-by-recovered-abstract", "record": prior})
        elif prior_decision:
            # Carried decisions keep their original timestamp (null for
            # records screened before timestamps existed).
            decision, decided_at = prior_decision, prior.get("decided_at")
        else:
            decision = "pending" if paper.abstract else "unresolved"
            decided_at = now
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
                "decided_at": decided_at,
                "rationale": prior.get("rationale", ""),
                "concepts": prior.get("concepts", []),
            }
        )

    for prior in prior_records:
        if id(prior) not in carried:
            history.append({"when": now, "reason": "dropped-from-candidates", "record": prior})

    screening: dict[str, Any] = {
        "topic": payload["topic"],
        "generated": datetime.now(UTC).date().isoformat(),
        "baseline_size": baseline,
    }
    protocol_path = run_dir / "protocol.md"
    if protocol_path.is_file():
        # Bind the decisions to the exact protocol text they were made under.
        protocol_sha = hashlib.sha256(protocol_path.read_bytes()).hexdigest()
        prior_sha = prior_screening.get("protocol_sha256")
        sha_history = list(prior_screening.get("protocol_sha256_history", []))
        if prior_sha and prior_sha != protocol_sha:
            # Carried decisions were made under the old protocol text; the
            # change is archived, never silently re-stamped.
            history.append({"when": now, "reason": "protocol-hash-changed", "old": prior_sha, "new": protocol_sha})
            if prior_sha not in sha_history:
                sha_history.append(prior_sha)
            logger.warning("protocol.md changed since the last init (%s -> %s).", prior_sha[:12], protocol_sha[:12])
        screening["protocol_sha256"] = protocol_sha
        if sha_history:
            screening["protocol_sha256_history"] = sha_history
    screening["criteria"] = {
        "core": "Directly answers the research question and warrants full text.",
        "supporting": "Contributes a method, limitation, benchmark, or combinable solution.",
        "context": "Useful background that does not require full-text synthesis.",
        "exclude": "Keyword collision, wrong field, duplicate, or out of scope.",
        "unresolved": "No usable abstract; inspect the landing page before exclusion.",
    }
    screening["records"] = records
    # History is archived before screening.json is replaced, so a failed
    # history write can never destroy the superseded decisions.
    append_history(run_dir, history)
    write_json_atomic(screening_path, screening)
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
    by_key = {item["key"]: item for item in records}
    by_title = {normalized_title(item["title"]): item for item in records}
    duplicate_keys = {key for key, count in Counter(item["key"] for item in records).items() if count > 1}
    # Keyed by id() of the bound screening record so two chunk rows can never
    # target one record, whichever lookup path found it.
    reviewed: dict[int, tuple[dict[str, Any], dict[str, Any]]] = {}
    valid_review_decisions = DECISIONS - {"pending"}

    for path in chunk_paths:
        chunk = json.loads(path.read_text(encoding="utf-8"))
        for item in chunk.get("records", []):
            key, title = item.get("key"), item.get("title")
            if not key:
                logger.error(
                    "%s: record lacks a key (rank=%s); positional binding is not accepted.",
                    path,
                    item.get("rank"),
                )
                return EXIT_ERROR
            target = by_key.get(key)
            if target is not None and not title:
                # A unique key match (e.g. a DOI) binds on its own; the title
                # cross-check is unavailable here, not failed.
                if key in duplicate_keys:
                    logger.error(
                        "%s: key %s is not unique in screening.json; a title is required to disambiguate.",
                        path, key,
                    )
                    return EXIT_ERROR
                logger.warning('%s: record %s carries no title; accepted on unique key match.', path, key)
            elif target is not None and normalized_title(title) != normalized_title(target["title"]):
                logger.error(
                    '%s: key %s title mismatch: chunk "%s" vs screening "%s".',
                    path, key, title, target["title"],
                )
                return EXIT_ERROR
            if target is None:
                if not title:
                    logger.error("%s: key %s matches no screening record and carries no title.", path, key)
                    return EXIT_ERROR
                # A DOI backfilled after chunking turns a title-derived key
                # into a DOI key; the normalized title still identifies it.
                target = by_title.get(normalized_title(title))
            if target is None:
                logger.error('%s: no screening record matches key=%s title="%s".', path, key, title)
                return EXIT_ERROR
            # Rank is redundant when present, but a stale rank means the chunk
            # was written against a different ordering: fail, never guess.
            if item.get("rank") is not None and item["rank"] != target["rank"]:
                logger.error(
                    "%s: rank cross-check failed for %s: chunk says %s, screening says %s.",
                    path, target["key"], item["rank"], target["rank"],
                )
                return EXIT_ERROR
            if id(target) in reviewed:
                logger.error("Record %s appears in multiple chunks.", target["key"])
                return EXIT_ERROR
            if item.get("decision") not in valid_review_decisions:
                logger.error("%s has invalid reviewed decision: %s", target["key"], item.get("decision"))
                return EXIT_ERROR
            if not isinstance(item.get("rationale"), str) or not item["rationale"].strip():
                logger.error("%s has no screening rationale.", target["key"])
                return EXIT_ERROR
            if not isinstance(item.get("concepts"), list):
                logger.error(
                    '%s: "concepts" must be a list of short topic labels (may be empty). '
                    "Chunk records require key, title, decision, rationale, and concepts.",
                    target["key"],
                )
                return EXIT_ERROR
            reviewed[id(target)] = (target, item)

    now = datetime.now(UTC).isoformat()
    history: list[dict[str, Any]] = []
    for target, item in reviewed.values():
        if target["decision"] != "pending":
            history.append({"when": now, "reason": "merge-overwrote-decision", "record": dict(target)})
        target["decision"] = item["decision"]
        target["rationale"] = item["rationale"].strip()
        target["concepts"] = sorted(set(item["concepts"]))
        target["decided_at"] = now

    # History is archived before screening.json is replaced, so a failed
    # history write can never destroy the superseded decisions.
    append_history(run_dir, history)
    write_json_atomic(screening_path, screening)
    counts = Counter(item["decision"] for item in records)
    logger.info("Merged %d reviewed abstracts from %d chunks.", len(reviewed), len(chunk_paths))
    logger.info("decisions=%s", dict(counts))
    return EXIT_SUCCESS


def sample_records(run_dir: Path, fraction: float, seed: int) -> int:
    screening_path = run_dir / "screening.json"
    if not screening_path.is_file():
        logger.error("No screening.json in %s; run screen.py init first.", run_dir)
        return EXIT_ERROR
    if not 0.0 < fraction <= 1.0:
        logger.error("--fraction must be in (0, 1].")
        return EXIT_ERROR
    screening = json.loads(screening_path.read_text(encoding="utf-8"))
    screened = [
        item for item in screening.get("records", []) if item.get("decision") in SCREENED_DECISIONS
    ]
    if not screened:
        logger.error("No screened decisions to sample; merge decisions first.")
        return EXIT_ERROR

    rng = random.Random(seed)
    chosen: list[dict[str, Any]] = []
    for decision in SCREENED_DECISIONS:
        # Strata are sorted by key so the draw depends only on --seed, not on
        # the rank order screening.json happened to be written in.
        stratum = sorted(
            (item for item in screened if item["decision"] == decision),
            key=lambda item: item["key"],
        )
        if not stratum:
            continue
        take = min(len(stratum), max(1, round(fraction * len(stratum))))
        chosen.extend(rng.sample(stratum, take))
    # Shuffled and stripped of the agent's decision so the human screens blind.
    rng.shuffle(chosen)
    payload = {
        "generated": datetime.now(UTC).isoformat(),
        "fraction": fraction,
        "seed": seed,
        "decision_categories": list(SCREENED_DECISIONS),
        "n": len(chosen),
        "entries": [
            {
                "key": item["key"],
                "title": item["title"],
                "abstract": item["abstract"],
                "human_decision": "",
                "note": "",
            }
            for item in chosen
        ],
    }
    sample_path = run_dir / "human-validation-sample.json"
    write_json_atomic(sample_path, payload)
    logger.info(
        "%d of %d screened records sampled (fraction=%.2f seed=%d) -> %s",
        len(chosen), len(screened), fraction, seed, sample_path,
    )
    return EXIT_SUCCESS


def kappa_report(run_dir: Path) -> int:
    screening_path = run_dir / "screening.json"
    sample_path = run_dir / "human-validation-sample.json"
    if not screening_path.is_file() or not sample_path.is_file():
        logger.error("Need screening.json and human-validation-sample.json in %s.", run_dir)
        return EXIT_ERROR
    screening = json.loads(screening_path.read_text(encoding="utf-8"))
    sample = json.loads(sample_path.read_text(encoding="utf-8"))
    records = screening.get("records", [])
    by_key = {item["key"]: item for item in records}
    by_title = {normalized_title(item["title"]): item for item in records}

    pairs: list[tuple[str, str, dict[str, Any]]] = []
    unmatched: list[str] = []
    blank = 0
    for entry in sample.get("entries", []):
        human = (entry.get("human_decision") or "").strip().lower()
        if not human:
            blank += 1
            continue
        if human not in SCREENED_DECISIONS:
            logger.error(
                'Invalid human_decision "%s" for %s; use one of %s.',
                human, entry["key"], "/".join(SCREENED_DECISIONS),
            )
            return EXIT_ERROR
        record = by_key.get(entry["key"]) or by_title.get(normalized_title(entry["title"]))
        if record is None:
            # A re-init between sample and kappa can drop records; count them
            # rather than silently shrinking n.
            unmatched.append(entry["key"])
            logger.warning("Sample entry no longer in screening.json: %s", entry["key"])
            continue
        pairs.append((human, record["decision"], entry))
    if not pairs:
        logger.error("No filled human decisions in %s.", sample_path)
        return EXIT_ERROR

    n = len(pairs)
    categories = sorted({human for human, _, _ in pairs} | {ai for _, ai, _ in pairs})
    confusion = {human: dict.fromkeys(categories, 0) for human in categories}
    human_marginal: Counter[str] = Counter()
    ai_marginal: Counter[str] = Counter()
    agree = 0
    for human, ai, _ in pairs:
        confusion[human][ai] += 1
        human_marginal[human] += 1
        ai_marginal[ai] += 1
        if human == ai:
            agree += 1
    po = agree / n
    pe = sum(human_marginal[c] * ai_marginal[c] for c in categories) / (n * n)
    # pe == 1 only when both raters used a single identical category.
    kappa = 1.0 if pe == 1.0 else (po - pe) / (1 - pe)

    disagreements = [
        {"key": entry["key"], "title": entry["title"], "human": human, "ai": ai}
        for human, ai, entry in pairs
        if human != ai
    ]
    report = {
        "generated": datetime.now(UTC).isoformat(),
        "kappa": round(kappa, 4),
        "n": n,
        "observed_agreement": round(po, 4),
        "expected_agreement": round(pe, 4),
        "per_category_confusion": confusion,
        "disagreements": disagreements,
        "blank_entries": blank,
        "unmatched_entries": unmatched,
    }
    report_path = run_dir / "human-validation-report.json"
    write_json_atomic(report_path, report)
    logger.info(
        "Cohen's kappa = %.3f over %d records (%d disagreements) -> %s",
        kappa, n, len(disagreements), report_path,
    )
    return EXIT_SUCCESS


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        if args.command == "init":
            return initialize(args.run_dir, args.baseline)
        if args.command == "merge":
            return merge_chunks(args.run_dir, args.chunks)
        if args.command == "sample":
            return sample_records(args.run_dir, args.fraction, args.seed)
        if args.command == "kappa":
            return kappa_report(args.run_dir)
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
