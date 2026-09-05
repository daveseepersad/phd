# Review Protocol — process model constraints versus natural language policy for compliance critical LLM business process agents

Preregistered before any search (Kitchenham Stage 0). Downstream stages stamp
this file's sha256 (`protocol.py hash`) into their artifacts, so any edit made
after searching begins is detectable. Fill every `<...>` placeholder, then run
the search.

- Registered: 2026-09-05T05:29:26+00:00
- Run folder: 20260905-process-model-constraints-versus-natural

## 1. Research questions (verbatim)

Record the questions exactly as they will appear in the methods chapter.

- RQ1. In compliance-critical business processes, does binding an LLM agent to an explicit process model reduce policy violations without a corresponding loss in task completion, compared with an agent given the same policy as natural-language instructions?
- RQ2. Which control mechanisms for agentic business process automation have been evaluated empirically, and against what baselines?

Provenance: selected as Candidate 1 (25/30) in
`results/20260905-ideation-llm-agents-for-business-process-automati-plus-1/ideas.md`,
scored against the topic-ideation rubric from a landscape scan of the seed area
"LLM agents for business process automation" (143 on-topic works since 2022;
15 in 2024, 38 in 2025, 87 in a partial 2026).

## 2. Search strategy (per source)

| Source | Interface | Query as sent | Cap | From-year | Planned |
|---|---|---|---|---|---|
| openalex | API | same as RQ1 | 50 | 2023 | yes |
| crossref | API | same as RQ1 | 50 | 2023 | yes |
| scholar | browser | same as RQ1 | 50 | 2023 | yes |
| acm | browser + institutional session | LLM agent business process automation compliance | 50 | 2023 | yes |
| ieee | browser + institutional session | LLM agent business process automation compliance | 50 | 2023 | yes |

ACM and IEEE reject long natural-language queries; record the condensed
keyword form actually sent (search.py `--keywords`), not the topic sentence.

### Amendment 2026-09-05: queries broadened after known-item validation failed

The preregistered strategy above sent RQ1 verbatim to the API sources. That
strategy recalled 0 of the 8 preregistered known items, so `protocol.py check`
correctly rejected it and the queries were broadened, as PRISMA-S requires. The
full set actually sent, in order, all with `--from-year 2023`:

| # | Query as sent | Sources | New candidates |
|---|---|---|---:|
| 1 | RQ1 verbatim | openalex, crossref, scholar, acm, ieee | 61 |
| 2 | RQ1 verbatim (repeat after the OpenAlex wildcard fix) | openalex, crossref, scholar, acm, ieee | 48 |
| 3 | LLM agents for business process automation compliance policy conformance | openalex, crossref | 96 |
| 4 | large language model agent business process management BPMN workflow governance | openalex, crossref | 96 |
| 5 | LLM agents for business process automation compliance | openalex, crossref | 77 |
| 6 | LLM agents for business process automation compliance (dual-scope OpenAlex) | openalex | 44 |
| 7 | BPMN process model driven multi-agent workflow automation | openalex, crossref | 115 |

Three tool defects were found and fixed during this stage, and they change how
the counts above should be read:

- OpenAlex parses `?` as a wildcard operator, so RQ1 verbatim returned HTTP 400
  and query 1 drew nothing at all from the primary source.
- The OpenAlex source queried only `search=` (full-text relevance). Scoped
  `title_and_abstract.search` retrieval was added because the question's own
  known items were unreachable otherwise: measured here, full-text search
  recalled 4 of 8 from a 14,241-work pool while the scoped filter recalled 8 of
  8 from 141.
- Known-item validation matched titles by exact equality, so the entry for
  10.3390/info16090809 reported MISSING while the corpus already held that
  work's Preprints.org version. Query 7 was run chasing a paper that was
  already present and is retained here only for an honest audit trail.

Final known-item recall: 8 of 8. ACM returned 0 results on both attempts
because its bot challenge did not clear; Google Scholar returned only 6, having
been sent the full-sentence question. Both are recorded as identification
limitations rather than as evidence of an empty literature.

## 3. Inclusion / exclusion criteria (testable)

Every candidate abstract receives exactly one decision. A criterion is
testable when two readers of the same abstract reach the same decision.

- **core**: directly answers a research question above and warrants full text.
- **supporting**: contributes a method, limitation, benchmark, or combinable solution.
- **context**: useful background that does not require full-text synthesis.
- **exclude**: keyword collision, wrong field, duplicate, or out of scope.
- **unresolved**: no usable abstract; inspect the landing page before exclusion.

Additional topic-specific tests (edit before searching):

- Include only if: the work concerns LLM-based or agentic automation of an
  organizational process, and reports either an empirical result, a named
  control or governance mechanism, or a deployed case study.
- Include also if: the work is pre-LLM business process management that
  defines conformance checking, process-model constraints, or compliance
  verification, and is reachable by backward snowballing from an included
  paper. Such work anchors the deterministic baseline and is not excluded by
  the 2023 from-year, which bounds the search rather than the corpus.
- Exclude if: not in English; agents are non-LLM and the work predates and is
  unconnected to the process-control question; the process is personal rather
  than organizational; or "agent" denotes a human worker, an insurance agent,
  or a chemical agent (keyword collision).

## 4. Preregistered evidence domains (20)

Saturation is evaluated against the taxonomy in this run's
`evidence-domains.json`, seeded below from the built-in default. That default
was derived from a software-engineering review: **edit it to fit this subject
before reading begins**, because concepts that map to no domain are
indistinguishable from a paper that introduced nothing new, and an ill-fitting
taxonomy reports saturation that never happened. `saturation.py check` warns
when read papers have unmapped concepts. Adding a domain after reading begins
invalidates the stopping rule; log any such change as a dated amendment.

- autonomy-control
- benchmarks-evaluation
- conformance-violation
- cost-latency
- deployment-case-study
- exception-handling
- explainability-rationale
- governance-accountability
- human-in-loop
- multi-agent-topology
- orchestration
- organizational-adoption
- policy-compliance
- process-mining
- process-modeling
- prompting-instruction
- reliability-nondeterminism
- security-privacy
- task-completion
- tool-integration

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

- [ ] Governed Agentic Process Automation: A Floor-Safety Guarantee for Compliance-Critical LLM Routing | doi:10.3390/a19080627
- [ ] NL2ProcessOps: Towards LLM-Guided Code Generation for Process Execution | doi:10.1007/978-3-031-70418-5_8
- [ ] BPMN-Based Design of Multi-Agent Systems: Personalized Language Learning Workflow Automation | doi:10.3390/info16090809
- [ ] Studies on the Use of Large Language Models for the Automation of Business Processes in Enterprise Resource Planning Systems | doi:10.1007/978-3-031-70239-6_2
- [ ] Enhancing Trust in LLM-Based AI Automation Agents: New Considerations and Future Challenges | doi:10.48550/arxiv.2308.05391
- [ ] CAPRI: A Context-Aware Privacy Framework for Multi-Agent Generative AI Applications | doi:10.1109/access.2025.3549312
- [ ] E2E Process Automation Leveraging Generative AI and IDP-Based Automation Agent: A Case Study on Corporate Expense Processing | doi:10.47852/bonviewaia52026307
- [ ] XPF: Agentic AI System for Business Workflow Automation | doi:10.1145/3731545.3743644
