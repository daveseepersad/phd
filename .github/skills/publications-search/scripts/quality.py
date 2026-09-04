# /// script
# requires-python = ">=3.12"
# ///
"""Per-paper quality assessment for the core full-text corpus.

Kitchenham-style checklist scored 0 / 0.5 / 1 per item; preprints additionally
carry Garousi grey-literature items. Synthesis claims should be weighted by
the resulting rigor score — the absence of any quality stage is the most
common committee criticism of software-engineering SLRs.
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
from _common import Paper, looks_preprint

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

CHECKLIST_ITEMS = (
    "aims_stated",
    "design_appropriate",
    "baseline_or_control",
    "metrics_defined",
    "threats_discussed",
    "data_or_artifacts_available",
    "conclusions_supported",
    "peer_reviewed_venue",
)
# Garousi et al. grey-literature criteria; applied only to preprints.
GREY_ITEMS = ("authority", "methodology", "objectivity", "novelty_impact")
VALID_SCORES = {0, 0.5, 1}
LOW_RIGOR_THRESHOLD = 0.5


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="Scaffold quality.json for core papers with full text.")
    init.add_argument("run_dir", type=Path)

    check = subparsers.add_parser("check", help="Validate scores and compute per-paper rigor.")
    check.add_argument("run_dir", type=Path)

    report = subparsers.add_parser("report", help="Render quality.md sorted by rigor.")
    report.add_argument("run_dir", type=Path)
    return parser


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_candidates_by_title(run_root: Path) -> dict[str, Paper]:
    path = run_root / "candidates.json"
    if not path.is_file():
        return {}
    payload = read_json(path)
    return {
        normalized_title(paper.title): paper
        for paper in (Paper.from_dict(item) for item in payload.get("papers", []))
    }


def initialize(run_root: Path) -> int:
    screening_path = run_root / "screening.json"
    if not screening_path.is_file():
        logger.error("No screening.json in %s; screen abstracts first.", run_root)
        return EXIT_ERROR
    manifest_path = run_root / "manifest.json"
    if not manifest_path.is_file():
        logger.error("No manifest.json in %s; run extract.py first.", run_root)
        return EXIT_ERROR

    manifest = {
        normalized_title(record["title"]): record for record in read_json(manifest_path)
    }
    candidates = load_candidates_by_title(run_root)
    quality_path = run_root / "quality.json"
    prior: dict[str, dict[str, Any]] = {}
    if quality_path.is_file():
        prior = {
            normalized_title(entry["title"]): entry
            for entry in read_json(quality_path).get("entries", [])
        }

    entries: list[dict[str, Any]] = []
    skipped_no_text = 0
    screening = read_json(screening_path)
    for record in screening.get("records", []):
        if record.get("decision") != "core":
            continue
        title_key = normalized_title(record["title"])
        manifest_record = manifest.get(title_key)
        if not manifest_record or not manifest_record.get("text_file"):
            skipped_no_text += 1
            continue
        paper = candidates.get(title_key)
        # Older candidates.json predates the is_preprint field; re-detect.
        is_preprint = bool(paper and (paper.is_preprint or looks_preprint(paper)))
        items = CHECKLIST_ITEMS + (GREY_ITEMS if is_preprint else ())
        previous = prior.get(title_key, {})
        previous_checklist = previous.get("checklist", {})
        entries.append(
            {
                "key": record.get("key") or title_key,
                "title": record["title"],
                "year": record.get("year"),
                "is_preprint": is_preprint,
                "text_file": manifest_record.get("text_file"),
                # Re-init keeps existing scores; only newly applicable items are null.
                "checklist": {item: previous_checklist.get(item) for item in items},
                "notes": previous.get("notes", ""),
            }
        )

    quality = {
        "topic": screening.get("topic", ""),
        "generated": datetime.now(UTC).date().isoformat(),
        "scale": "0 = not satisfied, 0.5 = partially satisfied, 1 = satisfied; null = not yet scored",
        "checklist_items": list(CHECKLIST_ITEMS),
        "grey_literature_items": list(GREY_ITEMS),
        "entries": entries,
    }
    quality_path.write_text(json.dumps(quality, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("%d core papers with full text -> %s", len(entries), quality_path)
    if skipped_no_text:
        logger.warning("%d core papers lack full text and were not scaffolded.", skipped_no_text)
    return EXIT_SUCCESS


def rigor(entry: dict[str, Any]) -> tuple[float | None, int, int]:
    """Mean of scored items, scored count, total items. None until any score exists."""
    values = [value for value in entry.get("checklist", {}).values() if value is not None]
    total = len(entry.get("checklist", {}))
    if not values:
        return None, 0, total
    return round(sum(values) / len(values), 3), len(values), total


def check(run_root: Path) -> int:
    quality_path = run_root / "quality.json"
    if not quality_path.is_file():
        logger.error("No quality.json in %s; run quality.py init first.", run_root)
        return EXIT_ERROR
    quality = read_json(quality_path)
    entries = quality.get("entries", [])

    invalid = 0
    complete = 0
    for entry in entries:
        checklist = entry.get("checklist", {})
        bad = {
            item: value
            for item, value in checklist.items()
            if value is not None and value not in VALID_SCORES
        }
        if bad:
            invalid += 1
            logger.error("Invalid scores on %r: %s", entry["title"][:60], bad)
        score, scored, total = rigor(entry)
        entry["rigor"] = score
        entry["items_scored"] = scored
        if scored == total:
            complete += 1
    if invalid:
        return EXIT_ERROR

    quality["generated"] = datetime.now(UTC).date().isoformat()
    quality_path.write_text(json.dumps(quality, indent=2, ensure_ascii=False), encoding="utf-8")
    low = [entry for entry in entries if entry["rigor"] is not None and entry["rigor"] < LOW_RIGOR_THRESHOLD]
    logger.info("%d/%d papers fully scored; rigor written back -> %s", complete, len(entries), quality_path)
    if complete < len(entries):
        logger.warning("%d papers still have unscored items.", len(entries) - complete)
    for entry in low:
        logger.warning("LOW RIGOR %.2f  %s", entry["rigor"], entry["title"][:70])
    return EXIT_SUCCESS


def report(run_root: Path) -> int:
    quality_path = run_root / "quality.json"
    if not quality_path.is_file():
        logger.error("No quality.json in %s; run quality.py init first.", run_root)
        return EXIT_ERROR
    quality = read_json(quality_path)
    entries = quality.get("entries", [])
    scored = []
    for entry in entries:
        score, count, total = rigor(entry)
        scored.append((score, count, total, entry))
    # Unscored papers sink to the bottom rather than masquerading as rigorous.
    scored.sort(key=lambda row: (row[0] is None, -(row[0] or 0.0), entry_title(row[3])))

    lines = [
        f"# Quality Assessment — {quality.get('topic', '')}",
        "",
        (
            f"Generated {datetime.now(UTC).date().isoformat()}. Rigor = mean of scored "
            f"checklist items (0/0.5/1). Papers below {LOW_RIGOR_THRESHOLD} are flagged; "
            "weight synthesis claims accordingly."
        ),
        "",
        "| Rigor | Flag | Scored | Type | Paper |",
        "|---|---|---|---|---|",
    ]
    for score, count, total, entry in scored:
        flag = "**LOW**" if score is not None and score < LOW_RIGOR_THRESHOLD else ""
        rigor_cell = f"{score:.2f}" if score is not None else "unscored"
        kind = "preprint" if entry.get("is_preprint") else "peer-reviewed"
        year = f" ({entry['year']})" if entry.get("year") else ""
        lines.append(
            f"| {rigor_cell} | {flag} | {count}/{total} | {kind} | {entry['title']}{year} |"
        )
    out = run_root / "quality.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    logger.info("%d papers -> %s", len(scored), out)
    return EXIT_SUCCESS


def entry_title(entry: dict[str, Any]) -> str:
    return entry.get("title", "")


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        if args.command == "init":
            return initialize(args.run_dir)
        if args.command == "check":
            return check(args.run_dir)
        return report(args.run_dir)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        logger.error("%s", exc)
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())
