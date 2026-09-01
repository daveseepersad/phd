"""Shared helpers for the publications-search skill.

Ranking, metadata normalization, and on-disk layout for a review run.
"""
from __future__ import annotations

import json
import math
import re
import time
import unicodedata
from collections.abc import Iterable
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

STOPWORDS = frozenset(
    ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "have", "how", "in", "is", "it", "its", "of", "on", "or", "that", "the", "to", "was", "were", "what", "when", "where", "which", "who", "why", "with", "using", "use", "can", "could", "do", "does", "using"]
)

# Browser profile holding the institutional SSO session; created by auth_setup.py.
DEFAULT_PROFILE_DIR = Path.home() / ".cache" / "publications-search" / "browser-profile"

# Without this flag ACM's Cloudflare challenge never clears. Headless is
# detected outright by both ACM and Scholar, so browser sources run headed;
# use xvfb-run for unattended batches.
BROWSER_ARGS = ["--disable-blink-features=AutomationControlled"]
CHALLENGE_MARKERS = ("just a moment", "checking your browser", "verifying you are human")


@dataclass(frozen=True)
class RankingProfile:
    """Weights for a repeatable literature-ranking strategy."""

    relevance: float
    citations: float
    recency: float
    half_life_years: float


RANKING_PROFILES = {
    "frontier": RankingProfile(0.50, 0.15, 0.35, 3.0),
    "balanced": RankingProfile(0.50, 0.30, 0.20, 4.0),
    "foundational": RankingProfile(0.45, 0.40, 0.15, 6.0),
}


def launch_context(playwright, profile_dir: Path, headless: bool = False):
    """Open the persistent profile with the flags these publishers require."""
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=str(profile_dir),
        headless=headless,
        args=BROWSER_ARGS,
        viewport={"width": 1440, "height": 900},
    )
    state_path = storage_state_path(profile_dir)
    if state_path.is_file():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
            context.add_cookies(state.get("cookies", []))
        except (json.JSONDecodeError, OSError, ValueError):
            pass
    return context


def storage_state_path(profile_dir: Path) -> Path:
    """Return the private snapshot used to preserve session-only SSO cookies."""
    return profile_dir.parent / f"{profile_dir.name}-storage-state.json"


def save_storage_state(context, profile_dir: Path) -> Path:
    """Persist Playwright cookies, including cookies Chromium drops at exit."""
    path = storage_state_path(profile_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    context.storage_state(path=str(path))
    path.chmod(0o600)
    return path


def wait_past_challenge(page, timeout_s: float = 40.0) -> bool:
    """Block until an interstitial bot check clears. Returns False on timeout."""
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        title = (page.title() or "").lower()
        if not any(marker in title for marker in CHALLENGE_MARKERS):
            return True
        page.wait_for_timeout(3000)
    return False


ACCESS_PROBES = {
    "ACM Digital Library": "https://dl.acm.org/",
    "IEEE Xplore": "https://ieeexplore.ieee.org/Xplore/home.jsp",
}
LIBRARY_ACCESS_URLS = {
    "ACM Digital Library": "https://sherman.library.nova.edu/elibrary/access/405?confirm=1&newtab=1",
    "IEEE Xplore": "https://sherman.library.nova.edu/elibrary/access/1001?confirm=1&newtab=1",
}
# Present only while the institutional session is live.
ACCESS_MARKERS = {
    "ACM Digital Library": ("nova southeastern university",),
    "IEEE Xplore": ("access provided by", "nova southeastern university"),
}


def seed_library_access(context, log=None) -> None:
    """Mint publisher entitlement cookies through NSU's database directory."""
    for name, url in LIBRARY_ACCESS_URLS.items():
        page = context.new_page()
        try:
            page.goto(url, wait_until="commit", timeout=90_000)
            page.wait_for_timeout(5000)
            if log:
                log.info("Seeded %-20s via Sherman Library", name)
        except Exception as exc:  # noqa: BLE001
            if log:
                log.warning("Could not seed %s: %s", name, exc)
        finally:
            page.close()


def check_access(context, log=None) -> dict[str, bool]:
    """Probe each paywalled database and report whether the session is live.

    Institutional SSO sessions expire well within a long run, so callers check
    up front rather than discovering expiry as a wall of silent download misses.
    """
    page = context.new_page()
    status: dict[str, bool] = {}
    try:
        for name, url in ACCESS_PROBES.items():
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=60_000)
                wait_past_challenge(page)
                body = page.inner_text("body")[:6000].lower()
                status[name] = any(marker in body for marker in ACCESS_MARKERS[name])
            except Exception as exc:  # noqa: BLE001
                if log:
                    log.warning("%s probe failed: %s", name, exc)
                status[name] = False
            if log:
                log.info("%-24s %s", name, "AUTHENTICATED" if status[name] else "not detected")
    finally:
        page.close()
    return status


@dataclass
class Paper:
    """Normalized record merged across every search source."""

    title: str
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    venue: str | None = None
    doi: str | None = None
    url: str | None = None
    pdf_url: str | None = None
    abstract: str | None = None
    cited_by: int = 0
    is_oa: bool = False
    sources: list[str] = field(default_factory=list)
    openalex_id: str | None = None
    discovery_methods: list[str] = field(default_factory=list)
    forward_citation_of: list[str] = field(default_factory=list)
    backward_reference_of: list[str] = field(default_factory=list)
    snowball_depth: int | None = None
    score: float = 0.0
    score_parts: dict[str, float] = field(default_factory=dict)

    def key(self) -> str:
        """Deduplication key: DOI when present, else a normalized title."""
        if self.doi:
            return self.doi.lower()
        return re.sub(r"[^a-z0-9]+", "", self.title.lower())[:120]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def slugify(text: str, max_len: int = 60) -> str:
    """Filesystem-safe slug used for run folders and PDF filenames."""
    norm = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    norm = re.sub(r"[^\w\s-]", "", norm).strip().lower()
    return re.sub(r"[-\s]+", "-", norm)[:max_len].strip("-") or "untitled"


def reconstruct_abstract(inverted: dict[str, list[int]] | None) -> str | None:
    """OpenAlex returns abstracts as an inverted index; rebuild reading order."""
    if not inverted:
        return None
    positions: list[tuple[int, str]] = [
        (pos, word) for word, spots in inverted.items() for pos in spots
    ]
    if not positions:
        return None
    positions.sort()
    return " ".join(word for _, word in positions)


def paper_from_openalex(
    item: dict[str, Any],
    discovery_method: str = "keyword",
    snowball_depth: int | None = None,
) -> Paper:
    """Normalize one OpenAlex work without coupling callers to its schema."""
    location = item.get("primary_location") or {}
    best_oa = item.get("best_oa_location") or {}
    doi = (item.get("doi") or "").replace("https://doi.org/", "") or None
    openalex_id = (item.get("id") or "").rsplit("/", 1)[-1] or None
    return Paper(
        title=item.get("display_name") or "",
        authors=[
            authorship["author"]["display_name"]
            for authorship in item.get("authorships", [])
            if authorship.get("author", {}).get("display_name")
        ],
        year=item.get("publication_year"),
        venue=(location.get("source") or {}).get("display_name"),
        doi=doi,
        url=item.get("doi") or location.get("landing_page_url"),
        pdf_url=best_oa.get("pdf_url"),
        abstract=reconstruct_abstract(item.get("abstract_inverted_index")),
        cited_by=item.get("cited_by_count", 0),
        is_oa=(item.get("open_access") or {}).get("is_oa", False),
        sources=["openalex"],
        openalex_id=openalex_id,
        discovery_methods=[discovery_method],
        snowball_depth=snowball_depth,
    )


def tokenize(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", (text or "").lower()) if t not in STOPWORDS]


def relevance(paper: Paper, terms: list[str]) -> float:
    """Term coverage over title and abstract, with the title weighted heavier.

    Returns 0.0-1.0. This is a coarse first pass; the agent makes the real
    relevance call after reading abstracts.
    """
    if not terms:
        return 0.0
    title_tokens = set(tokenize(paper.title))
    abstract_tokens = set(tokenize(paper.abstract or ""))
    hits = 0.0
    for term in terms:
        if term in title_tokens:
            hits += 1.0
        elif term in abstract_tokens:
            hits += 0.5
    return min(hits / len(terms), 1.0)


def score_papers(
    papers: Iterable[Paper],
    terms: list[str],
    w_relevance: float = 0.5,
    w_citations: float = 0.3,
    w_recency: float = 0.2,
    half_life_years: float = 4.0,
) -> list[Paper]:
    """Rank by relevance, citation impact, and recency.

    Citations use a log scale so a single 5000-citation classic cannot bury
    everything else. Recency uses exponential decay with a configurable
    half-life, which keeps recent work competitive against older, more-cited
    papers without discarding foundational references.
    """
    papers = list(papers)
    if not papers:
        return []
    max_cites = max(p.cited_by for p in papers) or 1
    this_year = datetime.now(UTC).year
    log_max = math.log1p(max_cites)

    for paper in papers:
        rel = relevance(paper, terms)
        cites = math.log1p(paper.cited_by) / log_max if log_max else 0.0
        if paper.year:
            age = max(this_year - paper.year, 0)
            rec = math.exp(-math.log(2) * age / half_life_years)
        else:
            rec = 0.0
        paper.score_parts = {
            "relevance": round(rel, 4),
            "citations": round(cites, 4),
            "recency": round(rec, 4),
        }
        paper.score = round(
            w_relevance * rel + w_citations * cites + w_recency * rec, 4
        )

    papers.sort(key=lambda p: p.score, reverse=True)
    return papers


def merge(*groups: Iterable[Paper]) -> list[Paper]:
    """Deduplicate across sources, preferring richer records.

    Runs twice: once on the DOI-or-title key, then again on title alone. The
    second pass catches the common case where one source supplies a DOI and
    another does not, which would otherwise leave two keys for one paper.
    """
    merged: dict[str, Paper] = {}
    for group in groups:
        for paper in group:
            _absorb(merged, paper.key(), paper)

    by_title: dict[str, Paper] = {}
    for paper in merged.values():
        _absorb(by_title, re.sub(r"[^a-z0-9]+", "", paper.title.lower())[:120], paper)
    return list(by_title.values())


def _absorb(index: dict[str, Paper], key: str, paper: Paper) -> None:
    existing = index.get(key)
    if existing is None:
        index[key] = paper
        return
    existing.sources = sorted(set(existing.sources) | set(paper.sources))
    existing.discovery_methods = sorted(
        set(existing.discovery_methods) | set(paper.discovery_methods)
    )
    existing.forward_citation_of = sorted(
        set(existing.forward_citation_of) | set(paper.forward_citation_of)
    )
    existing.backward_reference_of = sorted(
        set(existing.backward_reference_of) | set(paper.backward_reference_of)
    )
    existing.cited_by = max(existing.cited_by, paper.cited_by)
    existing.is_oa = existing.is_oa or paper.is_oa
    for attr in (
        "abstract",
        "doi",
        "pdf_url",
        "venue",
        "url",
        "year",
        "openalex_id",
    ):
        if not getattr(existing, attr) and getattr(paper, attr):
            setattr(existing, attr, getattr(paper, attr))
    depths = [depth for depth in (existing.snowball_depth, paper.snowball_depth) if depth]
    existing.snowball_depth = min(depths) if depths else None
    if len(paper.authors) > len(existing.authors):
        existing.authors = paper.authors


def citation_apa(paper: Paper) -> str:
    """APA-style reference string built only from retrieved metadata."""
    if not paper.authors:
        authors = "[No author listed]"
    elif len(paper.authors) == 1:
        authors = paper.authors[0]
    elif len(paper.authors) <= 20:
        authors = ", ".join(paper.authors[:-1]) + ", & " + paper.authors[-1]
    else:
        authors = ", ".join(paper.authors[:19]) + ", ... " + paper.authors[-1]
    year = paper.year or "n.d."
    venue = f" {paper.venue}." if paper.venue else ""
    doi = f" https://doi.org/{paper.doi}" if paper.doi else (f" {paper.url}" if paper.url else "")
    return f"{authors} ({year}). {paper.title}.{venue}{doi}".strip()


def citation_bibtex(paper: Paper, key: str) -> str:
    fields = [f"  title = {{{paper.title}}}"]
    if paper.authors:
        fields.append("  author = {" + " and ".join(paper.authors) + "}")
    if paper.year:
        fields.append(f"  year = {{{paper.year}}}")
    if paper.venue:
        fields.append(f"  booktitle = {{{paper.venue}}}")
    if paper.doi:
        fields.append(f"  doi = {{{paper.doi}}}")
    if paper.url:
        fields.append(f"  url = {{{paper.url}}}")
    return "@inproceedings{" + key + ",\n" + ",\n".join(fields) + "\n}"


def run_dir(base: Path, topic: str) -> Path:
    """Create the per-run folder layout and return its root."""
    root = base / f"{datetime.now(UTC):%Y%m%d}-{slugify(topic, 40)}"
    for sub in ("pdfs", "text"):
        (root / sub).mkdir(parents=True, exist_ok=True)
    return root


def load_papers(path: Path) -> list[Paper]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Paper(**item) for item in data["papers"]]


def save_papers(path: Path, topic: str, papers: list[Paper], **meta: Any) -> None:
    path.write_text(
        json.dumps(
            {
                "topic": topic,
                "generated": datetime.now(UTC).date().isoformat(),
                **meta,
                "papers": [p.to_dict() for p in papers],
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
