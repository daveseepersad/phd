"""Shared helpers for the publications-search skill.

Ranking, metadata normalization, and on-disk layout for a review run.
"""
from __future__ import annotations

import json
import math
import os
import re
import time
import unicodedata
from collections.abc import Iterable
from dataclasses import asdict, dataclass, field
from dataclasses import fields as dataclass_fields
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

STOPWORDS = frozenset(
    ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "have", "how", "in", "is", "it", "its", "of", "on", "or", "that", "the", "to", "was", "were", "what", "when", "where", "which", "who", "why", "with", "using", "use", "can", "could", "do", "does"]
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
    # Bibliographic typing for dissertation-grade citations (REVIEW.md A2).
    work_type: str | None = None  # Crossref/OpenAlex type, e.g. journal-article
    volume: str | None = None
    issue: str | None = None
    pages: str | None = None
    publisher: str | None = None
    is_preprint: bool = False
    # Author provenance (REVIEW.md A1): "api" (OpenAlex/Crossref/arXiv) beats
    # "scraped" (publisher DOM) regardless of list length.
    authors_source: str | None = None

    def key(self) -> str:
        """Deduplication key: DOI when present, else a normalized title."""
        if self.doi:
            return self.doi.lower()
        return re.sub(r"[^a-z0-9]+", "", self.title.lower())[:120]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, item: dict[str, Any]) -> Paper:
        """Load a record while tolerating unknown keys from older/newer schemas."""
        known = {f.name for f in dataclass_fields(cls)}
        return cls(**{k: v for k, v in item.items() if k in known})


# Toolbar/UI tokens that publisher DOMs inject next to author names.
AUTHOR_DENYLIST = frozenset(
    {
        "highlights", "ai summary", "get access", "abstract", "full text",
        "pdf", "epub", "references", "cited by", "index terms", "comments",
        "supplemental material", "media", "share", "tools", "author picks",
        "see all", "no access", "open access", "free access", "check for updates",
    }
)


def clean_authors(names: Iterable[str] | None) -> list[str]:
    """Drop toolbar junk, empties, and duplicates from a scraped author list."""
    cleaned: list[str] = []
    seen: set[str] = set()
    for raw in names or []:
        name = re.sub(r"\s+", " ", (raw or "")).strip(" ,;·|")
        low = name.lower()
        if not name or low in AUTHOR_DENYLIST or low in seen:
            continue
        # A personal name must contain at least one letter (any major script).
        if not re.search(r"[^\W\d_]", name, re.UNICODE):
            continue
        seen.add(low)
        cleaned.append(name)
    return cleaned


PREPRINT_MARKERS = ("arxiv", "ssrn", "research square", "researchsquare", "preprints.org", "biorxiv", "techrxiv", "osf preprints")


def looks_preprint(paper: Paper) -> bool:
    """Detect preprint hosting from DOI prefix or venue.

    Deliberately ignores url/pdf_url: published papers routinely carry a
    green-OA arXiv copy as their best OA location, and flagging those would
    demote peer-reviewed work to preprint citations.
    """
    if (paper.doi or "").startswith(("10.48550", "10.2139", "10.21203", "10.36227")):
        return True
    return any(marker in (paper.venue or "").lower() for marker in PREPRINT_MARKERS)


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
    biblio = item.get("biblio") or {}
    doi = (item.get("doi") or "").replace("https://doi.org/", "") or None
    openalex_id = (item.get("id") or "").rsplit("/", 1)[-1] or None
    first_page, last_page = biblio.get("first_page"), biblio.get("last_page")
    pages = f"{first_page}-{last_page}" if first_page and last_page else first_page
    paper = Paper(
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
        work_type=item.get("type"),
        volume=biblio.get("volume"),
        issue=biblio.get("issue"),
        pages=pages,
        publisher=(location.get("source") or {}).get("host_organization_name"),
        authors_source="api" if item.get("authorships") else None,
    )
    # Explicit version signals win; publishedVersion is authoritative, so a
    # green-OA arXiv copy never demotes the published record to a preprint.
    if location.get("version") == "submittedVersion" or item.get("type") == "preprint":
        paper.is_preprint = True
    elif location.get("version") == "publishedVersion":
        paper.is_preprint = False
    else:
        paper.is_preprint = looks_preprint(paper)
    return paper


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
    reference_year: int | None = None,
    scoring_meta: dict[str, Any] | None = None,
) -> list[Paper]:
    """Rank by relevance, citation impact, and recency.

    Citations use a log scale so a single 5000-citation classic cannot bury
    everything else. Recency uses exponential decay with a configurable
    half-life, which keeps recent work competitive against older, more-cited
    papers without discarding foundational references.

    Scores depend on the evaluation year and the corpus citation maximum. Pass
    ``reference_year`` to reproduce a historical ranking, and a ``scoring_meta``
    dict to capture both values for persistence alongside the ranked output.
    """
    papers = list(papers)
    if not papers:
        return []
    max_cites = max(p.cited_by for p in papers) or 1
    this_year = reference_year or datetime.now(UTC).year
    log_max = math.log1p(max_cites)
    if scoring_meta is not None:
        scoring_meta.update({"reference_year": this_year, "corpus_max_citations": max_cites})

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


def merge(*groups: Iterable[Paper], events: list[dict[str, Any]] | None = None) -> list[Paper]:
    """Deduplicate across sources, preferring richer records.

    Runs twice: once on the DOI-or-title key, then again on title alone. The
    second pass catches the common case where one source supplies a DOI and
    another does not, which would otherwise leave two keys for one paper.

    When ``events`` is a list, one entry per absorbed duplicate is appended so
    callers can persist a PRISMA-grade dedup log.
    """
    merged: dict[str, Paper] = {}
    for group in groups:
        for paper in group:
            _absorb(merged, paper.key(), paper, events=events, pass_name="doi-or-title")

    by_title: dict[str, Paper] = {}
    for paper in merged.values():
        _absorb(
            by_title,
            re.sub(r"[^a-z0-9]+", "", paper.title.lower())[:120],
            paper,
            events=events,
            pass_name="title-only",
        )
    return list(by_title.values())


def _author_rank(source: str | None) -> int:
    return {"api": 2, "scraped": 1}.get(source or "", 0)


def _absorb(
    index: dict[str, Paper],
    key: str,
    paper: Paper,
    events: list[dict[str, Any]] | None = None,
    pass_name: str = "",
) -> None:
    existing = index.get(key)
    if existing is None:
        index[key] = paper
        return
    if events is not None:
        events.append(
            {
                "pass": pass_name,
                "kept_key": existing.key(),
                "kept_title": existing.title,
                "absorbed_title": paper.title,
                "absorbed_sources": paper.sources,
                "absorbed_doi": paper.doi,
            }
        )
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
        "work_type",
        "volume",
        "issue",
        "pages",
        "publisher",
    ):
        if not getattr(existing, attr) and getattr(paper, attr):
            setattr(existing, attr, getattr(paper, attr))
    depths = [depth for depth in (existing.snowball_depth, paper.snowball_depth) if depth]
    existing.snowball_depth = min(depths) if depths else None
    # A False is_preprint may only mean "unknown" (metadata-poor sources never
    # set it). After the backfill above, keep the flag from either side unless
    # the merged record shows publication evidence: a published work type, or
    # a venue that is not a preprint host.
    if existing.is_preprint or paper.is_preprint:
        published_evidence = existing.work_type in _PUBLISHED_WORK_TYPES or bool(
            existing.venue
            and not any(marker in existing.venue.lower() for marker in PREPRINT_MARKERS)
        )
        existing.is_preprint = not published_evidence
    # API-sourced authorship beats scraped DOM lists regardless of length
    # (REVIEW.md A1: "longer list wins" let toolbar junk overwrite clean lists).
    incoming, current = _author_rank(paper.authors_source), _author_rank(existing.authors_source)
    if paper.authors and (
        not existing.authors
        or incoming > current
        or (incoming == current and len(paper.authors) > len(existing.authors))
    ):
        existing.authors = paper.authors
        existing.authors_source = paper.authors_source


# Surname particles that belong to the family name, not the given names:
# "Ludwig van Beethoven" -> "van Beethoven, L.", never "Beethoven, L. V.".
_NAME_PARTICLES = frozenset(
    ["van", "von", "de", "der", "den", "dem", "di", "da", "del", "della", "dos", "du", "la", "le", "ter", "ten", "op", "af", "bin", "ibn", "al"]
)


def apa_name(name: str) -> str:
    """Invert one personal name to APA form: 'Junda He' -> 'He, J.'."""
    # Parenthetical nicknames ("Robert (Bob) Smith") never become initials.
    name = re.sub(r"\s+", " ", re.sub(r"\([^)]*\)", " ", name)).strip()
    if not name:
        return name
    if "," in name:  # already inverted
        family, _, given = (part.strip() for part in name.partition(","))
    else:
        parts = name.split(" ")
        if len(parts) == 1:
            return parts[0]
        split_at = len(parts) - 1
        while split_at > 1 and parts[split_at - 1].lower() in _NAME_PARTICLES:
            split_at -= 1
        family, given = " ".join(parts[split_at:]), " ".join(parts[:split_at])
    initials: list[str] = []
    for token in given.split(" "):
        if not token:
            continue
        # Hyphenated given names keep the hyphen: Jean-Paul -> J.-P.
        initials.append("-".join(f"{sub[0].upper()}." for sub in token.split("-") if sub))
    return f"{family}, {' '.join(initials)}" if initials else family


def citation_apa(paper: Paper) -> str:
    """APA-7 reference string built only from retrieved metadata.

    Authors are cleaned here as well as at scrape time, so citations stay
    junk-free even for legacy corpora that predate the hygiene fixes.
    """
    names = [apa_name(n) for n in clean_authors(paper.authors)]
    if not names:
        authors = "[No author listed]"
    elif len(names) == 1:
        authors = names[0]
    elif len(names) <= 20:
        authors = ", ".join(names[:-1]) + ", & " + names[-1]
    else:  # APA 7: first 19, ellipsis, final author, no ampersand
        authors = ", ".join(names[:19]) + ", ... " + names[-1]
    year = paper.year or "n.d."
    source = ""
    if paper.venue:
        source = f" {paper.venue}"
        if paper.volume:
            source += f", {paper.volume}"
            if paper.issue:
                source += f"({paper.issue})"
        if paper.pages:
            source += f", {paper.pages}"
        source += "."
    doi = f" https://doi.org/{paper.doi}" if paper.doi else (f" {paper.url}" if paper.url else "")
    return f"{authors} ({year}). {paper.title}.{source}{doi}".strip()


# BibTeX special characters that break compilation when unescaped. Braces are
# left alone: titles legitimately contain protective {...} groups.
_BIBTEX_ESCAPES = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_"}


def bibtex_escape(text: str) -> str:
    return re.sub(r"(?<!\\)([&%$#_])", lambda m: _BIBTEX_ESCAPES[m.group(1)], text)


_PROCEEDINGS_HINTS = ("proceedings", "conference", "symposium", "workshop", "meeting", "congress")
_JOURNAL_TYPES = {"journal-article", "article"}
_PROCEEDINGS_TYPES = {"proceedings-article", "conference-paper", "proceedings"}
_PUBLISHED_WORK_TYPES = _JOURNAL_TYPES | _PROCEEDINGS_TYPES | {"book", "monograph", "book-chapter", "book-section"}


def bibtex_entry_type(paper: Paper) -> str:
    """Choose the entry type from work_type, falling back to venue heuristics."""
    if paper.is_preprint:
        return "misc"
    if paper.work_type in _JOURNAL_TYPES:
        return "article"
    if paper.work_type in _PROCEEDINGS_TYPES:
        return "inproceedings"
    if paper.work_type in {"book", "monograph"}:
        return "book"
    if paper.work_type in {"book-chapter", "book-section"}:
        return "incollection"
    if not paper.venue:
        return "misc"
    if any(hint in paper.venue.lower() for hint in _PROCEEDINGS_HINTS):
        return "inproceedings"
    return "article"


def _arxiv_id(paper: Paper) -> str | None:
    if (paper.doi or "").startswith("10.48550/"):
        # OpenAlex lowercases DOIs ("10.48550/arxiv.NNNN"), Crossref does not.
        return re.sub(r"^arxiv\.", "", paper.doi.split("/", 1)[1], flags=re.IGNORECASE)
    match = re.search(r"arxiv\.org/(?:abs|pdf)/([\w.]+?)(?:v\d+)?(?:$|[?\s])", f"{paper.url or ''} {paper.pdf_url or ''}")
    return match.group(1) if match else None


def citation_bibtex(paper: Paper, key: str) -> str:
    """Emit a type-correct BibTeX entry (REVIEW.md A2)."""
    entry = bibtex_entry_type(paper)
    fields = [f"  title = {{{bibtex_escape(paper.title)}}}"]
    authors = clean_authors(paper.authors)
    if authors:
        fields.append("  author = {" + " and ".join(bibtex_escape(a) for a in authors) + "}")
    if paper.year:
        fields.append(f"  year = {{{paper.year}}}")
    if paper.venue:
        venue_field = "journal" if entry == "article" else "booktitle" if entry in {"inproceedings", "incollection"} else "howpublished" if entry == "misc" and not paper.is_preprint else None
        if venue_field:
            fields.append(f"  {venue_field} = {{{bibtex_escape(paper.venue)}}}")
    if entry == "article":
        if paper.volume:
            fields.append(f"  volume = {{{paper.volume}}}")
        if paper.issue:
            fields.append(f"  number = {{{paper.issue}}}")
    if paper.pages and entry in {"article", "inproceedings", "incollection"}:
        fields.append(f"  pages = {{{paper.pages}}}")
    if paper.publisher and entry in {"inproceedings", "incollection", "book"}:
        fields.append(f"  publisher = {{{bibtex_escape(paper.publisher)}}}")
    arxiv = _arxiv_id(paper) if paper.is_preprint else None
    if arxiv:
        fields.append(f"  eprint = {{{arxiv}}}")
        fields.append("  archivePrefix = {arXiv}")
    elif paper.is_preprint and paper.venue:
        fields.append(f"  howpublished = {{{bibtex_escape(paper.venue)}}}")
    if paper.is_preprint:
        fields.append("  note = {Preprint}")
    if paper.doi:
        fields.append(f"  doi = {{{paper.doi}}}")
    if paper.url:
        fields.append(f"  url = {{{paper.url}}}")
    return f"@{entry}{{{key},\n" + ",\n".join(fields) + "\n}"


def make_bibtex_key(paper: Paper, used: set[str]) -> str:
    """Surname+year key with a/b/c collision suffixes; never crashes on empty authors."""
    surname = ""
    if paper.authors:
        first = clean_authors(paper.authors[:1])
        if first:
            surname = re.sub(r"[^a-z]", "", apa_name(first[0]).split(",")[0].lower())
    if not surname:
        surname = re.sub(r"[^a-z]", "", paper.title.lower())[:12] or "anon"
    base = f"{surname}{paper.year or 'nd'}"
    key = base
    suffix_index = 0
    while key in used:
        # Bijective base-26 suffix: a..z, aa, ab, ... — unbounded, so heavy
        # surname+year collisions (li2025 et al.) can never loop forever.
        suffix_index += 1
        n, suffix = suffix_index, ""
        while n:
            n, remainder = divmod(n - 1, 26)
            suffix = chr(ord("a") + remainder) + suffix
        key = base + suffix
    used.add(key)
    return key


def run_dir(base: Path, topic: str) -> Path:
    """Create the per-run folder layout and return its root."""
    root = base / f"{datetime.now(UTC):%Y%m%d}-{slugify(topic, 40)}"
    for sub in ("pdfs", "text"):
        (root / sub).mkdir(parents=True, exist_ok=True)
    return root


def load_papers(path: Path) -> list[Paper]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Paper.from_dict(item) for item in data["papers"]]


def write_json_atomic(path: Path, payload: Any) -> None:
    """Write via a sibling temp file + rename, so an interrupt mid-write can
    never leave truncated JSON behind (callers persist incrementally)."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, path)


def save_papers(path: Path, topic: str, papers: list[Paper], **meta: Any) -> None:
    write_json_atomic(
        path,
        {
            "topic": topic,
            "generated": datetime.now(UTC).date().isoformat(),
            **meta,
            "papers": [p.to_dict() for p in papers],
        },
    )
