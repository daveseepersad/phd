# /// script
# requires-python = ">=3.12"
# ///
"""Generate an annotated bibliography from artifacts the pipeline already has.

Every selected paper gets its APA-7 citation, screening decision and
rationale, evidence-ledger note summary, and quality rigor score when
quality.json exists. NSU's Appendix L rubric grades an annotated bibliography
directly (item 8), and all of its inputs were produced during screening and
reading — this render costs nothing new.
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
from _common import Paper, citation_apa, looks_preprint

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

# Core is the graded heart of the bibliography; anything else trails.
DECISION_ORDER = {"core": 0, "supporting": 1, "context": 2, "unresolved": 3}
NOTE_MAX_CHARS = 400


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Run folder containing selected.json.")
    return parser


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_papers_by_title(path: Path) -> dict[str, Paper]:
    if not path.is_file():
        return {}
    payload = read_json(path)
    return {
        normalized_title(paper.title): paper
        for paper in (Paper.from_dict(item) for item in payload.get("papers", []))
    }


def _first_string(value: Any) -> str:
    """Best display string from a str, dict, or list note fragment."""
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        # Reviewer shorthand like {"type": ..., "finding": ...}; the finding
        # is the substance.
        if isinstance(value.get("finding"), str):
            return value["finding"]
        return next((v for v in value.values() if isinstance(v, str) and v.strip()), "")
    if isinstance(value, list) and value:
        return _first_string(value[0])
    return ""


def summarize_note(notes: Any) -> str:
    """One-line evidence summary from either ledger note schema (str or dict)."""
    text = ""
    if isinstance(notes, dict):
        headline = notes.get("headline_results")
        if headline:
            text = _first_string(headline)
        if not text:
            text = _first_string(notes.get("research_design"))
        if not text:
            text = _first_string(notes)
    elif isinstance(notes, str):
        text = notes
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > NOTE_MAX_CHARS:
        text = text[: NOTE_MAX_CHARS - 1].rstrip() + "…"
    return text


def rigor_line(entry: dict[str, Any]) -> str | None:
    values = [value for value in entry.get("checklist", {}).values() if value is not None]
    if not values:
        return "not yet scored"
    return f"{sum(values) / len(values):.2f} ({len(values)}/{len(entry.get('checklist', {}))} items scored)"


def build(run_root: Path) -> int:
    selected_path = run_root / "selected.json"
    if not selected_path.is_file():
        logger.error("No selected.json in %s; apply abstract screening first.", run_root)
        return EXIT_ERROR
    selected = read_json(selected_path)
    # candidates.json carries the freshest enriched metadata; the selected
    # snapshot may predate a metadata repair pass.
    candidates = load_papers_by_title(run_root / "candidates.json")

    screening: dict[str, dict[str, Any]] = {}
    screening_path = run_root / "screening.json"
    if screening_path.is_file():
        screening = {
            normalized_title(record["title"]): record
            for record in read_json(screening_path).get("records", [])
        }
    ledger: dict[str, dict[str, Any]] = {}
    ledger_path = run_root / "evidence-ledger.json"
    if ledger_path.is_file():
        ledger = {
            normalized_title(record["title"]): record
            for record in read_json(ledger_path).get("records", [])
        }
    quality: dict[str, dict[str, Any]] = {}
    quality_path = run_root / "quality.json"
    if quality_path.is_file():
        quality = {
            normalized_title(entry["title"]): entry
            for entry in read_json(quality_path).get("entries", [])
        }

    entries: list[tuple[int, int, str, list[str]]] = []
    for item in selected.get("papers", []):
        paper = Paper.from_dict(item)
        title_key = normalized_title(paper.title)
        paper = candidates.get(title_key, paper)
        screen = screening.get(title_key, {})
        decision = screen.get("decision", "supporting")

        block = [f"### {citation_apa(paper)}", ""]
        # Older candidates.json predates the is_preprint field; re-detect.
        flags = " [preprint]" if paper.is_preprint or looks_preprint(paper) else ""
        rationale = screen.get("rationale") or "(no rationale recorded)"
        block.append(f"- **Decision:** {decision}{flags} — {rationale}")
        ledger_record = ledger.get(title_key)
        if ledger_record and ledger_record.get("status") == "read":
            summary = summarize_note(ledger_record.get("evidence_notes"))
            if summary:
                block.append(f"- **Evidence:** {summary}")
            if ledger_record.get("evidence_domains"):
                block.append(f"- **Domains:** {', '.join(ledger_record['evidence_domains'])}")
        elif ledger_record:
            block.append(f"- **Evidence:** full text not read (status: {ledger_record.get('status')}).")
        if title_key in quality:
            block.append(f"- **Quality:** rigor {rigor_line(quality[title_key])}")
        entries.append(
            (
                DECISION_ORDER.get(decision, len(DECISION_ORDER)),
                -(paper.year or 0),
                paper.title.lower(),
                block,
            )
        )

    entries.sort(key=lambda row: row[:3])
    lines = [
        f"# Annotated Bibliography — {selected.get('topic', '')}",
        "",
        (
            f"Generated {datetime.now(UTC).date().isoformat()} from screening decisions, "
            "evidence-ledger notes, and quality scores. Working material and audit "
            "evidence — not submission text."
        ),
    ]
    current_group = None
    group_counts: dict[str, int] = {}
    for order, _, _, _ in entries:
        name = next((k for k, v in DECISION_ORDER.items() if v == order), "other")
        group_counts[name] = group_counts.get(name, 0) + 1
    for order, _, _, block in entries:
        group = next((k for k, v in DECISION_ORDER.items() if v == order), "other")
        if group != current_group:
            current_group = group
            lines += ["", f"## {group.capitalize()} ({group_counts[group]})", ""]
        lines += block
        lines.append("")

    out = run_root / "annotated-bibliography.md"
    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    logger.info(
        "%d papers (%s) -> %s",
        len(entries),
        ", ".join(f"{name}: {count}" for name, count in sorted(group_counts.items(), key=lambda kv: DECISION_ORDER.get(kv[0], 9))),
        out,
    )
    if not quality:
        logger.info("No quality.json yet; entries omit rigor scores.")
    return EXIT_SUCCESS


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        return build(args.run_dir)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        logger.error("%s", exc)
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())
