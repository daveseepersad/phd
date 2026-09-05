# Dissertation Topic Candidates: The Agent Harness as a Confounding Variable

**Author:** Dave Seepersad
**Date:** 2026-09-05
**Program:** Ph.D. in Computer Science, Nova Southeastern University
**Purpose:** This document distills four dissertation-scale research problems from a saturation-bounded systematic review of 106 full-text studies on whether the agent harness — scaffold, control loop, retry policy, tool schema — confounds published comparisons of large language model agents. Each candidate targets a question the corpus raises insistently and cannot answer on its own evidence.

---

## How these topics were selected

- **Corpus.** 1,200 raw database records plus 42 from one round of citation chaining reduced to 1,006 unique records after removing 234 duplicates. Screening produced 117 core, 247 supporting, 179 context, 311 exclude and 152 unresolved decisions; 364 records were sought for retrieval, 258 could not be obtained, and 106 full texts were read and synthesized. Saturation was declared against 20 preregistered evidence domains, and the stopping rule held at every trailing-window width from 3 to 8 read papers rather than only at the preregistered width of 5.
- **Selection rule.** A candidate qualified only if the evidence for it spans several independent studies with defensible designs, and only if the primary authors themselves decline to close the question. Topics that would merely add a fifth instance of an existing measurement were rejected, and so were topics whose only contribution would be another proposal that nobody has tested.
- **The binding methodological fact.** The corpus answers its own first question clearly and then undermines the form of the answer. Harness-induced variance exceeded model-induced variance by a factor of 7.80 in the one fully pinned factorial that measured both, but the same grid reversed six of nine model orderings, one controlled study found a single tool worth +9.8 points to one model and −2.4 to another, and an automated scaffold search scored below plain input-output prompting. The harness effect is large, and it is not a scalar.
- **Verification.** Every quotation below was located in the run's extracted full-text corpus by an automated check that tolerates only PDF extraction artifacts and asserts the cited page as well as the wording; quotations that could not be located, or that resolved to a different page, were removed rather than repaired. Every reference string is copied verbatim from the run manifest. All 38 cited works were read at full text; none is cited from an abstract alone.
- **Rigour floor.** Mean rigour across the 106 read papers is 0.768, ranging from 0.375 to 1.000. Seven papers score at or below 0.50, including a harness-engineering survey at 0.38, a modular-benchmarking paper in a journal family advertising an implausible impact factor at 0.44, a harness-resilience position paper at 0.46, and a blockchain-inspired root-cause system at 0.50. No claim in this document rests on any of them; the lowest rigour score among the 38 works cited here is 0.54, and every magnitude claim is carried by a paper scoring 0.69 or above.
- **Preprint caution.** 84 of the 106 read papers carry a preprint flag in the run manifest, and the harness-specific literature is overwhelmingly unrefereed 2026 material. Of the 38 works cited below, 35 are preprints and are flagged as such in every attribution; only three are refereed.
- **Reliability, stated honestly.** A second-rater check over 102 sampled screening records excluded 2 as unratable and reported Cohen's kappa = 0.725 on the remaining 100, at 80.0 percent observed agreement against 27.4 percent expected. **This is not human inter-rater reliability.** The second rater was an independent blind re-prompt of the same language model instrument, so the coefficient measures the stability of the screening decision under repetition, not agreement with a human expert. Disagreement concentrates between *context* and *supporting* and between *supporting* and *core*; *exclude* is the most stable category.
- **Provenance caution.** 258 of the 364 records sought were never retrieved, so the corpus was bounded by retrieval success rather than by eligibility judgement at the full-text stage, and no full-text exclusions were recorded. Two generated artifacts in the run folder, the PRISMA flow file and the evidence ledger, carry a stale topic string from an earlier pipeline run; the counts and extractions in them belong to this review, but the topic label on those two files is wrong and is not evidence about scope.

---

# Topic 1 — Interaction rather than decomposition

**Proposed title:** *When Does the Harness Dominate? Predicting the Model-by-Harness Interaction Term in Large Language Model Agent Evaluation*

## The problem

The field has settled on a framing question — how much of a reported difference between agent configurations belongs to the harness rather than to the model — and that framing quietly presupposes that the answer is a number. A variance decomposition into a model share and a harness share is only meaningful if the two factors combine additively, so that each share stays roughly stable when the other factor is resampled. The corpus assembled for this review shows, repeatedly and from independent designs, that they do not.

The most precise estimate available makes the point against itself. A controlled three-by-three factorial that pinned task order, container runtime, evaluation pipeline, step budget, per-step timeout and decoding settings found harness-induced variance exceeding model-induced variance by a factor of 7.80 — and, in the same grid, six of the nine model-pair comparisons reversed order depending on which harness they were measured under. A ranking reversal is not a large main effect. It is an interaction term big enough to invert the sign of the quantity the decomposition is trying to estimate. Where the sign flips, the sentence *the harness accounts for X percent of the difference* has no stable referent, because X is a property of the particular model pool and harness pool that happened to be sampled.

The same non-additivity appears wherever a study is careful enough to look for it. One controlled experiment toggled a single test-runner tool across seven models on identical fixtures and found it worth +9.8 percentage points to one model and −2.4 to another. A skill-use benchmark run over eight models under two harnesses found rankings stable at the head of the leaderboard and unstable in the middle, with four of eight models reversing the sign of their harness delta. An automated workflow search scored below plain input-output prompting on average, so a scaffold change can be strongly negative. And a post-training study found that applying a rich harness only after reinforcement learning recovered little of the benefit of training with it in place, which means the harness is not even separable from the model's weights, let alone from its identity.

This is not a reason to abandon the question. It is a reason to change it. The scientifically tractable version is not *how much variance is the harness* but *under what conditions does the model-by-harness interaction dominate the main effects, and can that condition be predicted before the grid is run.* The corpus already contains candidate moderators, each observed but none tested as a moderator. Harness-Bench reports that stronger model backends achieve higher mean scores while exhibiting lower cross-harness variance, which makes the harness share a decreasing function of backbone strength. A robustness benchmark found static baselines under an identical harness spanning 0.130 to 0.432 across five models while controller changes shifted any given model by at most about nine points, and a matched-model penetration-testing study found a single model generation inside an unchanged scaffold moving pass@1 by 12 to 25 points against a harness residual of 5 to 10 — both consistent with the interaction shrinking as the capability gap widens. Harness-Bench also localizes the effect by task type, with cross-harness variance highest on structured data and analytics work and near zero on language-centric office tasks, which points at task horizon as a second moderator. A dissertation that converts these scattered observations into a preregistered, out-of-sample-tested moderator model would replace a contested constant with a conditional law.

## Evidence that this is a problem

1. **The best-controlled grid in the literature reports its own interaction term as ranking reversals** — six of nine model-pair comparisons change order with the harness, inside a design where everything else is pinned:
   > "The interaction term is visible as six ranking reversals across the nine possible model-pair / harness-pair comparisons."
   > — Zhang et al. (2026), p. 7 **[preprint]**
2. **A single harness component carries opposite signs for different models under an otherwise identical configuration** — the author names the interaction, not the main effect, as the finding:
   > "This interaction effect—the same tool helping some models while not helping others—is a central empirical finding."
   > — Chen (2026), p. 14 **[preprint]**
3. **Adding a harness layer degrades most models and improves one** — a memory or replay controller over an identical base call is not a uniformly signed treatment:
   > "Blind replay consistently degrades reference-free task success relative to static for four of five models; Kimi K2 is the exception, for which both blind replay and rules-only significantly improve over the static baseline."
   > — Assidiqi et al. (2026), p. 1
4. **Leaderboard position is a property of the pairing, not of the model** — the same eight models reorder when the harness changes, and the authors say so directly:
   > "SU is therefore a property of a model-harness configuration, and rankings under one harness may not transfer to another."
   > — Han et al. (2026), p. 6 **[preprint]**
5. **An automated scaffold search recovers a model-specific optimum that does not transfer** — the workflow found for one executor degrades on another:
   > "This suggests that different language models require different workflows to achieve their optimal performance."
   > — Zhang et al. (2024), p. 8 **[preprint]**
6. **The interaction survives training, so harness and model cannot even be separated across the weight boundary** — a factorial over harness informativeness, model size, algorithm and tool schema concludes:
   > "Our experiments establish that harness design and post-training cannot be treated as separable design choices."
   > — Kim et al. (2026), p. 8 **[preprint]**
7. **A candidate moderator is already visible but untested** — the harness share appears to be a decreasing function of backbone strength:
   > "This pattern suggests that stronger models may be more tolerant of differences in prompting, tool interfaces, state management, and recovery behavior."
   > — Yao et al. (2026), p. 7 **[preprint]**
8. **The authors of the headline ratio refuse to generalize it, and the field quotes it anyway** — the disclaimer is in the same paragraph as the number:
   > "We do not claim that the 7.80× ratio is universal."
   > — Zhang et al. (2026), p. 7 **[preprint]**
9. **Meanwhile the default publication practice changes both factors at once** — which is why the interaction is almost never estimable from the published record:
   > "Because these systems often change both architecture and backbone model, it is difficult to tell how much performance comes from the harness rather than from the underlying model."
   > — Dhakal et al. (2026), p. 1 **[preprint]**

## The experiment

**Design.** A preregistered crossed factorial in which the model-by-harness interaction is the estimand rather than a nuisance residual. Four harnesses spanning a measured configuration distance are crossed with six models sampled to span a wide and *measured* capability gap, over three task families chosen to span horizon length, with replication inside every cell fixed by a power analysis run against the noise floor established in Topic 2. Every non-manipulated factor is pinned in the manner the corpus has already demonstrated: identical task set and task order, one container image, one evaluation pipeline, one step budget, one per-step timeout, one decoding configuration, one gateway.

**Conditions:**

- Harness levels sampled to span a defensible configuration distance rather than convenience, using a published source-code taxonomy to select loop strategy, tool count, context-compaction policy and state-management style as the spanning dimensions.
- Model levels sampled in pairs at three capability separations — near-tied, one generation apart, and two or more generations apart — with separation measured on a harness-independent instrument fixed in advance.
- Task families sampled at short, medium and long horizon, with horizon operationalized as median successful trajectory length under a reference harness.

**Analysis.** A variance-components model with random effects for model, harness and task family plus the model-by-harness interaction, reporting each component with bootstrap intervals rather than point estimates. A second, non-parametric outcome is reported alongside it: the rank-reversal rate, defined as the proportion of model pairs whose ordering changes across harness pairs. Reversal rate is deliberately included because it is robust to the metric's scale and is the quantity that actually invalidates a leaderboard.

**Preregistered moderator hypotheses.**

- H1: the interaction share falls monotonically as the measured capability gap between the compared models widens.
- H2: the interaction share rises with task horizon.
- H3: within a model pool, cross-harness variance falls as backbone strength rises.

**Out-of-sample test.** The moderator model is fitted on the first grid and then used to predict the interaction share of a second, held-out grid built from different harnesses on a different benchmark family. The preregistered success criterion is that the fitted model beats a constant-share baseline on held-out prediction error. This is the step that separates a dissertation from a fifth replication of an existing measurement: a decomposition that cannot predict its own value on a new grid is a description, not a law.

**Metrics.** Variance components with intervals; rank-reversal rate; held-out prediction error against a constant-share baseline; and, reported for every cell, the tokens, dollars and wall-clock consumed, so the grid doubles as an input to Topic 3.

## Why this approach is viable

1. **The decomposition protocol already exists and produces interpretable estimates:**
   > "The grid demonstrates that harness variance can dominate model variance under controlled conditions and that the decomposition protocol produces interpretable estimates on a realistic task distribution."
   > — Zhang et al. (2026), p. 7 **[preprint]**
2. **The pinning discipline the design requires is demonstrated, not hypothetical:**
   > "All agents use temperature 0, tool_choice=required, a maximum of 50 tool calls per attempt, and up to 3 retry attempts with fresh conversation state."
   > — Chen (2026), p. 8 **[preprint]**
3. **Paired designs that hold every non-target factor fixed are already running at scale:**
   > "The paired design holds the task, harness, model, scorer, sandbox, and configured non-target skills fixed, so it is stronger than a single-condition live score."
   > — Kevin et al. (2026), p. 11 **[preprint]**
4. **Control can be pushed all the way down to the action interface, which is what a spanning harness sample needs:**
   > "Consequently, the reachable next states and retrieval substrate are fixed"
   > — Hou et al. (2026), p. 13 **[preprint]**
5. **The cross-harness replication check the out-of-sample arm depends on has been performed before:**
   > "The harness change preserves the distinction between target-omitting concentration and target-retaining breadth."
   > — Ziwei (2026), p. 19 **[preprint]**

## Assessment

- **Novelty:** The corpus contains several factorial grids, but every one of them reports main effects and treats the interaction as an anomaly worth a sentence. None treats the interaction as the estimand, none preregisters a moderator, and none tests whether a fitted decomposition predicts anything on a grid it has not seen. Reframing the field's central question from a constant to a conditional is the contribution.
- **Falsifiability:** Three preregistered directional hypotheses with a stated null, plus an out-of-sample criterion that the moderator model must beat a constant-share baseline. If interaction share turns out to be roughly constant across capability gaps and horizons, H1 through H3 are refuted and the field's scalar framing is vindicated — which is a publishable result in the opposite direction.
- **Feasibility:** Every ingredient is demonstrated in the corpus. The cost is the binding constraint: the one comparable three-by-three grid consumed roughly 261 million tokens and 216 US dollars for two runs per cell, and this design is larger in every dimension and requires more replicates. Scoping to open-weight models on self-hosted inference for the replication-heavy arms is the obvious mitigation, at the price of external validity against frontier systems.
- **Risk:** The chief threat is that harness distance has no principled metric, so the estimated harness variance depends on the sampling distribution over harnesses — a limitation the authors of the headline grid name themselves. Mitigation is to define harness distance in advance over the published taxonomy dimensions, preregister the sampling frame, and report sensitivity of every variance component to harness-pool composition.
- **Dependency:** This topic cannot be executed responsibly before Topic 2. Without an established noise floor, an interaction estimate cannot be distinguished from replication variance, and the corpus already contains a case where a naive crossing sat exactly at the noise floor and was uninterpretable.

---

# Topic 2 — The measurement floor

**Proposed title:** *The Minimum Detectable Effect in Agent Evaluation: A Replication-Based Noise Floor for Harness and Model Comparisons*

## The problem

Every number in the harness literature is an unlabelled sum of signal and replication noise, because almost nobody measures the noise. Exactly one study in this corpus reports a same-configuration floor: re-running the same frozen commit moved its score by roughly ±4.75 pair-score points, which is wide enough to swallow the majority of the 64 version switches that same paper observed. A second study measured a run-to-run resolution limit of about 1.5-fold typical spread and concluded that its own headline interface comparison could not be resolved in either direction. A third found that the crossing point it had treated as evidence of an orchestration advantage sat precisely at the noise floor. When the floor is measured, it routinely turns out to be the same size as the effect.

The obvious remedy — set a seed, fix the temperature — does not work, and the corpus explains why. Hosted inference is nondeterministic at temperature 0 for reasons that have nothing to do with sampling: floating-point non-associativity and batch-size-dependent kernels make the provider's own output a random variable, and some frontier models no longer accept a temperature parameter at all. On top of that, providers swap model weights behind stable endpoint names without notice and aggregators can serve different quantizations of the same endpoint on successive calls, so two runs a week apart are not necessarily two runs of the same system. The floor therefore has at least three components — within-cell replication, seed or sampling variation where it is controllable at all, and provider drift across time — and no published study estimates more than one of them.

The reporting record makes this worse than an oversight. A full-text audit of the sixteen studies in a scoping review that directly observe language-model multi-agent systems found seed reported in zero, sampling frequency in zero, number of runs in three and temperature in one, while model version, dataset, task and baseline were reported in all sixteen. The field documents what it studied and omits what it would take to know whether the result is repeatable.

Two further findings show that a single floor is not enough, and this is where the naive version of the topic has to be sharpened. First, the floor depends on the statistic. A fairness pilot demonstrated that comparing a six-group spread against a two-run pairwise difference inflates an apparent effect by roughly 2.4-fold through statistic arity alone, and showed an earlier draft of its own work reading that artifact as signal; once the null was arity-matched, every one of its scaffold effects fell below its own floor. Second, the floor depends on the slice. A deliberately injected single-layer scaffold regression moved an aggregate pass rate by only 1.7 to 5.9 points — dismissible as dashboard noise — while the responsible layer's own assertion slice collapsed by 25 to 91 points. A floor computed on an aggregate therefore cannot license a claim about a component, and a component-level floor cannot license a claim about the aggregate. What the field needs is not one number but a floor *function* over harness, model, task, metric and statistic arity, together with the run counts each cell would require to detect the effects people actually report.

## Evidence that this is a problem

1. **The only measured same-configuration floor in the corpus swallows most of the effects measured against it:**
   > "The same commit can vary by about ±4.75 pair-score points, so small gains cannot be attributed to code changes from score alone."
   > — Wu et al. (2026), p. 13 **[preprint]**
2. **The nondeterminism is provider-side, so pinning a seed does not remove it:**
   > "Providers are not deterministic. Even at temperature 0, hosted inference varies because of floating-point non-associativity and batch-size-dependent kernels"
   > — Shah (2026), p. 2 **[preprint]**
3. **The parameters that would let a reader bound the noise are essentially never reported:**
   > "Reproducibility reporting is limited: seed, number of runs, and sampling frequency are not reported in any study."
   > — Ahumada (2026), p. 1 **[preprint]**
4. **When a study does measure its resolution limit, the limit is large enough to void its own headline comparison:**
   > "This is the resolution limit of the study: a difference smaller than roughly twofold cannot be distinguished from run to run variation."
   > — Forment et al. (2026), p. 20 **[preprint]**
5. **The floor depends on the statistic, and getting the arity wrong manufactures effects** — a pilot that corrected its own error reports the consequence:
   > "But after the arity correction of Finding 1, every one of these values is below its own noise floor"
   > — Morla et al. (2026), p. 9 **[preprint]**
6. **An architecture result that looked like a crossing was a coincidence of sampling maxima:**
   > "The naive crossing sits at the noise floor and is uninterpretable."
   > — Strain (2026), p. 19
7. **The floor also depends on the slice, so one aggregate floor cannot govern component claims:**
   > "The effect we did not design in is masking—the aggregate pass-rate barely moves (−1.7 to −5.9 pp for six local regressions), small enough to vanish into dashboard noise, while the matching slice craters (−25 to −91 pp)."
   > — Zhang et al. (2026), p. 1 **[preprint]**
8. **Run-level instability is visible whenever anyone runs a configuration more than once:**
   > "The results suggests that the underlying stochasticity of the agent caused it to not consistently solve the same tasks."
   > — Siegel et al. (2024), p. 21 **[preprint]**
9. **A third variance component, drift in the system under test, is documented and almost never accounted for:**
   > "Providers swap model weights behind stable endpoints without notice."
   > — Kapoor et al. (2025), p. 20 **[preprint]**

## The experiment

**Design.** A replication study whose only purpose is to characterize the floor, executed at three nested levels and then applied retrospectively to the published record. Level one is within-cell replication: for each of a fixed set of harness-by-model-by-task cells, execute k identical runs back to back and estimate replication variance. Level two is decoding variation: where a seed or temperature is exposed, repeat the cell across a seed grid and separate seed variance from irreducible provider variance. Level three is temporal drift: re-execute the identical cell at fixed intervals over several months, with the endpoint name, harness commit and container digest held constant, so that any movement is attributable to the provider rather than to the experiment.

**Outputs.**

- A floor function reporting the minimum detectable effect as a function of harness, model, task family, metric and number of runs, published as a power calculator rather than as a table of numbers that will age.
- A required-n table: for the effect sizes the corpus actually reports — a 2-point pass-rate difference, an 8-point difference, a 23.8-point harness gap — the number of runs needed to detect them at conventional power.
- Separate floors for aggregate and sliced metrics, with the masking ratio reported as a first-class quantity.
- An arity-matched null construction, so that many-group spreads are never compared against two-run pairwise differences.

**Retrospective arm.** Harvest every within-model cross-harness delta reported in the corpus, pair each with its reported run count where one exists, and compute the fraction that exceed the corresponding floor. The preregistered hypothesis is that a majority of published harness deltas are not distinguishable from replication noise at their reported run counts. The secondary and more uncomfortable finding will be how many deltas cannot be evaluated at all because no run count was reported, which is a direct measurement of the disclosure problem in Topic 4.

**Metrics.** Variance components by level with intervals; minimum detectable effect curves; masking ratio between aggregate and sliced metrics; proportion of published deltas above floor, below floor and unevaluable.

## Why this approach is viable

1. **The field has already scheduled this work and not done it** — a corpus paper lists the repeated-measurement floor as a planned revision:
   > "Version 1.1 will pin sampling temperature, average across replicate runs, and ship a repeated-measurement noise floor, which together give a sharper separation between stochastic noise and any systematic effect."
   > — Morla et al. (2026), p. 11 **[preprint]**
2. **The statistical machinery is standard and already in use on exactly these outcomes:**
   > "Bootstrap uncertainty is reported as 95% paired-task bootstrap intervals (B = 10,000) for both pass rate and tokens per solved task."
   > — Vats & Golev (2026), p. 3 **[preprint]**
3. **The freeze-and-standardize protocol the design needs has been implemented:**
   > "Every score is produced by a frozen harness in a standardized runtime."
   > — Wu et al. (2026), p. 6 **[preprint]**
4. **The attribution logic that makes a floor necessary is already formalized:**
   > "Magnitude alone cannot localize the cause."
   > — Shah (2026), p. 3 **[preprint]**

## Assessment

- **Novelty:** No study in this corpus estimates more than one variance component, none separates provider drift from replication noise, and none publishes a minimum-detectable-effect curve. The retrospective arm is entirely new: nobody has asked what fraction of the field's published harness effects survive contact with a measured floor.
- **Falsifiability:** The central hypothesis is a proportion with a preregistered threshold. If most published deltas comfortably exceed the floor, the hypothesis fails and the field's existing results are vindicated, which is equally worth publishing.
- **Feasibility:** This is the most tractable of the four topics. It requires no new modelling, no new benchmark and no novel statistics — only disciplined repetition and honest accounting. It is embarrassingly parallel and the per-cell cost is bounded by the smallest task suite that preserves the effect sizes of interest.
- **Risk:** Two risks dominate. Provider drift may be so large that the temporal arm produces an uncomfortably wide floor, in which case the finding is that hosted-endpoint agent evaluation is not a reproducible practice at all — a serious claim that must be defended with self-hosted controls. Second, the retrospective arm depends on reported run counts, which are frequently absent; the mitigation is to treat unevaluable deltas as a reported category rather than dropping them.
- **Position in the sequence:** This is the enabling topic. Topics 1 and 3 both produce numbers that cannot be interpreted without it, and Topic 4 needs it to decide whether a reproduction gap is a failure of disclosure or ordinary noise.

---

# Topic 3 — The accuracy-per-dollar frontier

**Proposed title:** *Budget-Matched Cost Accounting for Agent Harnesses: Characterizing the Accuracy-per-Dollar Frontier as a First-Class Evaluation Outcome*

## The problem

Cost and accuracy come apart under harness variation more sharply than under any other manipulation in this corpus, and the field measures only one of them. Holding model, task instruction, test suite, sandbox and wall-time cap constant, harness choice moved tokens per solved task by roughly 40-fold while a model upgrade moved the same quantity by 1.0 to 1.3-fold — and over the same conditions the pass-rate differences stayed inside 0 to 8 points with bootstrap intervals mostly spanning zero. The largest standardized evaluation in the corpus records a 9-fold cost difference for a two-percentage-point accuracy difference on one benchmark. A seven-scaffold comparison on one task with identical models and verification found a factor of 20 between the cheapest and most expensive scaffold, and 139-fold for a single small model that completed the task under all of them. Five scaffolds wrapping identical weights produced solve rates clustering within about five points while cost per solve ranged from 104 to 341 US dollars. On the same backbone, framework choice moved energy consumption 9.4-fold.

That is a decision-relevant frontier and nobody has characterized it. The disclosure audit in this corpus found that none of the eight agent benchmark papers it examined reported inference cost in any form; the cost field's mean score was exactly zero. Practitioners are therefore choosing between a stronger model and a different harness with published evidence on only one axis, and the axis they can see is the one where the harness matters least.

The naive version of this topic — plot accuracy against cost and find the Pareto frontier — is under-specified in three ways this corpus exposes, and correcting them is the actual research contribution. First, the currency is not settled. Tokens are not dollars, because prices differ per model and change; dollars are not energy, and an energy study found consumption correlating strongly with wall-clock duration and output tokens but near zero with memory metrics, so no single proxy stands in for the rest. Worse, *tokens per solved task* is an accuracy-conditioned ratio whose denominator can approach zero: in the energy study, resolution rates were 4 percent in the best cell and 0 percent everywhere else, which makes the headline efficiency ratio unstable exactly where efficiency claims are most tempting. Second, the frontier is confounded with budget. One controlled study clamped a pipeline's token budget toward its baseline and found its advantage no longer detectable, so an architecture's position on a cost-accuracy plot partly encodes the compute it was permitted to spend rather than any property of its design. Third, aggregate cost hides where the money goes: separating solved from failed scans showed most wasted budget being spent *after* the agent has already stopped making progress, which means the actionable quantity is outcome-conditioned cost and not cost per task. A dissertation that measures a budget-matched, multi-currency, outcome-conditioned frontier and tests whether harness cost-efficiency rank transfers across models would give the field its missing axis.

## Evidence that this is a problem

1. **The cost asymmetry between harness and model is not close, and it runs opposite to where the field looks:**
   > "The cost-side asymmetry is overwhelming: harness choice shifts tokens-per-solved-task by 40×, while upgrading the model barely moves it (1.0–1.3×)."
   > — Vats & Golev (2026), p. 5 **[preprint]**
2. **The largest standardized evaluation infrastructure reports the same divergence as a headline:**
   > "Agent scaffolds create drastic differences in cost and accuracy."
   > — Kapoor et al. (2025), p. 7 **[preprint]**
3. **A controlled seven-scaffold comparison isolates the effect to the scaffold and nothing else:**
   > "The task, the models and the verification were identical in every row; only the scaffolding driving the model changed. Between the cheapest and the most expensive lies a factor of 20."
   > — Forment et al. (2026), p. 10 **[preprint]**
4. **Model and harness bind different outcomes, so a single-axis evaluation cannot see the trade:**
   > "The SLM's limited reasoning was the bottleneck for success, but the framework's design was the bottleneck for efficiency."
   > — Tripathy et al. (2025), p. 1 **[preprint]**
5. **A quarter of continuous harness development bought no capability and roughly doubled the bill:**
   > "Worse, later agent harness versions consume nearly double the computational tokens and tool calls without corresponding quality gains."
   > — Sghaier et al. (2026), p. 1 **[preprint]**
6. **A frontier position can be an artifact of the budget the system was allowed rather than of its design:**
   > "The probe certifies one claim: at matched budget P1's advantage over P0 is no longer detectable."
   > — Strain (2026), p. 20
7. **Aggregate cost conceals the operationally important quantity:**
   > "Table XI separates solved scans from failed scans because most wasted budget is spent after the agent has not found a viable exploit path."
   > — Dhakal et al. (2026), p. 7 **[preprint]**
8. **And the field's benchmark papers do not report cost at all:**
   > "none of the eight agent benchmarks report inference cost in any form. The agent-benchmark cost mean is exactly 0.00."
   > — Moghadasi & Ghaderi (2026), p. 5 **[preprint]**

## The experiment

**Design.** A budget-matched Pareto study. Harnesses are crossed with models and with explicit budget caps, so that budget becomes a manipulated factor rather than a nuisance the harness silently sets. Each cell is executed at three budget levels — a tight cap, a moderate cap and an uncapped control — with the cap enforced identically across harnesses on a harness-independent quantity, which the corpus shows is non-trivial because some harnesses expose no turn-budget flag and are bounded only by wall time.

**Multi-currency accounting.** Every run records five cost quantities rather than one: input and output tokens; dollars at a dated, published price sheet frozen before execution; wall-clock time; tool-call count; and measured energy at the CPU and GPU package level. Reporting all five is itself a contribution, because the corpus shows the proxies disagreeing, and because a study that reports only tokens cannot be repriced later.

**Outcome-conditioned reporting.** Cost is broken out by outcome — cost per solved task, cost per failed task, and the share of spend occurring after the last productive action — using trajectory logs rather than totals. The last of these is the quantity a practitioner can actually act on, and it is reported in only one study in the corpus.

**Transfer test.** The preregistered hypothesis is that harness cost-efficiency *rank* is largely model-invariant even though absolute cost is not. This is a direct extension of the finding that harness-specific failure fingerprints replicate across models, and it is falsifiable: if the ordering of harnesses on cost per solved task reorders across model families, then cost, like accuracy, is a property of the pairing and no harness can be recommended on efficiency grounds without naming its model.

**Metrics.** Pareto frontier membership at each budget level; accuracy per dollar and accuracy per joule with intervals; Kendall rank correlation of harness cost-efficiency ordering across models; share of budget spent post-productivity; and the sensitivity of every frontier claim to the choice of currency.

## Why this approach is viable

1. **The frontier infrastructure exists and is already public:**
   > "Shows accuracy vs. cost trade-offs. Only Pareto-optimal agents are labeled."
   > — Kapoor et al. (2025), p. 41 **[preprint]**
2. **The control discipline required for a clean cost comparison has been demonstrated:**
   > "Held constant: verbatim Terminal-Bench Pro instruction; native test suite; Daytona sandbox per task; 900-second wall-time cap per trial; OpenRouter as the model gateway."
   > — Vats & Golev (2026), p. 2 **[preprint]**
3. **Fixed-model, multi-scaffold cost comparison has been run end to end in a demanding domain:**
   > "All scaffolds compared in this paper share the same model (alias2-mini), the same per-challenge wall-clock timeout drawn from the upstream cybench Est. Time field, and the same per-challenge harness."
   > — Mayoral-Vilches et al. (2026), p. 3 **[preprint]**
4. **Energy instrumentation for agent frameworks is established, including its own limitations:**
   > "We find that framework architecture is the primary driver of energy consumption."
   > — Tripathy et al. (2025), p. 1 **[preprint]**

## Assessment

- **Novelty:** The corpus contains at least five cost-accuracy plots, and each is a single-study snapshot at whatever budget its harnesses happened to choose. None is budget-matched across harnesses, none reports more than two currencies, only one reports outcome-conditioned cost, and none tests whether cost-efficiency rank transfers across models. The frontier itself is unmeasured.
- **Falsifiability:** The transfer hypothesis has a clean statistical test with a stated null, and the budget-matching arm has a preregistered prediction — that a measurable share of published harness advantages will vanish under budget matching, as one study has already shown for orchestration.
- **Feasibility:** High, and the highest practical payoff of the four. The design is a sweep rather than a novel method; the main engineering work is enforcing a budget cap uniformly across harnesses that expose different control surfaces, and instrumenting energy on controlled hardware.
- **Risk:** Price sheets drift and vendor pricing is not a stable measurement instrument; the mitigation is to freeze and publish a dated price sheet and to release token counts so that every dollar figure can be recomputed. Energy measurement at the package level excludes memory, storage and wall-plug draw, so energy claims must be scoped to the measured envelope. Finally, tokens per solved task is unstable at low solve rates and must not be reported for cells below a preregistered minimum resolution rate.
- **Dependency:** Accuracy differences on the frontier are subject to the same floor as Topic 1, so cost claims can be made independently but accuracy claims cannot.

---

# Topic 4 — From disclosure to reproduction

**Proposed title:** *Is Disclosure Sufficient? A Reproduction Study of Harness-Disclosed Large Language Model Agent Results*

## The problem

The most decisive finding in this review is not about effect sizes at all. It is that the published record is structurally unable to answer the harness question, because the information required is absent. An audit of 66 language-model program-repair systems counted 2,145 possible pairwise comparisons, found only 100 sharing a benchmark label, only 32 falling inside bounded comparison windows, and exactly one pair that is model-controlled — and that single pair sits inside one paradigm, so the literature contains no model-controlled cross-paradigm comparison at all. Independently, the largest standardized agent evaluation found that only 2 of its 9 benchmarks had ever been run with the same scaffold across four or more of the models being compared. A third audit found the execution parameters missing: seed in zero of sixteen studies, sampling frequency in zero, number of runs in three, temperature in one. A fourth, on the supply side, found harness specification to be the field's worst-reported item, with seven of eight agent benchmarks scoring half marks, one scoring zero, none scoring full, and none pinning a content-addressed image for the evaluation environment.

Composed, these say something stronger than *reporting could be better*. They say that most published cross-configuration agent comparisons cannot in principle distinguish a harness effect from a model effect from noise, not because the analyses are wrong but because the information needed to check them was never recorded. Disclosure, not measurement, is the binding constraint on cumulative science in this area.

The naive response is to propose a reporting standard, and this is exactly where the topic must be developed critically rather than accepted. Three such proposals already exist inside this corpus alone: a harness card paired with a variance-decomposition protocol, a lightweight harness card presented as a fuller disclosure schema, and an open scoring schema with a machine-readable manifest. None has been tested. The authors of one of them state plainly that their paper argues agent improvements are harness-sensitive but supplies no controlled ablation of its own, and present their card as an untested proposal rather than a validated standard. A fourth card would add nothing.

The genuinely open question is whether disclosure is *sufficient* — whether a fully disclosed configuration actually reproduces. The corpus supplies concrete reasons to doubt it. Providers swap model weights behind stable endpoint names and aggregators serve different quantizations under one name, so a disclosed model identifier does not identify a system. Harness inventories decay in weeks, so a disclosed version pin may point at an artifact that no longer builds. And agents frequently ignore the tool interface they are assigned, so a disclosed interface is not necessarily the interface that was used, and a study that assigns one without verifying it measures an unknown mixture. If reproduction gaps remain above the noise floor even for the best-disclosed papers, then the remedy is not better cards but content-addressed artifacts, mandatory re-runs and endpoint-independent inference — a materially different prescription, and one no one has evidence for.

## Evidence that this is a problem

1. **In one entire literature, exactly one comparison is model-controlled:**
   > "no model-controlled cross-paradigm comparison exists. Benchmark-name overlap therefore does not support a paradigm leaderboard."
   > — Yang et al. (2025), p. 41 **[preprint]**
2. **Independently, the scaffold is almost never matched across the models being compared:**
   > "We found that only 2 of these benchmarks were ever evaluated with the same agent scaffold for 4 or more models from this list, making cross-model comparison hard (Section A9)."
   > — Kapoor et al. (2025), p. 2 **[preprint]**
3. **A full-text audit finds the asymmetry is systematic, not incidental:**
   > "the descriptive elements of the experiment are documented consistently, while the parameters needed to characterize execution, replication, and stochastic variability are documented much less frequently."
   > — Ahumada (2026), p. 6 **[preprint]**
4. **On the supply side, the harness is the single worst-disclosed field:**
   > "The harness field is universally partial."
   > — Moghadasi & Ghaderi (2026), p. 5 **[preprint]**
5. **The practical consequence is already visible to readers of the literature:**
   > "two papers will report results on the same benchmark with the same model name, and the numbers will disagree, and you cannot tell why."
   > — Moghadasi & Ghaderi (2026), p. 1 **[preprint]**
6. **Under-description also inflates apparent contribution, which is an incentive problem, not only a hygiene one:**
   > "A language-agent paper can appear more novel than it really is if the harness is under-described."
   > — He et al. (2026), p. 8 **[preprint]**
7. **A disclosed model name does not identify a system, so disclosure alone may not be enough:**
   > "We also found that some providers swap model weights behind the same endpoint without notice, and aggregators like OpenRouter could serve different quantizations of a model for the same endpoint name by default."
   > — Kapoor et al. (2025), p. 4 **[preprint]**
8. **Nor does a disclosed version pin, because the artifacts move faster than the papers:**
   > "inventory claims (tool counts, feature cells, version pins) decay in weeks, while structural claims (loop taxonomy, subsystem anatomy, the absences) have so far proven durable."
   > — Barbaste et al. (2026), p. 63 **[preprint]**
9. **Nor does a disclosed interface, because agents do not necessarily use the one they are given:**
   > "A measurement that assigns an interface without verifying which interface was used reports the cost of an unknown mixture."
   > — Forment et al. (2026), p. 19 **[preprint]**

## The experiment

**Design.** Two arms, run against each other rather than in sequence.

**Arm A — the reproduction arm.** Select the most completely disclosed harness-bearing results the literature offers, stratified by disclosure score, and attempt exact reproduction under the disclosed configuration. Every reproduction is executed three ways: on the original hosted endpoint, on a pinned self-hosted equivalent where the weights permit it, and on the original endpoint again after a fixed interval. The outcome is the reproduction gap — the difference between the published number and the reproduced number — evaluated against the floor established in Topic 2 rather than against zero, so that ordinary replication noise is not mistaken for a reproduction failure.

**Arm B — the audit arm.** Extend the existing twelve-paper disclosure pilot to a stratified sample of 50 to 100 papers with two independent raters, which is precisely the extension the pilot's own authors say a representative audit would need. Report Cohen's kappa between raters, and label it as human inter-rater reliability only if the raters are in fact human.

**The joint analysis.** Regress reproduction gap on disclosure score. The preregistered hypothesis is that disclosure score predicts reproduction gap but does not close it: that even the best-disclosed papers show gaps above the noise floor, driven by provider drift, artifact decay and interface non-compliance rather than by missing fields. Three named mechanisms are instrumented directly so the residual can be attributed: endpoint identity is checked by re-running a fingerprint probe before and after each reproduction; harness artifacts are captured as content-addressed images at reproduction time; and the interface actually exercised is recovered from trajectory logs rather than assumed from configuration.

**Deliverable.** Not a fourth reporting card, but an evidence-backed answer to which disclosure fields actually reduce the reproduction gap, and which are ceremonial. Fields that do not move the gap are removed from the recommendation; fields that do are ranked by effect. A standard justified by a measured reproduction gap is a different object from a standard justified by plausibility.

**Metrics.** Reproduction gap in benchmark units and in floor units; proportion of reproductions inside the floor; per-field marginal reduction in gap; inter-rater kappa on the audit; and the attributable share of residual gap assigned to endpoint drift, artifact decay and interface non-compliance.

## Why this approach is viable

1. **There is precedent for a field absorbing reporting expectations, and the pilot names it:**
   > "The ML/CV community has previously absorbed conference-level reporting expectations (the ML Reproducibility Checklist, datasheets, model cards), and adoption of those was not instant but did happen."
   > — Moghadasi & Ghaderi (2026), p. 7 **[preprint]**
2. **A candidate disclosure schema already exists in expanded form, so the audit instrument does not have to be invented:**
   > "The template below expands the compact main-paper version of HARNESS CARD into a fuller disclosure schema."
   > — He et al. (2026), p. 16 **[preprint]**
3. **The comparability-auditing method is established at the level of individual reported results, not benchmark names:**
   > "Shared benchmark names alone do not determine whether published repair scores are comparable."
   > — Yang et al. (2025), p. 36 **[preprint]**
4. **Automated computational reproduction is itself a working research instrument with published baselines:**
   > "Our baseline results show that while automating computational reproducibility is hard, simple task-specific modifications to existing general-purpose agents can already help increase accuracy."
   > — Siegel et al. (2024), p. 13 **[preprint]**
5. **And the field's most detailed source-code study names the missing study explicitly:**
   > "Whether the production scaffolding produces measurable improvements on the same benchmark under matched conditions is an open question that this study does not answer"
   > — Barbaste et al. (2026), p. 58 **[preprint]**

## Assessment

- **Novelty:** Three disclosure standards have been proposed in this corpus and none has been evaluated. Reframing the question from *what should be disclosed* to *does disclosure reproduce* is the contribution, and it inverts the field's assumption: if the residual gap is dominated by provider drift and artifact decay, then better cards are the wrong intervention.
- **Falsifiability:** The central hypothesis states a direction and a threshold — reproduction gaps above the noise floor even in the top disclosure stratum. If well-disclosed papers reproduce inside the floor, the hypothesis is refuted and the field's existing card proposals are vindicated as sufficient, which is a clean positive result.
- **Feasibility:** The audit arm is straightforward. The reproduction arm is the constraint, and this review is itself the evidence: 258 of the 364 reports sought here could not be retrieved with the available institutional session, and several harness-bearing papers withhold their production system prompts from public release. A candidate must scope Arm A to results whose artifacts are actually obtainable and report the selection as a bias, not as a sample.
- **Risk:** The dominant risk is that the reproduction arm produces a null through inability rather than through evidence — that too few results can be reproduced at all to support a regression. Mitigation is to preregister a minimum viable sample, to treat non-reproducibility-through-unavailability as a reported outcome category rather than a dropout, and to pair every hosted reproduction with a self-hosted control so that endpoint drift can be separated from configuration error.
- **Standing caution:** Any candidate pursuing this topic must not repeat the pilot's own reliability error. A second rater that is another instance of the same automated instrument measures decision stability, not agreement, and must be labelled accordingly — a caution this document applies to its own screening reliability figure above.

---

## Runner-up and cross-cutting findings

Three further problems recurred across the corpus without reaching the level of a standalone dissertation, and one methodological pattern cuts across all four primary topics.

**Runner-up A: the dissent, and why it does not close the question.** One study argues the opposite of everything above. A diagnostic evaluation of 800 research trajectories attributed 92.1 percent of 12,712 failure hits to three cognitive pillars and only 7.9 percent to engineering robustness, concluding that the same patterns recur across all eight harness-model combinations and that the deficit therefore sits at the model level (Fei et al., 2026). It is reported here as a genuine dissent and it is well executed, but two things qualify it. Its harness axis is thin — six of its eight cells share one backbone family — so *all eight harness-model combinations* describes one harness with several backbones rather than a crossed design. And the authors explicitly decline to test whether orchestration-level intervention would close the gap. A dissertation could take the dissent seriously by building the crossed design it lacks; that path is a variant of Topic 1 rather than a separate topic.

**Runner-up B: the harness is not one variable.** Treating the harness as a single confounder is a convenience that the evidence does not support. Leave-one-layer-out ablation across 126 model-environment cells shows the dominant harness component differing by environment (Xu et al., 2026). Isolating a runtime observer layer from the surrounding scaffold shrank a bundled gain of +6.0 to +11.7 points down to +0.7 to +6.7, with intervals crossing zero for two of three models (Zeng et al., 2026). Varying only reasoning-scaffold depth under fixed prompts, tools and decoding moved execution rates by 60 to 90 points, and in opposite directions for different models (Yu et al., 2026). Component-level attribution is important and under-served, but it is a refinement of Topic 1's design rather than an independent question, and it multiplies the cell count of an already expensive factorial.

**Runner-up C: the configuration surface nobody has priced.** Two descriptive studies map what a controlled comparison would actually have to hold fixed: eight repository-level configuration mechanisms across five agentic coding tools, dominated by static context files with advanced mechanisms adopted by under a fifth of repositories (Galster et al., 2026), and a source-code taxonomy of thirteen open-source scaffolds across twelve dimensions in three layers (Rombaut, 2026). Both explicitly decline to measure performance effects, and one declines to benchmark on the stated grounds that cross-agent results are not comparable because the models differ. The gap they leave — does deeper harness configuration buy anything measurable — is real, but it is a natural second study inside Topic 1's apparatus rather than a dissertation of its own.

**Cross-cutting pattern: the boundary condition is capability distance.** The corpus does not actually disagree about whether the harness or the model dominates; it disagrees about where. Harness variance dominates where models are close in capability and the task is long-horizon: that is the scope the headline factorial claims for itself. Model variance dominates where the capability gap is large. A fully crossed six-method by five-backend judge study decomposed accuracy variance at 49 percent method and 21 percent backbone, but excluding the two weakest purpose-built methods reversed the shares to 11 and 49 percent, so among competitive pipelines the backbone explained most of what remained (Wang et al., 2026). A planning study found the choice among re-ranking, iterative correction and tree search dominated by the quality of a different harness component entirely, and improved end-to-end accuracy by changing only the discriminator's environmental feedback without touching the generator or the planning method (Chen et al., 2024). A within-model harness swap produced a very large gap on one benchmark, no gap at all on another where the authors say harness choice matters little relative to experimental noise, and a reversal of ordering across model groups on a third (Karten et al., 2026). And the cleanest two-sided experiment in the corpus — scaffold swapped at fixed model, then model swapped at fixed scaffold, on one benchmark — moved true accuracy from 0.40 to 0.61 on the first manipulation and by about 6 percent on the second (Chevrot et al., 2025). Every one of the four topics above is, at root, a proposal to replace the field's argument about which factor is larger with a measurement of when each one is.

## References

- Ahumada, A. D. H. (2026). DYNAMIC MECHANISMS AND METRICS IN LANGUAGE MODEL-BASED MULTI-AGENT SYSTEMS: A SCOPING REVIEW. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22238539
- Assidiqi, M. H., Alghazzawi, D., Alarifi, S., & Cheng, L. (2026). Benchmarking Reference-Free LLM Agent Robustness Under Schema, Policy, and Toolset Drift. IEEE Access, 14, 79662-79672. https://doi.org/10.1109/access.2026.3696096
- Barbaste, P., Darrigol, T., Vu, G., & Wiltberger, T. (2026). Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2609.00006
- Chen, D. T. (2026). RefactorBench-JS: Evaluating LLM Agents on Behavior-Preserving Code Decomposition. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22204480
- Chen, Z., White, M., Mooney, R., Payani, A., Su, Y., & Sun, H. (2024). When is Tree Search Useful for LLM Planning? It Depends on the Discriminator. https://doi.org/10.18653/v1/2024.acl-long.738
- Chevrot, A., Vernotte, A., Falleri, J., Blanc, X., Legeard, B., & Cretin, A. (2025). Are Autonomous Web Agents Good Testers?. Proceedings of the ACM on software engineering., 2(ISSTA), 206-228. https://doi.org/10.1145/3728879
- Dhakal, A., Neupane, K., & Chaudhary, A. (2026). Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2607.13085
- Fei, Y., Liu, N., Yu, X., Chen, S., Li, L., Thapa, R., Ciobanu, M., Singh, N. P., Mao, Q., & Das, R. (2026). How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.14905
- Forment, M. A., Guerrero, M. J. C., García-Peñalvo, F. J., & Pereira, J. (2026). The Scaffolding Matters More Than the Interface: A Controlled Comparison of MCP and CLI Tool Use Across Seven Agent Scaffoldings, Five Language Models, and One Software Task. arXiv preprint. http://arxiv.org/abs/2608.08654v1
- Galster, M., Mohsenimofidi, S., Lulla, J. L., Abubakar, M. A., Treude, C., & Baltes, S. (2026). Harness Engineering for Agentic AI Coding Tools: An Exploratory Study. arXiv preprint. http://arxiv.org/abs/2602.14690v5
- Han, J., Xu, Y., Liao, Y., Wang, X., Jiang, Z., Di, Z., Lu, F., Hu, Z., & Xiao, Y. (2026). Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?. arXiv preprint. https://arxiv.org/abs/2608.04828
- He, C., Zhou, X., Wang, D., Xu, H., Liu, W., & Miao, C. (2026). Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime. Preprints.org. https://doi.org/10.20944/preprints202603.1756.v1
- Hou, Y., Chen, H., Zhou, S., Chen, X., Liu, X., Yuan, D., Meng, L., Wang, S., Liu, Q., & Huang, J. (2026). Harness-G: A Graph-Structured Harness for Search Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2607.27652
- Kapoor, S., Stroebl, B., Kirgis, P., Nadgir, N., Siegel, Z. S., Wei, B., Xue, T., Chen, Z., Chen, F., Utpala, S., Ndzomga, F., Oruganty, D., Luskin, S., Liu, K., Yu, B., Arora, A., Hahm, D., Trivedi, H., Sun, H., ... Narayanan, A. (2025). Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2510.11977
- Karten, S., Zhang, A. L., Thomas, K., Müller, S., Bakouch, E., Auras, D., Senghaas, M., Obeid, F., Dunas, K., Hagemann, J., & Jaghouar, S. (2026). Prime Agent: A Self-Improving RLM Harness. arXiv preprint. https://doi.org/10.48550/arxiv.2608.23552
- Kevin, C., Raghavan, N., Puget, J.-F., Malani, R., Puvvadi, M., Abramovitch, M., Gupta, M., Akkiraju, R., Prabhu, S., Dangi, Y., Luo, W., & Lee, S. H. (2026). Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills. arXiv preprint. http://arxiv.org/abs/2608.20614v1
- Kim, K., Choi, Y., Lee, S., Jun, S., Kim, D., & Park, S. (2026). The Interplay of Harness Design and Post-Training in LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2606.25447
- Mayoral-Vilches, V., Balassone, F., Sanz-Gómez, M., Landa, P. Z., Prieto, D. S., Álvarez, M. O., Quarta, D., & Pinzger, M. (2026). Towards Cybersecurity SuperIntelligence (CSI): What's the best harness for cybersecurity?. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2605.28334
- Moghadasi, M. N., & Ghaderi, F. (2026). What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2605.21404
- Morla, T., Bellibaltu, R. R., Singh, M., & Kapoor, M. S. (2026). AgentFairBench: Do LLM Agents Discriminate When They Act?. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2606.16723
- Rombaut, B. (2026). Inside the scaffold: A source-code taxonomy of coding agent architectures. arXiv preprint. https://arxiv.org/abs/2604.03515
- Sghaier, O. B., Li, H., Adams, B., & Hassan, A. E. (2026). Don't Blame the Large Language Model: How Scaffolding Evolution Shapes Coding Agent Quality. arXiv preprint. https://arxiv.org/abs/2607.03691
- Shah, J. (2026). Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures. arXiv preprint. https://doi.org/10.48550/arxiv.2606.08275
- Siegel, Z. S., Kapoor, S., Nadgir, N., Stroebl, B., & Narayanan, A. (2024). CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark. arXiv preprint. https://doi.org/10.48550/arxiv.2409.11363
- Strain, P. M. (2026). Bounded Returns to Orchestration: A Synthesis Ceiling Beneath Eleven Controlled Deep-Research Architectures. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21118281
- Tripathy, A., Harshit, C. P., & Vaidhyanathan, K. (2025). SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs. arXiv preprint, 104-111. https://doi.org/10.1145/3786167.3788406
- Vats, N., & Golev, O. (2026). The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation. arXiv preprint. http://arxiv.org/abs/2607.22585v1
- Wang, Z., Gu, L., Chi, Z., Liu, Z., Ayyoubzadeh, S. M., Yu, Y., & Wang, Y. (2026). Benchmarking LLM Judges for Mobile Agent Evaluation. arXiv preprint. https://doi.org/10.48550/arxiv.2608.11434
- Wu, Y., Zhang, J., Shi, J., Lei, X., Gu, Q., Zhang, Y., Wang, Z., He, C., Huang, C., Song, M., Zeng, Z., Wang, S., Liu, J., Shi, Y., Liu, J., Yan, S., Huang, W., Zhang, G., & Zhang, W. (2026). HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?. arXiv preprint. https://arxiv.org/abs/2609.01437
- Xu, T., Wen, H., & Li, M. (2026). Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents. arXiv preprint. http://arxiv.org/abs/2605.22166v2
- Yang, B., Cai, Z., Liu, F., Le, B., Zhang, L., Bissyandé, T. F., Liu, Y., & Tian, H. (2025). A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2506.23749
- Yao, Y., Tan, X., Liu, C.-H., Li, Y., Wang, Z., Yu, W., Tan, Z., Tian, Y., Zhao, G., Sun, L., Zhang, X., & Yang, T. (2026). Harness-Bench: Measuring harness effects across models in realistic agent workflows. arXiv preprint. https://arxiv.org/abs/2605.27922
- Yu, S., Carroll, F., & Bentley, B. L. (2026). The A-R Behavioral Space: Execution-Level Profiling of Tool-Using Language Model Agents in Organizational Deployment. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2604.12116
- Zeng, L., Zhang, S., & Zhang, X. (2026). EviDx: Evidence-Aware Active Diagnosis with Scaffolded LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.24570
- Zhang, J., Xiang, J., Yu, Z., Teng, F., Chen, X., Chen, J., Zhuge, M., Cheng, X., Hong, S., Wang, J., Zheng, B., Liu, B., Luo, Y., & Wu, C. (2024). AFlow: Automating Agentic Workflow Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2410.10762
- Zhang, S., Wang, A., & Sophie, L. (2026). Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2606.11686
- Zhang, Y., Wang, J., Ge, Y., Xu, W., Hamm, J., & Reddy, C. K. (2026). Stop Comparing LLM Agents Without Disclosing the Harness. arXiv (Cornell University). https://doi.org/10.20944/preprints202605.0711.v1
- Ziwei, Y. (2026). Set-shifting Behavioral Test for Harnessed Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2607.13396

---

*Distilled 2026-09-05 from the persisted artifacts of run `results/20260905-agent-harness-as-a-confounding-variable`. Quotations were verified against the run's page-marked extracted text with an exact-substring test and a normalization fallback that forgives PDF line-break hyphenation and collapsed spacing, asserting the cited page as well as the wording; citations were cross-checked against the run manifest. Preprint status is taken from the manifest and flagged in every attribution.*
