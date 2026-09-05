# Review Protocol — specialized multi-agent versus single-agent LLM software engineering: comparative performance, coordination failures, verification, reliability, sustainability, and future work

Preregistered before any search (Kitchenham Stage 0). Downstream stages stamp
this file's sha256 (`protocol.py hash`) into their artifacts, so any edit made
after searching begins is detectable. Fill every `<...>` placeholder, then run
the search.

- Registered: 2026-09-04T15:58:03+00:00
- Run folder: 20260904-specialized-multi-agent-versus-single-ag

## 1. Research questions (verbatim)

Record the questions exactly as they will appear in the methods chapter.

- RQ1. specialized multi-agent versus single-agent LLM software engineering: comparative performance, coordination failures, verification, reliability, sustainability, and future work
- RQ2. Under what conditions does role-specialized multi-agent orchestration outperform a single LLM agent on software engineering tasks, and where does it underperform?
- RQ3. What coordination, verification, and reliability failure modes are reported for LLM-based multi-agent software engineering systems, and how are they measured?

## 2. Search strategy (per source)

| Source | Interface | Query as sent | Cap | From-year | Planned |
|---|---|---|---|---|---|
| openalex | API | same as RQ1 | 50 | 2022 | yes |
| crossref | API | same as RQ1 | 50 | 2022 | yes |
| arxiv | API | same as RQ1 | 50 | 2022 | yes |
| scholar | browser | same as RQ1 | 50 | 2022 | yes |
| acm | browser + institutional session | multi-agent LLM software engineering | 50 | 2022 | yes |
| ieee | browser + institutional session | multi-agent LLM software engineering | 50 | 2022 | yes |

ACM and IEEE reject long natural-language queries; record the condensed
keyword form actually sent (search.py `--keywords`), not the topic sentence.

### Amendment 2026-09-04: ACM/IEEE keyword query

The first search pass used `search.py`'s auto-condensed query,
`specialized multi agent versus single llm`. IEEE Xplore applies implicit AND
across those six terms and returned **2 results total** ("Showing 1-2 of 2").
Measured alternatives on the same session:

| Query sent to IEEE | Total hits |
|---|---:|
| specialized multi agent versus single llm | 2 |
| multi-agent LLM software engineering | 259 |
| multi-agent large language model software engineering | 381 |
| LLM agent software engineering | 540 |

A six-term implicit-AND query is a search-strategy defect, not a finding about
the literature. The protocol is amended to send
`multi-agent LLM software engineering` to both publisher databases, capped at
50 as originally registered. The superseded pass remains in `search-log.json`
as run 1, so the change is auditable rather than silent. Broader variants were
rejected to keep publisher recall comparable to the API sources rather than
maximized.

## 3. Inclusion / exclusion criteria (testable)

Every candidate abstract receives exactly one decision. A criterion is
testable when two readers of the same abstract reach the same decision.

- **core**: directly answers a research question above and warrants full text.
- **supporting**: contributes a method, limitation, benchmark, or combinable solution.
- **context**: useful background that does not require full-text synthesis.
- **exclude**: keyword collision, wrong field, duplicate, or out of scope.
- **unresolved**: no usable abstract; inspect the landing page before exclusion.

Additional topic-specific tests (edit before searching):

- Include only if: the work concerns LLM-based agents applied to a software
  engineering activity (requirements, design, code generation, repair, testing,
  verification, review, operations), **and** it reports empirical results, a
  named architecture or framework, a benchmark, or an explicit limitation or
  failure-mode analysis.
- Include also if: the work compares single-agent against multi-agent LLM
  configurations in any domain, since such comparisons bear directly on RQ2
  even outside software engineering.
- Exclude if: published before 2022; not in English; the "agents" are not
  LLM-based (classical MAS, reinforcement-learning agents, agent-based
  simulation); the paper is a keyword collision (biological agents, chemical
  agents, insurance agents, real-estate agents); or it is a duplicate record.
- Preprints are eligible and are flagged `is_preprint` rather than excluded;
  their rigor is assessed with the Garousi grey-literature items in quality.py.

## 4. Preregistered evidence domains (20)

Saturation is evaluated against this fixed taxonomy (saturation.py
EVIDENCE_DOMAINS). Adding a domain after reading begins invalidates the
stopping rule; log any such change as a protocol amendment with its date.

- benchmarks-evaluation
- code-generation-repair
- communication
- comparative-single-vs-multi
- cost-latency
- debate-consensus
- end-to-end-sdlc
- formal-verification
- governance-accountability
- human-in-loop
- memory-context
- observability-fault-injection
- orchestration
- reliability-nondeterminism
- requirements-design
- role-specialization
- security
- topology
- transactions-concurrency
- verification-testing

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

## 6. Known-item validation (PRISMA-S)

Must-find papers known before searching. The search strategy is invalid until
`protocol.py check` locates every non-placeholder entry in candidates.json.
List 5-10; keep the `- [ ] title | doi:...` format (doi optional but preferred).

- [ ] LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead
- [ ] Understanding multi-agent LLM frameworks: A unified benchmark and experimental analysis
- [ ] Designing LLM-based multi-agent systems for software engineering tasks: Quality attributes, design patterns and rationale
- [ ] LLM-Based Multi-Agent Systems for Code Generation: A Multi-Vocal Literature Review
- [ ] Comparing Single-Agent and Multi-Agent Strategies in LLM-Based Title-Abstract Screening
- [ ] On the Reliability Limits of LLM-Based Multi-Agent Planning
- [ ] An empirical comparison of multi-agent LLM architectural patterns for automated unit test generation
- [ ] Traceability and Accountability in Role-Specialized Multi-Agent LLM Pipelines

Provenance: these eight titles were screened `core` in the 2026-08-30 run of the
same research question. Reusing them makes `protocol.py check` a recall test of
the revised search strategy against a known-good corpus rather than a
self-fulfilling list.
