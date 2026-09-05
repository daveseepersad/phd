# Dissertation Topic Candidates: Process Model Constraints versus Natural Language Policy for Compliance-Critical LLM Agents

**Author:** Dave Seepersad · **Date:** 2026-09-05
**Program:** Ph.D. in Computer Science, Nova Southeastern University
**Purpose:** This document distills three dissertation-scale research problems from a saturation-bounded systematic review of 32 full-text papers on binding large language model business-process agents to explicit process constraints rather than to natural-language policy. Each candidate targets a confound, a contradiction, or a measurement defect that the reviewed corpus exposes but cannot resolve from its own evidence.

---

## How these topics were selected

- **Corpus.** 892 database records and 177 citation-chaining records were reduced to 704 unique screened records after removing 355 duplicates. 221 reports were sought and 32 full texts were retrieved, read, and quality-appraised against a preregistered taxonomy of 20 evidence domains. Saturation was declared at 32 reads against a preregistered minimum of 20, with trailing zero domain novelty across read-order windows of 3, 4, 5, 6, 7, and 8.
- **Selection rule.** A candidate qualified only if the corpus contains at least two independent studies with defensible designs whose evidence bears on the same question and does not converge, or a defect that the primary authors themselves name as unresolved. Corpus search was used to test each candidate: a problem was retained only when its evidence was found in several papers rather than concentrated in one.
- **The binding methodological fact.** No study in the corpus runs the target comparison in its stated form. The five studies reporting large violation reductions each compiled the policy into a different artefact, and the single highest-rigour ablation that removes a workflow template on its own moved aggregate accuracy from 81.4% to 80.5% while removing tool mediation moved it from 81.4% to 57.3%. What the reviewed literature calls binding to an explicit process model is therefore a compound treatment, not a variable.
- **Quality weighting.** All 32 papers were scored on an eight-item checklist, with four extra grey-literature items for preprints. Scores range from 1.00 to 0.188 and six fall below the 0.50 flag threshold. The four papers whose figures most cleanly support a no-trade-off answer score 0.438, 0.312, 0.312, and 0.188; no claim in this document rests on any of them.
- **Verification.** Every quotation below was located in the run's extracted full-text corpus by an automated substring check that tolerates only PDF extraction artifacts, and every reference string is copied verbatim from the run manifest. Preprints are labeled in each attribution, and works cited from abstract metadata alone are labeled as such.
- **Reliability caveat.** The screening reliability check reports Cohen's kappa of 0.675 over 78 of 88 sampled records, with 10 records excluded as unratable, observed agreement 0.769 and expected agreement 0.289. The second rater was an independent blind large language model re-prompt, not a human coder, so the coefficient measures decision stability under re-prompting and is not human inter-rater reliability.
- **Provenance caution.** 15 of the 47 records screened as core could not be retrieved as full text and contributed to no claim. That set includes an eighteen-author research manifesto on agentic business process management (Calvanese et al., 2026), a practitioner study of agent governance in business processes (Vu et al., 2026), and a floor-safety guarantee for compliance-critical routing (Pacella et al., 2026), each cited here from abstract metadata only. Saturation was therefore declared over a corpus bounded by retrieval, not by the literature.

---

# Topic 1 — Which part of binding does the work

**Proposed title:** *Mediation or Model? A Factorial Dismantling of Process-Model Binding in Compliance-Critical LLM Business-Process Agents*

## The problem

The claim that binding an agent to an explicit process model reduces policy violations is stated across the literature as if *process model* named a single treatment. It does not. Every study that reports a large violation reduction has changed two things at once: **what the policy was compiled into**, and **where the compiled artefact is evaluated**. The artefacts in the corpus include a per-tool executable precondition, a satisfiability-modulo-theories constraint set, a risk-graph rule table injected into a prompt, a set of step-ordered skill procedures, and a bank of world-state invariants over an organizational graph. The evaluation sites include the model's own context window, an advisory checker whose verdict the model may ignore, and a blocking mediator interposed between the agent and its tools. No published design crosses these two factors, so no published effect size can be attributed to either.

The one study that treats the constraint as the experimental variable rather than as the intervention finds the process-structure term close to inert. Wang (2026), reporting Open-Rosalind, binds a biomedical agent to pre-declared workflow templates under mandatory tool mediation and mandatory traces, then removes each constraint separately across six model families over 1,770 runs with paired seed replications. Removing the workflow template moved aggregate accuracy from 81.4% to 80.5%. Removing tool mediation moved it from 81.4% to 57.3%. Read alongside the five studies that report large gains, the pattern is coherent rather than contradictory: what those studies share is not process structure but a **decision procedure evaluated outside the model, on an interface the model must pass through**. What was ablated was something else, a template that shapes planning order while enforcement lives elsewhere.

The consequence is that the field's central engineering question is currently unanswerable. An organization deciding whether to invest in process modeling, in policy compilation, or in runtime mediation has no evidence separating the three, and the same ambiguity propagates into the theory: Ait et al. (2025) argue that natural language is the wrong notation because collaboration and reflection strategies can only be expressed as free-text annotation, while Besanson (2026) argues that notation is irrelevant because prompt-layer constraints cannot bind by construction. Both may be right about different factors. A dissertation that crosses artefact form against enforcement site, on one agent and one policy, would convert the corpus's largest confound into a measured decomposition, and would tell the field whether *process model* is the right construct at all or whether it should be talking about mediation.

## Evidence that this is a problem

1. **Compiling policy into an executable precondition buys roughly twenty points, with the agent, tools, and tasks held fixed** — the treatment changes only the policy encoding:
   > "The fully automated ToolGuards generation and deployment pipeline shows substantial steady gains, improving passˆ1 and passˆ10 to 0.685 and 0.500, respectively – over 20 percentage points above the baseline."
   > — *Towards Enforcing Company Policy Adherence in Agentic Workflows* (2025), p. 6
2. **Restating exactly the same policy in natural language buys almost nothing** — two re-injection variants, one supplying the full document and one the ground-truth policy-to-tool mapping before every action, land in the same place:
   > "Both strategies led to only very modest improvements, reaching a passˆ10 of 0.273, with strategy (2) performing slightly better on average."
   > — *Towards Enforcing Company Policy Adherence in Agentic Workflows* (2025), p. 6
3. **The only ablation that isolates the workflow-template constraint finds it near-inert and credits tool mediation instead** — this is the corpus's highest-rigour dismantling of the treatment:
   > "The strongest and most stable effect is the drop from full to no_tool; citation and template ablations change accountability properties much more than average accuracy."
   > — Wang (2026), p. 9 **[preprint]**
4. **Even the mediation term is contingent rather than intrinsic** — against a free-form baseline with identical tools, the constrained pipeline won decisively only where the model was weak at unconstrained tool use:
   > "On Gemma, however, full and ReAct are statistically indistinguishable on the in-house benchmark (p = 0.74)."
   > — Wang (2026), p. 10 **[preprint]**
5. **An explicit decision model supplied purely inside the prompt can still move accuracy by more than fifty points** — so artefact form is not reducible to enforcement site, and the two factors must be crossed rather than conflated:
   > "rule-based prompts improved PL r classification accuracy by over 50 percentage points, highlighting the essential role of structured input for deterministic safety tasks."
   > — Iyenghar et al. (2025), p. 21
6. **A formal process model handed to the model as context conveys structure without producing enforcement** — the agent fabricates state it was never told about:
   > "As it is possible to see, the chatbot assumed the user had already booked the hotel even though that was not explicitly mentioned."
   > — Lins et al. (2023), p. 6
7. **Prompt-layer constraints cannot bind by construction, which is an argument about site rather than about artefact** — stated as a structural claim, not an empirical one:
   > "Prompt guardrails cannot enforce hard constraints by construction because the model may ignore, reinterpret, or route around them through tools whose effects are off-screen."
   > — Besanson (2026), p. 21 **[preprint]**
8. **The study best placed to separate architecture from training concedes that it did not** — the comparison that would have isolated the mechanism was named and left unrun:
   > "The comparison between LOM-action (fine-tuned) and frontier models (zero-shot) does not fully isolate the architectural contribution from the training contribution."
   > — Zhu et al. (2026), p. 13 **[preprint]**

## The experiment

**Design.** A fully crossed 3 × 3 factorial experiment: policy artefact form × enforcement site, applied to one agent, one tool surface, one policy document, and one task set drawn from a public benchmark whose tasks include requests that violate policy. The policy is authored once in natural language and then compiled, by a documented and released pipeline, into each of the other two artefact forms; semantic equivalence across the three encodings is established by a preregistered clause-coverage audit before any cell runs. Every cell is replicated k times per task with k fixed by power analysis against the smallest effect the corpus reports as meaningful, prompts differ only in the manipulated factor, per-task token budgets are identical, and every trajectory is archived. Protocol, hypotheses, exclusion rules, and stopping rule are registered before the first cell executes.

**Conditions:**
- Artefact A1: the policy as a natural-language document, supplied unchanged
- Artefact A2: the same policy compiled into declarative per-action preconditions, which prohibit rather than sequence
- Artefact A3: the same policy compiled into an imperative, step-ordered workflow template
- Site S1: in context only, with no external evaluation of the artefact
- Site S2: advisory evaluation, in which a checker's verdict is returned to the agent as text it is free to disregard
- Site S3: blocking mediation, in which the checker sits on the tool interface and refuses non-conforming calls with a machine-readable reason
- CTRL-BUDGET: the A1 × S1 cell re-run at the token and latency budget of the most expensive cell, so that no measured advantage can be an artifact of extra compute
- CTRL-ENCODE: A2 and A3 re-run with hand-verified encodings alongside the automatically compiled ones, separating compilation error from artefact form

**Metrics.** The primary compliance outcome is the trajectory-level violation rate, scored by replaying independently authored checks over the full tool-call trace rather than by comparing final states, because the corpus shows outcome-only scoring is biased. The primary completion outcome is benchmark task success, reported jointly with the violation rate from the same runs and never separately. Secondary outcomes are correct-action recall at the tool-call level, blocked-benign rate, tokens, monetary cost, and wall-clock latency. Analysis fits a mixed-effects model with artefact, site, and their interaction as fixed effects and task and replicate as random effects; the headline result is a variance decomposition stating how much of the compliance outcome each factor and the interaction explains. The mediation hypothesis is falsified if the artefact main effect exceeds the site main effect with a null interaction; the process-structure hypothesis is falsified under the converse; a significant interaction with neither factor dominating falsifies both readings the corpus currently supports and is the outcome the Open-Rosalind ablation most strongly predicts.

## Why this approach is viable

1. **A five-condition ablation over 1,770 runs across six model families is already an executed design** — the scale required here is established practice rather than aspiration:
   > "Under cluster-aware permutation tests, the full pipeline beats no_tool by 26.4 percentage points on Gemma and 19.3 percentage points on GPT-5-mini"
   > — Wang (2026), p. 10 **[preprint]**
2. **The compilation step from a policy document to executable per-tool preconditions has been automated and released as a pipeline** — artefact A2 does not have to be invented:
   > "The original τ-bench approach achieves a passˆ1 rate of 0.450 and a passˆ10 rate of 0.227."
   > — *Towards Enforcing Company Policy Adherence in Agentic Workflows* (2025), p. 6
3. **The declarative artefact form has an established generation mechanism evaluated at scale** — constrained generation over a metamodel produced two thousand declarative process models with better than 98% convention compliance:
   > "While our framework achieves high accuracy in basic constraint generation, we observed increased variability in handling complex negative constraints and intricate temporal conditions."
   > — Santos et al. (2025), p. 47
4. **The three-way site comparison this design requires has already been run once on identical traces, so the cells are known to separate** — no enforcement, policy in the system prompt, and world-state-grounded interception produce materially different violation rates:
   > "Under the policy-in-prompt condition, risky-case violations drop from 95.3% to 40.7% overall—a substantial reduction, but still leaving 122 violations across 300 risky cases."
   > — Wu and Gong (2026), p. 16 **[preprint]**
5. **The natural-language control arm is already named and operationalized as a baseline in a deployed policy-governed workload** — the comparator is standard, not exotic:
   > "The policy agent fails because the source policies, written for human auditors, neither abstract rules into a general, non-conflicting form nor make edge cases and grounding explicit."
   > — Wang et al. (2026), p. 5 **[preprint]**
6. **The design's central risk, that a hand-fixed template understates what process binding can do, is stated by the very study that produced the null** — which tells the replication exactly what to vary:
   > "The harness templates are hand-coded; while their fixity is a feature for reproducibility, it bounds the range of workflows the system can express."
   > — Wang (2026), p. 13 **[preprint]**

## Assessment

- **Novelty:** No study in the corpus crosses artefact form with enforcement site. Five studies vary both at once in a single step and one ablates a single term. The contribution is the first attribution of the reported violation reductions to a named factor rather than to a compound treatment.
- **Falsifiability:** The preregistered interaction test yields a decisive result in three mutually exclusive directions, and the budget-matched and hand-verified-encoding controls remove the two alternative explanations, extra compute and compilation error, that would otherwise absorb any finding.
- **Feasibility:** Nine cells plus two controls on one benchmark, one agent, and one policy is smaller than at least two executed studies in the corpus. The benchmark, the compilation pipeline, the trajectory-level scorer, and the mediator pattern all exist in published form.
- **Risk:** The principal threat is that semantic equivalence across the three encodings cannot be fully established, so an artefact effect could be a coverage effect. Mitigation is the preregistered clause-coverage audit, publication of all three encodings, and an adversarial review by a rater blind to condition. A secondary threat is that a single benchmark domain, which carries a disproportionate share of the corpus's direct evidence, will not generalize; mitigation is a second, structurally different compliance-critical domain as a preregistered replication arm.

---

# Topic 2 — What compliance costs

**Proposed title:** *The Strictness-Availability Frontier: Pricing the Task-Completion Cost of Policy Mediation in LLM Business-Process Agents*

## The problem

The literature reports enforcement results at a single operating point and then argues about whether the cost is acceptable. Nobody has drawn the curve. The one study in the corpus that reports both dependent variables at the granularity of the individual tool call found that solver-aided verification cut invalid write calls but also cut the recall of correct write calls from 0.61 to 0.49 while precision rose from 0.51 to 0.70. At the granularity of the task, the same runs showed no cost at all, and in fact a slight improvement. Both statements are true of the same experiment. That is not a nuance; it is a measurement crisis for the second half of the research question this review was built around, because the clause **without a corresponding loss in task completion** can be made true or false by choosing the granularity of the completion measure.

Availability costs then recur across the corpus as incidental findings that nobody has assembled into a curve. Nine benign proposals were quarantined by a strict conformance gate for adding a single unrequested annotation field, breaking a preregistered success criterion without any safety benefit. A tool specification that over-constrained an inherently open-ended task regressed it by 23.7% while improving nine others. Heavier structural transformation of agent input degraded success outright once referential integrity broke inside reasoning traces. Guard synthesis is itself named as a source of false positives that reduce usability. Each of these is a point on the same frontier, and none of the studies that produced them was designed to trace it.

What makes this a dissertation rather than an engineering note is that the objective function already exists in the corpus and has never been fitted. One study defines three cost channels for constraint calibration, false-positive cost as lost throughput when an admissible action is blocked, false-negative cost as regulatory exposure when an inadmissible action is permitted, and escalation cost as operator time, and argues that choosing an operating point is a capital-allocation decision. That paper drives a simulated procurement policy rather than a language model, so its cost model has never been estimated against real agent behavior. A study that sweeps strictness parametrically, measures the joint response at two granularities, and fits the operating point under a grid of cost ratios would replace the field's binary argument about whether constraints are worth it with a priced frontier that a compliance officer could actually read.

## Evidence that this is a problem

1. **The single direct measurement of both variables at tool-call granularity shows a genuine recall cost** — the constrained agent produces fewer correct write calls, not merely fewer wrong ones:
   > "This suggests a tradeoff: policy checking improves precision (fewer invalid tool calls) at the cost of a slight reduction in recall (fewer correct tool calls)."
   > — Winston et al. (2026), p. 4 **[preprint]**
2. **The same runs show the cost disappearing at task granularity, so the trade-off is an artifact of the measure as much as of the mechanism** — the clause about completion loss is therefore currently untestable:
   > "Overall, both achieve similar success rates, with the policy checker yielding a slight improvement."
   > — Winston et al. (2026), p. 5 **[preprint]**
3. **Strictness can cost availability while buying no safety at all** — a preregistered success criterion was broken by benign proposals quarantined for an unrequested field:
   > "OpenAI met the compound endpoint in 400/400 trials. Anthropic met it in 391/400: nine outputs for one benign payment case added an unrequested approval-scope ﬁeld and were quarantined before policy evaluation."
   > — Qasim and Kadim (2026), p. 2 **[preprint]**
4. **Over-constraining a broad task reverses the sign of the intervention** — nine of ten cases improved and the tenth regressed sharply, which is a frontier, not a uniform gain:
   > "The 'Semantic Summary' performance drop (-23.7%) occurred because strict nlp_hints over-constrained the LLM during inherently broad tasks, adding unnecessary token overhead."
   > — Chaitanya (n.d.), p. 5
5. **Light structure helps completion and heavy structure hurts it, in the same experiment on the same agent** — a graded utility cost that no enforcement study has replicated deliberately:
   > "The entity-only configuration improved the success rate by 4% and reduced the number of conversational turns by 1.3 compared to the baseline."
   > — Park and Madisetti (2025), p. 8
6. **The enforcement artefact is itself a source of false positives, so strictness and correctness are not the same axis** — the authors of the strongest measurement study in the corpus name this explicitly:
   > "Conversely, overly restrictive or hallucinated guard conditions may inflate false positives and reduce system usability."
   > — Rabinovich et al. (2026), p. 8 **[preprint]**
7. **The cost model that would let an operating point be chosen exists, and its author states that a system without one is under-specified** — but it has never been estimated against a language model agent:
   > "A vendor offering an agentic system whose hard constraints are hosted at the prompt layer is offering a system whose false-negative tail is uncharacterized"
   > — Besanson (2026), p. 34 **[preprint]**
8. **Published zero-violation results are idealized endpoints of an uncharacterized curve, not measurements of a deployable operating point** — stated by the study that reported them:
   > "The zero-violation result under SARC should be read as an idealized enforcement result, not as a claim that residual violations are impossible."
   > — Besanson (2026), p. 32 **[preprint]**

## The experiment

**Design.** A parametric strictness sweep on a single compliance-critical benchmark, holding the agent, the tool surface, and the policy fixed and varying only the mediator. Strictness is manipulated along two preregistered ladders that are crossed at a coarse grain: **coverage**, the proportion of policy clauses compiled into the mediator, sampled at five levels from none to all; and **tightness**, the mediator's response to a non-conforming call, at three levels of advisory, block-with-replan, and fail-closed. Each cell is replicated across tasks and seeds, with all runs scored by the same instruments so that points on the frontier are commensurable. A companion arm re-runs the full ladder with hand-verified encodings so that compilation defects can be separated from constraint tightness, which the corpus identifies as a recurring confound in this exact setting.

**Conditions:**
- L0: no mediation, policy supplied as a natural-language document, the reference arm
- L1 through L5: coverage levels from 20% to 100% of compiled policy clauses, at fixed block-with-replan tightness
- T1 through T3: advisory, block-with-replan, and fail-closed tightness, at fixed full coverage
- ORACLE: full coverage with hand-verified encodings, isolating compilation error
- STRESS: the frontier re-measured under injected predicate error, to test whether the curve's shape survives imperfect enforcement

**Metrics.** Five quantities are recorded from every run: trajectory-level violation rate, task completion, correct-action recall at the tool-call level, blocked-benign rate, and operator escalations, alongside token and latency overhead. The primary artifact is the fitted frontier relating violation rate to correct-action recall as strictness rises, reported separately at tool-call and task granularity so that the divergence between them is measured rather than assumed. The secondary artifact is an operating-point analysis: using the three declared cost channels, the expected cost is minimized over a grid of false-positive, false-negative, and escalation cost ratios, and every operating point published in the reviewed corpus is located on that grid to determine under which cost assumptions it is optimal. The frontier hypothesis is falsified if correct-action recall is flat across strictness levels, which would mean constraints are free, or if the violation rate is flat, which would mean they do nothing. A demonstration that the granularity divergence persists across all strictness levels is by itself a result, because it establishes that the completion clause must be specified at a stated granularity before it can be tested.

## Why this approach is viable

1. **A monotone degradation curve of exactly this shape has already been measured for a related parameter** — enforcement recall was swept from full to zero coverage with clean behavior at every level:
   > "These results support the central claim: the binding constraint on enforcement quality is world-model coverage, not invariant sophistication."
   > — Wu and Gong (2026), p. 20 **[preprint]**
2. **Constraint sets can be varied systematically and the variation is known to be detectable** — twelve first-order mutation operators applied to two independently implemented policy engines produced measurably different kill rates:
   > "The frozen corpus killed 7 of 12 mutants (58.33%). Subject widening, approval bypass, temporal deletion, fail-open exception handling, and reset omission survived."
   > — Qasim and Kadim (2026), p. 9 **[preprint]**
3. **The full dependent-variable set this study requires has already been specified as a metric template** — task completion rate and policy overhead are defined alongside unsafe-action rate, true block rate, escalation accuracy, and confirmation burden:
   > "actions must be verified at execution time, not trusted by default."
   > — Begum and Rosenzweig (2026), p. 4
4. **A residual-violation sweep under injected enforcement error has been run once, so the STRESS arm has a published precedent** — the curve is known to remain well behaved under non-trivial noise:
   > "First, the environment is synthetic and intentionally stylized; results from a synthetic procurement task do not generalize to real procurement, customer-service, or clinical settings without further empirical work."
   > — Besanson (2026), p. 32 **[preprint]**
5. **Compilation error is a known and separable confound, which is why the ORACLE arm is required rather than optional** — four successive automated designs failed before human-reviewed encodings were adopted:
   > "However, prompt-based guidance does not provide reliable policy enforcement. As policies grow longer and more complex, purely prompt-based enforcement becomes increasingly brittle and harder to validate."
   > — Winston et al. (2026), p. 2 **[preprint]**
6. **Ablating a validation layer is already known to move conformance without moving accuracy, so the two axes of the frontier are empirically distinguishable** — the design depends on that separation and the corpus supplies it:
   > "A system that selects the correct warehouse while failing to detect a cold-storage violation is accurate but unsafe, which is why any evaluation reporting only assignment accuracy will miss safety-layer failures."
   > — Veli (2026), p. 102 **[preprint]**

## Assessment

- **Novelty:** Every enforcement study in the corpus reports one operating point. None sweeps strictness, none reports the joint response at two granularities, and none fits the published cost model to a language model agent. The contribution is a priced frontier plus a decision rule, not another mechanism.
- **Falsifiability:** The flat-recall and flat-violation nulls are both stated in advance and both decisive, and the ORACLE arm prevents a compilation defect from masquerading as a cost of strictness.
- **Feasibility:** The sweep is a single agent and a single policy across roughly a dozen mediator configurations. Its most expensive component, generating the compiled constraint set, is already automated in published work, and the mutation literature shows constraint sets can be varied programmatically.
- **Risk:** The main threat is that the frontier is domain-specific, so a curve fitted on one benchmark misleads elsewhere. Mitigation is to fit the curve on two structurally different domains and report the shape parameters rather than the absolute values. A second threat is that the cost ratios needed for the operating-point analysis are organizational rather than technical facts; mitigation is to report the full grid and the break-even ratios instead of asserting a single optimum.

---

# Topic 3 — The instrument is part of the finding

**Proposed title:** *Compliance You Cannot See: Instrument Sensitivity in the Measurement of Policy Conformance for Tool-Using Business-Process Agents*

## The problem

The standard way to score policy adherence is to compare the final system state against an expected state. That instrument is not neutral, and its bias is asymmetric across exactly the two arms this literature compares. Between 8% and 17% of **successfully completed** trajectories contain a mutating tool call that was made without the mandatory check that policy requires, and because the outcome still matches the gold state, an outcome-only scorer records those trajectories as compliant. Nothing in an agent given only natural-language instructions prevents the skipped check, whereas a blocking mediator does prevent it. The undercount is therefore concentrated in the natural-language arm, every published effect size in favor of constraints is an underestimate of unknown magnitude, and every published null result is uninterpretable rather than negative.

The problem is deeper than a correction factor. Deterministic grading of tool-call traces against procedural manuals shows that the dominant failure is not doing things in the wrong order but skipping mandated gating reads before writes, which accounts for the majority of failed checks across six domains and six models. That is precisely the failure class an outcome metric cannot see, and precisely the class a sequence-shaped process model is least equipped to catch. Meanwhile the corpus contains a clean dissociation in the other direction: removing both validation layers from a pipeline left assignment accuracy unchanged at 0.98 while detected violations fell from 40% to zero. And in a graph-decision setting, frontier models produced correct answers on nearly every sampled case without ever calling a tool, which an accuracy metric rewards and a conformance metric must penalize.

Two further defects close the circle. The strongest enforcement result in the corpus operates before tool activation and therefore cannot, by construction, catch a policy-required call that the agent simply declines to make, so violations of omission are unenforced as well as unmeasured. And where the corpus reaches for an automated judge to scale scoring, that judge agrees with human raters only fairly. A dissertation that holds one comparison fixed and varies only the measuring instrument would give the field the quantity it currently lacks: the size and sign of the measurement-induced bias, and a reporting standard that makes future comparisons commensurable.

## Evidence that this is a problem

1. **Latent policy failures are common inside trajectories that outcome scoring counts as successes** — the rate is measured across six contemporary models on a public benchmark:
   > "We report the latent failure rate on the popular τ 2-bench Airline domain, showing that it ranges between 8% and 17% in successfully completed trajectories across several state-of-the-art open and commercial LLMs."
   > — Rabinovich et al. (2026), p. 2 **[preprint]**
2. **The effect survives human annotation rather than resting on an automated detector alone** — the authors state plainly that the annotation was in-house:
   > "Both Claude-Sonnet4 and Kimi-K2.5 show near-miss rate (NMR) of 7% per human annotation."
   > — Rabinovich et al. (2026), p. 6 **[preprint]**
3. **Policy violations are a large share of all failures even before latent ones are counted** — so the measure is not chasing a marginal phenomenon:
   > "Although not explicitly reported in prior work, our experiments suggest that policy violations account for approximately 25% of all simulation failures in the τ 2-bench Airlines domain"
   > — Rabinovich et al. (2026), p. 1 **[preprint]**
4. **Task accuracy and policy conformance are separable constructs that an accuracy-only design cannot distinguish** — removing both validation layers left accuracy untouched and detection at zero:
   > "A system that selects the correct warehouse while failing to detect a cold-storage violation is accurate but unsafe, which is why any evaluation reporting only assignment accuracy will miss safety-layer failures."
   > — Veli (2026), p. 102 **[preprint]**
5. **The dominant compliance failure is a skipped gating read, which is invisible to a final-state comparison** — deterministic trace grading across six domains locates the failure precisely:
   > "These missing tool calls in particular manifest themselves in the habit of weaker models to write prematurely, i.e., to call a write-style tool before any read-style tool."
   > — Anand et al. (2026), p. 13 **[preprint]**
6. **Models reach correct answers without engaging the tool chain at all, which accuracy rewards and conformance must not** — manual inspection of a random sample makes the gap concrete:
   > "Of 50 outputs: 47 produced correct binary answers with zero tool calls (pure natural language responses);"
   > — Zhu et al. (2026), p. 13 **[preprint]**
7. **The strongest enforcement mechanism in the corpus cannot catch violations of omission, by its own authors' account** — so omission is both unmeasured and unenforced:
   > "First, the proposed approach operates at the pre-tool activation level, meaning it does not capture violation cases where a tool (e.g., flight cancellation) should be invoked according to policy, but the agent chooses not to, thereby breaching the guidelines."
   > — *Towards Enforcing Company Policy Adherence in Agentic Workflows* (2025), p. 7
8. **Automated judges, the obvious way to scale conformance scoring, agree with human experts only fairly** — the substitution is not free:
   > "These metrics indicate that while automated evaluation shows promise for scalability, substantial discrepancies remain that warrant careful interpretation and human oversight"
   > — Kölbel et al. (2026), p. 20

## The experiment

**Design.** An instrument-comparison study in which the comparison is held fixed and only the measurement varies. One agent, one policy, one benchmark, and two arms, an agent given the policy as a natural-language document and the same agent behind a blocking mediator compiled from that document, are run over N tasks with k trials each. Every resulting trajectory is then scored, in parallel and independently, by four instruments plus an omission detector. Scoring is blind to arm: instrument implementations and the human adjudicators receive de-identified trajectories in shuffled order. The estimand is not the effect of the treatment but the **instrument by arm interaction**, which is the measurement-induced bias, reported with a confidence interval and a correction factor.

**Conditions:**
- I1: final-state outcome matching, the current standard
- I2: replay of generated guard code over the trajectory, detecting mutating calls that were not adequately informed
- I3: satisfiability-validated trace checks derived independently from the same procedural document, covering required calls, forbidden calls, and ordering anchors
- I4: human adjudication on a stratified sample, oversampling trajectories on which I1 through I3 disagree
- I5: an omission detector that flags policy-required calls the agent declined to make, the class no runtime mechanism in the corpus enforces
- CTRL-JUDGE: an automated judge scored against I4 on the same sample, to quantify what is lost by substituting a model for a human adjudicator

**Metrics.** For each arm and instrument, the reported quantity is the violation rate with its confidence interval; the headline result is the interaction term and the implied correction factor for the published literature. Secondary results are per-instrument agreement statistics against I4, the proportion of I1-compliant trajectories reclassified by I2, I3, and I5, and a failure-class breakdown separating commission from omission. Falsification is clean: if the instrument by arm interaction is indistinguishable from zero, outcome-only scoring is unbiased for this comparison and the field may keep using it. If the interaction is significant and positive, every prior effect size is a lower bound, and the study delivers the multiplier. A third, non-obvious outcome is available and would be the most consequential: if I5 shows that mediated arms trade commission violations for omission violations, then constraints do not reduce violations but relocate them, and the entire literature has been measuring one half of a conserved quantity.

## Why this approach is viable

1. **The trajectory-replay instrument has been validated against annotation and reaches ceiling performance in its best configuration** — I2 is a working detector, not a proposal:
   > "Among the evaluated agents, GPT-oss-120b achieves the best result with a near-miss rate of 8.6%, followed by Claude-Sonnet4 with 12.1%."
   > — Rabinovich et al. (2026), p. 7 **[preprint]**
2. **The satisfiability-validated trace instrument exists, is cross-validated in both directions, and states its own limits** — I3 can be adopted with its boundary declared rather than assumed:
   > "MANTRA does not provide full formal certification of compliance with the original document."
   > — Anand et al. (2026), p. 13 **[preprint]**
3. **That instrument already discriminates between systems rather than saturating, which is the property an instrument study needs** — no evaluated model was near ceiling:
   > "Another interesting observation is that none of the used models reached very high procedural compliance."
   > — Anand et al. (2026), p. 13 **[preprint]**
4. **Human adjudication at the scale I4 requires has been performed once already** — twelve hundred traces were reviewed by hand in a single study, so the sampling plan here is conservative by comparison:
   > "This suggests that prompt-level policy specification can help when the model attends to the injected rules, but it is not a reliable substitute for world-state-grounded enforcement."
   > — Wu and Gong (2026), p. 16 **[preprint]**
5. **A process model can serve as an oracle while the agent still receives only the natural-language document, which is the configuration this design depends on** — the pattern is established rather than novel:
   > "Consequently, the verifier fundamentally proves the absence of violations against explicitly defined axioms, rather than the absence of unsafe behaviors."
   > — Wu et al. (2026), p. 14 **[preprint]**
6. **The community has stated in print that experimental evidence about process execution is what is missing, which is the gap an instrument study unblocks** — a fifteen-author position from the field itself:
   > "what is still missing are experimental works that provide solid evidence for the effectiveness of LLMs in a process execution context."
   > — Kampik et al. (2024), p. 11

## Assessment

- **Novelty:** Each instrument exists, but no study has run more than one on the same trajectories, and none has estimated the bias that instrument choice induces in the constrained-versus-instructed comparison. The contribution is a measured correction factor and a reporting standard, both of which are prerequisites for the other two topics.
- **Falsifiability:** The null is exact and easy to state, and the design cannot produce it artifactually because scoring is blind to arm and the instruments are implemented independently of one another.
- **Feasibility:** Two arms on one benchmark is the smallest experimental footprint of the three candidates, and the dominant cost is human adjudication on a stratified sample rather than compute. Three of the five instruments are published with released implementations.
- **Risk:** The main threat is that I2 and I3 inherit defects from the generated artefacts they depend on, so an instrument disagreement could be a generation defect rather than a real divergence. Mitigation is to derive I2 and I3 from the same document by independent pipelines, adjudicate every disagreement in I4, and report generation quality as a first-class result. A second threat is that a single benchmark domain limits the correction factor's transferability; mitigation is to preregister a second domain and report the two factors separately rather than pooling them.

---

## Runner-up problems and cross-cutting findings

Four further problems surfaced during the review. Each is real but narrower, better suited to a chapter or a paper than to a dissertation, or blocked by evidence the corpus does not contain.

**Durability of a compiled constraint set.** Every comparison in the corpus is single-session. No study measures whether an artefact compiled from a policy remains correct as that policy changes, as the tool surface evolves, or as the underlying model is revised. The one paper reporting a drift monitor is among the least verifiable in the corpus, so the question is open but currently unsupported by any evidence worth building on. This is the natural extension of Topic 1 once the artefact axis has been isolated.

**Coverage of the world model rather than sophistication of the constraint.** The corpus's clearest mechanistic finding about enforcement quality is that recall is bounded by the facts available to the checker, not by the expressiveness of the rules. That relocates the practical difficulty from writing constraints to supplying the state they need, and it suggests a study of world-model construction cost. It is folded into Topic 1 as the enforcement-site factor rather than pursued separately, because on its own it measures an engineering pipeline rather than agent behavior.

**Manual compilation as the real bottleneck.** Translating human-readable policy into checkable logic repeatedly defeated automation in the corpus and settled on human-reviewed encodings, which makes every reported compliance gain contingent on curation. Two studies name manual constraint authoring as their principal deployment limitation. This is a genuine problem, but it is an artefact-generation problem, and Topic 1's CTRL-ENCODE arm measures its size without requiring a separate dissertation.

**Where a binding model must leave discretion.** The inverse intervention, relaxing a process model by embedding agent nodes at the points requiring judgement, is proposed by Ye et al. (2023) but never evaluated, and the same paper warns that people transfer trust from deterministic workflows onto agents that do not deserve it. The autonomy distinction that this question depends on, between supervised actions and autonomous actions that alter the business without oversight, is drawn cleanly by Schwartz et al. (2023), and Jeong et al. (2025) report a deployed hybrid in which a deterministic policy database carries the routine path while the model advises only on the residue and a human ratifies it. The gap is empirical rather than conceptual, and it needs a discretion benchmark that does not yet exist.

Three cross-cutting observations should travel with any of these topics. First, the corpus's compliance-critical evidence is thin and unrepresentative: one public airline benchmark carries a disproportionate share of the direct evidence, and beyond it there is one internal financial auditing corpus, one corporate collaboration suite, and a handful of synthetic environments, with no healthcare, no lending, no anti-money-laundering, and no regulated production deployment measured independently. Several of the highest-rigour enforcement studies do not evaluate a language model agent at all: Besanson (2026) drives a simulated procurement policy and Gatta (2026) a scripted probabilistic decision model, so both characterize an enforcement or assurance harness rather than agent behavior under instruction. Second, the direct evidence is preprint-dependent: of the studies carrying the sharpest results on the target comparison, most are preprints, while the peer-reviewed portion of the corpus is dominated by framework proposals, vision papers, and case studies without baselines. Third, and most important as a warning rather than a finding, the four papers whose numbers most cleanly report violation reduction with no completion cost are the four weakest in the corpus, scoring 0.438, 0.312, 0.312, and 0.188 on the appraisal checklist. Boinapalli (2026), Dutta (2026), Pulikonda (2025), and Onyekaonwu et al. (2024) release no code, data, or model identifiers, and three of the four contain figures that contradict other figures in the same paper. No claim in this document rests on any of them, and the pattern itself is the caution: the cleanest-looking answers in the published record come from the least verifiable studies.

Finally, this review's own reliability check is a stability measure rather than an inter-rater measure, and correlated error is not excluded. A human second rater over the same 88-record sample, and retrieval of the fifteen unobtained core papers, are both prerequisites for treating any of these three topics as fully scoped.

## References

- Ait, A., Izquierdo, J. L., & Cabot, J. (2025). Towards Modeling Human-Agentic Collaborative Workflows: A BPMN Extension. Lecture notes in computer science, 367-382. https://doi.org/10.1007/978-3-032-04190-6_22
- Anand, A., Chatzi, I., Raha, R., & Schmuck, A.-K. (2026). MANTRA: Synthesizing SMT-Validated Compliance Benchmarks for Tool-Using LLM Agents. arXiv preprint. https://arxiv.org/abs/2605.06334
- Begum, S., & Rosenzweig, M. (2026). A Privacy-Preserving On-Device Multi-Agent Architecture for AI PC (POMA) Workflow Automation. 2026 IEEE International Conference on AI and Data Analytics (ICAD), 1-8. https://doi.org/10.1109/icad69378.2026.11608651
- Besanson, G. (2026). SARC: A Governance-by-Architecture Framework for Agentic AI Systems. arXiv (Cornell University). https://arxiv.org/abs/2605.07728
- Boinapalli, N. R. (2026). GALENA: A Governance-Aware LLM Enterprise Navigation Architecture for Autonomous Multi-Agent Workflow Automation with Compliance Enforcement. https://doi.org/10.64971/j.cph.eijtem.v13.i3.12.2026
- Calvanese, D., Casciani, A., De Giacomo, G., Dumas, M., Fournier, F., Kampik, T., La Malfa, E., Limonad, L., Marrella, A., Metzger, A., Montali, M., Amyot, D., Fettke, P., Polyvyanyy, A., Rinderle-Ma, S., Sardiña, S., Tax, N., & Weber, B. (2026). Agentic Business Process Management: A research manifesto. Information Systems, 140, 102738-102738. https://doi.org/10.1016/j.is.2026.102738 [Abstract only; full text not retrieved.]
- Chaitanya, P. (n.d.). OpenMCPSpec: A Specification Framework for Robust, Governed, and Lifecycle-Managed Machine Communicable Processes in LLM-Agent Systems. 2026 Fourth International Conference on Secure Cyber Computing and Communications (ICSCCC). https://ieeexplore.ieee.org/document/11600150/
- Dutta, P. (2026). Accountable Multi-Agent AI Systems: Orchestration Frameworks for Enterprise Workflow Automation with Human-in-the-Loop Verification. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.19845387
- Gatta, V. S. (2026). Compliance Digital Twins for Autonomous Financial Agents: Reliability-Aware Scenario Assurance via Calibrated LLM Evaluation. Journal of International Crisis and Risk Communication Research, 168-181. https://doi.org/10.63278/jicrcr.vi.3783
- Iyenghar, P., Mansour, Z., & Wuebbelmann, J. (2025). Evaluation of Automated Machinery Functional Safety Risk Assessment Using LLMs. IEEE Access, 13, 203648-203669. https://doi.org/10.1109/access.2025.3632528
- Jeong, C., Sim, S., Cho, H., Kim, S., & Shin, B. (2025). E2E Process Automation Leveraging Generative AI and IDP-Based Automation Agent: A Case Study on Corporate Expense Processing. Artificial Intelligence and Applications. https://doi.org/10.47852/bonviewaia52026307
- Kampik, T., Warmuth, C., Rebmann, A., Agam, R., Egger, L., Gerber, A., Hoffart, J., Kolk, J., Herzig, P., Decker, G., van der Aa, H., Polyvyanyy, A., Rinderle‐Ma, S., Weber, I., & Weidlich, M. (2024). Large Process Models: A Vision for Business Process Management in the Age of Generative AI. K&uuml;nstliche Intell., 39(2), 81-95. https://doi.org/10.1007/s13218-024-00863-8
- Kölbel, L. M., Poss, L., & Schönig, S. (2026). Context is key for cybersecurity: leveraging external knowledge for process model explanation via LLMs. International Journal of Information Security, 25(4). https://doi.org/10.1007/s10207-026-01245-x
- Lins, L. F., Nascimento, N., Alencar, P., Oliveira, T., & Cowan, D. (2023). Comparing Generative Chatbots Based on Process Requirements: A Case Study. https://doi.org/10.1109/bigdata59044.2023.10386251
- Onyekaonwu, C. B., Igba, E., & Anyebe, A. C. P. (2024). Agentic AI for Regulatory Intelligence: Designing Scalable Compliance Lifecycle Systems in Multinational Tech Enterprises. International Journal of Scientific Research and Modern Technology., 205-222. https://doi.org/10.38124/ijsrmt.v3i12.934
- Pacella, M., Papadia, G., & Giliberti, V. (2026). Governed Agentic Process Automation: A Floor-Safety Guarantee for Compliance-Critical LLM Routing. Algorithms, 19(8), 627. https://doi.org/10.3390/a19080627 [Abstract only; full text not retrieved.]
- Park, J. H., & Madisetti, V. K. (2025). CAPRI: A Context-Aware Privacy Framework for Multi-Agent Generative AI Applications. IEEE Access, 13, 43168-43177. https://doi.org/10.1109/access.2025.3549312
- Pulikonda, N. K. M. (2025). Real-Time Regulatory Intelligence Framework: LLM-powered compliance automation for financial services. World Journal of Advanced Engineering Technology and Sciences, 15(2), 3106-3115. https://doi.org/10.30574/wjaets.2025.15.2.0784
- Qasim, H. F., & Kadim, S. A. (2026). PolicyFaultBench: Mutation-Based Assurance of Policy Mediation and Proposal-Interface Conformance for Tool- Using AI Agents. Research Square. https://doi.org/10.21203/rs.3.rs-10502893/v1
- Rabinovich, E., Boaz, D., Zwerdling, N., & Anaby-Tavor, A. (2026). Near-Miss: Latent Policy Failure Detection in Agentic Workflows. arXiv (Cornell University), 296-308. https://doi.org/10.48550/arxiv.2603.29665
- Santos, W. D. S., Coutinho, J. R., Baião, F., Spyrides, G. M., & Lopes, H. (2025). Enhancing declarative business process management availability through generative AI. Process Science, 2(1). https://doi.org/10.1007/s44311-025-00029-1
- Schwartz, S., Yaeli, A., & Shlomov, S. (2023). Enhancing Trust in LLM-Based AI Automation Agents: New Considerations and Future Challenges. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2308.05391
- Towards Enforcing Company Policy Adherence in Agentic Workflows. (2025). Underline Science Inc., 595-606. https://doi.org/10.18653/v1/2025.emnlp-industry.41
  Note. Rendered per APA 7 section 9.12 because the citation_apa field of manifest.json carries a corrupted corporate string in the author position. That field reads, verbatim: "2025, A. F. C. L., Anaby Tavor, A., Boaz, D., Rabinovich, E., Uziel, G., & Zwerdling, N. (2025). Towards Enforcing Company Policy Adherence in Agentic Workflows. Underline Science Inc., 595-606. https://doi.org/10.18653/v1/2025.emnlp-industry.41".
- Veli, E. (2026). A stigmergy-driven multi-agent framework for intelligent task orchestration. UPCommons institutional repository (Universitat Politècnica de Catalunya). https://hdl.handle.net/2117/463237
- Vu, H., Klievtsova, N., Leopold, H., Rinderle-Ma, S., & Kampik, T. (2026). Agentic Business Process Management: Practitioner Perspectives on Agent Governance in Business Processes. Lecture Notes in Business Information Processing, 29-43. https://doi.org/10.1007/978-3-032-02936-2_3 [Abstract only; full text not retrieved.]
- Wang, L. (2026). Open-Rosalind: Tool-First Biomedical LLM Agents with Process-Aware Benchmarking. https://doi.org/10.64898/2026.05.06.722404
- Wang, X., Shu, R., Dan, C., Xu, T., Luo, M., Mai, Y., & Wan, B. (2026). FRAMES: Guarded and Dual-Objective Skill Evolution for Agents in Policy-Governed Enterprise Workflows. arXiv preprint. https://doi.org/10.48550/arxiv.2608.01772
- Winston, C., Winston, C., & Just, R. (2026). Solver-Aided Verification of Policy Compliance in Tool-Augmented LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2603.20449
- Wu, B., Zhang, W., Chen, K., Fang, H., & Yu, N. (2026). Provably Secure Agent Guardrail. arXiv (Cornell University). https://arxiv.org/abs/2605.29251
- Wu, J., & Gong, M. (2026). Policy-Invisible Violations in LLM-Based Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2604.12177
- Ye, Y., Cong, X., Tian, S., Cao, J., Wang, H., Qin, Y., Lu, Y., Yu, H., Wang, H., Lin, Y., Liu, Z., & Sun, M. (2023). ProAgent: From Robotic Process Automation to Agentic Process Automation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2311.10751
- Zhu, H., Liang, J., Hou, M., Tang, R., Zhu, X., Yang, J., Mao, Y., & Wu, F. (2026). From Business Events to Auditable Decisions: Ontology-Governed Graph Simulation for Enterprise AI. arXiv (Cornell University). https://arxiv.org/abs/2604.08603

---

*Distilled from the run artifacts in results/20260905-process-model-constraints-versus-natural. Quotations verified against the run's extracted corpus; citations cross-checked against the run manifest and reference database.*
