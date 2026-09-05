---
name: topic-ideation
description: "Systematic dissertation-topic ideation across the generative-AI and agentic landscape: OpenAlex and arXiv area scans with momentum metrics, rubric-scored candidate research questions, and a handoff to publications-search for the saturated review. - Brought to you by dave/phd"
argument-hint: "[areas=a; b; c] [from-year=...]"
---

# Topic Ideation

Evaluates compelling alternative dissertation topics beyond the current one
(multi-agent software development), with emphasis on LLM agents for business —
the student's professional domain. The scanner handles the mechanical work:
volumes, venues, key papers, and fresh preprints per area. The agent supplies
the judgment: reading the landscape, drafting falsifiable research questions,
and scoring each against a fixed rubric.

API-only: no browser, no institutional session, no Playwright.

## Overview

| Stage | Who | Output |
|---|---|---|
| 1. Scan the landscape | `scan.py` | `landscape.json`, `landscape.md` |
| 2. Draft and score candidates | Agent + [RUBRIC.md](./references/RUBRIC.md) | 5-10 rubric-scored research questions |
| 3. Write the shortlist | Agent | `ideas.md` in the run folder |
| 4. Deep-dive the winners | publications-search skill | One self-contained review run per candidate |

Run folder layout:

```text
results/YYYYMMDD-ideation-<slug>/
├── landscape.json   # raw per-area data: volumes, venues, works, arXiv feed
├── landscape.md     # one comparison card per area, momentum overview first
└── ideas.md         # Stage 3 shortlist; template in references/RUBRIC.md
```

## Prerequisites

- `uv` on `PATH` (`~/.local/bin`). The script declares its own dependencies inline.
- Optional: `export CONTACT_EMAIL=you@example.com` to enter the OpenAlex polite pool.

## Quick Start

```bash
cd /home/davesee/repos/dave/phd
export PATH="$HOME/.local/bin:$PATH"
T=.github/skills/topic-ideation/scripts

# Scan the 12 default seed areas (references/SEED-AREAS.md)
RUN=$(uv run $T/scan.py --from-year 2022 | tail -1)

# Or scan ad-hoc areas without touching the seed file
uv run $T/scan.py --areas "LLM agents for financial compliance; GUI agents for claims processing"
```

## Parameters Reference

### scan.py

| Parameter | Default | Purpose |
|---|---|---|
| `--areas` | none | Semicolon-separated ad-hoc area queries; overrides the seed file |
| `--areas-file` | `references/SEED-AREAS.md` | Markdown file whose H2 headings name the areas |
| `--from-year` | `2022` | Earliest publication year for volumes and work lists |
| `--per-area` | `15` | Top-cited and most-recent works fetched per area |
| `--out` | `results` | Base folder for ideation run directories |
| `--delay` | `1.0` | Seconds between API calls; arXiv calls keep at least 3 s internally |

## Agent Workflow

### Stage 1: Scan

Mechanical. For each area, `scan.py` collects from OpenAlex the publication
volume by year, top venues, top-cited works, and most-recent works, plus the
freshest arXiv submissions. Momentum compares the last full year's volume
against the year before it; the current year is partial and never enters the
ratio. A failing endpoint degrades only its own area — check the per-area
`errors` list in `landscape.json` before trusting a thin card.

### Stage 2: Draft and score candidates

Read `landscape.md` in full, then [RUBRIC.md](./references/RUBRIC.md). Draft
5-10 candidate research questions with a complete rubric score table each.
Rules:

- Every volume, venue, or momentum claim must trace to `landscape.json`.
- OpenAlex full-text search is broad: a key-papers table can carry off-topic
  high-citation matches. Discount them; never cite a paper whose title does
  not plausibly belong to the area.
- Cite at least two scanned papers by DOI per candidate. arXiv entries are
  grey literature: momentum signals, never refereed anchors (criterion 4).
- A candidate may fuse two areas when the scan shows they intersect; say
  which cards support the fusion.
- Park any candidate scoring 0-1 on a single criterion, whatever its total.

### Stage 3: Write the shortlist

Write `ideas.md` into the ideation run folder using the template at the end
of [RUBRIC.md](./references/RUBRIC.md): per candidate — research question,
why-now, expected experiment shape, business relevance, rubric score table,
and a ready-to-run publications-search command with suggested `--from-year`
and `--sources`.

### Stage 4: Hand off the winners

Take the top one or two candidates by total score into the
[publications-search skill](../publications-search/SKILL.md) for a full
saturation-bounded review, using the command written in each candidate's
card. That command preregisters the protocol first and then pins the search to
the same folder with `--run-dir`, because `protocol.py` and `search.py` derive
their own run folders from whatever string each is given and would otherwise
split one review across two directories. The candidate's research question
belongs in `protocol.md`; the search itself gets a keyword phrase, since a
question's qualifiers dilute the terms that carry the topic.

Each deep-dive run is self-contained under its own `results/<run>/`
folder with its own `thesis.md` and rendered `.docx`; follow the
publications-search `SKILL.md` for the pipeline and its
[THESIS-TEMPLATE.md](../publications-search/references/THESIS-TEMPLATE.md)
for the document structure. Ideation runs and review runs never share a
folder — the ideation trail stays intact as evidence of how the topic was
chosen.

## Access and Conduct

- Calls are serial with polite delays; arXiv gets at least 3 seconds between
  requests. Do not loop scans to poll for changes — the landscape moves
  weekly, not hourly.
- Never fabricate metadata. Every DOI, citation count, venue, and volume in
  `ideas.md` comes from `landscape.json` verbatim; anything else must be
  verified in a publications-search run before it is written down.
- Scanner citation counts and venue lists are ranking signals, not
  dissertation-grade citations. The publications-search pipeline re-verifies
  everything that survives to a review.
- `landscape.md` and `ideas.md` are working material and audit evidence, not
  submission prose. NSU's Certification of Authorship requires disclosing
  skill assistance; anything entering a submitted document is rewritten in
  the student's own words.

> Brought to you by dave/phd
