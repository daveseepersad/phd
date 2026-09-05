# PhD-Worthiness Rubric

Score every candidate research question on six criteria, 0-5 each, after the
Stage 1 scan. Ground each score in scanned evidence: momentum numbers from
`landscape.json` and named papers (with DOIs) from the key-papers tables.
A score justified only by intuition is a guess, not a score.

Interpretation:

- **24-30**: strong candidate; hand to publications-search for a full review.
- **18-23**: workable, but reframe the weakest criterion before investing.
- **Below 18, or any single criterion at 0-1**: park it. A single fatal
  criterion (no refereed anchors, untractable experiment) sinks the total no
  matter how exciting the area feels.

## 1. Problem clarity

Documented, unresolved disagreement or gap in the refereed literature — not a
technology enthusiasm.

| Score | Descriptor |
|---:|---|
| 0 | No identifiable problem; the area is a technology description, not a question. |
| 1 | Vague dissatisfaction ("agents are unreliable") with no literature trace. |
| 2 | Gap asserted only in preprints or industry posts; no refereed source names it. |
| 3 | At least one refereed paper names the gap, but the framing is broad and not falsifiable as stated. |
| 4 | Multiple refereed papers document the same unresolved gap or disagreement; a falsifiable question fits in one sentence. |
| 5 | Documented head-to-head disagreement or an explicitly declared open problem in refereed work, with named papers on each side and a precise testable claim. |

## 2. Experimental tractability (solo PhD)

A controlled experiment one student can design, build, and run — commodity
hardware, hosted model APIs, public artifacts.

| Score | Descriptor |
|---:|---|
| 0 | Requires industrial deployment access, proprietary data, or a research team. |
| 1 | Feasible only with frontier-scale training runs or months of unbounded API spend. |
| 2 | An experiment is conceivable, but confounds (model drift, task leakage, human variance) are hard to isolate alone. |
| 3 | A controlled design is statable; infrastructure is buildable in weeks, though some instruments must be built from scratch. |
| 4 | Clear treatment/control design over public benchmarks or reproducible harnesses, within a modest API budget. |
| 5 | The full experiment matrix (conditions x tasks x repetitions) is enumerable today from public artifacts, and a power analysis is possible before building anything. |

## 3. Measurable direct outcomes

Benchmarks and metrics exist, so the dissertation reports numbers, not vibes.

| Score | Descriptor |
|---:|---|
| 0 | Success is unmeasurable or purely aesthetic. |
| 1 | Only proxy or self-reported measures; LLM-judge-only with no validation path. |
| 2 | Metrics exist but are contested, saturated, or incomparable across studies. |
| 3 | At least one established benchmark or metric applies with adaptation. |
| 4 | Established benchmarks plus secondary outcomes (cost, latency, human effort) apply directly. |
| 5 | Multiple orthogonal accepted metrics; effect direction is interpretable; results compare number-for-number against published baselines. |

## 4. Refereed anchor availability

Enough peer-reviewed literature to satisfy a dissertation committee — arXiv
volume alone anchors nothing.

| Score | Descriptor |
|---:|---|
| 0 | No peer-reviewed venue publishes this; the conversation is arXiv-only. |
| 1 | A handful of workshop papers; nothing archival. |
| 2 | Refereed work exists but is scattered across incidental venues with no citation spine. |
| 3 | Several refereed anchors in recognized SE/AI/IS venues within the last three years. |
| 4 | A steady refereed stream including at least one systematic review or benchmark paper to anchor Chapter 2. |
| 5 | A mature refereed conversation — surveys, replications, and documented disagreements a committee will recognize — that still leaves the specific question open. |

## 5. Practitioner alignment

Business-agent relevance and SME career value: the answer should matter at
work, not only at a conference.

| Score | Descriptor |
|---:|---|
| 0 | No business relevance. |
| 1 | Interesting in the abstract, with no plausible route into enterprise practice. |
| 2 | Relevant to some business function, but not one the student can access or credibly speak for. |
| 3 | Directly relevant to enterprise agent practice; the result would change a real build/buy/deploy decision. |
| 4 | Sits inside the student's professional domain; findings are usable at work and strengthen SME positioning. |
| 5 | Practitioners are visibly asking this question (industry surveys, incident reports, procurement criteria), and answering it compounds the student's career trajectory. |

## 6. Novelty window

Active but not saturated, and not a race the big labs win by scale.

| Score | Descriptor |
|---:|---|
| 0 | Saturated: multiple groups have published this exact comparison recently. |
| 1 | Big-lab territory; compute or data scale decides the outcome. |
| 2 | Active area, but the specific angle will likely be absorbed within a year. |
| 3 | Active and growing (momentum ratio above 1) with the specific angle unclaimed in the scan. |
| 4 | Growing area plus a gap that scale does not close: methodology, evaluation design, or domain-access advantage. |
| 5 | A clear open niche the scan shows rising yet under-published in refereed venues, where one well-designed solo study stays citable regardless of frontier-model progress. |

## ideas.md template

Write `ideas.md` into the ideation run folder next to `landscape.md`. One
section per candidate, 5-10 candidates, ordered by total score. Every DOI and
count must trace to `landscape.json`; never invent metadata.

```markdown
# Candidate Topics — <run folder name>

Scanned <generated date> from `landscape.json`; scored per
`.github/skills/topic-ideation/references/RUBRIC.md`.

## Candidate 1: <short working title>

**Research question.** One falsifiable sentence.

**Why now.** 2-4 sentences citing the area's momentum numbers and at least
two scanned papers by DOI.

**Expected experiment shape.** Design (conditions, controls, repetitions),
benchmark or task suite, metrics, and the infrastructure a solo student
needs.

**Business relevance.** Which enterprise function this touches and what
decision the answer changes.

**Rubric scores.**

| Criterion | Score | Justification (cite DOIs) |
|---|---:|---|
| Problem clarity | n/5 | ... |
| Experimental tractability | n/5 | ... |
| Measurable outcomes | n/5 | ... |
| Refereed anchors | n/5 | ... |
| Practitioner alignment | n/5 | ... |
| Novelty window | n/5 | ... |
| **Total** | **n/30** | |

**Next step.**

    S=.github/skills/publications-search/scripts
    RUN=$(uv run $S/protocol.py init "<short topic phrase>" | tail -1)
    # put the verbatim research question in RUN/protocol.md section 1
    uv run $S/search.py "<keyword-style topic phrase>" --run-dir "$RUN" \
      --sources openalex,crossref,scholar --from-year <year>
```

Choosing the command parameters: set `--from-year` to the year of the oldest
paper the candidate's justification actually cites (usually 2022 or later for
agentic topics — earlier only when a pre-LLM literature genuinely anchors the
question). Start `--sources` at `openalex,crossref,scholar`; add `acm,ieee`
when an institutional session is live, since both matter for refereed-anchor
verification.

Never pass the research question verbatim as the search topic. A question is
the right content for `protocol.md` and the wrong query for a search engine:
its qualifiers ("does", "without a corresponding loss in", "compared with")
dilute the terms that carry the topic. Measured on a run of this pipeline, the
verbatim question recalled 0 of 8 preregistered known items while a six-word
keyword phrase over the same sources recalled 8 of 8. Hand `search.py` the
keyword phrase, and pin both stages to one folder with `--run-dir` so the
preregistered protocol and the search artifacts do not separate.
