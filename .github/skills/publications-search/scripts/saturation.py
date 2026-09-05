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

sys.path.insert(0, str(Path(__file__).parent))
from _common import write_json_atomic

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

STATUSES = {"pending", "read", "unavailable", "excluded"}
# Fixed data-extraction form scaffolded onto every ledger record (REVIEW.md B:
# free-form notes cannot feed Ch2 evidence tables). Values stay null until the
# reviewer fills them while reading.
EXTRACTION_FIELDS = (
    "study_type",
    "framework",
    "agent_count",
    "topology",
    "benchmark",
    "baseline",
    "key_results",
    "limitations",
    "venue_type",
)
EPILOG = """\
Structured extraction form (scaffolded on init, filled while reading):
  study_type   empirical / benchmark-study / case-study / survey / position
  framework    system or toolkit under study (e.g. MetaGPT, AutoGen)
  agent_count  number of agents in the studied configuration
  topology     centralized / hierarchical / decentralized / pipeline / ...
  benchmark    evaluation suite used (e.g. SWE-bench, HumanEval)
  baseline     comparison condition (e.g. single-agent, agentless)
  key_results  headline quantitative or qualitative findings
  limitations  threats and caveats the paper itself reports
  venue_type   journal / conference / workshop / preprint

Records may also carry read_order (1-based reading sequence) and read_at
(UTC ISO timestamp). When every read record has read_order, the saturation
window is evaluated over reading order; otherwise it falls back to corpus
order and the report says so.
"""
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

# The built-in taxonomy above was derived from a software-engineering review. A
# run on another subject would map most of its concepts to nothing, every
# new_domains list would come back empty, and the stopping rule would fire on
# the minimum-read threshold alone while reporting saturation. Each run
# therefore preregisters its own taxonomy here, written by protocol.py init.
DOMAINS_FILE = "evidence-domains.json"


def load_domains(run_dir: Path) -> tuple[dict[str, tuple[str, ...]], str]:
    """The run's preregistered taxonomy, or the built-in default."""
    path = run_dir / DOMAINS_FILE
    if not path.is_file():
        return EVIDENCE_DOMAINS, "built-in"
    raw = json.loads(path.read_text(encoding="utf-8"))
    domains = raw.get("domains", raw)
    return {name: tuple(markers) for name, markers in domains.items()}, DOMAINS_FILE


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
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
    check.add_argument(
        "--window-sweep",
        action="store_true",
        help="Also evaluate the stopping decision for windows 3-8 (sensitivity sweep).",
    )
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
        record = {
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
            # Null scaffold merged under any values a prior init or reviewer
            # already filled; extra reviewer-added keys survive re-init too.
            "extraction": {
                **{field: None for field in EXTRACTION_FIELDS},
                **(previous.get("extraction") or {}),
            },
        }
        # Reading-sequence provenance must survive re-init or the saturation
        # window silently degrades back to corpus order.
        for field in ("read_order", "read_at"):
            if field in previous:
                record[field] = previous[field]
        records.append(record)

    ledger = {
        "topic": selected.get("topic", ""),
        "generated": datetime.now(UTC).date().isoformat(),
        "instructions": (
            "After reading each paper, set status=read, list its concepts, and list only "
            "concepts not already represented by earlier read papers in new_concepts. "
            "Record read_order (1-based reading sequence) and read_at (UTC ISO timestamp) "
            "as each paper is read, and fill the extraction form fields; leave unknown "
            "values null."
        ),
        "records": records,
    }
    write_json_atomic(ledger_path, ledger)
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
        # Reviewers hand back a bare array as often as a wrapped object, and a
        # shape mismatch used to surface as an AttributeError traceback.
        if isinstance(chunk, list):
            chunk_records = chunk
        elif isinstance(chunk, dict):
            chunk_records = chunk.get("records", [])
        else:
            logger.error(
                "%s: expected a JSON array of records or an object with a "
                "'records' array, got %s.",
                path,
                type(chunk).__name__,
            )
            return EXIT_ERROR
        if not chunk_records:
            logger.error("%s: contains no records.", path)
            return EXIT_ERROR
        for item in chunk_records:
            order = item.get("order")
            status = item.get("status")
            if order not in by_order:
                logger.error(
                    "%s contains unknown selected order: %s. Evidence chunks bind by "
                    "the ledger's 'order' field, not by key or title.",
                    path,
                    order,
                )
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
            # bool is an int subclass, so it must be rejected explicitly.
            read_order = item.get("read_order")
            if "read_order" in item and (
                isinstance(read_order, bool) or not isinstance(read_order, int) or read_order < 1
            ):
                logger.error("Order %s read_order must be a positive integer.", order)
                return EXIT_ERROR
            if "read_at" in item:
                try:
                    datetime.fromisoformat(str(item["read_at"]))
                except ValueError:
                    logger.error(
                        "Order %s read_at is not an ISO timestamp: %s", order, item["read_at"]
                    )
                    return EXIT_ERROR
            if "extraction" in item and not isinstance(item["extraction"], dict):
                logger.error("Order %s extraction must be an object.", order)
                return EXIT_ERROR
            reviewed[order] = item

    for order, item in reviewed.items():
        target = by_order[order]
        target["status"] = item["status"]
        target["concepts"] = sorted(
            {str(concept).strip() for concept in item.get("concepts", []) if str(concept).strip()}
        )
        # Optional fields update only when the chunk carries them: absent means
        # "leave the ledger value alone" (a read_order-only retrofit must not
        # wipe merged notes), while an explicit empty value still replaces.
        for field in ("evidence_notes", "read_order", "read_at"):
            if field in item:
                target[field] = item[field]
        if isinstance(item.get("extraction"), dict):
            target["extraction"] = {
                **{field: None for field in EXTRACTION_FIELDS},
                **(target.get("extraction") or {}),
                **item["extraction"],
            }

    # Two papers cannot share one slot in the reading sequence; refuse to
    # persist a ledger whose read order is ambiguous.
    read_orders = [
        item["read_order"]
        for item in records
        if isinstance(item.get("read_order"), int) and not isinstance(item.get("read_order"), bool)
    ]
    duplicates = sorted({value for value in read_orders if read_orders.count(value) > 1})
    if duplicates:
        logger.error("Duplicate read_order values across the ledger: %s", duplicates)
        return EXIT_ERROR

    read_records = [item for item in records if item["status"] == "read"]
    domains_taxonomy, taxonomy_source = load_domains(run_dir)
    for item in records:
        if item["status"] != "read":
            item["new_concepts"] = []
            item["evidence_domains"] = []
            item["new_domains"] = []

    # Novelty is attributed in the order papers were actually read, not the
    # order they sit in the corpus, so the trailing window measures reading.
    sequence, basis = reading_sequence(read_records)
    if basis == "corpus-order-fallback" and any("read_order" in item for item in read_records):
        logger.warning(
            "read_order is missing on some read records; novelty attributed in corpus order."
        )
    seen: set[str] = set()
    seen_domains: set[str] = set()
    for item in sequence:
        current = [concept for concept in item["concepts"] if concept.lower() not in seen]
        item["new_concepts"] = current
        seen.update(concept.lower() for concept in item["concepts"])
        domains = classify_domains(item["concepts"], domains_taxonomy)
        item["evidence_domains"] = domains
        item["new_domains"] = [domain for domain in domains if domain not in seen_domains]
        seen_domains.update(domains)

    unmapped = [
        item["key"]
        for item in sequence
        if item["concepts"] and not item["evidence_domains"]
    ]

    ledger["generated"] = datetime.now(UTC).date().isoformat()
    ledger["records"] = records
    write_json_atomic(ledger_path, ledger)
    logger.info("Merged evidence for %d papers from %d chunks.", len(reviewed), len(chunk_paths))
    logger.info("Concept vocabulary: %d", len(seen))
    logger.info(
        "Evidence domains: %d/%d (taxonomy: %s)",
        len(seen_domains),
        len(domains_taxonomy),
        taxonomy_source,
    )
    if unmapped:
        # Concepts that map nowhere look identical to genuine zero novelty.
        logger.warning(
            "%d read papers have concepts that map to no domain (%s). The taxonomy "
            "may not fit this subject; saturation would fire on read count alone.",
            len(unmapped),
            ", ".join(unmapped[:5]),
        )
    return EXIT_SUCCESS


def classify_domains(
    concepts: list[str], domains: dict[str, tuple[str, ...]] | None = None
) -> list[str]:
    """Map detailed reviewer labels into a stable, preregistered taxonomy."""
    taxonomy = EVIDENCE_DOMAINS if domains is None else domains
    found: list[str] = []
    for domain, markers in taxonomy.items():
        if domain in concepts or any(
            marker in concept for concept in concepts for marker in markers
        ):
            found.append(domain)
    return sorted(found)


def reading_sequence(read_records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], str]:
    """Order read papers by the recorded reading sequence when it is complete.

    A partial read_order cannot be interleaved with unordered records without
    guessing, so any gap falls back to corpus order — and callers must say so
    in the persisted report (REVIEW.md: novelty was computed in corpus order).
    """
    if read_records and all(
        isinstance(item.get("read_order"), int) and not isinstance(item.get("read_order"), bool)
        for item in read_records
    ):
        return sorted(read_records, key=lambda item: item["read_order"]), "read-order"
    return list(read_records), "corpus-order-fallback"


def window_is_quiet(sequence: list[dict[str, Any]], window: int) -> bool:
    """True when the last ``window`` read papers all produced zero new domains."""
    tail = sequence[-window:] if window > 0 else []
    return len(tail) == window and all(not item.get("new_domains") for item in tail)


def check(run_dir: Path, minimum_read: int, window: int, window_sweep: bool = False) -> int:
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
    sequence, basis = reading_sequence(read)
    warnings: list[str] = []
    domains_taxonomy, taxonomy_source = load_domains(run_dir)
    unmapped = [item for item in read if item.get("concepts") and not item.get("evidence_domains")]
    if unmapped:
        # A concept that maps to no domain is indistinguishable from a paper
        # that introduced nothing new, so an ill-fitting taxonomy reads as
        # saturation. Say so in the report rather than letting it pass.
        warnings.append(
            f"{len(unmapped)} of {len(read)} read papers have concepts that map to no "
            f"domain in the '{taxonomy_source}' taxonomy; zero novelty may be a "
            f"taxonomy mismatch rather than saturation"
        )
        logger.warning(warnings[-1])
    if basis == "corpus-order-fallback":
        warnings.append(
            "read_order absent; consecutive-novelty window evaluated over corpus order"
        )
        logger.warning(
            "No complete read_order in the ledger; the novelty window follows corpus order."
        )
    pending_core = [
        item
        for item in records
        if item.get("screening_decision") == "core" and item["status"] == "pending"
    ]
    no_novelty = window_is_quiet(sequence, window)
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
        "window_basis": basis,
        "pending_core": len(pending_core),
        "trailing_zero_novelty": no_novelty,
        "saturation_basis": "preregistered-evidence-domains",
        "domain_taxonomy": taxonomy_source,
        "domain_taxonomy_size": len(domains_taxonomy),
        "evidence_domains": sorted(
            {domain for item in read for domain in item.get("evidence_domains", [])}
        ),
        "reasons": reasons,
    }
    if warnings:
        report["warnings"] = warnings
    if window_sweep:
        # Sensitivity sweep (REVIEW.md B): show that the stopping decision is
        # not an artifact of one particular window choice.
        sweep = []
        for candidate in range(3, 9):
            quiet = window_is_quiet(sequence, candidate)
            decided = len(read) >= minimum_read and not pending_core and quiet
            sweep.append(
                {
                    "window": candidate,
                    "trailing_zero_novelty": quiet,
                    "status": "saturated" if decided else "continue",
                }
            )
        report["window_sweep"] = sweep
        for entry in sweep:
            logger.info("  window=%d -> %s", entry["window"], entry["status"])
    write_json_atomic(run_dir / "saturation-report.json", report)
    logger.info("%s (window basis: %s)", report["status"].upper(), basis)
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
        return check(args.run_dir, args.minimum_read, args.window, args.window_sweep)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        logger.error("%s", exc)
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())