# Publications-Search Skill Review — 2026-08-30

> **Implementation status (2026-09-03):** all four roadmap tiers below are
> implemented. A1 (author hygiene + provenance-aware merge), A2 (APA-7 names,
> typed/escaped BibTeX, collision-safe keys), A3 (key+title identity binding
> in `screen.py merge` and `resolve_abstracts.py`), A4 (`search-log.json` +
> `dedup-log.json`); methodology row fixes: `protocol.py` (Stage 0 +
> known-item check), `prisma.py`, full-text exclusion reasons
> (`fulltext-exclusions.json`), `quality.py` (Kitchenham + Garousi),
> `screen.py sample`/`kappa` (Cohen's kappa human validation), structured
> extraction form + `read_order` novelty + `--window-sweep` in
> `saturation.py`, arXiv as a first-class source, `crosscheck.py`,
> `annotated_bib.py`, snowball retry/partial-save/truncation flags,
> reproducible scoring metadata, interrupt-safe `fetch_pdfs.py`/`resolve_abstracts.py`.
> **Not verifiable offline:** the corrected ACM/IEEE DOM selectors and the
> authenticated fetch paths need one live institutional session to confirm.
> **Known live-run artifact:** `references.bib` in the 2026-08-30 run predates
> the fixes (e.g. the authorless `anon2026` entry crosscheck.py flagged);
> re-running `extract.py` on that run regenerates manifest citations from the
> repaired code.

Comprehensive review of the skill against (a) its own code, (b) established
systematic-review methodology, and (c) NSU's dissertation process
(`dissertation-guide.pdf`). Produced by a multi-agent review: one agent read
every script line-by-line, one compared the pipeline against published SLR
standards (with 2025–2026 web sources), and one mapped every skill artifact
onto the NSU Idea Paper / Proposal / Report requirements and the Appendix L
rubric. Findings verified against the live run
`results/20260830-specialized-multi-agent-versus-single-ag/`.

## What the skill already does well

- **Complete-corpus abstract screening** (every candidate, not a top-N cut) is
  *stronger* than ASReview-style active-learning partial screening — no recall
  estimation needed. State this explicitly in the methods chapter.
- **Auditable decision trail**: per-record screening decisions with rationale,
  citation edges with anchor + direction (Wohlin-faithful), preserved baseline
  snapshots, page-anchored quotes with anti-fabrication rules.
- **Saturation stopping rule is defensible** — it mirrors Guest, Bunce &
  Johnson's (2006) base-size/run-length design and modern stopping heuristics
  (SAFE; Boetje & van de Schoot 2024) — but must be framed as a
  *saturation-bounded* systematic review, never as exhaustive Kitchenham-style
  coverage. See "Methodology alignment" below for the required documentation.
- More transparent than Elicit / ResearchRabbit / Connected Papers workflows;
  DOI-first two-pass dedup matches current best practice.

## A. Script defects (highest impact first)

### A1. Citation metadata pollution — root cause chain (HIGH)
1. `scripts/search.py:250` scrapes ACM authors with the over-broad selector
   `ul.rlist--inline li a`, which also matches ACM's result-item toolbar —
   injecting `"Highlights"`, `"AI Summary"`, `"Get Access"`, and empty strings
   into `Paper.authors` (selector documented at `references/SOURCES.md:96`).
   Every junk-authored record in the live manifest has `acm` in `sources`.
2. `scripts/_common.py:348-349` merges with "longer author list wins", so the
   junk-padded ACM list *overwrites* clean Crossref/OpenAlex authors.
3. `scripts/search.py:300,347` enrichment only backfills *empty* author lists,
   so a contaminated list is never repaired; it flows verbatim into
   `citation_apa` (`_common.py:352-365`) and `bibtex` (`_common.py:368-380`).

**Fix**: scope the selector (`ul.rlist--inline.loa li a` or href contains
`/profile/`); add `clean_authors()` in `_common.py` (drop empties,
non-alphabetic entries, denylist {highlights, ai summary, get access, …});
track author provenance and prefer OpenAlex/Crossref authorship over scraped
DOM regardless of length; overwrite scraped authors on DOI resolution.
Manifest typos confirmed in the live run: "Zhenyy Mao" (→ Zhenyu Mao, order 32),
"Yu Ge" (→ Ge Yu, order 36), year=null + junk authors (order 43/44).

### A2. BibTeX / APA output is not dissertation-grade (HIGH)
- `_common.py:368-380` hardcodes `@inproceedings` + `booktitle` for everything
  — journal articles (e.g., MDPI *Software*, doi 10.3390/software5020026) and
  arXiv preprints included. Crossref `type` is fetched (`search.py:115`) then
  discarded; volume/issue/pages/publisher dropped (`search.py:126-142`).
- APA names are not inverted (`Junda He` should be `He, J.`), and NSU grades
  APA compliance (rubric item 18).
- `extract.py:70` `bibtex_key` crashes (IndexError) on an empty first author;
  surname+year keys have no collision handling (duplicate keys break LaTeX).

**Fix**: keep structured given/family names; emit `@article` / `@inproceedings`
/ `@misc`+eprint by work type; escape BibTeX specials; dedupe keys with
a/b/c suffixes; generate an APA-7 `references.md` (inverted names, volume,
issue, pages, DOI URL) alongside `references.bib`.

### A3. Positional-rank identity binding can corrupt decisions (HIGH)
`resolve_abstracts.py:178-183` and `screen.py:224-241` bind records by rank
only. Ranks are frozen at the last `screen.py init`, but `candidates.json` is
re-ranked by every snowball run — an intervening re-rank silently writes
abstracts/decisions onto the *wrong papers*. **Fix**: match by record `key` +
normalized-title check; abort loudly on mismatch.

### A4. PRISMA-critical data lives only in console logs (HIGH)
Per-source hit counts (`search.py:445,473`), the condensed ACM/IEEE query
(`search.py:455`), dedup-merge counts, `--per-source`/`--from-year` — none are
persisted. A PRISMA 2020 flow diagram cannot be reconstructed from the run
folder. **Fix**: write `search-log.json` (query-as-sent per source, interface,
date-time, raw n, dedup n, parameters) and a `dedup-log.json` of merge events.

### Medium/low findings (summary)
- ACM citation-count scrape can capture a year (e.g. 2024) as `cited_by`,
  inflating rank scores (`search.py:243-246`).
- Preprint/published title-merge creates chimera records; no `is_preprint`
  flag despite SKILL.md requiring preprints be labelled (`_common.py:300-345`).
- Snowball loses all fetched data on one HTTP failure (no retry/partial save,
  `snowball.py:85-91,241-298`); `resolve_abstracts`/`fetch_pdfs` don't persist
  state on interrupt.
- Scores are irreproducible: recency uses `datetime.now()` year; citation
  normalizer rescales with corpus max; neither is logged (`_common.py:275-294`).
- Recovered abstracts are never rescored (`resolve_abstracts.py:236-239`).
- Silent 60-record enrichment cap (`search.py:293-300`).
- Saturation novelty computed in corpus order, not read order
  (`saturation.py:171-185,219-226`) — record a `read_sequence` and evaluate the
  window over it.
- Schema drift: `evidence_notes` str-vs-dict; `extract.py` prefers stale
  `retrieved.json`; `Paper(**item)` crashes on extra keys.
- Screening audit: superseded decisions silently dropped on re-init; no
  per-decision timestamps (`screen.py:65-139`).
- Scholar cited-by/year parse fragility; fetch guard bypassable via absolute
  `--input` path.

## B. Methodology alignment (Kitchenham / PRISMA / Wohlin / AI-assist)

| Standard | Status | Required change |
|---|---|---|
| Kitchenham protocol | **Missing** | Stage 0 `protocol.md` written *before* search: verbatim RQs, per-source strategy, testable inclusion/exclusion criteria, the 20 evidence domains, saturation rule + parameters. Stamp its hash into `screening.json`. |
| PRISMA 2020 flow | **Not reconstructible** | `search-log.json` + `dedup-log.json` + a full-text exclusion stage (with reason enum) + a `prisma.py` that emits the four-phase counts/diagram. |
| Quality assessment | **Missing entirely** | Per-core-paper checklist (Kitchenham 5–8 questions, 0/0.5/1) + Garousi grey-literature criteria for preprints → `quality.json`; weight synthesis claims by rigor. The most common committee criticism of SE SLRs. |
| Saturation rule | **Defensible if documented** | Call it a "saturation-bounded systematic review"; cite Guest et al. 2006 + SAFE (Boetje & van de Schoot 2024); preregister domains; report both novelty curves + window sensitivity sweep; list unread papers as a limitation. |
| AI-use disclosure (RAISE / PRISMA-trAIce / ELEVATE-GenAI) | **Missing** | Human validation: independently screen a 10–20% stratified sample, report Cohen's kappa (target ≥ 0.8), escalate disagreement categories; add an "AI use" section (model, version, prompts, stages) to review.md. Converts the skill's biggest liability into a methodological contribution. |
| PRISMA-S search reporting | Partial | Per-source query overrides + persist query-as-sent; validate with a preregistered known-item list (5–10 papers the search must find). |
| Wohlin snowballing | Deviates | Either iterate rounds to zero-new-includes closure, or *document* the concept-bounded variant as a cited deviation; log forward-limit truncation. |
| Data extraction form | Free-form | Fixed schema per read paper: {study_type, framework, agent_count/topology, benchmark, baseline, key results, limitations, venue_type, quality_score} → enables Ch2 evidence tables. |
| Grey literature (Garousi) | Indirect | Add arXiv native API (cs.SE/cs.AI/cs.MA) as a first-class source; reconcile arXiv↔publisher DOIs; grey-specific quality criteria in QA stage. |
| Ranking vs ASReview | **Strength** | Position ranking as screening *prioritization* only (100% of abstracts screened — stronger than partial screening); post-hoc check: where did final core papers sit in the initial ranking? |

## C. NSU dissertation alignment (Idea Paper → Proposal → Report)

Artifact-to-deliverable mapping and gaps (Appendix L rubric items in parens):

| NSU section | Feeds from | Gap / needed transformation |
|---|---|---|
| Idea Paper: Problem Statement (items 6, 10) | evidence-ledger notes, review.md gaps | Tag evidence to the required frame — *what / why / how it evolved / precipitating events* — and render `problem-map.md` with page-anchored quotes. |
| Idea Paper: Goal | review.md precedent papers | Student-authored; skill supplies cited precedents of similar solutions. |
| Idea Paper: Relevance & Significance | supports/rejects + gaps sections | Reframe as scope / why-a-problem / why-solution-promises / knowledge-base contribution. |
| Idea Paper: Approach (items 13, 14) | — | Add per-paper methods extraction → `methods-matrix.md` (design, benchmark, metrics, threats). |
| Idea Paper: Resources | text/ corpus | Aggregate tools/benchmarks/models named by comparable studies → `resources-inventory.md`. |
| Idea Paper: References (items 9, 18) | references.bib, citation_apa | Fix A1/A2; emit APA-7 `references.md`; add `crosscheck.py`: every citation referenced and every reference cited (NSU states this requirement twice). |
| Proposal Ch2 | review.md | Restructure Stage 7 template to NSU Ch2 headings: domain-organized overview, criteria justification with funnel counts, strengths/weaknesses per theme, methods-validity analysis, gaps, synthesis; demote per-paper list to an appendix. |
| Rubric item 8 | screening rationale + ledger notes + citations | Generate `annotated-bibliography.md` (near-zero marginal effort, directly graded). |
| Rubric self-check | all artifacts | `rubric-selfcheck.md`: one row per Appendix L item → evidencing artifact, with explicit "student action required" markers for items 1, 11, 15–17, 20. |
| Report-stage refresh | screen.py init preserves decisions | Document the incremental refresh recipe (re-search with `--from-year`, re-init, re-check saturation, changelog). |
| Certification of Authorship | — | SKILL.md conduct note: skill-generated prose/judgments are *assistance* that NSU requires disclosing; artifacts are working material + audit evidence, not submission text. |

## D. Prioritized roadmap

1. **Now (blocks citation quality)**: A1 author hygiene + A2 BibTeX/APA typing
   + `crosscheck.py` citation↔reference completeness.
2. **Before the next run (blocks methods-chapter defensibility)**: Stage 0
   `protocol.md`; `search-log.json`/`dedup-log.json`; full-text exclusion
   reasons; A3 key-based identity binding.
3. **Before the Proposal**: quality-assessment stage; structured extraction
   form; NSU-Ch2 review.md template; annotated bibliography + rubric
   self-check + problem-map generators; human-validation kappa sample; arXiv
   source.
4. **Opportunistic**: robustness fixes (snowball retry, interrupt-safe saves),
   reproducible scoring, saturation read-order fix, refresh recipe docs.

*Scripts were reviewed but deliberately not modified: several fixes (ACM/IEEE
DOM selectors, browser flows) can only be validated against live institutional
sessions. All findings above carry file:line locations so each can be applied
and tested in isolation.*
