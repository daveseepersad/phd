# /// script
# requires-python = ">=3.12"
# ///
"""Track concept saturation while reading a screened full-text corpus.

After each paper, record concepts and concepts not already present in earlier
papers. Saturation requires every core paper, a minimum number of full texts,
and a trailing window with no new concepts. The ledger makes the stopping rule
auditable without pretending that a fixed paper count equals completeness.
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

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

STATUSES = {"pending", "read", "unavailable", "excluded"}
EVIDENCE_DOMAINS = {
    "benchmarks-evaluation": ("benchmark", "metric", "evaluation", "ecological-validity"),
    "code-generation-repair": ("code", "repair", "bug", "synthesis", "refactor", "compile"),
    "communication": ("communication", "handoff", "dialog", "conversation", "information-loss"),
    "comparative-single-vs-multi": ("comparative", "single-vs", "baseline", "parity", "agentless", "dominance"),
    "cost-latency": ("cost", "latency", "token", "efficiency", "overhead", "api-call", "resource"),
    "debate-consensus": ("debate", "consensus", "discussion", "negotiation", "conflict"),
    "end-to-end-sdlc": ("end-to-end", "sdlc", "lifecycle", "deployment", "production-readiness"),
    "formal-verification": ("formal-verification", "proof"),
    "governance-accountability": ("governance", "accountability", "traceability", "provenance", "liability"),
    "human-in-loop": ("human", "lived-experience", "source-blinded"),
    "memory-context": ("memory", "context", "historical", "state-persistence"),
    "observability-fault-injection": ("observability", "fault-injection", "monitoring", "runtime-trace"),
    "orchestration": ("orchestration", "workflow", "pipeline", "supervisor", "stage-selection", "turn-taking"),
    "reliability-nondeterminism": ("reliability", "nondetermin", "variance", "hallucination", "failure", "error", "drift", "stagnation", "robustness", "inconsistency"),
    "requirements-design": ("requirement", "specification", "goal", "architecture-quality", "design"),
    "role-specialization": ("role", "special", "persona", "teacher-learner", "navigator-driver", "model-pairing"),
    "security": ("security", "vulnerab", "attack", "privacy", "access-control", "cve"),
    "topology": ("topology", "graph", "hierarchical", "centralized", "decentralized", "tree"),
    "transactions-concurrency": ("transaction", "concurrency", "state-consistency"),
    "verification-testing": ("verification", "validation", "test", "compiler", "audit", "critic", "judge", "contract"),
}


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="Create or refresh evidence-ledger.json.")
    init.add_argument("run_dir", type=Path)

    merge = subparsers.add_parser("merge", help="Merge full-text evidence chunks.")
    merge.add_argument("run_dir", type=Path)
    merge.add_argument("chunks", type=Path, nargs="+")

    check = subparsers.add_parser("check", help="Evaluate the saturation stopping rule.")
    check.add_argument("run_dir", type=Path)
    check.add_argument("--minimum-read", type=int, default=20)
    check.add_argument("--window", type=int, default=5)
    return parser


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def initialize(run_dir: Path) -> int:
    selected_path = run_dir / "selected.json"
    if not selected_path.is_file():
        logger.error("No selected.json in %s; apply abstract screening first.", run_dir)
        return EXIT_ERROR
    selected = read_json(selected_path)
    screening = read_json(run_dir / "screening.json") if (run_dir / "screening.json").is_file() else {}
    decisions = {
        normalized_title(item["title"]): item.get("decision", "supporting")
        for item in screening.get("records", [])
    }
    ledger_path = run_dir / "evidence-ledger.json"
    old = read_json(ledger_path) if ledger_path.is_file() else {}
    prior = {
        normalized_title(item["title"]): item for item in old.get("records", [])
    }

    records: list[dict[str, Any]] = []
    for order, paper in enumerate(selected.get("papers", []), start=1):
        title_key = normalized_title(paper["title"])
        previous = prior.get(title_key, {})
        records.append(
            {
                "order": order,
                "key": paper.get("doi") or title_key,
                "title": paper["title"],
                "screening_decision": decisions.get(title_key, "supporting"),
                "status": previous.get("status", "pending"),
                "concepts": previous.get("concepts", []),
                "new_concepts": previous.get("new_concepts", []),
                "evidence_domains": previous.get("evidence_domains", []),
                "new_domains": previous.get("new_domains", []),
                "evidence_notes": previous.get("evidence_notes", ""),
            }
        )

    ledger = {
        "topic": selected.get("topic", ""),
        "generated": datetime.now(UTC).date().isoformat(),
        "instructions": (
            "After reading each paper, set status=read, list its concepts, and list only "
            "concepts not already represented by earlier read papers in new_concepts."
        ),
        "records": records,
    }
    ledger_path.write_text(json.dumps(ledger, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("%d selected papers -> %s", len(records), ledger_path)
    return EXIT_SUCCESS


def merge_chunks(run_dir: Path, chunk_paths: list[Path]) -> int:
    ledger_path = run_dir / "evidence-ledger.json"
    if not ledger_path.is_file():
        logger.error("No evidence-ledger.json in %s; run saturation.py init first.", run_dir)
        return EXIT_ERROR
    ledger = read_json(ledger_path)
    records = ledger.get("records", [])
    by_order = {item["order"]: item for item in records}
    reviewed: dict[int, dict[str, Any]] = {}

    for path in chunk_paths:
        chunk = read_json(path)
        for item in chunk.get("records", []):
            order = item.get("order")
            status = item.get("status")
            if order not in by_order:
                logger.error("%s contains unknown selected order: %s", path, order)
                return EXIT_ERROR
            if order in reviewed:
                logger.error("Selected order %s appears in multiple evidence chunks.", order)
                return EXIT_ERROR
            if status not in {"read", "unavailable", "excluded"}:
                logger.error("Order %s has invalid evidence status: %s", order, status)
                return EXIT_ERROR
            if status == "read" and not item.get("concepts"):
                logger.error("Read paper at order %s has no concepts.", order)
                return EXIT_ERROR
            if not isinstance(item.get("concepts", []), list):
                logger.error("Order %s concepts must be a list.", order)
                return EXIT_ERROR
            if not isinstance(item.get("evidence_notes", {}), dict):
                logger.error("Order %s evidence_notes must be an object.", order)
                return EXIT_ERROR
            reviewed[order] = item

    for order, item in reviewed.items():
        target = by_order[order]
        target["status"] = item["status"]
        target["concepts"] = sorted(
            {str(concept).strip() for concept in item.get("concepts", []) if str(concept).strip()}
        )
        target["evidence_notes"] = item.get("evidence_notes", {})

    seen: set[str] = set()
    seen_domains: set[str] = set()
    for item in records:
        if item["status"] != "read":
            item["new_concepts"] = []
            item["evidence_domains"] = []
            item["new_domains"] = []
            continue
        current = [concept for concept in item["concepts"] if concept.lower() not in seen]
        item["new_concepts"] = current
        seen.update(concept.lower() for concept in item["concepts"])
        domains = classify_domains(item["concepts"])
        item["evidence_domains"] = domains
        item["new_domains"] = [domain for domain in domains if domain not in seen_domains]
        seen_domains.update(domains)

    ledger["generated"] = datetime.now(UTC).date().isoformat()
    ledger["records"] = records
    ledger_path.write_text(json.dumps(ledger, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("Merged evidence for %d papers from %d chunks.", len(reviewed), len(chunk_paths))
    logger.info("Concept vocabulary: %d", len(seen))
    logger.info("Evidence domains: %d/%d", len(seen_domains), len(EVIDENCE_DOMAINS))
    return EXIT_SUCCESS


def classify_domains(concepts: list[str]) -> list[str]:
    """Map detailed reviewer labels into a stable, preregistered taxonomy."""
    domains: list[str] = []
    for domain, markers in EVIDENCE_DOMAINS.items():
        if domain in concepts or any(
            marker in concept for concept in concepts for marker in markers
        ):
            domains.append(domain)
    return sorted(domains)


def check(run_dir: Path, minimum_read: int, window: int) -> int:
    ledger_path = run_dir / "evidence-ledger.json"
    if not ledger_path.is_file():
        logger.error("No evidence-ledger.json in %s; run saturation.py init first.", run_dir)
        return EXIT_ERROR
    ledger = read_json(ledger_path)
    records = ledger.get("records", [])
    invalid = [item for item in records if item.get("status") not in STATUSES]
    if invalid:
        logger.error("%d records have invalid status values.", len(invalid))
        return EXIT_ERROR

    read = [item for item in records if item["status"] == "read"]
    pending_core = [
        item
        for item in records
        if item.get("screening_decision") == "core" and item["status"] == "pending"
    ]
    tail = read[-window:] if window > 0 else []
    no_novelty = len(tail) == window and all(not item.get("new_domains") for item in tail)
    saturated = len(read) >= minimum_read and not pending_core and no_novelty
    reasons: list[str] = []
    if len(read) < minimum_read:
        reasons.append(f"only {len(read)} of {minimum_read} minimum papers read")
    if pending_core:
        reasons.append(f"{len(pending_core)} core papers remain pending")
    if not no_novelty:
        reasons.append(f"the last {window} read papers have not all reached zero domain novelty")

    report = {
        "generated": datetime.now(UTC).date().isoformat(),
        "status": "saturated" if saturated else "continue",
        "read": len(read),
        "minimum_read": minimum_read,
        "window": window,
        "pending_core": len(pending_core),
        "trailing_zero_novelty": no_novelty,
        "saturation_basis": "preregistered-evidence-domains",
        "evidence_domains": sorted(
            {domain for item in read for domain in item.get("evidence_domains", [])}
        ),
        "reasons": reasons,
    }
    (run_dir / "saturation-report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    logger.info("%s", report["status"].upper())
    for reason in reasons:
        logger.info("  %s", reason)
    return EXIT_SUCCESS


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        if args.command == "init":
            return initialize(args.run_dir)
        if args.command == "merge":
            return merge_chunks(args.run_dir, args.chunks)
        return check(args.run_dir, args.minimum_read, args.window)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        logger.error("%s", exc)
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())