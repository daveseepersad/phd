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
import logging
import re
import sys
from pathlib import Path

from pypdf import PdfReader

sys.path.insert(0, str(Path(__file__).parent))
from _common import (
    citation_apa,
    citation_bibtex,
    clean_authors,
    load_papers,
    looks_preprint,
    make_bibtex_key,
    write_json_atomic,
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


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


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


def main() -> int:
    args = create_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    # Screened metadata is canonical: retrieved.json lags behind metadata
    # repairs (author fixes, DOI resolution), so it contributes only the
    # local PDF paths recorded at download time.
    selected = args.run_dir / "selected.json"
    candidates = args.run_dir / "candidates.json"
    meta_path = selected if selected.is_file() else candidates
    if not meta_path.is_file():
        logger.error(
            "No selected.json or candidates.json in %s. Run search and screening first.",
            args.run_dir,
        )
        return EXIT_ERROR

    papers = load_papers(meta_path)
    for paper in papers:
        # Corpora written before the is_preprint field default it to False;
        # BibTeX typing depends on it, so backfill from hosting heuristics.
        paper.is_preprint = paper.is_preprint or looks_preprint(paper)
        # Runs that predate the author-hygiene fix still carry scraped
        # toolbar junk; citations must never (REVIEW.md A1).
        paper.authors = clean_authors(paper.authors)
    retrieved_path = args.run_dir / "retrieved.json"
    if retrieved_path.is_file():
        # Join on key first, then on normalized title: a DOI backfilled after
        # download changes paper.key(), which would otherwise orphan the PDF
        # recorded under the old title-only key.
        by_key: dict[str, str] = {}
        by_title: dict[str, str] = {}
        for retrieved in load_papers(retrieved_path):
            if retrieved.pdf_url and Path(retrieved.pdf_url).is_file():
                by_key[retrieved.key()] = retrieved.pdf_url
                by_title[normalized_title(retrieved.title)] = retrieved.pdf_url
        for paper in papers:
            paper.pdf_url = (
                by_key.get(paper.key())
                or by_title.get(normalized_title(paper.title))
                or paper.pdf_url
            )
    text_dir = args.run_dir / "text"
    text_dir.mkdir(parents=True, exist_ok=True)

    used_keys: set[str] = set()
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
            "bibtex": citation_bibtex(paper, make_bibtex_key(paper, used_keys)),
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
    write_json_atomic(manifest, records)

    bib = args.run_dir / "references.bib"
    bib.write_text("\n\n".join(r["bibtex"] for r in records) + "\n", encoding="utf-8")

    with_text = sum(1 for r in records if r["text_file"])
    logger.info("%d/%d papers with full text -> %s", with_text, len(records), manifest)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
