# Process Model Constraints versus Natural Language Policy for Compliance-Critical LLM Business Process Agents

Synthesis of a saturation-bounded systematic review. Run folder: `results/20260905-process-model-constraints-versus-natural`. Generated 2026-09-05 from persisted run artifacts only.

Every quotation below was located in this run's extracted full-text corpus with `corpus_search.py --quote`. Every reference string is copied from `manifest.json`, with one disclosed exception recorded in the reference list itself.

---

## 1. Research questions

Restated verbatim from `protocol.md`, which was preregistered and hashed before any search was run.

> **RQ1.** In compliance-critical business processes, does binding an LLM agent to an explicit process model reduce policy violations without a corresponding loss in task completion, compared with an agent given the same policy as natural-language instructions?

> **RQ2.** Which control mechanisms for agentic business process automation have been evaluated empirically, and against what baselines?

---

## 2. Method summary

### 2.1 Design

This is a saturation-bounded systematic review following Kitchenham staging and PRISMA 2020 reporting. The protocol was registered at 2026-09-05T05:29:26+00:00 with the research questions, the per-source search strategy, testable screening criteria and a preregistered taxonomy of 20 evidence domains. Downstream stages stamp the protocol hash into their artifacts, so post-hoc edits to the protocol are detectable.

One amendment is on record. The preregistered strategy sent RQ1 verbatim to the API sources and recalled 0 of the 8 preregistered known items, so the queries were broadened as PRISMA-S requires. Three tool defects were found and fixed during that stage: OpenAlex parses `?` as a wildcard operator and rejected the verbatim question, the OpenAlex source queried only full-text relevance rather than a scoped title-and-abstract filter, and known-item validation matched titles by exact equality. The scoped filter recalled 8 of 8 known items from a pool of 141 works, where full-text search had recalled 4 of 8 from a pool of 14,241. **Final known-item recall is 8 of 8.**

Two identification limitations are recorded rather than hidden. ACM returned 0 results on both attempts because its bot challenge did not clear, and Google Scholar returned only 6 records because it was sent the full-sentence question.

### 2.2 PRISMA counts

Taken from `prisma.md`, which is generated from persisted artifacts.

| Phase | Measure | Value |
|---|---|---|
| Identification | Search runs | 8 |
| Identification | Database records (raw) | 892 |
| Identification | Records by source | crossref 300, ieee 16, openalex 564, scholar 12, acm 0 |
| Identification | Citation-chaining records (2 rounds) | 177 |
| Deduplication | Duplicates removed | 355 |
| Screening | Unique records after merge, and screened | 704 |
| Screening | Decisions | core 47, supporting 174, context 180, exclude 189, unresolved 114 |
| Retrieval | Reports sought | 221 |
| Retrieval | Reports not retrieved | 189 |
| Full text | Reports assessed for eligibility | 32 |
| Full text | Excluded with reasons after assessment | none recorded |
| Included | Studies in synthesis | 32 |

The screening decisions sum exactly to the 704 screened records. Reports sought (221) is the union of the core and supporting strata (47 + 174). The retrieval yield is the weakest link in the chain: 32 of 221 sought reports were retrieved as full text, and 15 of the 47 core papers could not be retrieved at all. Those 15 are enumerated in section 5 and are the single largest threat to the conclusions below.

### 2.3 Saturation

`saturation-report.json` records status `saturated` against the preregistered taxonomy of 20 evidence domains, with 32 papers read against a preregistered minimum of 20, zero pending core records at the stopping point, and trailing zero novelty in the read-order window. The stopping rule was swept rather than asserted at a single window size: windows of 3, 4, 5, 6, 7 and 8 all return `saturated` with trailing zero novelty. The reported window basis is read-order, not calendar order.

Saturation here means that new reads stopped contributing new preregistered evidence domains. It does not mean that the corpus contains the answer to RQ1, and section 5 argues that it does not.

### 2.4 Reliability of screening decisions

The reliability check reports **Cohen's kappa = 0.675 over 78 of 88 sampled records, with 10 records excluded as unratable**. Observed agreement was 0.769 and expected agreement 0.289. There were 18 recorded disagreements, no blank entries and no unmatched entries.

This measure must be read with an explicit caveat, which `second-rater-report.json` itself records in its `rater_b` field. The second rater was **an independent blind LLM re-prompt, not a human rater**. What the coefficient therefore measures is **decision stability under re-prompting**, not human inter-rater reliability. A conventional kappa of 0.675 would be described as substantial agreement between two human coders; here it means only that an independent pass by the same class of model reproduces roughly three quarters of the recorded decisions. The disagreement pattern is informative in its own right: the confusion matrix shows perfect agreement on `core` (5 of 5) and good agreement on `exclude` (21 of 26), with almost all instability concentrated on the `context` versus `supporting` boundary, which is the boundary that matters least for this synthesis because neither stratum reaches full-text extraction on its own merits.

### 2.5 Quality appraisal

Each of the 32 read papers was scored on an eight-item checklist (aims stated, design appropriate, baseline or control, metrics defined, threats discussed, data or artifacts available, conclusions supported, peer-reviewed venue), with four additional grey-literature items applied to preprints. Rigour is the mean of the scored items. Scores range from 1.00 to 0.188. Six papers fall below the 0.50 flag threshold. Every per-paper entry in section 4 carries its rigour score, and section 3 weights the evidence accordingly.

---

## 3. What the evidence supports, what it rejects, and where it disagrees

### 3.1 The headline: the RQ1 evidence is genuinely split, and the split tracks study quality

The corpus contains a clean, well-evidenced answer to one half of RQ1 and a contested answer to the other half.

The well-evidenced half is negative and concerns the comparator arm. **Giving an agent the same policy as natural-language instructions is a weak control.** This is supported by direct measurements from several independent groups, at several different points in the stack, and the highest-rigour studies agree on it. Restating the policy document before every action barely moves the needle; injecting high-level policy rules into a system prompt cuts violations substantially but leaves enormous cross-model variance; and prompt-level guidance provably cannot bind a model that can route around it through tools.

The contested half is positive and concerns the treatment arm. **Whether the benefit comes specifically from binding the agent to an explicit process model is not established.** The studies that report the largest violation reductions have compiled the policy into an executable artifact of some kind, but the artifacts differ enormously: a per-tool precondition, an SMT constraint, a risk-graph rule set, a structured skill procedure, a world-state invariant. The one study in the corpus that isolates the workflow-template constraint as its own ablation term finds it close to irrelevant.

### 3.2 What the evidence supports

**Compiling policy into an executable precondition reduces violations.** The clearest demonstration holds the agent, the tools and the tasks fixed and swaps only the policy encoding. On the 22 airline tasks whose user request violates policy, the prompt-only baseline reaches pass^1 0.450 and pass^10 0.227, and the generated guards reach 0.685 and 0.500.

> The original τ-bench approach achieves a passˆ1 rate of 0.450 and a passˆ10 rate of 0.227.
>
> *Towards Enforcing Company Policy Adherence in Agentic Workflows* (2025), p. 6

> The fully automated ToolGuards generation and deployment pipeline shows substantial steady gains, improving passˆ1 and passˆ10 to 0.685 and 0.500, respectively – over 20 percentage points above the baseline.
>
> *Towards Enforcing Company Policy Adherence in Agentic Workflows* (2025), p. 6

**Re-prompting the same policy in natural language buys almost nothing.** The same study runs two reflection variants that re-inject either the full policy document or the ground-truth compact policy-to-tool mapping before every agent action. Both land in the same place.

> Both strategies led to only very modest improvements, reaching a passˆ10 of 0.273, with strategy (2) performing slightly better on average.
>
> *Towards Enforcing Company Policy Adherence in Agentic Workflows* (2025), p. 6

**Structured input beats free-text instruction where the decision procedure is already determinate.** Iyenghar et al. (2025) inject the ISO 13849-1 Annex A risk graph verbatim as deterministic mapping rules and compare against a zero-shot prompt containing only the hazard description, over 7,800 scenarios derived from ISO 12100 Annex B.

> Results show that explicit ISO rule-based prompting lifts PL r accuracy from less than 50% (zero-shot) to about 99% with mid-scale, instruction-tuned models.
>
> Iyenghar et al. (2025), p. 1

**Prompt-level policy specification is not a reliable enforcement boundary.** Wu and Gong (2026) run the strongest three-way comparison on identical traces: no enforcement, the same policy injected as high-level rules in the system prompt, and world-state-grounded interception.

> Under the policy-in-prompt condition, risky-case violations drop from 95.3% to 40.7% overall—a substantial reduction, but still leaving 122 violations across 300 risky cases.
>
> Wu and Gong (2026), p. 16

> This suggests that prompt-level policy specification can help when the model attends to the injected rules, but it is not a reliable substitute for world-state-grounded enforcement.
>
> Wu and Gong (2026), p. 16

**Policy text written for humans is a poor specification for agents.** Wang et al. (2026), reporting the FRAMES system on a deployed financial document-auditing workload, diagnose why the prompt-only arm fails rather than merely recording that it does.

> The policy agent fails because the source policies, written for human auditors, neither abstract rules into a general, non-conflicting form nor make edge cases and grounding explicit.
>
> Wang et al. (2026), p. 5

### 3.3 What the evidence rejects, or at least refuses to grant

**It rejects the claim that the gain comes from the process structure itself.** This is the single most important result in the corpus for RQ1, and it comes from its highest-rigour ablation. Wang (2026), reporting Open-Rosalind, binds a biomedical agent to pre-declared workflow templates under a hard step bound with mandatory tool mediation and mandatory traces, then removes each constraint separately across six model families over 1,770 runs with paired seed replications. Removing the workflow template moved aggregate accuracy from 81.4% to 80.5%. Removing tool mediation moved it from 81.4% to 57.3%.

> The strongest and most stable effect is the drop from full to no_tool; citation and template ablations change accountability properties much more than average accuracy.
>
> Wang (2026), p. 9

> Under cluster-aware permutation tests, the full pipeline beats no_tool by 26.4 percentage points on Gemma and 19.3 percentage points on GPT-5-mini
>
> Wang (2026), p. 10

The same study then shows that even the tool-mediation gain is contingent rather than intrinsic. Against a free-form ReAct baseline the constrained pipeline won decisively only where the model was weak at unconstrained tool use, and on the deployment model the two were indistinguishable.

> On Gemma, however, full and ReAct are statistically indistinguishable on the in-house benchmark (p = 0.74).
>
> Wang (2026), p. 10

On an author-independent hold-out the constrained pipeline collapsed below both comparators, and recovered only partially after routing repairs.

> On Gemma, the constrained pipeline collapsed from internal-benchmark performance to 17.8% accuracy and was significantly worse than both ReAct (∆ =−31.1 percentage points, p = 0.004) and no_tool (∆ =−28.9 percentage points, p = 0.002).
>
> Wang (2026), p. 10

**It rejects the claim that the violation reduction is free.** Winston et al. (2026) give the same airline operational policy to one agent as a natural-language document in context and to another as SMT-LIB constraints checked by Z3 as a precondition on every planned tool call. Invalid write calls fell, but write-call recall fell with them, from 0.61 to 0.49, while precision rose from 0.51 to 0.70.

> While the baseline produced a roughly equal proportion of valid and invalid write tool calls, the TaLLM with policy checker reduced the fraction of invalid write tool calls to 29% (measured over all write tool calls).
>
> Winston et al. (2026), p. 4

> This suggests a tradeoff: policy checking improves precision (fewer invalid tool calls) at the cost of a slight reduction in recall (fewer correct tool calls).
>
> Winston et al. (2026), p. 4

This is the sharpest available answer to the second clause of RQ1, and it is nuanced rather than clean. At the level of the tool call there is a real cost: the constrained agent produces fewer correct write calls. At the level of the task there is not: end-to-end success was slightly better and degraded more slowly across repeated trials.

> Overall, both achieve similar success rates, with the policy checker yielding a slight improvement.
>
> Winston et al. (2026), p. 5

**It rejects outcome-only violation scoring as a valid measurement for RQ1.** Rabinovich et al. (2026) define a latent failure as a mutating tool call that was not adequately informed, and detect it by replaying guard code over the trajectory rather than comparing final states.

> We report the latent failure rate on the popular τ 2-bench Airline domain, showing that it ranges between 8% and 17% in successfully completed trajectories across several state-of-the-art open and commercial LLMs.
>
> Rabinovich et al. (2026), p. 2

> Although not explicitly reported in prior work, our experiments suggest that policy violations account for approximately 25% of all simulation failures in the τ 2-bench Airlines domain
>
> Rabinovich et al. (2026), p. 1

The consequence for RQ1 is directional and predictable. Between 8% and 17% of successful trajectories bypass a mandatory check without leaving a trace in the final state. A comparison that scores compliance from final state alone therefore **undercounts violations in the natural-language arm specifically**, because that is the arm in which nothing prevents the skipped check. Any measured advantage for the constrained arm is, on this evidence, an underestimate; and any study reporting parity between arms on final-state metrics has not measured what RQ1 asks about.

**It refuses to grant that task completion and policy conformance are the same construct.** Veli (2026) supplies the cleanest dissociation in the corpus. Removing both validation layers from a warehouse-brokerage pipeline left assignment accuracy unchanged at 0.98 while detected violations fell from 40% to 0%.

> A system that selects the correct warehouse while failing to detect a cold-storage violation is accurate but unsafe, which is why any evaluation reporting only assignment accuracy will miss safety-layer failures.
>
> Veli (2026), p. 102

### 3.4 Where the evidence disagrees, and how the disagreement correlates with quality

Five studies report large violation reductions from compiling policy into an executable constraint. Their rigour scores are 1.00 (compiled tool preconditions), 0.833 (solver-aided SMT verification), 0.938 (the ISO 13849-1 rule graph), 0.792 (structured skill procedures) and 0.792 (world-state invariants). Set against them, the 0.875-rigour ablation that removes the workflow-template constraint specifically finds it close to inert, and attributes the gain to tool mediation instead.

The disagreement is real, but it is not symmetrical, and it is not best described as "some studies find an effect and others do not". Reading the five supporting studies together with the disconfirming ablation, the mechanisms they actually manipulated line up as follows.

| Study | Mechanism actually compiled | Comparator | Reported effect |
|---|---|---|---|
| *Towards Enforcing Company Policy Adherence* (2025) | Per-tool executable precondition | Same policy in prompt, plus two re-injection variants | pass^10 0.227 to 0.500 |
| Winston et al. (2026) | SMT constraint checked before each tool call | Same policy as a document in context | Invalid write calls to 29%; recall 0.61 to 0.49 |
| Iyenghar et al. (2025) | ISO risk-graph mapping rules in the prompt | Zero-shot hazard description | Accuracy under 0.50 to about 0.99 |
| Wang et al. (2026), FRAMES | Structured, step-ordered skill procedures | Same policies supplied in the prompt | Held-out pass rate 0.21 to 0.80 |
| Wu and Gong (2026) | World-state invariants over an organisational graph | Policy injected into the system prompt | 40.7% residual violations to 92.99% accuracy |
| Wang (2026), Open-Rosalind | **Workflow template, ablated on its own** | Same pipeline without the template | 81.4% to 80.5% |

Read this way, the corpus is more coherent than it first appears. What the five supporting studies share is not a process model. It is a **decision procedure that is evaluated outside the model, on an interface the model must pass through**: a tool call, a solver query, a graph mutation, a typed proposal. What Wang (2026) ablated was a different thing: a template that shapes the order in which the model plans, while leaving enforcement elsewhere. The most defensible synthesis is therefore that **mediation, not process structure, is doing the work**, and that "binding to an explicit process model" is a confound in RQ1 as currently phrased unless the binding is enforced at an interface the agent cannot bypass.

Two further papers push in the same direction from opposite ends. Besanson (2026) argues the point from construction rather than measurement.

> Prompt guardrails cannot enforce hard constraints by construction because the model may ignore, reinterpret, or route around them through tools whose effects are off-screen.
>
> Besanson (2026), p. 21

And Lins et al. (2023) show the converse experimentally: a formal process model supplied as prompt context conveys structure well enough for the model to answer questions about it, but does not produce enforcement.

> As it is possible to see, the chatbot assumed the user had already booked the hotel even though that was not explicitly mentioned.
>
> Lins et al. (2023), p. 6

### 3.5 The papers whose numbers most cleanly support "binding works" are the weakest in the corpus

This has to be said plainly, because it is the most likely way for a reader to draw a false conclusion from this corpus.

Four papers report figures that appear to answer RQ1 in the affirmative with no trade-off at all: a 72.7% reduction in governance violations alongside the highest task completion accuracy in the comparison; a 94.7% mean reduction in unauthorised autonomous actions at 87.3% of baseline throughput; a 76.3% reduction in compliance assessment time with a 23.8 percentage-point coverage gain; and an architecture narrative asserting real-time constraint enforcement at enterprise scale. Their rigour scores are **0.438, 0.312, 0.312 and 0.188**. They are the four lowest-scored papers in the corpus after the two remaining sub-0.50 entries. All four are single-author or small-team works in venues without visible peer-review signal; none releases code, data or model identifiers; and three of the four contain figures that contradict other figures in the same paper.

Boinapalli (2026) reports every one of five metrics against every one of six baselines at p < 0.001, releases nothing, and describes a 15-point gap as an 18.3% absolute improvement.

> GALENA achieves a TCA of 0.97, an 18.3% absolute improvement over DataGovAgent (TCA = 0.82), and a 29.3% improvement over DSPy (TCA = 0.75).
>
> Boinapalli (2026), p. 14

Dutta (2026) reports a 90-day, three-site enterprise deployment with no model identification, no per-site sample sizes and no statistical test.

> 94.7% mean reduction in unauthorized autonomous actions (UAAR) compared to fully-autonomous baselines: 96.2% reduction in financial reporting, 93.4% in clinical document processing, and 94.5% in supply-chain optimization.
>
> Dutta (2026), p. 6

Pulikonda (2025) attributes its headline figures inline to third-party references rather than to any described experiment, and reports mutually inconsistent values in different sections (94.2% against 94.7% interpretation accuracy; time-to-compliance falling from 64.3 days to 7.8 in one section and from 63.7 to 7.2 in another).

> the AI -driven approach demonstrated a 76.3% reduction in compliance assessment time compared to traditional manual reviews, while improving compliance coverage by 23.8 percentage points
>
> Pulikonda (2025), p. 7

Onyekaonwu et al. (2024) contains no experiment, no benchmark, no baseline and no measurement, and its industrial case material is explicitly inferred rather than observed.

> In practice, Amazon ’s internal compliance engines likely ingest regulatory updates, map them to internal policy modules, and enforce constraints in real time
>
> Onyekaonwu et al. (2024), p. 13

**No conclusion in this review rests on any of these four papers.** They are retained in the corpus and cited because excluding them silently would misrepresent what a search on this question actually returns, and because the pattern itself is a finding: the cleanest-looking answers to RQ1 in the published record come from the least verifiable studies. Where a claim from these four is repeated above, it is recorded as claimed rather than established.

### 3.6 RQ2: the inventory of empirically evaluated control mechanisms

Collecting across the corpus, the control mechanisms that have actually been evaluated against a stated baseline, rather than merely proposed, are as follows.

| Control mechanism | Evaluated by | Baseline it was measured against |
|---|---|---|
| Executable per-tool precondition generated from a policy document | *Towards Enforcing Company Policy Adherence* (2025) | Same policy in prompt; two policy re-injection variants |
| SMT constraint checked before each tool call, with replanning on UNSAT | Winston et al. (2026) | Same policy as natural-language document in context |
| Deterministic first-order-logic reference monitor over typed action payloads | Wu et al. (2026) | Stateless attribute-based access control; LLM-as-a-Judge |
| World-state invariants over an organisational knowledge graph | Wu and Gong (2026) | No enforcement; policy-in-prompt; content-only DLP |
| Structured, step-ordered skill procedures with per-category non-regression floors | Wang et al. (2026), FRAMES | Prompt-only policy agent; LLM-converted skills; human-edited skills; batch update; a prior skill-evolution method |
| Explicit decision rules injected into the prompt (risk graph) | Iyenghar et al. (2025) | Zero-shot description with no rule logic |
| Pre-declared workflow templates, tool mediation and mandatory traces, ablated separately | Wang (2026), Open-Rosalind | Free-form ReAct with identical tools; three single-constraint ablations |
| Declarative structural validation plus a deterministic rule-based compliance agent | Veli (2026) | Coordination-free sequential calls; seven single-component ablations |
| Four-site constraint placement (pre-action gate, action-time monitor, post-action auditor, escalation router) | Besanson (2026) | Post-hoc audit; output filtering; workflow rules; policy-as-code only |
| Mandatory sandbox graph mutation before decision derivation | Zhu et al. (2026) | Zero-shot frontier models via native function calling |
| Pre-deployment scenario assurance against a compliance digital twin | Gatta (2026) | Conventional suite of 47 unit and 18 integration tests |
| Governance metadata embedded in the machine-readable tool contract | Chaitanya (n.d.) | Zero-shot prompt with basic tool descriptions only |
| Local pre-processing gate with reversible entity pseudonymisation | Park and Madisetti (2025) | Unmodified ToolEmu ReAct prompt |
| Risk-scored human-in-the-loop approval gates | Dutta (2026) | Same LLM and tools with gates disabled |
| Deterministic policy database with LLM advice and human ratification on the residue | Jeong et al. (2025) | None (no baseline arm) |
| Generated test cases and pass/fail gates | Mishra and Senapati (2025) | Human experts, not another agent configuration |
| Mutation-based assurance of the policy engine itself | Qasim and Kadim (2026) | Always-allow and always-deny; policy-only, full-object-gate and envelope-gate ablations |

Three observations follow. First, the baselines are heterogeneous and only four of these studies use the specific comparator RQ1 requires, namely the same policy delivered as natural language to an otherwise identical agent. Second, the strongest comparative designs cluster in the preprint literature rather than in the peer-reviewed venues. Third, several of the highest-rigour entries do not evaluate an LLM agent at all: Besanson (2026) drives a simulated procurement policy, Gatta (2026) drives a scripted probabilistic agent, and Qasim and Kadim (2026) deliberately reduce the model to a transcription role in order to test the mediator rather than the planner. Those studies characterise enforcement architecture, not agent behaviour under instruction, and should not be read as answering RQ1.

### 3.7 Two cross-cutting caveats on the treatment arm

**Compiling the policy is itself unreliable, and is usually done by hand.** Winston et al. (2026) report four successive failed designs for translating natural-language policy into logic, on grounds of syntactic correctness, semantic completeness and constraint tightness, and settle on human-reviewed encodings. Boinapalli (2026), for all its weaknesses, names the same cost.

> Third, the constraint set Ω must currently be defined manually for each new enterprise deployment domain, representing a non -trivial configuration burden that limits rapid onboarding to novel regulatory environments.
>
> Boinapalli (2026), p. 16

**Enforcement is only as complete as the declared constraint set, and its recall is bounded by world-model coverage rather than by constraint sophistication.** Wu et al. (2026) state the limit of formal guarantees exactly.

> Consequently, the verifier fundamentally proves the absence of violations against explicitly defined axioms, rather than the absence of unsafe behaviors.
>
> Wu et al. (2026), p. 14

Anand et al. (2026) add the complementary diagnostic from the measurement side: agents fail procedural compliance by skipping mandated gating reads before writes, not by misordering steps, which is precisely the failure class a sequence-oriented process model is least equipped to catch and a precondition-oriented mediator is best equipped to catch.

> These missing tool calls in particular manifest themselves in the habit of weaker models to write prematurely, i.e., to call a write-style tool before any read-style tool.
>
> Anand et al. (2026), p. 13

---

## 4. Per-paper entries, ordered by contribution

Ordering is by contribution to RQ1 and RQ2, not by rigour and not by date. Each entry gives the APA citation from `manifest.json`, the rigour score from `quality.json`, and one to three page-anchored quotations verified against the extracted corpus.

### 4.1 Direct tests of the RQ1 contrast

#### 1. Compiled tool preconditions versus the same policy re-prompted

Towards Enforcing Company Policy Adherence in Agentic Workflows. (2025). Underline Science Inc., 595-606. https://doi.org/10.18653/v1/2025.emnlp-industry.41

Rigour 1.00 (8 of 8 items scored). Peer-reviewed conference paper. The only paper in the corpus to score full marks, and the closest direct test of RQ1: the agent, tools and tasks are held fixed and only the policy encoding changes. An offline stage maps a free-form policy document onto the airline toolset and generates executable guards by test-driven development; at runtime each guard runs immediately before its tool call, blocks on violation, and returns the violated policy for revision. Compliance and completion are scored together by the benchmark's pass metric rather than traded off. The authors state the boundary of the result themselves.

> First, the proposed approach operates at the pre-tool activation level, meaning it does not capture violation cases where a tool (e.g., flight cancellation) should be invoked according to policy, but the agent chooses not to, thereby breaching the guidelines.
>
> *Towards Enforcing Company Policy Adherence in Agentic Workflows* (2025), p. 7

#### 2. Solver-aided verification, and the price of the reduction

Winston, C., Winston, C., & Just, R. (2026). Solver-Aided Verification of Policy Compliance in Tool-Augmented LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2603.20449

Rigour 0.833 (12 of 12 items scored). **Preprint.** The second direct RQ1 test, and the only one to report both dependent variables at the level of the tool call rather than only at the level of the task. Fifty tasks, thirteen tools, a 1,242-word policy document, four trials per task with pass^k reporting. Its second contribution is a rare negative result on the upstream translation step, which makes the compliance gain contingent on human-curated encodings rather than on automated policy compilation.

> However, prompt-based guidance does not provide reliable policy enforcement. As policies grow longer and more complex, purely prompt-based enforcement becomes increasingly brittle and harder to validate.
>
> Winston et al. (2026), p. 2

#### 3. The ablation that removes the process constraint and finds it nearly inert

Wang, L. (2026). Open-Rosalind: Tool-First Biomedical LLM Agents with Process-Aware Benchmarking. https://doi.org/10.64898/2026.05.06.722404

Rigour 0.875 (12 of 12 items scored). **Preprint** (posted to a preprint server, with the extracted text carrying the "not certified by peer review" watermark). The single most consequential study in this corpus for RQ1, because it treats the constraint as the experimental variable rather than as the intervention. Five conditions over 1,770 runs across six model families, with cluster-aware permutation tests on paired seed replications and an author-independent hold-out. Its diagnosis-and-repair reporting, in which a collapsed hold-out result is traced to routing and normalisation defects and partially recovered, is a methodological template worth carrying into any replication of RQ1. The three decisive quotations appear in section 3.3, the most important being the ablation summary at p. 9, which attributes the effect to tool mediation rather than to the template. The scope limitation matters for how far that null result travels.

> The harness templates are hand-coded; while their fixity is a feature for reproducibility, it bounds the range of workflows the system can express.
>
> Wang (2026), p. 13

A template that is fixed by hand for reproducibility is a weaker form of process binding than a mined or modelled process, so this study bounds the claim that process structure is inert rather than settling it.

#### 4. Structured skill procedures against the same policy in the prompt

Wang, X., Shu, R., Dan, C., Xu, T., Luo, M., Mai, Y., & Wan, B. (2026). FRAMES: Guarded and Dual-Objective Skill Evolution for Agents in Policy-Governed Enterprise Workflows. arXiv preprint. https://doi.org/10.48550/arxiv.2608.01772

Rigour 0.792 (12 of 12 items scored). **Preprint.** The comparator is exactly the RQ1 control arm, and it is named as such.

> B1 Raw LLM: the policy agent with policies Π supplied in its prompt and no skill bank S.
>
> Wang et al. (2026), p. 5

On a held-out set of 210 production financial document-auditing cases, that prompt-only arm reaches a total pass rate of 0.21, against 0.80 for the evolved structured skills, with the gap concentrated in the hallucination and special-case categories where the prompt-only and naively converted arms score 0.04 and 0.00.

> FRAMES reaches the best overall pass rate, leading the strongest baseline B5 in every category by 0.07–0.11
>
> Wang et al. (2026), p. 5

The generalisation caveat is severe and the authors state it: the main evidence is an internal production corpus, because nothing public tests the target construct.

> No public benchmark tests what FRAMES targets, the closest option, document-QA, only asks fixed questions over documents and does not test skill execution
>
> Wang et al. (2026), p. 7

#### 5. Policy-invisible violations, and the three-way enforcement comparison

Wu, J., & Gong, M. (2026). Policy-Invisible Violations in LLM-Based Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2604.12177

Rigour 0.792 (12 of 12 items scored). **Preprint.** Isolates the failure class that makes natural-language policy specification insufficient in principle: violations whose decisive facts are absent from the agent-visible context, in a cooperative and non-adversarial setting. Contributes a 120-case benchmark of matched violation and safe pairs across eight categories, with all tool responses stripped of policy metadata, and an enforcement layer that speculatively applies proposed mutations to an organisational graph and checks seven declarative invariants. All 600 baseline and 600 policy-in-prompt traces were human-reviewed. Its two comparative quotations appear in section 3.2. The more transferable result is the coverage-degradation experiment, in which enforcement recall falls monotonically from 100% to 20% as world-model coverage is removed, with zero false positives at every level.

> These results support the central claim: the binding constraint on enforcement quality is world-model coverage, not invariant sophistication.
>
> Wu and Gong (2026), p. 20

That finding relocates the practical difficulty of the treatment arm. Building the constraint is not the hard part; supplying the facts the constraint needs is.

#### 6. Explicit decision rules versus zero-shot instruction, on a determinate task

Iyenghar, P., Mansour, Z., & Wuebbelmann, J. (2025). Evaluation of Automated Machinery Functional Safety Risk Assessment Using LLMs. IEEE Access, 13, 203648-203669. https://doi.org/10.1109/access.2025.3632528

Rigour 0.938 (8 of 8 items scored). Peer-reviewed journal. Not an agent study, but the cleanest controlled ablation of the RQ1 contrast between an explicit decision model and unstructured natural language. Two secondary findings matter for RQ2: retrieval augmentation on top of the rules adds essentially nothing to accuracy while adding up to 56.87 seconds of latency per sample, and the benefit of structured input is model-capacity-dependent, since one small open model never exceeds 0.410 accuracy even with the rules supplied.

> rule-based prompts improved PL r classification accuracy by over 50 percentage points, highlighting the essential role of structured input for deterministic safety tasks.
>
> Iyenghar et al. (2025), p. 21

The generalisation limit is important and cuts against over-reading the result: this is single-turn classification with a deterministically computed ground truth, no tools, no state mutation and no task-completion dimension, so it cannot speak to the completion side of the RQ1 trade-off at all.

### 4.2 Measurement and construct validity

#### 7. Latent policy failures inside successful trajectories

Rabinovich, E., Boaz, D., Zwerdling, N., & Anaby-Tavor, A. (2026). Near-Miss: Latent Policy Failure Detection in Agentic Workflows. arXiv (Cornell University), 296-308. https://doi.org/10.48550/arxiv.2603.29665

Rigour 0.917 (12 of 12 items scored). **Preprint.** The highest-rigour preprint in the corpus, and the paper that most directly threatens the validity of any outcome-only RQ1 comparison. The detector was validated against author annotation, and the authors are explicit that annotation was in-house rather than independent.

> Both Claude-Sonnet4 and Kimi-K2.5 show near-miss rate (NMR) of 7% per human annotation.
>
> Rabinovich et al. (2026), p. 6

The two headline quotations appear in section 3.3. Note that the guard code is replayed offline for evaluation and is not enforced at runtime, so this study measures the blind spot rather than closing it.

#### 8. Deterministic grading of procedural compliance at scale

Anand, A., Chatzi, I., Raha, R., & Schmuck, A.-K. (2026). MANTRA: Synthesizing SMT-Validated Compliance Benchmarks for Tool-Using LLM Agents. arXiv preprint. https://arxiv.org/abs/2605.06334

Rigour 0.875 (12 of 12 items scored). **Preprint.** Solves the measurement problem behind RQ1: how to decide deterministically whether a tool-call trace followed a natural-language procedural manual. The design is directly relevant to RQ2 because the process model functions as an oracle while the agent still receives only the manual, which is exactly the configuration needed to measure the natural-language arm honestly. Across 285 validated cases in six domains, agent pass@1 ranges from 28.1% to 57.7%.

> Another interesting observation is that none of the used models reached very high procedural compliance.
>
> Anand et al. (2026), p. 13

> MANTRA does not provide full formal certification of compliance with the original document.
>
> Anand et al. (2026), p. 13

#### 9. Assurance of the policy engine itself

Qasim, H. F., & Kadim, S. A. (2026). PolicyFaultBench: Mutation-Based Assurance of Policy Mediation and Proposal-Interface Conformance for Tool- Using AI Agents. Research Square. https://doi.org/10.21203/rs.3.rs-10502893/v1

Rigour 0.792 (12 of 12 items scored). **Preprint.** Turns the policy from a trusted given into an object of assurance by applying twelve first-order mutation operators to two independently implemented policy architectures. The result is a warning to anyone who plans to answer RQ1 by building a corpus: high execution success on a corpus does not imply that the corpus can expose policy faults.

> The frozen corpus killed 7 of 12 mutants (58.33%). Subject widening, approval bypass, temporal deletion, fail-open exception handling, and reset omission survived.
>
> Qasim and Kadim (2026), p. 9

> Mutation adequacy did not transfer automatically. The external corpus killed only 2/12 ordered-rule mutants and 1/12 capability mutants before targeted probes.
>
> Qasim and Kadim (2026), p. 12

A second result speaks to the completion side of RQ1: strictness cost availability without buying safety, since nine benign proposals were quarantined purely for adding an unrequested approval-scope annotation.

> OpenAI met the compound endpoint in 400/400 trials. Anthropic met it in 391/400: nine outputs for one benign payment case added an unrequested approval-scope ﬁeld and were quarantined before policy evaluation.
>
> Qasim and Kadim (2026), p. 2

#### 10. Accuracy and conformance dissociated by ablation

Veli, E. (2026). A stigmergy-driven multi-agent framework for intelligent task orchestration. UPCommons institutional repository (Universitat Politècnica de Catalunya). https://hdl.handle.net/2117/463237

Rigour 0.833 (12 of 12 items scored). **Preprint** (master's thesis in an institutional repository). Carries the most thorough evaluation design in the corpus: 790 controlled runs across nine ablation configurations with expert-defined ground truth, effect sizes reported as Cliff's delta because the paired tests are underpowered, and a two-by-two factorial analysis of the two validation layers. It separately ablates five distinct control mechanisms and ranks their marginal contributions, which makes it the richest single source for RQ2.

> 48 percentage points in assignment accuracy and 40 percentage points in violation detection, at a measured cost of only 6.6% additional latency and 9.7% additional token consumption (H5).
>
> Veli (2026), p. 122

> All results derive from a single synthetic domain with five client archetypes and ten agents.
>
> Veli (2026), p. 115

The dissociation quotation appears in section 3.3.

### 4.3 Enforcement architectures evaluated against non-LLM or simulated agents

#### 11. Formal verification against the two mechanisms practitioners deploy

Wu, B., Zhang, W., Chen, K., Fang, H., & Yu, N. (2026). Provably Secure Agent Guardrail. arXiv (Cornell University). https://arxiv.org/abs/2605.29251

Rigour 0.833 (12 of 12 items scored). **Preprint.** Refuses natural-language intent at the enforcement boundary: actions must be serialised into typed payloads, compiled deterministically into first-order logic and checked by an SMT solver, so unsafe transitions become unsatisfiable rather than blocked by judgement. Valuable for RQ2 because the comparators are the two controls actually in production use, stateless attribute-based access control and LLM-as-a-Judge, run across six front-end models.

> In the Multi-Step Financial Transfer task, the mechanism achieved a zero attack success rate and a zero false positive rate across state-of-the-art models.
>
> Wu et al. (2026), p. 3

> For models that use LLM-as-the-Judge, the results are unstable.
>
> Wu et al. (2026), p. 10

The authors describe their experiments as illustrative realisations rather than statistically representative benchmarks, and the guarantee quotation in section 3.7 is the qualification that matters most for RQ1.

#### 12. Constraint placement as the independent variable

Besanson, G. (2026). SARC: A Governance-by-Architecture Framework for Agentic AI Systems. arXiv (Cornell University). https://arxiv.org/abs/2605.07728

Rigour 0.792 (12 of 12 items scored). **Preprint.** Compiles each constraint declaration into one of four enforcement sites in the agent loop and compares five governance regimes over 50 seeds. Unusually careful about attribution: the reduction is credited to where the declared response was placed, not to the framework label, and the authors state that a policy-as-code system with the same response would perform similarly.

> SARC reduces soft-window overages from ∼937 (policy-as-code-only) to 98.8± 1.0, a 89.5% reduction at 95% confidence.
>
> Besanson (2026), p. 30

> First, the environment is synthetic and intentionally stylized; results from a synthetic procurement task do not generalize to real procurement, customer-service, or clinical settings without further empirical work.
>
> Besanson (2026), p. 32

The critical qualifier for RQ1 is that the agent is a simulated procurement policy rather than an LLM, so the study measures enforcement architecture and not agent behaviour under instruction. Its constructive argument appears in section 3.4.

#### 13. Scenario conditions as soft preferences when supplied as prompt text

Zhu, H., Liang, J., Hou, M., Tang, R., Zhu, X., Yang, J., Mao, Y., & Wu, F. (2026). From Business Events to Auditable Decisions: Ontology-Governed Graph Simulation for Enterprise AI. arXiv (Cornell University). https://arxiv.org/abs/2604.08603

Rigour 0.625 (12 of 12 items scored). **Preprint.** Argues explicitly against the natural-language arm of RQ1: scenario conditions injected as prompt instructions are treated as soft preferences, so the model may still act on the unrestricted graph. Its most transferable contribution is a measurement idea, separating answer accuracy from tool-chain F1 and defining their difference as an illusive-accuracy index.

> Of 50 outputs: 47 produced correct binary answers with zero tool calls (pure natural language responses);
>
> Zhu et al. (2026), p. 13

> LOM-action achieves 1.00 accuracy against 0.66 and 0.64 for the baselines—a 34-point gap attributable to Phase 2 bypass
>
> Zhu et al. (2026), p. 12

The comparison is confounded and the authors concede it: the proposed system is fine-tuned while the baselines are zero-shot, and the controlled ablation that would separate architecture from training was not run.

#### 14. Pre-deployment scenario assurance against a process model

Gatta, V. S. (2026). Compliance Digital Twins for Autonomous Financial Agents: Reliability-Aware Scenario Assurance via Calibrated LLM Evaluation. Journal of International Crisis and Risk Communication Research, 168-181. https://doi.org/10.63278/jicrcr.vi.3783

Rigour 0.625 (8 of 8 items scored). Peer-reviewed journal. Uses an explicit process model as the normative baseline against which agent behaviour is judged, and converts an estimated violation risk into a three-level autonomy policy. Note that the reported baseline detection rate is 43% in the text and 47% in the per-family table.

> The CDT detected 89% of injected compliance violations and authorization failures before simulated deployment, compared with 43% for the conventional test suite, a 46 percentage -point improvement.
>
> Gatta (2026), p. 11

> These results are reported for a controlled simulation on a single synthetic workflow and should be interpreted as indicative rather than definitive.
>
> Gatta (2026), p. 12

The decisive caveat is that the agents were not LLM agents: agent behaviour was a probabilistic but scripted decision model, so the detection gains are properties of the assurance harness.

#### 15. Governance moved into the tool contract

Chaitanya, P. (n.d.). OpenMCPSpec: A Specification Framework for Robust, Governed, and Lifecycle-Managed Machine Communicable Processes in LLM-Agent Systems. 2026 Fourth International Conference on Secure Cyber Computing and Communications (ICSCCC). https://ieeexplore.ieee.org/document/11600150/

Rigour 0.500 (8 of 8 items scored). Conference paper. A close structural analogue of RQ1 at the tool-call level: the baseline is a zero-shot prompt carrying only basic tool descriptions, and the treatment is the same tools bound to an explicit specification. Nine of ten policy rules leaked without the specification and passed with it. The reliability evidence is far weaker, and the metric definition does not match the reported table, which reports execution times in seconds rather than argument-correctness rates.

> ACI specifically measures the reduction in argument hallucination and the resulting gain in tool-calling accuracy [6] when OpenMCPSpec is used compared to a basic MCP baseline.
>
> Chaitanya (n.d.), p. 4

> Free Cloud Ollama API key with REST API with Cloud llm & SQLite MCP server for a Total of 20 tests were run into two groups
>
> Chaitanya (n.d.), p. 5

The authors also report the one negative case in their own results, which is the most useful thing in the paper for RQ1's completion side.

> The 'Semantic Summary' performance drop (-23.7%) occurred because strict nlp_hints over-constrained the LLM during inherently broad tasks, adding unnecessary token overhead.
>
> Chaitanya (n.d.), p. 5

### 4.4 Process models as context rather than as control

#### 16. How much compliance is recoverable from natural-language context alone

Kölbel, L. M., Poss, L., & Schönig, S. (2026). Context is key for cybersecurity: leveraging external knowledge for process model explanation via LLMs. International Journal of Information Security, 25(4). https://doi.org/10.1007/s10207-026-01245-x

Rigour 0.812 (8 of 8 items scored). Peer-reviewed journal. Runs the RQ1 relationship in the opposite direction: it hands a process model plus an unstructured standard to a model and measures how well compliance can be decided. This quantifies the ceiling of the natural-language arm.

> The baseline strategy, nothing, achieved accuracy of only 49.3%. In contrast, simply adding context ( context) boosted accuracy to 70.4%, and the most effective strategy, contextFewShot, reached 74.6%.
>
> Kölbel et al. (2026), p. 16

Its most transferable contribution is a four-part error typology that reframes the compliance bottleneck away from fabrication and toward mapping structured process semantics onto unstructured rules.

> the most significant source of failure was Reasoning Failure, accounting for 49 instances, followed by Input Interpretation Failure (12) and Context Retrieval Failure (23).
>
> Kölbel et al. (2026), p. 18

One internal inconsistency should be noted when citing it: the results section counts 12 input-interpretation failures across 86 non-correct instances while the discussion reports 4 across 78. The paper also documents a measurement threat directly relevant to this review, in that its automated judge agreed with human raters only fairly (Cohen's kappa 0.3909).

#### 17. A process model in the prompt conveys structure but does not enforce it

Lins, L. F., Nascimento, N., Alencar, P., Oliveira, T., & Cowan, D. (2023). Comparing Generative Chatbots Based on Process Requirements: A Case Study. https://doi.org/10.1109/bigdata59044.2023.10386251

Rigour 0.750 (8 of 8 items scored). Peer-reviewed conference paper. Tests the weakest possible form of the RQ1 intervention: hand the model the process model as XML, instruct it to honour the restrictions, and see whether behaviour is constrained when no engine enforces anything. Both evaluated models let the user execute a task that was not yet enabled and both only partially handled the exclusive gateway, despite very different overall scores.

> In the Trip Planning scenario, GPT achieved a score of 92.31% in terms of meeting the evaluation questions, while PaLM only met 69.23% of the questions.
>
> Lins et al. (2023), p. 9

The state-fabrication quotation appears in section 3.4. Evidence rests on one process model, three construct types and two models, all qualitatively scored by the authors.

#### 18. Why natural language is the wrong notation for agent workflows

Ait, A., Izquierdo, J. L., & Cabot, J. (2025). Towards Modeling Human-Agentic Collaborative Workflows: A BPMN Extension. Lecture notes in computer science, 367-382. https://doi.org/10.1007/978-3-032-04190-6_22

Rigour 0.750 (8 of 8 items scored). Peer-reviewed conference paper. The clearest statement of the RQ1 mechanism as a modelling problem rather than a control problem: standard notation can only express agent collaboration, reflection strategies and agent uncertainty through free-text annotation.

> We rely on natural language to describe the collaboration and reflection strategies, which can lead to ambiguity and misinterpretation.
>
> Ait et al. (2025), p. 3

> Finally, we plan to empirically evaluate our extension and explore its application in industrial use cases.
>
> Ait et al. (2025), p. 8

Contributes a control-mechanism taxonomy and an explicit trust-score construct, but no benchmark and no measured effect on violations or completion.

#### 19. Generating the constraint artefacts themselves

Santos, W. D. S., Coutinho, J. R., Baião, F., Spyrides, G. M., & Lopes, H. (2025). Enhancing declarative business process management availability through generative AI. Process Science, 2(1). https://doi.org/10.1007/s44311-025-00029-1

Rigour 0.938 (8 of 8 items scored). Peer-reviewed journal, and one of the three highest-rigour papers in the corpus. Sits upstream of RQ1: rather than binding an agent to a process model, it manufactures declarative process models, and compares two constrained-generation mechanisms over 2,000 synthetic models. Relevant to RQ2 because declarative models constrain by prohibition rather than by prescribing a sequence, which is the alternative to the imperative binding RQ1 assumes.

> While our framework achieves high accuracy in basic constraint generation, we observed increased variability in handling complex negative constraints and intricate temporal conditions.
>
> Santos et al. (2025), p. 47

> dataset for MP-Declare models makes it difficult to definitively assess the quality and representativeness of our generated models against real-world examples.
>
> Santos et al. (2025), p. 47

The evaluation concerns artefact quality, not agent behaviour, so it contributes no violation or completion data.

#### 20. The vision that names the gap this review targets

Kampik, T., Warmuth, C., Rebmann, A., Agam, R., Egger, L., Gerber, A., Hoffart, J., Kolk, J., Herzig, P., Decker, G., van der Aa, H., Polyvyanyy, A., Rinderle‐Ma, S., Weber, I., & Weidlich, M. (2024). Large Process Models: A Vision for Business Process Management in the Age of Generative AI. K&uuml;nstliche Intell., 39(2), 81-95. https://doi.org/10.1007/s13218-024-00863-8

Rigour 0.562 (8 of 8 items scored). Peer-reviewed journal, vision paper, with a declared conflict of interest noting that all non-academic authors work for a process-management software vendor. Its architectural claim is the conceptual core of RQ1.

> due to their stochasticity, we assume that LLMs do not play a role in orchestration.
>
> Kampik et al. (2024), p. 5

> what is still missing are experimental works that provide solid evidence for the effectiveness of LLMs in a process execution context.
>
> Kampik et al. (2024), p. 11

The second quotation is the reason this review exists, and the fact that it was written in 2024 by fifteen authors spanning the field is itself evidence that the gap is acknowledged rather than merely asserted here.

#### 21. Relaxing a process model rather than constraining an agent

Ye, Y., Cong, X., Tian, S., Cao, J., Wang, H., Qin, Y., Lu, Y., Yu, H., Wang, H., Lin, Y., Liu, Z., & Sun, M. (2023). ProAgent: From Robotic Process Automation to Agentic Process Automation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2311.10751

Rigour 0.542 (12 of 12 items scored). **Preprint.** The inverse of the RQ1 intervention: instead of constraining an agent with a process model, it relaxes a process model by embedding agent nodes at the points that need judgement. Useful for characterising where a binding process model must leave discretion. Evidence is a single proof-of-concept on one commercial task, with no metrics, no baseline and no compliance measurement. Its safety discussion is more valuable than its results.

> Humans may shift their trust in the stability of traditional rule-based workflows to agents, mistakenly believing that the agent’s decision-making processes are equally reliable
>
> Ye et al. (2023), p. 9

### 4.5 Deployment reports and adjacent control mechanisms

#### 22. Constrained representations and the completion cost

Park, J. H., & Madisetti, V. K. (2025). CAPRI: A Context-Aware Privacy Framework for Multi-Agent Generative AI Applications. IEEE Access, 13, 43168-43177. https://doi.org/10.1109/access.2025.3549312

Rigour 0.688 (8 of 8 items scored). Peer-reviewed journal. Structurally analogous to RQ1 in that it measures what happens to task completion when an agent must operate over a constrained, structured representation instead of raw input. The finding is a graded utility cost: light structure helped, heavy transformation degraded success because referential integrity broke inside reasoning traces.

> The entity-only configuration improved the success rate by 4% and reduced the number of conversational turns by 1.3 compared to the baseline.
>
> Park and Madisetti (2025), p. 8

> Although the integration of entity structures into user queries yielded improvements, the overall success rate for all four (4) configurations remained limited to a maximum of 64%.
>
> Park and Madisetti (2025), p. 9

The paper reports no compliance or violation metric at all, so it speaks only to the completion side of RQ1.

#### 23. A runtime verifier design with the right metrics and no results

Begum, S., & Rosenzweig, M. (2026). A Privacy-Preserving On-Device Multi-Agent Architecture for AI PC (POMA) Workflow Automation. 2026 IEEE International Conference on AI and Data Analytics (ICAD), 1-8. https://doi.org/10.1109/icad69378.2026.11608651

Rigour 0.625 (8 of 8 items scored). Peer-reviewed conference paper. Articulates the RQ1 dependent-variable pair unusually cleanly, defining task completion rate and policy overhead alongside unsafe-action rate, true block rate, escalation accuracy and confirmation burden. It reports no results at all: the evaluation section is a proposed methodology, and the named baselines and ablations are planned rather than executed.

> actions must be verified at execution time, not trusted by default.
>
> Begum and Rosenzweig (2026), p. 4

> Baselines: (i) CUA -only without verifier gating, (ii) singleagent end -to-end baseline, (iii) optional cloud -first baseline (if permitted).
>
> Begum and Rosenzweig (2026), p. 7

Useful to RQ2 as a control-mechanism taxonomy and as a metric template, but it contributes no empirical evidence.

#### 24. The trust vocabulary, and the autonomy distinction RQ1 depends on

Schwartz, S., Yaeli, A., & Shlomov, S. (2023). Enhancing Trust in LLM-Based AI Automation Agents: New Considerations and Future Challenges. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2308.05391

Rigour 0.625 (12 of 12 items scored). **Preprint** (workshop position paper). Contributes a named catalogue of control considerations rather than results, and draws the operational distinction that RQ1 relies on.

> Autonomous Actions. Agents that perform autonomous actions that may influence the business without any human supervision.
>
> Schwartz et al. (2023), p. 7

> We note that this is not a detailed comparison and might not reflect the entire abilities of the tools but rather our own opinion after trying these models.
>
> Schwartz et al. (2023), p. 8

The self-assessment in the second quotation is accurate and should be respected: there is no measurement, no task set and no violation count here.

#### 25. Deterministic policy first, model second, human last

Jeong, C., Sim, S., Cho, H., Kim, S., & Shin, B. (2025). E2E Process Automation Leveraging Generative AI and IDP-Based Automation Agent: A Case Study on Corporate Expense Processing. Artificial Intelligence and Applications. https://doi.org/10.47852/bonviewaia52026307

Rigour 0.562 (8 of 8 items scored). Peer-reviewed journal. An industrial deployment report in which an explicit policy database, not the language model, carries the compliance decision on the routine path, with the model confined to advisory handling of the residue and the human decision persisted back as new policy. For RQ2 that is a concrete hybrid control mechanism deployed at production scale. Evidentially it is thin: one confusion matrix over 1,448 receipts, no baseline arm, and the widely quoted time saving presented explicitly as an expected effect derived from general adoption cases.

> An F1 score of 0.90 indicates that the model is performing well in both precision and recall
>
> Jeong et al. (2025), p. 22

> Third, since the decision-making process of generative AI operates as a black box, ensuring trustworthiness and explainability in judgments is required.
>
> Jeong et al. (2025), p. 23

#### 26. Test-driven gating, benchmarked against humans rather than agents

Mishra, L. N., & Senapati, B. (2025). Retail Resilience Engine: An Agentic AI Framework for Building Reliable Retail Systems With Test-Driven Development Approach. IEEE Access, 13, 50226-50243. https://doi.org/10.1109/access.2025.3552592

Rigour 0.562 (8 of 8 items scored). Peer-reviewed journal. Contributes a control mechanism of a different kind, generated test cases and pass/fail gates, but evaluated against a human-expert baseline rather than against another agent configuration. There is no policy, no violation metric and no compliance-critical process, so it carries no weight for RQ1. Reported numbers are internally inconsistent: the abstract and conclusion claim a 97.5% similarity index while the body reports a correlation of 0.96, and filtering accuracy is given as 98.2%, 98.20% and 98.22% in different places.

> The ρ is 0.96, which means that the decision made by the proposed system is 96% similar to the decision made by human specialists.
>
> Mishra and Senapati (2025), p. 12

> While the engine performs well across various retail domains, its effectiveness is currently limited to predefined categories such as inventory management and demand forecasting.
>
> Mishra and Senapati (2025), p. 15

Evaluation samples are very small: ten queries for the alignment experiment and ten domains for robustness.

### 4.6 Below the quality threshold

The six papers in this group score below the 0.50 flag threshold in `quality.json`. They are reported for completeness and for the finding described in section 3.5. **No conclusion in this review rests on any of them.**

#### 27. A process model compiled into agent nodes, with no comparison run

Tebourbi, H., Nouzri, S., Mualla, Y., Fatimi, M. E., Najjar, A., Abbas-Turki, A., & Dridi, M. (2025). BPMN-Based Design of Multi-Agent Systems: Personalized Language Learning Workflow Automation with RAG-Enhanced Knowledge Access. Information, 16(9), 809. https://doi.org/10.20944/preprints202507.1291.v1

Rigour 0.438, flagged low (8 of 8 items scored). **Preprint**, despite the journal-style citation string: the manifest marks it as not a preprint while the retrieved document carries a "not peer-reviewed version" header from a preprint server, and the quality appraisal scored the peer-review item accordingly. The mechanism is exactly the RQ1 intervention, with process elements compiled one-to-one into agent nodes, tool nodes, routers and message edges. The domain, however, is language tutoring, so no policy or violation construct exists. The only claimed comparison against an unconstrained agent is an assertion whose numbers are explicitly withheld.

> These results indicate strong contextual grounding (0.87) and high alignment between retrieved passages and generated answers, effectively reducing hallucination compared to a baseline single-agent LLM (not shown).
>
> Tebourbi et al. (2025), p. 20

> Human Validation Bottleneck: Teacher-in-the-loop content approval, while ensuring accuracy, creates scalability challenges for large learner groups.
>
> Tebourbi et al. (2025), p. 21

#### 28. The cleanest-looking RQ1 result in the corpus, and the least verifiable

Boinapalli, N. R. (2026). GALENA: A Governance-Aware LLM Enterprise Navigation Architecture for Autonomous Multi-Agent Workflow Automation with Compliance Enforcement. https://doi.org/10.64971/j.cph.eijtem.v13.i3.12.2026

Rigour 0.438, flagged low (8 of 8 items scored). Journal article by a single author, in a venue with a non-standard identifier prefix and no visible peer-review signal. On its face this maps more directly onto the RQ1 contrast than anything else in the corpus, because its six baselines represent the policy-as-prompt or post-hoc-filter condition and it reports both dependent variables jointly.

> On GVR, GALENA reaches 0.03 — a 72.7% reduction relative to DataGovAgent (GVR = 0.11) and an 86.4% reduction relative to DSPy (GVR = 0.22).
>
> Boinapalli (2026), p. 14

Every metric against every baseline is reported at p < 0.001, no artefacts or datasets are released, and the arithmetic in the headline claim does not hold, as shown in section 3.5. Its stated limitation about manual constraint authoring, quoted in section 3.7, is the most useful sentence in the paper.

#### 29. A secondary source that relays performance claims without appraisal

Wahab, M. B. A., Mazen, S. A., & Helal, I. M. A. (2025). Utilizing Large Language Models in Business Process Management: Applications and Challenges. Journal of Computer Science, 21(8), 1921-1932. https://doi.org/10.3844/jcssp.2025.1921.1932

Rigour 0.438, flagged low (8 of 8 items scored). Peer-reviewed journal. A review of 42 studies across the process-management lifecycle, with no formal quality appraisal or risk-of-bias assessment described. It frames the trade-off RQ1 targets but leaves it unresolved, and it relays primary-study numbers without method or citation, which is exactly how an under-evidenced claim propagates into received wisdom.

> prompt engineering improved conversational interfaces’ usability by 72 % in a 17-company pilot
>
> Wahab et al. (2025), p. 7

> It is also crucial to find the right balance between the adaptability of LLMs and the structured requirements of formal BPM systems.
>
> Wahab et al. (2025), p. 8

#### 30. Risk-gated human approval, reported without verifiable method

Dutta, P. (2026). Accountable Multi-Agent AI Systems: Orchestration Frameworks for Enterprise Workflow Automation with Human-in-the-Loop Verification. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.19845387

Rigour 0.312, flagged low (8 of 8 items scored). **Preprint** deposited in a general-purpose repository, single author. The reported experiment has the right shape for RQ1, because the control condition is the same model and tool configuration with the gates disabled and both dependent variables are reported together. The mechanism is risk-gated human approval rather than binding to a process model, so it belongs in the RQ2 inventory rather than as an answer to RQ1, and the absence of model identification, sample sizes, statistical tests and released data means the figures are recorded as claimed rather than established.

> Task throughput was maintained at 87.3% of baseline — the 12.7% overhead attributable primarily to Type-II HITL gate latency, with a mean human review time of 4.2 minutes per gate.
>
> Dutta (2026), p. 6

The headline violation-reduction claim is quoted in section 3.5.

#### 31. Directionally interesting, evidentially empty

Pulikonda, N. K. M. (2025). Real-Time Regulatory Intelligence Framework: LLM-powered compliance automation for financial services. World Journal of Advanced Engineering Technology and Sciences, 15(2), 3106-3115. https://doi.org/10.30574/wjaets.2025.15.2.0784

Rigour 0.312, flagged low (8 of 8 items scored). Journal article, single author. No experimental protocol, sample construction, model identity, statistical test, code or data is given, and headline figures are mutually inconsistent across sections. One directional observation is nonetheless consistent with the rest of the corpus and worth recording, namely that determinate rules are handled far better than provisions requiring contextual interpretation.

> Accuracy analysis revealed performance degradation for highly interpretive regulations that rely on subjective standards, with accuracy dropping to 84.7% for principles -based provisions compared to 96.8% for rules -based requirements
>
> Pulikonda (2025), p. 7

That pattern is exactly what the RQ1 hypothesis predicts, which is precisely why it should not be leaned on when the source cannot support it. The 76.3% claim is quoted in section 3.5.

#### 32. Vocabulary without evidence

Onyekaonwu, C. B., Igba, E., & Anyebe, A. C. P. (2024). Agentic AI for Regulatory Intelligence: Designing Scalable Compliance Lifecycle Systems in Multinational Tech Enterprises. International Journal of Scientific Research and Modern Technology., 205-222. https://doi.org/10.38124/ijsrmt.v3i12.934

Rigour 0.188, flagged low, the lowest score in the corpus (8 of 8 items scored). Journal article. A narrative review that states no search protocol, inclusion criteria or quality appraisal, and whose industrial case material is inferred from public sources as quoted in section 3.5. Its one transferable idea for RQ2 is an externalised control layer that intercepts agent actions and evaluates them against declarative rules without modifying agent internals, which is architecturally the inverse of embedding policy in the prompt.

> A governance layer external to agent cores, such as Governance-as-a-Service (GaaS) , can intercept agent actions, evaluate compliance with declarative rules, assign trust scores, and modulate behavior dynamically
>
> Onyekaonwu et al. (2024), p. 8

---

## 5. Evidence gaps

### 5.1 The fifteen core papers whose full text could not be retrieved

Fifteen of the 47 records screened as `core`, meaning they were judged from their abstracts to answer a research question directly, could not be retrieved as full text with the available institutional session. Each is recorded in `evidence-ledger.json` with status `unavailable` and reason `no-full-text-retrieved`, rather than being relabelled to let the stopping rule pass. **All fifteen are cited below from abstract metadata only. None was read, none was quality-appraised, and none contributed to any claim in sections 3 or 4.**

This is the largest single threat to the conclusions above, and its composition makes it worse than the count suggests. The unretrieved set contains the two works most likely to have reframed this review's central question, a research manifesto on agentic process management by an eighteen-author group spanning the field (Calvanese et al., 2026) and a practitioner-perspectives study on agent governance in business processes (Vu et al., 2026). It contains at least four works whose titles indicate a direct RQ1 design: a floor-safety guarantee for compliance-critical routing (Pacella et al., 2026), integration of agents with process rules (Kaltenpoth et al., 2026), runtime policy enforcement for tool-protocol agents (Wang et al., 2026), and a guardrails implementation study (Kumar, 2026). It contains the two enterprise-resource-planning studies that would have supplied the deployment evidence the corpus otherwise lacks (Schnepf et al., 2024; Schnepf et al., 2026). And it contains four workflow-generation and process-execution works that bear directly on the treatment arm (Zeng et al., 2023; Duesterwald et al., 2024; Monti et al., 2024; Rao et al., 2025), plus a healthcare compliance framework (Menezes et al., 2025), a vehicle-testing agent study (Unterschütz and Hansen, 2025) and a conceptual lifecycle framework (Dumitriu et al., 2026).

The practical consequence is that saturation was declared over a corpus from which roughly a third of the directly relevant literature is missing for access reasons rather than for relevance reasons. Saturation against evidence domains is not the same as saturation against evidence, and this review should be read as bounded by retrieval, not by the literature.

### 5.2 Gaps in what the retrieved corpus can measure

**No study runs the RQ1 comparison in its stated form.** The four studies that come closest all substitute a different treatment for "an explicit process model": a per-tool precondition, an SMT constraint set, a structured skill procedure, or a set of world-state invariants. The one study that ablates a workflow template as such finds it close to inert. As section 3.4 argues, the corpus therefore supports a reformulated question about mediated interfaces better than it supports RQ1 as written.

**Compliance-critical domains are barely represented.** The airline domain of one public benchmark carries a disproportionate share of the direct evidence, appearing in three separate studies. Beyond it, the compliance-critical evidence is one internal financial auditing corpus, one corporate email and file-sharing suite, one synthetic procurement environment, one synthetic accounts-payable workflow, one synthetic warehouse-brokerage domain and one machinery safety classification task. There is no healthcare, no lending, no anti-money-laundering, and nothing from a regulated production deployment with independent measurement.

**Violations of omission are systematically unmeasured.** The strongest enforcement result in the corpus operates at pre-tool activation and therefore cannot catch a policy-required call that the agent declines to make. The latent-failure work shows that omissions are common. No study in the corpus enforces against omission at runtime.

**Task completion and policy conformance are usually not reported together.** Only a minority of studies report both dependent variables from the same runs, which is the minimum requirement for answering RQ1's "without a corresponding loss" clause. Where both are reported, one study finds a genuine precision-recall trade-off at the tool-call level that does not surface at the task level, which suggests the clause is sensitive to the granularity of the completion measure and that future work should report both granularities.

**The comparator is under-specified across the literature.** "Policy in the prompt" covers at least four distinct conditions in this corpus: the full policy document supplied once, the document re-injected before every action, a compact policy-to-tool mapping injected before every action, and high-level rules in a system prompt. These produce materially different violation rates. Any replication must specify which one it means.

**Nothing in the corpus measures durability.** All comparisons are single-session. No study measures whether a compiled constraint set remains correct as the policy changes, and the one paper that reports a drift monitor is among the least verifiable in the corpus.

**Preprint dependence.** Of the six studies carrying the direct RQ1 evidence, four are preprints, and the highest-rigour ablation, the highest-rigour measurement study and the two strongest formal-verification studies are all preprints. The peer-reviewed portion of the corpus is dominated by framework proposals, vision papers and case studies without baselines.

### 5.3 A methodological gap in this review

The reliability check described in section 2.4 is a stability measure, not an inter-rater measure. Screening was performed by a single model-assisted rater and re-checked by an independent blind re-prompt of the same class of model. Correlated error is therefore not excluded: any systematic misreading of the inclusion criteria would reproduce across both passes and appear as agreement. A human second rater over the same 88-record sample is the correct next step, and until it is run the screening reliability of this review should be treated as unestablished.

---

## 6. References

- Ait, A., Izquierdo, J. L., & Cabot, J. (2025). Towards Modeling Human-Agentic Collaborative Workflows: A BPMN Extension. Lecture notes in computer science, 367-382. https://doi.org/10.1007/978-3-032-04190-6_22
- Anand, A., Chatzi, I., Raha, R., & Schmuck, A.-K. (2026). MANTRA: Synthesizing SMT-Validated Compliance Benchmarks for Tool-Using LLM Agents. arXiv preprint. https://arxiv.org/abs/2605.06334
- Begum, S., & Rosenzweig, M. (2026). A Privacy-Preserving On-Device Multi-Agent Architecture for AI PC (POMA) Workflow Automation. 2026 IEEE International Conference on AI and Data Analytics (ICAD), 1-8. https://doi.org/10.1109/icad69378.2026.11608651
- Besanson, G. (2026). SARC: A Governance-by-Architecture Framework for Agentic AI Systems. arXiv (Cornell University). https://arxiv.org/abs/2605.07728
- Boinapalli, N. R. (2026). GALENA: A Governance-Aware LLM Enterprise Navigation Architecture for Autonomous Multi-Agent Workflow Automation with Compliance Enforcement. https://doi.org/10.64971/j.cph.eijtem.v13.i3.12.2026
- Calvanese, D., Casciani, A., De Giacomo, G., Dumas, M., Fournier, F., Kampik, T., La Malfa, E., Limonad, L., Marrella, A., Metzger, A., Montali, M., Amyot, D., Fettke, P., Polyvyanyy, A., Rinderle-Ma, S., Sardiña, S., Tax, N., & Weber, B. (2026). Agentic Business Process Management: A research manifesto. Information Systems, 140, 102738-102738. https://doi.org/10.1016/j.is.2026.102738 [Abstract only; full text not retrieved.]
- Chaitanya, P. (n.d.). OpenMCPSpec: A Specification Framework for Robust, Governed, and Lifecycle-Managed Machine Communicable Processes in LLM-Agent Systems. 2026 Fourth International Conference on Secure Cyber Computing and Communications (ICSCCC). https://ieeexplore.ieee.org/document/11600150/
- Duesterwald, E., Isahagian, V., Jayaram, K. R., Kumar, R., Muthusamy, V., Oum, P., Thomas, G., & Venkateswaran, P. (2024). A Conversational Assistant Framework for Automation. https://doi.org/10.1145/3700824.3701093 [Abstract only; full text not retrieved.]
- Dumitriu, F., Greavu-Şerban, V., Necula, S.-C., & FĂTU, V.-C. (2026). Integrating LLM in Business Process Management: A Conceptual Framework for Augmenting the Process Lifecycle. Systems, 14(9), 1076-1076. https://doi.org/10.3390/systems14091076 [Abstract only; full text not retrieved.]
- Dutta, P. (2026). Accountable Multi-Agent AI Systems: Orchestration Frameworks for Enterprise Workflow Automation with Human-in-the-Loop Verification. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.19845387
- Gatta, V. S. (2026). Compliance Digital Twins for Autonomous Financial Agents: Reliability-Aware Scenario Assurance via Calibrated LLM Evaluation. Journal of International Crisis and Risk Communication Research, 168-181. https://doi.org/10.63278/jicrcr.vi.3783
- Iyenghar, P., Mansour, Z., & Wuebbelmann, J. (2025). Evaluation of Automated Machinery Functional Safety Risk Assessment Using LLMs. IEEE Access, 13, 203648-203669. https://doi.org/10.1109/access.2025.3632528
- Jeong, C., Sim, S., Cho, H., Kim, S., & Shin, B. (2025). E2E Process Automation Leveraging Generative AI and IDP-Based Automation Agent: A Case Study on Corporate Expense Processing. Artificial Intelligence and Applications. https://doi.org/10.47852/bonviewaia52026307
- Kaltenpoth, S., Skolik, A., Müller, O., & Beverungen, D. (2026). A Step Towards Cognitive Automation: Integrating LLM Agents with Process Rules. Lecture Notes in Computer Science, 308-324. https://doi.org/10.1007/978-3-032-02867-9_19 [Abstract only; full text not retrieved.]
- Kampik, T., Warmuth, C., Rebmann, A., Agam, R., Egger, L., Gerber, A., Hoffart, J., Kolk, J., Herzig, P., Decker, G., van der Aa, H., Polyvyanyy, A., Rinderle‐Ma, S., Weber, I., & Weidlich, M. (2024). Large Process Models: A Vision for Business Process Management in the Age of Generative AI. K&uuml;nstliche Intell., 39(2), 81-95. https://doi.org/10.1007/s13218-024-00863-8
- Kölbel, L. M., Poss, L., & Schönig, S. (2026). Context is key for cybersecurity: leveraging external knowledge for process model explanation via LLMs. International Journal of Information Security, 25(4). https://doi.org/10.1007/s10207-026-01245-x
- Kumar, K. (2026). Agentic Implementation in Business Processes with Guardrails. DigitalCommons - Kennesaw State University (Kennesaw State University). https://digitalcommons.kennesaw.edu/cognoconproceedings/7 [Abstract only; full text not retrieved.]
- Lins, L. F., Nascimento, N., Alencar, P., Oliveira, T., & Cowan, D. (2023). Comparing Generative Chatbots Based on Process Requirements: A Case Study. https://doi.org/10.1109/bigdata59044.2023.10386251
- Menezes, V. P., Chowdhury, M. J. M., & Mahmood, A. N. (2025). An Agentic Framework for Compliant, Ethical and Trustworthy GenAI Applications in Healthcare. https://doi.org/10.1145/3727166.3727191 [Abstract only; full text not retrieved.]
- Mishra, L. N., & Senapati, B. (2025). Retail Resilience Engine: An Agentic AI Framework for Building Reliable Retail Systems With Test-Driven Development Approach. IEEE Access, 13, 50226-50243. https://doi.org/10.1109/access.2025.3552592
- Monti, F., Leotta, F., Mangler, J., Mecella, M., & Rinderle‐Ma, S. (2024). NL2ProcessOps: Towards LLM-Guided Code Generation for Process Execution. Lecture notes in business information processing, 127-143. https://doi.org/10.1007/978-3-031-70418-5_8 [Abstract only; full text not retrieved.]
- Onyekaonwu, C. B., Igba, E., & Anyebe, A. C. P. (2024). Agentic AI for Regulatory Intelligence: Designing Scalable Compliance Lifecycle Systems in Multinational Tech Enterprises. International Journal of Scientific Research and Modern Technology., 205-222. https://doi.org/10.38124/ijsrmt.v3i12.934
- Pacella, M., Papadia, G., & Giliberti, V. (2026). Governed Agentic Process Automation: A Floor-Safety Guarantee for Compliance-Critical LLM Routing. Algorithms, 19(8), 627. https://doi.org/10.3390/a19080627 [Abstract only; full text not retrieved.]
- Park, J. H., & Madisetti, V. K. (2025). CAPRI: A Context-Aware Privacy Framework for Multi-Agent Generative AI Applications. IEEE Access, 13, 43168-43177. https://doi.org/10.1109/access.2025.3549312
- Pulikonda, N. K. M. (2025). Real-Time Regulatory Intelligence Framework: LLM-powered compliance automation for financial services. World Journal of Advanced Engineering Technology and Sciences, 15(2), 3106-3115. https://doi.org/10.30574/wjaets.2025.15.2.0784
- Qasim, H. F., & Kadim, S. A. (2026). PolicyFaultBench: Mutation-Based Assurance of Policy Mediation and Proposal-Interface Conformance for Tool- Using AI Agents. Research Square. https://doi.org/10.21203/rs.3.rs-10502893/v1
- Rabinovich, E., Boaz, D., Zwerdling, N., & Anaby-Tavor, A. (2026). Near-Miss: Latent Policy Failure Detection in Agentic Workflows. arXiv (Cornell University), 296-308. https://doi.org/10.48550/arxiv.2603.29665
- Rao, K., Coviello, G., Mellone, G., De Vita, C. G., & Chakradhar, S. (2025). XPF: Agentic AI System for Business Workflow Automation. https://doi.org/10.1145/3731545.3743644 [Abstract only; full text not retrieved.]
- Santos, W. D. S., Coutinho, J. R., Baião, F., Spyrides, G. M., & Lopes, H. (2025). Enhancing declarative business process management availability through generative AI. Process Science, 2(1). https://doi.org/10.1007/s44311-025-00029-1
- Schnepf, J., Engin, T., Anderer, S., & Scheuermann, B. (2024). Studies on the Use of Large Language Models for the Automation of Business Processes in Enterprise Resource Planning Systems. Lecture notes in computer science, 16-31. https://doi.org/10.1007/978-3-031-70239-6_2 [Abstract only; full text not retrieved.]
- Schnepf, J., Schwarz, M., Scheuermann, B., & Anderer, S. (2026). A Study on Multi-agent Collaboration for Business Process Automation in Enterprise Resource Planning Systems. Communications in computer and information science, 118-138. https://doi.org/10.1007/978-3-032-15632-7_7 [Abstract only; full text not retrieved.]
- Schwartz, S., Yaeli, A., & Shlomov, S. (2023). Enhancing Trust in LLM-Based AI Automation Agents: New Considerations and Future Challenges. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2308.05391
- Tebourbi, H., Nouzri, S., Mualla, Y., Fatimi, M. E., Najjar, A., Abbas-Turki, A., & Dridi, M. (2025). BPMN-Based Design of Multi-Agent Systems: Personalized Language Learning Workflow Automation with RAG-Enhanced Knowledge Access. Information, 16(9), 809. https://doi.org/10.20944/preprints202507.1291.v1
- Towards Enforcing Company Policy Adherence in Agentic Workflows. (2025). Underline Science Inc., 595-606. https://doi.org/10.18653/v1/2025.emnlp-industry.41
  Note. Rendered per APA 7 section 9.12 because the `citation_apa` field of `manifest.json` carries a corrupted corporate string in the author position. That field reads, verbatim: "2025, A. F. C. L., Anaby Tavor, A., Boaz, D., Rabinovich, E., Uziel, G., & Zwerdling, N. (2025). Towards Enforcing Company Policy Adherence in Agentic Workflows. Underline Science Inc., 595-606. https://doi.org/10.18653/v1/2025.emnlp-industry.41". The `authors` array of the same record lists Anaby Tavor, Boaz, Rabinovich, Uziel and Zwerdling behind the corrupted string, and `references.bib` carries the same corruption.
- Unterschütz, S., & Hansen, B. (2025). Leveraging LLM-Based AI Agents for Boosting Vehicle Testing Process. SAE Technical Paper Series, 1. https://doi.org/10.4271/2025-01-0300 [Abstract only; full text not retrieved.]
- Veli, E. (2026). A stigmergy-driven multi-agent framework for intelligent task orchestration. UPCommons institutional repository (Universitat Politècnica de Catalunya). https://hdl.handle.net/2117/463237
- Vu, H., Klievtsova, N., Leopold, H., Rinderle-Ma, S., & Kampik, T. (2026). Agentic Business Process Management: Practitioner Perspectives on Agent Governance in Business Processes. Lecture Notes in Business Information Processing, 29-43. https://doi.org/10.1007/978-3-032-02936-2_3 [Abstract only; full text not retrieved.]
- Wahab, M. B. A., Mazen, S. A., & Helal, I. M. A. (2025). Utilizing Large Language Models in Business Process Management: Applications and Challenges. Journal of Computer Science, 21(8), 1921-1932. https://doi.org/10.3844/jcssp.2025.1921.1932
- Wang, L. (2026). Open-Rosalind: Tool-First Biomedical LLM Agents with Process-Aware Benchmarking. https://doi.org/10.64898/2026.05.06.722404
- Wang, S., Zhu, S., & Li, R. (2026). Runtime Policy Enforcement for MCP-Based LLM Agents. Electronics, 15(13), 2829. https://doi.org/10.3390/electronics15132829 [Abstract only; full text not retrieved.]
- Wang, X., Shu, R., Dan, C., Xu, T., Luo, M., Mai, Y., & Wan, B. (2026). FRAMES: Guarded and Dual-Objective Skill Evolution for Agents in Policy-Governed Enterprise Workflows. arXiv preprint. https://doi.org/10.48550/arxiv.2608.01772
- Winston, C., Winston, C., & Just, R. (2026). Solver-Aided Verification of Policy Compliance in Tool-Augmented LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2603.20449
- Wu, B., Zhang, W., Chen, K., Fang, H., & Yu, N. (2026). Provably Secure Agent Guardrail. arXiv (Cornell University). https://arxiv.org/abs/2605.29251
- Wu, J., & Gong, M. (2026). Policy-Invisible Violations in LLM-Based Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2604.12177
- Ye, Y., Cong, X., Tian, S., Cao, J., Wang, H., Qin, Y., Lu, Y., Yu, H., Wang, H., Lin, Y., Liu, Z., & Sun, M. (2023). ProAgent: From Robotic Process Automation to Agentic Process Automation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2311.10751
- Zeng, Z., Watson, W., Cho, N., Rahimi, S., Reynolds, S., Balch, T., & Veloso, M. (2023). FlowMind: Automatic Workflow Generation with LLMs. https://doi.org/10.1145/3604237.3626908 [Abstract only; full text not retrieved.]
- Zhu, H., Liang, J., Hou, M., Tang, R., Zhu, X., Yang, J., Mao, Y., & Wu, F. (2026). From Business Events to Auditable Decisions: Ontology-Governed Graph Simulation for Enterprise AI. arXiv (Cornell University). https://arxiv.org/abs/2604.08603
