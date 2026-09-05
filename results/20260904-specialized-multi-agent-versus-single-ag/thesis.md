# Dissertation Topic Candidates: Specialized Multi-Agent versus Single-Agent LLM Software Engineering

**Author:** Dave Seepersad
**Date:** 2026-09-04
**Program:** Ph.D. in Computer Science, Nova Southeastern University
**Purpose:** This document distills three dissertation-scale research problems from a systematic review of 103 full-text papers on role-specialized multi-agent versus single-agent large language model systems for software engineering. Each candidate targets a contradiction or confound that the reviewed corpus surfaces but cannot resolve on its own evidence.

---

## How these topics were selected

- **Corpus.** 417 unique records were screened after deduplication, 203 were selected for retrieval, and 103 full texts were retrieved and read; 49 were graded core and 54 supporting. Saturation was declared against 20 preregistered evidence domains after zero new domains appeared across read-order windows 3 through 8.
- **Selection rule.** A candidate qualified only if the corpus contains at least two studies with defensible designs that report opposing results on an overlapping question, or a gap that the primary authors themselves name. Topics that merely extend an existing framework were rejected.
- **The binding methodological fact.** Of the 49 core papers, 23 carry a full baseline or control and 19 carry none at all; eight of those 19 nonetheless make explicit comparative claims. Only 16 core papers have both a full baseline and a direct single-versus-multi arm. Mean baseline-or-control score across the appraised core set is 0.541 and mean threats-discussed score is 0.531.
- **Verification.** Every quotation below was located in the run's extracted full-text corpus with an automated substring check that tolerates only PDF extraction artifacts, and every reference string is copied verbatim from the run manifest. Preprints are flagged in each attribution. Where a claim rests on a paper that was screened as core but never obtained in full text, that fact is stated rather than papered over.
- **Provenance caution.** 24 core papers were never retrieved in full text, concentrated in the publisher families hardest to obtain. Two retrieved files were found to contain a different paper than their metadata claimed and were excluded rather than quoted.

---

# Topic 1 — Architecture versus base model

**Proposed title:** *Architecture or Model? A Factorial Study of Orchestration Topology and Base-Model Capability in LLM-Based Software Engineering Agents*

## The problem

The field offers two incompatible explanations for why one agent system outperforms another, and each rests on a design that structurally cannot test the other. One line of work holds the language model fixed and varies the orchestration framework, then concludes that architecture governs behavior. The reciprocal line holds the framework fixed and swaps the model, then concludes that capability is a property of the model rather than the architecture. Both conclusions are stated generally. Neither design licenses a general conclusion, because each estimates one main effect while the other factor is silently held at a single arbitrary level.

This would be a tolerable division of labor if the two factors were additive. They are not. The largest controlled scaling study in the corpus reports that the sign of the coordination effect flips as a function of how strong the single-agent baseline already is, and single-agent strength is itself determined by the base model. That is an interaction term, and an interaction term cannot be recovered from two separate one-factor experiments run by different groups on different benchmarks. Every published ranking of the form *topology X beats topology Y* is therefore confounded with the model it happened to be measured on, and every claim of the form *model M lifts this pipeline* is confounded with the pipeline it happened to be measured in.

The practical cost is direct. An engineering organization choosing between investing in a stronger model and investing in an orchestration layer has no evidence base that separates the two, and the corpus contains same-model head-to-head comparisons that split in both directions — including one study whose own three architectures rank a pipeline above, and a supervisor-worker hierarchy far below, an identical single agent. A dissertation that varies both factors factorially, on one implementation, would convert the field's largest open methodological dispute into a measured variance decomposition.

## Evidence that this is a problem

1. **The architecture-dominant finding is large, and it is measured with the model held constant** — framework choice alone moves latency, planning, and coordination by margins that dwarf most reported model effects:
   > "Our results show that framework-level design choices alone can increase latency by over 100×, reduce planning accuracy by up to 30%, and lower coordination success from above 90% to below 30%."
   > — Orogat et al. (2026), p. 1 **[preprint]**
2. **That design forecloses the model question by construction, yet the conclusion is stated generally** — the authors state the holding explicitly:
   > "Using the MAFBench coordination pipeline, we fix the underlying LLM, task semantics, prompts, stopping criteria, and metric collection, and vary only the communication topology through controlled graph structures."
   > — Orogat et al. (2026), p. 9 **[preprint]**
3. **The reciprocal design produces the opposite general conclusion from a comparable margin** — with the pipeline unchanged, a model swap moves resolution by 13.4 points:
   > "In the Agentless framework, the transition from GPT-4o to Claude 3.5 Sonnet saw resolution rates improve from 27.3% to 40.7% (i.e., relative improvement of 49%). Hence, the improvement is a property of the model, not architecture."
   > — *Demystifying LLM-Based Software Engineering Agents: A Review of Capabilities, Benchmarks, and Failure Modes* (n.d.), p. 6
4. **Same-model head-to-head comparisons split in both directions within a single study** — across 270 executions on one model and one benchmark, the ranking depends entirely on topology:
   > "The Single-Agent Baseline reached a moderate success rate (81.1%) at the lowest cost (0.083 USD per task), while the Hierarchical pattern recorded the lowest success rate (54.4%), the highest median latency (142.37 s), and the highest mean cost (0.308 USD per task)."
   > — Agha & Miqdad (2026), p. 5
5. **At small parameter scale the model term dominates outright** — five coordination strategies over four 7-to-8-billion-parameter models produced a single-agent winner:
   > "These results address RQ1 and RQ2 by showing that model selection has a stronger impact on performance than coordination strategy."
   > — Radeva et al. (2026), p. 22 **[preprint]**
6. **The two factors interact, so neither main effect is estimable from a one-factor design** — the coordination effect changes sign as baseline capability rises:
   > "tasks where single-agent performance already exceeds 45% accuracy experience negative returns from additional agents, as coordination costs exceed diminishing improvement potential"
   > — Kim et al. (2026), p. 6 **[preprint]**
7. **Where both are measured on one benchmark, the architecture effect is marginal and the cost is not** — ten independent runs of black-box test generation:
   > "Although multi-agent architectures achieve superior test coverage — peaking at 99.54% — they yield an ESR comparable to single-agent frameworks (96.98% versus 96.89%)."
   > — Arnaudo et al. (2026), p. 1

## The experiment

**Design.** A fully crossed 3 × 3 × 2 factorial experiment: orchestration topology (single agent, sequential pipeline, supervisor-worker hierarchy) × base model capability tier (a small open-weight model, a mid-tier model, a frontier model) × task family (parallelizable repair tasks versus strictly sequential multi-step tasks). All 18 cells run on one implementation with one tool surface, identical prompts except for role text, an identical per-task token budget, and a fixed retry policy, so that no cell differs from another in anything but the manipulated factors. The protocol, hypotheses, exclusion rules, and stopping rule are preregistered before any cell is executed, and every trajectory is archived. Runs are replicated k times per cell, with k fixed by a power analysis targeting the smallest effect the corpus reports as practically meaningful.

**Conditions:**
- T1-A: single agent, small model, parallelizable tasks
- T1-B: single agent, small model, sequential tasks
- T1-C through T1-R: the remaining sixteen topology × model × task-family cells, each replicated k times
- T1-CTRL: a budget-matched single-agent arm that receives the same total token allowance as the most expensive multi-agent cell, so that any multi-agent advantage cannot be an artifact of extra compute
- T1-CONTAM: every cell re-run on a post-training-cutoff task split to separate capability from memorization

**Metrics.** The primary outcome is task resolution on the contamination-controlled split. Secondary outcomes are input and output tokens, monetary cost, and wall-clock latency, all reported as first-class results rather than appendix material. The analysis fits a mixed-effects model with topology, model tier, and task family as fixed effects, replicate as a random effect, and explicit topology × model and topology × task-family interaction terms; the headline result is a variance decomposition stating what proportion of outcome variance each factor and each interaction explains. The study is falsified in the architecture-dominant direction if the topology main effect explains less variance than the model main effect and the interaction is not significant; it is falsified in the model-dominant direction under the converse. A significant interaction with neither main effect dominating falsifies both published positions simultaneously and is the outcome the corpus most strongly predicts.

## Why this approach is viable

1. **A unified single-implementation harness has already been built to remove exactly this confound** — the authors of the closest existing study name implementation variance as the threat their design controls:
   > "The main threat arises from potential implementation errors in our unified agent framework, which could create confounding variables in our architectural comparison."
   > — Zeng et al. (2025), p. 10 **[preprint]**
2. **Crossing models against roles is already an executed design at smaller scale** — 27 model-role permutations were run and the stated hypothesis was rejected, showing the design produces decidable answers rather than ties:
   > "We cannot accept our hypothesis H1, as one-model MALLMs tend to perform better on specifc websites."
   > — Tomic et al. (2025), p. 9
3. **Per-task cost is low enough that an 18-cell replicated design is affordable** — the corpus's best-controlled architecture comparison reports costs in cents, not dollars:
   > "The Sequential pattern recorded the highest success rate (92.2%), the lowest latency variance (295.56 s2), and a competitive cost (0.089 USD per task)."
   > — Agha & Miqdad (2026), p. 5
4. **A published technique cuts the dominant cost term without disturbing the outcome** — trajectory reduction lowers spend while holding resolve rate flat, extending the achievable replicate count:
   > "After we further consider the computational overhead of the reflection module itself ($+), the final cost reduction becomes 21.1%–35.9%."
   > — Xiao et al. (2026), p. 15
5. **The design answers a methodological requirement the corpus has already stated in print** — a governance analysis prescribes precisely this control:
   > "Compare multi-agent outcomes against individual agents working on decomposable portions of the task to determine if coordination actually improves performance."
   > — Reid et al. (2025), p. 38 **[preprint]**

## Assessment

- **Novelty:** No study in the reviewed corpus varies orchestration topology and base model factorially. The contribution is not a new framework but the first estimate of how much of the observed variance each factor actually explains, plus the interaction term that reconciles the field's two standing positions.
- **Falsifiability:** The variance decomposition and the preregistered interaction test yield a decisive result in three mutually exclusive directions, and the budget-matched control removes the most common alternative explanation for any multi-agent advantage.
- **Feasibility:** Eighteen cells at replicate counts fixed by power analysis, at reported per-task costs in the range of 0.08 to 0.31 USD, is within a doctoral compute budget; the harness, benchmarks, and cost-reduction technique all exist in published form.
- **Risk:** The principal risk is that frontier models are revised mid-study, invalidating cross-cell comparability. Mitigation is version pinning, a fixed evaluation window, and inclusion of at least one open-weight model whose weights cannot change. A secondary risk is that a single unified implementation advantages one topology through incidental engineering choices; mitigation is public release of the harness and an adversarial review of per-topology prompt parity.

---

# Topic 2 — Role decomposition versus execution grounding

**Proposed title:** *Roles or Runtime? A Two-Factor Ablation of Role Decomposition and Execution Grounding in LLM-Based Program Repair and Test Generation*

## The problem

When a role-specialized multi-agent pipeline beats a single agent, two mechanisms are available to explain it, and the literature has never separated them. The first is role decomposition: dividing the task among agents with narrower briefs reduces the reasoning load on any one context and therefore raises the ceiling. The second is execution grounding: somewhere in the pipeline an agent is attached to a compiler, a test runner, a static analyzer, or a simulator, and the resulting non-language feedback signal is what actually repairs the output. Nearly every reported multi-agent gain in software engineering has both mechanisms present at once.

The corpus contains strong ablations on both sides, and each ablates only one factor. One study removes the diagnostic agent, finds the loss negligible, and attributes the pipeline's 17.5-point advantage to decomposition. Another study removes the agents, finds the runtime debugger alone delivers almost the entire benefit, and attributes it to grounding. Both ablations are internally valid. They are not comparable, because neither varies the other factor, and a ladder that removes a *planner* and a *tester* from the same pipeline confounds the two: dropping the tester removes a role and a feedback channel in one move.

The stakes are not academic. Decomposition is expensive — the corpus reports token and latency multipliers of roughly two to eight across independent studies — while attaching a test runner to a single agent is nearly free. If grounding carries most of the effect, a large fraction of current multi-agent engineering is paying a coordination tax for a benefit it could obtain from a single agent with a build loop. If decomposition carries it, the interaction with grounding still needs to be measured before any pipeline can be sized. A dissertation that crosses the two factors in one design, at matched compute, would settle which mechanism the field is actually buying.

## Evidence that this is a problem

1. **One ablation attributes the gain to decomposition, holding model and budget constant** — the diagnostic agent is removed and the advantage survives:
   > "Role decomposition is supported: the single-agent condition, run with the same model and the same budget, detects 17.5 fewer points under the differential criterion."
   > — Li (2026), p. 19
2. **The reciprocal ablation attributes almost the entire gain to the runtime debugger** — across 19 language models, the full agent chain adds under one point to what debugging alone achieves:
   > "In HumanEval, the combined approach achieved 64.82% mean accuracy, compared to 57.16% for ACT alone and 63.86% for Debug alone (comprehensive results in Table I)."
   > — Ashrafi et al. (n.d.), p. 4
3. **The same authors state the mechanistic reading explicitly** — the agent chain is not doing the work:
   > "This suggests Debug alone captures much of the combined approach’s benefits through focused debugging of code blocks and contextual feedback, limiting additional gains from ACT integration."
   > — Ashrafi et al. (n.d.), p. 5
4. **Compiler grounding outperforms both self-repair and a multi-agent collaboration baseline** — the feedback channel, not the agent count, is the operative variable:
   > "The experimental results show that code repair is more effective than directly prompting LLMs to generate codes."
   > — Wang et al. (2024), p. 6
5. **Removing the grounding layer, with the agent left in place, collapses performance to a plain model** — an ablation that isolates grounding rather than roles:
   > "Agent Orchestration (−10.0% F1): removing symbolic and RAG grounding reduces the system to a standard LLM, matching SMOTE’s drop at F1 = 0.820, which confirms that structured reasoning over static metrics is equally critical to balanced training data."
   > — Mohammad et al. (2026), p. 4
6. **The headline multi-agent results confound the two factors inside a single ablation ladder** — removing the tester removes a role and a feedback channel simultaneously, so the ladder cannot decompose the effect:
   > "AGENTFORGE achieves 40.0% task resolution, outperforming the single-agent baseline by +26.0% and the ReAct baseline by +28.0%."
   > — Kumar et al. (2026), p. 7 **[preprint]**
7. **Decomposition without a verification gate falls below the monolithic baseline** — direct evidence that the two factors interact rather than add:
   > "Without clear roles and checks, errors compound across stages and accuracy falls below a competent single model."
   > — Barrak (2025), p. 5
8. **Comparative superiority is asserted in studies that run no comparison at all** — one of eight core papers with no baseline that nonetheless make comparative claims:
   > "Even for models with imperfect first-attempt behavior, the combination of deterministic validation and bounded regeneration significantly increases the final success rate."
   > — Grabowski (2026), p. 11

## The experiment

**Design.** A 2 × 2 factorial ablation crossing role decomposition (monolithic single agent versus a role-decomposed pipeline) with execution grounding (no runtime feedback versus a mandatory build-and-test feedback loop), holding the base model, the tool surface, the prompt content, and the total token budget constant across all four cells. The task domains are automated program repair and unit-test generation, chosen because both admit an objective non-language oracle. Because grounding and decomposition differ in intrinsic compute, every cell is run twice: once at equal wall-clock budget and once at equal token budget, so that neither accounting convention can drive the result. A fifth arm gives the monolithic ungrounded agent the token budget of the most expensive cell, spent on repeated sampling, to test whether any measured decomposition effect is simply purchased compute.

**Conditions:**
- C1: monolithic agent, no execution grounding
- C2: monolithic agent, execution grounding (build, run, test, repair loop)
- C3: role-decomposed pipeline, no execution grounding
- C4: role-decomposed pipeline, execution grounding
- C5: monolithic agent, no grounding, budget-matched to C4 and spent on repeated sampling with self-consistency selection

**Metrics.** The primary outcome for test generation is a differential detection rate computed against a reference implementation, which separates genuine fault detection from language-model test artifacts; the primary outcome for repair is resolve rate verified by held-out tests. Secondary outcomes are tokens, monetary cost, and end-to-end latency per cell, plus a robustness delta measured as the drop from a standard test suite to an augmented one. The analysis reports both main effects and the decomposition × grounding interaction with effect sizes and confidence intervals. The decomposition hypothesis is falsified if, once grounding is enabled and budget is matched, the decomposition main effect is not statistically distinguishable from zero. The grounding hypothesis is falsified if C3 matches C4 while C2 lags C1 by less than the decomposition effect. A significant interaction — decomposition paying only when grounded — is the corpus's most likely prediction and is itself a publishable result.

## Why this approach is viable

1. **A validity-hardened outcome measure for the test-generation arm already exists and is calibrated** — the criterion choice alone moves the reported rate by 35 points, so the study must and can use the conservative one:
   > "The unconditional rate exceeds the differential rate by 35.0 points and the strict rate by 85.0 points."
   > — Li (2026), p. 14
2. **Component ablation at this precision is established practice in the corpus's highest-rigor study** — the losses are reported to three decimal places against a peer-reviewed protocol:
   > "Removing the Requirement Engineer agent and the panel discussion decreases oracle correctness by at least 0.007 and 0.067, respectively."
   > — Xu et al. (2026), p. 4
3. **Decomposition has already been shown to be insufficient on its own, which is the design's core premise** — a naive decomposition underperforms the monolith until a second mechanism is added:
   > "These observations suggest that the key factor contributing to the success of α-UMi lies in its ability to surpass the performance upper-bound of Single-LLM."
   > — Shen et al. (2024), p. 8 **[preprint]**
4. **The expected effect sizes are large enough to detect at feasible sample sizes** — a grounded pipeline lifts a rulebook-equipped single agent by more than 26 absolute points:
   > "Our results demonstrate a substantial improvement in generative AI performance: the rulebook-equipped single-agent baseline achieve only a 47.4% model-level pass rate, while our full multi-agent framework attains 73.7% across generated models."
   > — Abdalla et al. (2026), p. 1 **[preprint]**
5. **Separating a governance or verification factor from an agentic-execution factor has already produced a clean, interpretable split** — the agentic factor was indistinguishable from plain prompting while the verification factor was not:
   > "The evidence suggests that governance, rather than agentic execution alone, is the primary determinant of reliable enterprise software sustaining engineering."
   > — Vella et al. (2026), p. 1
6. **A secondary robustness measure already discriminates between the two factors** — chaining agents degrades stability under expanded test coverage, giving the design a second, independent dependent variable:
   > "AC and ACT showed substantial robustness drops (129.27 and 118.51), showing that agentic interaction introduces fragility."
   > — Ashrafi et al. (n.d.), p. 5

## Assessment

- **Novelty:** No study in the corpus ablates role decomposition and execution grounding within a single design. Both mechanisms are routinely credited, and each is credited by an ablation blind to the other. The contribution is the first interaction estimate between the two.
- **Falsifiability:** Each of the two competing mechanistic claims has a stated null, and the budget-matched fifth arm removes the confound that decomposition simply buys more compute. All four primary outcomes are objective and machine-checkable.
- **Feasibility:** The design is four cells plus one control across two task domains on a single model, which is smaller than several executed studies in the corpus, including one that ran six configurations over 19 language models.
- **Risk:** The main threat is that the grounded feedback signal is itself generated by a language model — brittle generated tests weaken the oracle. Mitigation is to use held-out human-authored tests for scoring and to report generated-test quality separately. A second risk is that results are domain-bound to function-level benchmarks; mitigation is to include a repository-level repair split alongside the function-level one.

---

# Topic 3 — Ground-truth attribution of coordination failure

**Proposed title:** *Injected Ground Truth: A Fault-Injection Benchmark for Measuring Coordination Failure and Failure Attribution in Multi-Agent LLM Software Engineering*

## The problem

Everything the field claims to know about how multi-agent software engineering systems fail is inferred backwards from whether the final artifact worked. Failure taxonomies are built by reading trajectories after the fact and labelling the step where something appears to have gone wrong. That inference is unreliable: on the one benchmark constructed specifically for the task, automated step-level attribution accuracy ranges from roughly a quarter to roughly half. Prevalence figures built on such attribution — *planning causes 55.8% of failures*, *inter-agent misalignment causes X%* — are therefore ordinal impressions rather than calibrated estimates, and they are the empirical basis for most current design guidance.

The problem compounds at the benchmark layer. Audits of agent benchmarks find that essentially none score coordination quality, cost, or trajectory quality, and that the large majority reduce a multi-step collaborative episode to a single binary. Agents that score identically can differ enormously in how they got there. At the same time the outcome metrics themselves have been shown to be unsound for cross-architecture comparison: augmenting an insufficient test suite does not merely lower reported scores, it reorders model rankings, and headline scores on a saturated benchmark collapse when the same systems face uncontaminated tasks. So the field is inferring coordination failure from a signal that does not measure coordination, using an attribution step that is right roughly a third of the time, on benchmarks whose rankings are not stable.

What is missing is a setting in which the cause of a failure is known rather than inferred. Fault injection supplies exactly that: if a specific fault is introduced at a specific inter-agent boundary at a specific step, then the ground-truth answer to *what went wrong, where, and because of whom* is known by construction, and every attribution technique can be scored against it. The infrastructure for trace-aligned injection into real multi-agent software engineering systems has been demonstrated at prototype scale. Turning it into a labelled benchmark, and using it to measure both attribution accuracy and topology-dependent fault amplification, is a dissertation.

## Evidence that this is a problem

1. **Automated failure attribution is unreliable at exactly the granularity the taxonomies require** — a survey of 55 trajectory-analysis papers reports the range:
   > "In terms of reported accuracy, on the Who&When benchmark, reported step-level attribution accuracy varies substantially across techniques, ranging from about 25% [11] to 52% [39]."
   > — Wang et al. (2026), p. 12
2. **The phenomena of interest are invisible to the benchmarks used to study them** — an audit of 15 agent benchmarks states the mismatch directly:
   > "Multi-agent systems bring about coordination failures, emergent behavior and dynamics of interaction that cannot be seen in single-agent benchmarks."
   > — Kehkashan et al. (2026), p. 43
3. **The same audit quantifies how little of the relevant behavior is scored at all** — coordination, cost, and trajectory quality are almost universally unmeasured:
   > "Across all 15 benchmarks examined, the evidence is unambiguous: safety is unscored (0/15), cost is untracked (0/15), trajectory quality is unmeasured in 14/15 cases, and binary success metrics are the sole evaluation criterion in 13/15 benchmarks."
   > — Kehkashan et al. (2026), p. 56
4. **Binary task completion can be identical while the underlying behavior diverges sharply** — in a production deployment, only the process-level metrics exposed the multi-agent failures:
   > "Memory failures increased with scenario complexity, while Environment violations appeared only in multi-agent scenarios where production states changed despite guardrails."
   > — Akshathala et al. (2026), p. 8
5. **Outcome metrics are not merely optimistic, they are order-unstable** — insufficient tests change which system appears best, which invalidates cross-architecture comparison:
   > "We also surprisingly found that test insufficiency can lead to mis-ranking."
   > — Liu et al. (2023), p. 1 **[preprint]**
6. **Headline benchmark scores substantially reflect memorization rather than capability** — the same systems lose 47 points on an uncontaminated benchmark:
   > "This 47-point decline strongly indicates memorization rather than genuine repair capability."
   > — Rodriguez-Cardenas et al. (2026), p. 2
7. **Errors are amplified between origin and observation, and the amplification depends on topology** — so the point where a failure becomes visible is systematically not where it began:
   > "Independent systems amplify errors 17.2× through unchecked error propagation"
   > — Kim et al. (2026), p. 6 **[preprint]**
8. **The orchestration frameworks themselves emit failures that deterministic testing does not catch** — a manual annotation of 1,026 bug instances identifies a symptom class specific to generative systems:
   > "Moreover, we identified Unexpected Output as a significant new symptom category (169 occurrences, 16.5%) uniquely relevant to LLM agent frameworks, reflecting their probabilistic and generative nature."
   > — Xue et al. (2025), p. 9

## The experiment

**Design.** Construct a fault-injection benchmark in which the injected fault is the attribution ground truth. Each task is executed twice against a real multi-agent software engineering workflow: once unperturbed to obtain a baseline trace, and once with exactly one fault injected at a known span — an inter-agent send or receive, a tool call, or a model call — to obtain a structurally aligned faulty trace. Because the injection point, step index, agent, and fault class are chosen by the harness, the correct answer to *which agent, which step, which cause* is known without human labelling. Published attribution techniques are then scored against that ground truth. The same fault schedules are replayed across topologies to measure how far a fault travels before it becomes observable, and end-state success is recorded alongside to demonstrate empirically that it does not discriminate.

**Conditions:**
- F0: unperturbed baseline run, used as the structural reference for every faulty run
- F1: message-layer faults — inter-agent delay, drop, and truncation at a known send or receive span
- F2: tool-layer faults — tool timeout, tool unavailability, and malformed tool response
- F3: model-layer faults — model call delay, rate limit, and malformed response
- F4: semantic faults — a deliberately incorrect but well-formed artifact injected into one agent's output, which no existing timing-based injector covers
- Each condition replayed across three topologies (single agent where applicable, pipeline, supervisor-worker) and, for the semantic class, at three severity levels

**Metrics.** The primary outcomes are attribution precision and recall at agent level and at step level, computed against injected ground truth, for each published attribution technique under test. Secondary outcomes are propagation distance, defined as the number of steps between injection and the first observable deviation from the aligned baseline trace; amplification ratio, defined as extra end-to-end runtime or extra token consumption per unit of injected fault; and recovery rate, the proportion of runs that return to the baseline trajectory. End-state task success is recorded as a negative control. The core hypothesis — that current attribution accuracy is limited by observability rather than by technique — is falsified if attribution accuracy under full trace instrumentation and known ground truth remains within the 25-to-52-percent band reported on existing benchmarks. A topology effect is falsified if propagation distance and amplification ratio do not differ significantly across topologies under identical fault schedules.

## Why this approach is viable

1. **The injection and trace-alignment mechanism has been built and validated on a real multi-agent system** — the two-run aligned protocol this design depends on is already published:
   > "Third, the user optionally enables one or more configured fault rules and re-executes the same task to obtain a structurally aligned faulty run."
   > — Seyedghorban et al. (2026), p. 2
2. **The effect the benchmark must detect is large in the systems of interest** — small injected perturbations produce order-of-magnitude runtime effects, so the measurement is not fighting the noise floor:
   > "Overall, these results highlight that in a multi-phase, message-heavy workflow, the runtime impact of small injected delays can be magnified dramatically"
   > — Seyedghorban et al. (2026), p. 4
3. **Process-level metrics have already been shown to reveal what outcome metrics conceal** — a stage-level fidelity measure exposed a bottleneck that resolve rate alone hid entirely:
   > "Once the correct file is identified, however, all configurations converge to a ∼22% conditional resolve rate, revealing a downstream bottleneck in LLM diff generation."
   > — Liu (2025), p. 1
4. **Trajectory-level annotation at the required scale is established methodology** — 120 trajectories over 2,822 model interactions were coded and yielded discriminating behavioral signals:
   > "Repetition wastes iterations and may induce unproductive loops, as also observed in RQ2."
   > — Bouzenia & Pradel (2025), p. 9
5. **The field has named this gap as its own bottleneck, so the artifact has a defined audience** — the survey that quantifies attribution weakness identifies benchmark scarcity as the limiting factor:
   > "the step-level attribution accuracy remains limited, and benchmark diversity is still a bottleneck"
   > — Wang et al. (2026), p. 1

## Assessment

- **Novelty:** Existing failure-attribution benchmarks rely on human or model-generated labels applied to naturally occurring failures. Injecting the fault makes the label a construction rather than a judgement, which is a categorical change in the evidential status of every attribution number the field reports. No study in the corpus does this, and the semantic-fault class is uncovered by existing injectors.
- **Falsifiability:** Attribution precision and recall against known ground truth are unambiguous quantities with a preregistered comparison band drawn from published results, and the topology hypothesis has a stated null on two independent process measures.
- **Feasibility:** The trace model, span vocabulary, and injection points exist in published, validated form; the work is extension to a semantic-fault class, scale-up to a labelled corpus, and evaluation of existing attributors against it. No new model training is required.
- **Risk:** The chief threat is construct validity — an injected fault may not resemble the naturally arising failures the taxonomies describe, making the benchmark internally valid but externally narrow. Mitigation is to derive the semantic-fault catalog from the failure categories already documented in the corpus and to report attribution accuracy on injected and naturally occurring failures side by side. A second risk is non-determinism swamping the injected signal; mitigation is replication with paired baseline alignment and reporting of per-run variance as a first-class result.

---

## Runner-up and cross-cutting findings

Three further problems recurred across the corpus without reaching the level of a standalone dissertation, and one methodological pattern cuts across all three primary topics.

**Runner-up A: routing as an alternative to fixed role sequences.** The strongest counter-evidence to fixed pipelines is that a router which dispatches by task class beat both a single agent and conventional designer-checker workflows on the same tasks, and had the lowest run-to-run variance, while the fixed sequential workflows underperformed the plain single agent (Youwai et al., 2026). This is a promising design direction, but the corpus contains one such study in one engineering domain, which is too thin a base for a dissertation without first resolving the confounds addressed in Topic 1.

**Runner-up B: complementarity rather than accuracy as the outcome.** Two studies argue that the correct measure of specialization is not accuracy but coverage of defects no single reviewer finds: domain-specialized review agents produced low-overlap findings against a monolithic model on the same pull request (Premasundera, 2025), and cross-lane data-contract defects were unreachable by single-file review by construction (Calboreanu, 2026). Reframing the comparison around complementarity would sidestep the saturated-benchmark problem entirely, but neither study ran the paired control needed to establish the claim.

**Runner-up C: the benchmark-to-deployment transfer gap.** A three-role pipeline deployed inside a commercial issue tracker localized files at 86% recall on a public benchmark against 30% on proprietary enterprise issues (Takerngsaksiri et al., 2025). Enterprise evidence in the corpus is limited to a handful of single-organization studies with self-reported outcomes, and nothing measures the maintenance cost of agent-authored code over time. The topic is important and under-served; it was not selected because access to proprietary corpora is a prerequisite a doctoral candidate may not be able to guarantee.

**Cross-cutting pattern: the missing control is the field's dominant defect.** The same weakness recurs in every direction the corpus is read. Nineteen of 49 core papers carry no baseline; a protocol-driven framework reports failure reductions of up to 69.6% while deferring both its single-agent baseline and its domain-detector baseline to future work (Mao et al., 2025); a routing study excludes single-agent baselines by task construction (Hosseini et al., 2026); a 19-cause failure taxonomy is derived from 104 failures over 204 runs on one benchmark (Lu et al., 2025); a well-designed enterprise study reports a large hierarchical advantage on 90 scenarios authored by the framework's own vendor team (Shu et al., 2024); and a shared-state architecture study computes that roughly 300 issues are needed for adequate power and reports on 50 (Liu, 2025). Variance is rarely reported even though non-determinism is the corpus's most-covered evidence domain. All three primary topics above are, at root, proposals to supply the control the field has been reasoning without.

**A provenance caveat that constrains Topic 1.** The model-dominant side of the architecture-versus-model dispute is represented in this corpus by a second-hand narrative review rather than by the primary study. The primary Agentless work (Xia et al., 2025) was graded core but was never obtained in full text, and it is one of 24 core papers in that category. Any dissertation built on Topic 1 must retrieve and read that primary source before treating the model-dominant position as established, and must not conflate it with the similarly titled review quoted here — they are different documents by different authors.

## References

- Abdalla, A. S., Thie, V., Schaub, J., Eisenbarth, M., Lee, S. H., & Andert, J. (2026). Multi-Agent Software Development for Automotive Model-Based Graphical Programming. IEEE Access. https://doi.org/10.2139/ssrn.6253838
- Agha, M., & Miqdad, A. (2026). An empirical comparison of multi-agent LLM architectural patterns for automated unit test generation. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.20309242
- Akshathala, S., Adnan, B., Ramesh, M., Vaidhyanathan, K., Muhammed, B., & Parthasarathy, K. (2026). Beyond Task Completion: An Assessment Framework for Evaluating Agentic AI Systems. AGENT '26: Proceedings of the 2026 International Workshop on Agentic Engineering, 9-17. https://doi.org/10.1145/3786167.3788414
- Arnaudo, A., Coppola, R., Giobergia, F., Morisio, M., Nguyen, V.-T., Chen, E., Ma, X., Ji, X., & Mai, M.-T. (2026). Automated Black-Box Testing: A Comparative Study of LLM Agent Architectures and Prompt Engineering. 2026 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW), 29-36. https://doi.org/10.1109/icstw72326.2026.00018
- Ashrafi, N., Bouktif, S., & Mediani, M. (n.d.). Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Accuracy, Reliability, and Latency. 2025 IEEE 19th International Conference on Application of Information and Communication Technologies (AICT). https://ieeexplore.ieee.org/document/11268754/
- Barrak, A. (2025). Traceability and Accountability in Role-Specialized Multi-Agent LLM Pipelines. 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW), 315-322. https://doi.org/10.1109/asew67777.2025.00064
- Bouzenia, I., & Pradel, M. (2025). Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 2846-2857. https://doi.org/10.1109/ase63991.2025.00234
- Calboreanu, E. (2026). Iterative Audit Convergence in LLM-Managed Multi-Agent Systems: A Case Study in Prompt-Engineering Quality Assurance. Software, 5(2), 26. https://doi.org/10.3390/software5020026
- Demystifying LLM-Based Software Engineering Agents: A Review of Capabilities, Benchmarks, and Failure Modes. (n.d.). https://journal.duc.edu.iq/index.php/djst/article/view/828
- Grabowski, H. (2026). A Modular Multi-Agent {LLM} Architecture for Text-to-Diagram Generation and User-Guided Refinement. e-Informatica Software Engineering Journal, 20(1), 260109. https://doi.org/10.37190/e-inf260109
- Hosseini, M.-P., Shah, A., Qureshi, S., Huang, A., Miao, C., & Wei, W. (2026). Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent LLM Systems. 2026 IEEE 50th Annual Computers, Software, and Applications Conference (COMPSAC), 179-188. https://doi.org/10.1109/compsac69091.2026.00034
- Kehkashan, T., Abdullah, M., Al-Shamayleh, A. S., Ivković, N., Ismail, N. A., Ahmad, S. S. S., Rehman, A., & Akhunzada, A. (2026). From benchmarks to deployment: a comprehensive review of agentic AI evaluation. Artificial Intelligence Review, 59(8). https://doi.org/10.1007/s10462-026-11571-0
- Kim, Y., Gu, K., Park, C., Park, C., Schmidgall, S., Heydari, A. A., Yan, Y., Zhang, Z., Zhuang, Y., Liu, Y., Malhotra, M., Liang, P., Park, H. W., Yang, Y., Xu, X., Du, Y., Patel, S., Althoff, T., McDuff, D., & Liu, X. (2026). Towards a Science of Scaling Agent Systems. Research Square. https://doi.org/10.21203/rs.3.rs-8414536/v1
- Kumar, R., Ali, W., Ahmed, J., Ali, N. I., & Usman, S. (2026). AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering. arXiv preprint. https://doi.org/10.48550/arxiv.2604.13120
- Li, Y. (2026). A Multi-Agent LLM Framework for Automated Software Testing. Transactions on Computing Science, 2(2), 1-25. https://doi.org/10.63808/tcs.v2i2.447
- Liu, E. (2025). SE-Blackboard: A Shared-State Architecture for Multi-Agent Software Engineering Pipelines. IEEE Access. https://doi.org/10.5281/zenodo.18911614
- Liu, J., Xia, C. S., Wang, Y., & Zhang, L. (2023). Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2305.01210
- Lu, R., Li, Y., & Huo, Y. (2025). Exploring Autonomous Agents: A Closer Look at Why They Fail When Completing Tasks. https://doi.org/10.1109/ase63991.2025.00330
- Mao, Z., Keung, J., Zhang, F., Liu, S., Wang, Y., & Li, J. (2025). Towards Engineering Multi-Agent LLMs: A Protocol-Driven Approach. https://doi.org/10.1109/apsec66846.2025.00100
- Mohammad, F., Kakar, J. K., Ndong, D. R. B. B., Chas, M., & Ryu, D. (2026). CodeQual-Agent: An Intelligent LLM-Agent Framework for Automated Software Quality Assessment with Explainable Predictions and Real-Time Analysis. 2026 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW), 123-128. https://doi.org/10.1109/icstw72326.2026.00035
- Orogat, A., Rostam, A., & Mansour, E. (2026). Understanding multi-agent LLM frameworks: A unified benchmark and experimental analysis. arXiv preprint. https://arxiv.org/abs/2602.03128
- Premasundera, S. (2025). MULTI-AGENT SYSTEM FOR AUTOMATED CODE REVIEWS. Tampere University Institutional Repository (Tampere University). https://trepo.tuni.fi/bitstream/handle/10024/232334/PremasunderaSavidya.pdf?sequence=2
- Radeva, I., Noncheva, T., Doukovska, L., & Popchev, I. (2026). Comparing Single-Agent and Multi-Agent Strategies in LLM-Based Title-Abstract Screening. https://doi.org/10.20944/preprints202603.2107.v1
- Reid, A., O'Callaghan, S., Carroll, L., & Caetano, T. (2025). Risk analysis techniques for governed LLM-based multi-agent systems. arXiv preprint. https://doi.org/10.48550/arxiv.2508.05687
- Rodriguez-Cardenas, D., Li, X., Macedo, M., Mastropaolo, A., Khati, D., Tian, Y., Shao, H., & Poshyvanyk, D. (2026). Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering. FORGE '26: Proceedings of the 2026 IEEE/ACM Third International Conference on AI Foundation Models and Software Engineering, 243-248. https://doi.org/10.1145/3793655.3793716
- Seyedghorban, Z., Klimov, E., van Deursen, A., Panichella, A., & Ozkan, B. K. (2026). Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering. 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST), 211-215. https://doi.org/10.1109/icst69053.2026.00037
- Shen, W., Li, C., Chen, H., Yan, M., Quan, X., Chen, H., Zhang, J., & Huang, F. (2024). Small LLMs Are Weak Tool Learners: A Multi-LLM Agent. arXiv preprint, 16658-16680. https://doi.org/10.18653/v1/2024.emnlp-main.929
- Shu, R., Das, N., Yuan, M., Sunkara, M., & Zhang, Y. (2024). Towards Effective GenAI Multi-Agent Collaboration: Design and Evaluation for Enterprise Applications. arXiv preprint. https://doi.org/10.48550/arxiv.2412.05449
- Takerngsaksiri, W., Pasuksmit, J., Thongtanunam, P., Tantithamthavorn, C., Zhang, R., Jiang, F., Li, J., Cook, E., Chen, K., & Wu, M. (2025). Human-In-The-Loop Software Development Agents. 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP), 342-352. https://doi.org/10.1109/icse-seip66354.2025.00036
- Tomic, S., Alégroth, E., & Isaac, M. (2025). Evaluation of the Choice of LLM in a Multi-Agent Solution for GUI-Test Generation. 2025 IEEE Conference on Software Testing, Verification and Validation (ICST), 487-497. https://doi.org/10.1109/icst62969.2025.10989038
- Vella, S., Ferworn, A., & Sharieh, M. (2026). ATeam: Governance-Aware LLM-Assisted Software Sustaining Engineering for Enterprise Systems. 2026 6th International Conference on Electrical, Computer and Energy Technologies (ICECET), 1-6. https://doi.org/10.1109/icecet65726.2026.11633274
- Wang, H., Liu, Z., Wang, S., Cui, G., Ding, N., Liu, Z., & Ge, Y. (2024). INTERVENOR: Prompting the Coding Ability of Large Language Models with the Interactive Chain of Repair. https://doi.org/10.18653/v1/2024.findings-acl.124
- Wang, J., Wang, Y., Chen, M., Xie, X., Chen, C., Mu, F., Liu, Z., & Wang, Q. (2026). A Survey for LLM Agent Trajectory Analysis: From Failure Attribution to Enhancement. IEEE Transactions on Software Engineering, 1-23. https://doi.org/10.1109/tse.2026.3717765
- Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2025). Demystifying LLM-Based Software Engineering Agents. Proceedings of the ACM on Software Engineering (PACMSE), Volume 2, Issue FSE, 2(FSE), 801-824. https://doi.org/10.1145/3715754
- Xiao, Y.-A., Gao, P., Peng, C., & Xiong, Y. (2026). Reducing Cost of LLM Agents with Trajectory Reduction. Proceedings of the ACM on Software Engineering (PACMSE), Volume 3, Issue FSE, 3(FSE), 1241-1263. https://doi.org/10.1145/3797084
- Xu, Q., Wang, G., Briand, L., & Liu, K. (2026). Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3803418
- Xue, Z., Zhao, Y., Wang, S., Chen, K., & Wang, H. (2025). A Characterization Study of Bugs in LLM Agent Workflow Orchestration Frameworks. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 3369-3380. https://doi.org/10.1109/ase63991.2025.00278
- Youwai, S., Phim, D., Murcia, V. G., & Onas, R. C. (2026). Large language model-based multi-agent systems for automated foundation design: router-driven task classification and expert selection framework. AI in Civil Engineering, 5(1). https://doi.org/10.1007/s43503-026-00088-8
- Zeng, Z., Li, Y., Xie, R., Ye, W., & Zhang, S. (2025). Benchmarking and Studying the LLM-based Agent System in End-to-End Software Development. arXiv preprint. https://doi.org/10.48550/arxiv.2511.04064

---

*Prepared from the systematic review run `results/20260904-specialized-multi-agent-versus-single-ag`: 417 unique records screened, 203 selected for retrieval, 103 full texts read, saturation declared against 20 preregistered evidence domains. Every quotation above was verified against the run's extracted full-text corpus with `corpus_search.py --quote`, and every reference string is reproduced verbatim from `manifest.json`. Preprint status is marked in each attribution.*
