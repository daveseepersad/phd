# Stage 8 Synthesis — Specialized Multi-Agent versus Single-Agent LLM Software Engineering

**Author:** Dave Seepersad · **Generated:** 2026-09-04 · **Run:** `results/20260904-specialized-multi-agent-versus-single-ag`

**Provenance:** 417 unique records screened after deduplication, 203 selected for retrieval, 103 full texts retrieved and read, 100 sought but not retrieved. Saturation was declared against 20 preregistered evidence domains with zero new domains across read-order windows 3 through 8. Every quotation below was located in the run's extracted full-text corpus with `corpus_search.py --quote`; every citation string is copied verbatim from `manifest.json`.

---

## 1. Research question

> specialized multi-agent versus single-agent LLM software engineering: comparative performance, coordination failures, verification, reliability, sustainability, and future work

Sub-questions addressed by this synthesis:

* **RQ2.** Under what conditions does role-specialized multi-agent orchestration outperform a single LLM agent on software engineering tasks, and where does it underperform?
* **RQ3.** What coordination, verification, and reliability failure modes are reported, and how are they measured?

---

## 2. What the evidence supports and rejects

### 2.1 The evidence base, and why most of it cannot answer the comparative question

The corpus is large, recent, and methodologically thin at precisely the point where the research question bites. Of the 103 papers read in full, 43 touch the `comparative-single-vs-multi` evidence domain, but only a minority of those actually run a controlled comparison.

| Slice of the corpus | Count |
|---|---|
| Full texts read | 103 |
| Graded **core** | 49 |
| Graded **supporting** | 54 |
| Core papers quality-appraised | 49 |
| Core papers with a full baseline or control (`baseline_or_control` = 1) | 23 |
| Core papers with **no** baseline at all (`baseline_or_control` = 0) | 19 |
| Core papers with a full baseline **and** a direct single-versus-multi arm | **16** |
| Papers touching `comparative-single-vs-multi` (core 22 / supporting 21) | 43 |

Mean `baseline_or_control` across the 49 appraised core papers is **0.541**; mean `threats_discussed` is **0.531**. In plain terms: the comparative question that motivates this review is answered by roughly two dozen properly controlled studies, and by only sixteen core papers that both hold something constant and run a single-agent arm. Everything else is architecture description, taxonomy, or secondary synthesis.

This matters because nineteen core papers carry no baseline at all, and **eight of those nineteen nonetheless make explicit comparative claims**: Otoum and Elkhalili (2026), Rasheeda et al. (2026), Grabowski (2026), Haseeb (2025), Ramírez-Rueda et al. (2024), the anonymous *Demystifying LLM-Based Software Engineering Agents* review, Jin et al. (2024), and Tang and Runkler (2026). Several are surveys that restate primary-study superiority claims without noting that the primary studies rarely used controls, which is how an under-evidenced result propagates into the field's received wisdom. The clearest single instance is a paper that claims to outperform monolithic generation while running no comparison at all:

> Even for models with imperfect first-attempt behavior, the combination of
> deterministic validation and bounded regeneration significantly increases the
> final success rate.
>
> Grabowski (2026), p. 11

The corpus is also young and preprint-heavy: 54 of the 103 read papers are dated 2026, 34 are dated 2025, and 37 of 103 are preprints that have not been peer reviewed. Preprint status is flagged on every per-paper entry in Section 3.

Two evidence domains are effectively empty. `formal-verification` appears in only 3 of 103 read papers and `transactions-concurrency` in exactly 1. Saturation was reached on domain *coverage*, not on domain *depth*, and Section 4 treats this as a gap rather than a finding.

One pair of entries is not independent evidence: Mandal et al. (2024) is the arXiv version and Mandal et al. (2025) the *Nature Communications* version of the same AILA/AFMBench study. Both were retrieved and both appear in Section 3, but the 70% versus 58% result they report is one finding, not two.

### 2.2 What the controlled evidence supports

Restricting attention to studies that hold the base model constant and run a genuine single-agent arm, four claims survive.

**S1. Decomposition can raise the ceiling of a fixed model, not merely redistribute its effort.** Shen et al. (2024) split a tool-use agent into separately fine-tuned planner, caller, and summarizer models and show that a 7B decomposed system beats a 13B single-LLM baseline trained on the same data, with ToolBench hallucination falling from about 2.3% to 0.37–0.57%.

> These observations suggest that the key factor contributing to the success of
> α-UMi lies in its ability to surpass the performance upper-bound of
> Single-LLM.
>
> Shen et al. (2024), p. 8

Zeng et al. (2025) reach a compatible conclusion by a different route, implementing three architectures on one unified toolset specifically to remove engineering confounds: a Dev-Test workflow reaches 49.48% requirement implementation versus 45.72% for a single agent. Li (2026) reports 55.0% differential defect detection for a four-agent framework versus 37.5% for a same-model, same-budget single-agent configuration, and its ablation attributes the gap to role decomposition rather than to the dedicated diagnostic agent.

**S2. Where the task decomposes into genuinely non-overlapping expertise, specialization produces complementary rather than duplicated coverage.** Shu et al. (2024) report a 0.90 goal success rate for a hierarchical supervisor-specialist framework across three enterprise domains against an equivalently tool-equipped single agent that regressed by up to 37 absolute points — though the 90 scenarios were authored by the framework's own vendor team specifically to exercise multi-agent collaboration, which bounds how far the result generalises. Premasundera (2025) finds low Jaccard overlap between four domain-specialized review agents and a monolithic LLM on the same pull request, indicating non-overlapping findings rather than replication. Muhammad et al. (2025) obtain 93.9% versus 86.9% accuracy on entity resolution while simultaneously reducing tokens by roughly 62%, because each agent retrieves selectively rather than reasoning over the union of context.

**S3. Consensus and adversarial cross-checking suppress a specific, measurable failure — unverified oracle hallucination.** Xu et al. (2026), the only paper in the corpus scoring 1.00 on the rigor checklist, ablate a panel-discussion stage and lose 0.067 to 0.086 oracle correctness; replacing consensus-by-reasoning with plain majority voting still loses at least 0.014, and panelists disagreed in over 70% of discussions. Yu et al. (2025) find the same shape in a production incident-triage deployment: removing multi-agent negotiation costs about 12 points of hop-1 accuracy and 21 points at hop 5, a larger loss than removing semantic distillation.

> The most substantial performance degradation is observed when the multi-agent
> negotiation mechanism is removed(w/o MAT).
>
> Yu et al. (2025), p. 8

**S4. Structure, not agent count, is what converts decomposition into gain.** Barrak (2025) is the cleanest demonstration: across eight ordered triples of three frontier models on three benchmarks, an unstructured Planner-Executor-Critic pipeline fell *below* a competent monolithic model, and only the addition of a structured, accountable handoff produced gains of up to 36.22 points.

> Without clear roles and checks, errors compound across stages and accuracy
> falls below a competent single model.
>
> Barrak (2025), p. 5

Shen et al. (2024) supply the training-side analogue: naive per-subtask multi-LLM training underperforms the single-LLM baseline on API-calling metrics, and only a two-stage global-to-local fine-tuning strategy recovers the advantage. Mao et al. (2025) report failure reductions of up to 69.6% purely from adding behavioural contracts, typed messaging, and verification-gated lifecycle state machines to an unchanged MetaGPT role set.

### 2.3 What the controlled evidence rejects

**R1. There is no general multi-agent advantage.** The most direct refutation comes from inside the corpus's best-controlled study. Agha and Miqdad (2026) ran 270 executions across three architectures on one fixed model and one benchmark; the sequential pipeline beat the single agent, and the hierarchical supervisor-worker pattern lost to it decisively.

> The Single-Agent Baseline reached a moderate success rate (81.1%) at the
> lowest cost (0.083 USD per task), while the Hierarchical pattern recorded the
> lowest success rate (54.4%), the highest median latency (142.37 s), and the
> highest mean cost (0.308 USD per task).
>
> Agha & Miqdad (2026), p. 5

Zeng et al. (2025) reproduce the same inversion at a different point in the design space: their Design-Dev-Test workflow collapses to 27.71% requirement implementation against 45.72% for a single agent, because the Design Agent's plan acquires spurious authority downstream.

> Once the Dev Agent receives what it perceives as an authoritative
> implementation plan, it tends to prioritize this plan over direct engagement
> with the original requirement document
>
> Zeng et al. (2025), p. 8

**R2. Multi-agent coordination can be pure overhead.** Radeva et al. (2026) compared five coordination strategies against four 7–8B open-source models on a title-abstract screening task with an archived audit trail, and reported a negative result: the single-agent configuration with the best-matched model in few-shot mode achieved 100% recall, 70.4% precision, and 82.6% F1, beating every multi-agent alternative.

> Multi-agent strategies introduced coordination overhead without measurable
> benefit under the conditions of this study.
>
> Radeva et al. (2026), p. 24

Arnaudo et al. (2026) reach a parallel conclusion in a peer-reviewed study of HumanEval black-box test generation over ten independent runs, and quantify the price:

> Although multi-agent architectures achieve superior test coverage — peaking at
> 99.54% — they yield an ESR comparable to single-agent frameworks (96.98%
> versus 96.89%).
>
> Arnaudo et al. (2026), p. 1

> Crucially, this comes at the expense of a threefold to fourfold increase in
> token expenditure.
>
> Arnaudo et al. (2026), p. 1

**R3. Adding agents is not compositional.** Kim et al. (2026) is the largest controlled scaling study in the corpus — 180 configurations, three LLM families, four benchmarks, standardized tools and token budgets — and it identifies a saturation point beyond which coordination is actively harmful.

> tasks where single-agent performance already exceeds 45% accuracy experience
> negative returns from additional agents, as coordination costs exceed
> diminishing improvement potential
>
> Kim et al. (2026), p. 6

> Yet for sequential reasoning tasks, every multi-agent variant we tested
> degraded performance by 39–70%.
>
> Kim et al. (2026), p. 3

Sapkota et al. (2025a) name the mechanism directly, and Yang et al. (2025) show it empirically in a heterogeneity ablation where role and model diversity *hurt* three-agent teams and only paid off at five agents.

> Unlike traditional modular systems, where adding components can enhance
> overall functionality, introducing additional agents in an Agentic AI
> architecture often increases cognitive load, noise, and coordination overhead.
>
> Sapkota et al. (2025a), p. 20

**R4. Role specialization is not the only, and often not the primary, source of measured gain.** Ashrafi et al. (n.d.) evaluated five configurations across 19 LLMs and found runtime execution debugging alone captured almost all of the accuracy benefit of a full Analyst-Coder-Tester chain plus debugger — a statistically insignificant 0.96-point gap — while agent chaining multiplied latency from 7.68 to 68.42 minutes and *degraded* robustness under expanded test coverage.

> AC and ACT showed substantial robustness drops (129.27 and 118.51), showing
> that agentic interaction introduces fragility.
>
> Ashrafi et al. (n.d.), p. 5

Wang et al. (2024) show external compiler grounding beating both self-repair and the multi-agent Self-Collaboration baseline. Pham et al. (2026) show a single retry lifting Pass@1 from below 25% to above 80% in a quantum debugging pipeline. Ravindran et al. (2026) show frontier models with a *single-agent* reflection loop and simulator feedback matching or exceeding published multi-agent RTL orchestration pipelines, though they read this as benchmark saturation rather than a general verdict. Vella et al. (2026) make the sharpest version of the point: in a controlled comparison on 24 IEEE 14764 maintenance tasks, an AutoGPT-style agentic baseline was statistically indistinguishable from unconstrained prompting (p = 0.69, d = 0.19), while governed template-driven execution beat both with effect sizes above d = 2.2.

> The evidence suggests that governance, rather than agentic execution alone, is
> the primary determinant of reliable enterprise software sustaining
> engineering.
>
> Vella et al. (2026), p. 1

**R5. Reported benchmark advantages do not transfer to production.** Takerngsaksiri et al. (2025) deployed a three-role pipeline inside Atlassian JIRA and measured 86% file-localization recall on SWE-bench Verified against 30% on proprietary enterprise issues. Rodriguez-Cardenas et al. (2026) report models exceeding 70% on SWE-bench Verified falling to 23% on SWE-bench Pro, concluding memorization rather than capability. Liu et al. (2023) show that augmenting HumanEval tests 80-fold drops pass@k by up to 28.9% *and reorders model rankings*, which invalidates cross-architecture comparisons drawn from the unaugmented benchmark.

> We also surprisingly found that test insufficiency can lead to mis-ranking.
>
> Liu et al. (2023), p. 1

### 2.4 Direct disagreements between papers

These are not differences of emphasis. In each case, two studies with defensible designs report opposing results on overlapping questions.

| # | Disagreement | Pro-multi-agent position | Counter-position |
|---|---|---|---|
| D1 | Does role-specialized orchestration beat a single agent on the same task with the same model? | Kumar et al. (2026): 40.0% vs 14.0% on SWE-bench Lite, +26 points, with per-role ablations. Shu et al. (2024): 0.90 vs 0.53 goal success in the software domain | Agha & Miqdad (2026): hierarchical 54.4% vs single-agent 81.1% on TestEval, same model. Radeva et al. (2026): single-agent F1 82.6% beats all five multi-agent strategies. Arnaudo et al. (2026): 96.98% vs 96.89% ESR at 3–4x tokens |
| D2 | Is the gain caused by role decomposition or by execution/verification grounding? | Li (2026): ablating the diagnostic agent costs only 2.5 points, so the 17.5-point advantage is attributed to decomposition. Xu et al. (2026): the panel ablation is the largest single loss | Ashrafi et al. (n.d.): ablating the agents leaves the debugger delivering 63.86% vs 64.82% for the full chain. Mohammad et al. (2026): removing symbolic and RAG grounding costs 10 F1 points. Abdalla et al. (2026): the test-diagnose-fix loop, not the roles, drives 47.4% to 73.7% |
| D3 | Does architecture or base-model choice explain more of the variance? | Orogat et al. (2026): with the LLM held fixed, framework design alone changes latency by over 100x and coordination success from above 90% to below 30% | *Demystifying LLM-Based Software Engineering Agents* (n.d.): swapping GPT-4o for Claude 3.5 Sonnet inside an unchanged Agentless pipeline lifted SWE-bench Lite resolution from 27.3% to 40.7%. Radeva et al. (2026): model selection outweighs coordination at 7–8B scale. Monteiro et al. (2025): 70.1% vs 34.3% successful tests from model choice alone inside one agent |
| D4 | Does hierarchical supervision help or hurt? | Shu et al. (2024): hierarchical supervisor-specialist reaches 0.90 GSR against 0.53 single-agent. Kim et al. (2026): centralized validation contains error amplification to 4.4x versus 17.2x for independent agents | Agha & Miqdad (2026): hierarchical is the worst of three patterns, with a supervisor information bottleneck in 100% of its failures. Youwai et al. (2026): conventional fixed designer-checker workflows underperformed even plain single agents on the same tasks, scoring 38.75% on shallow foundations with a Gemini 2.5 Pro backbone |

Two of these disagreements are internally consistent once the moderating variable is named, and one is not.

D1 and D4 dissolve into the same finding: **topology, not agent count, is the operative variable, and pipeline or router topologies beat supervisor-worker topologies when information must survive a handoff.** Agha and Miqdad (2026) attribute every hierarchical failure to a specific mechanism.

> The hierarchical pattern suffered from supervisor information bottleneck
> according to the qualitative results confirmed by 100% of the failing tasks
> of the architecture.
>
> Agha & Miqdad (2026), p. 5

Reid et al. (2025) predict exactly this shape from first principles, and Liu (2025) measures its cost: replacing message passing with a shared-state blackboard raises correct file targeting by 27.5 percentage points while costing 2.17x tokens.

D3 does not dissolve. Orogat et al. (2026) and the Agentless line of evidence are measuring different things — Orogat et al. fix the model to isolate framework effects, while the Agentless comparison fixes the framework to isolate model effects — but they draw *general* conclusions from those local designs, and the field currently has no study that varies both factors factorially. This is the single largest unresolved methodological dispute in the corpus and is carried forward as a gap in Section 4.

A further disagreement worth recording concerns heterogeneity. Tomic et al. (2025) pre-registered the hypothesis that mixed specialist models beat one shared model and rejected it per-site; Yang et al. (2025) found homogeneous three-agent teams outperform heterogeneous ones; but Barrak (2025) found heterogeneous pipelines repeatedly on the accuracy-cost Pareto frontier and Calboreanu (2026) found four frontier vendors had *non-overlapping* blind spots so that only the multi-vendor union detected all seeded defects. The reconciling variable appears to be whether the task rewards diverse error profiles (auditing, review) or penalizes interface mismatch (tightly coupled generation).

### 2.5 RQ2 — Conditions under which specialization pays, and where it does not

The controlled evidence supports a conditional rather than a general answer. The conditions below are each backed by at least one study with a same-model control.

**Specialization tends to pay when:**

1. **The single-agent baseline is weak on the task.** Kim et al. (2026) locate the crossover empirically at roughly 45% single-agent accuracy. Mandal et al. (2025) observe the corresponding model-side effect: the multi-agent configuration beat direct tool integration for GPT-4o (70% vs 58%) but made no measurable difference for weaker models that failed the cross-domain coordination regardless of topology.
2. **The decomposition mirrors a real information boundary.** Muhammad et al. (2025), Wang et al. (2025), and Premasundera (2025) all report gains where each agent consumes a genuinely different slice of context; Zeng et al. (2025) report losses where an added agent inserts an authoritative artifact between the implementer and the requirement.
3. **A specialized agent is attached to an external, non-LLM oracle.** Kumar et al. (2026), Abdalla et al. (2026), Wang et al. (2024), Essam et al. (2026), and Mohammad et al. (2026) all show the gain concentrating in whichever role owns compilation, simulation, static analysis, or a knowledge graph.
4. **The task rewards diverse error profiles.** Xu et al. (2026), Calboreanu (2026), Li, W., et al. (2025), and Premasundera (2025) show consensus and multi-vendor union recovering defects that no single reviewer finds.
5. **Failures are injected or expected.** Chebolu et al. (2026) report that a decentralized design's advantage over a centralized scheduler running identical planning and repair logic was concentrated under injected failures rather than under normal conditions.

**Specialization tends to underperform when:**

1. **The task is sequential and non-parallelizable.** Kim et al. (2026) measured 39–70% degradation across every multi-agent variant tested.
2. **The topology forces information through a single summarizing supervisor.** Agha and Miqdad (2026) and Reid et al. (2025) converge on this; Reid et al. note that a centralized orchestrator's own cognitive limits become a system-wide bottleneck because delegates lack visibility of the full task.
3. **A fixed role sequence is applied regardless of task type.** Youwai et al. (2026) found conventional designer-checker workflows underperforming plain single agents on the same tasks, while a router that dispatches by task class beat both and had the lowest run-to-run variance.
4. **Handoffs are unstructured natural language.** Barrak (2025) and Mao et al. (2025) both show that adding contracts to an existing role set recovers most of the deficit.
5. **The base model is small.** Radeva et al. (2026) found no coordination benefit at 7–8B, and hypothesize larger models may benefit more — a hypothesis the corpus does not test.
6. **The benchmark is near saturation.** Ravindran et al. (2026) and Rodriguez-Cardenas et al. (2026) both argue aggregate pass rates have stopped discriminating between architectures.

### 2.6 RQ3 — Coordination, verification, and reliability failure modes, and how they are measured

The corpus converges on a taxonomy far more consistently than it converges on performance. Failure modes cluster into five families.

| Family | Representative reported modes | How measured, and by whom |
|---|---|---|
| **Planning and decomposition** | requirement omission, misinterpretation, architectural design flaw, subtask immersion | Zeng et al. (2025) attribute 55.8% of all failures to planning (omission 27.9%, misinterpretation 22.2%) via a root-cause taxonomy over an LLM-judged requirement checklist; Lu et al. (2025) build a 19-cause three-tier taxonomy from 104 failures over 204 runs |
| **Inter-agent misalignment** | supervisor information bottleneck, delegation leak, interface mismatch, agent-selection misrouting, role flipping | Agha and Miqdad (2026) code 66 interaction traces; Mandal et al. (2025) report 28.3% agent-selection errors for Claude 3.5; Li et al. (2023) name role flipping, instruction repetition, flake replies, and infinite loops |
| **Non-adaptive loops and non-termination** | consecutive action repetition, cognitive deadlock, divergence without recovery, unreliable termination | Bouzenia and Pradel (2025) contrast 120 successful and failed trajectories over 2,822 LLM interactions; Kumar et al. (2026) find cognitive deadlock in 20.0% of 30 sampled failures; Basu et al. (2026) find pairs that diverged after 3, 21, and 69 iterations never recovered |
| **Verification and oracle failure** | oracle hallucination, test overfitting, self-confirming loops, goal substitution | Xu et al. (2026) use mutation score plus panel ablation; Li (2026) exposes a 35-point gap between an unconditional 90.0% detection figure and a 55.0% differential rate; Shinn et al. (2023) measure a 16.3% self-generated-test false-positive rate; Xu and Qin (2026) name goal substitution and diagnose it from the visible reasoning chain |
| **Cascading and emergent effects** | error amplification, anomaly propagation, semantic drift, monoculture and correlated error, collective toxicity | Kim et al. (2026) quantify 17.2x versus 4.4x amplification by topology; Seyedghorban et al. (2026) inject faults at communication boundaries; Hossain et al. (2026) synthesize a coordination-overhead threshold; the *Demystifying* review names correlated error |

Three measurement findings deserve separate emphasis because they constrain everything above.

**Attribution is weak.** Wang et al. (2026) survey 55 papers on trajectory analysis and report that step-level failure attribution accuracy on the Who&When benchmark spans only about 25% to 52%.

> In terms of reported accuracy, on the Who&When benchmark, reported step-level
> attribution accuracy varies substantially across techniques, ranging from
> about 25% [11] to 52% [39].
>
> Wang et al. (2026), p. 12

Qi et al. (2026) explain why: the point at which an anomaly becomes observable rarely coincides with its origin.

> As role diversity increases, so does interdependence among agents, making the
> system more sensitive to interface mismatches, cascading errors, and
> coordination overhead.
>
> Qi et al. (2026), p. 37

**Benchmarks do not measure coordination.** Kehkashan et al. (2026) audited 15 agent benchmarks and found 0/15 score safety or security, 0/15 include cost-efficiency in the primary protocol, and 13/15 rely solely on binary success; across 1,240 trajectories, action efficiency varied 340% among agents that scored identically.

> Multi-agent systems bring about coordination failures, emergent behavior and
> dynamics of interaction that cannot be seen in single-agent benchmarks.
>
> Kehkashan et al. (2026), p. 43

> The field evaluates what agents produce, not how well they collaborate.
>
> *LLM-Based Multi-Agent Orchestration* (2026), p. 22

**The frameworks themselves are buggy in ways deterministic testing cannot catch.** Xue et al. (2025) manually annotated 1,026 bug instances across LangChain, LlamaIndex, and Haystack.

> Moreover, we identified Unexpected Output as a significant new symptom
> category (169 occurrences, 16.5%) uniquely relevant to LLM agent frameworks,
> reflecting their probabilistic and generative nature.
>
> Xue et al. (2025), p. 9

Seyedghorban et al. (2026) show the operational consequence: perturbations at inter-agent communication boundaries propagate more damagingly than equivalent perturbations at a single LLM call, with 59.2x mean runtime amplification for an agent-to-agent delay against 48.1x for an LLM delay in ChatDev.

Calboreanu (2026) adds the one clean argument in the corpus for why some defects are *only* reachable by a multi-context reviewer:

> By construction, single-file review cannot detect cross-lane data-contract
> issues; in this study every cross-lane defect surfaced only after multi-file
> context loading was enabled.
>
> Calboreanu (2026), p. 16

### 2.7 Cost, latency, and sustainability

Cost reporting is sparse. Liu et al. (2024) note that only 46.7% of the papers they surveyed quantify efficiency at all, and Kehkashan et al. (2026) find 0/15 benchmarks include cost in the primary protocol. Where it is measured, the multiplier is consistent and large.

| Study | Cost or latency multiplier for the multi-agent arm |
|---|---|
| Arnaudo et al. (2026) | 3–4x tokens for statistically comparable execution success |
| Kumar et al. (2026) | ~2.7x per-task API cost ($0.1445 vs $0.054) |
| Lai and Li (2026) | ~4.6x tokens; a chain-of-thought single agent delivers 86.5% of top quality at 32.5% of the cost |
| Ashrafi et al. (n.d.) | 7.68 to 68.42 minutes end-to-end |
| Barrak (2025) | 2–3x spend, 8–10x median latency for the accountable pipeline |
| Agha & Miqdad (2026) | 3.7x cost for the worst-performing pattern |
| Li, W., et al. (2025) | 4.7 s to 37.5 s inference, roughly 8x |
| Akshathala et al. (2026) | Agent-as-Judge verification at 16x cost and 62x time versus LLM-as-Judge |
| Liu (2025) | 2.17x tokens and 1.61x latency for shared-state coordination |
| Chebolu et al. (2026) | 4.2% coordination overhead — the lowest reported, under a decentralized design |

Counter-evidence exists but is narrow. Muhammad et al. (2025) report a 62% token *reduction* from selective per-agent retrieval, and Parthasarathy et al. (2025) report faster end-to-end response despite higher token consumption. Both gains come from restricting what each agent reads, not from adding agents.

The sustainability evidence is thin and mostly indirect. Amalfitano et al. (2026) identify inter-agent communication overhead as a direct driver of energy cost in their roadmap; Otoum and Elkhalili (2026) warn that token cost scales disproportionately with system complexity; Thakur and Moin (2026) provide the only direct energy measurement in the corpus, and it concerns retrieval augmentation rather than multi-agent topology. Xiao et al. (2026) demonstrate that 39.9–59.7% of accumulated input tokens in coding-agent trajectories are removable with resolve rate held within −1.0% to +2.0%, which suggests much of the reported multi-agent cost is waste rather than an intrinsic coordination price.

### 2.8 Summary of confidence

| Claim | Confidence | Basis |
|---|---|---|
| No general multi-agent advantage exists; the effect is conditional on topology, task structure, and baseline strength | **High** | Multiple same-model controlled studies reporting in both directions, including within a single paper |
| Coordination overhead is real, large, and under-reported | **High** | Consistent 2–8x multipliers across independent studies; 0/15 benchmarks measure it |
| Supervisor-worker topologies underperform pipeline and router topologies on information-preserving tasks | **Moderate** | Agha and Miqdad (2026), Youwai et al. (2026), Liu (2025), Reid et al. (2025) agree; Shu et al. (2024) is a well-designed dissenter |
| Execution and verification grounding contributes more measured gain than role specialization | **Moderate** | Strong ablation evidence on both sides (D2); no study ablates both factors in one design |
| Planning and decomposition is the dominant failure origin | **Moderate** | Zeng et al. (2025) 55.8%, Lu et al. (2025), Barrak (2025) planner error rates 7.35–40.49%; all single-benchmark |
| Architecture explains more variance than base-model choice | **Low** | Directly contested (D3); no factorial design exists |
| Multi-agent systems are more sustainable or cheaper at equal quality | **Very low / rejected** | Only two narrow counter-examples, both from restricting per-agent context |

---

## 3. Per-paper entries, ordered by contribution

Entries are ordered by contribution to RQ2 and RQ3: controlled single-versus-multi comparisons first, then failure-mode and measurement studies, then secondary syntheses and position papers. Each entry gives the APA citation verbatim from `manifest.json`, the screening grade, the rigor score where one was assigned, peer-review status, and one to three page-anchored quotations verified against the extracted text. The *Contribution* line is a paraphrase, not a quotation.


### 1. An empirical comparison of multi-agent LLM architectural patterns for automated unit test generation

Agha, M., & Miqdad, A. (2026). An empirical comparison of multi-agent LLM architectural patterns for automated unit test generation. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.20309242

**Relevance**: core · **Rigor**: 0.96 · **Peer-reviewed** · **Design**: empirical · **Baseline/control**: present

*Contribution (paraphrase):* In a controlled 270-execution comparison on TestEval unit-test generation with one model held constant, the Sequential pipeline beat the Single-Agent baseline (92.2% vs 81.1% success) while the Hierarchical supervisor-worker pattern underperformed the single agent badly (54.4% success, 28.54% test failure rate, 3.7x the cost); every hierarchical failure was attributed to a 'supervisor information bottleneck' in which the supervisor never relayed the analyst's reasoning to the writer.

> The Sequential pattern recorded the highest success rate (92.2%), the
> lowest latency variance (295.56 s2), and a competitive cost (0.089 USD per
> task).
>
> Agha & Miqdad (2026), p. 5

> The Single-Agent Baseline reached a moderate success rate (81.1%) at the
> lowest cost (0.083 USD per task), while the Hierarchical pattern recorded
> the lowest success rate (54.4%), the highest median latency (142.37 s),
> and the highest mean cost (0.308 USD per task).
>
> Agha & Miqdad (2026), p. 5

> The hierarchical pattern suffered from supervisor information bottleneck
> according to the qualitative results confirmed by 100% of the failing
> tasks of the architecture.
>
> Agha & Miqdad (2026), p. 5

### 2. Towards a Science of Scaling Agent Systems

Kim, Y., Gu, K., Park, C., Park, C., Schmidgall, S., Heydari, A. A., Yan, Y., Zhang, Z., Zhuang, Y., Liu, Y., Malhotra, M., Liang, P., Park, H. W., Yang, Y., Xu, X., Du, Y., Patel, S., Althoff, T., McDuff, D., & Liu, X. (2026). Towards a Science of Scaling Agent Systems. Research Square. https://doi.org/10.21203/rs.3.rs-8414536/v1

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: benchmark-study

*Contribution (paraphrase):* A controlled 180-configuration comparison of single-agent versus four multi-agent topologies across four agentic benchmarks derives quantitative scaling principles: a tool-coordination trade-off, a capability saturation point around 45% single-agent accuracy beyond which coordination gives negative returns, and topology-dependent error amplification of 17.2x (independent) versus 4.4x (centralized).

> Yet for sequential reasoning tasks, every multi-agent variant we tested
> degraded performance by 39–70%.
>
> Kim et al. (2026), p. 3

> tasks where single-agent performance already exceeds 45% accuracy
> experience negative returns from additional agents, as coordination costs
> exceed diminishing improvement potential
>
> Kim et al. (2026), p. 6

> Independent systems amplify errors 17.2× through unchecked error
> propagation
>
> Kim et al. (2026), p. 6

### 3. Benchmarking and Studying the LLM-based Agent System in End-to-End Software Development

Zeng, Z., Li, Y., Xie, R., Ye, W., & Zhang, S. (2025). Benchmarking and Studying the LLM-based Agent System in End-to-End Software Development. arXiv preprint. https://doi.org/10.48550/arxiv.2511.04064

**Relevance**: core · **Rigor**: 0.92 · **Preprint (not peer reviewed)** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* With three agent architectures implemented on a unified toolset to remove engineering confounds, a Dev-Test multi-agent workflow beat a single agent (49.48% vs 45.72% requirement implementation rate) while a Design-Dev-Test workflow collapsed to 27.71%, showing multi-agent decomposition helps only when well structured; 55.8% of all failures originated in planning (requirement omission 27.9%, misinterpretation 22.2%) rather than code implementation.

> The results in Table 5, clearly indicate that “Task Planning” is the
> primary bottleneck in current agent systems, accounting for 55.8% of all
> issues.
>
> Zeng et al. (2025), p. 9

> Once the Dev Agent receives what it perceives as an authoritative
> implementation plan, it tends to prioritize this plan over direct
> engagement with the original requirement document
>
> Zeng et al. (2025), p. 8

### 4. Traceability and Accountability in Role-Specialized Multi-Agent LLM Pipelines

Barrak, A. (2025). Traceability and Accountability in Role-Specialized Multi-Agent LLM Pipelines. 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW), 315-322. https://doi.org/10.1109/asew67777.2025.00064

**Relevance**: core · **Rigor**: 0.92 · **Peer-reviewed** · **Design**: empirical · **Baseline/control**: present

*Contribution (paraphrase):* Across 8 pipeline configurations of 3 frontier LLMs on 3 benchmarks, an unstructured Planner-Executor-Critic pipeline fell below a competent monolithic model, while adding a structured accountable handoff raised accuracy by up to 36.22 points; blame attribution showed the Planner dominates failure (error rate 7.35% for the best model vs 40.49% for the worst) at a cost of 2-3x spend and 8-10x latency.

> Without clear roles and checks, errors compound across stages and accuracy
> falls below a competent single model.
>
> Barrak (2025), p. 5

### 5. Automated Black-Box Testing: A Comparative Study of LLM Agent Architectures and Prompt Engineering

Arnaudo, A., Coppola, R., Giobergia, F., Morisio, M., Nguyen, V.-T., Chen, E., Ma, X., Ji, X., & Mai, M.-T. (2026). Automated Black-Box Testing: A Comparative Study of LLM Agent Architectures and Prompt Engineering. 2026 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW), 29-36. https://doi.org/10.1109/icstw72326.2026.00018

**Relevance**: core · **Rigor**: 0.88 · **Peer-reviewed** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* On HumanEval black-box unit-test generation, prompt engineering rather than architecture is the primary driver: multi-agent collaborative and competitive configurations achieve marginally higher coverage (peak 99.54%) but statistically comparable execution success to a single agent (96.98% vs 96.89%) while consuming 3-4x the tokens.

> Although multi-agent architectures achieve superior test coverage —
> peaking at 99.54% — they yield an ESR comparable to single-agent
> frameworks (96.98% versus 96.89%).
>
> Arnaudo et al. (2026), p. 1

> Crucially, this comes at the expense of a threefold to fourfold increase
> in token expenditure.
>
> Arnaudo et al. (2026), p. 1

### 6. Comparing Single-Agent and Multi-Agent Strategies in LLM-Based Title-Abstract Screening

Radeva, I., Noncheva, T., Doukovska, L., & Popchev, I. (2026). Comparing Single-Agent and Multi-Agent Strategies in LLM-Based Title-Abstract Screening. https://doi.org/10.20944/preprints202603.2107.v1

**Relevance**: core · **Rigor**: 0.83 · **Preprint (not peer reviewed)** · **Design**: empirical · **Baseline/control**: present

*Contribution (paraphrase):* Across five coordination strategies and four 7-8B open-source models, a single-agent baseline with the best-matched model in few-shot mode outperformed every multi-agent alternative (recall 100%, precision 70.4%, F1 82.6%, WSS@95 43.4%), indicating model selection outweighs coordination strategy at this parameter scale.

> Multi-agent strategies introduced coordination overhead without measurable
> benefit under the conditions of this study.
>
> Radeva et al. (2026), p. 24

### 7. Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Accuracy, Reliability, and Latency

Ashrafi, N., Bouktif, S., & Mediani, M. (n.d.). Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Accuracy, Reliability, and Latency. 2025 IEEE 19th International Conference on Application of Information and Communication Technologies (AICT). https://ieeexplore.ieee.org/document/11268754/

**Relevance**: core · **Rigor**: 0.83 · **Peer-reviewed** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* Across 19 LLMs, runtime execution debugging alone captured almost all of the accuracy benefit (63.86% vs 64.82% for the full Analyst-Coder-Tester plus debugger chain, a statistically insignificant 0.96% gap), while adding agents multiplied latency (7.68 to 68.42 minutes) and degraded robustness under expanded test coverage, leading the authors to recommend simple agentic systems with debugging over complex multi-agent architectures.

> AC and ACT showed substantial robustness drops (129.27 and 118.51),
> showing that agentic interaction introduces fragility.
>
> Ashrafi et al. (n.d.), p. 5

### 8. Towards Effective GenAI Multi-Agent Collaboration: Design and Evaluation for Enterprise Applications

Shu, R., Das, N., Yuan, M., Sunkara, M., & Zhang, Y. (2024). Towards Effective GenAI Multi-Agent Collaboration: Design and Evaluation for Enterprise Applications. arXiv preprint. https://doi.org/10.48550/arxiv.2412.05449

**Relevance**: core · **Rigor**: 0.71 · **Preprint (not peer reviewed)** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* A hierarchical supervisor/specialist collaboration framework reached 90% goal success rate across three enterprise domains, while an equivalently tool-equipped single agent regressed by up to 37 absolute points (0.53 vs 0.90 in the software-development domain), with single-agent trajectories showing more tool-parameter hallucination and incorrect tool choice; the gain was bought with substantially higher latency (168.7s vs 52.6s per session in the software domain).

> In the single-agent setting, we observe an absolute regression of up to
> 37%.
>
> Shu et al. (2024), p. 11

### 9. Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation

Xu, Q., Wang, G., Briand, L., & Liu, K. (2026). Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3803418

**Relevance**: core · **Rigor**: 1.00 · **Peer-reviewed** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* CANDOR decomposes JUnit test generation across specialized agents (Initializer, Planner, Tester, Inspector, Requirement Engineer, Panelist, Interpreter, Curator) and shows that a panel-discussion consensus over multiple reasoning LLMs is what suppresses oracle hallucination: ablating the panel costs 0.067-0.086 oracle correctness, and consensus-by-reasoning beats plain majority voting.

> However, we found that these single-LLM approaches fall short on complex
> tasks, such as unit test generation.
>
> Xu et al. (2026), p. 18

### 10. Small LLMs Are Weak Tool Learners: A Multi-LLM Agent

Shen, W., Li, C., Chen, H., Yan, M., Quan, X., Chen, H., Zhang, J., & Huang, F. (2024). Small LLMs Are Weak Tool Learners: A Multi-LLM Agent. arXiv preprint, 16658-16680. https://doi.org/10.18653/v1/2024.emnlp-main.929

**Relevance**: core · **Rigor**: 0.96 · **Preprint (not peer reviewed)** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* Decomposing a tool-use agent into separately fine-tuned planner, caller, and summarizer LLMs raises the ceiling of a single LLM: alpha-UMi with a 7B backbone outperforms the 13B single-LLM baseline, and hallucination on ToolBench drops from about 2.3% to 0.37-0.57%, but the gain requires a two-stage global-to-local fine-tuning strategy, since naive per-subtask multi-LLM training underperforms the single-LLM baseline on API-calling metrics.

> These observations suggest that the key factor contributing to the success
> of α-UMi lies in its ability to surpass the performance upper-bound of
> Single-LLM.
>
> Shen et al. (2024), p. 8

### 11. AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering

Kumar, R., Ali, W., Ahmed, J., Ali, N. I., & Usman, S. (2026). AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering. arXiv preprint. https://doi.org/10.48550/arxiv.2604.13120

**Relevance**: core · **Rigor**: 0.54 · **Preprint (not peer reviewed)** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* A five-role pipeline (Planner, Coder, Tester, Debugger, Critic) with mandatory sandboxed execution of every patch resolves 40.0% of SWE-bench Lite tasks versus 14.0% for a same-model single-agent baseline and 12.0% for ReAct. Ablations attribute the gain jointly to execution feedback (Tester-Debugger loop) and role decomposition, at roughly 2.7x the per-task API cost.

> AGENTFORGE achieves 40.0% task resolution, outperforming the single-agent
> baseline by +26.0% and the ReAct baseline by +28.0%.
>
> Kumar et al. (2026), p. 7

### 12. Evaluating large language model agents for automation of atomic force microscopy

Mandal, I., Soni, J., Zaki, M., Smedskjær, M. M., Wondraczek, K., Wondraczek, L., Gosvami, N. N., & Krishnan, N. M. A. (2025). Evaluating large language model agents for automation of atomic force microscopy. Nature Communications, 16(1), 9104-9104. https://doi.org/10.1038/s41467-025-64105-7

**Relevance**: core · **Rigor**: 0.88 · **Peer-reviewed** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* On AFMBench the multi-agent AILA configuration beat direct single-agent tool integration for GPT-4o (70% vs 58% success) but made no measurable difference for weaker models, and the authors document 'sleepwalking', where agents take unauthorised actions beyond their instructions, as a distinct instruction-adherence failure mode separate from code-generation errors.

> In one of the four recorded errors, GPT-4o exceeded its designated
> operational limits, performing actions that were not authorized by the
> provided guidelines.
>
> Mandal et al. (2025), p. 6

### 13. Understanding multi-agent LLM frameworks: A unified benchmark and experimental analysis

Orogat, A., Rostam, A., & Mansour, E. (2026). Understanding multi-agent LLM frameworks: A unified benchmark and experimental analysis. arXiv preprint. https://arxiv.org/abs/2602.03128

**Relevance**: core · **Rigor**: 0.79 · **Preprint (not peer reviewed)** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* Under a fixed LLM and identical tasks, framework-level architectural choices alone drive over 100x latency differences, up to 30% planning accuracy loss, and coordination success collapsing from above 90% to below 30%, indicating multi-agent behavior is governed by execution semantics and interface design rather than model quality.

> Our results show that framework-level design choices alone can increase
> latency by over 100×, reduce planning accuracy by up to 30%, and lower
> coordination success from above 90% to below 30%.
>
> Orogat et al. (2026), p. 1

### 14. A Critical Review and Evaluation of LLMs for RTL Generation

Ravindran, A., Patra, A., Babaey, V., & Purini, S. (2026). A Critical Review and Evaluation of LLMs for RTL Generation. IEEE Access, 14, 28522-28539. https://doi.org/10.1109/access.2026.3665894

**Relevance**: core · **Rigor**: 0.83 · **Peer-reviewed** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* Across VerilogEvalV2 and RTLLM-v2.0, frontier models paired with a single-agent ReAct reflection loop and simulator feedback reached 89.74% and 96.08%, matching or exceeding prior multi-agent orchestration and fine-tuned RTL pipelines; the authors read this as benchmark saturation rather than as evidence that multi-agent specialization is unnecessary in general.

> This suggests a shift in the evaluation landscape: stronger base models
> plus minimal iterative refinement can match more elaborate pipelines,
> raising the bar for benchmark design and analysis going forward.
>
> Ravindran et al. (2026), p. 8

### 15. A Multi-Agent LLM Framework for Automated Software Testing

Li, Y. (2026). A Multi-Agent LLM Framework for Automated Software Testing. Transactions on Computing Science, 2(2), 1-25. https://doi.org/10.63808/tcs.v2i2.447

**Relevance**: core · **Rigor**: 0.71 · **Peer-reviewed** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* A four-agent testing framework reaches 55.0% differential defect detection on QuixBugs versus 37.5% for a same-model single-agent baseline, and the ablation attributes that 17.5-point advantage to role decomposition rather than to the dedicated diagnostic agent; the conventional unconditional criterion overstates detection by 35 points (90.0% vs 55.0%).

> Role decomposition is supported: the single-agent condition, run with the
> same model and the same budget, detects 17.5 fewer points under the
> differential criterion.
>
> Li (2026), p. 19

### 16. Evaluation of the Choice of LLM in a Multi-Agent Solution for GUI-Test Generation

Tomic, S., Alégroth, E., & Isaac, M. (2025). Evaluation of the Choice of LLM in a Multi-Agent Solution for GUI-Test Generation. 2025 IEEE Conference on Software Testing, Verification and Validation (ICST), 487-497. https://doi.org/10.1109/icst62969.2025.10989038

**Relevance**: core · **Rigor**: 0.92 · **Peer-reviewed** · **Design**: empirical · **Baseline/control**: partial

*Contribution (paraphrase):* Testing 27 permutations of three local LLMs across three agent roles in the PathFinder GUI-testing multi-agent system, the hypothesis that heterogeneous specialist LLMs beat a single shared LLM was rejected per-site (homogeneous constellations won on specific websites) and only weakly supported across sites (best mixed 0.703 F1 vs 0.660 for all-Gemma2), a marginal difference.

> We cannot accept our hypothesis H1, as one-model MALLMs tend to perform
> better on specifc websites.
>
> Tomic et al. (2025), p. 9

### 17. A Comparative Empirical Evaluation of Single-Agent and Multi-Agent LLM Prompting Strategies for Automated Formative Feedback in Education

Lai, J., & Li, Z. (2026). A Comparative Empirical Evaluation of Single-Agent and Multi-Agent LLM Prompting Strategies for Automated Formative Feedback in Education. Journal of Intelligence and Engineering Technology, 1(2), 29-38. https://doi.org/10.70393/6a696574.343135

**Relevance**: core · **Rigor**: 0.71 · **Peer-reviewed** · **Design**: empirical · **Baseline/control**: present

*Contribution (paraphrase):* A tri-role multi-agent pipeline (Evaluator, Student Simulator, Reviewer) produced the highest composite quality (CQS 4.21/5) and lowest over-praise and hallucination rates, but consumed roughly 4.6x the tokens of a zero-shot single agent, while a chain-of-thought single agent reached 86.5% of the top score at 32.5% of its token cost.

> The S4 strategy consumed approximately 4.6 times the tokens of S1,
> translating to proportionally higher API costs.
>
> Lai & Li (2026), p. 7

### 18. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing

Chebolu, I., Mallick, A., & Rana, H. (2026). SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing. arXiv preprint. https://doi.org/10.48550/arxiv.2602.04418

**Relevance**: core · **Rigor**: 0.79 · **Preprint (not peer reviewed)** · **Design**: case-study · **Baseline/control**: present

*Contribution (paraphrase):* In smart-contract auditing, a decentralized multi-agent design outperformed a centralized scheduler that implemented identical risk-aware planning and repair logic (F1 0.87 vs 0.83), with the advantage concentrated under injected failures rather than under normal conditions, at a measured coordination overhead of 4.2%.

> SPEAR achieves higher overall effectiveness than all baselines, including
> a centralized scheduler that implements identical planning and repair
> logic.
>
> Chebolu et al. (2026), p. 12

### 19. Triangle: Empowering Incident Triage with Multi-Agent

Yu, Z., Fang, A., Ma, M., Walia, J. S., Zhang, C., Chi, S., Li, Z., Chintalapati, M., Zhang, X., Wang, R., Bansal, C., Rajmohan, S., Lin, Q., Zhang, S., Pei, D., & He, P. (2025). Triangle: Empowering Incident Triage with Multi-Agent. https://doi.org/10.1109/ase63991.2025.00062

**Relevance**: core · **Rigor**: 0.88 · **Peer-reviewed** · **Design**: empirical · **Baseline/control**: present

*Contribution (paraphrase):* In a production cloud deployment, Triangle's multi-role negotiation is the single most load-bearing component: removing multi-agent negotiation costs about 12 points of hop-1 accuracy (54.7% -> 42.8%) and 21 points at hop 5 (91.7% -> 70.4%), more than removing semantic distillation, while automated team-information enrichment matters most at higher hop counts.

> The most substantial performance degradation is observed when the
> multi-agent negotiation mechanism is removed(w/o MAT).
>
> Yu et al. (2025), p. 8

### 20. Autonomous Microscopy Experiments through Large Language Model Agents

Mandal, I., Soni, J., Zaki, M., Smedskjær, M. M., Wondraczek, K., Wondraczek, L., Gosvami, N. N., & Krishnan, N. M. A. (2024). Autonomous Microscopy Experiments through Large Language Model Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2501.10385

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: benchmark-study

*Contribution (paraphrase):* In a controlled ablation on the same task subset, the role-specialized multi-agent configuration beat direct single-agent tool integration only for the strongest model (GPT-4o, 70% vs 58% success); weaker models showed minimal difference because they failed the cross-domain coordination the topology was meant to exploit, and single-agent architectures retained the compute and latency advantage.

> These findings indicate that while computational efficiency favours
> single-agent implementations, the enhanced coordination capabilities of
> multi-agent frameworks provide measurable performance gains for advanced
> models capable of complex reasoning.
>
> Mandal et al. (2024), p. 9

### 21. Multi-Agent Assisted Automatic Test Generation for Java JSON Libraries

Wang, S., Zhong, Z., Wen, S., & Liu, Y. (2025). Multi-Agent Assisted Automatic Test Generation for Java JSON Libraries. https://doi.org/10.1109/apsec66846.2025.00064

**Relevance**: core · **Rigor**: 0.92 · **Peer-reviewed** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* JSONATG's three-role decomposition (Code Summarizer, Test Programmer, Test Validator) with domain-specific mutation rules outperformed ChatTester and ChatUnitest on the large, complex fastjson classes and found 59 real bugs for $25, but the ablation shows the agent-written mutation rules actually reduced coverage on four of six classes because more generated tests failed to compile, and the Test Validator was near chance at classifying tests that throw library-defined exceptions.

> JSONATG achieves higher coverage on complex and large classes in the Java
> JSON library, demonstrating superior capability in exercising critical
> components of the library under test.
>
> Wang et al. (2025), p. 7

### 22. INTERVENOR: Prompting the Coding Ability of Large Language Models with the Interactive Chain of Repair

Wang, H., Liu, Z., Wang, S., Cui, G., Ding, N., Liu, Z., & Ge, Y. (2024). INTERVENOR: Prompting the Coding Ability of Large Language Models with the Interactive Chain of Repair. https://doi.org/10.18653/v1/2024.findings-acl.124

**Relevance**: core · **Rigor**: 0.88 · **Peer-reviewed** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* Splitting repair into a Code Teacher that reads compiler bug reports and a Code Learner that applies the resulting Chain-of-Repair beat GPT-3.5 by roughly 18% on code generation and 4.3% on translation, and outperformed both self-repair (Self-Debug, Self-Refine) and multi-agent Self-Collaboration, showing external compiler grounding matters more than agent count.

> The experimental results show that code repair is more effective than
> directly prompting LLMs to generate codes.
>
> Wang et al. (2024), p. 6

### 23. CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society

Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2303.17760

**Relevance**: core · **Rigor**: 0.83 · **Preprint (not peer reviewed)** · **Design**: empirical · **Baseline/control**: present

*Contribution (paraphrase):* Two role-playing agents driven by inception prompting beat a gpt-3.5-turbo single-shot solution in 76.3% of human comparisons and 73-76% of GPT-4 comparisons, but autonomous cooperation exhibited four recurring coordination failures: role flipping, instruction repetition, flake replies, and infinite message loops.

> Examples we encountered in our preliminary analysis include role flipping,
> assistant repeating instructions, flake replies, and infinite loop of
> messages.
>
> Li et al. (2023), p. 2

### 24. Beyond Task Completion: An Assessment Framework for Evaluating Agentic AI Systems

Akshathala, S., Adnan, B., Ramesh, M., Vaidhyanathan, K., Muhammed, B., & Parthasarathy, K. (2026). Beyond Task Completion: An Assessment Framework for Evaluating Agentic AI Systems. AGENT '26: Proceedings of the 2026 International Workshop on Agentic Engineering, 9-17. https://doi.org/10.1145/3786167.3788414

**Relevance**: core · **Rigor**: 0.92 · **Peer-reviewed** · **Design**: case-study · **Baseline/control**: present

*Contribution (paraphrase):* In a production CloudOps deployment, binary task-completion metrics were identical between baseline and framework evaluation while pillar-specific metrics exposed substantial hidden behavioural failures (S1 had 100% tool sequencing but 33% policy adherence; S2 completed the task with 13.1% memory recall), and the multi-agent scenario S3 had by far the worst tool-orchestration failure rate (7.67 average failures) and the only environment guardrail violations.

> Memory failures increased with scenario complexity, while Environment
> violations appeared only in multi-agent scenarios where production states
> changed despite guardrails.
>
> Akshathala et al. (2026), p. 8

### 25. Towards Engineering Multi-Agent LLMs: A Protocol-Driven Approach

Mao, Z., Keung, J., Zhang, F., Liu, S., Wang, Y., & Li, J. (2025). Towards Engineering Multi-Agent LLMs: A Protocol-Driven Approach. https://doi.org/10.1109/apsec66846.2025.00100

**Relevance**: core · **Rigor**: 0.62 · **Peer-reviewed** · **Design**: benchmark-study · **Baseline/control**: present

*Contribution (paraphrase):* SEMAP treats multi-agent LLM failure as a classical software-engineering design defect (missing contracts, untyped interfaces, ungated transitions) and shows that adding behavioural contracts, typed messaging, and verification-gated lifecycle FSMs cuts MAST-classified failures by up to 69.6% on function-level development and 47.4% on Python vulnerability detection relative to a MetaGPT baseline.

> Despite their conceptual appeal, current multi-agent LLM systems often
> under-perform in practice, as evidenced by high failure rates on SE tasks.
>
> Mao et al. (2025), p. 1

### 26. MULTI-AGENT SYSTEM FOR AUTOMATED CODE REVIEWS

Premasundera, S. (2025). MULTI-AGENT SYSTEM FOR AUTOMATED CODE REVIEWS. Tampere University Institutional Repository (Tampere University). https://trepo.tuni.fi/bitstream/handle/10024/232334/PremasunderaSavidya.pdf?sequence=2

**Relevance**: core · **Rigor**: 0.54 · **Preprint (not peer reviewed)** · **Design**: case-study · **Baseline/control**: present

*Contribution (paraphrase):* Four domain-specialized review agents (Readability, Refactoring, Performance, Security) plus a Consensus Agent produced broader category coverage, higher semantic diversity, lower internal redundancy, and more stable confidence than a single monolithic LLM on the same pull request, with only moderate inter-agent agreement indicating complementary rather than duplicated coverage.

> The MAS not only broadens coverage but also enhances semantic richness and
> reduces redundancy in its outputs.
>
> Premasundera (2025), p. 44

### 27. Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code

Haseeb, M. (2025). Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code. arXiv preprint. http://arxiv.org/abs/2508.08322v1

**Relevance**: core · **Rigor**: 0.17 · **Preprint (not peer reviewed)** · **Design**: case-study · **Baseline/control**: none

*Contribution (paraphrase):* On five non-trivial tasks in a ~180K-line Next.js repository, a context-engineered hub-and-spoke multi-agent Claude Code system succeeded on 4/5 tasks (80%) without human correction versus 2/5 (40%) for a single-agent Claude baseline, at roughly 3-5x the token cost; the baseline's failures were dominated by missed cross-file edits and hallucinated APIs.

> Out of 5 tasks attempted (including feature additions and bug fixes of
> varying complexity), our system achieved a successful outcome (defined by
> passing all tests and meeting the acceptance criteria) on 4 tasks (80%)
> without any human corrections.
>
> Haseeb (2025), p. 10

### 28. Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories

Bouzenia, I., & Pradel, M. (2025). Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 2846-2857. https://doi.org/10.1109/ase63991.2025.00234

**Relevance**: core · **Rigor**: 0.96 · **Peer-reviewed** · **Design**: empirical · **Baseline/control**: partial

*Contribution (paraphrase):* Across 120 trajectories and 2,822 LLM interactions from three single-agent SE systems, failed runs are distinguished by repetitive non-adaptive action cycles, result-insensitive next actions, and rare but costly thought-action misalignments; even a single misalignment correlated with failure or greatly increased cost (one bug extended from iteration 6 to iteration 38).

> Repetition wastes iterations and may induce unproductive loops, as also
> observed in RQ2.
>
> Bouzenia & Pradel (2025), p. 9

### 29. A Characterization Study of Bugs in LLM Agent Workflow Orchestration Frameworks

Xue, Z., Zhao, Y., Wang, S., Chen, K., & Wang, H. (2025). A Characterization Study of Bugs in LLM Agent Workflow Orchestration Frameworks. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 3369-3380. https://doi.org/10.1109/ase63991.2025.00278

**Relevance**: core · **Rigor**: 0.88 · **Peer-reviewed** · **Design**: empirical · **Baseline/control**: none

*Contribution (paraphrase):* Across 1,026 manually annotated bugs in LangChain, LlamaIndex, and Haystack, agent orchestration frameworks depart from traditional software bug profiles: Incorrect Functionality (315) nearly matches Crash (326), a new Unexpected Output category accounts for 16.5%, and the authors conclude that deterministic testing and static analysis are structurally inadequate for these probabilistic, heavily integrated systems.

> Moreover, we identified Unexpected Output as a significant new symptom
> category (169 occurrences, 16.5%) uniquely relevant to LLM agent
> frameworks, reflecting their probabilistic and generative nature.
>
> Xue et al. (2025), p. 9

### 30. A Survey for LLM Agent Trajectory Analysis: From Failure Attribution to Enhancement

Wang, J., Wang, Y., Chen, M., Xie, X., Chen, C., Mu, F., Liu, Z., & Wang, Q. (2026). A Survey for LLM Agent Trajectory Analysis: From Failure Attribution to Enhancement. IEEE Transactions on Software Engineering, 1-23. https://doi.org/10.1109/tse.2026.3717765

**Relevance**: core · **Rigor**: 0.62 · **Peer-reviewed** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* Surveying 55 papers on LLM agent trajectory analysis, the authors show automated failure attribution remains weak: step-level attribution accuracy on the Who&When benchmark spans only about 25-52%, with agent-level accuracy substantially higher, and benchmark diversity is the field's bottleneck. Multi-agent failure taxonomies (MAST) attribute failures to specification issues, inter-agent misalignment and task verification.

> In terms of reported accuracy, on the Who&When benchmark, reported
> step-level attribution accuracy varies substantially across techniques,
> ranging from about 25% [11] to 52% [39].
>
> Wang et al. (2026), p. 12

### 31. Exploring Autonomous Agents: A Closer Look at Why They Fail When Completing Tasks

Lu, R., Li, Y., & Huo, Y. (2025). Exploring Autonomous Agents: A Closer Look at Why They Fail When Completing Tasks. https://doi.org/10.1109/ase63991.2025.00330

**Relevance**: core · **Rigor**: 0.75 · **Peer-reviewed** · **Design**: benchmark-study · **Baseline/control**: partial

*Contribution (paraphrase):* Three popular planner/code-generator/executor agent frameworks completed only about half of 34 programmable tasks, and a 19-cause three-tier failure taxonomy (planning, execution, response generation) derived from 104 failures across 204 runs showed the most common problems were improper task decomposition, failed self-refinement loops, and context/format issues rather than raw model weakness; the weaker GPT-4o mini backbone often beat GPT-4o because of GPT-4o 'overthinking'.

> Surprisingly, the smaller GPT-4o-mini outperforms, especially in web
> crawling tasks, indicating that simpler models can remain highly
> competitive.
>
> Lu et al. (2025), p. 3

### 32. Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering

Seyedghorban, Z., Klimov, E., van Deursen, A., Panichella, A., & Ozkan, B. K. (2026). Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering. 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST), 211-215. https://doi.org/10.1109/icst69053.2026.00037

**Relevance**: core · **Rigor**: 0.75 · **Peer-reviewed** · **Design**: empirical · **Baseline/control**: partial

*Contribution (paraphrase):* Trace-aligned fault injection shows perturbations at inter-agent communication boundaries propagate more damagingly than equivalent perturbations at single LLM calls: in ChatDev a 1000 ms A2A delay produced 59.2x mean runtime amplification versus 48.1x for an LLM delay, and 1.295x vs 1.053x in a minimal two-agent demo.

> Overall, these results highlight that in a multi-phase, message-heavy
> workflow, the runtime impact of small injected delays can be magnified
> dramatically
>
> Seyedghorban et al. (2026), p. 4

### 33. Understanding Conversational Patterns in Multi-agent Programming: A Case Study on Fibonacci Game Development

Basu, S., Kjellberg, V., Sun, S., Haraldsson, B., Babu, M. A. A., Meding, W., Fotrousi, F., & Staron, M. (2026). Understanding Conversational Patterns in Multi-agent Programming: A Case Study on Fibonacci Game Development. AIware '26: Proceedings of the 3rd ACM International Conference on AI-Powered Software, 238-247. https://doi.org/10.1145/3805760.3814914

**Relevance**: core · **Rigor**: 0.67 · **Peer-reviewed** · **Design**: case-study · **Baseline/control**: none

*Contribution (paraphrase):* Across 12 Designer:Programmer agent pairs from 7 open-source LLMs on a single C programming task, convergence, role alignment and compilation success were not correlated: only DeepSeek-R1:DeepSeek-R1 converged and sustained a correct solution, several pairs achieved 100% compilation while never reaching a correct solution, and pairs that diverged after 3, 21 or 69 iterations never recovered.

> This suggests that once a correct solution emerges, it tends to be
> preserved for a bounded number of iterations (≤ 69 in our study), while
> later recovery is unlikely.
>
> Basu et al. (2026), p. 8

### 34. Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems

Qi, S., Ma, J., Xing, R., Guo, W., Huang, X., Gao, Z., Deng, J., Liu, J., Zhang, L., Wei, B., Yang, B., Wang, P., Sun, J., Tao, J., Wu, Y., Liu, H., Yao, Y., & Liu, T. (2026). Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems. arXiv preprint. https://arxiv.org/abs/2605.14892

**Relevance**: core · **Rigor**: 0.54 · **Preprint (not peer reviewed)** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* Role heterogeneity buys division of labour but raises interdependence, so specialized multi-agent systems become more sensitive to interface mismatches, cascading error propagation, and coordination overhead; the survey argues failure attribution is unsettled because the point where an anomaly becomes observable rarely coincides with its origin.

> As role diversity increases, so does interdependence among agents, making
> the system more sensitive to interface mismatches, cascading errors, and
> coordination overhead.
>
> Qi et al. (2026), p. 37

### 35. Iterative Audit Convergence in LLM-Managed Multi-Agent Systems: A Case Study in Prompt-Engineering Quality Assurance

Calboreanu, E. (2026). Iterative Audit Convergence in LLM-Managed Multi-Agent Systems: A Case Study in Prompt-Engineering Quality Assurance. Software, 5(2), 26. https://doi.org/10.3390/software5020026

**Relevance**: core · **Rigor**: 0.88 · **Peer-reviewed** · **Design**: case-study · **Baseline/control**: partial

*Contribution (paraphrase):* Iterative full-scope LLM auditing of a seven-lane multi-agent prompt-specification surface surfaced 51 defects over nine non-monotonic rounds; cross-lane data-contract defects were undetectable by single-file review by construction and only appeared once multi-file context loading was enabled.

> By construction, single-file review cannot detect cross-lane data-contract
> issues; in this study every cross-lane defect surfaced only after
> multi-file context loading was enabled.
>
> Calboreanu (2026), p. 16

### 36. SE-Blackboard: A Shared-State Architecture for Multi-Agent Software Engineering Pipelines

Liu, E. (2025). SE-Blackboard: A Shared-State Architecture for Multi-Agent Software Engineering Pipelines. IEEE Access. https://doi.org/10.5281/zenodo.18911614

**Relevance**: supporting · **Peer-reviewed** · **Design**: benchmark-study

*Contribution (paraphrase):* Holding the agent pipeline fixed and varying only the communication architecture, a shared-state blackboard raises Coder-stage information fidelity by 62% and correct file targeting by 27.5 percentage points over message passing, yet end-to-end resolve rate improves only 4 points because all configurations converge to a ~22% conditional resolve rate once the right file is found. The bottleneck is the LLM's intrinsic diff-generation ability, not information quality or tool access, and the blackboard's gains cost 2.17x tokens and 1.61x latency.

> Once the correct file is identified, however, all configurations converge
> to a ∼22% conditional resolve rate, revealing a downstream bottleneck in
> LLM diff generation.
>
> Liu (2025), p. 1

### 37. ATeam: Governance-Aware LLM-Assisted Software Sustaining Engineering for Enterprise Systems

Vella, S., Ferworn, A., & Sharieh, M. (2026). ATeam: Governance-Aware LLM-Assisted Software Sustaining Engineering for Enterprise Systems. 2026 6th International Conference on Electrical, Computer and Energy Technologies (ICECET), 1-6. https://doi.org/10.1109/icecet65726.2026.11633274

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* In a controlled comparison on 24 IEEE 14764 maintenance tasks over a seven-service microservice testbed, governed template-driven execution beat both an AutoGPT-style structured-reasoning agent and unconstrained prompting with huge effect sizes, while the difference between the agentic baseline and plain prompting was statistically negligible. This is direct evidence that agentic orchestration by itself does not improve sustaining-engineering outcomes; decomposition, dependency analysis and approval gates do.

> The evidence suggests that governance, rather than agentic execution
> alone, is the primary determinant of reliable enterprise software
> sustaining engineering.
>
> Vella et al. (2026), p. 1

### 38. From benchmarks to deployment: a comprehensive review of agentic AI evaluation

Kehkashan, T., Abdullah, M., Al-Shamayleh, A. S., Ivković, N., Ismail, N. A., Ahmad, S. S. S., Rehman, A., & Akhunzada, A. (2026). From benchmarks to deployment: a comprehensive review of agentic AI evaluation. Artificial Intelligence Review, 59(8). https://doi.org/10.1007/s10462-026-11571-0

**Relevance**: core · **Rigor**: 0.50 · **Peer-reviewed** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* A critical review of 15 agent benchmarks finds evaluation methodology, not model capability, is the binding constraint on deployment: 0/15 score safety or security, 0/15 include cost-efficiency in the primary protocol, 13/15 rely solely on binary success, and no benchmark exceeds 50% on the authors' deployment-readiness rubric.

> Multi-agent systems bring about coordination failures, emergent behavior
> and dynamics of interaction that cannot be seen in single-agent
> benchmarks.
>
> Kehkashan et al. (2026), p. 43

### 39. Demystifying LLM-Based Software Engineering Agents: A Review of Capabilities, Benchmarks, and Failure Modes

Demystifying LLM-Based Software Engineering Agents: A Review of Capabilities, Benchmarks, and Failure Modes. (n.d.). https://journal.duc.edu.iq/index.php/djst/article/view/828

**Relevance**: core · **Rigor**: 0.42 · **Peer-reviewed** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* A critical review of 20+ primary studies frames an 'Agentless Paradox': structured non-agentic pipelines match or beat autonomous single- and multi-agent systems on SWE-bench at up to an order of magnitude lower cost (Agentless 1.0 27.3% at $0.34/issue vs SWE-search MCTS 23.0% at ~$4.00), and base-model choice explains more variance than architecture; the review also warns that multi-agent debate reinforces rather than corrects correlated errors when all agents share one base model.

> When many agents make the same mistake, we call it a correlated error.
>
> Demystifying LLM-Based Software Engineering Agents (n.d.), p. 4

### 40. Large Language Model-Based Agents for Software Engineering: A Survey

Liu, J., Wang, K., Chen, Y., Peng, X., Chen, Z., Zhang, L., & Lou, Y. (2024). Large Language Model-Based Agents for Software Engineering: A Survey. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3796507

**Relevance**: core · **Rigor**: 0.79 · **Peer-reviewed** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* Surveying 124 papers, this review classifies multi-agent SE collaboration into layered, circular, star-like, tree-like, and mesh structures with unidirectional-transfer or bidirectional-chat information flow, and reports that all of these structures hit performance bottlenecks as agent count grows, with prior work showing benchmark performance saturating regardless of collaboration structure.

> The collaboration structures mentioned above may all encounter performance
> bottlenecks as the scale increases.
>
> Liu et al. (2024), p. 42

### 41. Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review

Otoum, N., & Elkhalili, N. (2026). Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review. IEEE Access, 14, 7443-7465. https://doi.org/10.1109/access.2026.3652325

**Relevance**: core · **Rigor**: 0.75 · **Peer-reviewed** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* This SLR of 61 studies (2022-2025) documents a field-wide migration from single-agent to role-specialized multi-agent architectures and asserts reliability and performance gains, but its own challenge analysis reports that inter-agent protocols are informal and non-standardised, conflict resolution is immature, and token cost scales disproportionately with system complexity.

> The complexity of a multi-agent system increases its computational costs
> disproportionately with the complexity of the system since multiple agents
> take a much larger number of tokens to interact with each other and
> require more processing time, which may render large-scale implementation
> uneconomical in practice.
>
> Otoum & Elkhalili (2026), p. 14

### 42. LLM-Based Multi-Agent Systems for Code Generation: A Multi-Vocal Literature Review

Rasheeda, Z., Waseema, M., Kemella, K.-K., Saari, M., & Abrahamsson, P. (2026). LLM-Based Multi-Agent Systems for Code Generation: A Multi-Vocal Literature Review. arXiv preprint. https://doi.org/10.5281/zenodo.21487935

**Relevance**: core · **Rigor**: 0.67 · **Preprint (not peer reviewed)** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* A multi-vocal review of 114 academic and grey-literature sources finds that reliability, security, cost and verification problems in LLM multi-agent code generation are systemic architectural weaknesses rather than isolated model failures, and that current benchmarks provide insufficient evaluation of multi-agent collaboration and coordination. The authors conclude the field is shifting from a model-centric phase to a systems-engineering phase where coordination stability, verification pipelines and cost governance dominate.

> Existing benchmarks often have limited real-world representativeness, lack
> scalability to large or long-horizon tasks, involve high computational
> costs, and provide insufficient evaluation of multi-agent collaboration
> and coordination.
>
> Rasheeda et al. (2026), p. 20

### 43. A comprehensive survey on benchmarks and solutions in software engineering of llm-empowered agentic system

Guo, J., Huang, S., Li, M., Huang, D., Chen, X., Zhang, R., Guo, Z., Yu, H., Yiu, S.-M., Lio, P., & Lam, K.-Y. (2025). A comprehensive survey on benchmarks and solutions in software engineering of llm-empowered agentic system. arXiv preprint. https://arxiv.org/abs/2510.09721

**Relevance**: core · **Rigor**: 0.42 · **Preprint (not peer reviewed)** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* Connecting 50+ benchmarks to prompt-based, fine-tuning-based and agent-based solution paradigms across 150+ papers, the survey argues that existing multi-agent SE frameworks rely on simplistic coordination (sequential pipelines or centralized orchestration) that cannot express real development workflows, and that no benchmarks measure coordination efficiency or communication overhead.

> Current multi-agent frameworks often rely on simple coordination
> mechanisms such as sequential pipelines or centralized orchestration,
> which fail to capture the dynamic, iterative, and often non-linear nature
> of real software development workflows.
>
> Guo et al. (2025), p. 17

### 44. From llms to llm-based agents for software engineering: A survey of current, challenges and future

Jin, H., Huang, L., Cai, H., Yan, J., Li, B., & Chen, H. (2024). From llms to llm-based agents for software engineering: A survey of current, challenges and future. arXiv preprint. https://arxiv.org/abs/2408.02479

**Relevance**: core · **Rigor**: 0.38 · **Preprint (not peer reviewed)** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* Surveying 139 papers across six SE topics, the authors argue LLM-based agents extend single LLMs through role specialization, iterative refinement and tool integration, but that multi-agent workflow complexity introduces synchronization, state-consistency and cascading-misunderstanding problems that single LLM pipelines do not exhibit, with no unified agent definition or evaluation protocol available.

> Traditional LLMs excel at isolated tasks but face limitations due to
> constrained context awareness, insufficient feedback mechanisms, and
> minimal autonomy.
>
> Jin et al. (2024), p. 19

### 45. Designing LLM-based multi-agent systems for software engineering tasks: Quality attributes, design patterns and rationale

Cai, Y., Li, R., Liang, P., Shahin, M., & Li, Z. (2025). Designing LLM-based multi-agent systems for software engineering tasks: Quality attributes, design patterns and rationale. arXiv preprint. https://arxiv.org/abs/2511.08475

**Relevance**: core · **Rigor**: 0.75 · **Preprint (not peer reviewed)** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* Across 94 papers on LLM-based multi-agent systems for SE, Role-Based Cooperation is the dominant design pattern (44 systems, 47.4%) among 16 identified patterns, chosen mainly to improve functional correctness and modularity, while performance efficiency (51.1%) and maintainability (50.0%) are traded off against each other.

> Role-Based Cooperation is the design pattern most frequently employed
> among 16 patterns used to construct LLM-based MASs
>
> Cai et al. (2025), p. 1

### 46. Human-In-The-Loop Software Development Agents

Takerngsaksiri, W., Pasuksmit, J., Thongtanunam, P., Tantithamthavorn, C., Zhang, R., Jiang, F., Li, J., Cook, E., Chen, K., & Wu, M. (2025). Human-In-The-Loop Software Development Agents. 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP), 342-352. https://doi.org/10.1109/icse-seip66354.2025.00036

**Relevance**: core · **Rigor**: 0.83 · **Peer-reviewed** · **Design**: empirical · **Baseline/control**: partial

*Contribution (paraphrase):* A three-role human-in-the-loop agent pipeline (AI Planner, AI Coding, Human) deployed inside Atlassian JIRA performed far worse on proprietary enterprise issues than on SWE-bench Verified (30% vs 86% file-localization recall; 30% vs 45% code similarity), showing that open-source benchmark results do not transfer to enterprise contexts. Human feedback at each stage recovered usefulness: 82% of generated plans were approved, 25% of code generations became pull requests, and 59% of those merged.

> These results highlight the success of the HULA framework where human
> feedback is incorporated into practice.
>
> Takerngsaksiri et al. (2025), p. 2

### 47. Multi-Agent Software Development for Automotive Model-Based Graphical Programming

Abdalla, A. S., Thie, V., Schaub, J., Eisenbarth, M., Lee, S. H., & Andert, J. (2026). Multi-Agent Software Development for Automotive Model-Based Graphical Programming. IEEE Access. https://doi.org/10.2139/ssrn.6253838

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: benchmark-study

*Contribution (paraphrase):* On a new 38-requirement automotive Simulink benchmark, a role-specialized multi-agent pipeline with an automated test-diagnose-fix loop lifts absolute pass rate from 47.4% for a rulebook-equipped single-agent baseline (and 15.8% for raw prompting) to 73.7%, isolating iterative verification as the dominant contributor.

> Our results demonstrate a substantial improvement in generative AI
> performance: the rulebook-equipped single-agent baseline achieve only a
> 47.4% model-level pass rate, while our full multi-agent framework attains
> 73.7% across generated models.
>
> Abdalla et al. (2026), p. 1

### 48. Multi-Agent RAG Framework for Entity Resolution: Advancing Beyond Single-LLM Approaches with Specialized Agent Coordination

Muhammad, A., Mohammed, M. A., Milanova, M., Talburt, J. R., & Cakmak, M. C. (2025). Multi-Agent RAG Framework for Entity Resolution: Advancing Beyond Single-LLM Approaches with Specialized Agent Coordination. Computers, 14(12), 525. https://doi.org/10.20944/preprints202510.2382.v1

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* A four-agent LangGraph RAG pipeline for entity resolution beat a single-LLM GPT-4 baseline on accuracy (93.9% vs 86.9%) while simultaneously cutting tokens ~62%, API calls >60%, and runtime 52%, attributed to selective retrieval per agent and shared state memory that avoids redundant inference.

> The proposed framework reduced token usage by approximately 62% and API
> calls by over 60% compared to the single-LLM baseline, leading to a 52%
> decrease in average runtime.
>
> Muhammad et al. (2025), p. 18

### 49. PhishDebate: An LLM-Based Multi-Agent Framework for Phishing Website Detection

Li, W., Manickam, S., Chong, Y.-W., & Karuppayah, S. (2025). PhishDebate: An LLM-Based Multi-Agent Framework for Phishing Website Detection. arXiv preprint, 6606-6615. https://doi.org/10.1109/BigData66926.2025.11401440

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: benchmark-study

*Contribution (paraphrase):* A four-specialist debate framework with Moderator and Judge lifted accuracy from 67.00% (single-agent direct prompting) and 90.70% (single-agent chain-of-thought) to 93.90%, largely by eliminating indecisive 'uncertain' outputs, but average inference time rose from 4.7 s to 37.5 s, roughly an eightfold latency cost.

> PhishDebate outperforms both baselines across all key evaluation metrics,
> achieving the highest precision (90.57%), accuracy (93.90%), recall
> (98.00%), and F1 score (94.14%).
>
> Li, W., et al. (2025), p. 6

### 50. AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems

Yang, Y., Chai, H., & Zhang, W. (2025). AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems. https://doi.org/10.32388/ws0vim

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: benchmark-study

*Contribution (paraphrase):* A decentralized DAG-structured framework with retrieval-augmented agent evolution outperformed centralized multi-agent baselines such as MetaGPT and GPTSwarm and matched or beat strong single-agent prompting, but the heterogeneity ablation showed role/model diversity actually hurts small teams and only pays off at larger scale, and several multi-agent baselines fell far below single-agent prompting.

> With 3 agents, the fully homogeneous setting performs best, while
> introducing either model or skill diversity reduces accuracy, suggesting
> uniform reasoning is more effective in small teams.
>
> Yang et al. (2025), p. 20

### 51. Large language model-based multi-agent systems for automated foundation design: router-driven task classification and expert selection framework

Youwai, S., Phim, D., Murcia, V. G., & Onas, R. C. (2026). Large language model-based multi-agent systems for automated foundation design: router-driven task classification and expert selection framework. AI in Civil Engineering, 5(1). https://doi.org/10.1007/s43503-026-00088-8

**Relevance**: supporting · **Peer-reviewed** · **Design**: benchmark-study

*Contribution (paraphrase):* Router-driven dispatch to domain-expert agents beat both a single strong agent (95.00% vs 86.25% shallow foundations; 90.63% vs 87.50% pile design with Grok 3) and conventional fixed designer-checker multi-agent workflows by 10.0-43.75 points, while the fixed sequential multi-agent workflows actually underperformed the plain single agent, and the router configuration also had the lowest run-to-run variance.

> Perfect scores (100.00%) consistently showed zero standard deviation,
> suggesting deterministic reasoning paths when models achieve complete
> problem understanding despite the probabilistic generation process.
>
> Youwai et al. (2026), p. 18

### 52. AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges

Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges. Information Fusion, 126(3), 103599-103599. https://doi.org/10.1016/j.inffus.2025.103599

**Relevance**: supporting · **Peer-reviewed** · **Design**: survey

*Contribution (paraphrase):* The review separates tool-augmented single "AI Agents" from multi-agent "Agentic AI" and argues each paradigm has its own failure profile: single agents suffer hallucination, shallow planning and prompt brittleness, while multi-agent systems add inter-agent misalignment, error cascades, emergent unpredictability and debugging opacity. It explicitly warns that adding agents is not compositional and can degrade rather than improve performance.

> Unlike traditional modular systems, where adding components can enhance
> overall functionality, introducing additional agents in an Agentic AI
> architecture often increases cognitive load, noise, and coordination
> overhead.
>
> Sapkota et al. (2025a), p. 20

### 53. Risk analysis techniques for governed LLM-based multi-agent systems

Reid, A., O'Callaghan, S., Carroll, L., & Caetano, T. (2025). Risk analysis techniques for governed LLM-based multi-agent systems. arXiv preprint. https://doi.org/10.48550/arxiv.2508.05687

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: position

*Contribution (paraphrase):* The report argues multi-agent deployment transforms rather than merely adds to the risk landscape, naming six failure modes (cascading reliability failures, inter-agent communication failures, monoculture collapse, conformity bias, deficient theory of mind, mixed-motive dynamics), and prescribes explicit single-agent baselining to test whether coordination actually improves performance at all.

> Compare multi-agent outcomes against individual agents working on
> decomposable portions of the task to determine if coordination actually
> improves performance.
>
> Reid et al. (2025), p. 38

### 54. Multi-agent collaboration mechanisms: A survey of llms

Li, S., Jia, X., Tam, W. F., Tabaro, L., Li, Q., Liu, G., Wang, C., & Abdelmoniem, A. M. (2025). Multi-agent collaboration mechanisms: A survey of llms. arXiv preprint. https://doi.org/10.2139/ssrn.7243979

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: survey

*Contribution (paraphrase):* The survey states the multi-agent advantage is conditional on collaboration design rather than intrinsic: well-designed collaboration channels let multi-agent systems beat single agents, but a poorly designed competitive multi-agent system can be beaten by a single agent given strong prompts.

> MAS approach with suboptimal design for their competitive collaboration
> channels can be overtaken by single-agent counterpart with strong prompts.
>
> Li, S., et al. (2025), p. 21

### 55. LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns

LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns. (2026). https://www.preprints.org/manuscript/202604.2147

**Relevance**: supporting · **Peer-reviewed** · **Design**: survey

*Contribution (paraphrase):* The survey identifies an evaluation vacuum: no widely adopted benchmark targets multi-agent orchestration itself, so coordination quality, communication efficiency, delegation appropriateness, and cost are unmeasured while only task outcomes are scored. It names task duplication, contradictory outputs, and convergence failure as the three canonical coordination failure modes whose frequency rises with agent count.

> The field evaluates what agents produce, not how well they collaborate.
>
> *LLM-Based Multi-Agent Orchestration* (2026), p. 22

### 56. Benchmarking Multi-Agent LLM and Single Agent LLM Efficiency for Contextual Text Generation

Arora, K., Naim, A., & Sharma, S. (2026). Benchmarking Multi-Agent LLM and Single Agent LLM Efficiency for Contextual Text Generation. 2026 International Conference on Intelligent Systems in Engineering, Secured Systems and Cybersecurity (ICISESSC), 741-745. https://doi.org/10.1109/icisessc68634.2026.11542788

**Relevance**: supporting · **Peer-reviewed** · **Design**: benchmark-study

*Contribution (paraphrase):* A three-agent retriever/reasoner/summarizer pipeline outscored a monolithic single-agent Gemini setup on every reference-overlap metric, but the single-agent arm answered without access to the supporting explanation documents that the multi-agent retriever consumed, so the reported gap confounds retrieval augmentation with multi-agent decomposition.

> As shown in the Table 1 the Multi agent system outperform the single agent
> system in every metrics.
>
> Arora et al. (2026), p. 3

### 57. Architectural Transparency in LLM-Based Cognitive Assessment: A Multidimensional TRACE-ED Evaluation of Single-Agent and Multi-Agent Systems

Pranoto, D. C. Y., Hussien, S. B., Sabariah, S., Bandono, A., & Bahrawi, A. (2026). Architectural Transparency in LLM-Based Cognitive Assessment: A Multidimensional TRACE-ED Evaluation of Single-Agent and Multi-Agent Systems. Research Square. https://doi.org/10.21203/rs.3.rs-8985839/v1

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: empirical

*Contribution (paraphrase):* Across 900 Monte Carlo runs, splitting scoring from explanation into two agents preserved reliability (ICC(1,k) = 0.9921) and sharply raised grounding and coherence, but introduced a small statistically significant contradiction rate (0.031, d = 0.43) between the scoring and explanation agents, evidencing a measurable coordination cost of decomposition.

> Empirical evidence from 900 Monte Carlo executions confirms that
> multi-agent architectural decomposition preserves psychometric robustness
> (ICC ≈ 0.99) while substantially enhancing semantic grounding and
> coherence.
>
> Pranoto et al. (2026), p. 21

### 58. Engineering LLM Powered Multi-Agent Framework for Autonomous CloudOps

Parthasarathy, K., Vaidhyanathan, K., Dhar, R., Krishnamachari, V., Kakran, A., Akshathala, S., Arun, S., Karan, A., Muhammed, B., Dubey, S., & Veerubhotla, M. (2025). Engineering LLM Powered Multi-Agent Framework for Autonomous CloudOps. 2025 IEEE/ACM 4th International Conference on AI Engineering – Software Engineering for AI (CAIN), 201-211. https://doi.org/10.1109/cain66642.2025.00031

**Relevance**: supporting · **Peer-reviewed** · **Design**: case-study

*Contribution (paraphrase):* In an industrial CloudOps deployment, replacing a monolithic single-LLM RAG system with the six-agent MOYA framework improved every automated metric against SME gold-standard answers and cut human-reported defects from 22 to 15, with the largest gain in misclassification; despite consuming more tokens, the multi-agent system was faster end-to-end.

> MOYA Framework outperformed the monolithic baseline in key areas,
> especially in metrics focused on semantic alignment (e.g., METEOR and
> BERTScore), indicating enhanced interpretative capabilities.
>
> Parthasarathy et al. (2025), p. 8

### 59. Rethinking software engineering for agentic ai systems

Alenezi, M. (2026). Rethinking software engineering for agentic ai systems. arXiv preprint. https://arxiv.org/abs/2604.10599

**Relevance**: core · **Rigor**: 0.50 · **Preprint (not peer reviewed)** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* As LLM and agentic code generation becomes abundant, verification rather than authorship becomes the rate-limiting activity; AI-generated defects are syntactically plausible but semantically flawed, so they evade superficial review and require layered hybrid verification pipelines plus accountable human oversight.

> Unlike traditional defects, these failures often evade superficial review
> due to their syntactic plausibility.
>
> Alenezi (2026), p. 10

### 60. Assessing and Enhancing the Robustness of LLM-Based Multi-Agent Systems Through Chaos Engineering

Owotogbe, J. (2025). Assessing and Enhancing the Robustness of LLM-Based Multi-Agent Systems Through Chaos Engineering. 2025 IEEE/ACM 4th International Conference on AI Engineering – Software Engineering for AI (CAIN), 250-252. https://doi.org/10.1109/cain66642.2025.00039

**Relevance**: core · **Rigor**: 0.42 · **Peer-reviewed** · **Design**: position · **Baseline/control**: none

*Contribution (paraphrase):* This doctoral-symposium research plan argues that LLM-based multi-agent systems fail in production through emergent, cascading modes (hallucination, agent failure, inter-agent communication failure) that conventional testing does not surface, and proposes chaos engineering as the systematic robustness-testing and certification method for them.

> However, LLM-MAS in production or preproduction environments can be
> vulnerable to emergent errors or disruptions, such as hallucinations,
> agent failures, and agent communication failures.
>
> Owotogbe (2025), p. 1

### 61. A Modular Multi-Agent {LLM} Architecture for Text-to-Diagram Generation and User-Guided Refinement

Grabowski, H. (2026). A Modular Multi-Agent {LLM} Architecture for Text-to-Diagram Generation and User-Guided Refinement. e-Informatica Software Engineering Journal, 20(1), 260109. https://doi.org/10.37190/e-inf260109

**Relevance**: core · **Rigor**: 0.46 · **Peer-reviewed** · **Design**: empirical · **Baseline/control**: none

*Contribution (paraphrase):* A deterministic validation agent wrapped in a bounded generate-validate-regenerate loop acts as a robustness amplifier that homogenizes output quality across ten heterogeneous LLM backends, so models differ mainly in first-attempt stability and latency rather than in ultimate ability to satisfy the specification.

> Even for models with imperfect first-attempt behavior, the combination of
> deterministic validation and bounded regeneration significantly increases
> the final success rate.
>
> Grabowski (2026), p. 11

### 62. ALMAS: an Autonomous LLM-based Multi-Agent Software Engineering Framework

Tawosi, V., Ramani, K., Alamir, S., & Liu, X. (2025). ALMAS: an Autonomous LLM-based Multi-Agent Software Engineering Framework. 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW), 287-290. https://doi.org/10.1109/asew67777.2025.00059

**Relevance**: core · **Rigor**: 0.33 · **Peer-reviewed** · **Design**: position · **Baseline/control**: none

*Contribution (paraphrase):* A vision paper proposing ALMAS, a tiered multi-agent framework aligning agents with agile roles across the full SDLC, in which a Supervisor Agent routes sub-tasks to cheaper or stronger LLMs by complexity and Meta-RAG code summaries mitigate context limits; the framework is demonstrated only on one illustrative application-generation use case, with end-to-end evaluation explicitly deferred.

> Looking ahead, we plan to conduct end-to-end evaluations of ALMAS on a
> range of coding tasks.
>
> Tawosi et al. (2025), p. 4

### 63. The Rise of Agentic Testing: Multi-Agent Systems for Robust Software Quality Assurance

Naqvi, S., Baqar, M., & Mohammad, N. A. (2026). The Rise of Agentic Testing: Multi-Agent Systems for Robust Software Quality Assurance. arXiv preprint. https://doi.org/10.48550/arxiv.2601.02454

**Relevance**: core · **Rigor**: 0.25 · **Preprint (not peer reviewed)** · **Design**: empirical · **Baseline/control**: partial

*Contribution (paraphrase):* A three-agent closed loop (generation, execution/analysis, review/optimization) with sandboxed execution feedback raises statement coverage from 72.8% to 94.9% and valid executable tests from 64.1% to 89.3% over a single-pass LLM baseline, but the authors report non-deterministic LLM behavior, coordination latency, and context drift as persistent reliability threats.

> Although agentic systems enhance adaptability, they remain subject to
> non-deterministic LLM behavior
>
> Naqvi et al. (2026), p. 8

### 64. Transforming Software Development: A Study on the Integration of Multi-Agent Systems and Large Language Models for Automatic Code Generation

Ramírez-Rueda, R., Benítez–Guerrero, E., Mezura-Godoy, C., & Bárcenas, E. (2024). Transforming Software Development: A Study on the Integration of Multi-Agent Systems and Large Language Models for Automatic Code Generation. 2024 12th International Conference in Software Engineering Research and Innovation (CONISOFT), 11-20. https://doi.org/10.1109/conisoft63288.2024.00013

**Relevance**: core · **Rigor**: 0.38 · **Peer-reviewed** · **Design**: case-study · **Baseline/control**: none

*Contribution (paraphrase):* Repeating one identical prompt ten times through ChatDev's seven-role waterfall chat chain produced working code only 70% of the time, with 30% failing on compilation errors and three hallucination cases surviving multi-agent review, showing that cross-agent verification does not guarantee code quality.

> However, despite these filters, there were three cases of hallucinations
> where the code, although validated, was inconclusive.
>
> Ramírez-Rueda et al. (2024), p. 9

### 65. Llm-based agentic systems for software engineering: Challenges and opportunities

Tang, Y., & Runkler, T. (2026). Llm-based agentic systems for software engineering: Challenges and opportunities. arXiv preprint. https://doi.org/10.18420/se2026-ws_15

**Relevance**: core · **Rigor**: 0.38 · **Preprint (not peer reviewed)** · **Design**: survey · **Baseline/control**: none

*Contribution (paraphrase):* A concept-paper review across the SDLC argues multi-agent specialization improves modularity, tool use, and parallelism, but that current SE benchmarks measure isolated tasks and therefore cannot assess the cooperative capabilities that multi-agent systems are supposed to provide.

> Existing benchmarks have focused on individual SE tasks and exhibit
> limitations as SE projects grow in complexity.
>
> Tang & Runkler (2026), p. 8

### 66. Reducing Cost of LLM Agents with Trajectory Reduction

Xiao, Y.-A., Gao, P., Peng, C., & Xiong, Y. (2026). Reducing Cost of LLM Agents with Trajectory Reduction. Proceedings of the ACM on Software Engineering (PACMSE), Volume 3, Issue FSE, 3(FSE), 1241-1263. https://doi.org/10.1145/3797084

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* Coding-agent trajectories accumulate useless, redundant and expired content that dominates cost; removing it at inference time via a separate reflection module cuts input tokens 39.9-59.7% and total cost 21.1-35.9% while holding resolve rate within -1.0% to +2.0%, contradicting the assumed token-efficiency versus performance trade-off.

> After we further consider the computational overhead of the reflection
> module itself ($+), the final cost reduction becomes 21.1%–35.9%.
>
> Xiao et al. (2026), p. 15

### 67. Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering

Rodriguez-Cardenas, D., Li, X., Macedo, M., Mastropaolo, A., Khati, D., Tian, Y., Shao, H., & Poshyvanyk, D. (2026). Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering. FORGE '26: Proceedings of the 2026 IEEE/ACM Third International Conference on AI Foundation Models and Software Engineering, 243-248. https://doi.org/10.1145/3793655.3793716

**Relevance**: supporting · **Peer-reviewed** · **Design**: survey

*Contribution (paraphrase):* A survey plus community workshop identifies three barriers to reliable LLM-for-SE evaluation — absent software-engineering-rich datasets, ML-centric metrics, and non-standardized data pipelines — and documents that headline benchmark scores largely reflect memorization: models exceeding 70% on SWE-bench Verified fall to 23% on SWE-bench Pro. Workshop participants concluded that agentic systems specifically require process-aware, milestone-based assessment rather than binary success/failure scoring.

> This 47-point decline strongly indicates memorization rather than genuine
> repair capability.
>
> Rodriguez-Cardenas et al. (2026), p. 2

### 68. Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation

Liu, J., Xia, C. S., Wang, Y., & Zhang, L. (2023). Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2305.01210

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: benchmark-study

*Contribution (paraphrase):* Test insufficiency in the standard HumanEval suite inflates measured correctness and, more damagingly for comparative claims, reorders model rankings: augmenting tests 80x drops pass@k by up to 19.3-28.9% and flips which models appear best.

> We also surprisingly found that test insufficiency can lead to
> mis-ranking.
>
> Liu et al. (2023), p. 1

### 69. Reflexion: Language Agents with Verbal Reinforcement Learning

Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2303.11366

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: empirical

*Contribution (paraphrase):* Verbal self-reflection over an episodic memory buffer lifts a single agent to 91.0 pass@1 on HumanEval versus 80.1 for GPT-4, but the gain is bounded by the quality of the agent's self-generated tests: on MBPP Python a 16.3% false-positive test rate makes Reflexion underperform its own baseline, and ablating test generation drops accuracy below baseline (52% vs 60%).

> We acknowledge that self-reflecting code-generation agents are bound to
> their ability to write diverse, comprehensive tests.
>
> Shinn et al. (2023), p. 8

### 70. QBugLM: An Agentic Benchmarking Framework for LLM-based Quantum Software Debugging

Pham, A. B. B., Nguyen, H. T., & Usman, M. (2026). QBugLM: An Agentic Benchmarking Framework for LLM-based Quantum Software Debugging. 2026 IEEE International Conference on Quantum Software (QSW). https://ieeexplore.ieee.org/document/11662247/

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: benchmark-study

*Contribution (paraphrase):* In a multi-agent quantum debugging pipeline that separates detection (QBugFind) from repair (QBugFix) and validates with simulation-based total variation distance, iterative feedback dominates every other design choice: a single retry lifts Pass@1 from below 25% to above 80%. Elaborate prompting is not the lever — simple structured prompting beat Chain-of-Thought and ReAct for reasoning-capable models under fixed resource budgets.

> Our results show that iterative feedback is critical, as a single retry
> raises Pass@1 from below 25% to above 80%.
>
> Pham et al. (2026), p. 1

### 71. CodeQual-Agent: An Intelligent LLM-Agent Framework for Automated Software Quality Assessment with Explainable Predictions and Real-Time Analysis

Mohammad, F., Kakar, J. K., Ndong, D. R. B. B., Chas, M., & Ryu, D. (2026). CodeQual-Agent: An Intelligent LLM-Agent Framework for Automated Software Quality Assessment with Explainable Predictions and Real-Time Analysis. 2026 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW), 123-128. https://doi.org/10.1109/icstw72326.2026.00035

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* An ablation shows that removing the agent's symbolic/RAG orchestration layer collapses it to a plain LLM and costs 10 F1 points, the same magnitude as removing class balancing, evidencing that grounding LLM reasoning in deterministic static-analysis metrics is what produces the quality gain rather than the LLM alone.

> Agent Orchestration (−10.0% F1): removing symbolic and RAG grounding
> reduces the system to a standard LLM, matching SMOTE's drop at F1 = 0.820,
> which confirms that structured reasoning over static metrics is equally
> critical to balanced training data.
>
> Mohammad et al. (2026), p. 4

### 72. Trust-Aware Multi-Agent Traceability: Confidence-Calibrated Knowledge Graphs for Consistent Software Artifact Management

Essam, M., Wael, K., Hassan, A., Haitham, A., Soliman, M., Saber, S., & Habib, I. (2026). Trust-Aware Multi-Agent Traceability: Confidence-Calibrated Knowledge Graphs for Consistent Software Artifact Management. 2026 15th Mediterranean Conference on Embedded Computing (MECO). https://doi.org/10.48550/arxiv.2606.17203

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: case-study

*Contribution (paraphrase):* In a sequential multi-agent artifact pipeline, upstream low-confidence decisions propagate downstream, so the paper turns calibrated confidence into a first-class coordination signal: threshold gating, divergence detection between derivation-time and validation-time confidence, and conflict materialization as graph nodes.

> In this pipeline, errors and low-confidence decisions made by upstream
> agents propagate to downstream stages: poorly seeded traceability links
> lead to misaligned components, which in turn produce inadequate tests.
>
> Essam et al. (2026), p. 1

### 73. Safe and Scalable Collaboration in Multiagent LLM Systems: A Comprehensive Review

Hossain, E., Nipu, M. H. B., Mahmood, M. S., Hossen, M. J., & Mridha, M. F. (2026). Safe and Scalable Collaboration in Multiagent LLM Systems: A Comprehensive Review. IEEE Transactions on Systems Man and Cybernetics Systems, 1-17. https://doi.org/10.1109/tsmc.2026.3704902

**Relevance**: supporting · **Peer-reviewed** · **Design**: survey

*Contribution (paraphrase):* A four-pillar review (coordination, communication, safety, alignment) that synthesises documented multi-agent deployment failures into a cross-system taxonomy, including a coordination-overhead threshold at which added modularity becomes net-negative, semantic drift and herding in long-running systems, and collective harms absent from any individual agent.

> In frameworks of this kind, modularity can become counterproductive beyond
> a critical threshold.
>
> Hossain et al. (2026), p. 9

### 74. Large language model agents: A comprehensive survey on architectures, capabilities, and applications

Large language model agents: A comprehensive survey on architectures, capabilities, and applications. (2025). https://www.preprints.org/manuscript/202512.2119

**Relevance**: supporting · **Peer-reviewed** · **Design**: survey

*Contribution (paraphrase):* The survey reports that multi-agent groups consistently outperform single agents on complex tasks needing diverse expertise (AgentVerse, DERA on MedQA, MetaGPT at 85.9%/87.7% Pass@1 on HumanEval/MBPP), while cataloguing the coordination failure modes that role-playing introduces: conversation deviation from the original objective, role flipping between assistant and user, and unreliable termination conditions. Structured intermediate artifacts and SOP-encoded workflows are identified as the main mitigation.

> Role flipping happens when agents confuse their assigned roles, with the
> assistant providing instructions or the user attempting to execute tasks.
>
> Large language model agents (2025), p. 18

### 75. A Systematic Survey of LLM-Based Agentic AI Frameworks for Multi-Agent Coordination and Interoperability

Mohamed, N., Chakrabarti, P., & Gupta, S. K. (2026). A Systematic Survey of LLM-Based Agentic AI Frameworks for Multi-Agent Coordination and Interoperability. Journal of Smart Algorithms and Applications (JSAA), 5(1), 1-23. https://doi.org/10.66279/y29vex64

**Relevance**: supporting · **Peer-reviewed** · **Design**: survey

*Contribution (paraphrase):* A PRISMA review of 121 studies concludes that the binding constraints on LLM multi-agent systems are architectural rather than model-level: evaluation standardization, long-horizon reliability, communication security, interoperability, cost-efficient orchestration, governance, and system-level interpretability. It argues agent systems must be evaluated as holistic architectures rather than by benchmarking the base LLM in isolation.

> The literature review suggests that these challenges are beyond the
> capabilities of individual language models and include evaluation
> standardization, long-horizon reliability, security, interoperability,
> communication efficiency, governance, and interpretability.
>
> Mohamed et al. (2026), p. 18

### 76. Minimizing Response Latency in LLM-Based Agent Systems: A Comprehensive Survey

Park, G., Lee, S. C., & Park, Y. (2026). Minimizing Response Latency in LLM-Based Agent Systems: A Comprehensive Survey. IEEE Access, 14, 26140-26168. https://doi.org/10.1109/access.2026.3664226

**Relevance**: supporting · **Peer-reviewed** · **Design**: survey

*Contribution (paraphrase):* A MetaGPT-versus-ChatDev case study shows that replacing dialogue-driven coordination with a hierarchical SOP pipeline using structured document handoffs cuts end-to-end latency by roughly 29% and simultaneously improves output executability, so coordination topology is a first-order determinant of both speed and reliability.

> The data in Table 11 reveals that MetaGPT completes complex software
> development tasks in significantly less time (541 s vs. 762 s on average),
> representing a ∼ 29% reduction in end-to-end latency
>
> Park et al. (2026), p. 22

### 77. Engineering LLM-based Multi-Agent Systems: A Taxonomy of Emerging Frameworks

Di Ruscio, D., Nguyen, P. T., Di Sipio, C., Rubei, R., & Di Rocco, J. (2026). Engineering LLM-based Multi-Agent Systems: A Taxonomy of Emerging Frameworks. IEEE Software, 1-8. https://doi.org/10.1109/ms.2026.3694089

**Relevance**: supporting · **Peer-reviewed** · **Design**: survey

*Contribution (paraphrase):* A five-dimension taxonomy derived from 18 systematic studies and 14 frameworks finds that architectural primitives (agents, tools, memory, roles) are mature while monitoring, KPI/value-addition modelling, human feedback, continual evolution, benchmarking, and agent discovery are largely unimplemented, making the robustness of agentic software-engineering solutions hard to justify or reproduce.

> Governance mechanisms introduce a trade-off between flexibility and
> controllability.
>
> Di Ruscio et al. (2026), p. 6

### 78. A Comparative Study Towards Designing a Hybrid Architecture of Microservices and LLM-based Multi-Agent Systems

Yazdanian, P., Liu, Y., & Li, Z. (2025). A Comparative Study Towards Designing a Hybrid Architecture of Microservices and LLM-based Multi-Agent Systems. 2025 32nd Asia-Pacific Software Engineering Conference (APSEC), 761-772. https://doi.org/10.1109/apsec66846.2025.00077

**Relevance**: supporting · **Peer-reviewed** · **Design**: position

*Contribution (paraphrase):* A structured architectural comparison of microservice systems against LLM-based multi-agent systems, which grounds LLM-MAS failure in design and coordination rather than model quality, and proposes microservice engineering practices (layered separation of concerns, fallback agents, CI/CD test suites, RBAC) as transferable mitigations.

> The MAST taxonomy reveals that failures in LLM-MAS are primarily due to
> systematic design and coordination issues, rather than simply the
> limitation of individual LLMs or prompts.
>
> Yazdanian et al. (2025), p. 1

### 79. SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems

Becattini, M., Verdecchia, R., & Vicario, E. (2025). SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems. 2025 IEEE/ACM International Workshop New Trends in Software Architecture (SATrends), 5-8. https://doi.org/10.1109/satrends66715.2025.00006

**Relevance**: supporting · **Peer-reviewed** · **Design**: position

*Contribution (paraphrase):* SALLMA motivates a role-specialized multi-agent architecture directly from single-agent deficiencies (no task-specific tuning, no persistent memory, no ground-truth validation, static centralized deployment) and separates an Operational Layer for runtime orchestration from a Knowledge Layer holding workflow and agent metamodels.

> Software architectures based on a single LLM agent face inherent
> challenges, such as lack of task customization, lack of memory, and
> limited access to ground truth.
>
> Becattini et al. (2025), p. 1

### 80. A Multi-Agent LLM Environment for Software Design and Refactoring: A Conceptual Framework

Rajendran, V., Besiahgari, D., Patil, S. C., Chandrashekaraiah, M., & Challagulla, V. (2025). A Multi-Agent LLM Environment for Software Design and Refactoring: A Conceptual Framework. SoutheastCon 2025, 488-493. https://doi.org/10.1109/southeastcon56624.2025.10971563

**Relevance**: supporting · **Peer-reviewed** · **Design**: position

*Contribution (paraphrase):* A conceptual framework arguing that single-agent refactoring optimises one quality attribute at the expense of others, and that domain-specialized agents (performance, security, maintainability, UI/UX) negotiating through consensus or auction protocols can reconcile conflicting objectives; the evaluation is proposed rather than executed.

> Preliminary experimental design is outlined to demonstrate how multi-agent
> interactions may resolve conflicting design goals more effectively than a
> single-agent approach.
>
> Rajendran et al. (2025), p. 1

### 81. Towards Role-Based Multi-Agent LLM Systems for Software Requirements Analysis

Trifković, N., & Antović, I. (2026). Towards Role-Based Multi-Agent LLM Systems for Software Requirements Analysis. 2026 30th International Conference on Information Technology (IT), 1-4. https://doi.org/10.1109/it67293.2026.11435673

**Relevance**: supporting · **Peer-reviewed** · **Design**: position

*Contribution (paraphrase):* A conceptual role-based architecture pairs redundant small language models per SWEBOK requirements-analysis subtask under a supervisory LLM arbitrator, and its probabilistic model shows that with four independent subprocesses at per-step reliability 0.5 the overall success probability collapses to 0.0625, so acceptable end-to-end reliability requires per-step reliability above 0.90.

> However, introducing multiple agents also raises challenges related to
> coordination, validation, and decision reliability.
>
> Trifković & Antović (2026), p. 2

### 82. Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent LLM Systems

Hosseini, M.-P., Shah, A., Qureshi, S., Huang, A., Miao, C., & Wei, W. (2026). Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent LLM Systems. 2026 IEEE 50th Annual Computers, Software, and Applications Conference (COMPSAC), 179-188. https://doi.org/10.1109/compsac69091.2026.00034

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* Because the split-knowledge tasks are constructed so no single agent can solve them, the study deliberately omits any single-agent baseline and instead isolates routing: belief-guided Thompson-sampling delegation matched random delegation on success (96.65% vs 96.46%) while using 0.72x tokens, 0.83x agent calls, and 0.81x time-to-success.

> Since split-knowledge tasks are unsolvable by any single agent,
> single-agent baselines are excluded by task design.
>
> Hosseini et al. (2026), p. 5

### 83. Developing LLM-based Multi-Agent Systems in Software Engineering: A Mixed-Method Experience Report

De Oliveira, M. C. S., Ibiyo, M. O., Gianrusso, M., Di Sipio, C., Di Ruscio, D., & Nguyen, P. T. (2026). Developing LLM-based Multi-Agent Systems in Software Engineering: A Mixed-Method Experience Report. arXiv preprint. https://doi.org/10.48550/arxiv.2608.11965

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: empirical

*Contribution (paraphrase):* A mixed-method comparison of open-source MAS frameworks found good coverage of foundational MAS concepts (roles, coordination rules, message handling) but immature telemetry, benchmarking, and human-in-the-loop support; on a README summarization task no framework dominated statistically (Dify ROUGE-L 0.479 vs Semantic Kernel 0.472, p>0.05) while completion time varied significantly.

> However, despite these differences, no single framework consistently
> outperforms the others; the effectiveness largely depends on the specific
> context in which the framework will be employed.
>
> De Oliveira et al. (2026), p. 34

### 84. CAPRA: Scaling Feedback on Software Architecture Deliverables with a Multi-Agent LLM System

Becattini, M., Caselli, N., Minin, M., Verdecchia, R., & Vicario, E. (2026). CAPRA: Scaling Feedback on Software Architecture Deliverables with a Multi-Agent LLM System. arXiv preprint. http://arxiv.org/abs/2606.18976v1

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: case-study

*Contribution (paraphrase):* Adding a deterministic Evidence Anchoring step (normalized Levenshtein fuzzy matching) plus a ConsistencyManager agent to a multi-agent LLM reviewer let CAPRA satisfy 88.8% of eight rubric criteria under strict two-rater aggregation, but reliability collapsed on the interpretive 'Grounded Issues' criterion (50% strict pass, kappa 0.348), so human oversight remains necessary for subjective dimensions.

> Importantly, the Evidence Anchoring mechanism acted as a verification
> gate: findings that could not be verified against the source text were
> filtered out, substantially reducing ungrounded critiques.
>
> Becattini et al. (2026), p. 10

### 85. Automated Summarization of Software Documents: An LLM-based Multi-Agent Approach

Nguyen, D. S. H., Nguyen, M. T., Nguyen, P. T., Di Rocco, J., & Di Ruscio, D. (2026). Automated Summarization of Software Documents: An LLM-based Multi-Agent Approach. arXiv preprint, 33(2). https://doi.org/10.1007/s10515-025-00588-4

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: empirical

*Contribution (paraphrase):* A four-agent teacher-student prompt-refinement system consistently outperformed single-LLM baselines (Mixtral-8x7B, Llama-2-7b, GPT-4o, Gemma-2-2b) on ROUGE and cosine similarity for software document summarization, and an adaptive stopping strategy cut training from 620 to 260 iterations with comparable quality, though the authors note multi-agent orchestration still adds computational overhead.

> Despite the efficiency gains achieved by the dynamic iteration strategy,
> the orchestration of multiple LLM-based agents inevitably introduces
> computational overhead.
>
> Nguyen et al. (2026), p. 27

### 86. Agentic AI Modernization: Transforming Institutional Infrastructure Through Orchestrated Multi-Agent LLM Framework

Damarched, M. K. (2026). Agentic AI Modernization: Transforming Institutional Infrastructure Through Orchestrated Multi-Agent LLM Framework. Journal of Computer Science and Technology Studies, 8(4), 01-24. https://doi.org/10.32996/jcsts.2026.8.4.1

**Relevance**: supporting · **Peer-reviewed** · **Design**: case-study

*Contribution (paraphrase):* A seven-agent, on-premises AutoGen pipeline applied to 2.12M lines of COBOL, MUMPS, and PeopleSoft legacy code across three universities achieved 87% behavioural equivalence with 35% manual intervention, versus a cited single-LLM GPT-4 COBOL study where 72% of function-level translations succeeded but only 34% achieved end-to-end behavioural equivalence.

> An average behavioural equivalence of 87% was achieved, with the highest
> accuracy (91%) observed in the large research university deployment,
> confirming strong functional preservation across diverse systems
>
> Damarched (2026), p. 16

### 87. THE CAPABILITIES AND LIMITATIONS OF AI AGENTS IN SOFTWARE DEVELOPMENT

Haataja, J. (2026). THE CAPABILITIES AND LIMITATIONS OF AI AGENTS IN SOFTWARE DEVELOPMENT. Tampere University Institutional Repository (Tampere University). https://trepo.tuni.fi/bitstream/handle/10024/238728/HaatajaJustus.pdf?sequence=2

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: survey

*Contribution (paraphrase):* A literature review concluding that multi-agent role specialization buys scalability and parallelism over single agents but introduces coordination overhead and new failure modes, and that benchmark success rates systematically overstate real-world engineering value.

> Compared to single-agent systems, multi-agent architectures may improve
> scalability and specialization by distributing tasks across role-specific
> agents.
>
> Haataja (2026), p. 20

### 88. An LLM-based multi-agent framework for agile effort estimation

Bui, T.-L., Dam, H. K., & Hoda, R. (2025). An LLM-based multi-agent framework for agile effort estimation. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 1032-1043. https://doi.org/10.1109/ase63991.2025.00090

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* A role-specialized LLM agent framework for planning-poker effort estimation beats deep-learning state of the art on three of four projects after project-specific fine-tuning, but the accuracy comparison deliberately isolates a single agent, so the multi-agent discussion mechanism is evaluated only through a 12-participant human study.

> When comparing against the current state-of-the-art (SOTA) approaches,
> SEEAgent fine-tuned outperforms in three out of four projects.
>
> Bui et al. (2025), p. 7

### 89. "ENERGY STAR" LLM-Enabled Software Engineering Tools

Thakur, H., & Moin, A. (2026). "ENERGY STAR" LLM-Enabled Software Engineering Tools. arXiv preprint. https://doi.org/10.48550/arxiv.2601.19260

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: empirical

*Contribution (paraphrase):* Measuring real-time energy and inference time for RAG-augmented code generation across four LLMs (125M-7B), the effect of retrieval augmentation on energy is model-dependent rather than size-dependent: two models got cheaper, two got more expensive.

> The findings showed reductions in energy consumption when using RAG for
> GPT-2 and CodeLlama.
>
> Thakur & Moin (2026), p. 2

### 90. Developing and Evaluating an LLM-based Agent for ExplorViz Using CopilotKit

Issa, K. (2026). Developing and Evaluating an LLM-based Agent for ExplorViz Using CopilotKit. Kiel Software Engineering Research. https://doi.org/10.38071/2026-00397-5

**Relevance**: supporting · **Peer-reviewed** · **Design**: case-study

*Contribution (paraphrase):* A controlled usability study of an LLM assistant embedded in a software visualization tool found a sharp reliability split: deterministic tool-grounded actions were rated near-perfect, while open-ended agent-driven editing scored only 3.00/5 for expectation match with high variance, motivating guardrails such as staged previews, explicit edit scoping and undo support.

> Editing was rated lower and showed higher variance across participants.
>
> Issa (2026), p. 55

### 91. LLM-assisted development of Rust for high-performance bioinformatics software: practices, workflows, and boundaries

Xu, Z.-G., & Qin, G. (2026). LLM-assisted development of Rust for high-performance bioinformatics software: practices, workflows, and boundaries. Genomics Communications, 3(1), 0-0. https://doi.org/10.48130/gcomm-0026-0018

**Relevance**: supporting · **Peer-reviewed** · **Design**: case-study

*Contribution (paraphrase):* Across three real Rust migration projects the authors observed three recurring agentic-coding failure modes — layer misidentification, semantic drift in script migration, and goal substitution in agentic loops — all sharing the structure that the agent optimises observable surface features while the true defect sits one abstraction level below. The countermeasure is process rather than model: every agentic iteration must introduce at least one fresh test constraint or input fixture, otherwise the loop overfits to the static test suite.

> This is goal substitution, in which the declared goal ("make the program
> correct") is silently replaced by the operationalized subgoal ("make this
> test pass on this input").
>
> Xu & Qin (2026), p. 4

### 92. A Research Roadmap for Augmenting Software Engineering Processes and Software Products with Generative AI

Amalfitano, D., Metzger, A., Autili, M., Fulcini, T., Hey, T., Keim, J., Pelliccione, P., Scotti, V., Koziolek, A., Mirandola, R., & Vogelsang, A. (2026). A Research Roadmap for Augmenting Software Engineering Processes and Software Products with Generative AI. ACM Transactions on Software Engineering and Methodology (TOSEM), Volume 35, Issue 9, 35(9), 1-52. https://doi.org/10.1145/3788879

**Relevance**: supporting · **Peer-reviewed** · **Design**: survey

*Contribution (paraphrase):* The roadmap classifies GenAI augmentation into four forms (Copilot, GenAIware, Teammate, Robot) and finds that the agentic 'GenAI Teammate' form enhances speed, prototyping and time-to-market but reverses Git versioning semantics, environmental sustainability, accountability and code ownership, and code comprehension. Inter-agent communication overhead is identified as a direct driver of energy cost, and multi-agent systems are flagged as capable of pursuing conflicting goals that must be planned for explicitly.

> Multi-agent systems may also pursue conflicting goals that should be taken
> into account when planning the overall system behavior.
>
> Amalfitano et al. (2026), p. 20

### 93. Developing Multi-Agent LLM Applications Through Continuous Human-LLM Co-Programming

Song, H., Göknil, A., Jiang, X., Melum, E., Joe, H., Gazzotti, C., Frascolla, V., Videsjorden, A. N., & Nguyen, P. H. (2025). Developing Multi-Agent LLM Applications Through Continuous Human-LLM Co-Programming. 2025 IEEE/ACM 4th International Conference on AI Engineering – Software Engineering for AI (CAIN), 42-47. https://doi.org/10.1109/cain66642.2025.00013

**Relevance**: supporting · **Peer-reviewed** · **Design**: case-study

*Contribution (paraphrase):* COPMA's refactoring patterns treat autonomy as a tunable dial: an autonomous group-manager agent planning workflows produces task misassignment and missing context, so the authors deliberately trade flexibility for predictability by fixing execution order, adding a moderator agent, or replacing the manager with code that orchestrates agents programmatically. Shifting implementations from the 'LLM world' to the 'code world' is presented as the main lever for controlling unpredictability and cost.

> A group manager agent can autonomously plan and coordinate workflows among
> agents, but this can lead to task misassignment or missing context.
>
> Song et al. (2025), p. 4

### 94. When Code Becomes Abundant: Redefining Software Engineering Around Orchestration and Verification

Kohl, K., & Carro, L. (2026). When Code Becomes Abundant: Redefining Software Engineering Around Orchestration and Verification. arXiv preprint. https://doi.org/10.1145/3793657.3793884

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: position

*Contribution (paraphrase):* The paper argues the SDLC is being compressed between cheap AI code generation and hardening physical/regulatory constraints, collapsing construction and routine maintenance into two remaining poles of human responsibility: orchestration (intent articulation and architectural control) and verification. Its central named risk is 'accountability collapse' — the erosion of the link between human decisions and system behaviour when automated synthesis rather than manual design determines software structure — with architecture repositioned as a governance control surface that preserves traceability.

> These boundaries are essential for preventing accountability collapse:
> they preserve traceability between intent, generation, and observed
> behavior, and define where responsibility can be meaningfully located.
>
> Kohl & Carro (2026), p. 3

### 95. Human-AI experience in integrated development environments: a systematic literature review

Sergeyuk, A., Zakharov, I., Koshchenko, E., & Izadi, M. (2026). Human-AI experience in integrated development environments: a systematic literature review. Empirical Software Engineering, 31(3). https://doi.org/10.1007/s10664-025-10793-0

**Relevance**: supporting · **Peer-reviewed** · **Design**: survey

*Contribution (paraphrase):* A PRISMA systematic review of 90 in-IDE human-AI experience studies finds that productivity gains from AI coding assistance are consistently accompanied by a verification tax: developers spend more time checking output, and reliance miscalibrates in both directions (novices over-rely and under-verify, professionals under-rely and reject correct output lacking a rationale). Research is heavily concentrated on GitHub Copilot and the implementation stage, leaving requirements, testing and deployment largely unstudied.

> Impact findings show that AI-assisted coding enhances developer
> productivity but also introduces challenges, such as verification overhead
> and over-reliance.
>
> Sergeyuk et al. (2026), p. 1

### 96. Toward Agentic Software Engineering Beyond Code: Framing Vision, Values, and Vocabulary

Hoda, R. (2026). Toward Agentic Software Engineering Beyond Code: Framing Vision, Values, and Vocabulary. AGENT '26: Proceedings of the 2026 International Workshop on Agentic Engineering, 181-185. https://doi.org/10.1145/3786167.3788422

**Relevance**: supporting · **Peer-reviewed** · **Design**: position

*Contribution (paraphrase):* The paper argues that current agentic SE visions (agentic AI software engineer, USEagent, SASE, AIDev) are almost entirely code-centric, while early empirical evidence shows AI acts as a 'personal accelerator' that does not fix teamwork, coordination, accountability or culture. It proposes a 'whole of process' vision spanning ethical alignment, requirements, design, development and operations, plus preliminary CRAFT values and a call for well-defined agentic SE vocabulary.

> These visions and efforts, while necessary and welcome, are primarily
> focused around one SE activity – coding.
>
> Hoda (2026), p. 2

### 97. Automated Generation of End-to-End Web Test Cases via a Generic AI Agent: A Comparative Study of DeepSeek V3 and Claude Sonnet 5

Monteiro, C. E. O., Guerino, L. R., Fernandes, G., Pereira, M. F. P., de Souza-Zinader, J. P., Braga, R. D. B., Pocivi, V. C. B., & Vincenzi, A. M. R. (2025). Automated Generation of End-to-End Web Test Cases via a Generic AI Agent: A Comparative Study of DeepSeek V3 and Claude Sonnet 5. https://doi.org/10.5753/webmedia.2025.16046

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* Wrapping an LLM in a generic AI agent (Suna) that can clone repositories, navigate sites, compile and orchestrate prompts produced usable end-to-end Selenium tests where direct chat-based prompting of the same models had failed to even compile. Model choice dominated outcome quality: Claude Sonnet 4 reached 70.1% successful tests versus DeepSeek V3's 34.3%, but the cheaper model was faster, never crashed, and produced largely disjoint error profiles, so the authors recommend a complementary incremental strategy.

> In contrast, Claude Sonnet 4 exhibited a longer generation time but
> produced more consistent and higher-quality test cases.
>
> Monteiro et al. (2025), p. 8

### 98. From Helpful to Trustworthy: LLM Agents for Pair Programming

Ayon, R. S. (2026). From Helpful to Trustworthy: LLM Agents for Pair Programming. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering, 39-40. https://doi.org/10.1145/3803437.3804875

**Relevance**: supporting · **Peer-reviewed** · **Design**: position

*Contribution (paraphrase):* This doctoral research plan argues that a driver/navigator multi-agent pair only earns trust over a single-agent setup when the navigator's critique is constrained to machine-checkable contracts and formal specifications validated by deterministic verifiers, rather than free-form LLM judgment. Preliminary verifier-guided specification synthesis (AutoReSpec, AutoJML) is offered as evidence that iterative verifier feedback improves correctness and completeness.

> We will study a driver-and-navigator setup to quantify when multi-agent
> collaboration improves reliability and trust signals relative to
> single-agent baselines.
>
> Ayon (2026), p. 2

### 99. ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control

Avgerinos, V., Ramantas, K., Alonso, L., & Verikoukis, C. (2025). ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control. IEEE Internet of Things Journal, 13(9), 18305-18315. https://doi.org/10.1109/jiot.2025.3648858

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* A single tool-calling LLM agent closes a detect-diagnose-remediate loop over a K3s cloud-edge cluster, but reliability is strongly model-dependent: GPT-5 identifies faults far more accurately and in roughly half the reasoning rounds of the GPT-5-mini baseline, and the binary success metric can score a run successful even when root-cause identification was 0%.

> Results show that the agent identifies SLA violations with 52.9% accuracy
> and mitigates 70.7% of them successfully.
>
> Avgerinos et al. (2025), p. 1

### 100. Vibe Coding vs. Agentic Coding: Fundamentals and Practical Implications of Agentic AI

Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). Vibe Coding vs. Agentic Coding: Fundamentals and Practical Implications of Agentic AI. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2505.19443

**Relevance**: supporting · **Preprint (not peer reviewed)** · **Design**: survey

*Contribution (paraphrase):* A taxonomic review contrasting human-in-the-loop 'vibe coding' with autonomous 'agentic coding', arguing that agentic scalability will come from orchestrator-coordinated specialized sub-agents rather than a monolithic agent, while cataloguing agentic failure modes of overdependence, silent error propagation across modules, and expanded runtime privilege as security surface.

> Scalability in agentic coding will emerge not from a single monolithic
> agent, but from a constellation of specialized sub-agents planners,
> coders, testers, reviewers coordinated by an orchestrator.
>
> Sapkota et al. (2025b), p. 27

### 101. Leveraging LLMs for the Quality Assurance of Software Requirements

Lubos, S., Felfernig, A., Tran, T. N. T., Garber, D., Mansi, M. E., Erdeniz, S. P., & Le, V.-M. (2024). Leveraging LLMs for the Quality Assurance of Software Requirements. https://doi.org/10.1109/re59067.2024.00046

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* A single LLM instructed against the ISO 29148 quality characteristics achieves high recall but low precision when human software engineers are treated as ground truth, so it works as a reviewer aid that surfaces candidate flaws with plausible explanations rather than as an autonomous quality gate.

> The current capabilities of LLMs are not sufficient to fully automate this
> task.
>
> Lubos et al. (2024), p. 7

### 102. AI Coders Are among Us: Rethinking Programming Language Grammar towards Efficient Code Generation

Sun, Z., Du, X., Yang, Z., Li, L., & Lo, D. (2024). AI Coders Are among Us: Rethinking Programming Language Grammar towards Efficient Code Generation. https://doi.org/10.1145/3650212.3680347

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* Human-oriented programming grammar imposes a measurable token tax on LLM inference; an AI-oriented grammar (SimPy) that preserves the Python AST cuts token usage by 13.5% (CodeLlama) and 10.4% (GPT-4) while models trained Python-then-SimPy match or exceed their Python baselines.

> In the experiments, compared with Python, SimPy enables a reduction in
> token usage by 13.5% and 10.4% for CodeLlama and GPT-4, respectively, when
> completing the same set of code-related tasks.
>
> Sun et al. (2024), p. 1

### 103. Explainable automated debugging via large language model-driven scientific debugging

Kang, S., Chen, B., Yoo, S., & Lou, J. (2024). Explainable automated debugging via large language model-driven scientific debugging. Empirical Software Engineering, 30(2). https://doi.org/10.1007/s10664-024-10594-x

**Relevance**: supporting · **Peer-reviewed** · **Design**: empirical

*Contribution (paraphrase):* Wrapping a single LLM in a debugger-grounded hypothesis-experiment-observation loop yields repair performance competitive with direct LLM patch generation while producing explanations that improved developer patch-correctness judgments in five of six real-world bugs, at a cost of 4.66x longer runtime and a regression on Defects4J v1.2.

> in our experiments, AutoSD took on average 4.66 times longer to generate a
> patch when compared to LLM-Base.
>
> Kang et al. (2024), p. 21

---

## 4. Unanswered evidence gaps

### 4.1 The 24 core papers with no retrievable full text

Screening graded 73 records as core. Only 49 were retrieved and read; **24 core papers were never obtained in full text** and contribute nothing to Section 2 beyond their titles and abstracts. This is the largest single threat to the synthesis, because the missing set is not random: it is concentrated in exactly the venues that are hardest to scrape (ACM Digital Library, Elsevier, Springer) and therefore skews toward the peer-reviewed, high-rigor end of the field.

| # | Missing core paper | Why it matters to RQ2/RQ3 |
|---|---|---|
| 1 | He, J., Treude, C., & Lo, D. (2025). *LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead.* TOSEM 34(5) | The field's most-cited dedicated SLR on this exact question |
| 2 | Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2025). *Demystifying LLM-Based Software Engineering Agents.* PACMSE 2(FSE) | The primary Agentless study. The corpus's evidence for the "Agentless paradox" (D3) is a **second-hand review** of this paper, not the paper itself |
| 3 | Kim, D.-K. (2026). *Artifact validity under varying agent configurations in LLM-assisted software development: A comparative analysis.* Information and Software Technology 192 | Directly titled on the comparative question |
| 4 | Shafin, W. I., Rafi, M. N., Li, Z., & Chen, T.-H. (2026). *An Empirical Study of Waterfall-style Multi-Agent Workflows for Class-Level Code Generation.* PROMISE '26 | Would bear directly on the D1/D4 topology disagreement |
| 5 | *Is Collaboration Worth It? A Decision-Oriented Survey in Multi-Agent Systems* (2026) | Frames the exact cost-benefit question this review answers only partially |
| 6 | Watanabe, M., Li, H., Kashiwa, Y., Reid, B., Iida, H., & Hassan, A. E. (2026). *On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub.* TOSEM | The corpus has almost no field data on accepted agent-authored changes |
| 7 | Liu, S., Guo, Q., Liu, X., & Liu, Y. (2026). *Mitigating Cognitive Vulnerabilities in Code Generation via Multi-Agent Adversarial Debate.* WWW '26 | Debate is a claimed mitigation for correlated error; this is the primary evidence |
| 8 | Zhang, Y., Ruan, H., Fan, Z., & Roychoudhury, A. (2024). *AutoCodeRover: Autonomous Program Improvement* | Studied second-hand via Bouzenia and Pradel (2025) trajectories only |
| 9 | Zhu, X. et al. (2026). *Bugs in Modern LLM Agent Frameworks: An Empirical Study.* FSE Companion '26 | Would corroborate or contradict Xue et al. (2025) |
| 10 | Zhang, S. et al. (2025). *Empowering Agile-Based Generative Software Development through Human-AI Teamwork.* TOSEM 34(6) | Human-in-the-loop evidence is thin in the corpus |
| 11 | Lima, I., Linhares, V., Gomes, A. M., & Maia, P. H. (2026). *A Catalogue of Evaluation Metrics for LLM-Based Multi-Agent Frameworks in Software Engineering.* AGENT '26 | Would address the "benchmarks do not measure coordination" gap |
| 12 | Shang, Y. et al. (2026). *TestAgent: A Multi-Agent LLM Framework for Repository-Level Unit Test Generation.* FSE Companion '26 | Repository-level test generation is under-covered |
| 13 | Kataria, V. (2025). *Intelligent Site Reliability Engineering: A Multi-agent LLM Framework...* IJIES 18(11) | Retrieval returned a different article from the same issue |
| 14 | Bass, T. (2026). *A Validation and Governance Framework for Multi-Agent LLM Scientific Software Development.* IAIT '26 | Governance evidence rests on few primaries |
| 15 | Mitrović, S. et al. (2026). *Multi-Agent Systems for Software Development: a Multi-Faceted Research Question-driven Reference Guide.* SSRN | Directly RQ-structured |
| 16 | Di Sipio, C. et al. (2025). *Agentware in software engineering: A taxonomy for leveraging llms-based multi-agent systems.* SSRN | Taxonomy corroboration |
| 17 | *MOSAIC: A Pattern Catalog and Formal Framework for Multi-Agent LLM Orchestration in Software Engineering* (2026) | The corpus has no formal orchestration semantics |
| 18 | *Llm-based multi-agent systems: Frameworks, evaluation, open challenges, and research frontiers* (2025). Springer | Evaluation-gap corroboration |
| 19 | Drammeh, P. (2025). *Multi-Agent LLM Orchestration Achieves Deterministic, High-Quality Decision Support for Incident Response* | Claims determinism, which the read corpus consistently rejects |
| 20 | Sami, M. et al. (2025). *A Multi-agent LLM System for Automated Requirements Analysis.* LNCS | Requirements evidence is thin (18/103 papers) |
| 21 | Li, J., & Storhaug, A. (2026). *Reproducible, Explainable, and Effective Evaluations of Agentic AI for Software Engineering.* FSE Companion '26 | Reproducibility is a named weakness throughout |
| 22 | Koduri, S. K. A. (2025). *Efficiency-First Design for LLM-Based Multi-Agent Systems: A Framework and Empirical Analysis* | Cost evidence is the corpus's weakest quantitative area |
| 23 | Zhang, H., Cheng, W., Wu, Y., & Hu, W. (2024). *A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement* | Two-agent baseline evidence |
| 24 | Rotar, C., & Zhang, Q. (2025). *A design science research approach to LLMBA4RS in low-code applications.* Requirements Engineering 30(4) | Requirements and low-code coverage |

Three consequences follow. First, the D3 disagreement about architecture versus base model **cannot be resolved from this corpus** because one side of it is represented only by a low-rigor second-hand review. Second, the note that Xia et al. (2025) and the anonymous *Demystifying* review share nearly the same title is a live citation hazard for Chapter 2; they are different documents and only the latter was read. Third, retrieval integrity itself is a finding: two records in this run were retrieved with full text belonging to a **different paper** and were marked unavailable rather than extracted, because extracting them would have attached quotations to the wrong DOI.

### 4.2 Design gaps in the evidence itself

**G1. No factorial design over architecture and base model.** Orogat et al. (2026) fix the model to isolate framework effects; the Agentless line fixes the framework to isolate model effects. No study in the corpus varies both. Until one does, D3 is unresolvable and every "architecture X beats architecture Y" claim is confounded with model choice.

**G2. Single-agent arms are frequently absent or weak.** Yu et al. (2025) explicitly ran no contemporary single-agent LLM baseline for a production system deployed at cloud scale, justifying the omission by citing prior work rather than by experiment. Mao et al. (2025) defer both a single-agent baseline and a domain-specific detector baseline to future work while reporting up to 69.6% failure reduction. Hosseini et al. (2026) exclude single-agent baselines by task construction. Reid et al. (2025) are the only source in the corpus that makes single-agent baselining a stated methodological requirement:

> Compare multi-agent outcomes against individual agents working on decomposable
> portions of the task to determine if coordination actually improves
> performance.
>
> Reid et al. (2025), p. 38

**G3. Variance is almost never reported.** Kumar et al. (2026) report single-run SWE-bench Lite numbers with no variance. Abdalla et al. (2026) report a single end-to-end run per configuration. Agha and Miqdad (2026) use three runs and say so is insufficient. Liu (2025) computes that N ≈ 300 is needed for 80% power and had 50 issues. Given that non-determinism is the corpus's most-covered evidence domain (65 of 103 papers), the field measures the phenomenon far more often than it controls for it.

**G4. Benchmarks are saturated, contaminated, or both, and none scores coordination.** Ravindran et al. (2026) report partial benchmark saturation making aggregate pass rates non-discriminative. Rodriguez-Cardenas et al. (2026) document a 47-point drop from SWE-bench Verified to SWE-bench Pro and note that temporal filtering alone is insufficient because roughly 65% of Python packages share repositories. Liu et al. (2023) show test insufficiency reordering model rankings. Kehkashan et al. (2026) find no benchmark exceeding 50% on a deployment-readiness rubric.

**G5. Formal verification and concurrency are nearly absent.** Only 3 of 103 read papers touch `formal-verification` and 1 touches `transactions-concurrency`. Guo et al. (2025) propose temporal-logic verification of coordination protocols; Ayon (2026) proposes solver-backed contracts as the basis for trusting a navigator agent; Alenezi (2026) argues verification should be treated as infrastructure. All three are proposals. No study in the corpus formally verifies a multi-agent coordination protocol, and no study addresses concurrent edits, race conditions, or transactional rollback across agents beyond the architectural analysis in Yazdanian et al. (2025).

**G6. Sustainability is asserted, not measured.** No paper in the corpus measures the energy cost of a multi-agent versus single-agent software engineering pipeline. Thakur and Moin (2026) measure energy but for retrieval augmentation on single models; Amalfitano et al. (2026) name inter-agent communication as an energy driver without measurement. Token count is used as a universal proxy, which conflates cost, latency, and energy across heterogeneous hardware.

**G7. Enterprise and longitudinal evidence is scarce.** Takerngsaksiri et al. (2025), Yu et al. (2025), Parthasarathy et al. (2025), Damarched (2026), and Vella et al. (2026) are the only deployment studies, and each is single-organization with self-reported outcomes. Nothing in the corpus measures maintenance cost of agent-authored code over time, which Otoum and Elkhalili (2026) flag as essentially unstudied.

**G8. Failure attribution is not yet reliable enough to support the failure taxonomies built on it.** With step-level attribution accuracy at 25–52% (Wang et al., 2026), the prevalence figures in Section 2.6 should be treated as ordinal rather than as calibrated estimates.

### 4.3 What a defensible follow-on study would need

Derived from the gaps above rather than from any single paper:

1. A factorial design crossing at least three topologies (single agent, pipeline, supervisor-worker) with at least three base models of differing capability, on at least two task families that differ in parallelizability, with a preregistered stopping rule and repeated runs sufficient for the effect sizes involved.
2. Cost, latency, and token accounting reported as primary outcomes rather than appendix material, alongside a same-task single-agent arm.
3. A contamination-controlled benchmark, or explicit reporting of pre- and post-cutoff splits.
4. Trajectory-level instrumentation aligned to a fault-injection overlay, so that coordination failures are observed rather than inferred from end-state success.

---

## 5. References

All 103 works read in full and cited above, in APA form matching `references.bib` (which holds 203 entries covering the full selected set, including the 100 records sought but not retrieved). Preprint status is marked on the corresponding entry in Section 3.

Citation notes. Two short forms are disambiguated in text and in Section 3: `Li, S., et al. (2025)` is *Multi-agent collaboration mechanisms* while `Li, W., et al. (2025)` is *PhishDebate*; `Sapkota et al. (2025a)` is *AI Agents vs. Agentic AI* while `Sapkota et al. (2025b)` is *Vibe Coding vs. Agentic Coding*. Two further entries share a surname but not a short form: `Xu et al. (2026)` is *Hallucination to Consensus* and `Xu and Qin (2026)` is the Rust bioinformatics case study. Reference strings below are reproduced exactly as generated in `manifest.json` and are therefore not annotated with the a/b suffixes.

1. Large language model agents: A comprehensive survey on architectures, capabilities, and applications. (2025). https://www.preprints.org/manuscript/202512.2119
2. LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns. (2026). https://www.preprints.org/manuscript/202604.2147
3. Demystifying LLM-Based Software Engineering Agents: A Review of Capabilities, Benchmarks, and Failure Modes. (n.d.). https://journal.duc.edu.iq/index.php/djst/article/view/828
4. Abdalla, A. S., Thie, V., Schaub, J., Eisenbarth, M., Lee, S. H., & Andert, J. (2026). Multi-Agent Software Development for Automotive Model-Based Graphical Programming. IEEE Access. https://doi.org/10.2139/ssrn.6253838
5. Agha, M., & Miqdad, A. (2026). An empirical comparison of multi-agent LLM architectural patterns for automated unit test generation. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.20309242
6. Akshathala, S., Adnan, B., Ramesh, M., Vaidhyanathan, K., Muhammed, B., & Parthasarathy, K. (2026). Beyond Task Completion: An Assessment Framework for Evaluating Agentic AI Systems. AGENT '26: Proceedings of the 2026 International Workshop on Agentic Engineering, 9-17. https://doi.org/10.1145/3786167.3788414
7. Alenezi, M. (2026). Rethinking software engineering for agentic ai systems. arXiv preprint. https://arxiv.org/abs/2604.10599
8. Amalfitano, D., Metzger, A., Autili, M., Fulcini, T., Hey, T., Keim, J., Pelliccione, P., Scotti, V., Koziolek, A., Mirandola, R., & Vogelsang, A. (2026). A Research Roadmap for Augmenting Software Engineering Processes and Software Products with Generative AI. ACM Transactions on Software Engineering and Methodology (TOSEM), Volume 35, Issue 9, 35(9), 1-52. https://doi.org/10.1145/3788879
9. Arnaudo, A., Coppola, R., Giobergia, F., Morisio, M., Nguyen, V.-T., Chen, E., Ma, X., Ji, X., & Mai, M.-T. (2026). Automated Black-Box Testing: A Comparative Study of LLM Agent Architectures and Prompt Engineering. 2026 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW), 29-36. https://doi.org/10.1109/icstw72326.2026.00018
10. Arora, K., Naim, A., & Sharma, S. (2026). Benchmarking Multi-Agent LLM and Single Agent LLM Efficiency for Contextual Text Generation. 2026 International Conference on Intelligent Systems in Engineering, Secured Systems and Cybersecurity (ICISESSC), 741-745. https://doi.org/10.1109/icisessc68634.2026.11542788
11. Ashrafi, N., Bouktif, S., & Mediani, M. (n.d.). Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Accuracy, Reliability, and Latency. 2025 IEEE 19th International Conference on Application of Information and Communication Technologies (AICT). https://ieeexplore.ieee.org/document/11268754/
12. Avgerinos, V., Ramantas, K., Alonso, L., & Verikoukis, C. (2025). ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control. IEEE Internet of Things Journal, 13(9), 18305-18315. https://doi.org/10.1109/jiot.2025.3648858
13. Ayon, R. S. (2026). From Helpful to Trustworthy: LLM Agents for Pair Programming. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering, 39-40. https://doi.org/10.1145/3803437.3804875
14. Barrak, A. (2025). Traceability and Accountability in Role-Specialized Multi-Agent LLM Pipelines. 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW), 315-322. https://doi.org/10.1109/asew67777.2025.00064
15. Basu, S., Kjellberg, V., Sun, S., Haraldsson, B., Babu, M. A. A., Meding, W., Fotrousi, F., & Staron, M. (2026). Understanding Conversational Patterns in Multi-agent Programming: A Case Study on Fibonacci Game Development. AIware '26: Proceedings of the 3rd ACM International Conference on AI-Powered Software, 238-247. https://doi.org/10.1145/3805760.3814914
16. Becattini, M., Caselli, N., Minin, M., Verdecchia, R., & Vicario, E. (2026). CAPRA: Scaling Feedback on Software Architecture Deliverables with a Multi-Agent LLM System. arXiv preprint. http://arxiv.org/abs/2606.18976v1
17. Becattini, M., Verdecchia, R., & Vicario, E. (2025). SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems. 2025 IEEE/ACM International Workshop New Trends in Software Architecture (SATrends), 5-8. https://doi.org/10.1109/satrends66715.2025.00006
18. Bouzenia, I., & Pradel, M. (2025). Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 2846-2857. https://doi.org/10.1109/ase63991.2025.00234
19. Bui, T.-L., Dam, H. K., & Hoda, R. (2025). An LLM-based multi-agent framework for agile effort estimation. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 1032-1043. https://doi.org/10.1109/ase63991.2025.00090
20. Cai, Y., Li, R., Liang, P., Shahin, M., & Li, Z. (2025). Designing LLM-based multi-agent systems for software engineering tasks: Quality attributes, design patterns and rationale. arXiv preprint. https://arxiv.org/abs/2511.08475
21. Calboreanu, E. (2026). Iterative Audit Convergence in LLM-Managed Multi-Agent Systems: A Case Study in Prompt-Engineering Quality Assurance. Software, 5(2), 26. https://doi.org/10.3390/software5020026
22. Chebolu, I., Mallick, A., & Rana, H. (2026). SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing. arXiv preprint. https://doi.org/10.48550/arxiv.2602.04418
23. Damarched, M. K. (2026). Agentic AI Modernization: Transforming Institutional Infrastructure Through Orchestrated Multi-Agent LLM Framework. Journal of Computer Science and Technology Studies, 8(4), 01-24. https://doi.org/10.32996/jcsts.2026.8.4.1
24. De Oliveira, M. C. S., Ibiyo, M. O., Gianrusso, M., Di Sipio, C., Di Ruscio, D., & Nguyen, P. T. (2026). Developing LLM-based Multi-Agent Systems in Software Engineering: A Mixed-Method Experience Report. arXiv preprint. https://doi.org/10.48550/arxiv.2608.11965
25. Di Ruscio, D., Nguyen, P. T., Di Sipio, C., Rubei, R., & Di Rocco, J. (2026). Engineering LLM-based Multi-Agent Systems: A Taxonomy of Emerging Frameworks. IEEE Software, 1-8. https://doi.org/10.1109/ms.2026.3694089
26. Essam, M., Wael, K., Hassan, A., Haitham, A., Soliman, M., Saber, S., & Habib, I. (2026). Trust-Aware Multi-Agent Traceability: Confidence-Calibrated Knowledge Graphs for Consistent Software Artifact Management. 2026 15th Mediterranean Conference on Embedded Computing (MECO). https://doi.org/10.48550/arxiv.2606.17203
27. Grabowski, H. (2026). A Modular Multi-Agent {LLM} Architecture for Text-to-Diagram Generation and User-Guided Refinement. e-Informatica Software Engineering Journal, 20(1), 260109. https://doi.org/10.37190/e-inf260109
28. Guo, J., Huang, S., Li, M., Huang, D., Chen, X., Zhang, R., Guo, Z., Yu, H., Yiu, S.-M., Lio, P., & Lam, K.-Y. (2025). A comprehensive survey on benchmarks and solutions in software engineering of llm-empowered agentic system. arXiv preprint. https://arxiv.org/abs/2510.09721
29. Haataja, J. (2026). THE CAPABILITIES AND LIMITATIONS OF AI AGENTS IN SOFTWARE DEVELOPMENT. Tampere University Institutional Repository (Tampere University). https://trepo.tuni.fi/bitstream/handle/10024/238728/HaatajaJustus.pdf?sequence=2
30. Haseeb, M. (2025). Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code. arXiv preprint. http://arxiv.org/abs/2508.08322v1
31. Hoda, R. (2026). Toward Agentic Software Engineering Beyond Code: Framing Vision, Values, and Vocabulary. AGENT '26: Proceedings of the 2026 International Workshop on Agentic Engineering, 181-185. https://doi.org/10.1145/3786167.3788422
32. Hossain, E., Nipu, M. H. B., Mahmood, M. S., Hossen, M. J., & Mridha, M. F. (2026). Safe and Scalable Collaboration in Multiagent LLM Systems: A Comprehensive Review. IEEE Transactions on Systems Man and Cybernetics Systems, 1-17. https://doi.org/10.1109/tsmc.2026.3704902
33. Hosseini, M.-P., Shah, A., Qureshi, S., Huang, A., Miao, C., & Wei, W. (2026). Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent LLM Systems. 2026 IEEE 50th Annual Computers, Software, and Applications Conference (COMPSAC), 179-188. https://doi.org/10.1109/compsac69091.2026.00034
34. Issa, K. (2026). Developing and Evaluating an LLM-based Agent for ExplorViz Using CopilotKit. Kiel Software Engineering Research. https://doi.org/10.38071/2026-00397-5
35. Jin, H., Huang, L., Cai, H., Yan, J., Li, B., & Chen, H. (2024). From llms to llm-based agents for software engineering: A survey of current, challenges and future. arXiv preprint. https://arxiv.org/abs/2408.02479
36. Kang, S., Chen, B., Yoo, S., & Lou, J. (2024). Explainable automated debugging via large language model-driven scientific debugging. Empirical Software Engineering, 30(2). https://doi.org/10.1007/s10664-024-10594-x
37. Kehkashan, T., Abdullah, M., Al-Shamayleh, A. S., Ivković, N., Ismail, N. A., Ahmad, S. S. S., Rehman, A., & Akhunzada, A. (2026). From benchmarks to deployment: a comprehensive review of agentic AI evaluation. Artificial Intelligence Review, 59(8). https://doi.org/10.1007/s10462-026-11571-0
38. Kim, Y., Gu, K., Park, C., Park, C., Schmidgall, S., Heydari, A. A., Yan, Y., Zhang, Z., Zhuang, Y., Liu, Y., Malhotra, M., Liang, P., Park, H. W., Yang, Y., Xu, X., Du, Y., Patel, S., Althoff, T., McDuff, D., & Liu, X. (2026). Towards a Science of Scaling Agent Systems. Research Square. https://doi.org/10.21203/rs.3.rs-8414536/v1
39. Kohl, K., & Carro, L. (2026). When Code Becomes Abundant: Redefining Software Engineering Around Orchestration and Verification. arXiv preprint. https://doi.org/10.1145/3793657.3793884
40. Kumar, R., Ali, W., Ahmed, J., Ali, N. I., & Usman, S. (2026). AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering. arXiv preprint. https://doi.org/10.48550/arxiv.2604.13120
41. Lai, J., & Li, Z. (2026). A Comparative Empirical Evaluation of Single-Agent and Multi-Agent LLM Prompting Strategies for Automated Formative Feedback in Education. Journal of Intelligence and Engineering Technology, 1(2), 29-38. https://doi.org/10.70393/6a696574.343135
42. Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2303.17760
43. Li, S., Jia, X., Tam, W. F., Tabaro, L., Li, Q., Liu, G., Wang, C., & Abdelmoniem, A. M. (2025). Multi-agent collaboration mechanisms: A survey of llms. arXiv preprint. https://doi.org/10.2139/ssrn.7243979
44. Li, W., Manickam, S., Chong, Y.-W., & Karuppayah, S. (2025). PhishDebate: An LLM-Based Multi-Agent Framework for Phishing Website Detection. arXiv preprint, 6606-6615. https://doi.org/10.1109/BigData66926.2025.11401440
45. Li, Y. (2026). A Multi-Agent LLM Framework for Automated Software Testing. Transactions on Computing Science, 2(2), 1-25. https://doi.org/10.63808/tcs.v2i2.447
46. Liu, E. (2025). SE-Blackboard: A Shared-State Architecture for Multi-Agent Software Engineering Pipelines. IEEE Access. https://doi.org/10.5281/zenodo.18911614
47. Liu, J., Wang, K., Chen, Y., Peng, X., Chen, Z., Zhang, L., & Lou, Y. (2024). Large Language Model-Based Agents for Software Engineering: A Survey. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3796507
48. Liu, J., Xia, C. S., Wang, Y., & Zhang, L. (2023). Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2305.01210
49. Lu, R., Li, Y., & Huo, Y. (2025). Exploring Autonomous Agents: A Closer Look at Why They Fail When Completing Tasks. https://doi.org/10.1109/ase63991.2025.00330
50. Lubos, S., Felfernig, A., Tran, T. N. T., Garber, D., Mansi, M. E., Erdeniz, S. P., & Le, V.-M. (2024). Leveraging LLMs for the Quality Assurance of Software Requirements. https://doi.org/10.1109/re59067.2024.00046
51. Mandal, I., Soni, J., Zaki, M., Smedskjær, M. M., Wondraczek, K., Wondraczek, L., Gosvami, N. N., & Krishnan, N. M. A. (2024). Autonomous Microscopy Experiments through Large Language Model Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2501.10385
52. Mandal, I., Soni, J., Zaki, M., Smedskjær, M. M., Wondraczek, K., Wondraczek, L., Gosvami, N. N., & Krishnan, N. M. A. (2025). Evaluating large language model agents for automation of atomic force microscopy. Nature Communications, 16(1), 9104-9104. https://doi.org/10.1038/s41467-025-64105-7
53. Mao, Z., Keung, J., Zhang, F., Liu, S., Wang, Y., & Li, J. (2025). Towards Engineering Multi-Agent LLMs: A Protocol-Driven Approach. https://doi.org/10.1109/apsec66846.2025.00100
54. Mohamed, N., Chakrabarti, P., & Gupta, S. K. (2026). A Systematic Survey of LLM-Based Agentic AI Frameworks for Multi-Agent Coordination and Interoperability. Journal of Smart Algorithms and Applications (JSAA), 5(1), 1-23. https://doi.org/10.66279/y29vex64
55. Mohammad, F., Kakar, J. K., Ndong, D. R. B. B., Chas, M., & Ryu, D. (2026). CodeQual-Agent: An Intelligent LLM-Agent Framework for Automated Software Quality Assessment with Explainable Predictions and Real-Time Analysis. 2026 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW), 123-128. https://doi.org/10.1109/icstw72326.2026.00035
56. Monteiro, C. E. O., Guerino, L. R., Fernandes, G., Pereira, M. F. P., de Souza-Zinader, J. P., Braga, R. D. B., Pocivi, V. C. B., & Vincenzi, A. M. R. (2025). Automated Generation of End-to-End Web Test Cases via a Generic AI Agent: A Comparative Study of DeepSeek V3 and Claude Sonnet 5. https://doi.org/10.5753/webmedia.2025.16046
57. Muhammad, A., Mohammed, M. A., Milanova, M., Talburt, J. R., & Cakmak, M. C. (2025). Multi-Agent RAG Framework for Entity Resolution: Advancing Beyond Single-LLM Approaches with Specialized Agent Coordination. Computers, 14(12), 525. https://doi.org/10.20944/preprints202510.2382.v1
58. Naqvi, S., Baqar, M., & Mohammad, N. A. (2026). The Rise of Agentic Testing: Multi-Agent Systems for Robust Software Quality Assurance. arXiv preprint. https://doi.org/10.48550/arxiv.2601.02454
59. Nguyen, D. S. H., Nguyen, M. T., Nguyen, P. T., Di Rocco, J., & Di Ruscio, D. (2026). Automated Summarization of Software Documents: An LLM-based Multi-Agent Approach. arXiv preprint, 33(2). https://doi.org/10.1007/s10515-025-00588-4
60. Orogat, A., Rostam, A., & Mansour, E. (2026). Understanding multi-agent LLM frameworks: A unified benchmark and experimental analysis. arXiv preprint. https://arxiv.org/abs/2602.03128
61. Otoum, N., & Elkhalili, N. (2026). Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review. IEEE Access, 14, 7443-7465. https://doi.org/10.1109/access.2026.3652325
62. Owotogbe, J. (2025). Assessing and Enhancing the Robustness of LLM-Based Multi-Agent Systems Through Chaos Engineering. 2025 IEEE/ACM 4th International Conference on AI Engineering – Software Engineering for AI (CAIN), 250-252. https://doi.org/10.1109/cain66642.2025.00039
63. Park, G., Lee, S. C., & Park, Y. (2026). Minimizing Response Latency in LLM-Based Agent Systems: A Comprehensive Survey. IEEE Access, 14, 26140-26168. https://doi.org/10.1109/access.2026.3664226
64. Parthasarathy, K., Vaidhyanathan, K., Dhar, R., Krishnamachari, V., Kakran, A., Akshathala, S., Arun, S., Karan, A., Muhammed, B., Dubey, S., & Veerubhotla, M. (2025). Engineering LLM Powered Multi-Agent Framework for Autonomous CloudOps. 2025 IEEE/ACM 4th International Conference on AI Engineering – Software Engineering for AI (CAIN), 201-211. https://doi.org/10.1109/cain66642.2025.00031
65. Pham, A. B. B., Nguyen, H. T., & Usman, M. (2026). QBugLM: An Agentic Benchmarking Framework for LLM-based Quantum Software Debugging. 2026 IEEE International Conference on Quantum Software (QSW). https://ieeexplore.ieee.org/document/11662247/
66. Pranoto, D. C. Y., Hussien, S. B., Sabariah, S., Bandono, A., & Bahrawi, A. (2026). Architectural Transparency in LLM-Based Cognitive Assessment: A Multidimensional TRACE-ED Evaluation of Single-Agent and Multi-Agent Systems. Research Square. https://doi.org/10.21203/rs.3.rs-8985839/v1
67. Premasundera, S. (2025). MULTI-AGENT SYSTEM FOR AUTOMATED CODE REVIEWS. Tampere University Institutional Repository (Tampere University). https://trepo.tuni.fi/bitstream/handle/10024/232334/PremasunderaSavidya.pdf?sequence=2
68. Qi, S., Ma, J., Xing, R., Guo, W., Huang, X., Gao, Z., Deng, J., Liu, J., Zhang, L., Wei, B., Yang, B., Wang, P., Sun, J., Tao, J., Wu, Y., Liu, H., Yao, Y., & Liu, T. (2026). Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems. arXiv preprint. https://arxiv.org/abs/2605.14892
69. Radeva, I., Noncheva, T., Doukovska, L., & Popchev, I. (2026). Comparing Single-Agent and Multi-Agent Strategies in LLM-Based Title-Abstract Screening. https://doi.org/10.20944/preprints202603.2107.v1
70. Rajendran, V., Besiahgari, D., Patil, S. C., Chandrashekaraiah, M., & Challagulla, V. (2025). A Multi-Agent LLM Environment for Software Design and Refactoring: A Conceptual Framework. SoutheastCon 2025, 488-493. https://doi.org/10.1109/southeastcon56624.2025.10971563
71. Ramírez-Rueda, R., Benítez–Guerrero, E., Mezura-Godoy, C., & Bárcenas, E. (2024). Transforming Software Development: A Study on the Integration of Multi-Agent Systems and Large Language Models for Automatic Code Generation. 2024 12th International Conference in Software Engineering Research and Innovation (CONISOFT), 11-20. https://doi.org/10.1109/conisoft63288.2024.00013
72. Rasheeda, Z., Waseema, M., Kemella, K.-K., Saari, M., & Abrahamsson, P. (2026). LLM-Based Multi-Agent Systems for Code Generation: A Multi-Vocal Literature Review. arXiv preprint. https://doi.org/10.5281/zenodo.21487935
73. Ravindran, A., Patra, A., Babaey, V., & Purini, S. (2026). A Critical Review and Evaluation of LLMs for RTL Generation. IEEE Access, 14, 28522-28539. https://doi.org/10.1109/access.2026.3665894
74. Reid, A., O'Callaghan, S., Carroll, L., & Caetano, T. (2025). Risk analysis techniques for governed LLM-based multi-agent systems. arXiv preprint. https://doi.org/10.48550/arxiv.2508.05687
75. Rodriguez-Cardenas, D., Li, X., Macedo, M., Mastropaolo, A., Khati, D., Tian, Y., Shao, H., & Poshyvanyk, D. (2026). Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering. FORGE '26: Proceedings of the 2026 IEEE/ACM Third International Conference on AI Foundation Models and Software Engineering, 243-248. https://doi.org/10.1145/3793655.3793716
76. Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges. Information Fusion, 126(3), 103599-103599. https://doi.org/10.1016/j.inffus.2025.103599
77. Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). Vibe Coding vs. Agentic Coding: Fundamentals and Practical Implications of Agentic AI. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2505.19443
78. Sergeyuk, A., Zakharov, I., Koshchenko, E., & Izadi, M. (2026). Human-AI experience in integrated development environments: a systematic literature review. Empirical Software Engineering, 31(3). https://doi.org/10.1007/s10664-025-10793-0
79. Seyedghorban, Z., Klimov, E., van Deursen, A., Panichella, A., & Ozkan, B. K. (2026). Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering. 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST), 211-215. https://doi.org/10.1109/icst69053.2026.00037
80. Shen, W., Li, C., Chen, H., Yan, M., Quan, X., Chen, H., Zhang, J., & Huang, F. (2024). Small LLMs Are Weak Tool Learners: A Multi-LLM Agent. arXiv preprint, 16658-16680. https://doi.org/10.18653/v1/2024.emnlp-main.929
81. Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2303.11366
82. Shu, R., Das, N., Yuan, M., Sunkara, M., & Zhang, Y. (2024). Towards Effective GenAI Multi-Agent Collaboration: Design and Evaluation for Enterprise Applications. arXiv preprint. https://doi.org/10.48550/arxiv.2412.05449
83. Song, H., Göknil, A., Jiang, X., Melum, E., Joe, H., Gazzotti, C., Frascolla, V., Videsjorden, A. N., & Nguyen, P. H. (2025). Developing Multi-Agent LLM Applications Through Continuous Human-LLM Co-Programming. 2025 IEEE/ACM 4th International Conference on AI Engineering – Software Engineering for AI (CAIN), 42-47. https://doi.org/10.1109/cain66642.2025.00013
84. Sun, Z., Du, X., Yang, Z., Li, L., & Lo, D. (2024). AI Coders Are among Us: Rethinking Programming Language Grammar towards Efficient Code Generation. https://doi.org/10.1145/3650212.3680347
85. Takerngsaksiri, W., Pasuksmit, J., Thongtanunam, P., Tantithamthavorn, C., Zhang, R., Jiang, F., Li, J., Cook, E., Chen, K., & Wu, M. (2025). Human-In-The-Loop Software Development Agents. 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP), 342-352. https://doi.org/10.1109/icse-seip66354.2025.00036
86. Tang, Y., & Runkler, T. (2026). Llm-based agentic systems for software engineering: Challenges and opportunities. arXiv preprint. https://doi.org/10.18420/se2026-ws_15
87. Tawosi, V., Ramani, K., Alamir, S., & Liu, X. (2025). ALMAS: an Autonomous LLM-based Multi-Agent Software Engineering Framework. 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW), 287-290. https://doi.org/10.1109/asew67777.2025.00059
88. Thakur, H., & Moin, A. (2026). "ENERGY STAR" LLM-Enabled Software Engineering Tools. arXiv preprint. https://doi.org/10.48550/arxiv.2601.19260
89. Tomic, S., Alégroth, E., & Isaac, M. (2025). Evaluation of the Choice of LLM in a Multi-Agent Solution for GUI-Test Generation. 2025 IEEE Conference on Software Testing, Verification and Validation (ICST), 487-497. https://doi.org/10.1109/icst62969.2025.10989038
90. Trifković, N., & Antović, I. (2026). Towards Role-Based Multi-Agent LLM Systems for Software Requirements Analysis. 2026 30th International Conference on Information Technology (IT), 1-4. https://doi.org/10.1109/it67293.2026.11435673
91. Vella, S., Ferworn, A., & Sharieh, M. (2026). ATeam: Governance-Aware LLM-Assisted Software Sustaining Engineering for Enterprise Systems. 2026 6th International Conference on Electrical, Computer and Energy Technologies (ICECET), 1-6. https://doi.org/10.1109/icecet65726.2026.11633274
92. Wang, H., Liu, Z., Wang, S., Cui, G., Ding, N., Liu, Z., & Ge, Y. (2024). INTERVENOR: Prompting the Coding Ability of Large Language Models with the Interactive Chain of Repair. https://doi.org/10.18653/v1/2024.findings-acl.124
93. Wang, J., Wang, Y., Chen, M., Xie, X., Chen, C., Mu, F., Liu, Z., & Wang, Q. (2026). A Survey for LLM Agent Trajectory Analysis: From Failure Attribution to Enhancement. IEEE Transactions on Software Engineering, 1-23. https://doi.org/10.1109/tse.2026.3717765
94. Wang, S., Zhong, Z., Wen, S., & Liu, Y. (2025). Multi-Agent Assisted Automatic Test Generation for Java JSON Libraries. https://doi.org/10.1109/apsec66846.2025.00064
95. Xiao, Y.-A., Gao, P., Peng, C., & Xiong, Y. (2026). Reducing Cost of LLM Agents with Trajectory Reduction. Proceedings of the ACM on Software Engineering (PACMSE), Volume 3, Issue FSE, 3(FSE), 1241-1263. https://doi.org/10.1145/3797084
96. Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2025). Demystifying LLM-Based Software Engineering Agents. Proceedings of the ACM on Software Engineering (PACMSE), Volume 2, Issue FSE, 2(FSE), 801-824. https://doi.org/10.1145/3715754
96. Xu, Q., Wang, G., Briand, L., & Liu, K. (2026). Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3803418
97. Xu, Z.-G., & Qin, G. (2026). LLM-assisted development of Rust for high-performance bioinformatics software: practices, workflows, and boundaries. Genomics Communications, 3(1), 0-0. https://doi.org/10.48130/gcomm-0026-0018
98. Xue, Z., Zhao, Y., Wang, S., Chen, K., & Wang, H. (2025). A Characterization Study of Bugs in LLM Agent Workflow Orchestration Frameworks. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 3369-3380. https://doi.org/10.1109/ase63991.2025.00278
99. Yang, Y., Chai, H., & Zhang, W. (2025). AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems. https://doi.org/10.32388/ws0vim
100. Yazdanian, P., Liu, Y., & Li, Z. (2025). A Comparative Study Towards Designing a Hybrid Architecture of Microservices and LLM-based Multi-Agent Systems. 2025 32nd Asia-Pacific Software Engineering Conference (APSEC), 761-772. https://doi.org/10.1109/apsec66846.2025.00077
101. Youwai, S., Phim, D., Murcia, V. G., & Onas, R. C. (2026). Large language model-based multi-agent systems for automated foundation design: router-driven task classification and expert selection framework. AI in Civil Engineering, 5(1). https://doi.org/10.1007/s43503-026-00088-8
102. Yu, Z., Fang, A., Ma, M., Walia, J. S., Zhang, C., Chi, S., Li, Z., Chintalapati, M., Zhang, X., Wang, R., Bansal, C., Rajmohan, S., Lin, Q., Zhang, S., Pei, D., & He, P. (2025). Triangle: Empowering Incident Triage with Multi-Agent. https://doi.org/10.1109/ase63991.2025.00062
103. Zeng, Z., Li, Y., Xie, R., Ye, W., & Zhang, S. (2025). Benchmarking and Studying the LLM-based Agent System in End-to-End Software Development. arXiv preprint. https://doi.org/10.48550/arxiv.2511.04064
