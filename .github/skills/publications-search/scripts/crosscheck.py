# /// script
# requires-python = ">=3.12"
# ///
"""Cross-check in-text citations against the reference list and references.bib.

NSU states the requirement twice: every citation must appear in the reference
list and every reference must be cited. Matching is surname + year only —
robust to APA formatting variation but blind to same-surname collisions — so
every flag means "unmatched, verify manually", never "confirmed defect".
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import unicodedata
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _common import apa_name

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)

YEAR = r"(?:19|20)\d{2}[a-z]?"
# Surname particles the SURNAME pattern accepts, mirrored in record() so
# "van der Aalst" and "Van der Aalst" both survive the name guard and key
# identically through norm_name.
PARTICLES = frozenset(
    ["van", "von", "de", "del", "della", "der", "den", "da", "di", "du", "la", "le", "ter", "ten"]
)
# One capitalized surname, optionally preceded by particles (van, de, ...)
# in either case ("van der Aalst", "Van der Aalst"). The leading \b keeps a
# particle from starting mid-word ("later van ..." must not yield "ter van ...").
SURNAME = r"\b(?:(?i:v[ao]n|de[lrn]?|d[aiu]|l[ae]|te[rn]|del|della)\s+)*[A-Z][\w'’-]+"
# Page/section locators that may trail a citation: ", p. 4", ", pp. 3-5", ", Chapter 2".
LOCATOR = r",\s*(?i:pp?\.\s*\d+(?:\s*[-–—]\s*\d+)?|chapter\s+\d+)"
# Narrative forms: Li (2026), Zeng et al. (2025), Agha and Miqdad (2026),
# A & B (2026), and author lists with or without a serial comma —
# "Guest, Bunce & Johnson's (2006)", "Orogat, Rostam, and Mansour (2026)".
NARRATIVE = re.compile(
    rf"(?P<authors>{SURNAME}(?:,\s+{SURNAME})*(?:,?\s+(?:and|&)\s+{SURNAME})?(?:\s+et al\.?)?)"
    rf"(?:['’]s)?\s+\((?P<year>{YEAR})(?:{LOCATOR})?\)"
)
PAREN_GROUP = re.compile(rf"\(([^()]*\b{YEAR}\b[^()]*)\)")
PAREN_SEGMENT = re.compile(rf"^(?P<authors>.+?),?\s+(?P<year>{YEAR})$")
TRAILING_LOCATOR = re.compile(rf"(?:{LOCATOR})\s*$")


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Run folder containing the document.")
    parser.add_argument(
        "--doc",
        type=Path,
        default=None,
        help="Document path relative to the run folder (default: thesis.md, else review.md).",
    )
    return parser


def norm_name(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z]", "", decomposed.lower())


def base_year(value: str) -> str:
    return value[:4]


def first_surname(authors: str) -> str:
    """First author's surname from any citation author fragment."""
    fragment = re.split(r",|&|\bet al\b|\band\b", authors, maxsplit=1)[0]
    fragment = re.sub(r"['’]s$", "", fragment.strip())
    return fragment.strip()


def extract_citations(body: str) -> dict[tuple[str, str], dict[str, Any]]:
    """All (surname, year) pairs cited in the body, with a display form."""
    citations: dict[tuple[str, str], dict[str, Any]] = {}

    def record(authors: str, year: str) -> None:
        surname = first_surname(authors)
        if not surname:
            return
        # A surname starts uppercase or with a known particle in either case
        # ("van der Aalst"); anything else is prose, not an author.
        if not surname[0].isupper() and surname.split(" ", 1)[0].lower() not in PARTICLES:
            return
        key = (norm_name(surname), base_year(year))
        entry = citations.setdefault(
            key, {"surname": surname, "year": year, "display": f"{authors} ({year})", "occurrences": 0}
        )
        entry["occurrences"] += 1

    for match in NARRATIVE.finditer(body):
        record(match.group("authors"), match.group("year"))
    for group in PAREN_GROUP.finditer(body):
        # A parenthetical may bundle several citations: (A, 2020; B et al., 2021),
        # wrap across a source line break, or carry a trailing page locator.
        content = re.sub(r"\s+", " ", group.group(1))
        for segment in content.split(";"):
            segment = re.sub(
                r"^\s*(?:e\.g\.|i\.e\.|cf\.|see also|see)[,\s]*",
                "",
                segment.strip(),
                flags=re.IGNORECASE,
            )
            segment = TRAILING_LOCATOR.sub("", segment).strip()
            match = PAREN_SEGMENT.match(segment)
            if not match:
                continue
            authors = match.group("authors").strip()
            # Page/section locators ("2025, p. 4") and bare years are not authors.
            if not authors or not re.search(r"[A-Za-z]", authors):
                continue
            record(authors, match.group("year"))
    return citations


def split_reference_entries(section: str) -> list[str]:
    """Split a References section into entries (bulleted, numbered, or hanging-indent)."""
    entries: list[str] = []
    current: list[str] = []
    lines = section.splitlines()
    marker = re.compile(r"^(?:[-*+]|\d+[.)])\s+")
    listed = any(marker.match(line) for line in lines)
    for line in lines:
        starts_entry = (
            bool(marker.match(line)) if listed else bool(line) and not line[0].isspace()
        )
        if starts_entry:
            if current:
                entries.append(" ".join(current))
            current = [marker.sub("", line).strip()]
        elif line.strip() and current:
            current.append(line.strip())
        elif not line.strip() and current and not listed:
            entries.append(" ".join(current))
            current = []
    if current:
        entries.append(" ".join(current))
    # Prose paragraphs around the list carry no (year); only real entries do.
    return [entry for entry in entries if re.search(rf"\(({YEAR})\)", entry)]


def parse_reference_entry(entry: str) -> dict[str, Any] | None:
    year_match = re.search(rf"\(({YEAR})\)", entry)
    if not year_match:
        return None
    head = entry[: year_match.start()].strip().rstrip(".").strip()
    # APA 7 section 9.12 puts the title in the author position when a work has
    # no author. An authored entry always opens "Surname, I."; anything else is
    # a title and has to be matched on its words rather than a surname.
    authored = re.match(r"^[^,]{1,60},\s+(?:[A-Z]\.|[A-Z][a-z]+,)", head)
    if head and not authored and len(head) > 40:
        return {
            "surname": head,
            "year": year_match.group(1),
            "entry": re.sub(r"\s+", " ", entry)[:140],
            "title_words": [w for w in re.findall(r"[a-z0-9]{4,}", head.lower())],
        }
    surname = entry.split(",", 1)[0].strip().strip("*_").strip()
    if not surname:
        return None
    return {
        "surname": surname,
        "year": year_match.group(1),
        "entry": re.sub(r"\s+", " ", entry)[:140],
        "title_words": [],
    }


def parse_bib(path: Path) -> list[dict[str, Any]]:
    """Minimal BibTeX read: key, first-author surname, year, title per entry."""
    entries: list[dict[str, Any]] = []
    for chunk in re.split(r"(?=^@\w+\s*\{)", path.read_text(encoding="utf-8"), flags=re.MULTILINE):
        head = re.match(r"@\w+\s*\{\s*([^,\s]+)", chunk)
        if not head:
            continue
        author = re.search(r"author\s*=\s*\{(.+?)\},?\s*$", chunk, flags=re.MULTILINE)
        year = re.search(r"year\s*=\s*\{(\d{4})\}", chunk)
        title = re.search(r"title\s*=\s*\{(.+?)\},?\s*$", chunk, flags=re.MULTILINE)
        surname = ""
        if author:
            first = author.group(1).split(" and ")[0].strip()
            surname = apa_name(first).split(",")[0].strip()
        entries.append(
            {
                "key": head.group(1),
                "surname": surname,
                "year": year.group(1) if year else None,
                "title": title.group(1) if title else "",
            }
        )
    return entries


def crosscheck(run_root: Path, doc: Path | None) -> tuple[dict[str, Any], int]:
    if doc is not None:
        doc_path = run_root / doc
    else:
        doc_path = next(
            (p for p in (run_root / "thesis.md", run_root / "review.md") if p.is_file()), None
        )
        if doc_path is None:
            raise FileNotFoundError(f"No thesis.md or review.md in {run_root}; pass --doc.")
    text = doc_path.read_text(encoding="utf-8")

    # Headings are commonly numbered ("## 5. References"); an over-strict match
    # silently yields zero entries and then reports every citation as unreferenced.
    parts = re.split(
        r"^#{1,3}\s+(?:[\d.]+\s*)?References?\s*$", text, maxsplit=1, flags=re.MULTILINE
    )
    body = parts[0]
    ref_section = parts[1] if len(parts) > 1 else ""
    if not ref_section:
        logger.warning(
            "%s has no References heading; reference-side checks are empty.", doc_path.name
        )
    # Stop at the next same-level heading so appendices are not read as entries.
    ref_section = re.split(r"^#{1,3}\s+", ref_section, maxsplit=1, flags=re.MULTILINE)[0]

    citations = extract_citations(body)
    references = [
        parsed
        for entry in split_reference_entries(ref_section)
        if (parsed := parse_reference_entry(entry))
    ]
    ref_keys = {(norm_name(r["surname"]), base_year(r["year"])) for r in references}
    if citations and not references:
        logger.error(
            "%s has %d in-text citations but no parseable reference entries; "
            "the reference list did not parse, so treat every 'cited but not in "
            "reference list' flag below as a parser failure, not a real gap.",
            doc_path.name,
            len(citations),
        )
    ref_by_surname: dict[str, set[str]] = {}
    for ref in references:
        ref_by_surname.setdefault(norm_name(ref["surname"]), set()).add(base_year(ref["year"]))

    bib_path = run_root / "references.bib"
    bib = parse_bib(bib_path) if bib_path.is_file() else []
    bib_keys = {(norm_name(b["surname"]), b["year"]) for b in bib if b["surname"] and b["year"]}
    bib_surnames = {norm_name(b["surname"]) for b in bib if b["surname"]}

    cited_not_referenced: list[dict[str, Any]] = []
    year_mismatches: list[dict[str, Any]] = []
    for (surname, year), info in sorted(citations.items()):
        if (surname, year) in ref_keys:
            continue
        ref_years = ref_by_surname.get(surname)
        item = dict(info)
        if ref_years:
            item["reference_years_for_surname"] = sorted(ref_years)
            year_mismatches.append(item)
        else:
            cited_not_referenced.append(item)

    cited_keys = set(citations)
    cited_surnames = {surname for surname, _ in cited_keys}
    body_words = re.findall(r"[a-z0-9]{4,}", body.lower())

    def cited_by_title(ref: dict[str, Any]) -> bool:
        """An author-less work is cited by a shortened italic title, not a surname."""
        words = ref.get("title_words") or []
        if len(words) < 3:
            return False
        lead = words[:4]
        return any(
            body_words[i : i + len(lead)] == lead for i in range(len(body_words) - len(lead) + 1)
        )

    referenced_never_cited = [
        ref
        for ref in references
        if (norm_name(ref["surname"]), base_year(ref["year"])) not in cited_keys
        # Same-surname multi-work references stay conservative: any citation of
        # the surname counts as possibly-this-entry, so only fully uncited
        # surnames are flagged.
        and norm_name(ref["surname"]) not in cited_surnames
        and not cited_by_title(ref)
    ]
    bib_titles = [b.get("title", "").lower() for b in bib]

    def in_bib_by_title(ref: dict[str, Any]) -> bool:
        words = ref.get("title_words") or []
        return bool(words) and any(
            sum(1 for w in set(words) if w in title) / len(set(words)) >= 0.6
            for title in bib_titles
        )

    in_references_not_in_bib = [
        ref
        for ref in references
        if bib
        and (norm_name(ref["surname"]), base_year(ref["year"])) not in bib_keys
        and norm_name(ref["surname"]) not in bib_surnames
        and not in_bib_by_title(ref)
    ]

    def reportable(refs: list[dict[str, Any]]) -> list[dict[str, Any]]:
        # title_words is a set used only for matching and is not JSON-serializable.
        return [{k: v for k, v in ref.items() if k != "title_words"} for ref in refs]

    report = {
        "generated": datetime.now(UTC).date().isoformat(),
        "document": doc_path.name,
        "bibliography": bib_path.name if bib else None,
        "counts": {
            "unique_citations": len(citations),
            "reference_entries": len(references),
            "bib_entries": len(bib),
            "cited_not_in_references": len(cited_not_referenced),
            "referenced_never_cited": len(referenced_never_cited),
            "in_references_not_in_bib": len(in_references_not_in_bib),
            "year_mismatches": len(year_mismatches),
        },
        "cited_not_in_references": reportable(cited_not_referenced),
        "referenced_never_cited": reportable(referenced_never_cited),
        "in_references_not_in_bib": reportable(in_references_not_in_bib),
        "year_mismatches": reportable(year_mismatches),
        "notes": [
            (
                "Matching is first-author surname + year only; every flag means "
                "'unmatched, verify manually', not 'confirmed defect'."
            ),
            (
                "Same-surname works are matched permissively, so collisions can "
                "hide a genuinely missing entry."
            ),
        ],
    }
    issues = (
        len(cited_not_referenced)
        + len(referenced_never_cited)
        + len(in_references_not_in_bib)
        + len(year_mismatches)
    )
    return report, issues


def print_report(report: dict[str, Any]) -> None:
    counts = report["counts"]
    print(f"Cross-check: {report['document']} vs References vs {report['bibliography'] or '(no .bib)'}")
    print(
        f"  {counts['unique_citations']} unique in-text citations, "
        f"{counts['reference_entries']} reference entries, {counts['bib_entries']} bib entries"
    )
    sections = (
        ("Cited but not in reference list", "cited_not_in_references", "display"),
        ("In reference list but never cited", "referenced_never_cited", "entry"),
        ("In reference list but not in references.bib", "in_references_not_in_bib", "entry"),
        ("Year mismatches (surname matches, year does not)", "year_mismatches", "display"),
    )
    for label, key, field_name in sections:
        items = report[key]
        print(f"\n{label}: {len(items)}")
        for item in items:
            detail = item.get(field_name) or item.get("entry") or ""
            extra = (
                f"  (references have {', '.join(item['reference_years_for_surname'])})"
                if "reference_years_for_surname" in item
                else ""
            )
            print(f"  - {detail}{extra}")
    print("\nAll flags are 'verify manually' — matching is surname + year only.")


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        report, issues = crosscheck(args.run_dir, args.doc)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        logger.error("%s", exc)
        return EXIT_ERROR

    out = args.run_dir / "crosscheck-report.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print_report(report)
    logger.info("%d potential issues -> %s", issues, out)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
