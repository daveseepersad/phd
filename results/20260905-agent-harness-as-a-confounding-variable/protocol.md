# Review Protocol — agent harness as a confounding variable in LLM agent performance comparisons

Preregistered before any search (Kitchenham Stage 0). Downstream stages stamp
this file's sha256 (`protocol.py hash`) into their artifacts, so any edit made
after searching begins is detectable. Fill every `<...>` placeholder, then run
the search.

- Registered: 2026-09-05T08:16:04+00:00
- Run folder: 20260905-agent-harness-as-a-confounding-variable

## 1. Research questions (verbatim)

Record the questions exactly as they will appear in the methods chapter.

- RQ1. How much of the reported performance difference between LLM agent configurations is attributable to the harness — scaffold, retry policy, and tool schema — rather than to the model or the agent topology under study?
- RQ2. Which studies hold the harness constant when comparing agent configurations, and what do they report when they do not?

Provenance: selected as Candidate 2 (25/30) in
`results/20260905-ideation-llm-agents-for-business-process-automati-plus-1/ideas.md`,
scored from a landscape scan of the seed area "LLM agent evaluation and
observability in production". That scan is the reason this protocol expects
trouble: the area held 0 on-topic works in 2022 and 2023, 1 in 2024, 3 in 2025
and 103 in a partial 2026, its venue list is led by Zenodo, Research Square and
Preprints.org, and its most-cited on-topic paper carries 5 citations. The
candidate therefore scored 2/5 on refereed anchors. This review exists partly to
determine whether archival anchors exist outside that scan's narrow query. If
they do not, the candidate should be parked rather than pursued.

## 2. Search strategy (per source)

| Source | Interface | Query as sent | Cap | From-year | Planned |
|---|---|---|---|---|---|
| openalex | API | LLM agent harness scaffold tool schema evaluation | 50 | 2024 | yes |
| crossref | API | LLM agent harness scaffold tool schema evaluation | 50 | 2024 | yes |
| arxiv | API | LLM agent harness scaffold tool schema evaluation | 50 | 2024 | yes |
| scholar | browser | LLM agent harness scaffold tool schema evaluation | 50 | 2024 | yes |
| acm | browser + institutional session | LLM agent harness scaffold evaluation | 50 | 2024 | yes |
| ieee | browser + institutional session | LLM agent harness scaffold evaluation | 50 | 2024 | yes |

The research question is not sent as a query. A question's qualifiers dilute the
terms that carry the topic, and a prior run of this pipeline measured the cost:
the verbatim question recalled 0 of 8 preregistered known items where a keyword
phrase over the same sources recalled 8 of 8.

ACM and IEEE reject long natural-language queries; record the condensed
keyword form actually sent (search.py `--keywords`), not the topic sentence.

## 3. Inclusion / exclusion criteria (testable)

Every candidate abstract receives exactly one decision. A criterion is
testable when two readers of the same abstract reach the same decision.

- **core**: directly answers a research question above and warrants full text.
- **supporting**: contributes a method, limitation, benchmark, or combinable solution.
- **context**: useful background that does not require full-text synthesis.
- **exclude**: keyword collision, wrong field, duplicate, or out of scope.
- **unresolved**: no usable abstract; inspect the landing page before exclusion.

Additional topic-specific tests (edit before searching):

- Include only if: the work evaluates LLM-based agents and either (a) varies a
  harness component — scaffold, control loop, retry or reflection policy, tool
  schema, memory, or prompt format — and reports the effect, or (b) compares
  agent configurations and states how the harness was controlled, or (c)
  analyses the validity of such comparisons.
- Include also if: the work is a benchmark or evaluation-methodology paper whose
  contribution is about measurement validity for agents, even when it varies no
  harness component itself.
- Exclude if: not in English; the agents are not LLM-based (reinforcement
  learning, BDI, agent-based simulation, or economic actors); "harness" refers
  to physical or test-instrumentation hardware; or the work reports an agent
  application with no evaluation and no comparison.
- Record separately, do not exclude: papers that compare configurations while
  leaving the harness uncontrolled. These are the evidence for RQ2 and the
  reason the question exists.

## 4. Preregistered evidence domains (20)

Saturation is evaluated against the taxonomy in this run's
`evidence-domains.json`, seeded below from the built-in default. That default
was derived from a software-engineering review: **edit it to fit this subject
before reading begins**, because concepts that map to no domain are
indistinguishable from a paper that introduced nothing new, and an ill-fitting
taxonomy reports saturation that never happened. `saturation.py check` warns
when read papers have unmapped concepts. Adding a domain after reading begins
invalidates the stopping rule; log any such change as a dated amendment.

- benchmark-design
- confounding-attribution
- cost-latency
- deployment-production
- environment-coupling
- evaluation-validity
- failure-attribution
- governance-safety
- harness-scaffold
- memory-context
- metric-definition
- model-versus-scaffold
- observability-tracing
- prompt-sensitivity
- reflection-planning
- reproducibility
- retry-recovery
- statistical-method
- tool-schema
- topology-comparison

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

- [ ] Agent Harness for Large Language Model Agents: A Survey | doi:10.20944/preprints202604.0428.v3
- [ ] Argos: Agentic Time-Series Anomaly Detection with Autonomous Rule Generation via Large Language Models | doi:10.48550/arxiv.2501.14170
- [ ] LATS-RCA: Language Agent Tree Search for Root Cause Analysis in Microservices | doi:10.1007/978-3-032-36590-3_14
- [ ] Did It Happen? Counterfactual Evaluation of LLM Agent Recovery from Ambiguous Tool Outcomes | doi:10.21203/rs.3.rs-10730245/v1
- [ ] Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent | doi:10.1145/3770855.3818432
- [ ] Engineering Agentic AI Systems: A Protocol-Aware Reference Architecture for Orchestration | doi:10.5281/zenodo.21897018
