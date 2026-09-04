# /// script
# requires-python = ">=3.12"
# ///
"""Preregister, fingerprint, and validate the review protocol (Kitchenham Stage 0).

`init` writes protocol.md before any search so questions, criteria, domains,
and the stopping rule are demonstrably fixed in advance. `hash` prints the
sha256 that downstream stages stamp into their artifacts, making later edits
to the protocol visible. `check` runs PRISMA-S known-item recall: every
must-find paper listed in the protocol has to surface in candidates.json.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
import re
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _common import Paper
from _common import run_dir as make_run_dir
from saturation import EVIDENCE_DOMAINS

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

# Rows mirror search.py defaults; the browser sources stay listed even when
# optional so the protocol records the decision to skip them, not an omission.
SEARCH_SOURCES = (
    ("openalex", "API", "yes"),
    ("crossref", "API", "yes"),
    ("scholar", "browser", "yes"),
    ("acm", "browser + institutional session", "optional"),
    ("ieee", "browser + institutional session", "optional"),
)

KNOWN_ITEM_HEADING = "## 6. Known-item validation (PRISMA-S)"


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="Write protocol.md before searching.")
    init.add_argument("topic", help="Research question or topic in plain language.")
    init.add_argument("--out", type=Path, default=Path("results"))
    init.add_argument(
        "--run-dir",
        type=Path,
        default=None,
        help="Reuse an existing run folder instead of creating a dated one.",
    )

    hash_cmd = subparsers.add_parser("hash", help="Print the protocol.md sha256.")
    hash_cmd.add_argument("run_dir", type=Path)

    check = subparsers.add_parser("check", help="Known-item recall against candidates.json.")
    check.add_argument("run_dir", type=Path)
    return parser


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def protocol_template(topic: str, run_root: Path) -> str:
    domains = "\n".join(f"- {domain}" for domain in sorted(EVIDENCE_DOMAINS))
    source_rows = "\n".join(
        f"| {name} | {interface} | <query as sent, or same as RQ1> | 50 | <none> | {planned} |"
        for name, interface, planned in SEARCH_SOURCES
    )
    return f"""# Review Protocol — {topic}

Preregistered before any search (Kitchenham Stage 0). Downstream stages stamp
this file's sha256 (`protocol.py hash`) into their artifacts, so any edit made
after searching begins is detectable. Fill every `<...>` placeholder, then run
the search.

- Registered: {datetime.now(UTC).isoformat(timespec="seconds")}
- Run folder: {run_root.name}

## 1. Research questions (verbatim)

Record the questions exactly as they will appear in the methods chapter.

- RQ1. {topic}
- RQ2. <add further questions or delete this line>

## 2. Search strategy (per source)

| Source | Interface | Query as sent | Cap | From-year | Planned |
|---|---|---|---|---|---|
{source_rows}

ACM and IEEE reject long natural-language queries; record the condensed
keyword form actually sent (search.py `--keywords`), not the topic sentence.

## 3. Inclusion / exclusion criteria (testable)

Every candidate abstract receives exactly one decision. A criterion is
testable when two readers of the same abstract reach the same decision.

- **core**: directly answers a research question above and warrants full text.
- **supporting**: contributes a method, limitation, benchmark, or combinable solution.
- **context**: useful background that does not require full-text synthesis.
- **exclude**: keyword collision, wrong field, duplicate, or out of scope.
- **unresolved**: no usable abstract; inspect the landing page before exclusion.

Additional topic-specific tests (edit before searching):

- Include only if: <e.g. the study evaluates an LLM-based agent system empirically>
- Exclude if: <e.g. published before YYYY; not in English; agents are non-LLM>

## 4. Preregistered evidence domains ({len(EVIDENCE_DOMAINS)})

Saturation is evaluated against this fixed taxonomy (saturation.py
EVIDENCE_DOMAINS). Adding a domain after reading begins invalidates the
stopping rule; log any such change as a protocol amendment with its date.

{domains}

## 5. Saturation stopping rule

Saturation-bounded systematic review (Guest, Bunce & Johnson 2006; SAFE,
Boetje & van de Schoot 2024) — not exhaustive Kitchenham coverage. Reading
stops only when all three conditions hold (saturation.py check):

- every paper screened **core** has been read (none pending);
- at least **20** full texts read (`--minimum-read`);
- the trailing window of **5** read papers (`--window`) introduced zero new
  evidence domains from the taxonomy above.

Unread supporting/context papers are reported as a limitation, not silently
dropped.

{KNOWN_ITEM_HEADING}

Must-find papers known before searching. The search strategy is invalid until
`protocol.py check` locates every non-placeholder entry in candidates.json.
List 5-10; keep the `- [ ] title | doi:...` format (doi optional but preferred).

- [ ] <exact title of a paper the search must find> | doi:<10.xxxx/xxxxx>
- [ ] <exact title of a paper the search must find> | doi:<10.xxxx/xxxxx>
- [ ] <exact title of a paper the search must find> | doi:<10.xxxx/xxxxx>
- [ ] <exact title of a paper the search must find> | doi:<10.xxxx/xxxxx>
- [ ] <exact title of a paper the search must find> | doi:<10.xxxx/xxxxx>
"""


def initialize(topic: str, out: Path, run_root: Path | None) -> int:
    if run_root is None:
        run_root = make_run_dir(out, topic)
    else:
        run_root.mkdir(parents=True, exist_ok=True)
    path = run_root / "protocol.md"
    if path.exists():
        logger.error(
            "%s already exists; a preregistered protocol must not be overwritten. "
            "Record changes as dated amendments inside the file instead.",
            path,
        )
        return EXIT_ERROR
    path.write_text(protocol_template(topic, run_root), encoding="utf-8")
    logger.info("Protocol scaffold -> %s", path)
    logger.info("Fill every <...> placeholder, then: protocol.py hash %s", run_root)
    return EXIT_SUCCESS


def protocol_hash(run_root: Path) -> int:
    path = run_root / "protocol.md"
    if not path.is_file():
        logger.error("No protocol.md in %s; run protocol.py init first.", run_root)
        return EXIT_ERROR
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(digest)
    return EXIT_SUCCESS


def parse_known_items(text: str) -> list[dict[str, Any]]:
    """Read the `- [ ] title | doi:...` entries under the known-item heading."""
    items: list[dict[str, Any]] = []
    in_section = False
    for line in text.splitlines():
        if line.startswith("## "):
            in_section = line.strip() == KNOWN_ITEM_HEADING.strip()
            continue
        if not in_section:
            continue
        match = re.match(r"-\s*\[[ xX]\]\s*(.+)", line.strip())
        if not match:
            continue
        body = match.group(1)
        title, _, doi_part = body.partition("|")
        doi_match = re.search(r"doi:\s*(\S+)", doi_part)
        doi = doi_match.group(1).strip(">").lower() if doi_match else None
        title = title.strip().strip("*_").strip()
        # Unfilled template rows keep their angle brackets; report, don't match.
        placeholder = "<" in body or "10.xxxx" in body.lower()
        items.append({"title": title, "doi": doi, "placeholder": placeholder})
    return items


def check_known_items(run_root: Path) -> int:
    path = run_root / "protocol.md"
    if not path.is_file():
        logger.error("No protocol.md in %s; run protocol.py init first.", run_root)
        return EXIT_ERROR
    candidates_path = run_root / "candidates.json"
    if not candidates_path.is_file():
        logger.error("No candidates.json in %s; run the search first.", run_root)
        return EXIT_ERROR

    items = parse_known_items(path.read_text(encoding="utf-8"))
    if not items:
        logger.error("protocol.md lists no known items under %r.", KNOWN_ITEM_HEADING)
        return EXIT_ERROR

    payload = json.loads(candidates_path.read_text(encoding="utf-8"))
    papers = [Paper.from_dict(item) for item in payload.get("papers", [])]
    by_doi = {paper.doi.lower(): paper for paper in papers if paper.doi}
    by_title = {normalized_title(paper.title): paper for paper in papers}

    found, missing, placeholders = 0, 0, 0
    for item in items:
        if item["placeholder"]:
            placeholders += 1
            logger.warning("PLACEHOLDER  %s", item["title"][:80])
            continue
        hit = by_doi.get(item["doi"]) if item["doi"] else None
        if hit is None:
            hit = by_title.get(normalized_title(item["title"]))
        if hit is None:
            missing += 1
            logger.error("MISSING      %s", item["title"][:80])
        else:
            found += 1
            logger.info("FOUND        %s", item["title"][:80])

    logger.info(
        "Known-item recall: %d found, %d missing, %d placeholders (of %d listed).",
        found, missing, placeholders, len(items),
    )
    if missing:
        logger.error("Search strategy fails PRISMA-S known-item validation; broaden the queries.")
        return EXIT_ERROR
    if not found:
        logger.error("Every known item is still a placeholder; fill the list before validating.")
        return EXIT_ERROR
    return EXIT_SUCCESS


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        if args.command == "init":
            return initialize(args.topic, args.out, args.run_dir)
        if args.command == "hash":
            return protocol_hash(args.run_dir)
        return check_known_items(args.run_dir)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        logger.error("%s", exc)
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())
