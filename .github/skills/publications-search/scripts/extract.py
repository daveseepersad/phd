# /// script
# requires-python = ">=3.12"
# dependencies = ["pypdf>=4.3"]
# ///
"""Extract page-anchored text and build citation records for downloaded PDFs.

Each page is prefixed with a [[page N]] marker so quotes pulled from the text
can be attributed to an exact page. Citations are assembled from retrieved
metadata only, never inferred.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from pathlib import Path

from pypdf import PdfReader

sys.path.insert(0, str(Path(__file__).parent))
from _common import (
    Paper,
    citation_apa,
    citation_bibtex,
    load_papers,
    slugify,
)

EXIT_SUCCESS = 0
EXIT_ERROR = 2

logger = logging.getLogger(__name__)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Run folder containing pdfs/.")
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Optional page cap. By default every page is extracted.",
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def extract_text(path: Path, max_pages: int | None) -> tuple[str, int]:
    reader = PdfReader(str(path))
    chunks: list[str] = []
    pages = reader.pages if max_pages is None else reader.pages[:max_pages]
    for number, page in enumerate(pages, start=1):
        try:
            body = page.extract_text() or ""
        except Exception as exc:  # noqa: BLE001
            logger.debug("page %d of %s: %s", number, path.name, exc)
            body = ""
        body = body.encode("utf-8", errors="replace").decode("utf-8")
        body = re.sub(r"[ \t]+", " ", body)
        body = re.sub(r"\n{3,}", "\n\n", body).strip()
        chunks.append(f"[[page {number}]]\n{body}")
    return "\n\n".join(chunks), len(reader.pages)


def bibtex_key(paper: Paper, index: int) -> str:
    surname = "anon"
    if paper.authors:
        surname = slugify(paper.authors[0].split()[-1], 20).replace("-", "") or "anon"
    return f"{surname}{paper.year or index}"


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    selected = args.run_dir / "selected.json"
    retrieved = args.run_dir / "retrieved.json"
    input_path = retrieved if retrieved.is_file() else selected
    if not input_path.is_file():
        logger.error("No selected.json in %s. Run abstract screening first.", args.run_dir)
        return EXIT_ERROR

    papers = load_papers(input_path)
    text_dir = args.run_dir / "text"
    text_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict] = []
    for index, paper in enumerate(papers, start=1):
        record = {
            "index": index,
            "title": paper.title,
            "authors": paper.authors,
            "year": paper.year,
            "venue": paper.venue,
            "doi": paper.doi,
            "url": paper.url,
            "cited_by": paper.cited_by,
            "score": paper.score,
            "score_parts": paper.score_parts,
            "sources": paper.sources,
            "citation_apa": citation_apa(paper),
            "bibtex": citation_bibtex(paper, bibtex_key(paper, index)),
            "pdf": paper.pdf_url,
            "text_file": None,
            "pages": None,
            "abstract": paper.abstract,
        }
        pdf_path = Path(paper.pdf_url) if paper.pdf_url else None
        if pdf_path and pdf_path.is_file():
            try:
                text, pages = extract_text(pdf_path, args.max_pages)
                out = text_dir / f"{pdf_path.stem}.txt"
                out.write_text(text, encoding="utf-8")
                record["text_file"] = str(out)
                record["pages"] = pages
                logger.info("[%02d] %d pages -> %s", index, pages, out.name)
            except Exception as exc:  # noqa: BLE001
                logger.warning("[%02d] extraction failed: %s", index, exc)
        else:
            logger.info("[%02d] no PDF; metadata and abstract only", index)
        records.append(record)

    manifest = args.run_dir / "manifest.json"
    manifest.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")

    bib = args.run_dir / "references.bib"
    bib.write_text("\n\n".join(r["bibtex"] for r in records) + "\n", encoding="utf-8")

    with_text = sum(1 for r in records if r["text_file"])
    logger.info("%d/%d papers with full text -> %s", with_text, len(records), manifest)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
