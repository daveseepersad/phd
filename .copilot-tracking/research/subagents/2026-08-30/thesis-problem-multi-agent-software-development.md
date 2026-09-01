---
title: Thesis Problems in Multi-Agent Software Development
description: Evidence-grounded candidate dissertation problems derived from the completed literature review artifacts
author: GitHub Copilot
ms.date: 2026-08-30
ms.topic: research
---

## Status

Complete

## Research Topics and Questions

* Identify three to five new thesis problems in multi-agent software development
  supported by recorded limitations or future work.
* Rank candidates by evidence-gap strength, novelty within this corpus,
  dissertation-scale tractability, practical importance, and falsifiability.
* Prefer direct software-engineering evidence and controlled studies.
* Require hypotheses that permit multi-agent systems to tie or underperform
  single-agent systems.
* Define a minimum controlled experiment, outcomes, threats, and comparative
  rationale for each candidate.
* Recommend one candidate and one concise thesis title.

## Sources

* results/20260830-specialized-multi-agent-versus-single-ag/evidence-ledger.json
* results/20260830-specialized-multi-agent-versus-single-ag/saturation-report.json
* results/20260830-specialized-multi-agent-versus-single-ag/screening.json

## Discoveries and Evidence

* The screening set contains 522 records. The evidence ledger contains 207
  selected records: 48 read in full, 153 pending supporting papers, and six
  unavailable papers. The read set comprises 39 core and nine supporting
  papers; five additional core papers were unavailable.
* The saturation report records conceptual saturation after 48 full texts,
  with no pending core paper and five consecutive papers adding no new
  preregistered evidence domain. This supports coverage of known domains, not
  proof that every causal question is closed.
* No read software-engineering study isolates specialist-agent multiplicity
  while matching model, exogenous information, tools, context capacity, model
  calls, and token or monetary budget. Orders 13, 15, 42, and 48 are the
  strongest direct comparisons, but each leaves resource, prompt, handoff, or
  workflow components confounded.
* Contrary results are substantial. Orders 9 and 10 favor a single agent in
  non-SE tasks. Order 42 finds the complete Waterfall workflow worse than raw
  prompting for two of three models. Order 15 finds Developer-Tester better
  with Gemini Pro but single-agent better with Gemini Flash. Order 46 finds
  team diversity harmful at three agents and diminishing returns with scale.
* Adaptive delegation remains untested in direct SE evidence. Orders 3, 24,
  42, and 46 explicitly call for cost-aware orchestration, learned routing,
  task-dependent stage selection, or efficient allocation under diminishing
  returns.
* Communication quality is a distinct causal mechanism. Order 11 formalizes
  information loss under redundant delegation; orders 13 and 15 observe
  authoritative-plan and supervisor bottlenecks; order 14 changes structured
  handoffs and validation together; order 44 identifies shared-state and
  delegation defects in framework issue reports.
* Fault-injection work is active but incomplete. Orders 4 and 5 lack a matched
  single-agent arm and do not jointly measure semantic propagation, recovery,
  clean-run harm, and resource cost on the same repository tasks. Orders 29
  and 44 add failure taxonomies without validating mitigations.
* Verification gains appear conditional on new evidence. Order 11 predicts no
  general value from redundant relays; order 24 finds complementary cross-model
  errors; order 36 finds compiler/test-grounded repair can beat self-reflection
  at similar calls; order 21 shows heterogeneous model teams need not beat
  homogeneous teams; orders 32 and 48 leave large token-budget confounds.
* Novelty is corpus-bounded and provisional. Unavailable core order 41 targets
  efficiency-first design. Unresolved screening ranks 27, 46, 95, 97, and 106
  may overlap adaptive spawning, configuration validity, independent
  verification, or contamination propagation, but their recovered abstracts
  are absent or too truncated to establish methods or findings.

## Candidate Ranking

Scores use a five-point scale in this order: evidence-gap strength, novelty
within the analyzed corpus, dissertation tractability, practical importance,
and falsifiability. Novelty is discounted for unavailable or unresolved close
matches; tractability breaks the tie between candidates two and three.

1. Resource-bounded adaptive delegation: 5, 4, 4, 5, 5 (23/25)
2. Independent-signal verification: 4, 3, 5, 5, 5 (22/25)
3. Information-preserving handoff contracts: 4, 4, 4, 5, 5 (22/25)
4. Semantic fault containment under matched architectures: 4, 3, 4, 5, 5
   (21/25)

### Resource-Bounded Adaptive Delegation

* Exact problem: Static single-agent and fixed multi-agent workflows cannot
  identify when specialist delegation earns its additional communication and
  inference cost. Existing comparisons bundle architecture with resources.
* Supporting orders: 3, 9, 10, 13, 15, 24, 42, 46, and 48.
* Research question: Under identical exogenous information, tools, and maximum
  resource ceilings, can a preregistered policy that selects one agent, a
  subset of specialists, or early stopping improve the held-out quality-cost-
  latency Pareto frontier over the best fixed policy?
* Hypothesis: Task-level heterogeneity makes adaptive delegation lower expected
  preregistered loss than fixed single-agent or fixed multi-agent workflows.
  The hypothesis fails if a fixed policy is noninferior in quality and cheaper.
* Minimum experiment: Train only on historical traces, then run a paired,
  repository-disjoint evaluation on at least 200 repository repair tasks with
  three seeds. Compare iterative single-agent, fixed Developer-Tester, fixed
  full specialist team, a simple complexity heuristic, and the learned policy.
  Hold model, prompt-optimization effort, tools, context sources, maximum
  calls, total token ceiling, and execution sandbox constant. Give the single
  agent equivalent self-refinement opportunities.
* Outcomes: Hidden-test resolution, regressions, requirement completion,
  tokens, calls, tool executions, wall-clock latency, monetary cost, Pareto
  hypervolume, and regret against the per-task oracle policy.
* Major threat and relative strength: A policy may learn benchmark-specific
  difficulty cues; temporal and repository holdouts are necessary. This is the
  strongest candidate because it unifies the dominant causal gap with an
  actionable architecture, rather than producing another fixed workflow.

### Independent-Signal Verification

* Exact problem: Repository-scale evidence does not separate verifier benefit
  due to extra inference, model diversity, independent context, or executable
  evidence from role labels and discussion.
* Supporting orders: 2, 11, 14, 21, 24, 32, 36, 43, and 48.
* Research question: At equal calls and tokens, which combinations of verifier
  identity and evidence access reduce residual patch defects and repair harm?
* Hypothesis: Verification value tracks conditional error independence and
  nonredundant executable evidence; same-model role play may tie or underperform
  equally budgeted self-refinement.
* Minimum experiment: Use one fixed patch generator and factorially vary same-
  model versus cross-model verifier and no evidence versus tests/static-analysis
  evidence. Add no-review and equal-budget centralized self-refinement controls.
  Give centralized and delegated conditions the same external evidence, model
  calls, token ceiling, tools, tasks, and seeds.
* Outcomes: Residual defects, valid rejection, false rejection, harmful repair,
  generator-verifier error correlation, calibration, tokens, latency, and cost.
* Major threat and relative strength: Tests and static analysis are imperfect
  oracles, and model families may share training-induced errors. This candidate
  is easier to execute than adaptive delegation but narrower and closer to
  orders 24 and 36.

### Information-Preserving Handoff Contracts

* Exact problem: Multi-agent software workflows lack validated handoff formats
  that preserve decision-relevant requirements, evidence, and provenance under
  bounded context without turning early plans into authoritative errors.
* Supporting orders: 1, 3, 11, 13, 14, 15, and 44.
* Research question: With equal exogenous information and terminal context
  capacity, do typed, evidence-linked handoffs reduce omissions and downstream
  error propagation relative to prose relays or full shared transcripts?
* Hypothesis: Typed handoffs improve long-horizon repository outcomes when the
  schema captures task-relevant state, but can underperform full context or a
  central agent when the schema omits a critical fact.
* Minimum experiment: Compare centralized single-agent, free-form relay, full-
  transcript shared state, and typed provenance blackboard conditions on paired
  repository tasks containing seeded requirement changes, dependency facts,
  and contradictory observations. Hold models, tools, total tokens, initial
  evidence, topology within multi-agent arms, and seeds constant.
* Outcomes: Hidden-test success, critical-fact retention, contradiction rate,
  propagation depth, integration defects, handoff tokens, latency, and repair
  harm.
* Major threat and relative strength: A hand-designed schema can encode task
  knowledge and make retention metrics circular. This candidate has the best
  theoretical mechanism but requires harder construct validation than the top
  two.

### Semantic Fault Containment

* Exact problem: It is unknown whether specialist coordination creates net
  resilience or a larger cascade surface when upstream messages remain fluent
  but are semantically wrong.
* Supporting orders: 4, 5, 14, 29, and 44.
* Research question: Under matched tasks, models, tools, and resource budgets,
  how do single-agent, linear specialist, and shared-state workflows degrade and
  recover under realistic semantic and coordination faults?
* Hypothesis: Without independent evidence, linear specialist workflows show
  equal or greater quality degradation than a matched single agent; evidence-
  grounded conditional checkpoints reduce degradation but may harm clean runs.
* Minimum experiment: Run a three-by-two-by-two factorial comparison of
  architecture, clean versus injected faults, and absent versus executable-
  evidence checkpoint on repository tasks with repeated seeds. Derive faults
  from production issue traces and inject equivalent corruptions into each
  architecture's information path.
* Outcomes: Robustness ratio, task success, cascade depth, time to detection,
  recovery rate, false intervention rate, residual defect severity, tokens,
  latency, and cost.
* Major threat and relative strength: Injected faults may not represent field
  failures. This is highly practical and readily falsifiable, but less novel
  because orders 4 and 5 already establish the fault-injection line.

## Recommendation

Recommended problem: resource-bounded adaptive delegation.

Recommended title: *When to Delegate: Resource-Aware Agent Teams for Software
Engineering*.

## Follow-On Questions

* Retrieve unavailable core order 41 before making a publication-level novelty
  claim about efficiency-first orchestration.
* Resolve screening ranks 27, 46, 95, 97, and 106 before preregistration.

## Clarifying Questions

None.