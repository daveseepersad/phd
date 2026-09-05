# The Agent Harness as a Confounding Variable in LLM Agent Performance Comparisons

A saturation-bounded systematic review of 106 full-text studies and 11 abstract-only core records.

Run folder: `results/20260905-agent-harness-as-a-confounding-variable`. Generated 2026-09-05 from persisted run artifacts. Every quotation in this document was verified against the extracted full-text corpus, page number included, before it was allowed to remain.

---

## 1. Research questions

The questions are reproduced exactly as preregistered.

- **RQ1.** How much of the reported performance difference between LLM agent configurations is attributable to the harness — scaffold, retry policy, and tool schema — rather than to the model or the agent topology under study?
- **RQ2.** Which studies hold the harness constant when comparing agent configurations, and what do they report when they do not?

---

## 2. Method

### 2.1 Design

This is a saturation-bounded systematic review, not an exhaustive census. The protocol was registered before any search ran, and every downstream stage stamps the protocol hash into its artifacts so that a post-hoc edit would be detectable. Reading stopped only when three preregistered conditions held together: every record screened *core* had been read, at least 20 full texts had been read, and a trailing window of read papers introduced no new evidence domain from a taxonomy of 20 domains fixed before reading began.

Screening assigned exactly one of five decisions to each candidate abstract — core, supporting, context, exclude, or unresolved — under topic-specific inclusion tests. The protocol also contains an instruction that shapes what follows: papers that compare configurations while leaving the harness uncontrolled were to be recorded rather than excluded, because they are the evidence for RQ2 and the reason the question exists.

### 2.2 PRISMA 2020 flow

Six search runs over ACM, arXiv, Crossref, IEEE, OpenAlex and Google Scholar returned 1,200 raw database records — 681 from OpenAlex, 300 from Crossref, 181 from arXiv, 38 from Scholar, and none from the ACM and IEEE browser sessions. One round of citation chaining added 42 records. Merging removed 234 duplicates, leaving 1,006 unique records screened.

Screening produced 117 core, 247 supporting, 179 context, 311 exclude and 152 unresolved decisions. The 364 core and supporting records were sought for retrieval; 258 could not be retrieved with the available institutional session; 106 reports were assessed at full text and all 106 were included in the synthesis. No full-text exclusions were recorded, which is itself a limitation: the corpus was bounded by retrieval success rather than by eligibility judgement at the full-text stage. The 247 supporting and 179 context records that were never read are reported as a limitation rather than silently dropped.

One artifact defect is disclosed for auditability. The generated `prisma.md` and `evidence-ledger.json` both carry a stale topic string from an earlier run of the pipeline; `protocol.md` and `quality.json` carry the correct topic. The counts, decisions, extractions and quotations in those files belong to this run — every record in the ledger is extracted against the two research questions above — but the topic label on two of the artifacts is wrong and should not be read as evidence about scope.

### 2.3 Saturation and the window sweep

The stopping rule was satisfied: 106 papers read against a minimum of 20, zero core records left pending, and zero new evidence domains in the trailing window. Because a stopping rule that holds at exactly one window width is a weak rule, the window was swept from 3 to 8 read papers. Every width in that range returned the same verdict, so the saturation decision is not an artefact of the preregistered window of 5.

Saturation here means domain saturation against a preregistered 20-domain taxonomy, not exhaustive coverage. It is entirely possible for a corpus to saturate on domains while still missing effect sizes, and Section 5 records where that happened.

### 2.4 Known-item validation

The protocol preregistered six must-find papers. The search strategy located all six in the candidate pool, so known-item recall is 6 of 6. The queries sent were keyword phrases rather than the research questions themselves; a prior run of this pipeline measured the difference and found the verbatim-question form recalling none of its preregistered known items where the keyword form recalled all of them.

### 2.5 Reliability check — what it is and what it is not

A second-rater check was run over a sample of 102 screened records. Two records were unratable and excluded, leaving 100 rated pairs. Agreement between the recorded screening decisions and the second rater was 80.0 percent observed against 27.4 percent expected, giving Cohen's kappa = 0.725.

**This is not human inter-rater reliability.** The second rater was an independent blind LLM re-prompt of the same screening task, and the artifact labels it as such. What the coefficient measures is decision stability under re-prompting — how reproducible the screening decisions are when the same instrument is run again without sight of the first pass. It says nothing about whether a human expert would have agreed with either pass. The disagreements are concentrated where the taxonomy is genuinely soft: the confusion matrix shows most conflict between *context* and *supporting*, and between *supporting* and *core*, while *exclude* is the most stable category. A single-auditor pilot in the corpus itself makes the same point about its own limits, calling for a second auditor precisely because one pass cannot establish agreement.

### 2.6 Quality appraisal and corpus composition

Every included paper was scored on an eight-item rigour checklist, extended to twelve items for grey literature. Mean rigour is 0.768, with a range from 0.375 to 1.000. Four papers reach 1.00 and four sit at or below 0.50.

The corpus is preprint-heavy: 84 of the 106 read papers are preprints, and much of the harness-specific literature dates from 2026 and has not been refereed. Every entry in Section 4 is labelled with its rigour score and its venue type, and papers below 0.50 are used for framing and vocabulary only. Section 3 states explicitly which conclusions do not rest on that tier.

### 2.7 Quote verification

Every quotation in this document was checked against the page-marked extracted text with an exact-substring test and a normalization fallback that forgives PDF line-break hyphenation and collapsed spacing, asserting the cited page as well as the wording. Quotations that could not be located, or that resolved to a different page than the one cited, were removed rather than repaired by guesswork. One quotation carried in the evidence ledger failed this check and does not appear here.

---

## 3. What the evidence supports, rejects, and where it disagrees

### 3.1 The central finding: harness effects rival or exceed model effects

This corpus answers RQ1 unusually clearly. Across designs that pin the model and vary only the surrounding execution layer, the harness accounts for as much of the reported difference between agent configurations as the model does, and frequently more.

The strongest single estimate comes from a controlled 3x3 factorial on SWE-bench Verified in which task order, Docker runtime, evaluation pipeline, step budget, per-step timeout and API settings were all pinned. Harness-induced variance exceeded model-induced variance by a factor of 7.80 — 18.48 pp^2 against 2.37 pp^2 — and six of the nine model-pair comparisons reversed order depending on which harness was used (Zhang et al., 2026, entry 1).

> Average HV is 18.48 pp2 versus average MV of 2.37 pp2, a ratio of 7.80×.
>
> Zhang et al. (2026), p. 7

Three independent designs put the effect in the same range. A full factorial crossing six harnesses with eight model backends over a fixed 106-task suite reports a 23.8-point gap between the best and worst harness under an identical task set and model pool (Yao et al., 2026, entry 2). A survey conditioning on the model across public Terminal-Bench 2.0 submissions finds a median within-model range of 13.6 points across harnesses, with 14 of 20 models varying by at least 10 points (Guo et al., 2026, entry 6). And in the cleanest two-sided experiment in the corpus, holding GPT-4o fixed and swapping the scaffold moved web-testing true accuracy from 0.40 to 0.61, while holding the scaffold and swapping across three frontier models moved it by only about 6 percent (Chevrot et al., 2025, entry 4).

> Our results reveal only minor differences across the three LLMs (see Table 4), with no single model emerging as significantly superior.
>
> Chevrot et al. (2025), p. 14

On cost the asymmetry is not close. Holding model, task instruction, test suite, sandbox and wall-time cap constant, harness choice shifted tokens per solved task by roughly 40x while a model upgrade shifted it by 1.0 to 1.3x (Vats & Golev, 2026, entry 3).

> The cost-side asymmetry is overwhelming: harness choice shifts tokens-per-solved-task by 40×, while upgrading the model barely moves it (1.0–1.3×).
>
> Vats & Golev (2026), p. 5

The same pattern appears in the largest standardized evaluation infrastructure in the corpus, where scaffold choice alone produced a 9x cost difference for a two-percentage-point accuracy difference on the same benchmark, and where model-scaffold pairings interacted by provider rather than adding independently (Kapoor et al., 2025, entry 5).

> Agent scaffolds create drastic differences in cost and accuracy.The choice of scaffold can be consequential in determining the final cost and accuracy of the agent.
>
> Kapoor et al. (2025), p. 7

### 3.2 Four qualifiers that must travel with that finding

**Harness effects are not additive and not uniformly signed.** The same test-runner tool is worth +9.8 points to one model and −2.4 points to another under an otherwise identical configuration, an interaction the author names as a central empirical finding (Chen, 2026, entry 24).

> This interaction effect—the same tool helping some models while not helping others—is a central empirical finding.
>
> Chen (2026), p. 14

A reflection step suppressed execution for two models and a planning step amplified it for a third, on identical prompts under fixed decoding (Yu et al., 2026, entry 37). An automated scaffold scored *below* plain input-output prompting on average, so scaffold changes can be strongly negative (Zhang et al., 2024, entry 21). Harness and model interact; they are not separable factors, and a single scalar estimate of "the harness effect" is a fiction.

> This suggests that different language models require different workflows to achieve their optimal performance.
>
> Zhang et al. (2024), p. 8

**Isolating a single harness component shrinks the effect sharply, and often across zero.** The bundled scaffold-plus-harness gain in one clinical diagnosis system was +6.0 to +11.7 points on average; isolating only the runtime observer layer left +0.7 to +6.7 points, with confidence intervals spanning zero for two of three models (Zeng et al., 2026, entry 25). The same pattern appears wherever a paper is careful enough to ablate rather than swap whole stacks. Most of the large numbers in Section 3.1 compare complete configurations, and the papers that report them say so.

**Pass-rate differences are frequently inside the noise even when cost differences are enormous.** Paired within-model pass-rate differences across harnesses stayed within 0 to 8 points with bootstrap intervals mostly including zero, while token cost moved 40x (Vats & Golev, 2026, entry 3). One study measured a same-commit noise floor of roughly ±4.75 pair-score points, wide enough to swallow most of its own 64 observed version switches (Wu et al., 2026, entry 7).

> The same commit can vary by about ±4.75 pair-score points, so small gains cannot be attributed to code changes from score alone.
>
> Wu et al. (2026), p. 13

A fairness pilot makes the statistical version of the same point: comparing a many-group spread against a two-run pairwise difference inflates an apparent effect by roughly 2.4x through statistic arity alone, and the authors show an earlier draft of their own work reading that artifact as signal (Morla et al., 2026, entry 73).

> That comparison is wrong, and correcting it is the central methodological lesson of the pilot.
>
> Morla et al. (2026), p. 8

**Aggregate metrics hide the effect in both directions.** A deliberately injected single-layer scaffold regression moved an aggregate pass rate by only 1.7 to 5.9 points — dismissible as run-to-run noise — while the responsible layer's own assertion slice collapsed by 25 to 91 points (Zhang et al., 2026, entry 42). Conversely, an endpoint metric can be right for the wrong reason: an unguarded pipeline reached a near-correct answer with only 81 percent of essential steps succeeding, because systematic errors partially cancelled (Wang et al., 2025, entry 82).

### 3.3 RQ2: who holds the harness constant, and what the rest report

Studies that do hold the harness constant exist and are identifiable. They pin the loop, step budget, temperature and model and vary one surface (entry 39); they run seven memory strategies under one harness, one synthesizer and one judge (entry 57); they fix feasible retrieval targets, transitions, budgets, corpora, reward, seeds and data order and change only the action schema (entry 40); they hold task, harness, model, scorer, sandbox and non-target components fixed and measure a paired lift (entry 38). The pattern in these papers is consistent: the tighter the control, the more precisely the effect is localised, and usually the smaller it becomes.

What happens when nobody holds the harness constant is answered by three disclosure audits, and they are the decisive RQ2 evidence.

First, only 2 of 9 benchmarks in a large standardized evaluation had ever been evaluated with the same agent scaffold for four or more of the models being compared (Kapoor et al., 2025, entry 5).

> We found that only 2 of these benchmarks were ever evaluated with the same agent scaffold for 4 or more models from this list, making cross-model comparison hard (Section A9).
>
> Kapoor et al. (2025), p. 2

Second, an audit of 66 LLM program-repair systems found that of 2,145 possible pairwise comparisons, only 100 share a benchmark label, only 32 fall inside bounded comparison windows, and exactly one pair is model-controlled — and that pair sits inside a single paradigm (Yang et al., 2025, entry 16).

> no model-controlled cross-paradigm comparison exists. Benchmark-name overlap therefore does not support a paradigm leaderboard.
>
> Yang et al. (2025), p. 41

Third, a scoping review audited the full text of the 16 studies that directly observe LLM-based multi-agent systems and found seed reported in 0 of 16, sampling frequency in 0, number of runs in 3 and temperature in 1, while model version, dataset, task and baseline were reported in all 16 (Ahumada, 2026, entry 17).

> Reproducibility reporting is limited: seed, number of runs, and sampling frequency are not reported in any study.
>
> Ahumada (2026), p. 1

Those three results compose into a single claim. If the execution parameters that determine run-to-run variance are almost never reported, and the scaffold is almost never matched across the models being compared, then most published cross-configuration agent comparisons cannot distinguish a harness effect from a model effect from noise — not because the analysis is wrong but because the information required is absent. A twelve-paper disclosure pilot puts the same finding on the supply side: harness specification is the field on which agent benchmark papers score worst, none disclose it fully, and none pin a content-addressed image for the evaluation environment (Moghadasi & Ghaderi, 2026, entry 18).

> The harness field is universally partial.Seven of the eight agent benchmarks score 0.5; one (SWE-bench, which predates the scaffold work) scores 0.0. Zero score 1.0.
>
> Moghadasi & Ghaderi (2026), p. 5

### 3.4 Where the evidence disagrees

One paper in this corpus argues the opposite of Section 3.1 and is reported here as a genuine dissent. A diagnostic evaluation of 800 research trajectories attributed 92.1 percent of 12,712 failure hits to three cognitive pillars and only 7.9 percent to engineering robustness, concluding that the same patterns recur across all eight harness-model combinations and that the deficit therefore sits at the model level (Fei et al., 2026, entry 19).

> The same patterns recur across all eight harness–model combinations, including the strongest models tested, locating the deficit at the model level rather than in any particular scaffold; whether orchestration-level interventions can close it is an open question this work does not test.
>
> Fei et al. (2026), p. 1

Two things qualify it. Its harness axis is thin — six of the eight cells are Claude Code backbones, against one Codex cell and one Gemini CLI cell — so "all eight harness-model combinations" is closer to one harness with several backbones than to a crossed design. And the authors explicitly decline to test whether orchestration-level intervention would close the gap, which leaves the attribution question open in their own framing. Their own engineering-robustness result also points the other way, since those failures depend on how the system is built rather than on the task.

A second, milder disagreement is quantitative rather than directional. A fully crossed six-method by five-backend judge study decomposed accuracy variance at 49 percent method and 21 percent backbone, but excluding the two weakest purpose-built methods reversed the shares to 11 percent and 49 percent, so among competitive pipelines the backbone explained most of the remaining variance (Wang et al., 2026, entry 26).

> Once those are excluded, backbone choice explains most of the remaining variance (Appendix D.4); among competitive methods, upgrading the backbone yields greater returns than engineering elaborate judge prompts.
>
> Wang et al. (2026), p. 8

Two further studies converge on the same boundary condition rather than contradicting the finding. In a robustness benchmark, static baselines under an identical harness spanned 0.130 to 0.432 across five models while controller changes shifted a given model by at most about nine points (entry 31); and in a matched-model penetration-testing comparison, a single model generation inside an unchanged scaffold moved pass@1 by 12 to 25 points against a harness residual of 5 to 10 (entry 44). Harness variance dominates where models are close in capability and the task is long-horizon; model variance dominates where the capability gap is large. The 3x3 factorial scopes its own claim to precisely the first case.

### 3.5 What the evidence does not support

The corpus does **not** support a universal multiplier. The 7.80x ratio is a measurement on one task distribution with three comparable frontier models, and its authors say so.

> We do not claim that the 7.80× ratio is universal. The grid demonstrates that harness variance can dominate model variance under controlled conditions and that the decomposition protocol produces interpretable estimates on a realistic task distribution.
>
> Zhang et al. (2026), p. 7

It does not support the claim that more scaffolding is better: an automated workflow search scored below plain prompting (entry 21), a chain-of-thought call matched or beat a ReAct agent for every model tested and was catastrophic for a weak one (entry 53), adding harness machinery to a memory system reduced accuracy (entry 62), supplying all retrieval components at once degraded coverage (entry 66), and higher reasoning effort gave equal or lower accuracy in 21 of 36 model-agent-benchmark combinations (entry 5).

It does not support treating the harness as one variable. Leave-one-layer-out ablation shows the dominant component differing by environment (entry 13); a source-code study decomposes production harnesses into seven subsystems spanning three orders of magnitude in code size (entry 93); and a taxonomy of eight repository-level configuration mechanisms shows what a controlled comparison would have to hold fixed (entry 95).

Finally, **no conclusion in this review rests on the low-rigour tier.** Four papers score between 0.375 and 0.50: a harness-engineering survey (entry 106, 0.38), a modular-benchmarking framework published in an IAEME-family journal that advertises an implausible impact factor (entry 105, 0.44), a harness-resilience position paper (entry 104, 0.46), and a blockchain-inspired multi-agent root-cause system (entry 103, 0.50). The first three run no experiments at all. The fourth carries an internal contradiction that should be stated explicitly: its Section 3.5 narrative reports an average score of 64.9 against baselines of 16.0 to 26.7, and neither figure corresponds to any value in the paper's own results table.

> However, our proposed MABC significantly outperformed all the baseline models and ReAct with GPT-4-Turbo, achieving an impressive average score of 64.9.
>
> Zhang et al. (2024), p. 7

These four are retained for vocabulary and framing. Every magnitude claim in Sections 3.1 to 3.4 is carried by papers scoring 0.69 or above.

---

## 4. The corpus, ordered by contribution

Entries are ordered by how directly they bear on the attribution question, then by rigour. Each entry gives the APA citation exactly as recorded in the run manifest, the rigour score, the venue type, and page-anchored quotations verified against the extracted text.

### 1. Stop Comparing LLM Agents Without Disclosing the Harness

Zhang, Y., Wang, J., Ge, Y., Xu, W., Hamm, J., & Reddy, C. K. (2026). Stop Comparing LLM Agents Without Disclosing the Harness. arXiv (Cornell University). https://doi.org/10.20944/preprints202605.0711.v1

*Rigour 0.83 · preprint*

The decisive study for RQ1. Zhang et al. (2026) formalise a benchmark score as a variance decomposition over model, harness and their interaction, then estimate it in a controlled 3x3 factorial on a 100-task SWE-bench Verified subset, pinning task order, Docker runtime, evaluation pipeline, a 50-step budget, a 120-second per-step timeout and default API settings, with two runs per cell. Harness-induced variance averaged 18.48 pp^2 against 2.37 pp^2 for model-induced variance, a ratio of 7.80x; a harness change moved a fixed model by 8.5 to 13.0 points while a model change inside a fixed harness moved scores by 2.5 to 5.0 points, and six of the nine model-pair comparisons reversed order depending on which harness was used. The authors decline to generalise the ratio, and the paper's own scope note confines the claim to long-horizon tasks with comparable frontier models.

> Every benchmark score is jointly produced by a model and a harness, but the harness is rarely disclosed and almost never held constant across comparisons.
>
> Zhang et al. (2026), p. 1

> Average HV is 18.48 pp2 versus average MV of 2.37 pp2, a ratio of 7.80×.
>
> Zhang et al. (2026), p. 7

> We do not claim that the 7.80× ratio is universal. The grid demonstrates that harness variance can dominate model variance under controlled conditions and that the decomposition protocol produces interpretable estimates on a realistic task distribution.
>
> Zhang et al. (2026), p. 7

### 2. Harness-Bench: Measuring harness effects across models in realistic agent workflows

Yao, Y., Tan, X., Liu, C.-H., Li, Y., Wang, Z., Yu, W., Tan, Z., Tian, Y., Zhao, G., Sun, L., Zhang, X., & Yang, T. (2026). Harness-Bench: Measuring harness effects across models in realistic agent workflows. arXiv preprint. https://arxiv.org/abs/2605.27922

*Rigour 0.92 · preprint*

The only full factorial in the corpus that makes the harness the primary axis: Yao et al. (2026) cross six configurable harnesses with eight model backends over 106 fixed sandboxed tasks, producing 5,194 trajectories. Under an identical task set and model pool the best and worst configurable harness are separated by 23.8 points. The secondary finding is an interaction rather than a main effect, since stronger backbones show lower cross-harness variance, so the harness share is itself a function of model strength. The authors disclaim causal decomposition: they compare complete harness configurations, not isolated mechanisms.

> However, the harness itself remains largely unmeasured: existing benchmarks either abstract away execution, conflate the harness with the full agent system, or fix the harness when comparing models.
>
> Yao et al. (2026), p. 2

> Among configurable harnesses, NanoBot obtains the highest aggregate score (76.2), while OpenClaw obtains the lowest score (52.4), giving a 23.8-point gap under the same task set and model-backend pool.
>
> Yao et al. (2026), p. 7

> Within these limits, the experiments support the central motivation of Harness-Bench: agent capability is not fully characterized by the base model alone, but also by the execution layer that mediates observation, action, recovery, and artifact production.
>
> Yao et al. (2026), p. 8

### 3. The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation

Vats, N., & Golev, O. (2026). The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation. arXiv preprint. http://arxiv.org/abs/2607.22585v1

*Rigour 0.92 · preprint*

Vats and Golev (2026) hold the model, task instruction, test suite, sandbox, wall-time cap and system-prompt template constant across three harnesses on a 50-task Terminal-Bench Pro subset and report the sharpest cost-side asymmetry in the corpus: harness choice moves tokens per solved task by roughly 40x while a model upgrade moves it 1.0 to 1.3x. Pass-rate differences, by contrast, stay within 0 to 8 points with bootstrap intervals mostly spanning zero, so on accuracy the two factors are not separable at n = 50. Harness-specific failure fingerprints replicated across both models, which the authors use to argue the fingerprint is a scaffold property. They are explicit that OpenCode exposes no turn-budget flag, an asymmetry they could not remove.

> Held constant: verbatim Terminal-Bench Pro instruction; native test suite; Daytona sandbox per task; 900-second wall-time cap per trial; OpenRouter as the model gateway.
>
> Vats & Golev (2026), p. 2

> The cost-side asymmetry is overwhelming: harness choice shifts tokens-per-solved-task by 40×, while upgrading the model barely moves it (1.0–1.3×).
>
> Vats & Golev (2026), p. 5

> Model-tomodel comparison is valid when the harness is fixed; when it varies, performance and efficiency conflate model and scaffold effects.
>
> Vats & Golev (2026), p. 1

### 4. Are Autonomous Web Agents Good Testers?

Chevrot, A., Vernotte, A., Falleri, J., Blanc, X., Legeard, B., & Cretin, A. (2025). Are Autonomous Web Agents Good Testers?. Proceedings of the ACM on software engineering., 2(ISSTA), 206-228. https://doi.org/10.1145/3728879

*Rigour 1.00 · peer-reviewed journal*

The cleanest two-sided attribution experiment in the corpus, and one of only four papers scoring 1.00 on the rigour checklist. Chevrot et al. (2025) run both halves on the same 113-test benchmark: with the model pinned to GPT-4o, swapping a thin single-prompt scaffold for an orchestrator-actor-assertor scaffold with retry moved average true accuracy from 0.40 to 0.61, while with the scaffold pinned and the model swapped across GPT-4o, Sonnet and Gemini the spread was about 6 percent. Twenty-six of 113 cases were misaligned with the human verdict under every model, and the largest qualitative failure category is attributed to limits of the browser-interaction framework rather than to model reasoning.

> First, we compare the SeeAct-ATA with PinATA, using GPT-4o, given its strong performance. As expected, our results indicate that PinATA outperforms SeeAct-ATA, achieving a 50% increase in true accuracy.
>
> Chevrot et al. (2025), p. 13

> Our results reveal only minor differences across the three LLMs (see Table 4), with no single model emerging as significantly superior.
>
> Chevrot et al. (2025), p. 14

> This category encompasses errors caused by limitations in the technical framework for interacting with the web browser, which restrict the agent’s ability to perform certain actions.
>
> Chevrot et al. (2025), p. 15

### 5. Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation

Kapoor, S., Stroebl, B., Kirgis, P., Nadgir, N., Siegel, Z. S., Wei, B., Xue, T., Chen, Z., Chen, F., Utpala, S., Ndzomga, F., Oruganty, D., Luskin, S., Liu, K., Yu, B., Arora, A., Hahm, D., Trivedi, H., Sun, H., ... Narayanan, A. (2025). Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2510.11977

*Rigour 0.92 · preprint*

HAL is the pivotal RQ2 disclosure audit. Kapoor et al. (2025) standardise the scaffold as an explicit third evaluation axis alongside model and benchmark across 21,730 rollouts, nine models and nine benchmarks, and then report that only 2 of those nine benchmarks had ever been evaluated with the same scaffold for four or more of the models compared. On the RQ1 side the effects are large and interacting: scaffold choice alone produced a 9x cost difference for a two-point accuracy difference on Online Mind2Web, Claude models paired better with BrowserUse and OpenAI models with SeeAct, and higher reasoning effort gave equal or lower accuracy in 21 of 36 combinations. Log analysis found environmental or scaffold barriers in roughly 40 percent of failed tasks and a leakage bug in an official scaffold that invalidated a completed evaluation.

> We found that only 2 of these benchmarks were ever evaluated with the same agent scaffold for 4 or more models from this list, making cross-model comparison hard (Section A9).
>
> Kapoor et al. (2025), p. 2

> Agent scaffolds create drastic differences in cost and accuracy.The choice of scaffold can be consequential in determining the final cost and accuracy of the agent.
>
> Kapoor et al. (2025), p. 7

> In cases where the same models are used for both task-specific and generalist scaffolds across three benchmarks, task-specific agents consistently outperform.
>
> Kapoor et al. (2025), p. 8

### 6. From Question Answering to Task Completion: A Survey on Agent System and Harness Design

Guo, J., Hao, Z., Wang, C., Fan, C., Luo, T., Li, H., Gao, Y., Mei, H., Peng, J., Xu, R., Dong, M., Wu, H., Zheng, M., Han, K., Wang, S., Xu, C., & Wang, Y. (2026). From Question Answering to Task Completion: A Survey on Agent System and Harness Design. arXiv preprint. https://doi.org/10.20944/preprints202606.1312.v1

*Rigour 0.67 · preprint*

The largest body of observational model-versus-harness evidence available. Guo et al. (2026) condition on the model across public Terminal-Bench 2.0 submissions and find a median within-model range of 13.6 points, with 14 of 20 models varying by at least 10 points and the largest spreads exceeding 20. The effect is regime-dependent: the SWE-bench Verified spread narrows for the strongest backbones, while the WebArena model-only to harnessed span reaches 41.5 points for GPT-4o. Scaffold complexity does not predict effectiveness, since a roughly 100-line minimal scaffold nearly matches a full-featured sandbox under Opus 4.5. The authors state plainly that this is a synthesis of uncontrolled public evidence, which is itself an RQ2 finding.

> At the same time, conditioning on the model reveals large harness-induced spreads. GPT-5.3Codex ranges from 64.7% with Terminus 2 to 78.4% with SageAgent, a 13.7% difference. Claude Opus 4.6 ranges from 58.0% with Claude Code to 76.4% with Meta-Harness, an 18.4% difference. Gemini 3.1 Pro ranges from 59.4% with Gemini CLI to 80.2% with TongAgents, a 20.8% difference.
>
> Guo et al. (2026), p. 32

> Among the 20 models that have at least three observed harness results, the median within-model range is 13.6% and 14 of the 20 models vary by at least 10% across harnesses.
>
> Guo et al. (2026), p. 33

> The table should be read as a compact synthesis of public evidence rather than a fully controlled factorial experiment.
>
> Guo et al. (2026), p. 29

### 7. HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?

Wu, Y., Zhang, J., Shi, J., Lei, X., Gu, Q., Zhang, Y., Wang, Z., He, C., Huang, C., Song, M., Zeng, Z., Wang, S., Liu, J., Shi, Y., Liu, J., Yan, S., Huang, W., Zhang, G., & Zhang, W. (2026). HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?. arXiv preprint. https://arxiv.org/abs/2609.01437

*Rigour 0.83 · preprint*

HarnessDev supplies both a control protocol and a noise floor. Wu et al. (2026) freeze each generated harness and evaluate it twice, once with its creator as executor and once with a single fixed executor, so score changes under the unified runtime are attributable to the harness. Several harnesses turn out to be co-adapted to the model that wrote them and collapse under a different executor, with one Opus harness falling from 69.3 to 33.0 on SWE-bench Pro. Critically for interpreting the rest of this corpus, the same frozen commit varied by roughly plus or minus 4.75 pair-score points, and feedback-set gains agreed in direction with held-out gains only 53.1 percent of the time.

> Its impact is substantial: with identical weights, GPT-5 solves 35.2% of Terminal-Bench 2.1 inside Terminus 2 but 49.6% inside Codex CLI [45].
>
> Wu et al. (2026), p. 1

> Every score is produced by a frozen harness in a standardized runtime. The executor LLMLE and evaluator J remain fixed within each comparison, so score changes reflect changes to the harness.
>
> Wu et al. (2026), p. 6

> Changing this harness while holding model weights fixed can substantially alter task performance.
>
> Wu et al. (2026), p. 1

### 8. Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?

Han, J., Xu, Y., Liao, Y., Wang, X., Jiang, Z., Di, Z., Lu, F., Hu, Z., & Xiao, Y. (2026). Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?. arXiv preprint. https://arxiv.org/abs/2608.04828

*Rigour 0.92 · preprint*

Han et al. (2026) hold task, sandbox, rubric and judge fixed and run the same eight models under two agent harnesses. Both absolute scores and model rankings move: the leaderboard head changes identity, four of eight models reverse the sign of their harness delta, and cross-harness correlation is weak in the middle of the ranking. Their diagnosis is that the two harnesses stress different sub-abilities rather than being uniformly better or worse, and that preloading a skill lifts recognition but not execution quality. The Gemini family had to be dropped because a gateway schema sanitiser made the skill tool non-invokable, which is itself a harness effect on who can be measured at all.

> Evaluating eight LLMs under two agent harnesses, we find that reliable skill use remains out of reach, as the strongest configuration reaches an SU of only 0.613.
>
> Han et al. (2026), p. 1

> SU is therefore a property of a model-harness configuration, and rankings under one harness may not transfer to another.
>
> Han et al. (2026), p. 6

> Recent studies show that the harness can account for more performance variance than the model and even reverse model rankings [17, 18].
>
> Han et al. (2026), p. 3

### 9. Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis

Orogat, A., Rostam, A., & Mansour, E. (2026). Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis. arXiv preprint. http://arxiv.org/abs/2602.03128v1

*Rigour 0.88 · preprint*

An explicit control-of-variables study: Orogat et al. (2026) fix the LLM, prompts, decoding settings, data and scoring, then vary exactly one framework-level dimension per experiment. The harness-attributable range is very large, with latency spanning 1.3x to 117x a direct call, planning accuracy moving by up to 30 points and coordination success collapsing from above 90 percent to below 30 percent. The mechanism behind the planning result is the sharpest single piece of attribution evidence in the corpus: a schema-constrained planning interface converted valid reasoning into measured failure, with 84.7 percent of GSM8K outputs violating the required output schema. The paper offers no limitations section and several comparisons rest on single runs without uncertainty estimates.

> We fix the underlying LLM to control for model effects and attribute observed differences to the framework architecture.
>
> Orogat et al. (2026), p. 2

> Our results show that framework-level design choices alone can increase latency by over 100×, reduce planning accuracy by up to 30%, and lower coordination success from above 90% to below 30%.
>
> Orogat et al. (2026), p. 1

> These results show that planning outcomes in deployed agent systems are driven primarily byinterface design, not LLM planning ability alone.
>
> Orogat et al. (2026), p. 8

### 10. CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark

Siegel, Z. S., Kapoor, S., Nadgir, N., Stroebl, B., & Narayanan, A. (2024). CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark. arXiv preprint. https://doi.org/10.48550/arxiv.2409.11363

*Rigour 0.92 · preprint*

The cleanest 2x2 in the corpus. Siegel et al. (2024) cross two scaffolds with two models on the same 270 tasks, and the scaffold effect is both large and asymmetric: prompt hints plus a programmatic output-format check lifted GPT-4o from 35.6 to 60.60 percent and GPT-4o-mini from 8.9 to 44.44 percent on the Easy split, so a model comparison run under only one of the two scaffolds would report a very different model gap. The authors emphasise that these were a few days of small task-specific modifications, which is precisely the class of change that goes unreported. The pass@1 versus pass^3 gap on the Hard split adds a stochasticity caution.

> a few modifications to the prompt and the programmatic check of the output format boosted the performance on CORE-Bench-Easy performance from 35.6% to 60.60%. The differences were even starker when using GPT-4o-mini: performance improved from 8.9% to 44.44%.
>
> Siegel et al. (2024), p. 10

> Our baseline results show that while automating computational reproducibility is hard, simple task-specific modifications to existing general-purpose agents can already help increase accuracy.
>
> Siegel et al. (2024), p. 13

> The results suggests that the underlying stochasticity of the agent caused it to not consistently solve the same tasks.
>
> Siegel et al. (2024), p. 21

### 11. The Interplay of Harness Design and Post-Training in LLM Agents

Kim, K., Choi, Y., Lee, S., Jun, S., Kim, D., & Park, S. (2026). The Interplay of Harness Design and Post-Training in LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2606.25447

*Rigour 0.83 · preprint*

Kim et al. (2026) run a factorial over harness informativeness, model size, RL algorithm, tool schema and task distribution on ALFWorld. A 3B model under a rich harness beat a 7B model under a minimal harness by 14.1 points after identical post-training, so the harness choice outweighed a more-than-doubling of model size. Post-training under a low-effort harness produced an agent that scored 2.7 under a shifted tool schema, 10.8 points below the untrained base model, because it had memorised a surface tool syntax. Their framing point for RQ2 is that prior ALFWorld post-training work silently fixes a highly informative harness and rarely flags it as an assumption.

> Our experiments establish that harness design and post-training cannot be treated as separable design choices.
>
> Kim et al. (2026), p. 8

> Applying a harness only after training recovers little of the benefit of training with it in place.
>
> Kim et al. (2026), p. 6

> The model post-trained under h-high generates 95.7% valid tool calls underv2.0, indicating that it well adapts to the tool environment shift at the surface level (Fig. 6).
>
> Kim et al. (2026), p. 7

### 12. Don't Blame the Large Language Model: How Scaffolding Evolution Shapes Coding Agent Quality

Sghaier, O. B., Li, H., Adams, B., & Hassan, A. E. (2026). Don't Blame the Large Language Model: How Scaffolding Evolution Shapes Coding Agent Quality. arXiv preprint. https://arxiv.org/abs/2607.03691

*Rigour 0.88 · preprint*

Sghaier et al. (2026) invert the usual design, freezing the model and varying only the harness across 35 sequential releases of one coding-agent CLI over 3,500 executions. A quarter of continuous harness development produced no statistically significant change in resolve rate (Spearman rho = 0.208, p = 0.231) while token consumption rose about 70 percent and tool calls rose with it. That is a large harness-attributable variance component carrying no capability payoff, and every documented degradation passed the project's CI because agent-level effectiveness is not regression-tested. The study covers a single harness and a single LLM, and the authors ask that it be read as evidence that harness matters rather than as a universal quantitative prediction.

> Unlike prior work that fixes the agent harness and varies the model, we fix the model and vary only the agent harness, evaluating 35 sequential releases to measure their impact on agent effectiveness and efficiency.
>
> Sghaier et al. (2026), p. 1

> Worse, later agent harness versions consume nearly double the computational tokens and tool calls without corresponding quality gains.
>
> Sghaier et al. (2026), p. 1

> Our findings should be interpreted as evidence that agent harness matters, not as universal quantitative predictions for all model-harness combinations.
>
> Sghaier et al. (2026), p. 35

### 13. Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents

Xu, T., Wen, H., & Li, M. (2026). Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents. arXiv preprint. http://arxiv.org/abs/2605.22166v2

*Rigour 0.83 · preprint*

The largest single-factor harness experiment here: 126 model-environment cells in which the weights and the evaluation environment are fixed and only the runtime interface changes. Xu et al. (2026) report improvement in 116 of 126 settings at an average 88.5 percent relative gain, with a base model plus harness beating the same base model after specialised tool-use training in domain. A leave-one-layer-out ablation shows the dominant component differs by environment, which argues against treating the harness as a single scalar confounder, and a harness evolved from one 4B model's trajectories transferred to 17 other backbones. The claim is scoped tightly to deterministic, rule-governed environments.

> Across 18 instruction-tuned, reasoning, and agent-specialized backbones, LIFE-HARNESSimproves 116 of 126 model–environment settings, yielding an average relative gain of88.5%.
>
> Xu et al. (2026), p. 3

> Such failures often stem not from a lack of latent reasoning ability, but from mismatches at the model–environment boundary
>
> Xu et al. (2026), p. 2

> 3) Specialized tool-use training does not necessarily transfer to out-of-domain (OOD) agent environments
>
> Xu et al. (2026), p. 8

### 14. Self-Harness: Harnesses That Improve Themselves

Zhang, H., Zhang, S., Li, K., Zhang, C., Chen, Y., Zhang, Y., Bai, L., & Hu, S. (2026). Self-Harness: Harnesses That Improve Themselves. arXiv preprint. http://arxiv.org/abs/2606.09498v3

*Rigour 0.83 · preprint*

Zhang et al. (2026) freeze model weights, decoding configuration, tool set, budget, benchmark environment and evaluator, then let the same model propose bounded edits to its own harness surfaces. All nine model-benchmark pairs improved on both held-in and held-out splits, with the largest absolute gain 40.6 points and the largest relative gain 132 percent, arising entirely from prompts, tools, memory and runtime policies. The retained edits differ qualitatively across the three backends, which is direct support for the claim that a harness tuned for one model is not a neutral control for another. Edits are bounded and gated only by pass-rate non-regression.

> All comparisons are therefore within-model comparisons: the decoding configuration, budget, tool set, benchmark environment, and evaluator are kept unchanged while only the harness is allowed to vary.
>
> Zhang et al. (2026), p. 9

> These results show that harness-level edits can yield measurable improvements while keeping the model backend, tool set, budget, benchmark environment, and evaluator fixed.
>
> Zhang et al. (2026), p. 11

> The same base model can thus exhibit substantially different performance under different harnesses
>
> Zhang et al. (2026), p. 1

### 15. Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference

Pan, W., Liu, S., Lin, C.-Y., Zeng, J., Tang, X., Zhou, X., Lu, Y., & Jia, X. (2026). Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference. arXiv preprint. https://doi.org/10.48550/arxiv.2606.05922

*Rigour 0.88 · preprint*

Holding the backbone, agent framework and held-out split fixed, Pan et al. (2026) edit only the harness of instructions, skills and executable tools and raise the SWE-Bench Pro pass rate by 19 points in a single round, against at most 5 points for three feedback-free baselines. The ablations localise the effect inside the harness, since a raw-trajectory baseline with the same editable surface reached only 0.60 against 0.78 for structured diagnosis. The paper is candid that its self-preference selector is a poor ranker, so the deployed candidate was not the best available. Everything runs on one backbone and one framework, so the harness effect is measured but its interaction with the model is not.

> Notably, a single optimization round improves the pass rate on SWE-Bench Pro from 59% to 78% without any external grading.
>
> Pan et al. (2026), p. 1

> on SWE-Bench Pro a less-preferred candidate in fact reached 0.85, above the chosen one’s 0.78.
>
> Pan et al. (2026), p. 8

> Third, all experiments use a single backbone and agent framework (a Codex-style CLI agent running GPT-5.5).
>
> Pan et al. (2026), p. 9

### 16. A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications

Yang, B., Cai, Z., Liu, F., Le, B., Zhang, L., Bissyandé, T. F., Liu, Y., & Tian, H. (2025). A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2506.23749

*Rigour 0.88 · preprint*

The most systematic RQ2 evidence about what happens when the harness is not held constant, because it audits comparability at the level of individual reported results rather than benchmark names. Yang et al. (2025) code 66 LLM repair systems and find that of 2,145 possible pairwise comparisons, only 100 share a benchmark label, only 32 fall inside bounded comparison windows, and exactly one pair is model-controlled; that pair sits inside a single paradigm, so no model-controlled cross-paradigm comparison exists in the corpus at all. Within-window scores span 18.00 to 58.30 percent on SWE-bench Lite and must be read as whole-system stacks. Independent double coding reached kappa 0.98 on primary paradigm.

> no model-controlled cross-paradigm comparison exists. Benchmark-name overlap therefore does not support a paradigm leaderboard.
>
> Yang et al. (2025), p. 41

> Shared benchmark names alone do not determine whether published repair scores are comparable.
>
> Yang et al. (2025), p. 36

> Within that window, scores reported by the original papers range from 18.00% to 58.30%, but they should be interpreted as whole-system stacks under the respective authors’ protocol rather than isolated paradigm effects because base models, search depth, cost budgets, and validation policies differ.
>
> Yang et al. (2025), p. 37

### 17. DYNAMIC MECHANISMS AND METRICS IN LANGUAGE MODEL-BASED MULTI-AGENT SYSTEMS: A SCOPING REVIEW

Ahumada, A. D. H. (2026). DYNAMIC MECHANISMS AND METRICS IN LANGUAGE MODEL-BASED MULTI-AGENT SYSTEMS: A SCOPING REVIEW. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22238539

*Rigour 0.56 · preprint*

The sharpest evidence on the reporting side of RQ2. Ahumada (2026) audits the full text of the 16 studies in a 229-study scoping review that directly observe LLM-based multi-agent systems and finds a systematic asymmetry: model version, dataset, task and baseline are reported in all 16, while seed is reported in 0, sampling frequency in 0, number of runs in 3 and temperature in 1. Without those execution parameters no reader can separate a reported configuration difference from run-to-run stochastic variation. The author is careful that this measures documentary reporting rather than actual reproducibility, that extraction for the wider corpus was abstract-based, and that the pre-registered contrast is not robust under all sensitivities.

> Reproducibility reporting is limited: seed, number of runs, and sampling frequency are not reported in any study.
>
> Ahumada (2026), p. 1

> The audit confirms at the full-text level what abstract-based extraction already suggested: the descriptive elements of the experiment are documented consistently, while the parameters needed to characterize execution, replication, and stochastic variability are documented much less frequently.
>
> Ahumada (2026), p. 6

> In the 14 empirical studies with applicable information, the proportion of reported descriptive fields was 100% in all studies (pA = 1.00), while the proportion of reported execution, replication, and variability fields ranged between 0% and 60% ( pB1+B2).
>
> Ahumada (2026), p. 7

### 18. What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema

Moghadasi, M. N., & Ghaderi, F. (2026). What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2605.21404

*Rigour 0.79 · preprint*

Moghadasi and Ghaderi (2026) score twelve benchmark papers on self-disclosure and find harness specification to be the field on which agent benchmark papers perform worst: seven of eight score 0.5, one scores 0.0, none score 1.0, and zero pin a content-addressed container digest for the evaluation environment. Their originating anecdote is the RQ1 problem in miniature, two reports of the same model on the same benchmark about ten points apart with no pinned scaffold. They usefully separate contamination, which explains levels, from harness under-specification, which explains spread. It is a single-auditor pilot over twelve papers, so it supports claims about disclosure practice rather than effect sizes.

> two papers will report results on the same benchmark with the same model name, and the numbers will disagree, and you cannot tell why. Was it the scaffold? The sampling settings? A different subset? An evaluator version?
>
> Moghadasi & Ghaderi (2026), p. 1

> The harness field is universally partial.Seven of the eight agent benchmarks score 0.5; one (SWE-bench, which predates the scaffold work) scores 0.0. Zero score 1.0.
>
> Moghadasi & Ghaderi (2026), p. 5

> Harness drift.Two papers report a number on the same benchmark using two different scaffolds and neither pins which scaffold.
>
> Moghadasi & Ghaderi (2026), p. 3

### 19. How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks

Fei, Y., Liu, N., Yu, X., Chen, S., Li, L., Thapa, R., Ciobanu, M., Singh, N. P., Mao, Q., & Das, R. (2026). How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.14905

*Rigour 0.83 · preprint*

The corpus contains one paper that argues the opposite of the central finding, and it must be reported as such. Fei et al. (2026) attribute 12,712 failure hits across 45 patterns in 800 trajectories and find that three cognitive pillars account for 92.1 percent while engineering robustness contributes 7.9 percent, concluding that the same patterns recur across all eight harness-model combinations and that the deficit therefore sits at the model level. Two qualifications travel with it. Their harness axis is thin, dominated by six Claude Code backbones against one Codex and one Gemini CLI cell, and they explicitly decline to test whether orchestration-level interventions could close the gap. Their own engineering-robustness finding also cuts the other way, since those failures depend on how the system is built rather than on the task.

> The same patterns recur across all eight harness–model combinations, including the strongest models tested, locating the deficit at the model level rather than in any particular scaffold; whether orchestration-level interventions can close it is an open question this work does not test.
>
> Fei et al. (2026), p. 1

> Running one backbone under several harnesses, and one harness over several backbones, separates failures of the scaffold from failures of the model and shows whether a failure mode is idiosyncratic to one system or shared.
>
> Fei et al. (2026), p. 6

> These failures depend on how the system is built, not on the task, which is also why benchmarks that supply a pre-configured environment and a known entry point [41] make execution look solved: they remove the surface where the failures concentrate.
>
> Fei et al. (2026), p. 13

### 20. Bounded Returns to Orchestration: A Synthesis Ceiling Beneath Eleven Controlled Deep-Research Architectures

Strain, P. M. (2026). Bounded Returns to Orchestration: A Synthesis Ceiling Beneath Eleven Controlled Deep-Research Architectures. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21118281

*Rigour 0.88 · preprint*

Strain (2026) fixes one model, one search and extraction tool layer and one retry policy, then varies only orchestration across eleven deep-research architectures scored by a reliability-audited three-judge panel. The five strongest pipelines are judge-robustly inseparable, and the raw baseline-to-cluster premium of +0.145 shrinks to a 0 to 0.05 band once report length is controlled and becomes undetectable once token budget is clamped, so much of the apparent architecture effect is compute and verbosity. Serving identical pooled sources lifts citation quality but leaves factual accuracy statistically equivalent to zero. Judge reliability is modest (Krippendorff alpha 0.42 overall, 0.13 for factual accuracy) and compute budget is not equalised across architectures.

> Deep-research agents pairing LLMs with web search are usually compared while orchestration, base model, and retrieval all change at once, so no difference is cleanly attributable to architecture.
>
> Strain (2026), p. 1

> The probe certifies one claim: at matched budget P1’s advantage over P0 is no longer detectable.
>
> Strain (2026), p. 20

> Citation quality is retrieval-bound, and factual accuracy is synthesis-bound. Neither ceiling is the orchestration layer the field optimises.
>
> Strain (2026), p. 4

### 21. AFlow: Automating Agentic Workflow Generation

Zhang, J., Xiang, J., Yu, Z., Teng, F., Chen, X., Chen, J., Zhuge, M., Cheng, X., Hong, S., Wang, J., Zheng, B., Liu, B., Luo, Y., & Wu, C. (2024). AFlow: Automating Agentic Workflow Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2410.10762

*Rigour 0.96 · preprint*

Every method compared in AFlow, manual and automated, executes with the same GPT-4o-mini on the same split, so the full 67.2 to 80.3 average spread is attributable to workflow structure. Two results matter for the qualifiers. ADAS, an automated scaffold, averages 67.2 against 72.8 for plain IO prompting, so a harness change can be strongly negative; and a workflow searched against one executor degrades when moved to another, which Zhang et al. (2024) read as evidence that different models require different workflows. Their own search fixes model, temperature and output format, an explicit statement of harness control. The reported gains carry no significance testing.

> we simplify the search space by fixing key parameters such as the model M, temperature τ, and format F . This simplification allows AF LOW to focus its search primarily on the code-represented edgesE and prompts.
>
> Zhang et al. (2024), p. 6

> Workflows optimized by AF LOW outperform all manually designed methods by an average of 5.7% and surpass contemporary automatic workflow optimization work by 19.5%.
>
> Zhang et al. (2024), p. 8

> This suggests that different language models require different workflows to achieve their optimal performance.
>
> Zhang et al. (2024), p. 8

### 22. LATS-RCA: Language Agent Tree Search for Root Cause Analysis in Microservices

Naakka, A., Wang, Y., & Mäntylä, M. (2026). LATS-RCA: Language Agent Tree Search for Root Cause Analysis in Microservices. Lecture notes in computer science, 196-212. https://doi.org/10.1007/978-3-032-36590-3_14

*Rigour 1.00 · peer-reviewed conference*

One of four papers at rigour 1.00, and a rare decomposition of a multi-agent gain into topology and scaffold components under a shared tool and data setting. Naakka et al. (2026) separate what specialisation and handoff contribute (39.8 to 57.4 percent) from what the tree-search scaffold adds on the same topology (57.4 to 91.3 percent), then pin the scaffold and sweep backbones, finding at most 1.6 points of variation across frontier-tier models. Ablations attribute the scaffold effect to candidate batching, backpropagation and reflection. Benchmark-to-production accuracy fell from 91.3 to 65.1 percent, which bounds how far benchmark-measured scaffold effects transfer.

> The improvement over the multi-agent ReAct baseline indicates that multi-agent specialization and cross-modal handoff alone do not fully contribute to the gains; rather, the structured search process further strengthens diagnostic accuracy beyond linear cross-modal reasoning under the same tool and data setting.
>
> Naakka et al. (2026), p. 9

> Accuracy varies by at most 1.6 % across frontier-tier models (Claude Sonnet 4.5, GPT-5, Gemini 3 Pro).
>
> Naakka et al. (2026), p. 11

> These results indicate that the diagnostic accuracy gains of LATS-RCA stem from systematic exploration and reflection-guided evaluation, rather than from gathering more monitoring data.
>
> Naakka et al. (2026), p. 10

### 23. When is Tree Search Useful for LLM Planning? It Depends on the Discriminator

Chen, Z., White, M., Mooney, R., Payani, A., Su, Y., & Sun, H. (2024). When is Tree Search Useful for LLM Planning? It Depends on the Discriminator. https://doi.org/10.18653/v1/2024.acl-long.738

*Rigour 1.00 · peer-reviewed conference*

Chen et al. (2024) hold the generator, sampling budget and prompts fixed and vary the planning method and the discriminator one factor at a time. The choice of scaffold turns out to be dominated by a different harness component: with realistic LLM discriminators, iterative correction and tree search do not beat simple re-ranking, and McNemar tests find no significant difference. Adding environmental observations to the discriminator improved end-to-end accuracy substantially with no change to the generator or the planning method, which localises a large share of measured performance in the harness. Tree search cost 10 to 20 times more inference time for negligible or negative gains.

> After enhancing the discriminators with two environmental observations (Section 6.2), we effectively improve the agents’ performance without any modifications to the generator or the planning methods.
>
> Chen et al. (2024), p. 7

> For these reasons, iterative correction and tree search cannot gain decent improvement over reranking with the same LLM-based discriminator.
>
> Chen et al. (2024), p. 9

> By calculating the average inference time per example (Figure 3), we find that our implementation of tree search is at least 10–20 times slower than the other two planning methods
>
> Chen et al. (2024), p. 6

### 24. RefactorBench-JS: Evaluating LLM Agents on Behavior-Preserving Code Decomposition

Chen, D. T. (2026). RefactorBench-JS: Evaluating LLM Agents on Behavior-Preserving Code Decomposition. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22204480

*Rigour 0.88 · preprint*

The clearest demonstration that harness effects are not uniformly signed. Chen (2026) pins 123 fixtures, temperature 0, required tool choice, a 50-call cap, up to three retries with fresh conversation state and a fixed system prompt, and toggles only a test-runner tool. The same tool is worth +9.8 points to one model (p = 0.0018) and -2.4 points to another, so a model ranking taken under one tool configuration does not transfer to another. Agents also reported success on 49 to 84 percent of runs that failed hidden behavioural tests. Only two tool configurations were evaluated, and the production harness and system prompts are withheld from the public release.

> This interaction effect—the same tool helping some models while not helping others—is a central empirical finding.
>
> Chen (2026), p. 14

> All agents use temperature 0,tool_choice=required, a maximum of 50 tool calls per attempt, and up to 3 retry attempts with fresh conversation state.
>
> Chen (2026), p. 8

> Because every condition runs onthe same fixtures, file complexity is controlled by design.
>
> Chen (2026), p. 9

### 25. EviDx: Evidence-Aware Active Diagnosis with Scaffolded LLM Agents

Zeng, L., Zhang, S., & Zhang, X. (2026). EviDx: Evidence-Aware Active Diagnosis with Scaffolded LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.24570

*Rigour 0.88 · preprint*

EviDx is the corpus's best illustration that isolating a single harness component shrinks the measured effect. Zeng et al. (2026) hold the scaffold, model, tool interface and the exact 100 cases fixed, and report a large gain for the full scaffold over static single-agent prompting (+6.0 to +11.7 points on average) alongside a much smaller, model-dependent gain for the Observer harness alone (+0.7 to +6.7 points, with intervals crossing zero for two of three models). Gains concentrate on 8B models while open-ended accuracy stays near zero for them, and one model produced over 500 tool-schema failure events on the identical interface.

> Because EviDx requires multi-step tool interaction and trajectory-level evaluation for each case, we conduct a controlled evaluation on a fixed random subset of 100 instances from each dataset, using the same sampled cases across all methods and models.
>
> Zeng et al. (2026), p. 6

> Although EviDx improves MC performance, small-scale models still struggle with open-ended diagnosis, with scores near 0% in several settings.
>
> Zeng et al. (2026), p. 7

> We interpret it as a descriptive process-control signal rather than a standalone measure of reasoning quality.
>
> Zeng et al. (2026), p. 5

### 26. Benchmarking LLM Judges for Mobile Agent Evaluation

Wang, Z., Gu, L., Chi, Z., Liu, Z., Ayyoubzadeh, S. M., Yu, Y., & Wang, Y. (2026). Benchmarking LLM Judges for Mobile Agent Evaluation. arXiv preprint. https://doi.org/10.48550/arxiv.2608.11434

*Rigour 0.88 · preprint*

A fully crossed six-method by five-backend design, and the strongest counterweight in the corpus to a blanket harness-dominates conclusion. Wang et al. (2026) decompose judge accuracy variance and find 49 percent attributable to method and 21 percent to backbone, but excluding the two weakest purpose-built methods reverses the shares to 11 percent and 49 percent, so among competitive pipelines the backbone explains most of the remaining variance. Ablations show that UI metadata and agent reasoning traces move accuracy by at most about two points while screenshot count dominates. Judge choice alone shifted agent rankings by up to 13 positions, which is a harness effect located in the measuring instrument.

> A two-way variance decomposition over the 6×5 grid quantifies the two factors: method choice explains 49% of the accuracy variance and the backbone 21%, but the method share is driven by the two weakest methods, both purpose-built (the A3 modes).
>
> Wang et al. (2026), p. 5

> Once those are excluded, backbone choice explains most of the remaining variance (Appendix D.4); among competitive methods, upgrading the backbone yields greater returns than engineering elaborate judge prompts.
>
> Wang et al. (2026), p. 8

> All conditions share identical hyperparameters; only the reward source differs.
>
> Wang et al. (2026), p. 6

### 27. RCAgentBench: An Agent-Oriented Benchmark for Multimodal Root Cause Analysis in Microservices

Jiang, H., Wang, Z., Nie, X., Gao, D., Li, J., & Pei, C. (2026). RCAgentBench: An Agent-Oriented Benchmark for Multimodal Root Cause Analysis in Microservices. 2026 IEEE/ACM International Symposium on Quality of Service (IWQoS), 1-10. https://doi.org/10.1109/iwqos70441.2026.11661026

*Rigour 0.94 · peer-reviewed conference*

RCAgentBench is built around the attribution problem. Jiang et al. (2026) standardise three multimodal diagnostic tools and hold them fixed while varying agent pattern and model, and find that topology effects invert with model scale: single-agent wins at 8B, multi-agent wins at 32B and DeepSeek-V3. Raw parameter scale barely moves localisation accuracy while removing a single contextual prompt element collapses it from 38.75 to 11.00, which places the dominant variance in the harness rather than the model. The authors concede that their own tool selection bounds the result, a residual confound they do not resolve.

> Current approaches often mix powerful tools with specific agent designs, making it impossible to determine whether success stems from the agent’s intelligence or the tool’s capability.
>
> Jiang et al. (2026), p. 1

> When high-quality diagnostic signals are provided by detection tools, even relatively small models can effectively integrate evidence and infer the correct root cause.
>
> Jiang et al. (2026), p. 7

> One limitation ofRCAgentBenchlies in the diversity of integrated diagnostic tools.
>
> Jiang et al. (2026), p. 9

### 28. BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent

Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025). BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2508.06600

*Rigour 0.92 · preprint*

A benchmark built specifically to remove a harness confound. Chen et al. (2025) replace live black-box web search with a fixed 100,195-document corpus so retrieval and reasoning can be evaluated separately, and the results quantify what the unheld component was worth: the same agent with the same prompt and tool interface moves from 55.90 to 70.12 percent (GPT-5) or 14.34 to 36.75 percent (Sonnet 4) purely by changing the retriever behind the search tool, and to 93.49 percent under oracle retrieval for gpt-4.1. Adding a document-reader tool adds 8.2 points for one model and 1.3 for another, so tool-schema effects interact with model capability rather than adding uniformly.

> Current evaluations of deep-research agents often conflate agent system performance with the effectiveness of their retrieval components, making it difficult to achieve fair and consistent comparisons across systems.
>
> Chen et al. (2025), p. 2

> In this setup, gpt-4.1 achieves an accuracy of 93.49%. This highlights two key points. First, it showcases the importance of the retriever: if the retriever is of perfect quality, search agents can attain substantially high accuracy on complex reasoning tasks in BrowseComp-Plus, in contrast to the 14.58% baseline accuracy of gpt-4.1 when using BM25 as the retriever.
>
> Chen et al. (2025), p. 10

> A consistent trend observed across all models is that stronger retrieval leads to higher final accuracy.
>
> Chen et al. (2025), p. 9

### 29. Reliable Weak-to-Strong Monitoring of LLM Agents

Kale, N., Zhang, C. B. C., Zhu, K., Aich, A., Rodriguez, P., Team, S. R., Knight, C. Q., & Wang, Z. (2025). Reliable Weak-to-Strong Monitoring of LLM Agents. arXiv preprint. http://arxiv.org/abs/2508.19461v1

*Rigour 0.92 · preprint*

Kale et al. (2025) factorially separate monitor scaffolding from monitor information, holding the monitor LLM, dataset and threat model fixed. Scaffolding dominates: a hybrid parsing scaffold wins AUC at every awareness level and is the most adversarially robust, while giving the monitor more information about the agent yields only trivial advantage. The consequence for attribution is a weak-to-strong effect in which a well-designed scaffold lets small monitor models reliably oversee stronger agents, weakening the model-capability scaling law that the baseline scaffolding exhibits. Only offline monitoring is studied and the three scaffolds are described as an initial foray rather than a design-space survey.

> Second, monitor scaffolding matters more than monitor awareness: the hybrid scaffolding consistently outperforms baseline monitor scaffolding, and can enable weaker models to reliably monitor stronger agents – a weak-to-strong scaling effect .
>
> Kale et al. (2025), p. 1

> Therefore, the most effective way of improving AUC is not by providing the monitor with more information about the agent. Instead, improving the agent scaffolding from the full trajectory baseline to a hybrid one is more effective.
>
> Kale et al. (2025), p. 13

> First, agent awareness dominates monitor awareness: an agent’s knowledge that it is being monitored substantially degrades the monitor’s reliability.
>
> Kale et al. (2025), p. 1

### 30. FHIR-AgentBench: Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering

Lee, G., Bach, E., Yang, E., Pollard, T., Johnson, A. E. W., Choi, E., jia, Y., & Lee, J. H. (2025). FHIR-AgentBench: Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2509.19319

*Rigour 1.00 · preprint*

A rigour-1.00 controlled ablation over three harness axes on a fixed benchmark, prompt family and 32k context budget. Lee et al. (2025) find that adding a code interpreter to a multi-turn agent more than doubles answer correctness from 0.20 to 0.50 while barely changing retrieval precision or recall, whereas swapping among four models under the same top architecture moves correctness only within a 44 to 50 percent band. The authors draw the attribution conclusion explicitly. A secondary harness effect is isolated too: the retriever is tuned to favour recall, and higher precision correlates with better answers even at perfect recall, so an over-retrieving scaffold looks worse at reasoning independently of the model.

> This suggests that the agent’s architecture and the inherent difficulty of the task are currently more significant bottlenecks than the choice of the base LLM.
>
> Lee et al. (2025), p. 7

> The highest-performing agent—a multi-turn agent with a retriever and code interpreter—achieves an answer correctness of only 50.0%, underscoring the difficulty of reasoning over realistic, interoperable clinical data, as further illustrated in Appendix A3.
>
> Lee et al. (2025), p. 7

> First, multi-turn interaction is crucial for high retrieval recall. Agents that can iteratively refine search consistently achieve higher recall (71%)
>
> Lee et al. (2025), p. 7

### 31. Benchmarking Reference-Free LLM Agent Robustness Under Schema, Policy, and Toolset Drift

Assidiqi, M. H., Alghazzawi, D., Alarifi, S., & Cheng, L. (2026). Benchmarking Reference-Free LLM Agent Robustness Under Schema, Policy, and Toolset Drift. IEEE Access, 14, 79662-79672. https://doi.org/10.1109/access.2026.3696096

*Rigour 0.94 · peer-reviewed journal*

The most rigorously controlled study in the corpus by checklist score, and a direct probe of the three harness components RQ1 names. Assidiqi et al. (2026) apply a repair-rule layer, a memory-replay layer and a schema-normalisation layer over an otherwise identical base LLM call at temperature 0 across five models and up to 270 trials per cell. The result is a warning against assuming harness additions help: the replay layer significantly degraded task success for four of five models (fitted odds ratio 0.554) while the rules layer helped only two of five. Static baselines under an identical harness span 0.130 to 0.432 across models while controller changes shift a given model by at most about nine points, so on this benchmark the model term is the larger one.

> Controller stack. Three reference-free controller conditions share the same base LLM call and differ only in which repair stages are active at each step.
>
> Assidiqi et al. (2026), p. 5

> Blind replay consistently degrades reference-free task success relative to static for four of five models; Kimi K2 is the exception, for which both blind replay and rules-only significantly improve over the static baseline.
>
> Assidiqi et al. (2026), p. 1

> Removing normalization reduces GPT-4o mini from 0.396 to 0.322 overall
>
> Assidiqi et al. (2026), p. 8

### 32. The Scaffolding Matters More Than the Interface: A Controlled Comparison of MCP and CLI Tool Use Across Seven Agent Scaffoldings, Five Language Models, and One Software Task

Forment, M. A., Guerrero, M. J. C., García-Peñalvo, F. J., & Pereira, J. (2026). The Scaffolding Matters More Than the Interface: A Controlled Comparison of MCP and CLI Tool Use Across Seven Agent Scaffoldings, Five Language Models, and One Software Task. arXiv preprint. http://arxiv.org/abs/2608.08654v1

*Rigour 0.75 · preprint*

Forment et al. (2026) hold the task, the models and the verification identical and vary only the scaffolding across a 54-cell matrix, finding a factor-of-20 cost difference between the cheapest and most expensive scaffolding and a 139x spread for a single 27B model that completed the task under all of them. They set out to measure the tool-interface effect and report it inconclusive: thirteen strictly paired MCP-to-CLI ratios span 0.43x to 29.06x against a measured run-to-run resolution limit of about 1.5x, so the scaffolding, not the interface, is the stable effect. Their methodological warning matters for RQ2: agents frequently ignore the interface they are assigned, so a study that assigns without verifying measures an unknown mixture.

> The task, the models and the verification were identical in every row; only the scaffolding driving the model changed. Between the cheapest and the most expensive lies a factor of 20.
>
> Forment et al. (2026), p. 10

> How much an AI coding agent costs to run can depend more on the agent scaffolding that drives it than on the interface through which it reaches its tools.
>
> Forment et al. (2026), p. 1

> A measurement that assigns an interface without verifying which interface was used reports the cost of an unknown mixture.
>
> Forment et al. (2026), p. 19

### 33. Towards Cybersecurity SuperIntelligence (CSI): What's the best harness for cybersecurity?

Mayoral-Vilches, V., Balassone, F., Sanz-Gómez, M., Landa, P. Z., Prieto, D. S., Álvarez, M. O., Quarta, D., & Pinzger, M. (2026). Towards Cybersecurity SuperIntelligence (CSI): What's the best harness for cybersecurity?. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2605.28334

*Rigour 0.75 · preprint*

Mayoral-Vilches et al. (2026) fix the model, the per-challenge timeout and the anti-cheat harness and vary only the scaffold across five systems on 33 cybench challenges. The most useful result is structural rather than scalar: five scaffolds wrapping identical weights succeed on different challenges, with three contributing exclusive solves and pairwise Jaccard similarity as low as 0.31, so the scaffold changes which problems are solvable and not only how many. Solve rates cluster within about five points while cost per solve differs more than 3x and total input tokens 6x. Single runs per cell and a single model limit the inference.

> All scaffolds compared in this paper share the same model (alias2-mini), the same per-challenge wall-clock timeout drawn from the upstream cybench Est. Time field, and the same per-challenge harness.
>
> Mayoral-Vilches et al. (2026), p. 3

> The empirical complementarity we measure is therefore a function of the scaffoldingalone, not of distinct knowledge bases.
>
> Mayoral-Vilches et al. (2026), p. 10

> Using CSI, we benchmark five scaffolds ( CSI::Claude, CSI::Codex, CSI::GCAI, CSI::Mistral, CSI::CAI) on the 33 cybench challenges, holding the model fixed at alias2-mini.
>
> Mayoral-Vilches et al. (2026), p. 1

### 34. SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs

Tripathy, A., Harshit, C. P., & Vaidhyanathan, K. (2025). SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs. arXiv preprint, 104-111. https://doi.org/10.1145/3786167.3788406

*Rigour 0.92 · preprint*

Tripathy et al. (2025) hold model, hardware, timeout, context window and benchmark constant and vary only the agentic framework across 1,200 runs. Framework architecture drove a 9.4x span in energy consumption on the same backbone while task resolution stayed at or near zero for every configuration. That separation is directly useful for RQ1: the harness dominated one reported metric while contributing nothing measurable to another under identical conditions. High energy is attributed to frameworks that allow the model into unproductive loops with no detection, and low energy is shown to mask premature termination and false-positive completions. The near-zero resolution rate is a stated conclusion-validity threat.

> We find that framework architecture is the primary driver of energy consumption. The most energy-intensive framework, AutoCodeRover (Gemma), consumed 9.4x more energy on average than the least energy-intensive, OpenHands (Gemma).
>
> Tripathy et al. (2025), p. 1

> The SLM’s limited reasoning was the bottleneck forsuccess, but the framework’s design was the bottleneck forefficiency.
>
> Tripathy et al. (2025), p. 1

> Second, our experiments were limited to two small, open-weight models.
>
> Tripathy et al. (2025), p. 7

### 35. Set-shifting Behavioral Test for Harnessed Agents

Ziwei, Y. (2026). Set-shifting Behavioral Test for Harnessed Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2607.13396

*Rigour 0.83 · preprint*

The only harness-transfer replication in the corpus. Ziwei (2026) runs four models inside one harness with the default system prompt, identical tool schemas and fixed sampling, then varies harness elements one at a time: a single trajectory-local policy prompt moved mean set-shifting accuracy from 0.14 to 0.86 for one model and 0.38 to 0.74 for another while barely moving the other two. Suspecting the behavioural profiles could be artifacts of that harness, the author re-ran the schedule on an independent harness, where each model kept its routing signature. Sample sizes are small (n = 16 prefixes per model on the tree) and the tools are simulated with mocked side effects.

> Mean accuracy rises from 0.14 to 0.86 for gpt-5.5 and from 0.38 to 0.74 for deepseek-v4-pro.
>
> Ziwei (2026), p. 8

> We suspected that the routing profiles in §4.1 could be artifacts of the Hermes harness and might not replicate in other harnesses.
>
> Ziwei (2026), p. 18

> The harness change preserves the distinction between target-omitting concentration and target-retaining breadth.
>
> Ziwei (2026), p. 19

### 36. HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety

Bai, Y., Duan, J., Peng, J., Wu, X., Liu, S., Wang, S., & Chen, T. (2026). HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety. arXiv preprint. https://doi.org/10.48550/arxiv.2608.17597

*Rigour 0.88 · preprint*

Bai et al. (2026) transfer the harness-as-confounder argument into safety and report one of the largest single-model swings here: attack success rate for the same model is 4.3 times higher on one harness than another, and the identity of the safest model changes with the harness. The paper is also an honest RQ2 negative case, since the authors state that their three harnesses differ in system prompts, tool surfaces and state management and are evaluated as deployed rather than held fixed. They add a second-order measurement warning that harnesses expose different amounts of internal state, so cross-harness differences in detection can reflect observability rather than behaviour.

> Table 2 shows that harness choice can change the ASR of the same model by more than fourfold. GLM-5.2 records a 54.7% ASR on OpenClaw but only 12.6% on Nanobot, a4.3× difference.
>
> Bai et al. (2026), p. 8

> further shows that agent capability varies across combinations of models and harnesses, which motivates evaluation at the configuration level rather than attributing outcomes to the model alone.
>
> Bai et al. (2026), p. 10

> The three harnesses differ in their system prompts, tool surfaces, and statemanagement, andthesecomponentsareevaluatedasdeployedratherthanheldfixed. Cross-harness contrasts should therefore be read as comparisons between deployed configurations, not as controlled estimates of a harness-only effect.
>
> Bai et al. (2026), p. 19

### 37. The A-R Behavioral Space: Execution-Level Profiling of Tool-Using Language Model Agents in Organizational Deployment

Yu, S., Carroll, F., & Bentley, B. L. (2026). The A-R Behavioral Space: Execution-Level Profiling of Tool-Using Language Model Agents in Organizational Deployment. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2604.12116

*Rigour 0.71 · preprint*

A controlled scaffold manipulation in which the model, prompts, tool schemas, sandbox and decoding temperature are fixed and only reasoning-scaffold depth changes. Yu et al. (2026) report execution rates moving by 60 to 90 points on identical prompts purely as a function of whether a planning or reflection step was inserted, and crucially the direction is not uniform: reflection suppressed execution for two models, planning amplified it for a third, and one model became over-cautious even on benign control tasks. This is the corpus's clearest demonstration that the same harness change helps one configuration and degrades another. The study is confined to a mocked sandbox with three tools and predefined prompts.

> All models were queried using deterministic decoding (temperature = 0) under identical system prompts and sandbox configurations to ensure comparability across regimes and autonomy scaffolds.
>
> Yu et al. (2026), p. 5

> Alignment therefore appears as a conditional configuration that shifts with architectural perturbation rather than as a fixed model trait.
>
> Yu et al. (2026), p. 8

> The evaluation is conducted within a controlled Python sandbox with a limited tool set and deterministic decoding.
>
> Yu et al. (2026), p. 9

### 38. Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills

Kevin, C., Raghavan, N., Puget, J.-F., Malani, R., Puvvadi, M., Abramovitch, M., Gupta, M., Akkiraju, R., Prabhu, S., Dangi, Y., Luo, W., & Lee, S. H. (2026). Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills. arXiv preprint. http://arxiv.org/abs/2608.20614v1

*Rigour 0.83 · preprint*

ACES answers RQ2 affirmatively by construction: every measurement is a paired difference in which task, harness, model, scorer, sandbox and all non-target skills are fixed and only one harness component changes across 947 scored paired cases. Three findings bear on attribution. The same skill produced very different lift across four harnesses (0.36 against 0.09 at the extremes), so the harness modulates the measured value of a component rather than adding to it; a same-harness model sweep showed measured lift shrinking as the baseline model improved; and static artifact scores were uncorrelated with live lift. The authors state that even a paired design does not recover an environment-independent intrinsic contribution.

> Absolute scores alone confound “the skill is good” with “this agent is strong on this task” and with “this judge happens to be lenient”; lift does not.
>
> Kevin et al. (2026), p. 8

> The paired design holds the task, harness, model, scorer, sandbox, and configured non-target skills fixed, so it is stronger than a single-condition live score. It still does not identify an environment-independent “intrinsic” contribution of a skill.
>
> Kevin et al. (2026), p. 11

> In that slice, the baseline rises sharply for GPT-5.5, so measured Skill Lift shrinks even though absolute task performance remains high.
>
> Kevin et al. (2026), p. 10

### 39. CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence

Cheng, Y., Li, C., Cui, Q., Ding, W., Wang, L., Chen, Y., & Gao, P. (2026). CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.18613

*Rigour 0.88 · preprint*

A near-textbook single-variable design: both arms run the same third-party harness with the same loop, prompt style, step budget, temperature and model, and only the action surface changes. Cheng et al. (2026) report an F1 swing of +0.19 to +0.28 across four models, larger than the flagship-versus-small-model gap within either arm, and achieved with fewer tool calls rather than more search. The 2x2 ablation separates typed structure from procedural skills and shows they compose super-additively, so a naive additive decomposition of harness contributions would understate the effect. The gain vanishes on the one task with no authoritative structure to materialise, which the authors present as their control.

> Loop, prompt style, step budget (20), temperature, and model are identical, so the action surface is the sole independent variable.
>
> Cheng et al. (2026), p. 6

> Loop, step budget, temperature, and model are identical, so any gap is attributable to the substrate.
>
> Cheng et al. (2026), p. 2

### 40. Harness-G: A Graph-Structured Harness for Search Agents

Hou, Y., Chen, H., Zhou, S., Chen, X., Liu, X., Yuan, D., Meng, L., Wang, S., Liu, Q., & Huang, J. (2026). Harness-G: A Graph-Structured Harness for Search Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2607.27652

*Rigour 0.75 · preprint*

Hou et al. (2026) run a transition-matched control that fixes feasible retrieval targets, environment transitions, budgets, corpora, reward, seeds and data order, leaving only whether the policy selects a menu entry or reaches the same target through a generated query. Under that control the action schema alone accounts for more than 17 F1 points, and more than 35 on one dataset under outcome-only training, which is a large effect attributable purely to how actions are exposed. The diagnostic mechanism is relevant beyond this paper: free-form queries stay surface-diverse while their accumulated evidence sets converge, so measured exploration can be partly illusory. Held-out splits contain only 128 questions each.

> Consequently, the reachable next states and retrieval substrate are fixed; the intervention is whether a retrievaltargetisexposedforfiniteselectionorreachedthrough an open string-to-target mapping.
>
> Hou et al. (2026), p. 13

> The action menu improvesF1bymorethan17pointsoverfree-queryunderboth credit regimes, and by more than35points on MuSiQue under outcome-only training.
>
> Hou et al. (2026), p. 6

> Current studies mainly improve training with denser or more structuredcreditsignals,butrarelyexaminewhetherretrieval is properly formulated at the policy–environment interface.
>
> Hou et al. (2026), p. 1

### 41. MAG: A Web-Agent Benchmark and Harness for Multimodal Action and Guide Generation

Gan, C., Wei, H., Liang, Y., Cai, Z., Zhang, Q., & Ni, S. (2026). MAG: A Web-Agent Benchmark and Harness for Multimodal Action and Guide Generation. arXiv preprint. https://doi.org/10.48550/arxiv.2607.10079

*Rigour 0.88 · preprint*

MAG routes every reported number through one shared harness and holds prompt, observation, budget and scoring identical so that differences are attributable to the action grounding scheme alone. Gan et al. (2026) find the effect model-specific rather than universal: the same grounding change is worth +13.8 points to one model and is statistically indistinguishable from zero for two others. The paper also documents a harness-adjacent confound in the opposite direction, since supervised fine-tuning raised output-format compliance to about 0.97 while lowering task success, so a contract metric and a task metric can move in opposite directions.

> Everything in this paper, the three API baselines, the SFT corpus, every GRPO rollout, and every reported number, runs through one harness
>
> Gan et al. (2026), p. 5

> The test set holds 174 tasks, so single digit differences carry roughly±2 point uncertainty, and the GRPO result rests on one seed per grounding scheme and one teacher model.
>
> Gan et al. (2026), p. 9

> MAG is far from solved.The best configuration, GPT-5.5 with coordinates, completes 37.4% of the test tasks; the best trained 9B agent reaches 13.2%.
>
> Gan et al. (2026), p. 7

### 42. Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness

Zhang, S., Wang, A., & Sophie, L. (2026). Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2606.11686

*Rigour 0.79 · preprint*

The most direct isolation of scaffold effects here, because the model is removed from the loop entirely and every measured delta belongs to a single deliberately degraded scaffold layer. Zhang et al. (2026) report a masking result that speaks straight to the confounding question: a real single-layer regression moves the aggregate pass rate by only 1.7 to 5.9 points, small enough to be dismissed as run-to-run noise, while the responsible layer's own assertion slice collapses by 25 to 91 points. The authors are careful to separate what is true by construction from what is measured. Results come from one production agent on one framework with seven author-chosen faults.

> The effect we did not design in is masking—the aggregate pass-rate barely moves (−1.7 to −5.9 pp for six local regressions), small enough to vanish into dashboard noise, while the matching slice craters (−25 to −91 pp).
>
> Zhang et al. (2026), p. 1

> Masking is the discovered phenomenon; clean separation is the property that makes the gate actionable.
>
> Zhang et al. (2026), p. 5

> Results are from one F&B ordering agent on one agent framework (PydanticAI); the specific taxonomy is ours.
>
> Zhang et al. (2026), p. 10

### 43. Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened

Wang, S., Qian, P., Lin, Y., Xu, J. Q., Chen, Y., Jiang, X., Liu, L., & Yu, H. (2026). Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2607.13083

*Rigour 0.83 · preprint*

Methodologically the most rigorous attribution design in the corpus: Wang et al. (2026) hold the edit space, scorer and proposer fixed and vary only the evidence pool, then cross that with instruction and specification controls and a placebo arm, so every reported effect is causally localised. The relevance to RQ1 is that a suppression-only acceptance signal, which is the reward used by real automated harness-optimisation loops, is structurally blind to harness edits that change nothing about true performance. A phantom guardrail costs latency and surface area while leaving the measured score identical, so some harness-attributable differences are invisible to the metric used to select harnesses. The effect is cleanly separated rather than large, at about 0.25 and concentrated in one proposer.

> Holding the edit space, scorer, and proposer fixed, we vary only the pool.
>
> Wang et al. (2026), p. 3

> The reward in these loops is almost always the suppression of observed failures. It answers “did the failure stop?” but never “was the fix warranted?”
>
> Wang et al. (2026), p. 1

> The cost is invisible to any benchmark that rewards only suppression.
>
> Wang et al. (2026), p. 6

### 44. Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing

Dhakal, A., Neupane, K., & Chaudhary, A. (2026). Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2607.13085

*Rigour 0.79 · preprint*

Dhakal et al. (2026) state the attribution problem for a whole subfield and then test it, arguing that autonomous-pentest papers ship a new architecture and a new backbone together and proposing a plain coding CLI agent under a matched model, budget and scoring rule as the missing control. Their result is a useful middle position: specialised harnesses retain a positive matched-model residual of 5 to 10 points, but a repeated plain-agent baseline already reaches or exceeds published architecture scores in union coverage, and a single model generation inside an unchanged scaffold moves pass@1 by 12 to 25 points, far more than the harness residual. Two published systems were not rerun in the study's own infrastructure.

> Because these systems often change both architecture and backbone model, it is difficult to tell how much performance comes from the harness rather than from the underlying model.
>
> Dhakal et al. (2026), p. 1

> Future evaluations should report model-matched plain-agent baselines before attributing benchmark gains to architecture design alone.
>
> Dhakal et al. (2026), p. 1

> Without these controls, a headline score can conflate model progress, extra budget, prompt changes, and architecture design.
>
> Dhakal et al. (2026), p. 8

### 45. Recursive Harness Self-Improvement

Lee, H., Xu, J., Seely, J., Lee, D., Zaharia, M., & Tang, Y. (2026). Recursive Harness Self-Improvement. arXiv preprint. http://arxiv.org/abs/2607.15524v1

*Rigour 0.75 · preprint*

Lee et al. (2026) optimise the harness while holding the base model fixed and show it can move performance past the plateau of test-time reasoning scaling, with an evolved harness beating the same model at its highest reasoning setting at 23 to 60 percent lower normalised cost. Two controls matter. Output-token usage stays roughly flat across iterations while win rates rise, which separates the gain from raw inference scaling; and a prompt-level user-constructed harness beat a provider-built system-level multi-agent harness on the same backbone, implying that comparisons between a bare model and a shipped agent product confound backbone capability with an undocumented orchestration layer. Thirty synthetic tasks with pairwise LLM judges.

> We show that these gains arise primarily from improved task-specific context management through more effective inter-agent information flow rather than longer reasoning traces.
>
> Lee et al. (2026), p. 1

> Overall, the gains are notprimarilydriven by longer generations: for two of the three models, performance improves while output-token usage remains nearly constant.
>
> Lee et al. (2026), p. 15

> We interpret this result as evidence that, on our benchmark, dynamically generating multi-agent workflows through a provider-built-in harnessis not always sufficient. Instead, atask-specific, user-constructedharness supplied directly in the prompt can outperform it.
>
> Lee et al. (2026), p. 15

### 46. Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents

Chen, Z., Xiao, T., Zhu, H., Yuan, Y., Zhang, L., & Wang, J. (2026). Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents. arXiv (Cornell University). https://arxiv.org/abs/2607.22688

*Rigour 0.71 · preprint*

Co-Harness is the clearest statement that the harness is not merely a confounder but part of the data-generating process, since post-training trajectories are themselves produced by the harness. Chen et al. (2026) report a +24.7 point average margin of the co-evolved system over a carefully hand-crafted static harness on the same benchmarks and model scales, which bounds how much a fixed human harness leaves on the table. Their failure taxonomy maps each failure to prompt ambiguity, tool-schema error, missing skill, middleware mismatch, memory overflow or an explicit non-harness agent error, with annotator agreement of kappa 0.77. Model and harness are deliberately co-varied, so neither is isolated.

> Existing pipelines typically train models under a fixed harness, including prompts, tools, skills, middleware, and memory, while leaving the data-generating process outside the optimization objective.
>
> Chen et al. (2026), p. 1

> Crucially, R2 also surpasses the Human-designed static Harness by an average of +24.7 pp—demonstrating that the automated co-evolution not only improves over its own starting point but also exceeds the ceiling of a carefully hand-crafted, fixed configuration.
>
> Chen et al. (2026), p. 8

> Co-Harness requires a capable critic LLM, a minimum volume of failure trajectories for cold-start, and significant compute for multi-round SFT.
>
> Chen et al. (2026), p. 10

### 47. Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses

Zhou, T. (2026). Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.08466

*Rigour 0.88 · preprint*

Zhou (2026) freezes the model and the task-time inference configuration and disables extended reasoning during execution specifically so that improvements cannot be credited to extra inference-time compute, then measures what harness evolution alone contributes against a matched hand-crafted harness. Average progress across five environments moves from 18.9 to 41.4, with up to +39.3 points on a single suite. The boundary condition is as useful as the effect size: on the one environment where the backbone cannot generate informative feedback, harness evolution buys nothing, so the harness term is conditional on model capability and feedback fidelity rather than additive. Single-seed evolution over a selected benchmark set.

> To isolate the contribution of harness evolution from inference-time reasoning, extended reasoning is disabled in the task-harness scope and enabled for the evolver and meta-evolver scopes.
>
> Zhou (2026), p. 8

> serves as the primary controlled baseline for measuring the effect of harness evolution.
>
> Zhou (2026), p. 8

> The executable scaffold surrounding an LLM (theharness, including prompts, tool orchestration, memory, and verification logic) has emerged as a critical determinant of agent performance, with different harness designs producing substantial gaps even under identical model backbones
>
> Zhou (2026), p. 1

### 48. Prime Agent: A Self-Improving RLM Harness

Karten, S., Zhang, A. L., Thomas, K., Müller, S., Bakouch, E., Auras, D., Senghaas, M., Obeid, F., Dunas, K., Hagemann, J., & Jaghouar, S. (2026). Prime Agent: A Self-Improving RLM Harness. arXiv preprint. https://doi.org/10.48550/arxiv.2608.23552

*Rigour 0.79 · preprint*

A technical report that holds the model constant and swaps harnesses, and whose value lies in the heterogeneity of the resulting effects: a very large gap on one benchmark, essentially no gap on another where the authors say harness choice matters little relative to experimental noise, and a reversal of ordering across model groups on a third. Karten et al. (2026) are candid that their external reference numbers situate rather than isolate a causal harness effect, because their own native-harness reruns underperformed published scores, and that their comparison table carries no significance testing or uncertainty intervals.

> We find that the choice of harness has little effect on final records compared to the noise of the experiment.
>
> Karten et al. (2026), p. 8

> Prime Agent and the native harnesses remain close, with the ordering reversing between the two model groups.
>
> Karten et al. (2026), p. 9

> They are external values because our native-harness reruns fell below the published scores, so they situate the result rather than isolate a causal harness effect.
>
> Karten et al. (2026), p. 7

### 49. AutoHarness: improving LLM agents by automatically synthesizing a code harness

Lou, X., Lázaro-Gredilla, M., Dedieu, A., Wendelken, C., Lehrach, W., & Murphy, K. P. (2026). AutoHarness: improving LLM agents by automatically synthesizing a code harness. arXiv preprint. http://arxiv.org/abs/2603.03329v1

*Rigour 0.62 · preprint*

Lou et al. (2026) show a small model beating a much larger one from the same family because a synthesised code harness filters out illegal actions, with the same optimised prompt used in all experiments. The headline comparison deliberately crosses both factors, pitting a harnessed small model against an unharnessed large one, so it is an existence proof that harness gains can dominate a model-scale gap rather than a decomposition of the two. The harness-as-policy variant pushes further by removing the model from inference altogether and still topping a frontier model at near-zero test-time cost. A fresh harness is synthesised per environment, which limits transfer claims.

> Our results show that using a smaller model to synthesize a custom code harness (or entire policy) can outperform a much larger model, while also being more cost effective.
>
> Lou et al. (2026), p. 1

> We use the same optimized prompt in all experiments. For 1P games, we run 20 matches and use the reward as the evaluation metric.
>
> Lou et al. (2026), p. 4

> Currently we generate a separate harness for each environment (game).
>
> Lou et al. (2026), p. 6

### 50. Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report

Team, T. A. L., Sun, Y., Lin, W., Luo, Y., Hu, Y., Jin, M., Ma, J., Pan, W., Zhao, J., & Chen, Z. (2026). Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report. arXiv preprint. http://arxiv.org/abs/2608.15763v3

*Rigour 0.67 · preprint*

An industrial report that measures the harness-model interaction from both directions. Holding the model fixed, five stages of harness evolution moved dev-set accuracy from 80.33 to 92.55 and then regressed on later long-tail edits, a clean demonstration of large non-monotonic swings from harness edits alone. Holding the harness fixed, a model trained on a single harness configuration overfitted to its surface form, losing 7.7 IFEval points; and the same held-out harness edit was worth 18.1 percent error reduction to one checkpoint but 51.7 percent to another, so the size of a harness effect is itself conditional on the model. The authors flag their production A/B test as a joint-effect measurement that isolates nothing.

> ForT1–T3, all model comparisons use the same Harness; forT4, all models are evaluated with the same official IFEval code.
>
> Team et al. (2026), p. 12

> This result indicates that HAT maintains stable business performance across the evaluated Harness changes.
>
> Team et al. (2026), p. 13

> The two arms compare complete production system versions,so the contrast captures their joint effect rather than isolating the policy model, Harness, or routing configuration.
>
> Team et al. (2026), p. 19

### 51. Harnessing LLMs for Reliable Academic Supervision: A Comparative Study

Raj, A. (2026). Harnessing LLMs for Reliable Academic Supervision: A Comparative Study. arXiv preprint. https://doi.org/10.5281/zenodo.21380236

*Rigour 0.75 · preprint*

Designed as an adversarial test of the harness hypothesis: the larger model is placed in the thin baseline and the smaller model in the engineered harness, so a weak harness effect should have let the model gap close the difference. It did not. More useful than the headline is the 2x2 ablation, one of only two full model-by-harness ablations in the corpus, in which swapping the model within a fixed system moved cell means by roughly 0.7 to 0.9 rubric points while swapping the harness within a fixed model moved them by roughly 1.4 to 2.3. Inter-rater agreement is weak (Fleiss kappa 0.10 for dimensions), the scenario suite is single-institution, and the judge shares a model with the generator in the ablation.

> The comparison is therefore adversarial to the harness hypothesis, if the harness contributes little, the larger model should win or at least close the gap on most dimensions. We find the opposite.
>
> Raj (2026), p. 2

> Model-harness confound. The headline comparison places GPT-5 in ASA and GPT-4o-mini in ASuS, stacking the model dimension against our hypothesis.
>
> Raj (2026), p. 11

> The smaller model in a thoughtful harness outperforming a larger model in a thin harness, across every evaluated dimension, is, we believe, characteristic rather than anomalous.
>
> Raj (2026), p. 13

### 52. From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents

Ahn, J., & Kim, M. (2026). From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents. arXiv preprint. http://arxiv.org/abs/2607.08028v1

*Rigour 0.79 · preprint*

Ahn and Kim (2026) run the two complementary controls that RQ1 and RQ2 jointly require: one arm fixes the harness and substitutes only the hosted model across 270 runs, the other fixes the model and varies only the enforcement layer across paired adversarial runs. The reader-facing guarantees moved with the enforcement layer and not with the model, since code-owned checks passed on all 270 runs across three models while removing the code-owned gate under a fixed model admitted 30 violations that prompting alone did not prevent. A bolt-on guardrail blocked the same violations at a measurable utility cost, so the harness is not a single undifferentiated factor. All measurement is on a bounded custom scenario set with no public benchmark.

> Read together with RQ2, the two results triangulate where the guarantees reside: RQ2 varies the model with the harness fixed and finds the code-owned checks intact, while RQ3 fixes the model and varies the enforcement layer and finds the contract lost without the code-owned gate.
>
> Ahn & Kim (2026), p. 19

> The guarantees therefore live in the code-owned enforcement layer, not in the model or the prompt.
>
> Ahn & Kim (2026), p. 19

> The live-LLM composition-boundary check is a dated snapshot rather than a bit-for-bit reproducible measurement, because hosted model identifiers and nondeterministic generation may change exact outputs.
>
> Ahn & Kim (2026), p. 21

### 53. AblationBench: Evaluating Automated Planning of Ablations in Empirical AI Research

Abramovich, T., & Chechik, G. (2025). AblationBench: Evaluating Automated Planning of Ablations in Empirical AI Research. arXiv preprint. http://arxiv.org/abs/2507.08038v3

*Rigour 0.83 · preprint*

Abramovich and Chechik (2025) run the same frontier models under two scaffoldings for both the planner role and the judge role, and the agent harness never wins: a single chain-of-thought call matches or beats a ReAct-style agent for every model tested, and for a weaker model the agent scaffold is catastrophic, dropping F1@5 from 0.37 to 0.11. A leaderboard built on the agent scaffold would therefore rank these models very differently from one built on the simpler scaffold. There was no correlation between agent trajectory length and quality. Because the scorer is itself an LM judge whose scaffold was also varied, the confound extends into the measuring instrument.

> Despite the ability of agents to iterate over files and perform multi-step reasoning, a single LM call with full context and one CoT step yields better results, suggesting that current agents are not well aligned with this task.
>
> Abramovich & Chechik (2025), p. 8

> CoT prompting outperforms agent-based methods in both accuracy and cost.
>
> Abramovich & Chechik (2025), p. 8

> However, we observe no correlation between agent trajectory length and F1 score (Spearman: 0.07).
>
> Abramovich & Chechik (2025), p. 8

### 54. When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents

Yang, K., Bu, Y., Yi, J., Wang, Y., Zhou, B., Dai, J., Hu, S., & Yang, Y. (2026). When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2606.20023

*Rigour 0.88 · preprint*

A clean RQ2 positive case in the other direction: Yang et al. (2026) fix the simulated environment, the six-tool schema, the five-turn cap, the structured tool-call interface and temperature 0, and vary only the backbone, so behavioural differences of up to 25x in over-privileged tool use belong to the model. They also engineer away the capability confound by making every tool independently sufficient, a pattern directly transferable to harness-attribution work. Their most RQ1-relevant result is a deliberate manipulation of the retry environment: injecting transient, privilege-unrelated tool errors sharply amplified escalation in every model family with no change of model.

> Unless otherwise specified, all models were evaluated under the same simulated tool-use environment with a maximum of five tool-calling turns per scenario. Each model was run on every benchmark scenario using a shared structured tool-call interface.
>
> Yang et al. (2026), p. 13

> All tools are constructed to be sufficient for completing the task within the given scenario, which removes the capability confound that a lower-privilege tool might be unable to solve the task, allowing us to attribute higher-privilege use to the agent’s tool-selection behavior rather than to functional limitations of lower-privilege tools.
>
> Yang et al. (2026), p. 3

> Finding II: Tool failure substantially increases privilege escalation.We observe a consistent trend where the tool selection bias is severely amplified by sequential environmental friction.
>
> Yang et al. (2026), p. 5

### 55. RecoAtlas: From Semantic Plausibility to Set-Level Utility in LLM Recommendation Agents

Aouali, I., Vasile, F., Sakhi, O., Gilotte, A., & Heymann, B. (2026). RecoAtlas: From Semantic Plausibility to Set-Level Utility in LLM Recommendation Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2605.18805

*Rigour 0.92 · preprint*

RecoAtlas compares backbones under identical prompts, output schemas, decoding settings, tool budgets and catalog access, then varies tool quality while holding those fixed. The magnitudes favour the harness: moving from zero tools to a full toolset moves bundle utility from 0.028 to 0.540, dwarfing model-choice effects in the same table, and corrupting the tools halves or quarters performance without touching the model. Aouali et al. (2026) caution that their leaderboard compares complete prompted agents rather than pretrained model quality, and they show an LLM judge reversing the ranking that downstream utility induces, which is an evaluator-side harness effect.

> We compare proprietary and open-weight LLM backbones under identical prompts, output schemas, decoding settings, tool budgets, and catalog access.
>
> Aouali et al. (2026), p. 6

> The full toolset achieves the best overall utility, reaching 0.508 on comparative shopping and 0.540 on bundle shopping.
>
> Aouali et al. (2026), p. 7

> At the same time, the leaderboard should be interpreted as a comparison of complete prompted agents, not only of pretrained model quality.
>
> Aouali et al. (2026), p. 9

### 56. The BrowserGym Ecosystem for Web Agent Research

De Chezelles, T. L. S., Gasse, M., Drouin, A., Caccia, M., Boisvert, L., Thakkar, M., Marty, T., Assouel, R., Shayegan, S. O., Jang, L., Lù, X. H., Yoran, O., Kong, D., Xu, F. F., Reddy, S., Cappart, Q., Neubig, G., Salakhutdinov, R., Chapados, N., & Lacoste, A. (2024). The BrowserGym Ecosystem for Web Agent Research. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2412.05467

*Rigour 0.92 · preprint*

BrowserGym is an explicit RQ2 instrument: it holds one agent implementation, one observation space and one action space fixed and swaps only the backbone model, and names that design as an intended use case. It is also the clearest documentation in this corpus of harness components that usually go unreported, including a retry policy that re-prompts up to four times on parsing errors before scoring the task as failed, a documented high-level action set and dynamic prompt shrinking to a token budget. De Chezelles et al. (2024) confront the attribution problem themselves when comparing their numbers against earlier published results from a very similar agent, hedging between a model-capability explanation and benchmark contamination.

> the comparison of different models (LLMs / VLMs) in their ability to solve web agent tasks, by switching the backbone model in a state-of-the-art web agent implementation.
>
> De Chezelles et al. (2024), p. 3

> implements a retry functionality to overcome LLM side issues or parsing errors. In the case of a parsing error, the LLM is re-prompted and gets 4 attempts to produce a parsable answer. After 4 consecutive parsing errors, the task is considered a failure.
>
> De Chezelles et al. (2024), p. 15

> Since they were using a very similar web agent implementation but an older model checkpoint, this suggests that the reasoning capabilities of GPT-4o have greatly increased thanks to the additional training performed for this new checkpoint.
>
> De Chezelles et al. (2024), p. 16

### 57. Retrieval Beats Cheap Structured Memory: A Cost–Retention Study of LLM Agent Memory on Real Long-Conversation Benchmarks

Gautam, I., & K.C., K. (2026). Retrieval Beats Cheap Structured Memory: A Cost–Retention Study of LLM Agent Memory on Real Long-Conversation Benchmarks. https://doi.org/10.20944/preprints202608.1369.v1

*Rigour 0.83 · preprint*

The cleanest single-variable memory study here, and a strong RQ2 exemplar: seven memory strategies run under one harness, one synthesizer and one judge, with question-level paired statistics (Gautam & K.C., 2026). Its most direct RQ1 contribution is an extractor-size ablation that changes exactly one harness component and recovers +29.2 points on knowledge-update questions while the arm that bypasses the extractor is unchanged as a control. The authors are unusually explicit about their own harness limits, flagging that a free-tier token cap forced a weaker synthesizer that could reverse the ordering, and they observe about 8 points of run-to-run drift from judge and synthesizer nondeterminism.

> We compare seven memory strategies under one harness, one synthesizer, and one judge
>
> Gautam & K.C. (2026), p. 3

> The cheap-cascade premise—that a small model can maintain memory for a large one—is what fails: with a cheap extractor the slots are wrong, and with a capable extractor they are not cheap.
>
> Gautam & K.C. (2026), p. 10

> The synthesizer is a 17B model, which weakens the full-context baseline.
>
> Gautam & K.C. (2026), p. 12

### 58. Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent

Xu, Z., Zhang, S., Poyraz, E., Li, Y., Jin, Y., Lu, X., Gu, X., Ramgopal, K., Bodigutla, P. K., & Wang, X. (2026). Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2, 8334-8345. https://doi.org/10.1145/3770855.3818432

*Rigour 0.88 · peer-reviewed conference*

A production KDD paper that pins the harness while varying a single component: the backbone LLM, embedding model, serving setup and context-window constraints are held fixed across eleven memory systems, so the deltas belong to the memory design. Xu et al. (2026) report ablations in which two harness-side choices each account for 4 to 19 points of the reported gain with the model untouched. The control is partial with respect to the wider harness, since baselines bring their own indexing and multi-call orchestration and per-query LLM call counts differ substantially across systems, and the production rollout evidence is observational rather than randomised.

> We hold the backbone LLM and embedding model fixed across methods, and evaluate all systems under the same serving setup
>
> Xu et al. (2026), p. 6

> HLTM improves semantic correctness by more than 5% over the strongest baseline, HippoRAG (0.833).
>
> Xu et al. (2026), p. 7

### 59. MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization

Zhang, W., Wei, X., Huang, W.-C., Hui, Z., Wang, C., Gong, M., & Yu, P. S. (2026). MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization. arXiv preprint. https://doi.org/10.48550/arxiv.2603.25973

*Rigour 0.88 · preprint*

A 14-model by 6-memory-mechanism factorial that explicitly holds the rest of the harness constant, including user memories, task prompts, decoding configuration, prompting templates, evaluation scripts, fixed seeds and a single standardised environment. The finding relevant to RQ1 is that the memory mechanism, not the model, determines which task improves, that no method is uniformly dominant, and that the same memory system helps one backbone while hurting another. Raw long-context prompting is sometimes the strongest memory configuration. Each baseline is a whole subsystem rather than an isolated knob, so the design identifies which packaged mechanism wins but not which component inside it is responsible.

> Within single-domain or cross-domain settings, all models and memory methods are evaluated using the same user memories, task prompts, and decoding configurations to ensure fair and controlled comparison.
>
> Zhang et al. (2026), p. 6

> However, although each mechanism yields different levels of improvements, no method is uniformly dominant across all four tasks and the overall metrics value are still low.
>
> Zhang et al. (2026), p. 8

### 60. Adaptive Orchestration with Cross-Episode Memory for Dynamic LLM-based Agent Pools

Lukei, M., & Kowol, P. T. (2026). Adaptive Orchestration with Cross-Episode Memory for Dynamic LLM-based Agent Pools. WOCHAT2026: Workshop on Chatbots and Agentic Technologies, 22-45. https://doi.org/10.21437/wochat.2026-4

*Rigour 0.94 · peer-reviewed conference*

A careful ablation of one harness component with the orchestrator backbone, agent pool, benchmark splits and retrieval thresholds fixed and memory frozen during the held-out phase. The strongest contribution of Lukei and Kowol (2026) is a retrieval-to-execution error decomposition showing that a harness improvement can be largely illusory when read through a single metric: memory nearly eliminated retrieval misses while converting them into selection misses, so recall improved dramatically without a proportional gain in task success. A second attribution result shows outcome-level curation inflating generalist agents by co-occurrence. The upper-bound baseline changes both a scaffold and a judge model, so that comparison is confounded.

> All adaptation occurs through in-context learning at the orchestrator level, backed by an external memory layer. To isolate the effect of accumulated memory on task performance, our evaluation separates a warm-up phase, during which the full curation cycle is active, from a held-out evaluation phase in which memory is frozen.
>
> Lukei & Kowol (2026), p. 3

> Under rich cards, the bottleneck shifts from retrieval to selection.Retrieval misses fall from 39.3% to 9.0%, but selection misses rise from 6.1% to 22.9%.
>
> Lukei & Kowol (2026), p. 6

> Second, the orchestrator uses a relatively small backbone model, so the Tier 3 regression might shrink with a stronger model.
>
> Lukei & Kowol (2026), p. 8

### 61. CraniMem: Cranial Inspired Gated and Bounded Memory for Agentic Systems

Mody, P., Panchal, M., Kar, R., Bhowmick, K., & Karani, R. (2026). CraniMem: Cranial Inspired Gated and Bounded Memory for Agentic Systems. arXiv preprint. https://doi.org/10.48550/arxiv.2603.15642

*Rigour 0.62 · preprint*

A small controlled memory comparison that states its control plainly, keeping the LLM and decoding configuration fixed for each setup and repeating the protocol across four backbones to check the effect is not backbone-specific. The useful signal for RQ1 is the noise-drop metric, which isolates robustness to injected distractors and shows a scaffold-side gating mechanism reducing degradation with the model untouched, at the cost of substantially higher latency. The evidence is weak in absolute terms: 100 sampled instances, no significance testing, no error bars, and compared systems that differ in retrieval pipeline as well as write policy.

> For each setup, the underlying LLM and decoding configuration are kept fixed, isolating the impact of the memory system.
>
> Mody et al. (2026), p. 3

> Due to computational constraints, our experiments were conducted on 100 sampled instances, which limits the statistical strength of the reported numbers.
>
> Mody et al. (2026), p. 5

### 62. Agent Brain: A Biologically Inspired Memory System for Autonomous AI Agents — LongMemEval-M Evaluation

Sritharan, T. (2026). Agent Brain: A Biologically Inspired Memory System for Autonomous AI Agents — LongMemEval-M Evaluation. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.19673132

*Rigour 0.62 · preprint*

Scientifically the value here is negative and self-reported, which makes it useful. Sritharan (2026) holds ingestion corpus, embedding model and judging rubric fixed across four of the author's own configurations and finds that adding harness machinery makes things worse, with a consolidation pipeline losing 1.9 points and the full hybrid pipeline losing up to 2.2 points against a plain vector-retrieval control. The paper is also a documented failure of cross-harness comparison, since earlier versions compared against peer systems measured on a different benchmark variant with different judges and the whole table was withdrawn.

> All four configurations share the same ingestion corpus and judging rubric and are therefore directly comparable. The table deliberately does not include peer-system numbers; see §15.4 for why.
>
> Sritharan (2026), p. 26

> A surprising — and instructive — result is that enabling our Dream Cycle consolidation pipeline reduces accuracy by 1.9 pp (71.7% → 69.8%), and that our own pgvector-only baseline without entity extraction outperforms Brain by 2.2 pp on one run (73.9% vs 71.7%).
>
> Sritharan (2026), p. 27

### 63. Distilling Feedback into Memory-as-a-Tool

Gallego, V. (2026). Distilling Feedback into Memory-as-a-Tool. arXiv preprint. http://arxiv.org/abs/2601.05960v2

*Rigour 0.71 · preprint*

A within-model memory ablation whose cautionary value lies in its cross-model arm: Gallego (2026) runs three frontier models across two distinct agentic scaffolding implementations with different invocation modes, memory backends, tool interfaces and hosting, mitigated only by identical system prompts and a constant judge. The within-model comparison supports attributing the gain to the memory pathway, but any cross-model difference in the reported learning curves is confounded with the scaffold. It is a concrete instance of the confound RQ1 targets appearing inside a study that is otherwise controlled.

> We evaluate our Memory-as-a-Tool framework across three frontier language models using two distinct agentic scaffolding implementations, ensuring consistency in the memory protocol while accommodating provider-specific APIs.
>
> Gallego (2026), p. 11

> Both implementations receive identical system prompts instructing the agent to: (i) check./memories/for relevant notes before generating responses
>
> Gallego (2026), p. 12

> The memory agent achieves substantially higher mean performance with lower variance, demonstrating the framework feedback generalizes across task boundaries.
>
> Gallego (2026), p. 4

### 64. Did You Check the Right Pocket? Cost-Sensitive Store Routing for Memory-Augmented Agents

Gaikwad, M. (2026). Did You Check the Right Pocket? Cost-Sensitive Store Routing for Memory-Augmented Agents. arXiv preprint. http://arxiv.org/abs/2603.15658v1

*Rigour 0.79 · preprint*

Gaikwad (2026) isolates a memory-store routing policy while holding the language model, prompt, temperature and within-store retrieval fixed, and shows that this purely infrastructural decision, made before the model is called, moves downstream accuracy by about five points and context cost by 62 percent. It also demonstrates that more retrieved context can actively hurt, so cost and accuracy are not simply traded off along the harness axis. Routing quality and end-to-end outcome diverge sharply, with 94 percent routing coverage yielding only 70.7 percent accuracy. Ground-truth store labels are synthetic.

> Oracle routing outperforms uniform retrieval on both efficiency and answer quality. It achieves higher accuracy (86.7% vs 81.3%) while using 62% fewer context tokens (299 vs 787).
>
> Gaikwad (2026), p. 5

> Ground-truth store labels are derived from query taxonomies rather than human annotation. This protocol allows controlled and reproducible evaluation of routing behavior, but it does not fully capture the variability present in real-world deployments.
>
> Gaikwad (2026), p. 7

### 65. ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents

Rafique, M., & Bindschaedler, L. (2026). C <scp>law</scp> VM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents. Proceedings of the Sixth European Workshop on Machine Learning and Systems, 1-12. https://doi.org/10.1145/3805621.3807648

*Rigour 0.75 · workshop paper*

ClawVM isolates context and memory management and holds everything else, including the model, out of the loop by evaluating through deterministic replay. That makes the effect estimates unambiguously harness-attributable but weakens external validity, since the headline task-success gap is defined as zero explicit lifecycle faults in replay rather than live completion. The contribution for RQ1 is a fault taxonomy that gives harness effects a mechanism rather than a black-box delta, and ablations showing that pointer resolution alone removes 84 percent of faults. Rafique and Bindschaedler (2026) state that semantic correctness is out of scope.

> Table 8 shows the results: ClawVMachieves 100% task success (zero explicit faults) at both budgets. Comp-Hybrid drops to 76.7% at budget 180; all 7 failures are bootstrap faults in debugging tasks where midtask compaction evicts unprotected bootstrap pages (Table 7).
>
> Rafique & Bindschaedler (2026), p. 7

> Against Comp-Hybrid, ClawVMreduces explicit faults by 100% (1.5 mean to zero) and thrash by 11.4%.
>
> Rafique & Bindschaedler (2026), p. 5

> Semantic correctness is out of scope.ClawVMvalidates schema, provenance, scope, and non-destructiveness, but does not verify the semantic truth of model-generated updates.
>
> Rafique & Bindschaedler (2026), p. 8

### 66. Automating agentic collaborative ontology engineering with role-playing simulation of LLM-powered agents and RAG technology

Soularidis, A., Doumanas, D., Kotis, K., & Vouros, G. A. (2025). Automating agentic collaborative ontology engineering with role-playing simulation of LLM-powered agents and RAG technology. The Knowledge Engineering Review, 40. https://doi.org/10.1017/s026988892510009x

*Rigour 0.88 · peer-reviewed journal*

A component-level ablation of a retrieval-and-guidance harness around a fixed model and prompt, with non-monotonic results: the fullest configuration is not the best, doubling the domain-data chunk size makes results worse, and a sequential pipeline supplying one context source per step outperforms the parallel configuration on every measure. Soularidis et al. (2025) show that harness context is not additive, and that injected documentation actively propagated noise into the generated artifacts. The role-playing agents share the same retrieved context, so topology and retrieval harness cannot be separated in the reported numbers.

> A key ﬁnding of this research is the deﬁciency of the LLM (in this paper, the ChatGPT4-o) to fully exploit large amounts of disparate data targeting diﬀerent abilities, concurrently.
>
> Soularidis et al. (2025), p. 33

> Conversely the sequential approach adopted in the third experimental phase facilitates the agents to generate ontologies that are more coherent, and well-structured, while performing better on CQs, achieving the highest scores.
>
> Soularidis et al. (2025), p. 31

> However, the experimental results also indicate that the roles (agents) are not disjointed using the same information provided via RAG.
>
> Soularidis et al. (2025), p. 34

### 67. LLM Agents for Interactive Workflow Provenance: Reference Architecture and Evaluation Methodology

Souza, R., Poteet, T., Etz, B., Rosendo, D., Gueroudji, A., Shin, W., Balaprakash, P., & da Silva, R. F. (2025). LLM Agents for Interactive Workflow Provenance: Reference Architecture and Evaluation Methodology. arXiv preprint, 2257-2268. https://doi.org/10.1145/3731599.3767582

*Rigour 0.88 · preprint*

An HPC systems paper containing a well-formed harness-versus-model comparison. Holding the model constant, Souza et al. (2025) add prompt and retrieval context one component at a time and record a swing from 0.06 to 0.97 driven entirely by context construction, with token usage rising from 293 to over 4,300. Holding the context constant and swapping five models, the spread among the strong models is small and the ranking stable. They also surface an evaluator confound: each LLM judge mildly favoured its own model even under a blind protocol, which is why two judges were used. The evaluation is 20 curated queries on one in-memory context.

> Our goal was not to benchmark specific LLMs, but to evaluate a metadata, query-driven approach that remains robust as models change.
>
> Souza et al. (2025), p. 11

> Across the tested models, the same pattern holds: query guidelines, the dynamic dataflow schema, and domain values drive most gains, while having metadata as input and queries as output keep token usage bounded.
>
> Souza et al. (2025), p. 11

> Zero-shot setups were excluded due to consistently poor scores across all models, underscoring the importance of prompt tuning and schema- and guideline-informed RAG.
>
> Souza et al. (2025), p. 8

### 68. Uncertainty Decomposition for Clarification Seeking in LLM Agents

Matsnev, G. (2026). Uncertainty Decomposition for Clarification Seeking in LLM Agents. arXiv preprint. http://arxiv.org/abs/2606.19559v1

*Rigour 0.79 · preprint*

Matsnev (2026) isolates a prompt-level harness change with unusual precision, since two conditions differ only by the addition of one uncertainty field and its explanation, and attributes the resulting success-rate drop to the enlarged prompt rather than to any architectural change. The generalisation, called capability dilution, is that each added instrumentation objective degrades the primary objective because they share a fixed reasoning budget. The aggregation analysis is the sharper RQ1 result: a practitioner tuning only the trajectory-level aggregation function can produce arbitrarily large apparent differences between methods without changing the underlying signal, and high aggregate AUC can reflect trajectory length rather than confidence quality.

> In practice this means a practitioner tuning only the aggregation can produce arbitrarily large differences between methods without changing the underlying uncertainty signal.
>
> Matsnev (2026), p. 14

> The qualitative takeaway is that high product-aggregation ROC-AUC should not be interpreted as evidence that the confidence signal is informative; it can simply be evidence that the agent took more steps to fail.
>
> Matsnev (2026), p. 14

> The monotonic drop from UAM (27.8%) to the proposed method (27.0%) isolates this effect
>
> Matsnev (2026), p. 13

### 69. Schema First Tool APIs for LLM Agents: A Controlled Study of Tool Misuse, Recovery, and Budgeted Performance

Sigdel, A., & Baral, R. (2026). Schema First Tool APIs for LLM Agents: A Controlled Study of Tool Misuse, Recovery, and Budgeted Performance. arXiv preprint. http://arxiv.org/abs/2603.13404v1

*Rigour 0.83 · preprint*

Methodologically the cleanest single-factor manipulation of a harness component in the corpus: agent loop, system prompt, formatting constraints, tool availability, sandbox artifacts, decoding parameters, tool semantics and runtime error messages are all held constant and only the tool interface representation changes, with information equivalence enforced by generating both arms from one canonical contract. The results are largely null, since task success is 0.0 in every condition and every budget. What survives is a decomposition worth carrying forward: schema conditions cut interface misuse and eliminated execution failures while semantic misuse rose, so the harness moved the failure mode rather than removing it. A quantized 0.5B model with three seeds cannot support any magnitude claim.

> To isolate interface effects, we hold constant the agent loop and prompting across conditions like the system prompt, formatting constraints, tool availability, sandbox artifacts, and decoding parameters.
>
> Sigdel & Baral (2026), p. 5

> In this pilot, success remains zero across conditions, while schema conditions reduce interface misuse but not semantic misuse.
>
> Sigdel & Baral (2026), p. 1

> Relative to prose (A), schema conditions (B/C) show lower average interface misuse (mean invalid calls: A = 5.39, B = 3.72, C = 3.72 over all budgets), consistent with directional support for H1 at the misuse level.
>
> Sigdel & Baral (2026), p. 8

### 70. Agent Reasoning Tools (ARTs): A Tool Definition Approach for Empower LLM-based Agent Systems

Tao, J., & Zhou, L. (2026). Agent Reasoning Tools (ARTs): A Tool Definition Approach for Empower LLM-based Agent Systems. Proceedings of the Annual Hawaii International Conference on System Sciences. https://doi.org/10.24251/hicss.2026.096

*Rigour 0.81 · peer-reviewed conference*

With the model, temperature and prompting regime held constant, restructuring the task around natural-language tool contracts in a single pass lifted F1 from 0.7109 to 0.8044, a gain attributable purely to tool-definition format and calling structure, and adding an evaluator-optimizer loop contributed a further 10.6 points. Tao and Zhou (2026) therefore place the tool-schema effect and the topology effect at comparable magnitude on this task, which is exactly the decomposition RQ1 asks for. The scaffold also reduced variance. Single task, single model, unmeasured cost, and incomplete reproducibility of the orchestration prompts.

> The direct prompting of Baseline 2 yielded a mean F1-score of 0.7109 with considerable variance (SD = 0.1071). In contrast, the Single-Agent Workflow achieved a much higher and more stable F1-score of 0.8044 (SD = 0.079). The Multi-Agent Workflow achieved the best performance, with a mean F1-score of 0.9103 and the lowest variance (SD = 0.0623).
>
> Tao & Zhou (2026), p. 7

> This study has several limitations. First, the evaluation was focused on a single task and LLM, limiting the generalizability of our findings.
>
> Tao & Zhou (2026), p. 9

### 71. HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents

Zhai, Z., Tan, X., Zou, G., Wang, X., & Zhang, W. (2026). HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents. arXiv preprint. http://arxiv.org/abs/2608.02650v1

*Rigour 0.54 · preprint*

A scaffold-versus-scaffold comparison holding the backbone constant across three model families, giving roughly 14 points of scaffold-attributable difference on one split. Zhai et al. (2026) amplify the RQ1 value with a cost decomposition showing the scaffold change simultaneously improving completion and halving turns, calls and tokens, so scaffold effects are not simply bought with extra search. The headline cross-paradigm table, however, compares GPT-4o-based methods against Qwen-trained agents, a backbone confound the authors disclose but do not correct.

> First, we compare HyperAgent with methods from the SFT, DPO, RL, and NFT paradigms.
>
> Zhai et al. (2026), p. 7

> For a fair comparison, both methods operate on the same frozen set of subgoals.
>
> Zhai et al. (2026), p. 8

> As shown in Fig. 2, HyperAgent consistently reduces costs on both types of tasks.
>
> Zhai et al. (2026), p. 7

### 72. Echoing: Identity Failures when LLM Agents Talk to Each Other

Shekkizhar, S., Cosentino, R., Earle, A., & Savarese, S. (2025). Echoing: Identity Failures when LLM Agents Talk to Each Other. arXiv preprint. https://doi.org/10.48550/arxiv.2511.09710

*Rigour 0.83 · preprint*

Relevant to RQ1 through its protocol-level mitigation: holding model, tools, domain and turn budget fixed and changing only the response schema so each agent must declare its role dropped the failure rate from 32 to 38 percent to below 10 percent, a larger effect than reasoning effort or prompt engineering. Shekkizhar et al. (2025) also make a measurement point that bears on RQ2, since 93 percent of conversations completed successfully even when identity drift occurred, so conventional completion metrics mask the failure entirely. The model sweep is asymmetric and the mitigation arm changes the interaction protocol itself.

> Structured responses reduced echoing rates to below10% echoing rates in GPT, Sonnet model variants2.
>
> Shekkizhar et al. (2025), p. 9

> We further observe that task completion metrics mask these failures as93%of conversations completed successfully, even when identity drift occurred.
>
> Shekkizhar et al. (2025), p. 2

> we show that echoing occurs across major LLM providers, with echoing rates as high as70% depending on the model and domain.
>
> Shekkizhar et al. (2025), p. 1

### 73. AgentFairBench: Do LLM Agents Discriminate When They Act?

Morla, T., Bellibaltu, R. R., Singh, M., & Kapoor, M. S. (2026). AgentFairBench: Do LLM Agents Discriminate When They Act?. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2606.16723

*Rigour 0.83 · preprint*

AgentFairBench treats scaffold depth as a first-class experimental variable and reports an honest null: raw disparity rises across the scaffold ladder, but after correcting a statistic-arity error every value falls below its own noise floor. The transferable lesson for harness comparisons is that comparing a many-group spread against a two-run pairwise difference inflates the apparent effect by roughly 2.4x through arity alone, and Morla et al. (2026) show earlier drafts of their own work reading that artifact as signal. The pilot also documents an 8 percent decision flip rate on pure resampling at default temperature, which bounds how small a harness effect can be credibly detected without pinning decoding.

> That comparison is wrong, and correcting it is the central methodological lesson of the pilot.
>
> Morla et al. (2026), p. 8

> But after the arity correction of Finding 1, every one of these values is below its own noise floor
>
> Morla et al. (2026), p. 9

> Scaffolding complexity is a first-class variable in AgentFairBench, reflecting BCF Proposition P3 (super-additivity) and the claim that agentic structure can amplify or attenuate bias introduced at any component.
>
> Morla et al. (2026), p. 5

### 74. Five Whys as an Epistemic-Honesty Scaffold for Multi-Agent LLM Analysis of Industrial Time Series

Ochi, Y., & Uchiyama, Y. (2026). Five Whys as an Epistemic-Honesty Scaffold for Multi-Agent LLM Analysis of Industrial Time Series. International Journal of Advanced Computer Science and Applications, 17(8). https://doi.org/10.14569/ijacsa.2026.0170803

*Rigour 0.71 · preprint*

A clean harness-isolation design: the same multi-agent system, seed and shared synthesis procedure are fixed and the single manipulated factor is whether a data-blind reviewer scaffold is present, with analysis depth equalised across arms specifically to remove trajectory length as a confound. Ochi and Uchiyama (2026) find a scaffold change flipping the system's headline output from a confident unverified root cause to an honest abstention with no change of model, tools or data. They also bound the effect by capability tier, since the strongest model reaches the honest verdict unaided. Against RQ2 the paper under-reports its own harness, explicitly withholding sampling parameters, context limits and retry behaviour.

> We treat the MAS architecture as fixed across all conditions; the only manipulated factor is the presence or absence of the reviewer.
>
> Ochi & Uchiyama (2026), p. 3

> the comparison is between an MAS that analyses to the same depth with and without the Five Whys discipline, not between a longer and a shorter run.
>
> Ochi & Uchiyama (2026), p. 4

> We report model identifiers, seeds, chain count, and round budget, and give the operator in Appendix A, but not full API-level configuration such as sampling parameters, context limits, and retry behaviour, on which LLM outputs can depend.
>
> Ochi & Uchiyama (2026), p. 8

### 75. The Observability Gap: Why Output-Level Human Feedback Fails for LLM Coding Agents

Wang, Y., & Wang, C. (2026). The Observability Gap: Why Output-Level Human Feedback Fails for LLM Coding Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2603.26942

*Rigour 0.62 · preprint*

A small case study in which the human feedback channel, not the model, is the binding constraint: instruction granularity varies across four groups while the loop architecture, tooling and model family are held fixed. Changing only that harness component moved the system from zero successes in ten runs to reliable convergence, with model competence explicitly ruled out because the agent rediscovered the reference utility functions in every arm. Wang and Wang (2026) name the mechanism failure mode oscillation. The arms are not matched in sample size and no statistical comparison is reported.

> This result strongly supports the interpretation that the key limitation was not an inability to write utility code, but the lack of access to the code-level information needed to diagnose visually ambiguous failures.
>
> Wang & Wang (2026), p. 3

> A persistent pattern across Groups A–C was failure mode oscillation: correcting one visible symptom repeatedly introduced a complementary failure, preventing convergence.
>
> Wang & Wang (2026), p. 3

> The findings are based on a single task domain (Blender scene generation), a single evaluator, and a single LLM family (Claude), so the severity and form of the observability gap may differ across domains, interfaces, and model classes.
>
> Wang & Wang (2026), p. 4

### 76. Hierarchical Online Prompt Mutation with Dual-Loop Feedback for Guardrailed Evidence Document Generation: A Production-Evaluation Case Study

Sundar, N. A., & Morabia, T. (2026). Hierarchical Online Prompt Mutation with Dual-Loop Feedback for Guardrailed Evidence Document Generation: A Production-Evaluation Case Study. arXiv preprint. http://arxiv.org/abs/2606.01472v1

*Rigour 0.79 · preprint*

A component-attribution design in production: the base model and the exact 600 cases are matched across seven variants and only the harness machinery changes, so exact paired tests are available. Sundar and Morabia (2026) report a monotone ladder from static prompting to a full dual-loop harness worth +11.0 points on count win rate and +19.1 points amount-weighted, with each feedback channel contributing separately. They label the design component attribution under matched production evaluation rather than randomised deployment lift. No model was varied, so the study bounds the harness effect without a model-effect comparator.

> The production ablation uses 600 matched cases shared across all variants. Each case preserves the same hashed case identifier and disputed amount across variants, so pairwise amount-difference bootstraps compare like with like.
>
> Sundar & Morabia (2026), p. 3

> It substantially strengthens component attribution because all variants are evaluated on the same 600 cases, but it cannot by itself prove live deployment lift under future traffic shifts.
>
> Sundar & Morabia (2026), p. 5

> The mean Likert score increases from 3.18 under static control to 4.40 under full dual-loop HOPM, while the issue-flag rate falls from 15.3% to 5.2%.
>
> Sundar & Morabia (2026), p. 5

### 77. Advancing LLM Agents for Code Generation: Observability, Orchestration, Reliable Performance

Kaplunovich, A. (2025). Advancing LLM Agents for Code Generation: Observability, Orchestration, Reliable Performance. 2025 International Conference on Intelligent Computing, Communication, Networking and Services (ICCNS), 108-116. https://doi.org/10.1109/iccns66249.2025.11428688

*Rigour 0.56 · peer-reviewed conference*

One of the few papers that treats the retry budget as a first-class experimental variable, reporting accuracy at each retry index from zero through six for every model pairing. The confound is then plain: one model leads at retry 0 but ends lower than a model that starts far behind and overtakes it, so a single-shot comparison of these models would invert the ranking a retry-enabled harness produces. Component assignment matters as much as model identity, with the same two models yielding 98 percent in one developer-evaluator order and 93 percent in the reverse. Kaplunovich (2025) reports no task counts, seeds or variance alongside the percentages, and the central architectural claim is asserted rather than measured.

> We achieved an accuracy of 98% after three retries, whereas using Llama3 - 2 - 11B - Instruct for both developm ent and validation resulted in only 92% accuracy.
>
> Kaplunovich (2025), p. 7

> Moreover, in the tandem of models the order ( tool) of model inference matters, because we only got 93% ac curacy when using claude - 3 - haiku for tool_developer and llama3 - 2 - 11b - instruct for tool_eval.
>
> Kaplunovich (2025), p. 7

> One important lesson we have learned – it is important to make sure the LLM follows certain workflow and if possible we need to control flow, iteration parameters, data exchang es, model arguments, and LLM prompts rather than relying on models to figure it our autonomously.
>
> Kaplunovich (2025), p. 8

### 78. OpenAI single-agent LLM architecture reduces computational overhead relative to multi-agent orchestration in a simulated mars rover decision-support benchmark

Sanabria, D. (2026). OpenAI single-agent LLM architecture reduces computational overhead relative to multi-agent orchestration in a simulated mars rover decision-support benchmark. Frontiers in Robotics and AI, 13, 1877762-1877762. https://doi.org/10.3389/frobt.2026.1877762

*Rigour 0.75 · peer-reviewed journal*

A topology comparison that reports a null honestly and names the harness confound itself. Both conditions share the same models, sanitised inputs, output schema and an explicit label-leakage control, yet Sanabria (2026) concedes that differences may reflect prompt design as well as architectural structure because the orchestration condition necessarily rewrites the prompts. After scenario-level pairing and multiplicity control almost none of the decision-quality advantage survives, while latency and token differences are enormous. The hazard over-identification result is harness-attributable: the aggregator-style orchestrator behaves like a union operator, which a critic or filter design would change.

> This documentation is important because the comparison evaluates prompt-defined agent architectures rather than independently trained expert models.
>
> Sanabria (2026), p. 5

> However, this pattern may reflect the specific orchestrator prompt design rather than an inherent limitation of all multi-agent architectures.
>
> Sanabria (2026), p. 14

> In the GPT-4o evaluation, the single-agent architecture achieved 0.810 decision accuracy, 0.081 exact hazard F1, and 0.131 semantic hazard F1. By comparison, GPT-4o multi-agent orchestration achieved 0.734 decision accuracy, 0.043 exact hazard F1, and 0.106 semantic hazard F1.
>
> Sanabria (2026), p. 9

### 79. A Comparative Empirical Evaluation of Single-Agent and Multi-Agent LLM Prompting Strategies for Automated Formative Feedback in Education

Lai, J., & Li, Z. (2026). A Comparative Empirical Evaluation of Single-Agent and Multi-Agent LLM Prompting Strategies for Automated Formative Feedback in Education. Journal of Intelligence and Engineering Technology, 1(2), 29-38. https://doi.org/10.70393/6a696574.343135

*Rigour 0.69 · peer-reviewed journal*

This study believes it is isolating architecture, and it does hold the model, decoding settings and rubric constant across four conditions. But the design confounds exactly the two things RQ1 separates, since moving up the ladder adds agent roles and simultaneously adds chain-of-thought, role-playing and rubric-guided prompting, so the reported single-agent versus multi-agent gap cannot be attributed to topology alone. Lai and Li (2026) report nothing about tool schemas, retry policy or orchestration failure handling. It is useful for RQ2 precisely as a case where authors believe the harness was held constant while the varied factor was a bundle of scaffold changes.

> These principles were embedded into the prompt templates for all four strategies, ensuring that observed quality differences could be attributed to architectural and prompting variations rather than inconsistencies in instructional framing.
>
> Lai & Li (2026), p. 3

> A one -way repeated -measures ANOVA confirmed a statistically significant main effect of prompting strategy on CQS, F(3, 597) = 47.32, p < 0.001, partial eta -squared = 0.19.
>
> Lai & Li (2026), p. 5

> The most striking finding is the monotonic decrease in error rates as architectural complexity increases.
>
> Lai & Li (2026), p. 6

### 80. WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration

Zhang, Y., Ma, Z., Ma, Y., Han, Z., Wu, Y., & Tresp, V. (2024). WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2408.15978

*Rigour 0.62 · preprint*

A system paper whose headline comparisons illustrate the confound rather than control for it: the reported relative gain over a concurrent tree-search method and the lead over a strong baseline are whole-stack comparisons in which orchestration, prompting strategy and demonstration budget all differ at once. Within its own architecture, however, Zhang et al. (2024) isolate two factors cleanly, with a model swap adding 6.6 to 11.8 points across domains, a model effect of similar magnitude to the reported architectural advantage, and component ablations showing removal of the planner dropping interaction success from 100 to 24 percent. The ablations run on a curated subset of already-solved tasks.

> However, transitioning from GPT-3.5 to GPT4o yields substantial gains, particularly in the Shopping, Reddit, and GitLab, with SR increases of 11.8%, 6.6%, and 9.4%, respectively.
>
> Zhang et al. (2024), p. 8

> Notably, on WebArena, WebPilot achieves SOTA performance with GPT-4, achieving a 93% relative increase in success rate over the concurrent tree search-based method.
>
> Zhang et al. (2024), p. 1

> First, the effectiveness of WebPilot is limited by the capabilities of LLMs, particularly in accurately understanding and interacting with complex web environments via text-based actions.
>
> Zhang et al. (2024), p. 9

### 81. AgentSwift: Efficient LLM Agent Design via Value-Guided Hierarchical Search

Li, Y., Li, L., Wu, Z., Liao, Q., HAO, J., Shao, K., & Xu, F. (2026). AgentSwift: Efficient LLM Agent Design via Value-Guided Hierarchical Search. Proceedings of the AAAI Conference on Artificial Intelligence, 40(38), 31843-31851. https://doi.org/10.1609/aaai.v40i38.40453

*Rigour 0.88 · peer-reviewed conference*

Not designed to answer RQ1, but a clean side-effect contribution: the entire search runs with the model held fixed, so every reported difference is harness-attributable. Under that fixed backbone, hand-crafted scaffolds on one benchmark span 0.336 to 0.587 and the searched scaffold reaches 0.806, a range wider than most reported model-generation gaps on the same task. Li et al. (2026) also quantify why such comparisons are rarely run properly, noting the dollar cost of evaluating a single agent configuration, which is a concrete mechanism behind the under-reporting RQ2 targets. The paper states no limitations and defers ablations and cost analysis to an unavailable appendix.

> Evaluated across a comprehensive set of seven benchmarks spanning embodied, math, web, tool, and game domains, AgentSwift discovers agents that achieve an average performance gain of 8.34% over both existing automated agent search methods and manually designed agents.
>
> Li et al. (2026), p. 1

> evaluating a single CoT agent in ALFWorld costs $60
>
> Li et al. (2026), p. 1

> Table 1: Performance comparison of our method against hand-crafted agents and agent search methods across seven diverse benchmarks using GPT-4o-mini.
>
> Li et al. (2026), p. 5

### 82. DREAMS: Density Functional Theory Based Research Engine for Agentic Materials Simulation

Wang, Z., Huang, H., Zhao, H., Xu, C., Zhu, S., Janßen, J., & Viswanathan, V. (2025). DREAMS: Density Functional Theory Based Research Engine for Agentic Materials Simulation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2507.14267

*Rigour 0.88 · preprint*

DREAMS contains an explicitly designed ablation in which the canvas, orchestration and backbone model are fixed and only a multi-tier safety guard varies, which the authors present as the one contrast in the paper that isolates a causal contribution. It produced no change in the headline number but a large change in process validity and cost, since the unguarded system reached a near-correct answer with only 81 percent of essential steps succeeding because systematic errors partially cancelled. That is the sharpest illustration here that an endpoint metric can be right for the wrong reason and therefore cannot support harness attribution. Wang et al. (2025) also state that their cross-framework comparisons confound several architectural differences at once.

> By contrast, the comparison between DREAMS and DREAMS_safe holds the canvas and orchestration fixed and directly evaluates the added effect and cost of the safety guard.
>
> Wang et al. (2025), p. 23

> Because the baseline systems differ from DREAMS in several respects simultaneously, comparisons with MDCrow and ChemGraph evaluate overall end-to-end behavior rather than isolate the causal contribution of any individual architectural choice.
>
> Wang et al. (2025), p. 23

> DREAMS_safe uses approximately 13x more input tokens than DREAMS for both benchmarks and 17x to 32x more output tokens.
>
> Wang et al. (2025), p. 25

### 83. BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML

Miller, H. E., Greenig, M., Tenmann, B., & Wang, B. (2025). BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML. bioRxiv (Cold Spring Harbor Laboratory). https://doi.org/10.1101/2025.09.01.673319

*Rigour 0.71 · preprint*

A benchmark paper whose headline finding is on-topic: no consistent advantage for domain-specialised agents over generalist ones, with architecture and scaffolding rather than domain specialisation appearing to be the primary drivers. It is equally useful as a cautionary case for RQ2, because each agent runs its own recommended LLM backend and Miller et al. (2025) name that confound in their own limitations. The ranking also flips depending on whether failed runs are scored as zero or excluded, and the failures are attributed to addressable scaffolding and execution faults rather than architectural limits. Compute is genuinely matched.

> While performance varies across agents, all agents on average underperform human baselines; moreover, we observe no consistent advantage for biomedical-specialized over generalist agents, suggesting that agent architecture and scaffolding may be the primary drivers of capability at present.
>
> Miller et al. (2025), p. 2

> First, the choice of LLMs for agents introduces potential confounds: stronger base LLMs may yield stronger agent performance.
>
> Miller et al. (2025), p. 6

> Importantly, these failure modes did not reflect fundamental architectural flaws but rather are likely addressable issues in scaffolding and execution.
>
> Miller et al. (2025), p. 5

### 84. LLM Agents Can Be Choice-Supportive Biased Evaluators: An Empirical Study

Zhuang, N., Cao, B., Yang, Y., Xu, J., Xu, M., Wang, Y., & Liu, Q. (2025). LLM Agents Can Be Choice-Supportive Biased Evaluators: An Empirical Study. Proceedings of the AAAI Conference on Artificial Intelligence, 39(25), 26436-26444. https://doi.org/10.1609/aaai.v39i25.34843

*Rigour 0.88 · peer-reviewed conference*

Only indirectly about harnesses, but it supplies a sharp prompt-sensitivity result: changing two words in an evaluator's system prompt increased the chosen-option bias and roughly tripled the F statistic with everything else held constant. Since the phrasing of an evaluator prompt is a harness-level authoring decision rather than a model property, Zhuang et al. (2025) provide evidence that prompt wording inside the scaffold is an attributable source of measured behavioural difference, and they warn that in multi-agent or iterative settings the bias could compound through the chain. No harness variants are compared, so the paper contributes nothing directly to RQ2, and its own judge calibration is weaker than the other judge-based papers here.

> The chosen option’s mean score increases to 3.50 (SE: 0.62), while the rejected option’s score decreases to -2.3 (SE: 0.91).
>
> Zhuang et al. (2025), p. 6

### 85. Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures

Shah, J. (2026). Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures. arXiv preprint. https://doi.org/10.48550/arxiv.2606.08275

*Rigour 0.71 · preprint*

Shah (2026) supplies the methodological machinery RQ1 needs, treating an agent run as a structural causal model and attributing outcome change to a specific step by intervening on it while holding the rest of the run at factual values. The five interventions map onto harness components, so the same algebra could attribute an outcome difference to scaffold versus model. Two findings matter for confounding: provider nondeterminism means a faithful replay cannot be assumed even at temperature 0, and resampling one step re-rolls every downstream stochastic step, so an irrelevant early step can appear causally influential. Validation is on synthetic causal models rather than real agent workloads.

> Providers are not deterministic. Even at temperature0, hosted inference varies because of floating-point non-associativity and batch-size-dependent kernels [11]; and current frontier models may not accept a temperature parameter at all.
>
> Shah (2026), p. 2

> Magnitude alone cannot localize the cause.
>
> Shah (2026), p. 3

> The contrastive effect is a total effect through a stochastic continuation; isolating a step's direct effect calls for common random numbers across branches, which is hard across divergent LLM contexts and is left as a refinement.
>
> Shah (2026), p. 5

### 86. Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight

Purwar, A., Singh, S., & Srivastava, K. (2026). Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight. arXiv preprint. http://arxiv.org/abs/2608.24314v1

*Rigour 0.71 · preprint*

The design tests whether automated judgments are sensitive to the evaluation setup by scoring the same interactions under three configurations and two judge models with identical rubrics. Purwar et al. (2026) report a partial dissociation: changing the evaluator model or prompting configuration has minimal impact on the direction and relative ordering of metric scores but a large, domain-dependent impact on absolute calibration. A study reporting absolute LLM-judge scores is therefore reporting a quantity that moves with the evaluation harness, while rank-order comparisons are more robust. The agent-side harness is only partly controlled, since two of the three configurations change what context the agent receives.

> The same interactions are scored under three evaluation configurations, p0, p1, and p2, to test whether automated judgments are sensitive to the evaluation setup and whether observed patterns generalize across configurations and judge models.
>
> Purwar et al. (2026), p. 1

> The results indicate that changes in evaluator model or prompting strategy have minimal impact on overall metric behavior, with the primary difference lying in score calibration rather than evaluation direction.
>
> Purwar et al. (2026), p. 4

> Neither GPT-4.1 nor GPT-5 consistently leads the other in agreement with human judgment. Instead, alignment shifts by metric.
>
> Purwar et al. (2026), p. 5

### 87. First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope

Inguglia, G. (2026). First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope. arXiv preprint. https://doi.org/10.48550/arxiv.2605.28916

*Rigour 0.54 · preprint*

A textbook RQ2 negative case: the specification, data, hardware and task are matched exactly, but the two compared units are whole commercial agent products bundling a harness and a model stack, and Inguglia (2026) states in the limitations that the two agents used different underlying models for one pipeline step. What makes the paper useful anyway is that the differences it does isolate are harness-level: a 4.7x runtime gap attributed primarily to restart policy rather than intrinsic computation, and a proceed-and-correct versus diagnose-and-restart error-handling philosophy that produced silent specification deviations in one system and logged self-corrections in the other. A second run produced a genuine scientific divergence from a single ambiguous instruction.

> Both agents received identical written specifications and identical compute resources.
>
> Inguglia (2026), p. 1

> The 4.7× runtime difference (15.92/3.38) is attributable primarily to these restarts rather than to intrinsic computational differences.
>
> Inguglia (2026), p. 6

### 88. BATITONG: Deterministic Reliability for LLM-Driven Offensive-Security Orchestration

Wahid, A. R. (2026). BATITONG: Deterministic Reliability for LLM-Driven Offensive-Security Orchestration. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21759172

*Rigour 0.56 · preprint*

Wahid (2026) asks how much of an offensive-security system's reliability comes from the model versus the architecture around it, and answers by running the pipeline on free-tier models and measuring what a deterministic verification layer adds. Because every finding stores both the pre-gate claim and the post-gate result, a within-run counterfactual is available for one harness component with model, targets, tools and traces fixed by construction. The measured contribution is real but modest and one-directional. The authors are explicit that the other five scaffold mechanisms are only pre-registered for ablation, not measured, and that no paid-model or no-scaffold arm was run.

> The gate lowered 28 findings (D = 28/416 = 6.7%), all confirmed→suspected (Fig. 6), each for a missing reproducible request/response pair.
>
> Wahid (2026), p. 7

> A substantial part of the machinery for a trustworthy LLM-driven offensive-security assessment can be supplied by architecture rather than by an expensive model.
>
> Wahid (2026), p. 8

> (i) Observational, single-deployment evidence; the verifier magnitude across independent settings is unestablished. (ii) No controlled ablation yet for the five non-verifier mechanisms.
>
> Wahid (2026), p. 8

### 89. Process-Aware LLM-Agent Scaffolds for Metric-Based Microservice Root-Cause Analysis with Evidence-Trace Scoring

Liao, M. (2025). Process-Aware LLM-Agent Scaffolds for Metric-Based Microservice Root-Cause Analysis with Evidence-Trace Scoring. Stout in Computer Science and Technology Studies, 1(1), 48-61. https://doi.org/10.61424/zngee941

*Rigour 0.62 · peer-reviewed journal*

Despite its title this paper evaluates a deterministic scaffold and its audit record rather than any language model, which the author states outright. It contributes a separability result: swapping the evidence policy changed the evidence-trace score from 0.653 to 0.893 while leaving every top-one prediction unchanged, so grounding and accuracy are independent axes and an outcome-only metric is blind to the difference. Liao (2025) also shows the proposed scaffold is statistically indistinguishable from a plain tree ensemble on accuracy. As RQ2 evidence it is weak, since no LLM harness is held constant because no LLM is used, and residual leakage limits how much of the accuracy is attributable to the design.

> Evidence policy changed audit quality without changing labels.
>
> Liao (2025), p. 9

> The experiment evaluated the scaffold and record rather than named generative LLMs.
>
> Liao (2025), p. 12

> The model was strongly underconfident, so raw probabilities should not be treated as incident risk estimates.
>
> Liao (2025), p. 11

### 90. RE-Bench Is a Systems Benchmark: What Its Scorers and Selection Rules Actually Support

Buldurgan, H. (2026). RE-Bench Is a Systems Benchmark: What Its Scorers and Selection Rules Actually Support. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22089194

*Rigour 0.62 · preprint*

A source-contract audit rather than an experiment, and its whole argument is the RQ1 argument: a benchmark number belongs to a versioned model-plus-scaffold-plus-protocol system, not to a base model. Buldurgan (2026) makes the confound concrete by naming the components that travel with the score, including scaffold, prompt and context policy, tools, hardware, feedback, time budget, attempt allocation and the selection rule, and shows that within-run aggregation and across-run selection are separate harness layers that can move a headline number without any change in per-run quality. It supplies a minimum reporting set but no effect size, and the record is AI-assisted and not independently adjudicated.

> A model-scaffold-protocol result is therefore not a scaffold-free property of the model.
>
> Buldurgan (2026), p. 4

> Changing the scaffold changes candidate generation, context retention, tool use, score-query frequency, and selection.
>
> Buldurgan (2026), p. 4

> These findings do not invalidate the paper's historical results. They show that scorer design, source provenance, repeated attempts, and selection rules are part of the capability claim.
>
> Buldurgan (2026), p. 2

### 91. The Necessity of a Unified Framework for LLM-Based Agent Evaluation

Zhu, P., Sun, L., Yu, P. S., & Su, S. (2026). The Necessity of a Unified Framework for LLM-Based Agent Evaluation. arXiv preprint. https://arxiv.org/abs/2602.03238

*Rigour 0.54 · preprint*

The methodological backbone for RQ2. Zhu et al. (2026) argue that whether the harness must be held constant is not a universal rule but a function of the declared candidate boundary, so fixing the scaffold is required for model-level claims, optional for agent-system claims and deliberately relaxed for robustness claims. They enumerate exactly the components RQ1 names, treating prompt scaffolding, planning strategy, memory serialization and compaction, tool-schema translation, and parsing and retry or repair policy as factors that must be fixed or semantically matched before any difference is attributed to the model. Their most consequential caveat is that a fixed reference harness yields only a conditional capability estimate. The paper is deliberately agnostic on which variance term dominates.

> LLM agent benchmark scores are shaped not only by the model but also by the agent harness, environment, evaluator, and inference budget.
>
> Zhu et al. (2026), p. 1

> Small differences in this stack can redirect subsequent actions and observations, altering both absolute scores and model rankings
>
> Zhu et al. (2026), p. 1

> A reference harness is not neutral and may interact differently with different model families.
>
> Zhu et al. (2026), p. 9

### 92. Code as Agent Harness

Ning, X., Tieu, K., Fu, D., Wei, T., Li, Z., Bei, Y., Zou, J., Ai, M., Liu, Z., Li, T.-W., Chen, L., Zhao, Y., Yang, K., Li, B., Qian, C., Li, G., Lin, X., Zeng, Z., Qiu, R., ... He, J. (2026). Code as Agent Harness. arXiv preprint. http://arxiv.org/abs/2605.18747v1

*Rigour 0.58 · preprint*

A large survey that reframes code as the operational substrate of the harness, and whose treatment of measurement is a direct statement of the confound: once an LLM is embedded in a code-agent harness, performance depends on which files are retrieved, which tools are exposed, how many retries are allowed, whether tests can be executed, how failures are summarised and what verifier decides success. Ning et al. (2026) propose six harness-level metric dimensions as a complement to accuracy and identify oracle adequacy as the central bottleneck. They also warn specifically that reported planning gains may not survive once execution environments, feedback quality, tool access and trajectory budgets are accounted for. No new experiments are reported.

> In this setting, performance is no longer determined by the base model alone, but also by the surrounding runtime: which repository files are retrieved, which tools are exposed, how many retries are allowed, whether the agent can execute tests, how failures are summarized, and what verifier decides success.
>
> Ning et al. (2026), p. 62

> Such metrics conflate the capabilities of the base model, the quality of the harness, the reliability of tools, the informativeness of feedback, and the difficulty of the environment.
>
> Ning et al. (2026), p. 62

> Many current conclusions about the benefits of planning depend heavily on the surrounding execution conditions, including execution environments, feedback quality, tool access, trajectory budgets, and whether the benchmark truly stresses long-range dependency management rather than localized patch generation.
>
> Ning et al. (2026), p. 21

### 93. Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems

Barbaste, P., Darrigol, T., Vu, G., & Wiltberger, T. (2026). Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2609.00006

*Rigour 0.58 · preprint*

The most detailed available description of what the harness variable actually contains, decomposing eleven production coding harnesses into seven subsystems with per-system minimal and maximal implementations, which lets the harness be treated as a structured set of factors rather than an undifferentiated confounder. The first observation is the central claim in qualitative form: systems spanning three orders of magnitude in code size target similar tasks, yet loop sophistication does not predict benchmark performance. Barbaste et al. (2026) are explicit that they do not resolve attribution quantitatively and name a cross-system controlled run study as future work. They also document a reproducibility hazard, since inventory-level claims about the harness layer decay within a quarter.

> The eleven systems span three orders of magnitude in code size while targeting similar tasks, yet loop sophistication does not predict benchmark performance.
>
> Barbaste et al. (2026), p. 12

> Whether the production scaffolding produces measurable improvements on the same benchmark under matched conditions is an open question that this study does not answer
>
> Barbaste et al. (2026), p. 58

> The analysis rests on source-code reading, not runtime measurement.
>
> Barbaste et al. (2026), p. 66

### 94. Inside the scaffold: A source-code taxonomy of coding agent architectures

Rombaut, B. (2026). Inside the scaffold: A source-code taxonomy of coding agent architectures. arXiv preprint. https://arxiv.org/abs/2604.03515

*Rigour 0.54 · preprint*

Rombaut (2026) names the confound in the language the review needs and documents the concrete mechanism by which prior work fails, citing trajectory studies that compared agents built on different backbones and so made scaffold and model effects inseparable. The most useful contribution for RQ2 is a refusal: the author declines to benchmark on the stated grounds that cross-agent results are not comparable when the underlying models differ, and instead supplies the variable list a controlled experiment would need, proposing identical tool sets with different loop strategies or identical loops with different compaction strategies at a fixed model. A single-author analysis with LLM-assisted code navigation and self-verification.

> First, without a shared vocabulary for scaffold design, researchers studying agent behavior cannot attribute observed differences to specific architectural choices; the confound between scaffold design and model capability goes unacknowledged.
>
> Rombaut (2026), p. 2

> As noted in Section 3.5, SWE-bench comparisons between agents confound scaffold design, model choice, and configuration in a single metric.
>
> Rombaut (2026), p. 32

> finding that prompt interventions that add or remove testing change outcomes by at most 2.6 percentage points
>
> Rombaut (2026), p. 6

### 95. Harness Engineering for Agentic AI Coding Tools: An Exploratory Study

Galster, M., Mohsenimofidi, S., Lulla, J. L., Abubakar, M. A., Treude, C., & Baltes, S. (2026). Harness Engineering for Agentic AI Coding Tools: An Exploratory Study. arXiv preprint. http://arxiv.org/abs/2602.14690v5

*Rigour 0.83 · preprint*

Supplies the definitional and empirical grounding for what a harness is, distinguishing the context supplied to a single model call from the software layers that assemble that context, expose tool schemas and manage turn-by-turn state. Galster et al. (2026) map eight repository-level configuration mechanisms across five agentic coding tools over 2,853 repositories and show that harness configuration in open source is overwhelmingly static context files, with skills, subagents, hooks and MCP each adopted by under 20 percent of repositories per tool. The contribution is descriptive rather than causal, and the authors explicitly flag the absence of controlled evidence about whether deeper configuration improves outcomes.

> The emerging termharness engineeringextends context engineering, broadening the focus from a model’s context to the full set of mechanisms configured around it.
>
> Galster et al. (2026), p. 1

> Harness engineering in open source today is therefore mostly context engineering.
>
> Galster et al. (2026), p. 9

> Future work should assess whether deeper configuration leads to measurable performance gains, extending early evidence on the impact ofContext Files[ 16].
>
> Galster et al. (2026), p. 9

### 96. Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime

He, C., Zhou, X., Wang, D., Xu, H., Liu, W., & Miao, C. (2026). Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime. Preprints.org. https://doi.org/10.20944/preprints202603.1756.v1

*Rigour 0.62 · preprint*

A position paper that states the thesis explicitly and, unusually, concedes it supplies no causal evidence for it. He et al. (2026) argue that the experimental unit in agent research is the coupled execution regime, so matching model family while changing tool access, retry budgets, verifier strictness or escalation policy is not a controlled comparison. For RQ2 they name the specific failure of practice, that retry budgets, hidden human escalations, tool filters, repository instructions and grader prompts routinely stay implicit even when load-bearing, and they propose a disclosure artifact and layer-aware baselines that vary one layer at a time. The only original data is a small visibility audit of 40 works.

> In agent settings, the experimental unit is the coupled execution regime.
>
> He et al. (2026), p. 8

> A language-agent paper can appear more novel than it really is if the harness is under-described.
>
> He et al. (2026), p. 8

> In real systems the two are often entangled: a stronger model may need less scaffolding, while a stronger harness can make a weaker model look far more capable.
>
> He et al. (2026), p. 12

### 97. Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

Zhou, C., Chai, H., Chen, W., Guo, Z., Shan, R., Song, Y., Xu, T., Yang, Y., Yu, A., Zhang, W., Zheng, C., Zhu, J., Zheng, Z., Zhang, Z., Lou, X., Zhang, C., Fu, Z., Wang, J., Liu, W., ... Zhang, W. (2026). Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering. arXiv preprint. http://arxiv.org/abs/2604.08224v1

*Rigour 0.50 · preprint*

A conceptual survey whose value is that it names the attribution problem rather than measuring it: many of the largest reliability gains come from changing the environment around the model rather than the model, and current evaluation cannot distinguish the two because a harness improvement surfaces only as a higher pass rate. Zhou et al. (2026) propose ablation studies that remove individual harness components, cross-model transfer tests that hold the harness constant while varying the base model, and long-horizon reliability metrics. No new empirical results are reported, so it functions as framing and taxonomy rather than evidence.

> Many of the largest gains in reliability do not come from changing the base model at all. They come from changing the environment around the model: adding persistent memory, organizing reusable skills, standardizing tool interfaces, constraining execution, instrumenting behavior, and routing work through explicit control logic
>
> Zhou et al. (2026), p. 5

> A harness that improves reliability through better memory retrieval, more precise skill loading, or tighter execution governance will show up only as a higher pass rate, with no way to attribute the gain to its actual source.
>
> Zhou et al. (2026), p. 43

> Concrete evaluation strategies might include ablation studies that remove individual harness components and measure the resulting degradation; cross-model transfer tests that hold the harness constant while varying the base model; and long-horizon reliability metrics that track success rates, cost, and drift over extended multi-session interactions rather than single-turn completions.
>
> Zhou et al. (2026), p. 43

### 98. Agent harness for large language model agents: A survey

Meng, Q., Wang, Y., Chen, L., Li, Y., Wu, W., Jiang, W., Wang, Q., Lu, C., Gao, Y., Wu, Y., & Hu, Y. (2026). Agent harness for large language model agents: A survey. Preprints.org. https://doi.org/10.20944/preprints202604.0428.v1

*Rigour 0.54 · preprint*

The closest thing in the corpus to a literature-level statement of RQ1, decomposing evaluation unreliability into environment drift, task-specification ambiguity and harness coupling, and framing the last as a measurement-validity problem in which reported performance is a property of the agent-harness-environment triplet while evaluation infrastructure implicitly assumes the harness is neutral. For RQ2 the actionable contribution is a requirement that every published evaluation report the full harness configuration alongside model and task specifications. Meng et al. (2026) run no experiments of their own, and several of their most quotable figures come from unreviewed preprints that they explicitly flag as requiring corroboration, so the survey is used here for framing rather than magnitude.

> Harness coupling is a measurement validity problem. The measured performance is a property of the (agent, harness, environment) triplet, not of the agent alone—yet evaluation infrastructure implicitly assumes that the harness is neutral.
>
> Meng et al. (2026), p. 53

> Every published evaluation result should report the complete harness configuration alongside model and task specifications
>
> Meng et al. (2026), p. 53

> harness coupling affects all benchmarks, because the measured performance is a property of the (agent, harness, environment) triplet rather than of the agent alone.
>
> Meng et al. (2026), p. 52

### 99. Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents

Albayaydh, W., Zhao, R., & Flechais, I. (2026). Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents. arXiv preprint. https://arxiv.org/abs/2607.05775

*Rigour 0.54 · preprint*

A narrative synthesis whose cross-cutting pattern of uneven returns to additional scaffolding states directly that adding more agents, tools, reasoning effort or context does not uniformly improve reliability and can reduce it. Albayaydh et al. (2026) also document the reverse direction, compiling a case in which bolting external verifiers and critics onto a planning benchmark moves success from 0.6 percent to about 65 percent with no change to the underlying task. Their measurement-validity cluster supplies useful RQ2 framing, arguing that part of the apparent year-over-year improvement in agent scores reflects tightening of evaluation methodology rather than capability gain alone. It is explicitly a narrative rather than systematic review with no pre-registered protocol and no primary measurement.

> Adding more agents, more tools, more reasoning effort, or more context does not uniformly improve reliability, and can sometimes reduce it.
>
> Albayaydh et al. (2026), p. 12

> Agents that correctly execute the large majority of individual tool calls, or that satisfy most individual planning constraints, frequently fail the composed task as a whole.
>
> Albayaydh et al. (2026), p. 12

> Taken together, these findings suggest that at least part of the apparent year -over-year improvement in agent benchmark scores reflects tightening of evaluation methodology and correction of earlier measurement error, alongside a genuine rise in underlying capability, rather than one or the other in isolation.
>
> Albayaydh et al. (2026), p. 9

### 100. Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture

Xia, B., Lu, Q., Zhu, L., Xing, Z., Zhao, D., & Zhang, H. (2024). Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2411.13768

*Rigour 0.75 · preprint*

A corpus-level argument rather than a controlled experiment: across 134 academic sources Xia et al. (2024) find two thirds evaluating at the model level and only about 12 percent evaluating models and systems jointly, and argue that isolating prompts and responses hides orchestration, tool behaviour, dependencies and error propagation. Because 97.76 percent of academic sources use static suites and 92.54 percent report only end-to-end aggregates, the corpus provides indirect evidence that most published agent comparisons lack the intermediate instrumentation needed to attribute a difference to harness versus model. The paper names the evaluation harness as an engineering lever tunable independently of weights, but reports no comparative performance numbers of its own.

> Testing prompts and responses in isolation does not capture orchestration effects, tool behaviour, external dependencies, or error propagation across steps, so models that score well in isolation may still underperform once embedded in workflows.
>
> Xia et al. (2024), p. 10

> As shown in Fig. 4, academic sources primarily evaluate at the model level (89/134, 66.42%), with fewer at the system level (29/134, 21.64%) and a smaller share using integrated evaluations (16/134, 11.94%).
>
> Xia et al. (2024), p. 9

> This treats the evaluation harness itself as an engineering lever during development time and sits at the system or pipeline level, because it modifies interfaces, curricula, and guardrails around the model rather than only tuning the weights.
>
> Xia et al. (2024), p. 4

### 101. From Agent Loops to Structured Graphs: A Scheduler-Theoretic Framework for LLM Agent Execution

Wei, H. (2026). From Agent Loops to Structured Graphs: A Scheduler-Theoretic Framework for LLM Agent Execution. arXiv preprint. https://arxiv.org/abs/2604.11378

*Rigour 0.50 · preprint*

A design proposal rather than a study, but it contributes the most explicit attribution protocol in the corpus: a seven-group ladder in which each adjacent pair isolates exactly one harness factor, with the task set, base model, decoding parameters, tool set, timeout and token budget held constant across all groups and a control group included specifically so that improvements attributed to graph structure cannot be confused with the benefit of richer task information. Wei (2026) acknowledges that the additive decomposition may conflate an interaction term. None of it has been run, and the author states repeatedly that the predictions are not empirically validated, so it is a source for method design rather than effect sizes.

> Note: This section describes the design of an experimental protocol, not completed experimental results. We present this framework to (1) make our design choices falsifiable and (2) provide a rigorous protocol for future empirical evaluation.
>
> Wei (2026), p. 29

> The most significant limitation is the lack of experimental validation.
>
> Wei (2026), p. 35

### 102. Affordance-Compiled Intelligence: Observable-Only Cognitive Impedance Matching for No-Meta LLM-Integrated Systems

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-T., Rocktäschel, T., Riedel, S., & Kiela, D. (2026). Affordance-Compiled Intelligence: Observable-Only Cognitive Impedance Matching for No-Meta LLM-Integrated Systems. arXiv (Cornell University). https://doi.org/10.5281/zenodo.20116149

*Rigour 0.50 · preprint*

A formal theory paper that treats the attribution question as its central object, defining world-side capability amplification and then building machinery to certify it without a privileged evaluator. Its most directly useful contribution is a specification of what holding the harness constant actually requires: model weights, system prompts outside the controlled view, decoding parameters, tool-call syntax, context limits, randomness policy and service commitments must be identical or replay-equivalent across arms, and anything unmonitored becomes declared debt. It also formalises a condition preventing a candidate harness from defining its own success criterion. No empirical study is reported, the worked instantiations carry hypothetical numbers, and the ledger record for this item carries a metadata problem in its author list.

> model weights, system prompts outside the compiler-controlled view, decoding parameters, tool-call syntax, context limits, randomness policy, and service commitments are identical or replay-equivalent across baseline and candidate trials.
>
> Lewis et al. (2026), p. 10

> These systems suggest a general phenomenon: a fixed model-policy's realized capability is strongly affected by the form in which the world is presented to it.
>
> Lewis et al. (2026), p. 5

> A model's unobserved competence is not identical to a system's target-channel capability. Poorly surfaced worlds produce unrecorded dependencies, ambiguous handles, delayed validation, irreversible errors, and context overload. A better compiled world can reduce these obstacles without changing model weights or the fixed model-policy.
>
> Lewis et al. (2026), p. 67

### 103. mABC: multi-Agent Blockchain-Inspired Collaboration for root cause analysis in micro-services architecture

Zhang, W., Guo, H., Yang, J., Tian, Z., Zhang, Y., Yan, C., Li, Z., Li, T., Shi, X., Zheng, L., & Zhang, B. (2024). mABC: multi-Agent Blockchain-Inspired Collaboration for root cause analysis in micro-services architecture. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2404.12135

*Rigour 0.50 · preprint*

A topology-comparison paper whose ablation is partially harness-controlled: with the backbone pinned, removing multi-agent decomposition, the workflow layer and the voting layer in turn shows collapsing to a single agent causing the largest drop. The harness is not held constant against the external baselines, since the proposed system bundles a structured seven-role workflow, a step cap, tool access and a re-answer retry loop while the baseline has none of these. The paper also swaps the base LLM under a fixed framework, and that spread is smaller than the ablation spread. One reporting caution, and a reason not to rest any conclusion on this source: the narrative in Section 3.5 cites an average score and a baseline range that do not correspond to any values in the paper's own results table.

> Removing Agent Workflow significantly reduces performance, indicating its crucial role. Limiting the framework to a Single Agent results in the lowest scores, severely diminishing its capability for AIOps tasks.
>
> Zhang et al. (2024), p. 8

> However, our proposed MABC significantly outperformed all the baseline models and ReAct with GPT-4-Turbo, achieving an impressive average score of 64.9.
>
> Zhang et al. (2024), p. 7

> MABC faces challenges in complexity and scalability as the number of agents and alert events increase, leading to higher computational overhead and longer processing times
>
> Zhang et al. (2024), p. 9

### 104. Harness Resilience: From LLM Availability to Toolchain Continuity in Agentic AI Engineering

Cheung, J. (2026). Harness Resilience: From LLM Availability to Toolchain Continuity in Agentic AI Engineering. https://doi.org/10.33774/coe-2026-4f53g

*Rigour 0.46 · preprint*

A definitional and vocabulary contribution rather than a measurement. Cheung (2026) draws an operational boundary between model, harness and application, and offers four concrete tests for whether a component is harness-critical, which is usable as a coding scheme for classifying what counts as a harness change in other studies. A minimum provenance trace schema requires model and harness version, feature flags, prompt-policy version and context-compression module to be recorded before every model call. No empirical estimate of harness attribution is supplied: the only numbers in the paper are explicitly labelled a synthetic example, and at rigour 0.46 it carries no evidential weight in this review.

> The practical unit of dependency is no longer “the model” but the model-harness combination.
>
> Cheung (2026), p. 1

> This paper is primarily a position paper and practice framework. It does not yet report a controlled empirical study, multi-organization case evidence, or statistically powered comparison of harnesses.
>
> Cheung (2026), p. 12

> Increasingly, productivity depends on an execution harness: the surrounding runtime of prompts, tools, sandboxes, permissions, memory, repositories, connectors, model-routing policies, observability, and user-interface affordances that turn a model into an operational coding or general-purpose agent.
>
> Cheung (2026), p. 1

### 105. A MODULAR BENCHMARKING FRAMEWORK FOR EVALUATING LLM-BASED AGENT APPLICATIONS

Perikala, K. (2026). A MODULAR BENCHMARKING FRAMEWORK FOR EVALUATING LLM-BASED AGENT APPLICATIONS. INTERNATIONAL JOURNAL OF RESEARCH IN COMPUTER APPLICATIONS AND INFORMATION TECHNOLOGY, 9(1), 1-14. https://doi.org/10.34218/ijrcait_09_01_001

*Rigour 0.44 · peer-reviewed journal*

States the problem crisply and then proposes trace-first, component-decoupled benchmarking as the remedy, nominally holding dataset, judge configuration, retrieval settings and decoding parameters fixed while varying one factor per experiment. In practice the control is only partial, since the three compared variants differ simultaneously in orchestration, tool access and number of retrieval calls, and no model is reported at all. The evidential weight is low: no dataset identity, no sample sizes, no variance, no statistics, only anonymised ordinal rubric scores produced by an LLM judge whose systematic biases Perikala (2026) flags as unmitigated. The publishing venue advertises an implausible impact factor, which should be weighed alongside the rigour score of 0.44.

> In addition, agent performance is often tightly coupled to implementation details, including prompt structure, tool schemas, and orchestration logic, obscuring the relative contributions of models versus agents.
>
> Perikala (2026), p. 5

> We evaluate agent applications under a controlled benchmark configuration by holding the dataset and judge settings fixed while varying a single factor per experiment.
>
> Perikala (2026), p. 12

> Across variants, retrieval relevance remains strong, but agent strategy determines whether evidence is used effectively.
>
> Perikala (2026), p. 13

### 106. Agent harness engineering: A survey

Li, J., Wu, Y., & Chang, Y. (2026). Agent harness engineering: A survey. Preprints.org. https://doi.org/10.20944/preprints202606.2203.v1

*Rigour 0.38 · preprint*

The most direct conceptual framing of RQ1 in the corpus and, at rigour 0.38, the weakest source in it. Li et al. (2026) define the harness as a system-level execution structure independent of model weights and argue it is a performance lever orthogonal to model capability, and their strongest quantitative support is second-hand, a cited industry report in which harness-only changes moved one coding model from roughly rank 30 to rank 5 on a public leaderboard. For RQ2 the paper is a negative finding about current practice, stating that end-to-end success metrics conflate base-model ability with harness support. It runs no experiments, so it is used here only for framing and vocabulary and carries none of the review's conclusions.

> Holding the foundation model fixed, changes to the harness can substantially alter end-to-end performance, making the harness a performance lever orthogonal to model capability [17,18].
>
> Li et al. (2026), p. 3

> End-to-end success metrics conflate base-model ability and harness support.
>
> Li et al. (2026), p. 31

> For example, LangChain reports that harness-level changes such as prompts and middleware hooks moved the same coding model from roughly the top 30 to the top 5 on Terminal-Bench 2.0, with a score increase from 52.8 to 66.5 [76].
>
> Li et al. (2026), p. 7

---

## 5. Evidence gaps

### 5.1 Eleven core papers whose full text could not be retrieved

Eleven records were screened *core* from their abstracts but could not be retrieved with the available institutional session. They were recorded as an explicit gap rather than relabelled to let the stopping rule pass, which means the saturation verdict in Section 2.3 holds over 106 read papers with eleven known holes in it. All eleven are cited from their abstracts only and none contributes evidence, quotations or effect sizes to Section 3.

Four of them look, from their abstracts, as though they would have borne directly on RQ1. Kinjo and Yamamoto (2026) describe an ablation-driven redesign of the schema documentation supplied to a model at query time — a tool-schema manipulation with the model held fixed, which is the exact design this review is short of. Zhang and Wang (2026) apply an explicit harness strategy to agent interfaces in a materials-science case study. Banjade (2026) constrains an LLM planner with an explicit schema and a restricted tool registry, again a tool-schema intervention. Palmer (2026) is a software deposit accompanying a preprint whose stated claim — that repository-scale agent reasoning is bound by state architecture rather than context — is a harness-attribution claim, and the deposit itself contains the experimental harness.

Three would have borne on RQ2. Li and Storhaug (2026) address missing information in agent evaluation design descriptions, which is the disclosure question of Section 3.3. Balusu (2026) reports that five agent orchestration phases have no span-level representation in current observability conventions, which is the instrumentation prerequisite for component-level attribution. AUDEBEAU (2025) is a structured peer review of a code-retrieval study in coding agents.

The remaining four are peripheral: Sarkar (2026) is a structured review of agentic architectures and evaluation practice; Mahdi (2026) proposes an architectural vocabulary for goal-directed agent systems; Yan and Yang (2025) reports schema-preserving generation with iterative debugging in a clinical setting; and Kuligin et al. (2025) studies the interaction of prompting technique and foundational model choice on medical question answering, which is a prompt-by-model factorial in a domain outside this review's centre.

### 5.2 The corpus is bounded by retrieval, not by eligibility

Of 364 core and supporting reports sought, 258 could not be retrieved. No report was excluded on eligibility grounds after full-text assessment, which means the boundary of this corpus is a retrieval boundary. In addition, 247 supporting and 179 context records were never read at all. Any claim in Section 3 about the *distribution* of practice across the literature — as opposed to claims about what the read papers report — inherits that limit.

### 5.3 The corpus is preprint-heavy, and the harness-specific work is the newest part of it

Eighty-four of the 106 read papers are preprints, and only 22 carry a non-preprint work type, several of those being self-deposited archive records rather than refereed proceedings. The protocol registered a specific worry on this point: the landscape scan that produced this topic was led by preprint servers, and the review was run partly to determine whether archival anchors exist outside that scan's narrow query.

They do. The corpus contains refereed work at ACL, two AAAI proceedings, ACM SIGKDD, the Proceedings of the ACM on Software Engineering, IEEE Access, IEEE/ACM IWQoS, Lecture Notes in Computer Science, EuroMLSys, HICSS, Frontiers in Robotics and AI and The Knowledge Engineering Review, including three of the four papers at rigour 1.00. What those archival papers do *not* provide is the harness-versus-model decomposition itself. Every study that measures the harness term directly — the 3x3 factorial, the 6x8 factorial, the 35-release study, the scaffold-effect study, the disclosure audits — is a 2026 preprint. The refereed anchors exist for the surrounding questions; the central question is currently answered only by unrefereed work.

### 5.4 What no study in this corpus did

- **No crossed factorial at scale with reported variance components.** The largest factorial crosses six harnesses with eight models but explicitly disclaims causal decomposition of individual mechanisms (entry 2). The only study that reports variance components runs a 3x3 grid with two runs per cell (entry 1). Nothing in between exists: no design with many harnesses, many models, repeated runs and a published decomposition.
- **Almost no reported noise floors.** Two papers estimate one — roughly ±4.75 pair-score points on a frozen commit (entry 7) and an 8 percent decision flip rate on pure resampling (entry 73). Every other effect size in this corpus is reported against an unmeasured baseline of run-to-run variation, and the scoping review in entry 17 shows why: seeds and run counts are essentially never published.
- **One harness-transfer check.** Exactly one study suspected its behavioural findings might be artifacts of its harness and re-ran the protocol on an independent harness (entry 35). No other paper tests whether its own harness-conditioned result survives a harness change.
- **Component-level ablation is rare and, where it exists, deflationary.** The corpus contains many whole-stack swaps and few single-component isolations. Where a single component is isolated, the effect shrinks and its interval often crosses zero (entry 25), or the manipulation moves the failure mode without moving the outcome (entry 69), or the outcome does not move at all (entry 82).
- **No cost-normalized comparison.** Cost is reported alongside accuracy by several papers, and the cost asymmetry is the largest and most consistent harness effect in the corpus, but no study compares harnesses at matched token or dollar budget across more than one benchmark. Where budget was clamped, an architecture advantage became undetectable (entry 20).
- **No deployment-level attribution.** Production evidence appears three times and is observational in all three cases: a rollout with a reduced negative-feedback rate (entry 58), an incrementally deployed refactoring agent confounded with other engineering changes (entry 24), and an online A/B test that its own authors describe as capturing a joint effect that isolates nothing (entry 50).

### 5.5 Domain and instrument skew

Coding agents and web agents dominate; SWE-bench variants, Terminal-Bench and WebArena carry most of the quantitative claims. Root-cause analysis, memory, safety and evaluation-judge studies are represented, but embodied, multimodal and non-English settings are essentially absent, and only three studies treat a human oversight channel as a harness component to be varied (entries 29, 75 and 76). The measuring instrument is also implicated: judge choice alone shifted agent rankings by up to 13 positions (entry 26), an LLM judge reversed the ranking that downstream utility induced (entry 55), and judges mildly favoured their own model family even under a blind protocol (entry 67). Harness confounding is not confined to the system under test; it extends into the evaluator.

### 5.6 Temporal instability

The harness layer changes faster than the literature describing it. A source-code study of eleven production coding harnesses reports that three of its own prior observations required revision within a single quarter (entry 93), and a survey notes that provider endpoints can serve different weights or quantizations under an unchanged name (entry 5). Any harness-controlled comparison that does not pin a content-addressed environment image — which, per entry 18, none of the audited benchmark papers do — is not reproducible even in principle.

### 5.7 Limits of this review's own instruments

The reliability check reported in Section 2.5 measures decision stability under LLM re-prompting, not human agreement, and 100 rated records is a small sample of 1,006 screened. The rigour checklist is an eight-item instrument applied by a single scorer. Saturation was assessed against a 20-domain taxonomy fixed before reading; a corpus can saturate on domains while remaining thin on effect sizes, and Section 5.4 records exactly that outcome.

---

## 6. References

Abramovich, T., & Chechik, G. (2025). AblationBench: Evaluating Automated Planning of Ablations in Empirical AI Research. arXiv preprint. http://arxiv.org/abs/2507.08038v3

Ahn, J., & Kim, M. (2026). From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents. arXiv preprint. http://arxiv.org/abs/2607.08028v1

Ahumada, A. D. H. (2026). DYNAMIC MECHANISMS AND METRICS IN LANGUAGE MODEL-BASED MULTI-AGENT SYSTEMS: A SCOPING REVIEW. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22238539

Albayaydh, W., Zhao, R., & Flechais, I. (2026). Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents. arXiv preprint. https://arxiv.org/abs/2607.05775

Aouali, I., Vasile, F., Sakhi, O., Gilotte, A., & Heymann, B. (2026). RecoAtlas: From Semantic Plausibility to Set-Level Utility in LLM Recommendation Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2605.18805

Assidiqi, M. H., Alghazzawi, D., Alarifi, S., & Cheng, L. (2026). Benchmarking Reference-Free LLM Agent Robustness Under Schema, Policy, and Toolset Drift. IEEE Access, 14, 79662-79672. https://doi.org/10.1109/access.2026.3696096

AUDEBEAU, A. C. (2025). Structured PREreview of "An Exploratory Study of Code Retrieval Techniques in Coding Agents". Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.17536687 [Abstract only; full text could not be retrieved.]

Bai, Y., Duan, J., Peng, J., Wu, X., Liu, S., Wang, S., & Chen, T. (2026). HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety. arXiv preprint. https://doi.org/10.48550/arxiv.2608.17597

Balusu, K. C. (2026). AgentTelemetry: A Fault Detection Benchmark and Toolkit for LLM Agent Observability. Proceedings of the 3rd ACM International Conference on AI-Powered Software, 380-387. https://doi.org/10.1145/3805760.3814931 [Abstract only; full text could not be retrieved.]

Banjade, S. (2026). Schema-Constrained LLM Planning for Executable Molecular Workflows: An Intent-to-Execution Infrastructure for Cheminformatics. ChemRxiv. https://doi.org/10.26434/chemrxiv.15005091/v1 [Abstract only; full text could not be retrieved.]

Barbaste, P., Darrigol, T., Vu, G., & Wiltberger, T. (2026). Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2609.00006

Buldurgan, H. (2026). RE-Bench Is a Systems Benchmark: What Its Scorers and Selection Rules Actually Support. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22089194

Chen, D. T. (2026). RefactorBench-JS: Evaluating LLM Agents on Behavior-Preserving Code Decomposition. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22204480

Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025). BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2508.06600

Chen, Z., White, M., Mooney, R., Payani, A., Su, Y., & Sun, H. (2024). When is Tree Search Useful for LLM Planning? It Depends on the Discriminator. https://doi.org/10.18653/v1/2024.acl-long.738

Chen, Z., Xiao, T., Zhu, H., Yuan, Y., Zhang, L., & Wang, J. (2026). Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents. arXiv (Cornell University). https://arxiv.org/abs/2607.22688

Cheng, Y., Li, C., Cui, Q., Ding, W., Wang, L., Chen, Y., & Gao, P. (2026). CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.18613

Cheung, J. (2026). Harness Resilience: From LLM Availability to Toolchain Continuity in Agentic AI Engineering. https://doi.org/10.33774/coe-2026-4f53g

Chevrot, A., Vernotte, A., Falleri, J., Blanc, X., Legeard, B., & Cretin, A. (2025). Are Autonomous Web Agents Good Testers?. Proceedings of the ACM on software engineering., 2(ISSTA), 206-228. https://doi.org/10.1145/3728879

De Chezelles, T. L. S., Gasse, M., Drouin, A., Caccia, M., Boisvert, L., Thakkar, M., Marty, T., Assouel, R., Shayegan, S. O., Jang, L., Lù, X. H., Yoran, O., Kong, D., Xu, F. F., Reddy, S., Cappart, Q., Neubig, G., Salakhutdinov, R., Chapados, N., & Lacoste, A. (2024). The BrowserGym Ecosystem for Web Agent Research. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2412.05467

Dhakal, A., Neupane, K., & Chaudhary, A. (2026). Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2607.13085

Fei, Y., Liu, N., Yu, X., Chen, S., Li, L., Thapa, R., Ciobanu, M., Singh, N. P., Mao, Q., & Das, R. (2026). How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.14905

Forment, M. A., Guerrero, M. J. C., García-Peñalvo, F. J., & Pereira, J. (2026). The Scaffolding Matters More Than the Interface: A Controlled Comparison of MCP and CLI Tool Use Across Seven Agent Scaffoldings, Five Language Models, and One Software Task. arXiv preprint. http://arxiv.org/abs/2608.08654v1

Gaikwad, M. (2026). Did You Check the Right Pocket? Cost-Sensitive Store Routing for Memory-Augmented Agents. arXiv preprint. http://arxiv.org/abs/2603.15658v1

Gallego, V. (2026). Distilling Feedback into Memory-as-a-Tool. arXiv preprint. http://arxiv.org/abs/2601.05960v2

Galster, M., Mohsenimofidi, S., Lulla, J. L., Abubakar, M. A., Treude, C., & Baltes, S. (2026). Harness Engineering for Agentic AI Coding Tools: An Exploratory Study. arXiv preprint. http://arxiv.org/abs/2602.14690v5

Gan, C., Wei, H., Liang, Y., Cai, Z., Zhang, Q., & Ni, S. (2026). MAG: A Web-Agent Benchmark and Harness for Multimodal Action and Guide Generation. arXiv preprint. https://doi.org/10.48550/arxiv.2607.10079

Gautam, I., & K.C., K. (2026). Retrieval Beats Cheap Structured Memory: A Cost–Retention Study of LLM Agent Memory on Real Long-Conversation Benchmarks. https://doi.org/10.20944/preprints202608.1369.v1

Guo, J., Hao, Z., Wang, C., Fan, C., Luo, T., Li, H., Gao, Y., Mei, H., Peng, J., Xu, R., Dong, M., Wu, H., Zheng, M., Han, K., Wang, S., Xu, C., & Wang, Y. (2026). From Question Answering to Task Completion: A Survey on Agent System and Harness Design. arXiv preprint. https://doi.org/10.20944/preprints202606.1312.v1

Han, J., Xu, Y., Liao, Y., Wang, X., Jiang, Z., Di, Z., Lu, F., Hu, Z., & Xiao, Y. (2026). Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?. arXiv preprint. https://arxiv.org/abs/2608.04828

He, C., Zhou, X., Wang, D., Xu, H., Liu, W., & Miao, C. (2026). Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime. Preprints.org. https://doi.org/10.20944/preprints202603.1756.v1

Hou, Y., Chen, H., Zhou, S., Chen, X., Liu, X., Yuan, D., Meng, L., Wang, S., Liu, Q., & Huang, J. (2026). Harness-G: A Graph-Structured Harness for Search Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2607.27652

Inguglia, G. (2026). First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope. arXiv preprint. https://doi.org/10.48550/arxiv.2605.28916

Jiang, H., Wang, Z., Nie, X., Gao, D., Li, J., & Pei, C. (2026). RCAgentBench: An Agent-Oriented Benchmark for Multimodal Root Cause Analysis in Microservices. 2026 IEEE/ACM International Symposium on Quality of Service (IWQoS), 1-10. https://doi.org/10.1109/iwqos70441.2026.11661026

Kale, N., Zhang, C. B. C., Zhu, K., Aich, A., Rodriguez, P., Team, S. R., Knight, C. Q., & Wang, Z. (2025). Reliable Weak-to-Strong Monitoring of LLM Agents. arXiv preprint. http://arxiv.org/abs/2508.19461v1

Kaplunovich, A. (2025). Advancing LLM Agents for Code Generation: Observability, Orchestration, Reliable Performance. 2025 International Conference on Intelligent Computing, Communication, Networking and Services (ICCNS), 108-116. https://doi.org/10.1109/iccns66249.2025.11428688

Kapoor, S., Stroebl, B., Kirgis, P., Nadgir, N., Siegel, Z. S., Wei, B., Xue, T., Chen, Z., Chen, F., Utpala, S., Ndzomga, F., Oruganty, D., Luskin, S., Liu, K., Yu, B., Arora, A., Hahm, D., Trivedi, H., Sun, H., ... Narayanan, A. (2025). Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2510.11977

Karten, S., Zhang, A. L., Thomas, K., Müller, S., Bakouch, E., Auras, D., Senghaas, M., Obeid, F., Dunas, K., Hagemann, J., & Jaghouar, S. (2026). Prime Agent: A Self-Improving RLM Harness. arXiv preprint. https://doi.org/10.48550/arxiv.2608.23552

Kevin, C., Raghavan, N., Puget, J.-F., Malani, R., Puvvadi, M., Abramovitch, M., Gupta, M., Akkiraju, R., Prabhu, S., Dangi, Y., Luo, W., & Lee, S. H. (2026). Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills. arXiv preprint. http://arxiv.org/abs/2608.20614v1

Kim, K., Choi, Y., Lee, S., Jun, S., Kim, D., & Park, S. (2026). The Interplay of Harness Design and Post-Training in LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2606.25447

Kinjo, A. R., & Yamamoto, Y. (2026). Measure before you rewrite: ablation-driven redesign of LLM-facing RDF schema documentation in TogoMCP. https://doi.org/10.37044/osf.io/6v5ra_v1 [Abstract only; full text could not be retrieved.]

Kuligin, L., Lammert, J., Ostapenko, A., Bressem, K. K., Boeker, M., & Tschochohei, M. (2025). Prompt design for medical question answering with Large Language Models. Machine Learning with Applications, 22, 100758-100758. https://doi.org/10.1016/j.mlwa.2025.100758 [Abstract only; full text could not be retrieved.]

Lai, J., & Li, Z. (2026). A Comparative Empirical Evaluation of Single-Agent and Multi-Agent LLM Prompting Strategies for Automated Formative Feedback in Education. Journal of Intelligence and Engineering Technology, 1(2), 29-38. https://doi.org/10.70393/6a696574.343135

Lee, G., Bach, E., Yang, E., Pollard, T., Johnson, A. E. W., Choi, E., jia, Y., & Lee, J. H. (2025). FHIR-AgentBench: Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2509.19319

Lee, H., Xu, J., Seely, J., Lee, D., Zaharia, M., & Tang, Y. (2026). Recursive Harness Self-Improvement. arXiv preprint. http://arxiv.org/abs/2607.15524v1

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-T., Rocktäschel, T., Riedel, S., & Kiela, D. (2026). Affordance-Compiled Intelligence: Observable-Only Cognitive Impedance Matching for No-Meta LLM-Integrated Systems. arXiv (Cornell University). https://doi.org/10.5281/zenodo.20116149

Li, J., & Storhaug, A. (2026). Reproducible, Explainable, and Effective Evaluations of Agentic AI for Software Engineering. https://doi.org/10.1145/3803437.3805548 [Abstract only; full text could not be retrieved.]

Li, J., Wu, Y., & Chang, Y. (2026). Agent harness engineering: A survey. Preprints.org. https://doi.org/10.20944/preprints202606.2203.v1

Li, Y., Li, L., Wu, Z., Liao, Q., HAO, J., Shao, K., & Xu, F. (2026). AgentSwift: Efficient LLM Agent Design via Value-Guided Hierarchical Search. Proceedings of the AAAI Conference on Artificial Intelligence, 40(38), 31843-31851. https://doi.org/10.1609/aaai.v40i38.40453

Liao, M. (2025). Process-Aware LLM-Agent Scaffolds for Metric-Based Microservice Root-Cause Analysis with Evidence-Trace Scoring. Stout in Computer Science and Technology Studies, 1(1), 48-61. https://doi.org/10.61424/zngee941

Lou, X., Lázaro-Gredilla, M., Dedieu, A., Wendelken, C., Lehrach, W., & Murphy, K. P. (2026). AutoHarness: improving LLM agents by automatically synthesizing a code harness. arXiv preprint. http://arxiv.org/abs/2603.03329v1

Lukei, M., & Kowol, P. T. (2026). Adaptive Orchestration with Cross-Episode Memory for Dynamic LLM-based Agent Pools. WOCHAT2026: Workshop on Chatbots and Agentic Technologies, 22-45. https://doi.org/10.21437/wochat.2026-4

Mahdi, H. (2026). Perceive, Plan, Act, Self-Correct: An Architectural Framework for Goal-Directed Agentic AI Systems. https://doi.org/10.31224/6738 [Abstract only; full text could not be retrieved.]

Matsnev, G. (2026). Uncertainty Decomposition for Clarification Seeking in LLM Agents. arXiv preprint. http://arxiv.org/abs/2606.19559v1

Mayoral-Vilches, V., Balassone, F., Sanz-Gómez, M., Landa, P. Z., Prieto, D. S., Álvarez, M. O., Quarta, D., & Pinzger, M. (2026). Towards Cybersecurity SuperIntelligence (CSI): What's the best harness for cybersecurity?. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2605.28334

Meng, Q., Wang, Y., Chen, L., Li, Y., Wu, W., Jiang, W., Wang, Q., Lu, C., Gao, Y., Wu, Y., & Hu, Y. (2026). Agent harness for large language model agents: A survey. Preprints.org. https://doi.org/10.20944/preprints202604.0428.v1

Miller, H. E., Greenig, M., Tenmann, B., & Wang, B. (2025). BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML. bioRxiv (Cold Spring Harbor Laboratory). https://doi.org/10.1101/2025.09.01.673319

Mody, P., Panchal, M., Kar, R., Bhowmick, K., & Karani, R. (2026). CraniMem: Cranial Inspired Gated and Bounded Memory for Agentic Systems. arXiv preprint. https://doi.org/10.48550/arxiv.2603.15642

Moghadasi, M. N., & Ghaderi, F. (2026). What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2605.21404

Morla, T., Bellibaltu, R. R., Singh, M., & Kapoor, M. S. (2026). AgentFairBench: Do LLM Agents Discriminate When They Act?. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2606.16723

Naakka, A., Wang, Y., & Mäntylä, M. (2026). LATS-RCA: Language Agent Tree Search for Root Cause Analysis in Microservices. Lecture notes in computer science, 196-212. https://doi.org/10.1007/978-3-032-36590-3_14

Ning, X., Tieu, K., Fu, D., Wei, T., Li, Z., Bei, Y., Zou, J., Ai, M., Liu, Z., Li, T.-W., Chen, L., Zhao, Y., Yang, K., Li, B., Qian, C., Li, G., Lin, X., Zeng, Z., Qiu, R., ... He, J. (2026). Code as Agent Harness. arXiv preprint. http://arxiv.org/abs/2605.18747v1

Ochi, Y., & Uchiyama, Y. (2026). Five Whys as an Epistemic-Honesty Scaffold for Multi-Agent LLM Analysis of Industrial Time Series. International Journal of Advanced Computer Science and Applications, 17(8). https://doi.org/10.14569/ijacsa.2026.0170803

Orogat, A., Rostam, A., & Mansour, E. (2026). Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis. arXiv preprint. http://arxiv.org/abs/2602.03128v1

Palmer, C. (2026). professorpalmer/durable-state-vs-context: v1.0.0 — State, Not Tokens. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.20709566 [Abstract only; full text could not be retrieved.]

Pan, W., Liu, S., Lin, C.-Y., Zeng, J., Tang, X., Zhou, X., Lu, Y., & Jia, X. (2026). Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference. arXiv preprint. https://doi.org/10.48550/arxiv.2606.05922

Perikala, K. (2026). A MODULAR BENCHMARKING FRAMEWORK FOR EVALUATING LLM-BASED AGENT APPLICATIONS. INTERNATIONAL JOURNAL OF RESEARCH IN COMPUTER APPLICATIONS AND INFORMATION TECHNOLOGY, 9(1), 1-14. https://doi.org/10.34218/ijrcait_09_01_001

Purwar, A., Singh, S., & Srivastava, K. (2026). Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight. arXiv preprint. http://arxiv.org/abs/2608.24314v1

Rafique, M., & Bindschaedler, L. (2026). C <scp>law</scp> VM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents. Proceedings of the Sixth European Workshop on Machine Learning and Systems, 1-12. https://doi.org/10.1145/3805621.3807648

Raj, A. (2026). Harnessing LLMs for Reliable Academic Supervision: A Comparative Study. arXiv preprint. https://doi.org/10.5281/zenodo.21380236

Rombaut, B. (2026). Inside the scaffold: A source-code taxonomy of coding agent architectures. arXiv preprint. https://arxiv.org/abs/2604.03515

Sanabria, D. (2026). OpenAI single-agent LLM architecture reduces computational overhead relative to multi-agent orchestration in a simulated mars rover decision-support benchmark. Frontiers in Robotics and AI, 13, 1877762-1877762. https://doi.org/10.3389/frobt.2026.1877762

Sarkar, I. (2026). Agentic AI Between Capability and Reliability: A Structured Review of Architectures, Design Patterns, Evaluation Practice, and Enterprise Deployment. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21809562 [Abstract only; full text could not be retrieved.]

Sghaier, O. B., Li, H., Adams, B., & Hassan, A. E. (2026). Don't Blame the Large Language Model: How Scaffolding Evolution Shapes Coding Agent Quality. arXiv preprint. https://arxiv.org/abs/2607.03691

Shah, J. (2026). Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures. arXiv preprint. https://doi.org/10.48550/arxiv.2606.08275

Shekkizhar, S., Cosentino, R., Earle, A., & Savarese, S. (2025). Echoing: Identity Failures when LLM Agents Talk to Each Other. arXiv preprint. https://doi.org/10.48550/arxiv.2511.09710

Siegel, Z. S., Kapoor, S., Nadgir, N., Stroebl, B., & Narayanan, A. (2024). CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark. arXiv preprint. https://doi.org/10.48550/arxiv.2409.11363

Sigdel, A., & Baral, R. (2026). Schema First Tool APIs for LLM Agents: A Controlled Study of Tool Misuse, Recovery, and Budgeted Performance. arXiv preprint. http://arxiv.org/abs/2603.13404v1

Soularidis, A., Doumanas, D., Kotis, K., & Vouros, G. A. (2025). Automating agentic collaborative ontology engineering with role-playing simulation of LLM-powered agents and RAG technology. The Knowledge Engineering Review, 40. https://doi.org/10.1017/s026988892510009x

Souza, R., Poteet, T., Etz, B., Rosendo, D., Gueroudji, A., Shin, W., Balaprakash, P., & da Silva, R. F. (2025). LLM Agents for Interactive Workflow Provenance: Reference Architecture and Evaluation Methodology. arXiv preprint, 2257-2268. https://doi.org/10.1145/3731599.3767582

Sritharan, T. (2026). Agent Brain: A Biologically Inspired Memory System for Autonomous AI Agents — LongMemEval-M Evaluation. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.19673132

Strain, P. M. (2026). Bounded Returns to Orchestration: A Synthesis Ceiling Beneath Eleven Controlled Deep-Research Architectures. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21118281

Sundar, N. A., & Morabia, T. (2026). Hierarchical Online Prompt Mutation with Dual-Loop Feedback for Guardrailed Evidence Document Generation: A Production-Evaluation Case Study. arXiv preprint. http://arxiv.org/abs/2606.01472v1

Tao, J., & Zhou, L. (2026). Agent Reasoning Tools (ARTs): A Tool Definition Approach for Empower LLM-based Agent Systems. Proceedings of the Annual Hawaii International Conference on System Sciences. https://doi.org/10.24251/hicss.2026.096

Team, T. A. L., Sun, Y., Lin, W., Luo, Y., Hu, Y., Jin, M., Ma, J., Pan, W., Zhao, J., & Chen, Z. (2026). Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report. arXiv preprint. http://arxiv.org/abs/2608.15763v3

Tripathy, A., Harshit, C. P., & Vaidhyanathan, K. (2025). SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs. arXiv preprint, 104-111. https://doi.org/10.1145/3786167.3788406

Vats, N., & Golev, O. (2026). The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation. arXiv preprint. http://arxiv.org/abs/2607.22585v1

Wahid, A. R. (2026). BATITONG: Deterministic Reliability for LLM-Driven Offensive-Security Orchestration. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21759172

Wang, S., Qian, P., Lin, Y., Xu, J. Q., Chen, Y., Jiang, X., Liu, L., & Yu, H. (2026). Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2607.13083

Wang, Y., & Wang, C. (2026). The Observability Gap: Why Output-Level Human Feedback Fails for LLM Coding Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2603.26942

Wang, Z., Gu, L., Chi, Z., Liu, Z., Ayyoubzadeh, S. M., Yu, Y., & Wang, Y. (2026). Benchmarking LLM Judges for Mobile Agent Evaluation. arXiv preprint. https://doi.org/10.48550/arxiv.2608.11434

Wang, Z., Huang, H., Zhao, H., Xu, C., Zhu, S., Janßen, J., & Viswanathan, V. (2025). DREAMS: Density Functional Theory Based Research Engine for Agentic Materials Simulation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2507.14267

Wei, H. (2026). From Agent Loops to Structured Graphs: A Scheduler-Theoretic Framework for LLM Agent Execution. arXiv preprint. https://arxiv.org/abs/2604.11378

Wu, Y., Zhang, J., Shi, J., Lei, X., Gu, Q., Zhang, Y., Wang, Z., He, C., Huang, C., Song, M., Zeng, Z., Wang, S., Liu, J., Shi, Y., Liu, J., Yan, S., Huang, W., Zhang, G., & Zhang, W. (2026). HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?. arXiv preprint. https://arxiv.org/abs/2609.01437

Xia, B., Lu, Q., Zhu, L., Xing, Z., Zhao, D., & Zhang, H. (2024). Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2411.13768

Xu, T., Wen, H., & Li, M. (2026). Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents. arXiv preprint. http://arxiv.org/abs/2605.22166v2

Xu, Z., Zhang, S., Poyraz, E., Li, Y., Jin, Y., Lu, X., Gu, X., Ramgopal, K., Bodigutla, P. K., & Wang, X. (2026). Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2, 8334-8345. https://doi.org/10.1145/3770855.3818432

Yan, J., & Yang, M. (2025). Schema-Preserving Generation of Clinical TLF Templates and Executable R Code via Iterative LLM-Guided Debugging. https://doi.org/10.36227/techrxiv.176045741.13024122/v1 [Abstract only; full text could not be retrieved.]

Yang, B., Cai, Z., Liu, F., Le, B., Zhang, L., Bissyandé, T. F., Liu, Y., & Tian, H. (2025). A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2506.23749

Yang, K., Bu, Y., Yi, J., Wang, Y., Zhou, B., Dai, J., Hu, S., & Yang, Y. (2026). When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2606.20023

Yao, Y., Tan, X., Liu, C.-H., Li, Y., Wang, Z., Yu, W., Tan, Z., Tian, Y., Zhao, G., Sun, L., Zhang, X., & Yang, T. (2026). Harness-Bench: Measuring harness effects across models in realistic agent workflows. arXiv preprint. https://arxiv.org/abs/2605.27922

Yu, S., Carroll, F., & Bentley, B. L. (2026). The A-R Behavioral Space: Execution-Level Profiling of Tool-Using Language Model Agents in Organizational Deployment. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2604.12116

Zeng, L., Zhang, S., & Zhang, X. (2026). EviDx: Evidence-Aware Active Diagnosis with Scaffolded LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.24570

Zhai, Z., Tan, X., Zou, G., Wang, X., & Zhang, W. (2026). HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents. arXiv preprint. http://arxiv.org/abs/2608.02650v1

Zhang, H., Zhang, S., Li, K., Zhang, C., Chen, Y., Zhang, Y., Bai, L., & Hu, S. (2026). Self-Harness: Harnesses That Improve Themselves. arXiv preprint. http://arxiv.org/abs/2606.09498v3

Zhang, J., Xiang, J., Yu, Z., Teng, F., Chen, X., Chen, J., Zhuge, M., Cheng, X., Hong, S., Wang, J., Zheng, B., Liu, B., Luo, Y., & Wu, C. (2024). AFlow: Automating Agentic Workflow Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2410.10762

Zhang, L., & Wang, T. (2026). Harness Engineered LLM Agents for Material Science: A Case Study on Perovskite Materials with Machine Learning and Materials Project. ChemRxiv. https://doi.org/10.26434/chemrxiv.15004684/v1 [Abstract only; full text could not be retrieved.]

Zhang, S., Wang, A., & Sophie, L. (2026). Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2606.11686

Zhang, W., Guo, H., Yang, J., Tian, Z., Zhang, Y., Yan, C., Li, Z., Li, T., Shi, X., Zheng, L., & Zhang, B. (2024). mABC: multi-Agent Blockchain-Inspired Collaboration for root cause analysis in micro-services architecture. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2404.12135

Zhang, W., Wei, X., Huang, W.-C., Hui, Z., Wang, C., Gong, M., & Yu, P. S. (2026). MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization. arXiv preprint. https://doi.org/10.48550/arxiv.2603.25973

Zhang, Y., Ma, Z., Ma, Y., Han, Z., Wu, Y., & Tresp, V. (2024). WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2408.15978

Zhang, Y., Wang, J., Ge, Y., Xu, W., Hamm, J., & Reddy, C. K. (2026). Stop Comparing LLM Agents Without Disclosing the Harness. arXiv (Cornell University). https://doi.org/10.20944/preprints202605.0711.v1

Zhou, C., Chai, H., Chen, W., Guo, Z., Shan, R., Song, Y., Xu, T., Yang, Y., Yu, A., Zhang, W., Zheng, C., Zhu, J., Zheng, Z., Zhang, Z., Lou, X., Zhang, C., Fu, Z., Wang, J., Liu, W., ... Zhang, W. (2026). Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering. arXiv preprint. http://arxiv.org/abs/2604.08224v1

Zhou, T. (2026). Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.08466

Zhu, P., Sun, L., Yu, P. S., & Su, S. (2026). The Necessity of a Unified Framework for LLM-Based Agent Evaluation. arXiv preprint. https://arxiv.org/abs/2602.03238

Zhuang, N., Cao, B., Yang, Y., Xu, J., Xu, M., Wang, Y., & Liu, Q. (2025). LLM Agents Can Be Choice-Supportive Biased Evaluators: An Empirical Study. Proceedings of the AAAI Conference on Artificial Intelligence, 39(25), 26436-26444. https://doi.org/10.1609/aaai.v39i25.34843

Ziwei, Y. (2026). Set-shifting Behavioral Test for Harnessed Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2607.13396
