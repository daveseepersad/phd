# /// script
# requires-python = ">=3.12"
# ///
"""Reconstruct the PRISMA 2020 flow from a run folder's artifacts.

Counts are taken only from persisted files, never re-derived from memory of a
session. Runs made before search-log.json / dedup-log.json existed degrade to
"not recorded" for those cells rather than failing, so older corpora can still
report an honest partial diagram.

Full-text exclusions are read from an optional fulltext-exclusions.json:
{"exclusions": [{"key": ..., "title": ..., "reason": ...}]} with reason one of
no-pdf-available, wrong-scope-on-fulltext, duplicate-version, quality-fail,
other.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

NOT_RECORDED = "not recorded"
FULLTEXT_EXCLUSION_REASONS = {
    "no-pdf-available",
    "wrong-scope-on-fulltext",
    "duplicate-version",
    "quality-fail",
    "other",
}


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("run_dir", type=Path, help="Run folder containing candidates.json.")
    return parser


def read_json(path: Path) -> Any | None:
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None


def _first_int(entry: dict[str, Any], *names: str) -> int | None:
    for name in names:
        value = entry.get(name)
        if isinstance(value, int):
            return value
    return None


def identification(run_root: Path, candidates: dict[str, Any], notes: list[str]) -> dict[str, Any]:
    per_source: Any = NOT_RECORDED
    total_raw: Any = NOT_RECORDED
    search_runs: Any = NOT_RECORDED
    search_log = read_json(run_root / "search-log.json")
    if isinstance(search_log, dict):
        runs = search_log.get("runs")
        if isinstance(runs, list):
            # search.py appends one entry per run; a source hit in several
            # runs (e.g. a refresh) contributes the sum of its hits.
            search_runs = len(runs)
            entries: Any = [
                entry
                for run in runs
                if isinstance(run, dict)
                for entry in run.get("per_source") or []
            ]
        else:
            # Tolerate schema drift: older logs listed entries under
            # "searches" or "sources" at the top level.
            entries = search_log.get("searches") or search_log.get("sources")
        if isinstance(entries, list):
            per_source = {}
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                name = str(entry.get("source") or entry.get("name") or "unknown")
                count = _first_int(
                    entry, "returned", "raw_count", "raw_n", "results", "count", "hits"
                )
                if count is None:
                    per_source.setdefault(name, NOT_RECORDED)
                elif isinstance(per_source.get(name), int):
                    per_source[name] += count
                else:
                    per_source[name] = count
            counted = [n for n in per_source.values() if isinstance(n, int)]
            total_raw = sum(counted) if counted else NOT_RECORDED
    if not (isinstance(per_source, dict) and per_source):
        per_source = NOT_RECORDED
        notes.append("Per-source hit counts were not persisted (no usable search-log.json).")

    rounds: list[dict[str, Any]] = []
    for path in sorted(run_root.glob("snowball-round-*.json")):
        payload = read_json(path)
        if isinstance(payload, dict):
            rounds.append(
                {
                    "round": payload.get("round"),
                    "unique_discovered": payload.get("unique_discovered", 0),
                    "corpus_before": payload.get("corpus_before"),
                    "corpus_after": payload.get("corpus_after"),
                }
            )
    return {
        "databases": {
            "sources_used": candidates.get("sources", []),
            "search_runs": search_runs,
            "records_per_source": per_source,
            "records_total_raw": total_raw,
        },
        "citation_chaining": {
            "rounds": rounds,
            "records_discovered": sum(r["unique_discovered"] for r in rounds),
        },
        "unique_records_after_merge": len(candidates.get("papers", [])),
    }


def deduplication(run_root: Path, notes: list[str]) -> dict[str, Any]:
    dedup_log = read_json(run_root / "dedup-log.json")
    if isinstance(dedup_log, dict) and isinstance(dedup_log.get("runs"), list):
        runs = [run for run in dedup_log["runs"] if isinstance(run, dict)]
    elif isinstance(dedup_log, dict):
        # Legacy flat file from before dedup-log.json gained a runs list.
        runs = [dedup_log]
    elif isinstance(dedup_log, list):
        runs = [{"events": dedup_log}]
    else:
        notes.append("Duplicate-removal counts were not persisted (no dedup-log.json).")
        return {"duplicates_removed": NOT_RECORDED}
    removed = 0
    for run in runs:
        count = run.get("event_count")
        removed += count if isinstance(count, int) else len(run.get("events") or [])
    events = [event for run in runs for event in run.get("events") or []]
    by_pass = Counter(
        event.get("pass", "unknown") for event in events if isinstance(event, dict)
    )
    return {"duplicates_removed": removed, "by_pass": dict(by_pass)}


def fulltext_exclusions(run_root: Path, notes: list[str]) -> tuple[Any, list[dict[str, Any]]]:
    payload = read_json(run_root / "fulltext-exclusions.json")
    if payload is None:
        # The evidence ledger already accounts for every assessed report, so a
        # missing file is only unknown when the ledger is missing too.
        ledger = read_json(run_root / "evidence-ledger.json")
        records = (ledger or {}).get("records") if isinstance(ledger, dict) else None
        if not records:
            notes.append(
                "No fulltext-exclusions.json and no evidence ledger; full-text "
                "exclusions (if any) were not recorded."
            )
            return NOT_RECORDED, []
        derived = [
            {
                "key": item.get("key"),
                "title": item.get("title"),
                "reason": (item.get("evidence_notes") or {}).get("reason", "other"),
                "source": "evidence-ledger",
            }
            for item in records
            if item.get("status") == "excluded"
        ]
        notes.append(
            f"Full-text exclusions derived from evidence-ledger.json ({len(derived)} "
            "excluded after assessment); write fulltext-exclusions.json to override."
        )
        return dict(Counter(record["reason"] for record in derived)), derived
    records = payload.get("exclusions", []) if isinstance(payload, dict) else []
    for record in records:
        reason = record.get("reason")
        if reason not in FULLTEXT_EXCLUSION_REASONS:
            logger.warning(
                "Unknown full-text exclusion reason %r on %r; keeping it verbatim.",
                reason, (record.get("title") or record.get("key") or "?")[:60],
            )
    by_reason = Counter(record.get("reason", "other") for record in records)
    return dict(by_reason), records


def build_flow(run_root: Path) -> dict[str, Any]:
    candidates = read_json(run_root / "candidates.json")
    if not isinstance(candidates, dict):
        raise FileNotFoundError(f"No candidates.json in {run_root}")
    screening = read_json(run_root / "screening.json") or {}
    selected = read_json(run_root / "selected.json") or {}
    retrieved = read_json(run_root / "retrieved.json") or {}
    manifest = read_json(run_root / "manifest.json") or []
    ledger = read_json(run_root / "evidence-ledger.json") or {}

    notes: list[str] = []
    decisions = Counter(
        record.get("decision", "pending") for record in screening.get("records", [])
    )
    sought = len(selected.get("papers", []))
    with_fulltext = sum(1 for record in manifest if record.get("text_file"))
    fetched = retrieved.get("fetched")
    if not isinstance(fetched, int):
        fetched = with_fulltext
    excluded_by_reason, exclusion_records = fulltext_exclusions(run_root, notes)
    ledger_status = Counter(
        record.get("status", "pending") for record in ledger.get("records", [])
    )
    included = ledger_status.get("read", 0)
    if not ledger.get("records"):
        notes.append("No evidence-ledger.json; included-in-synthesis falls back to 0.")

    return {
        "generated": datetime.now(UTC).date().isoformat(),
        "topic": candidates.get("topic", ""),
        "identification": identification(run_root, candidates, notes),
        "deduplication": deduplication(run_root, notes),
        "screening": {
            "records_screened": len(screening.get("records", [])),
            "decisions": dict(decisions),
            "records_excluded": decisions.get("exclude", 0),
            "reports_sought_for_retrieval": sought,
        },
        "retrieval": {
            "reports_sought": sought,
            "reports_retrieved": fetched,
            "reports_not_retrieved": max(sought - fetched, 0),
        },
        "fulltext_assessment": {
            "reports_assessed": with_fulltext,
            "excluded_by_reason": excluded_by_reason,
            "exclusions": exclusion_records,
        },
        "included": {
            "studies_in_synthesis": included,
            "read_status": dict(ledger_status),
        },
        "notes": notes,
    }


def _cell(value: Any) -> str:
    return str(value) if isinstance(value, int) else NOT_RECORDED


def render_markdown(flow: dict[str, Any]) -> str:
    ident = flow["identification"]
    databases = ident["databases"]
    chaining = ident["citation_chaining"]
    screening = flow["screening"]
    retrieval = flow["retrieval"]
    fulltext = flow["fulltext_assessment"]

    per_source = databases["records_per_source"]
    if isinstance(per_source, dict):
        source_lines = "<br/>".join(
            f"{name}: {_cell(count)}" for name, count in sorted(per_source.items())
        )
    else:
        source_lines = NOT_RECORDED
    dupes = flow["deduplication"].get("duplicates_removed")
    excluded_reasons = fulltext["excluded_by_reason"]
    if isinstance(excluded_reasons, dict) and excluded_reasons:
        reason_lines = "<br/>".join(
            f"{reason}: {count}" for reason, count in sorted(excluded_reasons.items())
        )
    elif excluded_reasons == NOT_RECORDED:
        reason_lines = NOT_RECORDED
    else:
        reason_lines = "none recorded"
    non_core_excluded = (
        f"context: {screening['decisions'].get('context', 0)}<br/>"
        f"unresolved: {screening['decisions'].get('unresolved', 0)}"
    )

    mermaid = f"""```mermaid
flowchart TD
    A["Identification<br/>Database records: {_cell(databases["records_total_raw"])}<br/>{source_lines}"]
    B["Citation chaining ({len(chaining["rounds"])} round{"s" if len(chaining["rounds"]) != 1 else ""})<br/>Records discovered: {chaining["records_discovered"]}"]
    C["Unique records after merge: {ident["unique_records_after_merge"]}<br/>Duplicates removed: {_cell(dupes)}"]
    D["Records screened: {screening["records_screened"]}"]
    E["Records excluded: {screening["records_excluded"]}<br/>{non_core_excluded}"]
    F["Reports sought for retrieval: {retrieval["reports_sought"]}"]
    G["Reports not retrieved: {retrieval["reports_not_retrieved"]}"]
    H["Reports assessed for eligibility: {fulltext["reports_assessed"]}"]
    I["Reports excluded:<br/>{reason_lines}"]
    J["Studies included in synthesis: {flow["included"]["studies_in_synthesis"]}"]
    A --> C
    B --> C
    C --> D
    D --> E
    D --> F
    F --> G
    F --> H
    H --> I
    H --> J
```"""

    decisions_row = ", ".join(
        f"{name}: {count}" for name, count in sorted(screening["decisions"].items())
    )
    table = "\n".join(
        [
            "| Phase | Measure | Value |",
            "|---|---|---|",
            f"| Identification | Search runs | {_cell(databases['search_runs'])} |",
            f"| Identification | Database records (raw) | {_cell(databases['records_total_raw'])} |",
            f"| Identification | Sources used | {', '.join(databases['sources_used']) or NOT_RECORDED} |",
            f"| Identification | Citation-chaining records | {chaining['records_discovered']} |",
            f"| Identification | Unique records after merge | {ident['unique_records_after_merge']} |",
            f"| Deduplication | Duplicates removed | {_cell(dupes)} |",
            f"| Screening | Records screened | {screening['records_screened']} |",
            f"| Screening | Decisions | {decisions_row or NOT_RECORDED} |",
            f"| Retrieval | Reports sought | {retrieval['reports_sought']} |",
            f"| Retrieval | Reports retrieved | {retrieval['reports_retrieved']} |",
            f"| Full-text | Reports assessed | {fulltext['reports_assessed']} |",
            f"| Full-text | Excluded with reasons | {reason_lines.replace('<br/>', ', ')} |",
            f"| Included | Studies in synthesis | {flow['included']['studies_in_synthesis']} |",
        ]
    )

    notes = "".join(f"\n- {note}" for note in flow["notes"])
    notes_section = f"\n## Not recorded\n{notes}\n" if notes else ""
    return (
        f"# PRISMA 2020 Flow — {flow['topic']}\n\n"
        f"Generated {flow['generated']} from persisted run artifacts only.\n\n"
        f"{mermaid}\n\n{table}\n{notes_section}"
    )


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        flow = build_flow(args.run_dir)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        logger.error("%s", exc)
        return EXIT_ERROR

    json_path = args.run_dir / "prisma.json"
    json_path.write_text(json.dumps(flow, indent=2, ensure_ascii=False), encoding="utf-8")
    md_path = args.run_dir / "prisma.md"
    md_path.write_text(render_markdown(flow), encoding="utf-8")
    logger.info(
        "screened=%d sought=%d assessed=%d included=%d -> %s, %s",
        flow["screening"]["records_screened"],
        flow["retrieval"]["reports_sought"],
        flow["fulltext_assessment"]["reports_assessed"],
        flow["included"]["studies_in_synthesis"],
        json_path,
        md_path,
    )
    for note in flow["notes"]:
        logger.warning("%s", note)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
