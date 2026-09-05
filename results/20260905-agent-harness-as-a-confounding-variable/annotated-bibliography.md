# Annotated Bibliography — long-term semantic memory hiring agent production LLM

Generated 2026-09-05 from screening decisions, evidence-ledger notes, and quality scores. Working material and audit evidence — not submission text.

## Core (117)

### Lai, J., & Li, Z. (2026). A Comparative Empirical Evaluation of Single-Agent and Multi-Agent LLM Prompting Strategies for Automated Formative Feedback in Education. Journal of Intelligence and Engineering Technology, 1(2), 29-38. https://doi.org/10.70393/6a696574.343135

- **Decision:** core — Controlled comparison of four prompting and agent configurations over one essay corpus with a fixed rubric and rater panel, reporting quality and inference-cost differences.
- **Evidence:** This study frames itself as isolating architecture, and it does hold the model, decoding settings and rubric constant across the four conditions, explicitly claiming that shared instructional framing lets quality differences be attributed to architectural and prompting variation. But the design confounds exactly the two things RQ1 separates: moving from S2 to S3 to S4 adds agent roles and simulta…
- **Domains:** cost-latency, evaluation-validity, harness-scaffold, metric-definition, model-versus-scaffold, prompt-sensitivity, topology-comparison
- **Quality:** rigor not yet scored

### Perikala, K. (2026). A MODULAR BENCHMARKING FRAMEWORK FOR EVALUATING LLM-BASED AGENT APPLICATIONS. INTERNATIONAL JOURNAL OF RESEARCH IN COMPUTER APPLICATIONS AND INFORMATION TECHNOLOGY, 9(1), 1-14. https://doi.org/10.34218/ijrcait_09_01_001

- **Decision:** core — Benchmarking framework that decouples datasets, agents, models, and metrics to evaluate across models, agent architectures, and execution strategies.
- **Evidence:** This paper states the RQ1 problem crisply in its related-work section - agent performance is often tightly coupled to implementation details including prompt structure, tool schemas and orchestration logic, obscuring the relative contributions of models versus agents - and then proposes trace-first, component-decoupled benchmarking as the remedy. Its experimental design nominally holds the harnes…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, harness-scaffold, metric-definition, model-versus-scaffold, observability-tracing
- **Quality:** rigor not yet scored

### Xu, T., Wen, H., & Li, M. (2026). Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents. arXiv preprint. http://arxiv.org/abs/2605.22166v2

- **Decision:** core [preprint] — Freezes model weights and evaluation environments and varies only the runtime harness, reporting gains across 126 model-environment settings and 18 backbones.
- **Evidence:** This is the largest single-factor harness experiment in the batch: 126 model-environment cells in which the model weights and the evaluation environment are held fixed and only the runtime interface changes. For RQ1 it provides a direct effect-size estimate for the harness term, an average 88.5% relative gain that is achieved with no weight update and no change to the evaluation protocol, and its…
- **Domains:** benchmark-design, confounding-attribution, environment-coupling, failure-attribution, harness-scaffold, model-versus-scaffold, retry-recovery, tool-schema
- **Quality:** rigor not yet scored

### Lukei, M., & Kowol, P. T. (2026). Adaptive Orchestration with Cross-Episode Memory for Dynamic LLM-based Agent Pools. WOCHAT2026: Workshop on Chatbots and Agentic Technologies, 22-45. https://doi.org/10.21437/wochat.2026-4

- **Decision:** core — Adds an external memory layer of playbooks and blueprints to orchestration and ablates which components drive gains on OfficeBench with a fixed model.
- **Evidence:** A careful ablation of one harness component - cross-episode memory - with the orchestrator backbone, agent pool, benchmark splits and retrieval thresholds fixed and memory frozen during the held-out evaluation phase, so the measured effect is not contaminated by continued curation. The strongest RQ1 contribution is the retrieval-to-execution error decomposition, which shows that a harness improve…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, memory-context, prompt-sensitivity, tool-schema, topology-comparison
- **Quality:** rigor not yet scored

### Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-T., Rocktäschel, T., Riedel, S., & Kiela, D. (2026). Affordance-Compiled Intelligence: Observable-Only Cognitive Impedance Matching for No-Meta LLM-Integrated Systems. arXiv (Cornell University). https://doi.org/10.5281/zenodo.20116149

- **Decision:** core [preprint] — Develops a certification theory for how a fixed model policy gains capability when validators, typed action handles, and repair paths are redesigned.
- **Evidence:** A formal theory paper that treats RQ1 as its central object: it defines world-side capability amplification, the claim that a fixed model-policy's realized capability depends strongly on how the world is surfaced to it, and then builds the machinery required to certify that claim without a privileged evaluator. The most directly useful contribution for RQ2 is its definition of what holding the ha…
- **Domains:** confounding-attribution, evaluation-validity, governance-safety, harness-scaffold, model-versus-scaffold, observability-tracing, statistical-method, tool-schema
- **Quality:** rigor not yet scored

### Sritharan, T. (2026). Agent Brain: A Biologically Inspired Memory System for Autonomous AI Agents — LongMemEval-M Evaluation. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.19673132

- **Decision:** core [preprint] — Compares an eleven-layer agent memory harness against a pgvector-only control and a consolidation ablation on LongMemEval-M with the model held fixed.
- **Evidence:** The scientific value here for RQ1 is almost entirely negative and self-reported: the authors hold ingestion corpus, embedding model and judging rubric fixed across four of their own configurations and find that adding harness machinery makes things worse - the Dream Cycle consolidation loses 1.9 pp and the full hybrid-plus-entity pipeline loses up to 2.2 pp against a plain pgvector top-5 control…
- **Domains:** benchmark-design, confounding-attribution, deployment-production, evaluation-validity, memory-context, reproducibility
- **Quality:** rigor not yet scored

### Li, J., Wu, Y., & Chang, Y. (2026). Agent harness engineering: A survey. Preprints.org. https://doi.org/10.20944/preprints202606.2203.v1

- **Decision:** core [preprint] — Survey treating the harness as a performance lever separable from base model capability, with a two-stage logic distinguishing model capability gaps from harness compensation effects.
- **Evidence:** This is the most direct conceptual framing of RQ1 in the assignment set: it defines the harness as a system-level execution structure independent of model weights and argues explicitly that it is a performance lever orthogonal to model capability, so that holding the model fixed and changing the harness can substantially alter end-to-end performance. Its strongest quantitative support is second-h…
- **Domains:** confounding-attribution, evaluation-validity, governance-safety, harness-scaffold, memory-context, model-versus-scaffold, observability-tracing, tool-schema
- **Quality:** rigor not yet scored

### Meng, Q., Wang, Y., Chen, L., Li, Y., Wu, W., Jiang, W., Wang, Q., Lu, C., Gao, Y., Wu, Y., & Hu, Y. (2026). Agent harness for large language model agents: A survey. Preprints.org. https://doi.org/10.20944/preprints202604.0428.v1

- **Decision:** core [preprint] — Survey defining the agent harness as a distinct research object and arguing it, not the model, is the binding constraint on LLM agent performance; directly addresses RQ1.
- **Evidence:** This survey is the closest thing in the batch to a literature-level statement of RQ1: it argues the harness is the binding constraint rather than the model, and it decomposes the evaluation-unreliability problem into three structurally distinct causes - environment drift, task specification ambiguity, and harness coupling - of which only the third is an infrastructure problem and the only one who…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, governance-safety, harness-scaffold, memory-context, reproducibility, tool-schema
- **Quality:** rigor not yet scored

### Tao, J., & Zhou, L. (2026). Agent Reasoning Tools (ARTs): A Tool Definition Approach for Empower LLM-based Agent Systems. Proceedings of the Annual Hawaii International Conference on System Sciences. https://doi.org/10.24251/hicss.2026.096

- **Decision:** core — Introduces a tool-definition approach for LLM agents and evaluates its effect on task performance, making tool schema the manipulated variable.
- **Evidence:** This paper is useful for RQ1 mainly through a comparison it does not foreground: with the model, temperature and prompting regime held constant, simply restructuring the task around ART tool definitions in a single pass lifts F1 from 0.7109 to 0.8044, a gain of about 9.4 points that is attributable purely to tool-definition format and calling structure. Adding the evaluator-optimizer loop contrib…
- **Domains:** evaluation-validity, harness-scaffold, model-versus-scaffold, reflection-planning, statistical-method, tool-schema, topology-comparison
- **Quality:** rigor not yet scored

### Morla, T., Bellibaltu, R. R., Singh, M., & Kapoor, M. S. (2026). AgentFairBench: Do LLM Agents Discriminate When They Act?. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2606.16723

- **Decision:** core [preprint] — Varies four agent scaffolds of increasing agency over matched counterfactual sets and shows statistic arity alone inflates apparent disparity by about 2.4x.
- **Evidence:** AgentFairBench treats scaffold depth as a first-class experimental variable rather than an implementation detail, running the identical counterfactual matched sets through four rungs of increasing agency and holding profile content constant so any measured difference is attributable to the manipulated factor. That design is a direct template for RQ1: it asks whether adding chain-of-thought, delib…
- **Domains:** benchmark-design, evaluation-validity, governance-safety, harness-scaffold, reproducibility, statistical-method, tool-schema, topology-comparison
- **Quality:** rigor not yet scored

### Sarkar, I. (2026). Agentic AI Between Capability and Reliability: A Structured Review of Architectures, Design Patterns, Evaluation Practice, and Enterprise Deployment. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21809562

- **Decision:** core — Review analysing why curated benchmark scores diverge from live long-horizon performance and modelling the gap, addressing the validity of reported agent performance.
- **Evidence:** full text not read (status: unavailable).

### Li, Y., Li, L., Wu, Z., Liao, Q., HAO, J., Shao, K., & Xu, F. (2026). AgentSwift: Efficient LLM Agent Design via Value-Guided Hierarchical Search. Proceedings of the AAAI Conference on Artificial Intelligence, 40(38), 31843-31851. https://doi.org/10.1609/aaai.v40i38.40453

- **Decision:** core — Automated agent design that co-optimizes workflow topology with memory, planning, and tool-use components and reports the resulting gains.
- **Evidence:** AgentSwift is not designed to answer RQ1 but supplies unusually clean evidence for it as a side effect: the entire search is conducted with the model held fixed at GPT-4o-mini, so every reported difference is harness-attributable. Under that fixed backbone, hand-crafted scaffolds on ALFWorld span 0.336 to 0.587 and the searched scaffold reaches 0.806, meaning scaffold choice alone accounts for a…
- **Domains:** benchmark-design, cost-latency, harness-scaffold, memory-context, model-versus-scaffold, reflection-planning, tool-schema
- **Quality:** rigor not yet scored

### Balusu, K. C. (2026). AgentTelemetry: A Fault Detection Benchmark and Toolkit for LLM Agent Observability. Proceedings of the 3rd ACM International Conference on AI-Powered Software, 380-387. https://doi.org/10.1145/3805760.3814931

- **Decision:** core — Controlled fault-detection harness crossing 14 fault types, 5 observability conditions, and 7 agent frameworks, with a span-kind ablation.
- **Evidence:** full text not read (status: unavailable).

### Lou, X., Lázaro-Gredilla, M., Dedieu, A., Wendelken, C., Lehrach, W., & Murphy, K. P. (2026). AutoHarness: improving LLM agents by automatically synthesizing a code harness. arXiv preprint. http://arxiv.org/abs/2603.03329v1

- **Decision:** core [preprint] — Synthesised code harness eliminates illegal actions across 145 games and lets a smaller model outperform a larger one, isolating harness from model capability.
- **Evidence:** AutoHarness is a direct demonstration of the RQ1 confound in its strongest form: the same small model beats a much larger model from the same family purely because a synthesised code harness filters out illegal actions. The comparison is well controlled on the prompt dimension, since the authors state that the same optimised prompt is used in all experiments and all agents face the same environme…
- **Domains:** benchmark-design, cost-latency, environment-coupling, harness-scaffold, model-versus-scaffold, retry-recovery, tool-schema
- **Quality:** rigor not yet scored

### Dhakal, A., Neupane, K., & Chaudhary, A. (2026). Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2607.13085

- **Decision:** core [preprint] — Model-matched plain-agent baselines on XBOW test how much penetration-testing performance comes from specialised harnesses rather than the backbone model.
- **Evidence:** This is the clearest single statement of the RQ1 attribution problem in the batch and it tests it directly. The authors argue that autonomous-pentest papers ship a new architecture and a new backbone model together, so a higher solve rate cannot be charged to the harness rather than the model, and they propose a plain coding CLI agent under a matched model, budget, target interface and scoring ru…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, model-versus-scaffold, prompt-sensitivity, reproducibility
- **Quality:** rigor not yet scored

### Wahid, A. R. (2026). BATITONG: Deterministic Reliability for LLM-Driven Offensive-Security Orchestration. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21759172

- **Decision:** core — Explicitly separates how much reliability comes from the model versus the architecture, then audits a deterministic reliability scaffold across 66 campaigns.
- **Evidence:** This paper is built on exactly the question behind RQ1: it asks how much of an LLM offensive-security system's reliability comes from the model versus from the architecture wrapped around it, and answers by running the whole pipeline on free-tier models and measuring what a deterministic verification layer adds. Because every finding stores both the model's own claim and the post-gate result, the…
- **Domains:** confounding-attribution, cost-latency, failure-attribution, governance-safety, harness-scaffold, model-versus-scaffold, reproducibility, retry-recovery
- **Quality:** rigor not yet scored

### Wang, Z., Gu, L., Chi, Z., Liu, Z., Ayyoubzadeh, S. M., Yu, Y., & Wang, Y. (2026). Benchmarking LLM Judges for Mobile Agent Evaluation. arXiv preprint. https://doi.org/10.48550/arxiv.2608.11434

- **Decision:** core [preprint] — Shows elaborate judge pipelines do not improve judge quality while the LLM backbone dominates, and ties judge quality to agent ranking fidelity.
- **Evidence:** This is a fully crossed 6 methods x 5 backends design, which makes it one of the few studies in the batch that can actually decompose how much of a reported difference belongs to the pipeline versus the model. Its central RQ1 finding is that among competitive methods the backbone explains far more accuracy variance than the judge pipeline (11% method versus 49% backbone once the two weakest purpo…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, harness-scaffold, metric-definition, model-versus-scaffold, statistical-method
- **Quality:** rigor not yet scored

### Purwar, A., Singh, S., & Srivastava, K. (2026). Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight. arXiv preprint. http://arxiv.org/abs/2608.24314v1

- **Decision:** core [preprint] — Scores identical voice-agent interactions under three evaluation configurations and two judge models to test whether measured results depend on the evaluation setup.
- **Evidence:** The design explicitly tests whether automated judgments are sensitive to the evaluation setup by scoring the same interactions under three configurations (no persona, static persona injection, dynamically inferred context) and two judge models, with identical rubric definitions and an identical aggregation procedure supplied to humans and judges. The headline RQ1-relevant result is a partial diss…
- **Domains:** confounding-attribution, evaluation-validity, failure-attribution, governance-safety, harness-scaffold, metric-definition, model-versus-scaffold, prompt-sensitivity, statistical-method
- **Quality:** rigor not yet scored

### Assidiqi, M. H., Alghazzawi, D., Alarifi, S., & Cheng, L. (2026). Benchmarking Reference-Free LLM Agent Robustness Under Schema, Policy, and Toolset Drift. IEEE Access, 14, 79662-79672. https://doi.org/10.1109/access.2026.3696096

- **Decision:** core — Controlled schema, policy, and toolset drift perturbations across five models with a normalization ablation, reporting how tool-interface changes shift agent task success.
- **Evidence:** This is the most rigorously controlled study in the assignment set and the one that most directly probes RQ1's harness components, since its treatments are exactly a repair-rule layer, a memory-hint layer and a schema-normalization layer applied over an otherwise identical base LLM call at temperature 0. Its central finding is a warning against assuming harness additions help: a memory or replay…
- **Domains:** confounding-attribution, deployment-production, environment-coupling, evaluation-validity, failure-attribution, memory-context, retry-recovery, statistical-method, tool-schema
- **Quality:** rigor not yet scored

### Albayaydh, W., Zhao, R., & Flechais, I. (2026). Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents. arXiv preprint. https://arxiv.org/abs/2607.05775

- **Decision:** core [preprint] — Cross-benchmark synthesis of agent failure modes including measurement-validity problems, reporting that additional scaffolding does not consistently improve reliability.
- **Evidence:** This synthesis is the closest thing in the batch to a prior statement of RQ1 at review level. Its cross-cutting pattern of uneven returns to additional scaffolding states directly that adding more agents, tools, reasoning effort or context does not uniformly improve reliability and can reduce it, citing multi-agent coordination overhead, context accumulation effects, and the Holistic Agent Leader…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, governance-safety, harness-scaffold, reproducibility, tool-schema, topology-comparison
- **Quality:** rigor not yet scored

### Strain, P. M. (2026). Bounded Returns to Orchestration: A Synthesis Ceiling Beneath Eleven Controlled Deep-Research Architectures. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21118281

- **Decision:** core — Holds the tool layer and base model fixed across eleven deep-research architectures, with judge audits and budget controls bounding orchestration's isolable contribution.
- **Evidence:** This is the most direct test of RQ1 in the batch: it fixes one model (GPT-4o), one search/extraction tool layer, and one retry policy, then varies only orchestration across eleven deep-research architectures scored by a reliability-audited three-judge panel. The headline is that orchestration has bounded, task-conditional returns: the five strongest pipelines are judge-robustly inseparable, and t…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, model-versus-scaffold, reproducibility, topology-comparison
- **Quality:** rigor not yet scored

### Rafique, M., & Bindschaedler, L. (2026). C
                    <scp>law</scp>
                    VM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents. Proceedings of the Sixth European Workshop on Machine Learning and Systems, 1-12. https://doi.org/10.1145/3805621.3807648

- **Decision:** core — Places residency and durability contracts in the harness and measures fault elimination and per-turn overhead across traces and stress tests.
- **Evidence:** ClawVM isolates one harness component, context and memory management, and holds everything else including the model entirely out of the loop by evaluating through deterministic replay. That makes its effect estimates unambiguously harness-attributable but also weakens their external validity, since the headline 76.7% versus 100% task-success gap is defined as zero explicit lifecycle faults in rep…
- **Domains:** confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, memory-context, observability-tracing, reproducibility, retry-recovery
- **Quality:** rigor not yet scored

### Shah, J. (2026). Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures. arXiv preprint. https://doi.org/10.48550/arxiv.2606.08275

- **Decision:** core [preprint] — Attributes agent outcomes to individual steps by intervention and run-forward replay with Shapley credit and confidence intervals, addressing causal attribution directly.
- **Evidence:** CAR supplies the methodological machinery RQ1 needs: it treats an agent run as a structural causal model and attributes outcome change to a specific step by intervening on that step while holding the rest of the run at its factual values, then re-executing under the same stochastic policy. Its five do-operations map neatly onto harness components (do_context edits the assembled history, do_policy…
- **Domains:** confounding-attribution, environment-coupling, failure-attribution, observability-tracing, reproducibility, statistical-method
- **Quality:** rigor not yet scored

### Chen, Z., Xiao, T., Zhu, H., Yuan, Y., Zhang, L., & Wang, J. (2026). Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents. arXiv (Cornell University). https://arxiv.org/abs/2607.22688

- **Decision:** core [preprint] — Jointly optimizes harness and model weights, showing that training under a fixed harness mismatches the scaffolding that shapes trajectory quality.
- **Evidence:** Co-Harness is the clearest statement in the set that the harness is not merely a confounder but part of the data-generating process, since the trajectories used for post-training are themselves produced by the harness. For RQ1 the most useful number is the +24.7 pp average margin of the co-evolved system over a carefully hand-crafted static harness on the same benchmarks and model scales, which p…
- **Domains:** confounding-attribution, failure-attribution, harness-scaffold, memory-context, model-versus-scaffold, reproducibility, retry-recovery, tool-schema
- **Quality:** rigor not yet scored

### Ning, X., Tieu, K., Fu, D., Wei, T., Li, Z., Bei, Y., Zou, J., Ai, M., Liu, Z., Li, T.-W., Chen, L., Zhao, Y., Yang, K., Li, B., Qian, C., Li, G., Lin, X., Zeng, Z., Qiu, R., ... He, J. (2026). Code as Agent Harness. arXiv preprint. http://arxiv.org/abs/2605.18747v1

- **Decision:** core [preprint] — Survey framing code as the agent harness and organizing the harness interface, harness mechanisms, and multi-agent harness scaling.
- **Evidence:** A large survey that reframes code as the operational substrate of the harness rather than as model output, and whose §5.2.1 is a direct statement of RQ1's confound: once an LLM is embedded in a code-agent harness, performance depends on which repository files are retrieved, which tools are exposed, how many retries are allowed, whether tests can be executed, how failures are summarized and what v…
- **Domains:** confounding-attribution, evaluation-validity, governance-safety, harness-scaffold, memory-context, observability-tracing, retry-recovery, tool-schema
- **Quality:** rigor not yet scored

### Mody, P., Panchal, M., Kar, R., Bhowmick, K., & Karani, R. (2026). CraniMem: Cranial Inspired Gated and Bounded Memory for Agentic Systems. arXiv preprint. https://doi.org/10.48550/arxiv.2603.15642

- **Decision:** core [preprint] — Gated bounded memory design compared against Vanilla RAG and Mem0 baselines under clean and noise-injected inputs on long-horizon benchmarks.
- **Evidence:** A small controlled memory comparison that states its control condition plainly: for each setup the underlying LLM and decoding configuration are kept fixed so that only the memory system varies, and the same protocol is repeated across four backbones to check that the effect is not backbone-specific. For RQ1 the useful signal is the noise-drop metric, which isolates robustness to injected distrac…
- **Domains:** benchmark-design, cost-latency, environment-coupling, harness-scaffold, memory-context, model-versus-scaffold, statistical-method
- **Quality:** rigor not yet scored

### Cheng, Y., Li, C., Cui, Q., Ding, W., Wang, L., Chen, Y., & Gao, P. (2026). CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.18613

- **Decision:** core [preprint] — Swaps only the action surface under an identical harness across a four-model panel and ablates typed structure against procedural skills to attribute the F1 gain.
- **Evidence:** This paper is a near-textbook RQ2 exemplar: both arms run the same third-party harness with the same loop, prompt style, step budget, temperature and model, and only the action surface changes, which the authors state explicitly as the sole independent variable. It is relevant to RQ1 because it quantifies how much of a reported performance difference is attributable to something outside the model…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, harness-scaffold, model-versus-scaffold, reproducibility, tool-schema
- **Quality:** rigor not yet scored

### Gaikwad, M. (2026). Did You Check the Right Pocket? Cost-Sensitive Store Routing for Memory-Augmented Agents. arXiv preprint. http://arxiv.org/abs/2603.15658v1

- **Decision:** core [preprint] — Treats memory store routing as a first-class agent design component and measures oracle versus uniform retrieval on accuracy and token cost.
- **Evidence:** This paper isolates one harness component, the memory-store routing policy, while holding the language model, prompt, temperature and within-store retrieval fixed, and shows that the component alone moves downstream QA accuracy by roughly five points and context cost by 62%. For RQ1 it supplies a clean single-factor estimate: a purely infrastructural decision made before the model is called chang…
- **Domains:** benchmark-design, cost-latency, evaluation-validity, harness-scaffold, memory-context, metric-definition
- **Quality:** rigor not yet scored

### Gallego, V. (2026). Distilling Feedback into Memory-as-a-Tool. arXiv preprint. http://arxiv.org/abs/2601.05960v2

- **Decision:** core [preprint] — Varies the memory harness by converting critiques into retrievable guidelines via agent tool calls and reports parity with test-time refinement at lower cost.
- **Evidence:** This short workshop paper is a memory-mechanism ablation in which, within a model, the scaffold is held fixed and only the memory pathway changes across three arms (zero-shot, self-critique, memory + feedback), which supports a clean within-model attribution of the gain to the memory component rather than to the model. Its value for RQ1 is mostly cautionary and comes from the appendix: the cross-…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, memory-context, reflection-planning
- **Quality:** rigor not yet scored

### Sghaier, O. B., Li, H., Adams, B., & Hassan, A. E. (2026). Don't Blame the Large Language Model: How Scaffolding Evolution Shapes Coding Agent Quality. arXiv preprint. https://arxiv.org/abs/2607.03691

- **Decision:** core [preprint] — Controlled longitudinal study fixes the LLM and varies only the agent harness across 35 Qwen Code releases, attributing quality shifts to harness rather than model.
- **Evidence:** This is the single most directly on-point paper in the batch for RQ1: it inverts the usual design by freezing the model and varying only the harness across 35 sequential releases of one coding-agent CLI. The headline result is that a quarter of continuous harness development produced no statistically significant change in SWE-bench Verified resolve rate while roughly doubling tokens and tool call…
- **Domains:** confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, model-versus-scaffold, reproducibility, statistical-method
- **Quality:** rigor not yet scored

### Ahumada, A. D. H. (2026). DYNAMIC MECHANISMS AND METRICS IN LANGUAGE MODEL-BASED MULTI-AGENT SYSTEMS: A SCOPING REVIEW. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22238539

- **Decision:** core — Scoping review of 229 studies reporting that no LLM multi-agent study documented seeds, run counts, or sampling frequency and only three gave quantitative metric values.
- **Evidence:** This scoping review supplies the sharpest available evidence for the reporting side of RQ2. Its audited finding is a systematic asymmetry: every one of the 16 direct LLM multi-agent studies documents what was studied (model, dataset, task, baseline) while almost none documents how the run was executed and replicated, with seed and sampling frequency reported in zero studies, number of runs in thr…
- **Domains:** benchmark-design, evaluation-validity, metric-definition, reproducibility, statistical-method, topology-comparison
- **Quality:** rigor not yet scored

### Kevin, C., Raghavan, N., Puget, J.-F., Malani, R., Puvvadi, M., Abramovitch, M., Gupta, M., Akkiraju, R., Prabhu, S., Dangi, Y., Luo, W., & Lee, S. H. (2026). Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills. arXiv preprint. http://arxiv.org/abs/2608.20614v1

- **Decision:** core [preprint] — Runs paired live trials with and without a target skill under a fixed model, harness, workspace and scorer, reporting the isolated skill lift.
- **Evidence:** ACES is the clearest example in the batch of a study that answers RQ2 affirmatively by construction: every measurement is a paired difference in which the task, harness, model, scorer, sandbox and all non-target skills are held fixed and only one harness component changes. Its argument for why that matters is exactly the RQ1 argument - absolute scores confound the quality of the component under s…
- **Domains:** benchmark-design, confounding-attribution, deployment-production, evaluation-validity, harness-scaffold, metric-definition, observability-tracing, statistical-method
- **Quality:** rigor not yet scored

### Zeng, L., Zhang, S., & Zhang, X. (2026). EviDx: Evidence-Aware Active Diagnosis with Scaffolded LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.24570

- **Decision:** core [preprint] — Introduces an explicit diagnostic scaffold and observer-guided runtime harness that controls termination, evaluating execution robustness separately from outcomes.
- **Evidence:** EviDx is unusual for this corpus because it separates the scaffold layer from the runtime harness layer and then ablates only the harness, holding the scaffold, the model, the tool interface and the exact 100 cases fixed. That design lets the paper report two different effect sizes for the same system: a large scaffold-plus-harness gain over static single-agent prompting, and a much smaller, more…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, harness-scaffold, model-versus-scaffold, reflection-planning, tool-schema
- **Quality:** rigor not yet scored

### Pan, W., Liu, S., Lin, C.-Y., Zeng, J., Tang, X., Zhou, X., Lu, Y., & Jia, X. (2026). Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference. arXiv preprint. https://doi.org/10.48550/arxiv.2606.05922

- **Decision:** core [preprint] — Optimises the agent harness of skills, tools and workflows from past trajectories and reports the resulting pass-rate gain on SWE-Bench Pro.
- **Evidence:** RHO is the largest single-factor harness effect reported in this batch: holding the backbone (GPT-5.5), the agent framework and the held-out split fixed, editing only the harness of instructions, skills and executable tools raised SWE-Bench Pro pass rate by 19 points in one round. That is a direct RQ1 estimate of how much a scaffold change alone can move a benchmark number, and it is larger than…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, reflection-planning, reproducibility, statistical-method
- **Quality:** rigor not yet scored

### Zhou, C., Chai, H., Chen, W., Guo, Z., Shan, R., Song, Y., Xu, T., Yang, Y., Yu, A., Zhang, W., Zheng, C., Zhu, J., Zheng, Z., Zhang, Z., Lou, X., Zhang, C., Fu, Z., Wang, J., Liu, W., ... Zhang, W. (2026). Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering. arXiv preprint. http://arxiv.org/abs/2604.08224v1

- **Decision:** core [preprint] — Review arguing agent capability now comes from externalized memory, skills, protocols, and harness engineering rather than from model weights.
- **Evidence:** A conceptual survey whose value for RQ1 is that it names the attribution problem directly rather than measuring it: it argues that many of the largest reliability gains do not come from changing the base model at all but from changing the environment around it, and then observes that current evaluation cannot distinguish the two because a harness improvement surfaces only as a higher pass rate. I…
- **Domains:** confounding-attribution, evaluation-validity, governance-safety, harness-scaffold, memory-context, model-versus-scaffold, observability-tracing, tool-schema
- **Quality:** rigor not yet scored

### Inguglia, G. (2026). First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope. arXiv preprint. https://doi.org/10.48550/arxiv.2605.28916

- **Decision:** core [preprint] — Head-to-head run of two coding agents on identical specifications and compute, attributing divergent cost, error handling and outputs to harness behaviour.
- **Evidence:** This is a textbook RQ2 negative case: the specification, data, hardware and task are matched exactly, but the two compared units are whole commercial agent products that bundle a harness and a model stack, so the observed differences cannot be attributed to either factor. The author says so directly in the limitations, noting that the agents used different underlying models for the manuscript ste…
- **Domains:** confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, observability-tracing, reproducibility, retry-recovery
- **Quality:** rigor not yet scored

### Ochi, Y., & Uchiyama, Y. (2026). Five Whys as an Epistemic-Honesty Scaffold for Multi-Agent LLM Analysis of Industrial Time Series. International Journal of Advanced Computer Science and Applications, 17(8). https://doi.org/10.14569/ijacsa.2026.0170803

- **Decision:** core [preprint] — Adds a Five Whys reviewer scaffold to a multi-agent pipeline and compares it against a matched baseline run to the same depth over three seeds, reporting per-seed variance.
- **Evidence:** This is one of the cleanest harness-isolation designs in the batch: the same multi-agent system, the same seed, the same Domain prefix and the same shared synthesis procedure are held fixed, and the single manipulated factor is whether a data-blind reviewer scaffold is present. The authors additionally equalise analysis depth across arms explicitly to remove trajectory length as a confound, which…
- **Domains:** confounding-attribution, evaluation-validity, failure-attribution, harness-scaffold, reflection-planning, reproducibility
- **Quality:** rigor not yet scored

### Wei, H. (2026). From Agent Loops to Structured Graphs: A Scheduler-Theoretic Framework for LLM Agent Execution. arXiv preprint. https://arxiv.org/abs/2604.11378

- **Decision:** core [preprint] — Analyses the agent control loop as a scheduler, proposes a structured graph harness with an explicit recovery escalation policy, and specifies a seven-group attributable experiment design.
- **Evidence:** A design proposal rather than a study, but it contributes the single most explicit attribution protocol in the batch: a seven-group ladder (naive loop, SOTA prompt-augmented loop, planner loop, structured loop, graph core, +patch, +replan) in which each adjacent pair isolates exactly one harness factor, yielding named gains G_plan, G_scaffold, G_graph, G_patch and G_replan that decompose total im…
- **Domains:** confounding-attribution, evaluation-validity, harness-scaffold, observability-tracing, reflection-planning, reproducibility, retry-recovery
- **Quality:** rigor not yet scored

### Ahn, J., & Kim, M. (2026). From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents. arXiv preprint. http://arxiv.org/abs/2607.08028v1

- **Decision:** core [preprint] — Holds the model fixed and varies only the enforcement layer, and holds the harness fixed under model substitution across 270 runs.
- **Evidence:** This paper runs the two complementary controls that RQ1 and RQ2 jointly require: RQ2 fixes the harness and substitutes only the hosted model across 270 runs, and RQ3 fixes the model and varies only the enforcement layer across 120 paired runs per condition. The result is an unusually clean attribution claim - the reader-facing guarantees moved with the enforcement layer and not with the model, si…
- **Domains:** confounding-attribution, deployment-production, evaluation-validity, governance-safety, harness-scaffold, model-versus-scaffold, observability-tracing, statistical-method
- **Quality:** rigor not yet scored

### Guo, J., Hao, Z., Wang, C., Fan, C., Luo, T., Li, H., Gao, Y., Mei, H., Peng, J., Xu, R., Dong, M., Wu, H., Zheng, M., Han, K., Wang, S., Xu, C., & Wang, Y. (2026). From Question Answering to Task Completion: A Survey on Agent System and Harness Design. arXiv preprint. https://doi.org/10.20944/preprints202606.1312.v1

- **Decision:** core [preprint] — Survey explicitly asking whether the agent performance bottleneck lies in the model, the execution harness or their coupling, and synthesising model-harness evidence; directly addresses RQ1.
- **Evidence:** This survey supplies the largest body of quantitative model-versus-harness evidence in the assignment set, and it is the closest thing available to a direct answer to RQ1's magnitude question. Its central result is that conditioning on the model still leaves a median within-model range of 13.6 percentage points on Terminal-Bench 2.0, with 14 of 20 models varying by at least 10 points and the larg…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, metric-definition, model-versus-scaffold, reproducibility
- **Quality:** rigor not yet scored

### Zhang, L., & Wang, T. (2026). Harness Engineered LLM Agents for Material Science: A Case Study on Perovskite Materials with Machine Learning and Materials Project. ChemRxiv. https://doi.org/10.26434/chemrxiv.15004684/v1

- **Decision:** core [preprint] — Evaluates eleven regressors under an explicit without-Harness versus with-Harness contrast in an LLM-driven materials agent, isolating the harness effect.
- **Evidence:** full text not read (status: unavailable).

### Galster, M., Mohsenimofidi, S., Lulla, J. L., Abubakar, M. A., Treude, C., & Baltes, S. (2026). Harness Engineering for Agentic AI Coding Tools: An Exploratory Study. arXiv preprint. http://arxiv.org/abs/2602.14690v5

- **Decision:** core [preprint] — Empirical study of eight configuration mechanisms for agentic coding tools across 2,853 repositories, making harness configuration itself the measured object.
- **Evidence:** This paper supplies the definitional and empirical grounding for what a harness is, distinguishing context (the input to a single model call) from the harness (the software layers that assemble that context, expose tool schemas and manage turn-by-turn state), and naming the practice of configuring that harness 'harness engineering'. Its contribution to RQ1 is descriptive rather than causal: it ma…
- **Domains:** deployment-production, harness-scaffold, memory-context, prompt-sensitivity, reproducibility, tool-schema
- **Quality:** rigor not yet scored

### He, C., Zhou, X., Wang, D., Xu, H., Liu, W., & Miao, C. (2026). Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime. Preprints.org. https://doi.org/10.20944/preprints202603.1756.v1

- **Decision:** core [preprint] — Position paper decomposing the harness into control, agency and runtime, arguing reported agent gains may be harness-sensitive and proposing HarnessCard reporting.
- **Evidence:** This position paper states the RQ1 thesis explicitly and, unusually, concedes that it supplies no causal evidence for it. Its contribution is conceptual: it decomposes the harness into control, agency and runtime, and argues that the experimental unit in agent research is the coupled execution regime rather than the model, so matching model family while changing tool access, retry budgets, verifi…
- **Domains:** confounding-attribution, evaluation-validity, governance-safety, harness-scaffold, metric-definition, observability-tracing, reproducibility, retry-recovery
- **Quality:** rigor not yet scored

### Barbaste, P., Darrigol, T., Vu, G., & Wiltberger, T. (2026). Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2609.00006

- **Decision:** core [preprint] — Source-code anatomy of eleven production coding harnesses mapping seven subsystems and 29 patterns, establishing how much harnesses differ across systems.
- **Evidence:** This is the most detailed available description of what the harness variable actually contains, which makes it the natural taxonomy source for RQ1: it decomposes the harness into seven subsystems and documents, per system, the minimal and maximal implementation of each, so that 'the harness' can be treated as a structured set of factors rather than an undifferentiated confounder. Its first observ…
- **Domains:** governance-safety, harness-scaffold, memory-context, model-versus-scaffold, reproducibility, retry-recovery, tool-schema, topology-comparison
- **Quality:** rigor not yet scored

### Cheung, J. (2026). Harness Resilience: From LLM Availability to Toolchain Continuity in Agentic AI Engineering. https://doi.org/10.33774/coe-2026-4f53g

- **Decision:** core [preprint] — Argues productivity depends on the execution harness rather than the model alone and contributes a harness reference architecture, failure taxonomy, and evaluation plan.
- **Evidence:** This paper contributes the definitional and vocabulary layer that RQ1 needs rather than any measurement. It draws an explicit operational boundary between the model, the harness (planning loop, context assembly, tool exposure, permissions, approvals, traces, fallback routing) and the application, and argues that the practical unit of dependency is the model-harness combination rather than the mod…
- **Domains:** cost-latency, deployment-production, governance-safety, harness-scaffold, observability-tracing, reproducibility, tool-schema
- **Quality:** rigor not yet scored

### Yao, Y., Tan, X., Liu, C.-H., Li, Y., Wang, Z., Yu, W., Tan, Z., Tian, Y., Zhao, G., Sun, L., Zhang, X., & Yang, T. (2026). Harness-Bench: Measuring harness effects across models in realistic agent workflows. arXiv preprint. https://arxiv.org/abs/2605.27922

- **Decision:** core [preprint] — Diagnostic benchmark that varies harness configurations across model backends under shared tasks and budgets, attributing capability to model-harness pairings rather than the model alone.
- **Evidence:** Harness-Bench is the only paper in the set that makes the harness the primary axis of a full factorial design, crossing 6 harnesses with 8 model backends over 106 fixed tasks, and it is therefore the best available estimate of configuration-level harness variance under matched external conditions. The 23.8-point gap between the best and worst configurable harness under the same task set and model…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, model-versus-scaffold, observability-tracing
- **Quality:** rigor not yet scored

### Hou, Y., Chen, H., Zhou, S., Chen, X., Liu, X., Yuan, D., Meng, L., Wang, S., Liu, Q., & Huang, J. (2026). Harness-G: A Graph-Structured Harness for Search Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2607.27652

- **Decision:** core [preprint] — Redesigns the policy-environment retrieval interface for LLM search agents and shows the interface formulation, not the credit signal, drives measured gains.
- **Evidence:** Harness-G is a rare example of an intervention on the tool and action schema itself, with an explicit transition-matched control that answers RQ2 in the affirmative. The authors hold feasible retrieval targets, environment transitions, deduplication, candidate caps, top-K, budgets, corpora, graph indices, initial checkpoints, questions, reward, group size, batch size, training steps, loss masking…
- **Domains:** benchmark-design, confounding-attribution, environment-coupling, evaluation-validity, harness-scaffold, memory-context, statistical-method, tool-schema
- **Quality:** rigor not yet scored

### Wu, Y., Zhang, J., Shi, J., Lei, X., Gu, Q., Zhang, Y., Wang, Z., He, C., Huang, C., Song, M., Zeng, Z., Wang, S., Liu, J., Shi, Y., Liu, J., Yan, S., Huang, W., Zhang, G., & Zhang, W. (2026). HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?. arXiv preprint. https://arxiv.org/abs/2609.01437

- **Decision:** core [preprint] — Benchmark on LLM-created and self-evolved harnesses under fixed model weights; reports capability and token cost and shows gains depend strongly on the executing model.
- **Evidence:** HarnessDev is the most methodologically explicit paper in the batch on separating harness from model: it freezes each generated harness, then evaluates it twice, once with the creator as executor (Self-Eval) and once with a single fixed executor (Unified-Eval), so that score changes under Unified-Eval are attributable to the harness. The result is a large attribution finding for RQ1: several harn…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, model-versus-scaffold, reproducibility, statistical-method
- **Quality:** rigor not yet scored

### Raj, A. (2026). Harnessing LLMs for Reliable Academic Supervision: A Comparative Study. arXiv preprint. https://doi.org/10.5281/zenodo.21380236

- **Decision:** core [preprint] — Argues harness engineering is a discipline and runs a 2x2 model-by-harness ablation comparing a LangGraph pipeline on a small model against a larger standalone LLM.
- **Evidence:** This case study is designed as an adversarial test of the harness hypothesis: the larger model (GPT-5) is deliberately placed in the thin baseline and the smaller model (GPT-4o-mini) in the engineered harness, so that if the harness contributed little the model gap should have closed the difference. It did not; the harnessed small model won all six rubric dimensions with a 2.85-point pooled gap.…
- **Domains:** confounding-attribution, deployment-production, evaluation-validity, harness-scaffold, model-versus-scaffold, observability-tracing, retry-recovery, statistical-method
- **Quality:** rigor not yet scored

### Bai, Y., Duan, J., Peng, J., Wu, X., Liu, S., Wang, S., & Chen, T. (2026). HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety. arXiv preprint. https://doi.org/10.48550/arxiv.2608.17597

- **Decision:** core [preprint] — Evaluates 14 model-and-harness configurations across three harnesses and six models, showing attack success varies by harness phase independently of the model.
- **Evidence:** HarnessRisk transfers the harness-as-confounder argument into the safety domain and reports one of the largest single-model swings in the batch: GLM-5.2's attack success rate is 4.3x higher on OpenClaw than on Nanobot, and the model ranking for safety reorders across harnesses, so a model-level safety claim derived from one harness does not transfer. For RQ1 the paper is a clear demonstration tha…
- **Domains:** benchmark-design, confounding-attribution, deployment-production, environment-coupling, evaluation-validity, governance-safety, harness-scaffold, model-versus-scaffold
- **Quality:** rigor not yet scored

### Xu, Z., Zhang, S., Poyraz, E., Li, Y., Jin, Y., Lu, X., Gu, X., Ramgopal, K., Bodigutla, P. K., & Wang, X. (2026). Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2, 8334-8345. https://doi.org/10.1145/3770855.3818432

- **Decision:** core — Introduces a hierarchical long-term memory layer for a deployed LLM hiring agent and reports its measured effect on answer correctness, retrieval F1, and latency.
- **Evidence:** This is one of the few papers in the batch that explicitly pins the harness while varying a single component: the backbone LLM, embedding model, serving setup and context-window constraints are held fixed across all eleven memory systems, so the reported deltas are attributable to the memory design rather than to the model. That makes it a clean positive example for RQ2 on the memory axis, though…
- **Domains:** cost-latency, deployment-production, evaluation-validity, governance-safety, harness-scaffold, memory-context, model-versus-scaffold
- **Quality:** rigor not yet scored

### Sundar, N. A., & Morabia, T. (2026). Hierarchical Online Prompt Mutation with Dual-Loop Feedback for Guardrailed Evidence Document Generation: A Production-Evaluation Case Study. arXiv preprint. http://arxiv.org/abs/2606.01472v1

- **Decision:** core [preprint] — Matched production ablation over seven variants on the same 600 cases isolates prompt routing, mutation and feedback components with paired significance tests.
- **Evidence:** HOPM is a clean component-attribution design for RQ1 in a production setting: the base model and the exact 600 cases are matched across seven variants, and the only thing that changes is which harness machinery is switched on (bandit routing, guardrail-attributed prompt mutation, human feedback, automated judge). Because the arms are case-paired, the authors can run exact McNemar tests and paired…
- **Domains:** deployment-production, evaluation-validity, harness-scaffold, metric-definition, prompt-sensitivity, reflection-planning, statistical-method
- **Quality:** rigor not yet scored

### Zhou, T. (2026). Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.08466

- **Decision:** core [preprint] — Contrasts a fixed post-deployment harness with a task-specific evolvable harness under a frozen LLM, isolating the scaffold as the varied factor.
- **Evidence:** HSI is directly aimed at the attribution problem RQ1 poses. It freezes the model, freezes the task-time inference configuration, and disables extended reasoning during task execution specifically so that improvements cannot be credited to extra inference-time compute, then measures what harness evolution alone contributes against a matched hand-crafted harness. The resulting deltas are large (up…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, harness-scaffold, memory-context, model-versus-scaffold, reflection-planning
- **Quality:** rigor not yet scored

### Fei, Y., Liu, N., Yu, X., Chen, S., Li, L., Thapa, R., Ciobanu, M., Singh, N. P., Mao, Q., & Das, R. (2026). How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.14905

- **Decision:** core [preprint] — Evaluates eight harness-model combinations over 800 trajectories and derives a failure taxonomy separating harness-induced from model-induced breakdowns.
- **Evidence:** This is the clearest counter-position to the harness-effect literature in the batch, and it is the only paper here that argues explicitly against a scaffold-level attribution: the same failure patterns recur across all eight harness-model combinations, which the authors take as locating the deficit at the model level rather than in any particular scaffold. They state the intended design for that…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, harness-scaffold, metric-definition, model-versus-scaffold, observability-tracing, reflection-planning
- **Quality:** rigor not yet scored

### Zhai, Z., Tan, X., Zou, G., Wang, X., & Zhang, W. (2026). HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents. arXiv preprint. http://arxiv.org/abs/2608.02650v1

- **Decision:** core [preprint] — Makes the tool schema itself the object of study, planning over a tool-schema hypergraph and reporting the effect on tool-use execution.
- **Evidence:** HyperAgent is a scaffold-versus-scaffold comparison on AppWorld that holds the backbone constant across three model families while swapping ReAct, PlanExec, FullCodeRefl and HyperAgent, which makes it a usable data point for the size of scaffold-attributable differences under a fixed model: roughly 14 TGC points on Test-N for GPT-4o. Its RQ1 value is amplified by the cost decomposition, since the…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, harness-scaffold, reflection-planning, tool-schema
- **Quality:** rigor not yet scored

### Rombaut, B. (2026). Inside the scaffold: A source-code taxonomy of coding agent architectures. arXiv preprint. https://arxiv.org/abs/2604.03515

- **Decision:** core [preprint] — Source-code-level taxonomy of 13 coding-agent scaffolds across control loop, tool interface, and resource management, arguing capability-level surveys cannot distinguish agent architectures.
- **Evidence:** This paper names the RQ1 confound explicitly and in the language the review needs: without a shared vocabulary for scaffold design, researchers cannot attribute observed differences to specific architectural choices, and the confound between scaffold design and model capability goes unacknowledged. It also documents the concrete mechanism by which prior work fails, citing trajectory studies that…
- **Domains:** confounding-attribution, evaluation-validity, harness-scaffold, memory-context, model-versus-scaffold, reproducibility, retry-recovery, tool-schema
- **Quality:** rigor not yet scored

### Naakka, A., Wang, Y., & Mäntylä, M. (2026). LATS-RCA: Language Agent Tree Search for Root Cause Analysis in Microservices. Lecture notes in computer science, 196-212. https://doi.org/10.1007/978-3-032-36590-3_14

- **Decision:** core — Holds the tree-search scaffold fixed while swapping three frontier models, finds only a 1.6-point spread, and contrasts benchmark accuracy with production incidents.
- **Evidence:** This is a rare study that decomposes a multi-agent gain into topology and search-scaffold components rather than reporting a single multi-agent-versus-single-agent delta. Because the two ReAct baselines use the same tools and the same data under the same task formulation, the design separates what specialization plus cross-modal handoff contributes (39.8% to 57.4%) from what the tree-search scaff…
- **Domains:** benchmark-design, cost-latency, deployment-production, evaluation-validity, harness-scaffold, model-versus-scaffold, reflection-planning, topology-comparison
- **Quality:** rigor not yet scored

### Zhang, S., Wang, A., & Sophie, L. (2026). Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2606.11686

- **Decision:** core [preprint] — Decomposes a production agent into layers and shows by controlled regression injection that aggregate task success masks layer-level scaffold faults.
- **Evidence:** The most methodologically direct RQ1 evidence in this batch: the model is removed from the loop entirely (deterministic pure mode, no LLM call), so every measured delta is attributable to a single deliberately degraded scaffold layer while all other layers and the tenant catalog stay fixed. The headline finding is a masking result that speaks straight to the confounding question - a real single-l…
- **Domains:** confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, metric-definition, observability-tracing, reproducibility
- **Quality:** rigor not yet scored

### Gan, C., Wei, H., Liang, Y., Cai, Z., Zhang, Q., & Ni, S. (2026). MAG: A Web-Agent Benchmark and Harness for Multimodal Action and Guide Generation. arXiv preprint. https://doi.org/10.48550/arxiv.2607.10079

- **Decision:** core [preprint] — Builds one harness and holds it constant while comparing frontier models and two grounding schemes over screenshots for the same compound task.
- **Evidence:** MAG is relevant to RQ2 because it is explicit about routing every number in the paper - API baselines, SFT corpus, GRPO rollouts and evaluation - through one shared harness, and because its central comparison holds prompt, observation, budget and scoring identical so that any difference is attributable to the action grounding scheme alone. That makes it one of the few papers here that offers a co…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, harness-scaffold, metric-definition, reproducibility, tool-schema
- **Quality:** rigor not yet scored

### Kinjo, A. R., & Yamamoto, Y. (2026). Measure before you rewrite: ablation-driven redesign of LLM-facing RDF schema documentation in TogoMCP. https://doi.org/10.37044/osf.io/6v5ra_v1

- **Decision:** core [preprint] — Eighteen ablation conditions measure whether each section of the LLM-facing MCP schema documentation earns its tokens, isolating tool-schema effects.
- **Evidence:** full text not read (status: unavailable).

### Zhang, W., Wei, X., Huang, W.-C., Hui, Z., Wang, C., Gong, M., & Yu, P. S. (2026). MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization. arXiv preprint. https://doi.org/10.48550/arxiv.2603.25973

- **Decision:** core [preprint] — Memory benchmark crossing 14 base models with 6 memory methods across 4 tasks, separating model contribution from memory-method contribution.
- **Evidence:** MEMORYCD is a factorial benchmark that crosses 14 models with 6 memory mechanisms while explicitly holding the rest of the harness constant - same user memories, same task prompts, same decoding configuration, same prompting templates, same evaluation scripts, fixed seeds, single standardized cloud environment - so it is a good RQ2 example of a study that does hold the harness constant while vary…
- **Domains:** benchmark-design, evaluation-validity, harness-scaffold, memory-context, metric-definition, model-versus-scaffold, reproducibility
- **Quality:** rigor not yet scored

### Sanabria, D. (2026). OpenAI single-agent LLM architecture reduces computational overhead relative to multi-agent orchestration in a simulated mars rover decision-support benchmark. Frontiers in Robotics and AI, 13, 1877762-1877762. https://doi.org/10.3389/frobt.2026.1877762

- **Decision:** core — Controlled 100-scenario benchmark comparing single-agent and multi-agent architectures on two models with repeated runs, paired statistics, and ablations.
- **Evidence:** This is a rare case of a topology comparison that reports a null result honestly and names the harness confound itself. Both conditions share the same models, the same sanitised inputs, the same JSON output schema and an explicit label-leakage control, so the design is tighter than most single-versus-multi comparisons, but the authors still concede that differences may reflect prompt design as we…
- **Domains:** confounding-attribution, cost-latency, evaluation-validity, failure-attribution, metric-definition, prompt-sensitivity, statistical-method, topology-comparison
- **Quality:** rigor not yet scored

### Mahdi, H. (2026). Perceive, Plan, Act, Self-Correct: An Architectural Framework for Goal-Directed Agentic AI Systems. https://doi.org/10.31224/6738

- **Decision:** core [preprint] — Motivated by incomparability across agent frameworks, it compares five design patterns on standardised suites alongside a benchmark meta-analysis and protocol analysis.
- **Evidence:** full text not read (status: unavailable).

### Wang, S., Qian, P., Lin, Y., Xu, J. Q., Chen, Y., Jiang, X., Liu, L., & Yu, H. (2026). Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2607.13083

- **Decision:** core [preprint] — Deterministic lab showing automated harness optimizers edit scaffolds to fix fabricated failures, quantifying spurious harness change rates.
- **Evidence:** This paper is methodologically the most rigorous attribution study in the batch: it holds the edit space, scorer and proposer fixed and varies only the evidence pool, then crosses that with instruction and specification controls, so every reported effect is causally localised. Its RQ1 relevance is indirect but sharp - it shows that a suppression-only acceptance signal, which is the reward used by…
- **Domains:** confounding-attribution, evaluation-validity, failure-attribution, governance-safety, harness-scaffold, metric-definition, prompt-sensitivity, statistical-method
- **Quality:** rigor not yet scored

### Karten, S., Zhang, A. L., Thomas, K., Müller, S., Bakouch, E., Auras, D., Senghaas, M., Obeid, F., Dunas, K., Hagemann, J., & Jaghouar, S. (2026). Prime Agent: A Self-Improving RLM Harness. arXiv preprint. https://doi.org/10.48550/arxiv.2608.23552

- **Decision:** core [preprint] — Open-source agent harness explicitly framed to stop harness failures being read as model failures; benchmarked against native and popular harnesses.
- **Evidence:** This technical report proposes a harness and evaluates it by holding the model constant and swapping harnesses, so it is a direct source of within-model, cross-harness effect sizes for RQ1. Its most useful contribution is the heterogeneity of those effects: a very large gap on ARC-AGI-3, essentially no gap on the nanoGPT speedrun where the authors say harness choice matters little relative to exp…
- **Domains:** confounding-attribution, cost-latency, evaluation-validity, governance-safety, harness-scaffold, memory-context, observability-tracing, topology-comparison
- **Quality:** rigor not yet scored

### Palmer, C. (2026). professorpalmer/durable-state-vs-context: v1.0.0 — State, Not Tokens. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.20709566

- **Decision:** core — Controlled study varying only how state flows between workers while model, tools, scaffold and oracle are held constant across three architecture arms.
- **Evidence:** full text not read (status: unavailable).

### Jiang, H., Wang, Z., Nie, X., Gao, D., Li, J., & Pei, C. (2026). RCAgentBench: An Agent-Oriented Benchmark for Multimodal Root Cause Analysis in Microservices. 2026 IEEE/ACM International Symposium on Quality of Service (IWQoS), 1-10. https://doi.org/10.1109/iwqos70441.2026.11661026

- **Decision:** core — Agent-oriented RCA benchmark that standardizes tools and agent patterns to decouple tool capability from agent reasoning across a spectrum of LLMs.
- **Evidence:** RCAgentBench is built explicitly around the RQ1 problem: the authors argue that prior root-cause-analysis work mixes powerful tools with specific agent designs so that success cannot be attributed to the agent or the tool, and they respond by standardising three multimodal diagnostic tools and holding them fixed while varying agent pattern and model. Under that control they find that agent-topolo…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, harness-scaffold, model-versus-scaffold, reproducibility, tool-schema, topology-comparison
- **Quality:** rigor not yet scored

### Buldurgan, H. (2026). RE-Bench Is a Systems Benchmark: What Its Scorers and Selection Rules Actually Support. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22089194

- **Decision:** core — Argues RE-Bench scores measure a complete agent system including model, scaffold, tools and budget, directly analysing the validity of model-level inferences.
- **Evidence:** This is a source-contract audit rather than an experiment, and its whole argument is the RQ1 argument: a RE-Bench number belongs to a versioned model-plus-scaffold-plus-protocol system, not to a base model. The audit makes the confound concrete by naming the components that travel with the score, including scaffold, prompt and context policy, tools, hardware, feedback, time budget, attempt alloca…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, harness-scaffold, metric-definition, model-versus-scaffold, reproducibility
- **Quality:** rigor not yet scored

### Aouali, I., Vasile, F., Sakhi, O., Gilotte, A., & Heymann, B. (2026). RecoAtlas: From Semantic Plausibility to Set-Level Utility in LLM Recommendation Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2605.18805

- **Decision:** core [preprint] — Exposes agents to semantic, behaviour-aligned, or faulty tools specifically to diagnose whether gains come from reasoning, signal quality, or tool-use policy.
- **Evidence:** RecoAtlas is designed around exactly the attribution question RQ1 asks: its controlled tool environment exposes agents to semantic, behaviour-aligned or deliberately faulty tools so that performance differences can be diagnosed as coming from stronger reasoning, better signals, or better tool-use policies. Backbones are compared under identical prompts, output schemas, decoding settings, tool bud…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, harness-scaffold, metric-definition, model-versus-scaffold, tool-schema
- **Quality:** rigor not yet scored

### Lee, H., Xu, J., Seely, J., Lee, D., Zaharia, M., & Tang, Y. (2026). Recursive Harness Self-Improvement. arXiv preprint. http://arxiv.org/abs/2607.15524v1

- **Decision:** core [preprint] — Optimises the agent-loop specification itself as a harness variable, raising low-effort agent performance while cutting inference cost by up to 60%.
- **Evidence:** This paper is the mirror image of the harness-as-confound question: instead of holding the harness fixed it deliberately optimises it while holding the base model fixed, and shows the harness alone can move performance past the plateau of test-time reasoning scaling. That is strong evidence for RQ1, because it demonstrates a large, repeatable performance delta attributable to scaffold and inter-a…
- **Domains:** cost-latency, evaluation-validity, harness-scaffold, memory-context, model-versus-scaffold, reflection-planning, topology-comparison
- **Quality:** rigor not yet scored

### Chen, D. T. (2026). RefactorBench-JS: Evaluating LLM Agents on Behavior-Preserving Code Decomposition. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22204480

- **Decision:** core — Evaluates coding agents across two tool configurations, reports model-dependent tool effects, and explicitly flags its production result as not a controlled causal estimate.
- **Evidence:** This is the strongest direct evidence in the batch for RQ1, because it varies exactly one harness component while pinning everything else: same 123 fixtures, temperature 0, tool_choice required, a 50 tool-call cap, up to 3 retries with fresh conversation state, and the same system prompt, with only the test-runner tool toggled. The result is that the same tool is worth +9.8pp for one model and -2…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, model-versus-scaffold, retry-recovery, tool-schema
- **Quality:** rigor not yet scored

### Li, J., & Storhaug, A. (2026). Reproducible, Explainable, and Effective Evaluations of Agentic AI for Software Engineering. https://doi.org/10.1145/3803437.3805548

- **Decision:** core — Analyses evaluation practice across 18 agentic SE papers, showing baseline superiority claims are unjustifiable and irreproducible, and proposes trajectory-level reporting guidelines.
- **Evidence:** full text not read (status: unavailable).

### Gautam, I., & K.C., K. (2026). Retrieval Beats Cheap Structured Memory: A Cost–Retention Study of LLM Agent Memory on Real Long-Conversation Benchmarks. https://doi.org/10.20944/preprints202608.1369.v1

- **Decision:** core [preprint] — Controlled cost-retention comparison of seven LLM-agent memory strategies with paired statistics and an extractor-size ablation isolating the causal bottleneck.
- **Evidence:** This is the cleanest single-variable memory study in the batch and a strong RQ2 exemplar: seven memory strategies are run under one harness, one synthesizer and one judge, with question-level paired statistics rather than aggregate comparisons. Its most direct RQ1 contribution is the extractor-size ablation, which changes exactly one harness component (the 8B write-side extractor becomes 70B) and…
- **Domains:** cost-latency, evaluation-validity, harness-scaffold, memory-context, metric-definition, model-versus-scaffold, reproducibility, statistical-method
- **Quality:** rigor not yet scored

### Sigdel, A., & Baral, R. (2026). Schema First Tool APIs for LLM Agents: A Controlled Study of Tool Misuse, Recovery, and Budgeted Performance. arXiv preprint. http://arxiv.org/abs/2603.13404v1

- **Decision:** core [preprint] — Isolates tool interface design as the experimental variable, holding tool semantics and information content constant across free-form, JSON Schema, and schema-plus-diagnostics conditions.
- **Evidence:** This pilot is methodologically the cleanest single-factor manipulation of a harness component in the set, since the agent loop, system prompt, formatting constraints, tool availability, sandbox artifacts, decoding parameters, tool semantics and runtime error messages are all held constant and only the tool interface representation and validation-diagnostic format change, with information equivale…
- **Domains:** confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, reproducibility, retry-recovery, statistical-method, tool-schema
- **Quality:** rigor not yet scored

### Banjade, S. (2026). Schema-Constrained LLM Planning for Executable Molecular Workflows: An Intent-to-Execution Infrastructure for Cheminformatics. ChemRxiv. https://doi.org/10.26434/chemrxiv.15005091/v1

- **Decision:** core [preprint] — Compares schema-constrained against unconstrained LLM planners and a rule baseline, reporting executable workflow rate rising from 1.8% to 69.1%.
- **Evidence:** full text not read (status: unavailable).

### Zhang, H., Zhang, S., Li, K., Zhang, C., Chen, Y., Zhang, Y., Bai, L., & Hu, S. (2026). Self-Harness: Harnesses That Improve Themselves. arXiv preprint. http://arxiv.org/abs/2606.09498v3

- **Decision:** core [preprint] — Treats agent performance as jointly shaped by model and harness, mining failures to propose validated harness edits across three models and three benchmarks.
- **Evidence:** This is the strongest single piece of harness-attribution evidence in my batch, because the harness is the only thing allowed to move. The authors freeze the model weights, decoding configuration, tool set, budget, benchmark environment and evaluator, then let the same model propose bounded edits to its own harness surfaces, and every one of nine model-benchmark pairs improves on both a held-in s…
- **Domains:** benchmark-design, confounding-attribution, failure-attribution, harness-scaffold, model-versus-scaffold, prompt-sensitivity, reproducibility, retry-recovery
- **Quality:** rigor not yet scored

### Ziwei, Y. (2026). Set-shifting Behavioral Test for Harnessed Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2607.13396

- **Decision:** core [preprint] — Controlled set-shifting design isolates the effect of hidden tool-reliability shifts on harnessed agents across models and measures the effect of policy prompting.
- **Evidence:** This is the clearest RQ2 example in my batch of a study that deliberately holds the harness constant and then checks whether that choice mattered. All four models run inside the same Hermes Agent v0.16.0 with the default system prompt, identical tool schemas, fixed sampling settings and no memory compaction, so cross-model behavioural differences cannot be attributed to scaffold differences. The…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, harness-scaffold, memory-context, prompt-sensitivity, reproducibility, tool-schema
- **Quality:** rigor not yet scored

### Han, J., Xu, Y., Liao, Y., Wang, X., Jiang, Z., Di, Z., Lu, F., Hu, Z., & Xiao, Y. (2026). Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?. arXiv preprint. https://arxiv.org/abs/2608.04828

- **Decision:** core [preprint] — Benchmark evaluating eight LLMs under two agent harnesses; scores and model rankings shift with the harness, making skill use harness-conditioned rather than model-intrinsic.
- **Evidence:** This is one of the strongest direct answers to RQ2 in the set: the authors hold task, sandbox, rubric and judge fixed and run the same eight models under two harnesses, then report that both absolute scores and model rankings move. The head of the leaderboard changes identity (GPT-5.5 under Claude Code, Claude Opus 4.8 under Codex), and four of eight models reverse the sign of their harness delta…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, harness-scaffold, memory-context, model-versus-scaffold, prompt-sensitivity, reproducibility
- **Quality:** rigor not yet scored

### Zhang, Y., Wang, J., Ge, Y., Xu, W., Hamm, J., & Reddy, C. K. (2026). Stop Comparing LLM Agents Without Disclosing the Harness. arXiv (Cornell University). https://doi.org/10.20944/preprints202605.0711.v1

- **Decision:** core [preprint] — Position paper formalizing the claim that harness configuration outweighs model choice and that evaluations misattribute harness gains to models.
- **Evidence:** This is the single most on-target paper in the batch for both research questions. It formalizes RQ1 as a variance decomposition - total benchmark variance splits into model variance, harness variance and a model-by-harness interaction term - and then measures it in a controlled 3x3 factorial on SWE-bench Verified with everything else pinned (same tasks and order, same Docker runtime and evaluatio…
- **Domains:** confounding-attribution, evaluation-validity, harness-scaffold, model-versus-scaffold, reproducibility, retry-recovery, statistical-method, tool-schema
- **Quality:** rigor not yet scored

### Yu, S., Carroll, F., & Bentley, B. L. (2026). The A-R Behavioral Space: Execution-Level Profiling of Tool-Using Language Model Agents in Organizational Deployment. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2604.12116

- **Decision:** core [preprint] — Profiles tool-using agents across three autonomy scaffolds (direct, planning, reflection) and four regimes, making scaffold-induced behavioural shifts the measured object.
- **Evidence:** This study is a controlled scaffold manipulation: the model, prompts, tool schemas, sandbox and decoding temperature are all held fixed while only the reasoning scaffold depth changes across A0, A1 and A2, which makes it a rare direct measurement of a single harness knob's behavioural effect. The magnitudes are large enough to matter for RQ1, with execution rates moving by 60 to 90 percentage poi…
- **Domains:** deployment-production, evaluation-validity, governance-safety, harness-scaffold, metric-definition, reflection-planning, tool-schema
- **Quality:** rigor not yet scored

### Kim, K., Choi, Y., Lee, S., Jun, S., Kim, D., & Park, S. (2026). The Interplay of Harness Design and Post-Training in LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2606.25447

- **Decision:** core [preprint] — Extends ALFWorld to treat the harness as a controllable design dimension and shows harness design changes post-training outcomes under tool-environment shift.
- **Evidence:** This paper is the closest thing in my batch to a direct answer to RQ1, because it runs a factorial over harness informativeness, model size, RL algorithm, tool schema and task distribution on one environment and reports every cell. Its sharpest result for attribution is that a 3B model under a rich harness beats a 7B model under a minimal harness by 14.1 points after identical post-training, mean…
- **Domains:** benchmark-design, confounding-attribution, environment-coupling, evaluation-validity, harness-scaffold, model-versus-scaffold, prompt-sensitivity, tool-schema
- **Quality:** rigor not yet scored

### Zhu, P., Sun, L., Yu, P. S., & Su, S. (2026). The Necessity of a Unified Framework for LLM-Based Agent Evaluation. arXiv preprint. https://arxiv.org/abs/2602.03238

- **Decision:** core [preprint] — Position paper showing that agent benchmark scores confound model, harness, environment, and budget, and that a score's claim depends on the declared candidate boundary.
- **Evidence:** This is the methodological backbone for RQ2 in the assignment set: it argues that whether a harness must be held constant is not a universal rule but a function of the declared candidate boundary, so fixing the scaffold is required for model-level claims, optional for agent-system claims, and deliberately relaxed for robustness claims. It supplies a checklist of exactly the harness components RQ1…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, harness-scaffold, metric-definition, model-versus-scaffold, reproducibility, tool-schema
- **Quality:** rigor not yet scored

### Wang, Y., & Wang, C. (2026). The Observability Gap: Why Output-Level Human Feedback Fails for LLM Coding Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2603.26942

- **Decision:** core [preprint] — Attributes persistent coding-agent failure to an observability gap in the feedback channel rather than model competence, confirmed by a code-level diagnostic intervention.
- **Evidence:** This is a small case study of a multi-agent coding loop in which the human feedback channel, not the model, is the binding constraint: instruction granularity is varied across four groups while the loop architecture, tooling and model family are held fixed. It matters for RQ1 because it isolates one harness component - the feedback/observability channel - and shows that changing only that compone…
- **Domains:** confounding-attribution, environment-coupling, evaluation-validity, failure-attribution, harness-scaffold, observability-tracing, reflection-planning
- **Quality:** rigor not yet scored

### Vats, N., & Golev, O. (2026). The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation. arXiv preprint. http://arxiv.org/abs/2607.22585v1

- **Decision:** core [preprint] — Holds models fixed across three open-source harnesses and attributes 40x token differences and replicated failure fingerprints to harness rather than model.
- **Evidence:** This paper is the closest match in the batch to RQ1 as posed, because it explicitly frames harness choice as a hidden variable and quantifies its share against the model. Holding the model, task instruction, test suite, sandbox, wall-time cap and system-prompt template constant, it finds that harness choice shifts tokens per solved task by 40x while a model upgrade shifts it only 1.0-1.3x, and th…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, model-versus-scaffold, statistical-method
- **Quality:** rigor not yet scored

### Forment, M. A., Guerrero, M. J. C., García-Peñalvo, F. J., & Pereira, J. (2026). The Scaffolding Matters More Than the Interface: A Controlled Comparison of MCP and CLI Tool Use Across Seven Agent Scaffoldings, Five Language Models, and One Software Task. arXiv preprint. http://arxiv.org/abs/2608.08654v1

- **Decision:** core [preprint] — Controlled comparison across seven scaffoldings, five models and one fixed task finds scaffolding, not the MCP-versus-CLI tool interface, dominates cost.
- **Evidence:** This is the most directly on-point paper in the batch for RQ1: it holds the task, the models and the verification identical and varies only the scaffolding, finding a factor-of-20 cost difference between the cheapest and most expensive scaffolding and a 139x spread for a single small model that completed the task under all of them. The authors set out to measure the tool-interface effect (MCP ver…
- **Domains:** confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, model-versus-scaffold, observability-tracing, reproducibility, tool-schema
- **Quality:** rigor not yet scored

### Mayoral-Vilches, V., Balassone, F., Sanz-Gómez, M., Landa, P. Z., Prieto, D. S., Álvarez, M. O., Quarta, D., & Pinzger, M. (2026). Towards Cybersecurity SuperIntelligence (CSI): What's the best harness for cybersecurity?. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2605.28334

- **Decision:** core [preprint] — Benchmarks five agent scaffolds on cybench with the model held fixed, showing no single harness dominates and scaffold choice drives solve rates.
- **Evidence:** This study fixes the model, the per-challenge timeout and the anti-cheat harness and varies only the scaffold, so it is a controlled measurement of the scaffold's contribution in the offensive-security domain. Its most useful RQ1 result is not a single effect size but a structural one: five scaffolds wrapping identical weights fail and succeed on different challenges, with three contributing excl…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, model-versus-scaffold, topology-comparison
- **Quality:** rigor not yet scored

### Team, T. A. L., Sun, Y., Lin, W., Luo, Y., Hu, Y., Jin, M., Ma, J., Pan, W., Zhao, J., & Chen, Z. (2026). Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report. arXiv preprint. http://arxiv.org/abs/2608.15763v3

- **Decision:** core [preprint] — Trains models under harness-state augmentation of skill ids, tool schemas, prompt structures and hooks, reporting harness-variant robustness against fixed-harness training.
- **Evidence:** This industrial technical report is valuable for RQ1 because it measures the harness-model interaction from both directions inside one system. Holding the model fixed, five stages of human-in-the-loop harness evolution move dev-set accuracy from 80.33 to 92.55 and then regress on later long-tail edits, which is a clean demonstration that harness edits alone produce large non-monotonic performance…
- **Domains:** confounding-attribution, cost-latency, deployment-production, evaluation-validity, harness-scaffold, model-versus-scaffold, prompt-sensitivity, tool-schema
- **Quality:** rigor not yet scored

### Matsnev, G. (2026). Uncertainty Decomposition for Clarification Seeking in LLM Agents. arXiv preprint. http://arxiv.org/abs/2606.19559v1

- **Decision:** core [preprint] — Compares clarification scaffolds (ReAct+UE, UAM, and the proposed decomposition) on shared benchmarks across five backbones, separating scaffold gains from model identity.
- **Evidence:** This paper isolates a prompt-level harness change with unusual precision: UAM and the proposed method differ only by the addition of one uncertainty field and its explanation, and the authors attribute the resulting 0.8 percentage-point success-rate drop directly to the enlarged prompt rather than to any architectural change. That is a clean, if small, measurement of harness cost, and it generali…
- **Domains:** confounding-attribution, evaluation-validity, harness-scaffold, memory-context, metric-definition, prompt-sensitivity
- **Quality:** rigor not yet scored

### Orogat, A., Rostam, A., & Mansour, E. (2026). Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis. arXiv preprint. http://arxiv.org/abs/2602.03128v1

- **Decision:** core [preprint] — Introduces an architectural taxonomy and benchmark to isolate multi-agent framework effects under controlled framework-level conditions.
- **Evidence:** This is the strongest controlled evidence in the assignment set for RQ1, because it is explicitly designed as a control-of-variables study: the LLM, prompts, decoding settings, data and scoring are fixed and exactly one framework-level dimension is varied per experiment. Under that design the harness-attributable range is very large, with latency spanning 1.3x to 117x a direct call, planning accu…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, memory-context, reflection-planning, topology-comparison
- **Quality:** rigor not yet scored

### Moghadasi, M. N., & Ghaderi, F. (2026). What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2605.21404

- **Decision:** core [preprint] — Audits twelve agent benchmark papers for disclosure of harness specification, inference settings, cost, and failure breakdown.
- **Evidence:** This is the single most directly relevant paper for RQ2 in the assignment set, because it measures rather than asserts how badly the harness is reported. Its originating anecdote is exactly the RQ1 problem: two reports gave SWE-bench Verified numbers about ten points apart for nominally the same model, and the difference traced to different scaffolds with no pinned version. The audit finds that h…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, metric-definition, reproducibility
- **Quality:** rigor not yet scored

### Yang, K., Bu, Y., Yi, J., Wang, Y., Zhou, B., Dai, J., Hu, S., & Yang, Y. (2026). When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2606.20023

- **Decision:** core [preprint] — Measures how tool privilege schemas and transient tool failures drive escalation in LLM agents and how far prompt-level controls mitigate it.
- **Evidence:** This study fixes the harness completely (same simulated tool-use environment, same six-tool schema, same five-turn cap, same structured tool-call interface, temperature 0) and varies only the backbone model, so behavioural differences of up to 25x in over-privileged tool use are attributable to the model rather than the scaffold. That makes it an unusually clean RQ2 example of holding the harness…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, governance-safety, retry-recovery, tool-schema
- **Quality:** rigor not yet scored

### Yang, B., Cai, Z., Liu, F., Le, B., Zhang, L., Bissyandé, T. F., Liu, Y., & Tian, H. (2025). A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2506.23749

- **Decision:** core [preprint] — Survey classifying 66 LLM repair systems by where control logic resides and auditing which reported results are defensibly comparable across paradigms.
- **Evidence:** This survey is the most systematic RQ2 evidence in the batch about what happens when the harness is not held constant, because it audits comparability at the level of individual reported results rather than benchmark names. Its central quantitative finding is that across 66 LLM repair systems there are 2,145 possible pairwise comparisons, only 100 share a benchmark label, only 32 fall inside boun…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, harness-scaffold, metric-definition, reproducibility, statistical-method
- **Quality:** rigor not yet scored

### Abramovich, T., & Chechik, G. (2025). AblationBench: Evaluating Automated Planning of Ablations in Empirical AI Research. arXiv preprint. http://arxiv.org/abs/2507.08038v3

- **Decision:** core [preprint] — Benchmark for agent ablation planning that reports chain-of-thought prompting outperforming an agent-based scaffold on the same tasks and models.
- **Evidence:** AblationBench runs the same frontier models under two scaffoldings, a single chain-of-thought call and a ReAct-style SWE-agent, for both the planner role and the judge role, which makes it a direct harness-versus-model experiment. The result is a strong negative for scaffold complexity: the agent harness never wins and for weaker models it is catastrophic, dropping GPT-OSS-120B from 0.37 to 0.11…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, model-versus-scaffold, reflection-planning, statistical-method
- **Quality:** rigor not yet scored

### Kaplunovich, A. (2025). Advancing LLM Agents for Code Generation: Observability, Orchestration, Reliable Performance. 2025 International Conference on Intelligent Computing, Communication, Networking and Services (ICCNS), 108-116. https://doi.org/10.1109/iccns66249.2025.11428688

- **Decision:** core — Contrasts default agent framework implementations against workflow, flow-control, prompt-management and logging additions across LlamaIndex, LangChain and CrewAI, reporting reliability gains.
- **Evidence:** This is one of the few papers in the batch that treats the retry budget as a first-class experimental variable, reporting accuracy at each retry index from 0 through 6 for every model pairing, which makes the harness contribution legible rather than bundled into a single headline number. The retry curves show the confound plainly: claude-3-haiku leads at retry 0 with 85% but ends lower than llama…
- **Domains:** confounding-attribution, cost-latency, failure-attribution, harness-scaffold, model-versus-scaffold, observability-tracing, retry-recovery, topology-comparison
- **Quality:** rigor not yet scored

### Chevrot, A., Vernotte, A., Falleri, J., Blanc, X., Legeard, B., & Cretin, A. (2025). Are Autonomous Web Agents Good Testers?. Proceedings of the ACM on software engineering., 2(ISSTA), 206-228. https://doi.org/10.1145/3728879

- **Decision:** core — Benchmarks two autonomous test-agent implementations on the same 113 test cases, attributing a 50% performance gap to the agent scaffold rather than the model.
- **Evidence:** This is the single most direct RQ1 study in this batch because it runs both halves of the attribution experiment on the same benchmark. With the model pinned to GPT-4o, replacing a thin single-prompt scaffold with an orchestrator-actor-assertor scaffold with retry produced a greater than 50 percent relative gain in true accuracy; with the scaffold pinned to PinATA, swapping across GPT-4o, Sonnet…
- **Domains:** benchmark-design, confounding-attribution, environment-coupling, evaluation-validity, failure-attribution, harness-scaffold, metric-definition, model-versus-scaffold, topology-comparison
- **Quality:** rigor not yet scored

### Soularidis, A., Doumanas, D., Kotis, K., & Vouros, G. A. (2025). Automating agentic collaborative ontology engineering with role-playing simulation of LLM-powered agents and RAG technology. The Knowledge Engineering Review, 40. https://doi.org/10.1017/s026988892510009x

- **Decision:** core — Investigates how far the selected RAG components and ReAct guidelines change the quality of ontologies produced by an LLM role-playing agent system.
- **Evidence:** This paper is a component-level ablation of a retrieval-and-guidance harness around a fixed LLM, model and prompt, which makes it usable evidence for RQ1 even though its framing is ontology engineering rather than agent evaluation. Across four settings the authors add and remove domain documents, OWL documentation and ReAct thought-action-observation guidelines and observe non-monotonic effects:…
- **Domains:** benchmark-design, evaluation-validity, harness-scaffold, memory-context, prompt-sensitivity, reflection-planning
- **Quality:** rigor not yet scored

### Miller, H. E., Greenig, M., Tenmann, B., & Wang, B. (2025). BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML. bioRxiv (Cold Spring Harbor Laboratory). https://doi.org/10.1101/2025.09.01.673319

- **Decision:** core [preprint] — Benchmarks four LLM agents on identical biomedical ML tasks and concludes architecture and scaffolding may determine performance more than domain specialisation.
- **Evidence:** BioML-bench is a benchmark paper whose main finding is directly on-topic for RQ1: it reports no consistent advantage for biomedical-specialised agents over generalist ML agents and concludes that architecture and scaffolding, not domain specialisation, appear to be the primary drivers of measured capability. It is equally useful as a cautionary case for RQ2, because the study explicitly does not…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, harness-scaffold, model-versus-scaffold, reproducibility
- **Quality:** rigor not yet scored

### Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025). BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2508.06600

- **Decision:** core [preprint] — Rebuilds BrowseComp on a fixed curated corpus expressly to make deep-research agent comparisons fair and reproducible and to isolate retriever contributions.
- **Evidence:** BrowseComp-Plus is a benchmark built explicitly to remove a harness confound: it argues that live black-box web search APIs conflate agent system performance with retrieval-component effectiveness, making fair comparison and reproducibility impossible, and replaces them with a fixed, human-verified corpus so retrieval and reasoning can be evaluated separately. That is a direct RQ2 case of a study…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, harness-scaffold, memory-context, model-versus-scaffold, reproducibility, tool-schema
- **Quality:** rigor not yet scored

### Wang, Z., Huang, H., Zhao, H., Xu, C., Zhu, S., Janßen, J., & Viswanathan, V. (2025). DREAMS: Density Functional Theory Based Research Engine for Agentic Materials Simulation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2507.14267

- **Decision:** core [preprint] — Ablates the multi-tier verification guard against an unguarded counterpart and disables verification layers individually, reporting accuracy and token-cost effects.
- **Evidence:** DREAMS contributes an explicitly designed ablation for RQ1: the DREAMS versus DREAMS_safe comparison holds the canvas, orchestration and backbone model fixed and varies only the multi-tier safety guard, which the authors present as the one contrast in the paper that isolates a causal contribution. That contrast produced no change in the headline number but a large change in process validity and c…
- **Domains:** confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, memory-context, observability-tracing, reproducibility
- **Quality:** rigor not yet scored

### Shekkizhar, S., Cosentino, R., Earle, A., & Savarese, S. (2025). Echoing: Identity Failures when LLM Agents Talk to Each Other. arXiv preprint. https://doi.org/10.48550/arxiv.2511.09710

- **Decision:** core [preprint] — Measures echoing across 66 agent-agent configurations, argues it is not an experiment-design artifact, and shows a structured-response protocol change cuts it to 9%.
- **Evidence:** Echoing is relevant to RQ1 mainly through its protocol-level mitigation result: holding the model, tools, domain and turn budget fixed and changing only the response schema so that each agent must explicitly declare its role drops the failure rate from 32-38% to below 10%. That is a tool-schema and message-format intervention producing a larger effect than reasoning effort or prompt engineering,…
- **Domains:** confounding-attribution, evaluation-validity, failure-attribution, governance-safety, harness-scaffold, metric-definition, prompt-sensitivity, tool-schema, topology-comparison
- **Quality:** rigor not yet scored

### Lee, G., Bach, E., Yang, E., Pollard, T., Johnson, A. E. W., Choi, E., jia, Y., & Lee, J. H. (2025). FHIR-AgentBench: Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2509.19319

- **Decision:** core [preprint] — Benchmark that systematically compares retrieval strategies, single-turn versus multi-turn interaction and reasoning strategies for agents on fixed clinical questions.
- **Evidence:** FHIR-AgentBench runs a controlled ablation over three harness axes on a fixed benchmark, prompt family and 32k context budget: interaction pattern (single-turn versus multi-turn), retrieval mechanism (direct FHIR API query generation versus a specialized retriever), and reasoning strategy (natural language versus code generation). The result is a clean RQ1 data point that harness composition domi…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, harness-scaffold, memory-context, model-versus-scaffold, tool-schema
- **Quality:** rigor not yet scored

### Kapoor, S., Stroebl, B., Kirgis, P., Nadgir, N., Siegel, Z. S., Wei, B., Xue, T., Chen, Z., Chen, F., Utpala, S., Ndzomga, F., Oruganty, D., Luskin, S., Liu, K., Yu, B., Arora, A., Hahm, D., Trivedi, H., Sun, H., ... Narayanan, A. (2025). Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2510.11977

- **Decision:** core [preprint] — Standardised evaluation harness with 21,730 rollouts analysed three-dimensionally across models, scaffolds, and benchmarks - the separation RQ1 asks for.
- **Evidence:** HAL is the central RQ1 and RQ2 reference in this batch because it makes scaffold an explicit third evaluation axis alongside model and benchmark, and standardizes the harness so that cross-model comparison is apples-to-apples. Its most consequential RQ2 finding is that prior work almost never did this: only 2 of the nine benchmarks had ever been run with the same scaffold across four or more of t…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, model-versus-scaffold, observability-tracing, reproducibility
- **Quality:** rigor not yet scored

### Zhuang, N., Cao, B., Yang, Y., Xu, J., Xu, M., Wang, Y., & Liu, Q. (2025). LLM Agents Can Be Choice-Supportive Biased Evaluators: An Empirical Study. Proceedings of the AAAI Conference on Artificial Intelligence, 39(25), 26436-26444. https://doi.org/10.1609/aaai.v39i25.34843

- **Decision:** core — Empirical study across nineteen models showing evaluator bias in LLM agents varies sharply with prompt construction and context preservation.
- **Evidence:** This paper is only indirectly about harnesses, but it supplies a sharp prompt-sensitivity result relevant to RQ1: changing two words in the evaluator's system prompt, from 'was chosen' to 'was chosen by you', increased the chosen-option bias from 2.30/-1.6 to 3.50/-2.3 and roughly tripled the F statistic, with everything else held constant (same models, temperature zero, randomised feature and op…
- **Domains:** confounding-attribution, evaluation-validity, failure-attribution, governance-safety, prompt-sensitivity, reflection-planning, statistical-method
- **Quality:** rigor not yet scored

### Souza, R., Poteet, T., Etz, B., Rosendo, D., Gueroudji, A., Shin, W., Balaprakash, P., & da Silva, R. F. (2025). LLM Agents for Interactive Workflow Provenance: Reference Architecture and Evaluation Methodology. arXiv preprint, 2257-2268. https://doi.org/10.1145/3731599.3767582

- **Decision:** core [preprint] — Evaluation methodology for provenance agents comparing four models within one architecture and reporting the effect of modular design, prompt tuning and RAG.
- **Evidence:** Although this is an HPC systems paper rather than an agent-methodology paper, it contains a well-formed harness-versus-model comparison. Holding the model constant, the authors add prompt and retrieval context one component at a time and record both accuracy and token cost, showing a swing from 0.06 to 0.97 driven entirely by context construction, with query guidelines delivering the largest gain…
- **Domains:** cost-latency, evaluation-validity, harness-scaffold, memory-context, model-versus-scaffold, observability-tracing, prompt-sensitivity
- **Quality:** rigor not yet scored

### Liao, M. (2025). Process-Aware LLM-Agent Scaffolds for Metric-Based Microservice Root-Cause Analysis with Evidence-Trace Scoring. Stout in Computer Science and Technology Studies, 1(1), 48-61. https://doi.org/10.61424/zngee941

- **Decision:** core — Evaluates a process-aware LLM-agent scaffold under leakage controls and leave-one-repetition-out folds with evidence-trace scoring of the cited support.
- **Evidence:** Despite its title, this paper evaluates a deterministic scaffold and its audit record rather than any language model, which the authors state outright; it therefore contributes to RQ1 as a demonstration that scaffold and evidence-retrieval choices can be varied while the underlying prediction is held exactly fixed. The key result is a separability claim: swapping the evidence policy changed the e…
- **Domains:** confounding-attribution, evaluation-validity, failure-attribution, harness-scaffold, metric-definition, observability-tracing, reproducibility, statistical-method
- **Quality:** rigor not yet scored

### Kuligin, L., Lammert, J., Ostapenko, A., Bressem, K. K., Boeker, M., & Tschochohei, M. (2025). Prompt design for medical question answering with Large Language Models. Machine Learning with Applications, 22, 100758-100758. https://doi.org/10.1016/j.mlwa.2025.100758

- **Decision:** core — Evaluates 21 LLMs across five prompting techniques including ReAct with search, attributing end-to-end performance to the technique and model combination.
- **Evidence:** full text not read (status: unavailable).

### Kale, N., Zhang, C. B. C., Zhu, K., Aich, A., Rodriguez, P., Team, S. R., Knight, C. Q., & Wang, Z. (2025). Reliable Weak-to-Strong Monitoring of LLM Agents. arXiv preprint. http://arxiv.org/abs/2508.19461v1

- **Decision:** core [preprint] — Red-teams monitor scaffoldings and reports that monitor scaffolding matters more than monitor awareness, attributing outcomes directly to the scaffold.
- **Evidence:** This is one of the strongest RQ1 results in the batch outside the deep-research setting, because it factorially separates monitor scaffolding from monitor information. Holding the monitor LLM, dataset and threat model fixed, the authors vary only how the agent trajectory is parsed into the monitor (full trajectory, hierarchical summarization, sequential windows, or a hybrid) and separately vary h…
- **Domains:** benchmark-design, confounding-attribution, evaluation-validity, failure-attribution, governance-safety, harness-scaffold, metric-definition, observability-tracing
- **Quality:** rigor not yet scored

### Yan, J., & Yang, M. (2025). Schema-Preserving Generation of Clinical TLF Templates and Executable R Code via Iterative LLM-Guided Debugging. https://doi.org/10.36227/techrxiv.176045741.13024122/v1

- **Decision:** core [preprint] — Compares five generation methods across three LLM providers with 1,999 bootstrap experiments and an iterative debugging loop, separating method from model effects.
- **Evidence:** full text not read (status: unavailable).

### AUDEBEAU, A. C. (2025). Structured PREreview of "An Exploratory Study of Code Retrieval Techniques in Coding Agents". Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.17536687

- **Decision:** core — Structured review of a coding-agent retrieval study naming uncontrolled confounds (model, context window, prompts, tool inventory, architecture) that block causal attribution.
- **Evidence:** full text not read (status: unavailable).

### Tripathy, A., Harshit, C. P., & Vaidhyanathan, K. (2025). SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs. arXiv preprint, 104-111. https://doi.org/10.1145/3786167.3788406

- **Decision:** core [preprint] — Controlled evaluation of four agentic issue-resolution frameworks on fixed SLMs, hardware and benchmark, finding framework architecture drives energy consumption.
- **Evidence:** SWEnergy holds the model, hardware, timeout, context window and benchmark constant and varies only the agentic framework, which makes it a clean single-factor harness experiment even though its outcome variable is energy rather than accuracy. Its finding is that framework architecture is the primary driver of resource consumption, spanning 9.4x between the most and least energy-intensive scaffold…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, model-versus-scaffold, retry-recovery
- **Quality:** rigor not yet scored

### Zhang, J., Xiang, J., Yu, Z., Teng, F., Chen, X., Chen, J., Zhuge, M., Cheng, X., Hong, S., Wang, J., Zheng, B., Liu, B., Luo, Y., & Wu, C. (2024). AFlow: Automating Agentic Workflow Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2410.10762

- **Decision:** core [preprint] — Searches over code-represented agentic workflows and reports that the optimised scaffold lets smaller models beat GPT-4o at a fraction of the cost.
- **Evidence:** AFLOW is the strongest single quantification of harness effect size in this batch, because every compared method, manual and automated, is executed with the same GPT-4o-mini on the same split, so the full 67.2 to 80.3 average spread is attributable to workflow structure rather than to the model. Notably ADAS, an automated scaffold, scores below plain IO prompting on average (67.2 versus 72.8), sh…
- **Domains:** benchmark-design, confounding-attribution, cost-latency, harness-scaffold, model-versus-scaffold, prompt-sensitivity, reflection-planning
- **Quality:** rigor not yet scored

### Siegel, Z. S., Kapoor, S., Nadgir, N., Stroebl, B., & Narayanan, A. (2024). CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark. arXiv preprint. https://doi.org/10.48550/arxiv.2409.11363

- **Decision:** core [preprint] — Crosses two agent scaffolds (generic AutoGPT vs task-specific CORE-Agent) with two underlying models on one benchmark, separating scaffold from model.
- **Evidence:** CORE-Bench provides the cleanest 2x2 attribution table in this batch: for each fixed LLM the authors compare a generalist AutoGPT against a lightly customised CORE-Agent, and for each fixed agent they compare two models. The scaffold effect is very large and asymmetric, taking GPT-4o-mini from 8.89 to 44.44 percent on Easy and GPT-4o from 35.56 to 60.00, meaning that a comparison of these two mod…
- **Domains:** benchmark-design, cost-latency, evaluation-validity, harness-scaffold, model-versus-scaffold, prompt-sensitivity, reproducibility, tool-schema
- **Quality:** rigor not yet scored

### Xia, B., Lu, Q., Zhu, L., Xing, Z., Zhao, D., & Zhang, H. (2024). Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2411.13768

- **Decision:** core [preprint] — Argues fixed benchmarks cannot capture agent behaviour shaped by system-level interactions, and derives a lifecycle evaluation process model and architecture.
- **Evidence:** This paper contributes a measured, corpus-level argument for RQ1 rather than a controlled experiment: across 134 academic sources it finds that two thirds evaluate at the model level and only 12 percent evaluate models and systems jointly, and it argues explicitly that isolating prompts and responses hides orchestration, tool behaviour, dependencies and error propagation, so models that look stro…
- **Domains:** confounding-attribution, deployment-production, evaluation-validity, failure-attribution, governance-safety, harness-scaffold, metric-definition, observability-tracing, reproducibility
- **Quality:** rigor not yet scored

### Zhang, W., Guo, H., Yang, J., Tian, Z., Zhang, Y., Yan, C., Li, Z., Li, T., Shi, X., Zheng, L., & Zhang, B. (2024). mABC: multi-Agent Blockchain-Inspired Collaboration for root cause analysis in micro-services architecture. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2404.12135

- **Decision:** core [preprint] — Multi-agent LLM root cause analysis that standardises an Agent Workflow with step limits and voting, and ablates the workflow to isolate its contribution.
- **Evidence:** MABC is a topology-comparison paper whose ablation is partially harness-controlled: with the backbone pinned to GPT-4-Turbo the authors remove multi-agent decomposition, the Agent Workflow, and the voting layer in turn, and report that collapsing to a single agent causes the largest drop (54.4 to 38.4 RA on Train-Ticket). That is useful for RQ2 because it isolates topology from the model. However…
- **Domains:** confounding-attribution, deployment-production, evaluation-validity, failure-attribution, harness-scaffold, metric-definition, model-versus-scaffold, retry-recovery, topology-comparison
- **Quality:** rigor not yet scored

### De Chezelles, T. L. S., Gasse, M., Drouin, A., Caccia, M., Boisvert, L., Thakkar, M., Marty, T., Assouel, R., Shayegan, S. O., Jang, L., Lù, X. H., Yoran, O., Kong, D., Xu, F. F., Reddy, S., Cappart, Q., Neubig, G., Salakhutdinov, R., Chapados, N., & Lacoste, A. (2024). The BrowserGym Ecosystem for Web Agent Research. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2412.05467

- **Decision:** core [preprint] — Unifies web-agent benchmarks in one gym-like harness precisely to fix inconsistent evaluation, then compares six LLMs under that fixed scaffold.
- **Evidence:** This paper is an explicit RQ2 example: it holds one agent implementation, one observation space and one action space fixed and swaps only the backbone model, and it names that design as one of three intended use cases for the ecosystem. It is also the clearest documentation in this batch of harness components that usually go unreported, including a retry policy that re-prompts the LLM up to four…
- **Domains:** benchmark-design, evaluation-validity, harness-scaffold, model-versus-scaffold, observability-tracing, reproducibility, retry-recovery, tool-schema
- **Quality:** rigor not yet scored

### Zhang, Y., Ma, Z., Ma, Y., Han, Z., Wu, Y., & Tresp, V. (2024). WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2408.15978

- **Decision:** core [preprint] — Holds GPT-4 fixed while replacing the control loop with dual-optimization MCTS and reports a 93% relative success-rate gain over a concurrent tree-search scaffold.
- **Evidence:** WebPilot is a system paper whose comparisons illustrate the confound rather than control for it, which makes it useful as a RQ2 negative example alongside its ablation evidence. Its headline 93% relative gain over LM-Tree Search and its lead over SteP are whole-stack comparisons in which orchestration, prompting strategy and demonstration budget all differ simultaneously, since SteP uses 10 actio…
- **Domains:** benchmark-design, environment-coupling, evaluation-validity, harness-scaffold, model-versus-scaffold, reflection-planning, topology-comparison
- **Quality:** rigor not yet scored

### Chen, Z., White, M., Mooney, R., Payani, A., Su, Y., & Sun, H. (2024). When is Tree Search Useful for LLM Planning? It Depends on the Discriminator. https://doi.org/10.18653/v1/2024.acl-long.738

- **Decision:** core — Decomposes a language agent into generator, discriminator and planner, showing discriminator accuracy, not the planning scaffold, governs whether tree search helps.
- **Evidence:** This paper is close to a controlled experiment on harness attribution: the generator LLM, sampling budget and prompts are held fixed while the planning method and the discriminator are varied one factor at a time. It shows that the choice of scaffold (re-ranking versus iterative correction versus tree search) is largely dominated by the quality of a different harness component, the discriminator,…
- **Domains:** confounding-attribution, cost-latency, evaluation-validity, failure-attribution, harness-scaffold, model-versus-scaffold, reflection-planning, statistical-method
- **Quality:** rigor not yet scored


## Supporting (247)

### Ferrag, M. A., Lakas, A., & Debbah, M. (2026). 6G-Bench: An Open Benchmark for Semantic Communication and Network-Level Reasoning With Foundation Models in AI-Native 6G Networks. IEEE Open Journal of the Communications Society, 7, 3305-3330. https://doi.org/10.1109/ojcoms.2026.3680457

- **Decision:** supporting — Open benchmark of 30 network decision tasks for foundation models and multi-agent coordination in 6G settings.
- **Evidence:** full text not read (status: pending).

### Luoma, K., & Kumar, A. (2026). A Comparative Evaluation of Schema Subsetting for LLM-based NL-to-SQL over Large-Schema Databases. Proceedings of the VLDB Endowment, 19(9), 2019-2031. https://doi.org/10.14778/3819518.3819531

- **Decision:** supporting — Systematic ablation of seven schema-subsetting modules across three NL-to-SQL benchmarks quantifying how context/schema reduction shifts LLM accuracy.
- **Evidence:** full text not read (status: pending).

### Srinivasan, V. (2026). A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2605.20173

- **Decision:** supporting [preprint] — Catalog of six production agent runtime patterns plus a selection methodology; a combinable design method without empirical evaluation.
- **Evidence:** full text not read (status: pending).

### Trong, M. P., Son, N. T., Giang, V. T., Viet, B. H., Hai, L. N., & Tung, D. T. (2026). A process-centric review of large language models in graphical user interface testing: architectures, lifecycle impact, and challenges. PeerJ Computer Science, 12, e3695-e3695. https://doi.org/10.7717/peerj-cs.3695

- **Decision:** supporting — Process-centric review of 55 LLM-agent GUI testing studies that maps architectures and flags a reliability, cost and latency gap between prototypes and industry.
- **Evidence:** full text not read (status: pending).

### Arora, J., & Singh, G. (2026). A Reliability Control Framework for Robust Multi-Agent LLM Systems: Managing Workflows in Large Language Model Systems. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.20071516

- **Decision:** supporting — Seven-layer reliability control framework with fault recovery, observability, and simulation evidence for production multi-agent systems.
- **Evidence:** full text not read (status: pending).

### Syromiatnikov, M. V., & Ruvinskaya, V. M. (2026). A system internals modeling and annotation language for large language model-driven software engineering. Applied Aspects of Information Technology, 9(1), 103-121. https://doi.org/10.15276/aait.09.2026.08

- **Decision:** supporting — Compact context-representation language for LLM software workflows validated on token efficiency, schema validity and semantic faithfulness.
- **Evidence:** full text not read (status: pending).

### Peter, J. B. J. (2026). A Tiered Multimodal Memory and Event-Graph Architecture for Real-Time Agentic AI Systems. SoutheastCon 2026, 1-5. https://doi.org/10.1109/southeastcon63549.2026.11476389

- **Decision:** supporting — Tiered memory and event-graph architecture for agentic reasoning evaluated on latency, accuracy and storage cost against full-retention baselines.
- **Evidence:** full text not read (status: pending).

### Xia, X., Yao, C., Tsoi, M., Mao, X., Huang, W., Wei, J., Wu, H., Tan, C., Yu, L., Yang, Y., Liu, M., Sun, S., & Gao, Z. (2026). AblateCell: A Reproduce-then-Ablate Agent for Virtual Cell Repositories. arXiv preprint. https://doi.org/10.48550/arxiv.2604.19606

- **Decision:** supporting [preprint] — Agent that reproduces baselines then runs isolated ablations to attribute performance gains, contributing attribution methodology in a biology setting.
- **Evidence:** full text not read (status: pending).

### Lee, Y., Koneru, K., Moslemi, Z., Kumar, S., & Radhakrishnan, R. (2026). AEMA: Verifiable Evaluation Framework for Trustworthy and Controlled Agentic LLM Systems. arXiv preprint. http://arxiv.org/abs/2601.11903v1

- **Decision:** supporting [preprint] — Evaluation-methodology framework for multi-agent LLM systems claiming greater stability and human alignment than single LLM-as-a-Judge scoring.
- **Evidence:** full text not read (status: pending).

### Nageshwaran, V., & Ezekiel, S. (2026). Agentic AI and Large Language Models for Autonomous IoT Cybersecurity: A Systematic Survey, Taxonomy, and Research Roadmap. Electronics, 15(12), 2740-2740. https://doi.org/10.3390/electronics15122740

- **Decision:** supporting — PRISMA survey of 153 studies taxonomizing agent architecture, reasoning strategy and deployment topology, and consolidating datasets and benchmarks.
- **Evidence:** full text not read (status: pending).

### Makroum, R. E., Zwickl-Bernhard, S., & Kranzl, L. (2026). Agentic AI home energy management system: A large language model framework for residential load scheduling. Results in Engineering, 29, 109857-109857. https://doi.org/10.1016/j.rineng.2026.109857

- **Decision:** supporting — Compares three open-source LLMs inside one fixed ReAct orchestrator-plus-specialist architecture without analysing how much of the gap the harness contributes.
- **Evidence:** full text not read (status: pending).

### Alva, L., & Pandey, B. K. (2026). Agentic AI systems in the age of generative models: architectures, cloud scalability, and real-world applications. Artificial Intelligence Review, 59(3). https://doi.org/10.1007/s10462-025-11458-6

- **Decision:** supporting — Proposes an agentic framework contrasted with AutoGPT and ReAct with experimental verification but no stated harness control.
- **Evidence:** full text not read (status: pending).

### Gajwani, G., & Soni, V. (2026). Agentic AI-Driven Workflow Orchestration in Loan Trading Platforms: A Microservices and Hybrid Cloud Architecture Perspective. 2026 International Conference on Artificial Intelligence, Systems, and Emerging Technologies (ICAISET), 1-6. https://doi.org/10.1109/icaiset66439.2026.11541301

- **Decision:** supporting — Compares static with policy-driven agentic recovery under injected failures; harness here denotes the test rig and LLM involvement is never stated.
- **Evidence:** full text not read (status: pending).

### Vuppu, D., & Achanta, M. (2026). Agentic Data Pipeline Orchestration with Multi-Agent AI. SoutheastCon 2026, 1-6. https://doi.org/10.1109/southeastcon63549.2026.11476299

- **Decision:** supporting — Multi-agent pipeline control plane with adaptive retries and risk gates validated by fault injection, but the retry policy is never isolated.
- **Evidence:** full text not read (status: pending).

### Zhang, L., Jia, T., Zhai, Y., Pan, L., Duan, C., He, M., Jia, M., & Li, Y. (2026). Agentic Memory Enhanced Recursive Reasoning for Root Cause Localization in Microservices. https://doi.org/10.1145/3786583.3786853

- **Decision:** supporting — Agentic memory and recursive reasoning for microservice root-cause localization, compared against LLM baselines without harness control.
- **Evidence:** full text not read (status: pending).

### Gao, Z. (2026). Agentic Verifier-in-the-Loop Solver Orchestration for Cell-Free Massive MIMO Downlink Power Control. arXiv preprint. http://arxiv.org/abs/2603.23128v1

- **Decision:** supporting [preprint] — Verifier-in-the-loop router over trusted solvers is compared with fixed single-solver baselines on a reproducible prototype benchmark.
- **Evidence:** full text not read (status: pending).

### Yagoubi, F. E., Badu-Marfo, G., & Al Mallah, R. (2026). AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems. IEEE Access, 14, 94960-94978. https://doi.org/10.1109/access.2026.3704541

- **Decision:** supporting — Benchmark comparing single-agent versus coordinator-worker LLM configurations for internal-channel leakage across five models; configuration comparison with harness control unstated.
- **Evidence:** full text not read (status: pending).

### Chen, F., Wu, T., Nguyen, V., Nepal, S., & Rudolph, C. (2026). Agents at Risk: How Users Unwittingly Undermine LLM Safety. arXiv preprint. http://arxiv.org/abs/2601.10758v3

- **Decision:** supporting [preprint] — Evaluates a context-manipulation attack against five prompt-injection baselines under prevention and detection defences that are themselves harness layers.
- **Evidence:** full text not read (status: pending).

### Fang, E. (2026). AgentVerify: Compositional Formal Verification of AI Agent Safety Properties via LTL Model Checking. Preprints.org. https://doi.org/10.20944/preprints202604.1029.v1

- **Decision:** supporting [preprint] — Formal LTL verification of agent memory, tool-call, and human-in-the-loop properties, evaluated on 15 scenarios against a monolithic baseline.
- **Evidence:** full text not read (status: pending).

### Santos-Grueiro, I. (2026). Alignment Verifiability in Large Language Models: Normative Indistinguishability under Behavioral Evaluation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2602.05656

- **Decision:** supporting [preprint] — Formalises why bounded behavioural evaluation cannot identify latent alignment when policies are evaluation-aware; a validity limitation for agent benchmarking.
- **Evidence:** full text not read (status: pending).

### Liu, G., He, M., Sun, L., 成福仙, & Zhang, Y. (2026). An autonomous LLM-agent platform for computational binder design and conjugation-aware prioritization of antibody–drug conjugates. bioRxiv (Cold Spring Harbor Laboratory). https://doi.org/10.64898/2026.04.21.719907

- **Decision:** supporting [preprint] — Autonomous LLM-agent platform whose controlled ablation compares routing strategies and claims LLM-agnostic behavior across models.
- **Evidence:** full text not read (status: pending).

### Yang, J., Liu, P., Zhang, C., & Stojkovic, J. (2026). Architectural Implications of Agentic AI Workflows. arXiv preprint. https://doi.org/10.48550/arxiv.2608.04458

- **Decision:** supporting [preprint] — Production and controlled framework characterisation quantifying how orchestration and tool execution drive latency and utilisation; harness cost evidence, not task performance.
- **Evidence:** full text not read (status: pending).

### Qi, C., Wang, W., Jiang, S., Liu, Q., Song, X., Fang, H., & Wei, Z. (2026). Artificial Intelligence agents for biological research: a survey. Briefings in Bioinformatics, 27(1). https://doi.org/10.1093/bib/bbag075

- **Decision:** supporting — Survey of over 100 biological AI agent studies with a taxonomy spanning system architectures, interaction modes and evaluation strategies.
- **Evidence:** full text not read (status: pending).

### Yan, B., Zhang, X., Zhou, Z., Li, C., Zeng, R., Qi, Y., Wang, T., & Zhang, L. (2026). Attack the Messages, Not the Agents: A Multi-round Adaptive Stealthy Tampering Framework for LLM-MAS. Proceedings of the AAAI Conference on Artificial Intelligence, 40(35), 29784-29792. https://doi.org/10.1609/aaai.v40i35.40224

- **Decision:** supporting — Communication-tampering attack evaluated across tasks, communication architectures, and LLMs; a robustness result across configurations.
- **Evidence:** full text not read (status: pending).

### Krämer, R., & Heger, J. (2026). Automated Generation of Simulation Models for Production and Logistics Processes Using LLM-Based Multi-Agent Systems. SNE Simulation Notes Europe, 36(1), 9-14. https://doi.org/10.11128/sne.36.tn.10762

- **Decision:** supporting — LLM multi-agent simulation-model generator compared against a manual approach and the authors' prior system with the harness uncontrolled.
- **Evidence:** full text not read (status: pending).

### Jaber, J., & Jaber, O. (2026). AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis. arXiv preprint. https://doi.org/10.48550/arxiv.2606.09682

- **Decision:** supporting [preprint] — Agent harness whose static schedule validator gates agent-proposed actions is measured on adversarial schedules, though the study targets kernel synthesis.
- **Evidence:** full text not read (status: pending).

### Chilkuri, V. C. S. S. (2026). Autonomous Evaluation Architectures: Multi-Agent LLM Pipelines, Browser-Grounded Testing: Programmatic Alignment via DSPy, and Adversarial Robustness in Production Orchestration Systems. Computer Fraud and Security, 1268-1279. https://doi.org/10.52710/cfs.1067

- **Decision:** supporting — Closed-loop evaluation architecture arguing per-agent benchmarks miss cross-stage multi-agent failures; an evaluation method for agent pipelines.
- **Evidence:** full text not read (status: pending).

### Arora, K., Naim, A., & Sharma, S. (2026). Benchmarking Multi-Agent LLM and Single Agent LLM Efficiency for Contextual Text Generation. 2026 International Conference on Intelligent Systems in Engineering, Secured Systems and Cybersecurity (ICISESSC), 741-745. https://doi.org/10.1109/icisessc68634.2026.11542788

- **Decision:** supporting — Compares multi-agent against single-agent generation on one model, but the arms differ in scaffold entirely, so the harness is left uncontrolled - RQ2 evidence.
- **Evidence:** full text not read (status: pending).

### Maiti, S. (2026). Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare. arXiv preprint. https://doi.org/10.48550/arxiv.2603.17419

- **Decision:** supporting [preprint] — Ninety-day production report on isolation, credential proxying, egress control and a prompt-integrity envelope framework for nine LLM agents.
- **Evidence:** full text not read (status: pending).

### Hossain, S. M. A., Shayoni, R. K., & Morol, M. K. (2026). CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2609.02265

- **Decision:** supporting [preprint] — Memory belief-tracking method evaluated against an identically supervised baseline; the measured outcome is poisoning resistance, not task attribution.
- **Evidence:** full text not read (status: pending).

### Wang, Z., Yuan, H., Dong, W., Cong, G., & Li, F. (2026). CARROT: A Learned Cost-Constrained Retrieval Optimization System for RAG. https://doi.org/10.1109/icde65706.2026.00162

- **Decision:** supporting — Retrieval optimization study showing chunk utility is non-monotonic and order-dependent, a limitation directly relevant to context assembly.
- **Evidence:** full text not read (status: pending).

### Srivastava, R. (2026). CFAgentBench: A Reproducible Environment and Benchmark for Autonomous Construction-Finance Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2606.22000

- **Decision:** supporting [preprint] — Self-hostable executable environment and benchmark for finance agents graded by state diffs, contributing reproducible evaluation infrastructure.
- **Evidence:** full text not read (status: pending).

### Fan, E., Hu, K., Wu, Z., Ge, J., Miao, J., Zhang, Y., Sun, H., Wang, W., & Zhang, T. (2026). ChatCFD: A Large Language Model‐Driven Agent for End‐to‐End Computational Fluid Dynamics Automation with Structured Knowledge and Reasoning. Advanced Intelligent Discovery, 2(3). https://doi.org/10.1002/aidi.202500174

- **Decision:** supporting — Domain CFD agent whose ablations quantify the contribution of the knowledge base and error-locator modules, giving component-level effects with the model held fixed.
- **Evidence:** full text not read (status: pending).

### Ge, Z., Li, H., Wang, Y., Hu, N., Zhang, C., & Li, Q. (2026). ClinicalAgents: Multi-Agent Orchestration for Clinical Decision Making with Dual-Memory. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2603.26182

- **Decision:** supporting [preprint] — MCTS-orchestrated clinical multi-agent framework with dual memory and experiments; harness control not stated.
- **Evidence:** full text not read (status: pending).

### Fernandez, M. P. (2026). Closing the Execution Gap in LLM Agent Systems Empirical Evidence for Compliant Drift, Partial Observability, and Integrated Runtime. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.19929771

- **Decision:** supporting [preprint] — Empirical experiments instrumented into a LangGraph agent that isolate trajectory-level governance failures decision-boundary checks miss.
- **Evidence:** full text not read (status: pending).

### Storf, S., Barton-Cooper, R., Peters-Gill, J., & Hobbhahn, M. (2026). Constitutional Black-Box Monitoring for Scheming in LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2603.00829

- **Decision:** supporting [preprint] — Finds simple prompt sweeps match extensive prompt optimisation for scheming monitors and that synthetic-data selection transfers; a useful negative prompt-sensitivity result.
- **Evidence:** full text not read (status: pending).

### Divi, V. R., Gullapalli, S., & Brahmandam, B. A. (2026). Containing the Cascade: A Benchmark and Reference Mediator for Failure Propagation in Tool-Using LLM Multi-Agent Systems. 2026 5th International Conference on Electronics Representation and Algorithm (ICERA), 604-609. https://doi.org/10.1109/icera72709.2026.11666599

- **Decision:** supporting — Fault-injection testbed and containment metrics for cascading failures in tool-using LLM multi-agent systems.
- **Evidence:** full text not read (status: pending).

### Sharma, A. (2026). Contamination Percolation in Multi-Agent LLM Systems: A Measurement Framework and Benchmark. IEEE Access, 14, 127686-127706. https://doi.org/10.1109/access.2026.3717722

- **Decision:** supporting — Benchmark, diagnostic metric, and statistically controlled measurement pipeline for misinformation spread across five model families.
- **Evidence:** full text not read (status: pending).

### Mouzouni, C. (2026). Context Kubernetes: Declarative Orchestration of Enterprise Knowledge for Agentic AI Systems. arXiv preprint. http://arxiv.org/abs/2604.11623v3

- **Decision:** supporting [preprint] — Compares four escalating governance configurations for agent knowledge access, isolating what each context-orchestration layer contributes.
- **Evidence:** full text not read (status: pending).

### Raja, K. A. (2026). Continuous Evaluation &amp; Observability for Enterprise AI Agents: A Unified Framework for LLM and ML Systems. International Journal of Computational and Experimental Science and Engineering, 12(1). https://doi.org/10.22399/ijcesen.4959

- **Decision:** supporting — Proposes a continuous evaluation and observability framework for enterprise agents; contributes evaluation methodology without isolating harness effects.
- **Evidence:** full text not read (status: pending).

### Systems, N. A.  I. (2026). CRUCIBLE as an Integrity Catalyst for Multi-Agent Safety Evaluation: Gate-Transfer Methodology, Prospective Protocol Scaffold & Exploratory Results. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21421242

- **Decision:** supporting — Transfers software test-integrity gates to LLM-judge auditing with a controlled A/B over three repositories; an exploratory evaluation-integrity method.
- **Evidence:** full text not read (status: pending).

### Wu, J., Gong, M., Cheng, F., & Zhao, Q. (2026). EcoAgent-Bench: Evaluating Economic Decision-Making in Budget-Constrained LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2608.05519

- **Decision:** supporting [preprint] — Budget-aware agent benchmark exposing a metric artefact and evaluating agents under tool-API and workspace-CLI settings with frozen environments.
- **Evidence:** full text not read (status: pending).

### Hatamian, E. (2026). Econometric Foundations for Multi-Agent Negotiation Systems: A Theoretical Framework for LLM-Driven Strategic Advisor Evaluation. Business &amp; Management Compass, 70(1), 22-40. https://doi.org/10.56065/w2xbtf92

- **Decision:** supporting — Econometric evaluation framework adapting RCT, IV, RDD, and DiD designs and 24 metrics to LLM multi-agent negotiation systems.
- **Evidence:** full text not read (status: pending).

### Shukla, A., & Rajput, P. (2026). Emergent Autonomous Sub-Agent Spawning in LLM-Based Multi-Agent Software Engineering Systems:An Empirical Case Study, Controlled Pilot Experiment, and Benchmark Framework"Can AI Agents Have Babies?". International Journal of Research and Scientific Innovation, 13(3), 208-219. https://doi.org/10.51244/ijrsi.2026.1303000020

- **Decision:** supporting — Controlled pilot showing sub-agent spawning depends on shell access and task load; a tooling manipulation with significance testing, but the outcome is behaviour not performance.
- **Evidence:** full text not read (status: pending).

### Kumar, A., Saha, S., & Gembali, M. (2026). Engineering Agentic AI Systems: A Protocol-Aware Reference Architecture for Orchestration, Retrieval, Governance, Evaluation, and Production Rollout. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21897018

- **Decision:** supporting — Protocol-aware reference architecture organizing orchestration, governance, evaluation, and rollout responsibilities for agentic systems.
- **Evidence:** full text not read (status: pending).

### Khaki, A. M. Z., & Choi, A. (2026). Evaluating Fairness in LLM Negotiator Agents via Economic Games Using Multi-Agent Systems. Mathematics, 14(3), 458-458. https://doi.org/10.3390/math14030458

- **Decision:** supporting — Economic-game study of LLM negotiator agents that varies prompt conditioning and counterpart awareness and reports the effect on outcomes.
- **Evidence:** full text not read (status: pending).

### Shlomov, S., Oved, A., Marreed, S., Levy, I., Akrabi, O., Yaeli, A., Strąk, Ł., Koumpan, E., Goldshtein, Y., Shapira, E., Mashkif, N., & Adi, A. (2026). From Benchmarks to Business Impact: Deploying IBM Generalist Agent in Enterprise Production. Proceedings of the AAAI Conference on Artificial Intelligence, 40(47), 40423-40431. https://doi.org/10.1609/aaai.v40i47.41485

- **Decision:** supporting — Generalist agent reporting benchmark results and an enterprise pilot while noting the absence of standardized agent evaluation practice.
- **Evidence:** full text not read (status: pending).

### From Language Models to Agentic AI: A Survey of Autonomous, Action-Enabled, and Collaborative LLM Agents. (2026). https://link.springer.com/article/10.1007/s12559-026-10619-1

- **Decision:** supporting — Taxonomy-driven survey of agentic AI that reviews evaluation methodologies and documents why ad hoc architectures make agent systems hard to compare.
- **Evidence:** full text not read (status: pending).

### Ferrag, M. A., Tihanyi, N., & Debbah, M. (2026). From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review. IEEE Access, 14, 84237-84285. https://doi.org/10.1109/access.2026.3698694

- **Decision:** supporting — Review comparing roughly 60 agent and LLM benchmarks and agent frameworks side by side.
- **Evidence:** full text not read (status: pending).

### Siddiqui, M. M. F. L. (2026). From Prompt Engineering to Loop Engineering: A Five-Layer Taxonomy for Evaluating AI Systems Engineering Practice. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.22098121

- **Decision:** supporting — Taxonomy separating prompt, context, harness, agent and loop engineering with per-layer metrics; explicitly a case study, not a controlled experiment.
- **Evidence:** full text not read (status: pending).

### Balasubramanian, A. (2026). From Signals to Root Cause: A Systems Architecture for Agentic AI in Observability. International Journal of Intelligent Systems and Applications in Engineering. https://doi.org/10.5281/zenodo.20583512

- **Decision:** supporting — Layered observability agent evaluated on 1,200 tasks against prompt-only and static pipeline baselines, reporting success, recovery, and token effects of the architecture.
- **Evidence:** full text not read (status: pending).

### BESLEAGA, A. N. (2026). GABBE: A Neurocognitive Swarm Architecture for Agentic AI Software Engineering. https://doi.org/10.36227/techrxiv.177220787.72010996/v1

- **Decision:** supporting [preprint] — Claims architectural superiority over flat-topology orchestrators from a comparative analysis with no stated control of models, prompts, or tooling - RQ2 evidence.
- **Evidence:** full text not read (status: pending).

### Das, D., Nigam, L., Bahadur, S. K. J., & Dhar, G. (2026). Genflow Ad Studio: A Compound AI Architecture for Brand-Aligned, Self-Correcting Video Generation. arXiv preprint, 1193-1198. https://doi.org/10.1145/3786335.3813213

- **Decision:** supporting [preprint] — Replaces single-pass generation with an adversarial evaluator-agent critique loop and reports yield gains, but the loop is not isolated from other changes.
- **Evidence:** full text not read (status: pending).

### Sylvestre, J. (2026). Gold Label Errors in the SciFact Benchmark: An LLM-Assisted Annotation Audit. BioNLP 2026, 97-103. https://doi.org/10.18653/v1/2026.bionlp-1.9

- **Decision:** supporting — Annotation audit showing benchmark gold-label errors shift macro-F1 by margins comparable to inter-system gaps, a benchmark-validity result.
- **Evidence:** full text not read (status: pending).

### Karuppuchamy, S. (2026). Governed Agentic AI for Software Platforms: A Reference Architecture for Safe Autonomy at Scale. SoutheastCon 2026, 1-6. https://doi.org/10.1109/southeastcon63549.2026.11475963

- **Decision:** supporting — Governance control plane whose prototype measurements characterise autonomy, policy enforcement, and oversight trade-offs; harness-adjacent evidence on safety controls.
- **Evidence:** full text not read (status: pending).

### Fu, J., Wang, Z., Lu, P., & Tong, K. (2026). GraphRCA-Chorus: Choreographed Multi-Agent Graph Transformers for Root Cause Analysis in Microservices. 2026 International Conference on Embedded Systems, Mobile Communication and Computing (EMC²), 186-192. https://doi.org/10.36227/techrxiv.177162133.31720831/v1

- **Decision:** supporting [preprint] — Decentralised multi-agent root cause analysis framework compared with baselines without reporting how the surrounding harness was held constant.
- **Evidence:** full text not read (status: pending).

### Lima, J. C. S., Correia, L. H. A., Salgado, A. D. L., & Souza, M. R. D. A. (2026). GTAA-LM: Artifact and Experimental Data - SBCARS 2026. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21860724

- **Decision:** supporting — Reproducible artifact for a governed LLM-agent microservice architecture with controlled tools, observability and failure injection, but no harness contrast.
- **Evidence:** full text not read (status: pending).

### Panavas, L., Minus, S., Monton, B., Ray, D., Garre, S., Mehta, S., & Chen, E. (2026). HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following. arXiv preprint. https://doi.org/10.48550/arxiv.2607.25398

- **Decision:** supporting [preprint] — Deterministic agentic benchmark testing whether long policy documents in context constrain tool-use behaviour, with programmatic rubric grading.
- **Evidence:** full text not read (status: pending).

### Wang, R., Shi, Y., Li, Z., Li, Z., Yu, Y., Yang, J., Panaganti, K., Mi, H., Zhou, D., & Leoweiliang (2026). Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable. arXiv preprint. http://arxiv.org/abs/2607.13285v1

- **Decision:** supporting [preprint] — Behavior-centric representation for locating and editing harness code, addressing harness evolution rather than harness effects on performance.
- **Evidence:** full text not read (status: pending).

### Zhang, L., Jia, T., Zhai, Y., Pan, L., Duan, C., He, M., Xiao, P., & Li, Y. (2026). Hypothesize-Then-Verify: Speculative Root Cause Analysis for Microservices with Pathwise Parallelism. https://doi.org/10.1145/3786582.3786803

- **Decision:** supporting — Speculative hypothesise-then-verify control loop for root cause analysis compared with existing LLM approaches for accuracy and efficiency without harness control.
- **Evidence:** full text not read (status: pending).

### Du, C., Vosseler, A., Mazza, F., & Borrmann, A. (2026). IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM Information Retrieval. arXiv preprint. https://doi.org/10.48550/arxiv.2607.26072

- **Decision:** supporting [preprint] — Benchmark that decomposes long-term memory performance into ingestion, retrieval, and utilization for BIM agents; a measurement method rather than harness attribution.
- **Evidence:** full text not read (status: pending).

### Tam, Z. R., Lin, C.-Y., Chen, Y.-N., Sun, S.-H., & Lee, H.-Y. (2026). Joint Optimization of Tool Creation and Use for Large Language Model Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2608.24571

- **Decision:** supporting [preprint] — Jointly trains tool creation and use with separate schema, code and outcome reward axes; a tool-schema method with baseline comparison, not a harness-control study.
- **Evidence:** full text not read (status: pending).

### Liu, Z., Zhao, W., Yuan, X., Ma, N., Huang, Y., & Jiang, M. (2026). Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives. arXiv preprint. https://doi.org/10.48550/arxiv.2608.26372

- **Decision:** supporting [preprint] — Knowledge-verified deception benchmark applied across eighteen models; a measurement-validity contribution rather than a harness manipulation.
- **Evidence:** full text not read (status: pending).

### Ilves, M., Barbu, E., & Übi, J. (2026). Large Language Models for Knowledge Graph Extraction: A Schema-Constrained Evaluation Framework. Proceedings of the Language Resources and Evaluation Conference, 221-228. https://doi.org/10.63317/3icoxh7axwxy

- **Decision:** supporting — Schema-constrained extraction framework with controlled inference settings, repeated-run stability analysis and evidence that automatic triple F1 understates quality.
- **Evidence:** full text not read (status: pending).

### Mo, G., Zhong, W., Chen, J., Yuan, Q., Chen, X., Lu, Y., Lin, H., He, B.-H., Han, X., & Sun, L. (2026). LiveMCPBench: Can Agents Navigate an Ocean of MCP Tools?. https://doi.org/10.1145/3770855.3817478

- **Decision:** supporting — MCP benchmark with a ready-to-deploy 70-server tool suite and LLM-as-judge grading that attributes nearly half of failures to tool retrieval.
- **Evidence:** full text not read (status: pending).

### Demirhan, H., & Zadrozny, W. (2026). LLM-Based Control for Simulated Physical Reasoning: Modular Evaluation in the NeurIPS Embodied Agent Interface Challenge. AI, 7(4), 131. https://doi.org/10.3390/ai7040131

- **Decision:** supporting — Staged benchmark submission that separates planning quality from interface reliability and uses schema-constrained regeneration, without varying those settings experimentally.
- **Evidence:** full text not read (status: pending).

### Patel, T. P., Bayyavarapu, S. R. K. V., Soni, V., Purushothaman, R., Thokala, G. B., & Ranganathan, V. (2026). LLMDebug: Prompt-Engineered Large Language Models for Automated Root Cause Analysis in Microservices Architectures. 2026 International Conference on Advances in Artificial Intelligence and Machine Learning (AAIML), 373-380. https://doi.org/10.1109/aaiml67890.2026.11498111

- **Decision:** supporting — Multi-stage prompting framework for microservice root cause analysis with ablations reporting the contribution of each prompting strategy and a reproducibility release.
- **Evidence:** full text not read (status: pending).

### M.A.K.S: Multidimensional Access Knowledge Scoring for Long-Horizon LLM Agent Memory Management. (2026). Iconic Research and Engineering Journals, 9(11). https://doi.org/10.64388/irev9i11-1718160

- **Decision:** supporting — Proposes an LLM-agent memory eviction/revival mechanism with ablation and overhead benchmarking against FIFO/LRU baselines; component effect but not an attribution study.
- **Evidence:** full text not read (status: pending).

### Kim, E., Gu, C., Tiwari, V., & Kolter, J. Z. (2026). Measuring Five-Nines Reliability: Sample-Efficient LLM Evaluation in Saturated Benchmarks. arXiv preprint. https://doi.org/10.48550/arxiv.2605.11209

- **Decision:** supporting [preprint] — Sample-efficient estimator for rare LLM failure rates under limited compute; a statistical method for reliability measurement.
- **Evidence:** full text not read (status: pending).

### Lacasse, S., Hatier, J., & Baker, A. (2026). Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture. arXiv preprint. http://arxiv.org/abs/2607.04391v1

- **Decision:** supporting [preprint] — Model-agnostic, auditable agentic memory architecture with symbolic reproducible retrieval, evaluated over a year-long production deployment.
- **Evidence:** full text not read (status: pending).

### Wang, Y., Xia, C., Zhao, W., Du, J., Miao, C., Deng, Z., Yu, P. S., & Xing, C. (2026). MultiFileTest: A Multi-File-Level LLM Unit Test Generation Benchmark and Impact of Error Fixing Mechanisms. https://doi.org/10.18653/v1/2026.findings-acl.1403

- **Decision:** supporting — Multi-file unit-test benchmark that additionally measures frontier LLMs under manual and self error-fixing, an explicit repair-loop ablation.
- **Evidence:** full text not read (status: pending).

### Seyedghorban, Z., Klimov, E., van Deursen, A., Panichella, A., & Ozkan, B. K. (2026). Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering. 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST), 211-215. https://doi.org/10.1109/icst69053.2026.00037

- **Decision:** supporting — Tracing and fault-injection tooling that makes baseline-versus-faulty agent executions reproducibly comparable; a method contribution validated only on a demo workflow.
- **Evidence:** full text not read (status: pending).

### Hu, J., Li, T., Yu, L., & Han, A. (2026). OxyGent: Making Multi-Agent Systems Modular, Observable, and Evolvable via Oxy Abstraction. Underline Science Inc.. https://doi.org/10.48448/0tzn-dg98

- **Decision:** supporting — Modular multi-agent framework with pluggable agent, tool and LLM components plus runtime execution-graph observability; combinable harness solution.
- **Evidence:** full text not read (status: pending).

### Yuan, C., Wei, T., Li, C., Yi, X., Liu, S., Zhang, Z., Cai, Y., & Du, X. (2026). PaperOrchestrator: An LLM-Orchestrated multi-agent pipeline for automated end-to-end scientific paper writing. Journal of King Saud University - Computer and Information Sciences, 38(5). https://doi.org/10.1007/s44443-026-00708-4

- **Decision:** supporting — Multi-agent paper-writing pipeline compared against 11 baseline systems with no statement of how the harness was held constant.
- **Evidence:** full text not read (status: pending).

### Liu, X., Sadikoglu, E., Chatterjee, R., & Senanayake, R. (2026). Physical Agentic AI: An Architecture for Orchestrating a Robot Crew with LLMs. arXiv preprint. https://doi.org/10.48550/arxiv.2608.22657

- **Decision:** supporting [preprint] — Typed skill library and deterministic orchestrator define the tool schema and control loop for robot agents, but no configuration comparison is reported.
- **Evidence:** full text not read (status: pending).

### Moslemi, Z., Koneru, K., Lee, Y.-T., Kumar, S., & Radhakrishnan, R. (2026). POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation. arXiv preprint. https://doi.org/10.48550/arxiv.2601.11816

- **Decision:** supporting [preprint] — Typed plan DAGs, validator gates and a bounded repair loop are evaluated end to end, but their individual contributions are not isolated.
- **Evidence:** full text not read (status: pending).

### Trashchenkov, S. (2026). Power Systems Agent Benchmark: Executable Evaluation of AI Agents in Electric Power Engineering. arXiv preprint. https://doi.org/10.48550/arxiv.2606.20950

- **Decision:** supporting [preprint] — Executable benchmark with a deterministic evaluator for power-engineering agents; contributes measurement validity but varies no harness component.
- **Evidence:** full text not read (status: pending).

### Cui, S., Krishna, R., Jha, S., & Iyer, R. K. (2026). Praxis: Integrating Program Analysis with Observability for Root-Cause Analysis. https://doi.org/10.1109/dsn69566.2026.00021

- **Decision:** supporting — New RCA orchestrator reporting large accuracy and token gains over ReAct baselines; a scaffold comparison where harness control is not stated.
- **Evidence:** full text not read (status: pending).

### Jayanth, N., & Grunwald, A. (2026). PROBE: An Executable Physics-Validation Benchmark for LLM-Generated Process Model Code. ChemRxiv. https://doi.org/10.26434/chemrxiv.15007535/v1

- **Decision:** supporting [preprint] — Executable physics-validation benchmark replacing lenient LLM judges with reproducible scoring, contributing measurement validity for generated code.
- **Evidence:** full text not read (status: pending).

### Li, S., Abdelmoniem, A. M., & Wang, S. (2026). ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs. arXiv preprint. https://doi.org/10.48550/arxiv.2608.25992

- **Decision:** supporting [preprint] — Progress-guided router selecting LLM agents across workflow steps under cost budgets; a configuration comparison without harness control.
- **Evidence:** full text not read (status: pending).

### Munirathinam, T. (2026). PurgeBench: A Benchmark and Metric for Adversarial Memory-Poison Recovery in LLM Agents. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21379140

- **Decision:** supporting [preprint] — Benchmark and composite metric for memory-poison recovery that scores seven recovery procedures over a fixed memory substrate.
- **Evidence:** full text not read (status: pending).

### 2026, A. F. A. I., Cai, Z., Gao, Y., & Yang, B. (2026). RCAFlow: A Workflow-Informed Hierarchical Planning Multi-Agent System for Root Cause Analysis. Proceedings of the AAAI Conference on Artificial Intelligence, 40(1), 300-308. https://doi.org/10.1609/aaai.v40i1.36991

- **Decision:** supporting — Workflow-informed hierarchical multi-agent root cause analysis with module-level ablations on OpenRCA benchmarks; ablation evidence inside a system paper.
- **Evidence:** full text not read (status: pending).

### Tang, Y., Cetin, E., Xu, J., Sun, Q., Nielsen, S., Richard, V., Goda, H., Tymchenko, I., Nguyen, N., Lee, H., Ashiga, M., Kotyan, S., Kuroki, S., & Clanuwat, T. (2026). Sakana Fugu Technical Report. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2606.21228

- **Decision:** supporting [preprint] — Orchestrator models that generate adaptive agentic scaffolds and claim benchmark wins over other systems without controlling the compared harnesses.
- **Evidence:** full text not read (status: pending).

### Ozpinar, A., & Ozpinar, S. B. (2026). SAPIENT: A Multi-Agent Framework for Corporate Reputation Intelligence Through Sentinel Monitoring and LLM-Based Synthetic Population Simulation. Systems, 14(4), 425. https://doi.org/10.3390/systems14040425

- **Decision:** supporting — Multi-condition simulation study reporting prompt-paraphrase sensitivity and cross-backend consistency with repeated runs and variance, though its agents are synthetic personas.
- **Evidence:** full text not read (status: pending).

### Radanliev, P., Maple, C., Santos, O., & Atefi, K. (2026). SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility Evaluation. arXiv preprint, 7(2), 1-35. https://doi.org/10.1145/3798285

- **Decision:** supporting [preprint] — Multi-agent provenance framework with a reproducibility evaluation and ablations showing each agent's distinct contribution.
- **Evidence:** full text not read (status: pending).

### Zhang, Z., Zheng, H., & Xu, Y. (2026). SEAR: Schema-Based Evaluation and Routing for LLM Gateways. Proceedings of the ACM Conference on AI and Agentic Systems, 1084-1099. https://doi.org/10.1145/3786335.3813131

- **Decision:** supporting — Schema-based evaluation and routing layer producing structured quality, latency and cost signals over production LLM gateway sessions.
- **Evidence:** full text not read (status: pending).

### Louck, Y. (2026). Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees. arXiv preprint. http://arxiv.org/abs/2606.24322v1

- **Decision:** supporting [preprint] — Formal defense of agent long-term memory against poisoning; a memory-component reliability result rather than a performance-attribution study.
- **Evidence:** full text not read (status: pending).

### Arceo, F. J., & Narsing, V. P. (2026). Securing the Agent: Vendor-Neutral, Multitenant Enterprise Retrieval and Tool Use. arXiv preprint, 862-872. https://doi.org/10.1145/3786335.3813145

- **Decision:** supporting [preprint] — Server-side agentic orchestration and authorization layer, empirically evaluated for leakage elimination and overhead in a multitenant deployment.
- **Evidence:** full text not read (status: pending).

### Ding, Y., Twabi, A., Yu, J., Zhang, L., Kondo, T., & Satō, H. (2026). SEMA: Self-Evolving Multi-Agent Auditing for Smart Contracts. Electronics, 15(10), 2187-2187. https://doi.org/10.3390/electronics15102187

- **Decision:** supporting — Multi-agent auditing framework with replay-certified reporting and ablations that disable knowledge evolution and cross-agent artefact reuse under a fixed budget.
- **Evidence:** full text not read (status: pending).

### LI, X. (2026). Semantic Camouflage in Artificial Organizations: A Real-LLM Multi-Agent Simulation of Information Distortion and Audit. https://doi.org/10.21203/rs.3.rs-9875459/v1

- **Decision:** supporting [preprint] — Simulation of role-based LLM agent teams comparing organisational structures and goal misalignment; a topology comparison with no stated harness control (RQ2 evidence).
- **Evidence:** full text not read (status: pending).

### Harada, Y. (2026). Simulating Lay Health-Seeking Behavior with LLM Personas and Illness Vignettes: Reproducibility, Prompt Sensitivity, and Slice Dependence. Qeios. https://doi.org/10.32388/be0zbc

- **Decision:** supporting [preprint] — Quantifies prompt sensitivity, run-to-run variance and slice dependence, and shows within-batch paired designs understate prompt effects.
- **Evidence:** full text not read (status: pending).

### Tang, D., Jiang, Q., Yang, J., Zhao, J., Du, X., Miao, F., & Zhang, X. (2026). SLTP: A Symbolic Travel-Planning Agent Framework with Decoupled Translation and Heuristic Tree Search. Electronics, 15(2), 422-422. https://doi.org/10.3390/electronics15020422

- **Decision:** supporting — Reports an 8B agent with symbolic scaffolding matching or beating GPT-4o and DeepSeek-V3 backed methods, a scaffold-versus-model claim from an uncontrolled comparison.
- **Evidence:** full text not read (status: pending).

### Ouaarous, R., Hilal, I., & Mezrioui, A. (2026). Software quality assurance in the era of Agentic AI: a systematic mapping study. Frontiers in Computer Science, 8. https://doi.org/10.3389/fcomp.2026.1936730

- **Decision:** supporting — Systematic mapping of 37 agentic AI studies in software quality assurance, classifying architectures and autonomy and naming transparency and validation as gaps.
- **Evidence:** full text not read (status: pending).

### Jiang, Y., Li, D., Deng, H., Ma, B., Wang, X., Wang, Q., & Yu, G. (2026). SoK: Agentic Skills--Beyond Tool Use in LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2602.20867

- **Decision:** supporting [preprint] — Systematisation of the agentic skill layer (tool schema, execution policy, termination) surveying deterministic evaluation and evidence that curated versus self-generated skills shift success rates.
- **Evidence:** full text not read (status: pending).

### Engelberg, G., Koutsyi, K., Goldberg, L., Elezra, R., Pinto, I., Moalem, T., Cohen, S., & Weintrob, Y. (2026). Sola-Visibility-ISPM: Benchmarking Agentic AI for Identity Security Posture Management Visibility. arXiv preprint. http://arxiv.org/abs/2601.07880v1

- **Decision:** supporting [preprint] — Benchmark for agentic AI on identity posture visibility tasks in a live environment, contributing measurement apparatus rather than harness attribution.
- **Evidence:** full text not read (status: pending).

### MM, L. (2026). Standardized Context Sensitivity Benchmark Across 25 LLM-Domain Configurations. Preprints.org. https://doi.org/10.20944/preprints202602.1114.v2

- **Decision:** supporting [preprint] — Standardised three-condition protocol quantifies context sensitivity across 25 model-domain runs, offering a method for measuring prompt and context effects.
- **Evidence:** full text not read (status: pending).

### Reinicke, N., & Fitzgerald, R. (2026). TETA Autoresearch [SWR-26-089]. OSTI OAI (U.S. Department of Energy Office of Scientific and Technical Information). https://doi.org/10.11578/dc.20260813.1

- **Decision:** supporting — Autoresearch template in which an LLM-agent mode and an optimizer mode share one harness, supplying apparatus for controlled comparison but no results.
- **Evidence:** full text not read (status: pending).

### Cacioli, J.-P. (2026). The Metacognitive Monitoring Battery: A Cross-Domain Benchmark for LLM Self-Monitoring. arXiv preprint. https://doi.org/10.48550/arxiv.2604.15702

- **Decision:** supporting [preprint] — Pre-registered psychometric battery measuring LLM self-monitoring across 20 models, contributing metrics relevant to reflection and self-validation policies.
- **Evidence:** full text not read (status: pending).

### Yu, S., Liang, J., & Hu, H. (2026). ToC: Tree-of-Claims Search with Multi-Agent Language Models. Proceedings of the AAAI Conference on Artificial Intelligence, 40(41), 34495-34502. https://doi.org/10.1609/aaai.v40i41.40748

- **Decision:** supporting — Multi-agent tree-search claim editor compared against plain LLM prompting with ablations; an agent-configuration comparison whose surrounding harness is uncontrolled.
- **Evidence:** full text not read (status: pending).

### Qi, J., Zhang, W., Ng, S. M., Xu, F., Chen, Y., Li, Y., & King, I. (2026). TREK: A Travel Reasoning and Evaluation Kit for LLM Agents in Complex Trip Planning. arXiv preprint. https://doi.org/10.48550/arxiv.2607.26977

- **Decision:** supporting [preprint] — Benchmark with a deterministic rule-based evaluator and an achievable gold ceiling so residual gaps attach to the agent rather than to scorer strictness.
- **Evidence:** full text not read (status: pending).

### Jahnavi Somaraju, K. R. K. J. B. M. S. Y. S. (2026). TruthLens: Real-Time Evidence Verification and AI Hallucination Detection for Large Language Models via a Multi-Agent Architecture. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.21523001

- **Decision:** supporting — Compares a five-agent verification pipeline against single-agent RAG and a static baseline with an ablation isolating which agents drive the hallucination reduction.
- **Evidence:** full text not read (status: pending).

### Haresh, P. (2026). Turning Enterprise Policies into Autonomous Execution: A Reference Architecture and Evaluation Protocol for Agentic AI in End-to-End Healthcare Claims Audit (Preprint). https://doi.org/10.2196/preprints.103914

- **Decision:** supporting [preprint] — Reference architecture plus a prospective evaluation protocol with datasets, baselines and metrics for agentic claims audit; no empirical results reported.
- **Evidence:** full text not read (status: pending).

### Teoh, X., Lin, Y., Nguyen, D.-M., Ren, R., Zhang, W., & Dong, J. S. (2026). WebTestPilot: Agentic End-to-End Web Testing against Natural Language Specification by Inferring Oracles with Symbolized GUI Elements. Proceedings of the ACM on software engineering., 3(FSE), 1933-1956. https://doi.org/10.1145/3797115

- **Decision:** supporting — Neurosymbolic GUI-testing agent whose symbolization constrains oracle reasoning, evaluated on a new bug-injected benchmark against baselines without stating harness control.
- **Evidence:** full text not read (status: pending).

### Westover, J. H. (2026). When Algorithms Meet Ethics: Systematic Evidence of Framing Effects in LLM Organizational Decision-Making. Preprints.org. https://doi.org/10.20944/preprints202602.1103.v1

- **Decision:** supporting [preprint] — Preregistered factorial experiment over 14,306 responses quantifying how six framing dimensions shift recommendations across three frontier models.
- **Evidence:** full text not read (status: pending).

### Yang, X., He, Y., Ji, S., Hooi, B., & Dong, J. S. (2026). Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections. arXiv preprint. https://doi.org/10.48550/arxiv.2602.15654

- **Decision:** supporting [preprint] — Memory-poisoning attack persisting across sessions with mechanism-specific strategies for sliding-window and retrieval-augmented memory.
- **Evidence:** full text not read (status: pending).

### Mohapatra, B., Walia, B., & Dash, S. (2025). A Modular Multi-Agent Framework for Clinical Documentation and Hospital Operations. https://doi.org/10.1109/acai68217.2025.11406271

- **Decision:** supporting — Multi-agent clinical documentation reporting significance-tested gains from agentic orchestration over a non-orchestrated baseline, with the harness uncontrolled.
- **Evidence:** full text not read (status: pending).

### Li, G., Wu, R., & Tan, H. (2025). A Plan Reuse Mechanism for LLM-Driven Agent. arXiv preprint. https://doi.org/10.48550/arxiv.2512.21309

- **Decision:** supporting [preprint] — Plan-reuse caching in the agent control loop cuts latency by 93%, a harness-level change measured only for cost rather than task accuracy.
- **Evidence:** full text not read (status: pending).

### Yang, Y., Chai, H., Song, Y., Qi, S., Wen, M., Li, N., Liao, J., Hu, H., Lin, J., Chang, G., Liu, W., Wen, Y., Yu, Y., & Zhang, W. (2025). A Survey of AI Agent Protocols. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2504.16736

- **Decision:** supporting [preprint] — Survey and comparative analysis of context-oriented and inter-agent protocols, which define the tool interface layer of the harness.
- **Evidence:** full text not read (status: pending).

### Zhang, L., Jia, T., Jia, M., Wu, Y., Liu, A., Yang, Y., Wu, Z., Hu, X., Yu, P. S., & Li, Y. (2025). A Survey of AIOps in the Era of Large Language Models. ACM Computing Surveys, 58(2), 1-35. https://doi.org/10.1145/3746635

- **Decision:** supporting — Survey of LLM-based AIOps whose fourth research question reviews evaluation methodologies for LLM-integrated approaches, usable as evaluation-method evidence.
- **Evidence:** full text not read (status: pending).

### Ray, P. P. (2025). A Survey on Model Context Protocol: Architecture, State-of-the-art, Challenges and Future Directions. https://doi.org/10.36227/techrxiv.174495492.22752319/v1

- **Decision:** supporting [preprint] — Survey that dissects and benchmarks MCP implementations, covering the tool-invocation interface and its latency and security overheads.
- **Evidence:** full text not read (status: pending).

### Zhang, Z., Dai, Q., Bo, X., Ma, C., Li, R., Chen, X., Zhu, J., Dong, Z., & Wen, J.-R. (2025). A Survey on the Memory Mechanism of Large Language Model-based Agents. ACM Transactions on Information Systems, 43(6), 1-47. https://doi.org/10.1145/3748302

- **Decision:** supporting — Survey of how memory modules in LLM-based agents are designed and evaluated; method-level contribution on one preregistered harness component.
- **Evidence:** full text not read (status: pending).

### Brown, A., Roman, M., & Devereux, B. (2025). A Systematic Literature Review of Retrieval-Augmented Generation: Techniques, Metrics, and Challenges. Big Data and Cognitive Computing, 9(12), 320-320. https://doi.org/10.3390/bdcc9120320

- **Decision:** supporting — PRISMA systematic review synthesising RAG effectiveness and mapping evaluation practices and metric inconsistency across studies.
- **Evidence:** full text not read (status: pending).

### Kang, M., Chen, W., Han, D., Inan, H. A., Wutschitz, L., Chen, Y., Sim, R. B., & Rajmohan, S. (2025). ACON: Optimizing Context Compression for Long-horizon LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2510.00615

- **Decision:** supporting [preprint] — Varies the context/memory compression component and reports success and token effects, usable as an ablation-style result rather than a harness-attribution study.
- **Evidence:** full text not read (status: pending).

### Chen, J., & Cong, S. L. (2025). AgentGuard: Repurposing Agentic Orchestrator for Safety Evaluation of Tool Orchestration. arXiv preprint. https://doi.org/10.48550/arxiv.2502.09809

- **Decision:** supporting [preprint] — Uses the agent orchestrator itself to discover unsafe tool-use workflows and generate constraints, an evaluation method for tool orchestration.
- **Evidence:** full text not read (status: pending).

### Roumeliotis, K. I., Sapkota, R., Karkee, M., & Tselikas, N. D. (2025). Agentic AI with Orchestrator-Agent Trust: A Modular Visual Classification Framework with Trust-Aware Orchestration and RAG-Based Reasoning. arXiv preprint, 14, 26965-26982. https://doi.org/10.1109/access.2026.3662282

- **Decision:** supporting [preprint] — Benchmarks zero-shot, fine-tuned and trust-calibrated orchestration configurations, contrasting model-side tuning with orchestration gains in one application.
- **Evidence:** full text not read (status: pending).

### Zheng, Y., Hu, Y., Yu, T., & Quinn, A. (2025). AgentSight: System-Level Observability for AI Agents Using eBPF. https://doi.org/10.1145/3766882.3767169

- **Decision:** supporting — eBPF boundary tracing correlates agent intent with system actions, supplying observability that supports failure attribution in agent runs.
- **Evidence:** full text not read (status: pending).

### Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges. Information Fusion, 126(3), 103599-103599. https://doi.org/10.1016/j.inffus.2025.103599

- **Decision:** supporting — Review taxonomy contrasting tool-using AI agents with agentic AI across architecture, memory and autonomy, synthesizing configuration differences.
- **Evidence:** full text not read (status: pending).

### Krishnan, N. (2025). AI Agents: Evolution, Architecture, and Real-World Applications. arXiv preprint. http://arxiv.org/abs/2503.12687v1

- **Decision:** supporting [preprint] — Reviews agent paradigms, criticises limitations of current agent benchmarks and proposes a holistic evaluation framework.
- **Evidence:** full text not read (status: pending).

### Jiang, Z., Schmidt, D., Srikanth, D., Xu, D., Kaplan, I., Jacenko, D., & Wu, Y. (2025). AIDE: AI-Driven Exploration in the Space of Code. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2502.13138

- **Decision:** supporting [preprint] — Tree-search coding-agent scaffold benchmarked on MLE-Bench and RE-Bench; reports scaffold performance without separating harness from model effects.
- **Evidence:** full text not read (status: pending).

### Feng, W., Hao, C., Zhang, Y., Jiang, G., & Song, J. (2025). AirRAG: Autonomous Strategic Planning and Reasoning Steer Retrieval Augmented Generation. https://doi.org/10.18653/v1/2025.findings-emnlp.1030

- **Decision:** supporting — Adds MCTS-expanded reasoning actions, self-consistency verification and compute allocation to agentic RAG and reports gains over baselines.
- **Evidence:** full text not read (status: pending).

### Gu, Y., Xiong, Y., Mace, J., Jiang, Y., Hu, Y. C., Kasikci, B., & Cheng, P. (2025). Argos: Agentic Time-Series Anomaly Detection with Autonomous Rule Generation via Large Language Models. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2501.14170

- **Decision:** supporting [preprint] — Agentic anomaly-detection system built for explainability, reproducibility and autonomy in production; reports gains without controlling harness components.
- **Evidence:** full text not read (status: pending).

### Allam, A., Mansour, Y., & Shalan, M. (2025). ASIC-Agent: An Autonomous Multi-Agent System for ASIC Design with Benchmark Evaluation. 2025 IEEE International Conference on LLM-Aided Design (ICLAD), 23-29. https://doi.org/10.1109/iclad65226.2025.00033

- **Decision:** supporting — Domain agent plus benchmark that swaps base LLMs under one fixed multi-agent scaffold, giving an agent comparison with the harness described but never varied.
- **Evidence:** full text not read (status: pending).

### Liu, F., Wang, H., Cho, J., Roth, D., & Lo, A. W. (2025). AutoCT: Automating Interpretable Clinical Trial Prediction with LLM Agents. https://doi.org/10.18653/v1/2025.emnlp-main.1575

- **Decision:** supporting — LLM-agent framework using Monte Carlo tree search self-refinement for clinical trial prediction, compared with state-of-the-art methods without harness control.
- **Evidence:** full text not read (status: pending).

### Chen, H., Zuccon, G., & Leelanupab, T. (2025). Beyond GeneGPT: A Multi-Agent Architecture with Open-Source LLMs for Enhanced Genomic Question Answering. https://doi.org/10.1145/3767695.3769488

- **Decision:** supporting — Reproduces GeneGPT with open-source models then compares a monolithic architecture against a modular multi-agent one, changing model and topology together.
- **Evidence:** full text not read (status: pending).

### Sheth, I., Fatemi, B., & Fritz, M. (2025). CausalGraph2LLM: Evaluating LLMs for Causal Queries. https://doi.org/10.18653/v1/2025.findings-naacl.110

- **Decision:** supporting — Shows LLM causal-reasoning results swing about 60% with graph encoding alone, a direct demonstration of input-format confounding.
- **Evidence:** full text not read (status: pending).

### Lee, Y., Kim, J. H., Kim, J., Cho, H., Kang, J., Kang, P., & Kim, N. (2025). CheckEval: A reliable LLM-as-a-Judge framework for evaluating text generation using checklists. https://doi.org/10.18653/v1/2025.emnlp-main.796

- **Decision:** supporting — Checklist-based judging framework that raises inter-evaluator agreement and cuts score variance, addressing evaluator reliability in LLM measurement.
- **Evidence:** full text not read (status: pending).

### Wang, X., Li, Q., & Jia, W. (2025). Cognitive Edge Computing: A Comprehensive Survey on Optimizing Large Models and AI Agents for Pervasive Deployment. arXiv (Cornell University). https://doi.org/10.22541/au.176348756.61222219/v1

- **Decision:** supporting [preprint] — Edge-deployment survey proposing a standardised evaluation protocol with explicit measurement assumptions to make latency, energy and accuracy comparable.
- **Evidence:** full text not read (status: pending).

### Zu, L., Lin, L., Fu, S., Zhao, N., & Zhou, P. (2025). Collaborative Tree Search for Enhancing Embodied Multi-Agent Collaboration. https://doi.org/10.1109/cvpr52734.2025.02748

- **Decision:** supporting — Adds tree search and a plan-evaluation module to embodied multi-agent collaboration and reports gains over prior methods without controlling the surrounding harness.
- **Evidence:** full text not read (status: pending).

### Rivera, C. G., Byrd, G., Paul, W., Feldman, T., Booker, M., Holmes, E., Handelman, D. A., Kemp, B., Badger, A. R., Schmidt, A., Jatavallabhula, K. M., de Melo, C. M., Seenivasan, L., Unberath, M., & Chellappa, R. (2025). ConceptAgent: LLM-Driven Precondition Grounding and Tree Search for Robust Task Planning and Execution. https://doi.org/10.1109/icra55743.2025.11128414

- **Decision:** supporting — LLM robot planner whose ablations quantify predicate grounding and reflective tree search, a scaffold ablation rather than a harness-attribution study.
- **Evidence:** full text not read (status: pending).

### Haseeb, M. (2025). Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code. arXiv preprint. http://arxiv.org/abs/2508.08322v1

- **Decision:** supporting [preprint] — Reports a multi-agent context-engineering workflow beating single-agent baselines and rival frameworks while models, tools, and prompts all differ - RQ2 evidence.
- **Evidence:** full text not read (status: pending).

### Hyun, J.-S., Waytowich, N. R., & Chen, B. (2025). CREW-WILDFIRE: Benchmarking Agentic Multi-Agent Collaborations at Scale. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2507.05178

- **Decision:** supporting [preprint] — Benchmark evaluating several LLM multi-agent frameworks at scale, where framework identity is confounded with scaffold, making it RQ2 evidence.
- **Evidence:** full text not read (status: pending).

### Sun, H., Tan, W., Liu, L., Yan, Z., Lu, X., & Dai, H. (2025). DebateNav: Structured Multi-VLM Expert Debate for Robust Zero-Shot Object Navigation. https://doi.org/10.1109/hpcc67675.2025.00068

- **Decision:** supporting — Multi-round VLM expert debate compared against static one-shot planning, an uncontrolled scaffold comparison in embodied navigation.
- **Evidence:** full text not read (status: pending).

### Anghel, C., Anghel, A. A., Pecheanu, E., Cocu, A., Istrate, A., & Andrei, C. A. (2025). Diagnosing Bias and Instability in LLM Evaluation: A Scalable Pairwise Meta-Evaluator. Information, 16(8), 652-652. https://doi.org/10.3390/info16080652

- **Decision:** supporting — Meta-evaluation of LLM judges showing 48.4% of verdicts reverse under mirrored response order, a reliability limit for agent evaluation.
- **Evidence:** full text not read (status: pending).

### Berti, A., & Kourani, H. (2025). Diagnosing LLM Hallucinations in Process Mining Tasks: a Taxonomy and a Benchmark. https://doi.org/10.36227/techrxiv.175977705.50503509/v1

- **Decision:** supporting [preprint] — Hallucination taxonomy and audit layered on a process-mining benchmark with LLM-as-judge; an evaluation-methodology contribution, not harness variation.
- **Evidence:** full text not read (status: pending).

### Wei, P., Dimitriadis, D., Xu, Y., & Shen, M. (2025). Don't Just Demo, Teach Me the Principles: A Principle-Based Multi-Agent Prompting Strategy for Text Classification. arXiv preprint. http://arxiv.org/abs/2502.07165v1

- **Decision:** supporting [preprint] — Multi-agent prompting strategy benchmarked against zero-shot, CoT and stepback baselines, with ablations isolating the multi-agent framework's contribution.
- **Evidence:** full text not read (status: pending).

### Saha, B. K., Aarthi, V., & Naidu, O. D. (2025). DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. https://doi.org/10.1109/icaiic64266.2025.10920654

- **Decision:** supporting — LLM agentic workflow for grid fault analysis using argument reconstruction to repair malformed tool calls and tool-output caching, evaluated by expert scoring without isolating those mechanisms.
- **Evidence:** full text not read (status: pending).

### Zhou, W., Mesgar, M., Friedrich, A., & Adel, H. (2025). Efficient Multi-Agent Collaboration with Tool Use for Online Planning in Complex Table Question Answering. https://doi.org/10.18653/v1/2025.findings-naacl.54

- **Decision:** supporting — Multi-agent planner-plus-coder framework benchmarked against prior systems on table QA without holding the harness constant.
- **Evidence:** full text not read (status: pending).

### Zhai, Y., Liu, H., Zhang, Z., Lin, T., Xu, K., Yang, C., Feng, D., Ding, B., & Wang, H. (2025). Empowering Large Language Model Agent through Step-Level Self-Critique and Self-Training. https://doi.org/10.1145/3726302.3729965

- **Decision:** supporting — Contrasts step-level with trajectory-level self-critique inside an MCTS agent loop, a reflection-policy variation presented as a method contribution.
- **Evidence:** full text not read (status: pending).

### Zhai, Y., Yang, T., Xu, K., Feng, D., Yang, C., Ding, B., & Wang, H. (2025). Enhancing Decision-Making for LLM Agents via Step-Level Q-Value Models. Proceedings of the AAAI Conference on Artificial Intelligence, 39(25), 27161-27169. https://doi.org/10.1609/aaai.v39i25.34924

- **Decision:** supporting — Step-level Q-value guidance added to several LLM agents lifts a small model past GPT-4o-mini, a scaffold-versus-model result presented as a method.
- **Evidence:** full text not read (status: pending).

### Papageorgiou, G., Sarlis, V., Μaragoudakis, M., Magnisalis, I., & Tjortjis, C. (2025). Evaluating Faithfulness in Agentic RAG Systems for e-Governance Applications Using LLM-Based Judging Frameworks. Big Data and Cognitive Computing, 9(12), 309-309. https://doi.org/10.3390/bdcc9120309

- **Decision:** supporting — Compares simple and agentic RAG pipelines for faithfulness using three LLM judges and tool-level attribution; evaluation methodology with architecture-dependent results.
- **Evidence:** full text not read (status: pending).

### Zhou, J., Jiang, B., Gong, R., & Jiang, H. (2025). Evaluating LLM-based Role-playing Agent Authenticity via Event-driven Response Simulation: A Benchmark on Real-World Events Responses. 2025 2nd International Symposium on AI and Cybersecurity (ISAICS), 1-6. https://doi.org/10.1109/isaics66888.2025.11350200

- **Decision:** supporting — Benchmark and dataset for assessing role-playing agent fidelity; an evaluation-method contribution with no harness variation.
- **Evidence:** full text not read (status: pending).

### Hu, Y., Wang, Y., & McAuley, J. (2025). Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2507.05257

- **Decision:** supporting [preprint] — Benchmark for memory mechanisms in LLM agents; supplies measurement methodology for a harness component without isolating harness effects.
- **Evidence:** full text not read (status: pending).

### Mohammadi, M., Li, Y., Lo, J. C., & Yip, W. (2025). Evaluation and Benchmarking of LLM Agents: A Survey. https://doi.org/10.1145/3711896.3736570

- **Decision:** supporting — Survey of LLM agent evaluation objectives and processes including tooling and metric computation; organises measurement practice without isolating harness effects.
- **Evidence:** full text not read (status: pending).

### Iyenghar, P., Mansour, Z., & Wuebbelmann, J. (2025). Evaluation of Automated Machinery Functional Safety Risk Assessment Using LLMs. IEEE Access, 13, 203648-203669. https://doi.org/10.1109/access.2025.3632528

- **Decision:** supporting — Ablates zero-shot, rule-based, retrieval-augmented and hybrid prompting across architectures, showing prompt structure dominates model choice for accuracy.
- **Evidence:** full text not read (status: pending).

### SHERIFF, A. (2025). FATA: A Framework-Agnostic, Task-Agnostic Agentic AI Platform for Serverless Multi-Agent Orchestration. https://doi.org/10.36227/techrxiv.175099921.10546764/v1

- **Decision:** supporting [preprint] — Framework-agnostic control plane with a unified tool-management layer for agents; evaluated across domains but reports no controlled harness comparison.
- **Evidence:** full text not read (status: pending).

### Ullah, S., Balasubramanian, P., Guo, W., Burnett, A., Pearce, H., Kruegel, C., Vigna, G., & Stringhini, G. (2025). From CVE Entries to Verifiable Exploits: An Automated Multi-Agent Framework for Reproducing CVEs. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2509.01835

- **Decision:** supporting [preprint] — Multi-agent pipeline reproducing CVEs at a reported per-CVE cost, yielding reproducible benchmark material rather than harness analysis.
- **Evidence:** full text not read (status: pending).

### Saxena, Y., Bommireddy, R., Padia, A., & Gaur, M. (2025). Generation-Time vs. Post-hoc Citation: A Holistic Evaluation of LLM Attribution. arXiv preprint. https://doi.org/10.13016/m2l19h-mtre

- **Decision:** supporting [preprint] — Compares generation-time versus post-hoc citation pipelines and attributes attribution quality mainly to retrieval rather than to the paradigm.
- **Evidence:** full text not read (status: pending).

### Krechetova, V., & Kochedykov, D. (2025). GeoBenchX: Benchmarking LLMs in Agent Solving Multistep Geospatial Tasks. arXiv preprint, 27-35. https://doi.org/10.1145/3764915.3770721

- **Decision:** supporting [preprint] — Benchmarks eight models through one simple tool-calling agent with a fixed 23-function inventory, an agent comparison whose harness control is incidental.
- **Evidence:** full text not read (status: pending).

### Choube, A., Le, H., Li, J., Ji, K., Swain, V. D., & Mishra, V. (2025). GLOSS: Group of LLMs for Open-ended Sensemaking of Passive Sensing Data for Health and Wellbeing. Proceedings of the ACM on Interactive Mobile Wearable and Ubiquitous Technologies, 9(3), 1-32. https://doi.org/10.1145/3749474

- **Decision:** supporting — Multi-LLM sensemaking system compared against a RAG baseline on accuracy and consistency, with the surrounding harness left uncontrolled.
- **Evidence:** full text not read (status: pending).

### Song, X., Wang, Z., Wu, S., Shi, T., & Ai, L. (2025). Gradientsys: A Multi-Agent LLM Scheduler with ReAct Orchestration. arXiv preprint. https://doi.org/10.48550/arxiv.2507.06520

- **Decision:** supporting [preprint] — Multi-agent scheduler with typed MCP tools, retry-and-replan and observability compared to a MinionS-style baseline on GAIA with the harness uncontrolled.
- **Evidence:** full text not read (status: pending).

### Qiu, C. (2025). Hierarchical Expert Multi-Agent Framework for Causal Root Cause Localization in Cloud-Native Microservices. 2025 5th International Conference on Electronic Information Engineering and Computer Technology (EIECT), 818-821. https://doi.org/10.20944/preprints202511.0911.v1

- **Decision:** supporting — Hierarchical multi-agent root cause localization mixing model sizes, agent generation and prompt optimization, claiming gains over prior methods without stating harness control.
- **Evidence:** full text not read (status: pending).

### Xu, W., Shi, Y., Liang, Z., Ning, X., Mei, K., Wang, K., Zhu, X., Xu, M., & Zhang, Y. (2025). iAgent: LLM Agent as a Shield between User and Recommender Systems. https://doi.org/10.18653/v1/2025.findings-acl.928

- **Decision:** supporting — Recommendation agent whose dynamic-memory variant is compared against its memoryless counterpart, giving a memory-component effect inside an application study.
- **Evidence:** full text not read (status: pending).

### Kataria, V. (2025). Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination. International Journal of Intelligent Engineering and Systems, 18(11), 450-466. https://doi.org/10.22266/ijies2025.1231.28

- **Decision:** supporting — Hierarchical multi-agent LLM incident-analysis system evaluated against traditional monitoring and single-LLM limitations without stating harness control.
- **Evidence:** full text not read (status: pending).

### Wang, Z., Lin, S., Yan, G., Ghorbani, S., Yu, M., Zhou, J., Hu, N., Baruah, L., Peters, S., Kamath, S., Yang, J., & Zhang, Y. (2025). Intent-Driven Network Management with Multi-Agent LLMs: The Confucius Framework. https://doi.org/10.1145/3718958.3750537

- **Decision:** supporting — Two-year production multi-agent network-management deployment with its own validation framework; harness not controlled for comparison.
- **Evidence:** full text not read (status: pending).

### Szalontai, B., Márton, B., Pintér, B., & Gregorics, T. (2025). Investigating Reproducibility Challenges in LLM Bugfixing on the HumanEvalFix Benchmark. Software, 4(3), 17. https://doi.org/10.20944/preprints202505.2321.v1

- **Decision:** supporting — Reproduces HumanEvalFix results across 11 models and shows prompt template, generation length, quantization and decoding choices drive reported differences.
- **Evidence:** full text not read (status: pending).

### He, X., You, L., Tian, H., Han, B., Tsang, I., & Ong, Y.-S. (2025). Lang-PINN: From Language to Physics-Informed Neural Networks via a Multi-Agent Framework. arXiv preprint. https://doi.org/10.48550/arxiv.2510.05158

- **Decision:** supporting [preprint] — Multi-agent PINN construction system with a feedback agent for error diagnosis, compared against baselines without controlling the harness.
- **Evidence:** full text not read (status: pending).

### Sapkota, R., Shrestha, R., Rijal, M., & Karkee, M. (2025). LangChain vs. LangGraph vs. LangSmith: Taxonomies of Agentic AI Toolchains for End-to-End Orchestration. https://doi.org/10.36227/techrxiv.175695645.52670060/v1

- **Decision:** supporting [preprint] — Comparative taxonomy of LangChain, LangGraph and LangSmith orchestration layers proposing a reproducible benchmarking protocol including debugging resolution time.
- **Evidence:** full text not read (status: pending).

### Sucal, V., Jullien, M., Njifenjou, A., & Lefèvre, F. (2025). LLM-based Agentic Workflow on Verbal and Non-verbal Audiovisual Perceptions and Actions for Proactive Situated Human-Robot Interactions. https://doi.org/10.1145/3765766.3765797

- **Decision:** supporting — Compares a unified LLM agentic policy against a rule-based multi-policy system without controlling harness factors, so it is RQ2 evidence rather than a controlled study.
- **Evidence:** full text not read (status: pending).

### Salemi, A., Parmar, M., Goyal, P., Song, Y., Yoon, J., Zamani, H., Pfister, T., & Palangi, H. (2025). LLM-Based Multi-Agent Blackboard System for Information Discovery in Data Science. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2510.01285

- **Decision:** supporting [preprint] — Compares blackboard, master-slave and single-agent topologies for data discovery without stating how tools, prompts or control loop were equalised.
- **Evidence:** full text not read (status: pending).

### Li, H., Li, Z., Huang, W., & Guo, X. (2025). LLM-Cave: A benchmark and light environment for large language models reasoning and decision-making system. https://doi.org/10.1109/icicn67355.2025.11430449

- **Decision:** supporting — Lightweight decision-making benchmark reporting that speculation and planner-critic strategies let smaller models close the gap with stronger ones at higher cost.
- **Evidence:** full text not read (status: pending).

### Hundt, A., Azeem, R., Mansouri, M., & Brandão, M. (2025). LLM-Driven Robots Risk Enacting Discrimination, Violence, and Unlawful Actions. International Journal of Social Robotics, 17(11), 2663-2711. https://doi.org/10.1007/s12369-025-01301-x

- **Decision:** supporting — Evaluates several LLMs on discrimination and safety criteria for robot tasks with reproducible code, a model-level evaluation method.
- **Evidence:** full text not read (status: pending).

### Shojaee, P., Nguyen, N.-H., Meidani, K., Farimani, A. B., Doan, K. D., & Reddy, C. K. (2025). LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models. arXiv preprint. https://doi.org/10.48550/arxiv.2504.10415

- **Decision:** supporting [preprint] — Benchmark designed to block memorization so measured equation-discovery skill is valid; contributes measurement validity rather than harness analysis.
- **Evidence:** full text not read (status: pending).

### Huang, L., Liu, Y., Jiang, J., Zhang, R. Y., Yan, J., Li, J., & Zhao, X. (2025). ManuSearch: Democratizing Deep Search in Large Language Models with a Transparent and Open Multi-Agent Framework. https://doi.org/10.18653/v1/2025.findings-emnlp.130

- **Decision:** supporting — Open multi-agent deep-search framework plus the ORION benchmark, compared with open and closed-source baselines without harness control.
- **Evidence:** full text not read (status: pending).

### Liu, Z., Qiu, J., Wang, S., Zhang, J., Liu, Z., Ram, R., Chen, H., Yao, W., Heinecke, S., Savarese, S., Wang, H., & Xiong, C. (2025). MCPEval: Automatic MCP-based Deep Evaluation for AI Agent Models. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2507.12806

- **Decision:** supporting [preprint] — MCP-based framework automating task generation and standardising metrics for agent evaluation, an evaluation-methodology contribution.
- **Evidence:** full text not read (status: pending).

### Gundu, V. (2025). Methodological foundations of AI observability for enterprise LLM applications. International Journal Of Engineering And Computer Science, 14(10), 27742-27747. https://doi.org/10.18535/ijecs.v14i10.5277

- **Decision:** supporting — Proposes a multi-level observability methodology for enterprise LLM systems spanning quality, cost, security and responsibility metrics.
- **Evidence:** full text not read (status: pending).

### Liu, L. (2025). Monte Carlo Tree Search for Graph Reasoning in Large Language Model Agents. https://doi.org/10.1145/3746252.3760854

- **Decision:** supporting — Graph-guided MCTS augmentation for LLM agents evaluated across several model architectures, but harness differences from baselines are not controlled.
- **Evidence:** full text not read (status: pending).

### Constantinov, A. (2025). Multi-Agent Systems for Root Cause Analysis in Microservices. Työväentutkimus Vuosikirja. http://hdl.handle.net/10138/627125

- **Decision:** supporting [preprint] — Thesis comparing tree-search multi-agent root cause analysis against a multi-agent baseline with token and time costs, but no statement that the harness was held constant.
- **Evidence:** full text not read (status: pending).

### Anghel, C., Anghel, A. A., Pecheanu, E., Șușnea, I., Cocu, A., & Istrate, A. (2025). Multi-Model Dialectical Evaluation of LLM Reasoning Chains: A Structured Framework with Dual Scoring Agents. Informatics, 12(3), 76-76. https://doi.org/10.3390/informatics12030076

- **Decision:** supporting — Structured three-stage evaluation framework scored by two independent LLM raters with inter-rater agreement over four models; an evaluation methodology contribution.
- **Evidence:** full text not read (status: pending).

### Restrepo, D., Wu, C., Tang, Z., Shuai, Z., Phan, T. N. M., Ding, J.-E., Dao, C.-T., Gallifant, J., Dychiao, R. G., Artiaga, J. C. M., Bando, A. H., Gracitelli, C. P. B., Ferrer, V., Celi, L. A., Bitterman, D. S., Morley, M., & Nakayama, L. F. (2025). Multi-OphthaLingua: A Multilingual Benchmark for Assessing and Debiasing LLM Ophthalmological QA in LMICs. Proceedings of the AAAI Conference on Artificial Intelligence, 39(27), 28321-28330. https://doi.org/10.1609/aaai.v39i27.35053

- **Decision:** supporting — Multilingual ophthalmology question-answering benchmark plus a reflective agentic debiasing method, contributing measurement of cross-lingual performance gaps.
- **Evidence:** full text not read (status: pending).

### Vosoughi, A., Shahnazari, A., Xi, Y., Zhang, Z., Hess, G., Xu, C., & Abdolrahim, N. (2025). OPENXRD: A Comprehensive Benchmark Framework for LLM/MLLM XRD Question Answering. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2507.09155

- **Decision:** supporting [preprint] — Benchmarks 74 LLMs under matched closed-book and open-book conditions, quantifying how supplied context interacts with model architecture and scale.
- **Evidence:** full text not read (status: pending).

### Chen, W., Yuan, J., Chen, Q., Yang, C., Liu, Z., & Sun, M. (2025). Optima: Optimizing Effectiveness and Efficiency for LLM-Based Multi-Agent System. https://doi.org/10.18653/v1/2025.findings-acl.601

- **Decision:** supporting — Trains multi-agent communication policies and compares against single-agent and vanilla multi-agent baselines on the same base models, reporting token-efficiency trade-offs.
- **Evidence:** full text not read (status: pending).

### Watson, E., Amer, A., Harris, E., Ravindra, P., & Zhang, S. (2025). Personalized Constitutionally-Aligned Agentic Superego: Secure AI Behavior Aligned to Diverse Human Values. Information, 16(8), 651-651. https://doi.org/10.3390/info16080651

- **Decision:** supporting — Adds a constitution-checking oversight layer to the agent planning loop and measures harm reduction across several models on agent safety benchmarks.
- **Evidence:** full text not read (status: pending).

### Neumann, A., Kirsten, E., Zafar, M. B., & Singh, J. (2025). Position is Power: System Prompts as a Mechanism of Bias in Large Language Models (LLMs). https://doi.org/10.1145/3715275.3732038

- **Decision:** supporting — Compares identical demographic information placed in system versus user prompts across six commercial LLMs, quantifying an effect of prompt-format position.
- **Evidence:** full text not read (status: pending).

### Souza, R. P., Gueroudji, A., DeWitt, S., Rosendo, D., Ghosal, T., Ross, R., Balaprakash, P., & da Silva, R. F. (2025). PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows. https://doi.org/10.1109/escience65000.2025.00093

- **Decision:** supporting — Provenance model and system capturing agent prompts, responses and decisions across workflows, evaluated across edge, cloud and HPC facilities.
- **Evidence:** full text not read (status: pending).

### Hu, Y. C., Zhou, Q., Chen, Q., Li, X., Liu, L., Zhang, D., Kachroo, A., Oz, T., & Tripp, O. (2025). QualityFlow: An Agentic Workflow for Program Synthesis Controlled by LLM Quality Checks. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2501.17167

- **Decision:** supporting [preprint] — Agentic program-synthesis workflow whose quality checker controls retries and reverts, benchmarked to state of the art without isolating harness effects.
- **Evidence:** full text not read (status: pending).

### Chen, Z., Zhao, C., Chen, B., Lin, D., Chen, Y., Leung, A., Rajbahadur, G. K., Oliva, G. A., Zhang, H., Bhatia, A., Yong, C. C., & Hassan, A. E. (2025). RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2508.01550

- **Decision:** supporting [preprint] — Builds an execution harness, sandboxed environments and an RL scaffold for training SWE agents; reports benchmark gains without isolating harness effects.
- **Evidence:** full text not read (status: pending).

### Raza, S., Sapkota, R., Karkee, M., & Emmanouilidis, C. (2025). Responsible Agentic Reasoning and AI Agents: A Critical Survey. SuperIntelligence - Robotics - Safety & Alignment, 2(6). https://doi.org/10.36227/techrxiv.175735299.97215847/v2

- **Decision:** supporting [preprint] — Critical survey of agentic reasoning that proposes a unified evaluation methodology for agents with embedded safety mechanisms.
- **Evidence:** full text not read (status: pending).

### Sacoransky, E. (2025). Review of: "MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents". https://doi.org/10.32388/6k4anl

- **Decision:** supporting — Peer-review record of MedAgentBench, a realistic EHR benchmark for medical LLM agents; contributes evaluation-environment design rather than harness manipulation.
- **Evidence:** full text not read (status: pending).

### Temyingyong, N., Jain, D. K., Kumarsahu, N., Kumar, P., Phondi, R., Modecrua, W., Kaewtawee, K., Pachtrachai, K., & Kraisingkorn, T. (2025). ROAD: Reflective Optimization via Automated Debugging for Zero-Shot Agent Alignment. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2512.24040

- **Decision:** supporting [preprint] — Automated prompt and protocol optimisation raises agent success rate with the model fixed, but is framed as a method contribution rather than harness attribution.
- **Evidence:** full text not read (status: pending).

### Gupta, A., Mali, B., & Karfa, C. (2025). SANGAM: SystemVerilog Assertion Generation via Monte Carlo Tree Self-Refine. https://doi.org/10.1109/iclad65226.2025.00024

- **Decision:** supporting — Three-stage multi-agent MCTS pipeline for assertion generation compared against recent methods with no harness control.
- **Evidence:** full text not read (status: pending).

### Lee, H.-C., Zhang, Z., Lu, H., & Zhang, L. (2025). SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks. https://doi.org/10.52202/085713-3878

- **Decision:** supporting — Automated benchmark framework for evaluating LLM agents on authentic security engineering tasks with reproducible artifacts and gold patches.
- **Evidence:** full text not read (status: pending).

### Kutasov, J., Sun, Y., Colognese, P., van der Weij, T., Petrini, L., Zhang, C. B. C., Hughes, J., Deng, X., Sleight, H., Tracy, T., Shlegeris, B., & Benton, J. (2025). SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2506.15740

- **Decision:** supporting [preprint] — Sabotage and monitoring benchmark that also reports side-task success depending heavily on a hidden scratchpad, a context-affordance effect on measured behaviour.
- **Evidence:** full text not read (status: pending).

### Härer, F. (2025). Specification and Evaluation of Multi-Agent LLM Systems - Prototype and Cybersecurity Applications. 2025 International Conference on Cybersecurity and AI-Based Systems (Cyber-AI), 340-347. https://doi.org/10.1109/cyber-ai66431.2025.11233474

- **Decision:** supporting — Proposes an agent schema specification language and prototype architecture to make multi-agent LLM system evaluations systematic; feasibility shown on cybersecurity test cases.
- **Evidence:** full text not read (status: pending).

### Besrour, I., He, J., Schreieder, T., & Färber, M. (2025). SQuAI: Scientific Question-Answering with Multi-Agent Retrieval-Augmented Generation. https://doi.org/10.1145/3746252.3761471

- **Decision:** supporting — Multi-agent RAG QA system compared against a strong RAG baseline and released with a benchmark, an uncontrolled agent comparison plus a measurement resource.
- **Evidence:** full text not read (status: pending).

### Vaddhiparthy, S. S. S., Gokulraj, R., Dasari, R. N., & Mandava, S. (2025). Technical Report on KshemaGPT: A Multi-Agent LLM for Agriculture & Enterprise AI. https://doi.org/10.36227/techrxiv.175372827.71128287/v1

- **Decision:** supporting [preprint] — Deployed multi-agent agriculture assistant with per-agent latency measurement; evaluation exists but no harness component is varied or controlled.
- **Evidence:** full text not read (status: pending).

### Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025). The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2504.08066

- **Decision:** supporting [preprint] — End-to-end agentic discovery system whose tree-search scaffold and reviewer loop are judged by peer-review outcomes, without a controlled harness comparison.
- **Evidence:** full text not read (status: pending).

### Loru, E., Nudo, J., Di Marco, N., Santirocchi, A., Atzeni, R., Cinelli, M., Cestari, V., Rossi‐Arnaud, C., & Quattrociocchi, W. (2025). The simulation of judgment in LLMs. Proceedings of the National Academy of Sciences, 122(42), e2518443122-e2518443122. https://doi.org/10.1073/pnas.2518443122

- **Decision:** supporting — Benchmarks six LLMs and human raters through one identical structured agentic evaluation procedure, evidence on holding the procedure fixed while varying the judge.
- **Evidence:** full text not read (status: pending).

### Reza, Z. (2025). The Social Laboratory: A Psychometric Framework for Multi-Agent LLM Evaluation. arXiv preprint. https://doi.org/10.48550/arxiv.2510.01295

- **Decision:** supporting [preprint] — Psychometric evaluation framework for multi-agent debate that measures how assigned and moderator personas shift agent behaviour.
- **Evidence:** full text not read (status: pending).

### Xu, F. F., Song, Y., Li, B., Tang, Y., Jain, K., Bao, M., Wang, Z. Z., Zhou, X., Guo, Z., Cao, M., Yang, M., Lu, H., Martin, A., Su, Z., Maben, L., Mehta, R., Chi, W., Jang, L., Xie, Y., ... Neubig, G. (2025). TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks. https://doi.org/10.52202/085713-0315

- **Decision:** supporting — Benchmark of LLM agents on realistic workplace tasks comparing closed and open models in one fixed environment, with no harness variation reported.
- **Evidence:** full text not read (status: pending).

### Wu, X., Yang, C., Lin, X., Xu, C., Jiang, X., Sun, Y., Xiong, H., Li, J., & Guo, J. (2025). Think-on-Graph 3.0: Efficient and Adaptive LLM Reasoning on Heterogeneous Graphs via Multi-Agent Dual-Evolving Context Retrieval. arXiv preprint. http://arxiv.org/abs/2509.21710v2

- **Decision:** supporting [preprint] — GraphRAG multi-agent retrieval framework whose ablations confirm component contributions in an otherwise uncontrolled framework comparison.
- **Evidence:** full text not read (status: pending).

### Wang, Z., Cornacchia, A., Galante, F., Centofanti, C., Sacco, A., & Jiang, D. (2025). Towards a Playground to Democratize Experimentation and Benchmarking of AI Agents for Network Troubleshooting. https://doi.org/10.1145/3748496.3748990

- **Decision:** supporting — Open benchmarking platform giving network-troubleshooting agents a single API, fault injection and telemetry for reproducible comparison.
- **Evidence:** full text not read (status: pending).

### Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D. (2025). Towards reliable generative AI-driven scaffolding: Reducing hallucinations and enhancing quality in self-regulated learning support. Computers & Education, 240, 105448-105448. https://doi.org/10.1016/j.compedu.2025.105448

- **Decision:** supporting — Multi-agent LLM evaluator for educational scaffolds compared against single-agent LLM baselines; pedagogical sense of scaffold but an uncontrolled topology contrast.
- **Evidence:** full text not read (status: pending).

### Kuznetsov, I., Jost, A., Pantiukhin, D., Shapkin, B., Jung, T., & Koldunov, N. (2025). Transforming climate services with LLMs and multi-source data integration. npj Climate Action, 4(1). https://doi.org/10.1038/s44168-025-00300-y

- **Decision:** supporting — Climate information platform with an agent-based architecture whose real-world evaluation compares LLM configurations and speed-cost-accuracy trade-offs.
- **Evidence:** full text not read (status: pending).

### Lyn, J., & Graham, Y. (2025). TransLaTeX: Exposing the Last-Mile Execution Gap in LLM-Agent for Scientific Formatting. Proceedings of The First Workshop on Human–LLM Collaboration for Ethical and Responsible Science Production (SciProdLLM), 19-24. https://doi.org/10.18653/v1/2025.sciprodllm-1.3

- **Decision:** supporting — Introduces SafeFormat-Bench with execution-grounded verification for LLM formatting agents, a benchmark-design contribution.
- **Evidence:** full text not read (status: pending).

### Raza, S., Sapkota, R., Karkee, M., & Emmanouilidis, C. (2025). TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2506.04133

- **Decision:** supporting [preprint] — Review of trust, risk and security management for LLM multi-agent systems that introduces collaboration and tool-utilization metrics.
- **Evidence:** full text not read (status: pending).

### Qin, Y., Ye, Y., Fang, J., Wang, H., Liang, S., Tian, S., Zhang, J., Li, J., Li, Y., Huang, S., Zhong, W., Li, K., Yang, J., Yu, M., Lin, W., Liu, L., Xu, J., Ma, Q., Li, J., ... Shi, G. (2025). UI-TARS: Pioneering Automated GUI Interaction with Native Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2501.12326

- **Decision:** supporting [preprint] — Argues an end-to-end GUI model beats scaffolded GPT-4o and Claude frameworks, an explicit model-versus-scaffold claim made without holding the harness constant.
- **Evidence:** full text not read (status: pending).

### Rombaut, B., Masoumzadeh, S., Vasilevski, K., Lin, D., & Hassan, A. E. (2025). Watson: A Cognitive Observability Framework for the Reasoning of LLM-Powered Agents. https://doi.org/10.1109/ase63991.2025.00067

- **Decision:** supporting — Recovers reasoning traces from two different coding agents without altering behaviour, contributing observability and failure-attribution method.
- **Evidence:** full text not read (status: pending).

### Miyai, A., Zhao, Z., Egashira, K., Sato, A., Sunada, T., Onohara, S., Yamanishi, H., Toyooka, M., Nishina, K., Maeda, R., Aizawa, K., & Yamasaki, T. (2025). WebChoreArena: Evaluating Web Browsing Agents on Realistic Tedious Web Tasks. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2506.01952

- **Decision:** supporting [preprint] — Benchmark extension built on reproducible WebArena environments explicitly to enable fair, controlled comparison with prior agent work.
- **Evidence:** full text not read (status: pending).

### Shourya, T., Wang, Y., Hou, Z. J., Roy, S., Kumar, V. B., & Gangadharaiah, R. (2025). When Users Are Happy but Agents Are Wrong: Multi-Dimensional Evaluation of Tool-Augmented Dialogue. arXiv preprint, 862-892. https://doi.org/10.18653/v1/2026.gem-main.72

- **Decision:** supporting [preprint] — TRACE benchmark showing existing conversation evaluation frameworks miss agents that misread tool results yet satisfy users.
- **Evidence:** full text not read (status: pending).

### Shome, P., Krishnan, S., & Das, S. (2025). Why Johnny Can't Use Agents: Industry Aspirations vs. User Realities with AI Agents. arXiv preprint, 597-619. https://doi.org/10.1145/3786335.3813140

- **Decision:** supporting [preprint] — Usability study comparing two commercial agents on matched tasks, exposing gaps between marketed and realized capability with uncontrolled proprietary harnesses.
- **Evidence:** full text not read (status: pending).

### Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., & Wen, J.-R. (2024). A survey on large language model based autonomous agents. Frontiers of Computer Science, 18(6). https://doi.org/10.1007/s11704-024-40231-1

- **Decision:** supporting — Canonical survey of LLM-based autonomous agents proposing a unified construction framework and reviewing agent evaluation strategies.
- **Evidence:** full text not read (status: pending).

### Gu, J., Jiang, X., Shi, Z., Tan, H., Zhai, X., Xu, C., Li, W., Shen, Y., Ma, S., Liu, H.-Y., Wang, S., Zhang, K., Wang, Y., Gao, W., Ni, L., & Guo, J. (2024). A Survey on LLM-as-a-Judge. PubMed, 7(6), 101253-101253. https://doi.org/10.48550/arxiv.2411.15594

- **Decision:** supporting [preprint] — Survey of LLM-as-a-judge proposing reliability-evaluation methodologies and a benchmark, evidence about evaluator measurement validity.
- **Evidence:** full text not read (status: pending).

### Putta, P., Mills, E., Garg, N., Motwani, S., Finn, C., Garg, D., & Rafailov, R. (2024). Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2408.07199

- **Decision:** supporting [preprint] — Combines tree search, self-critique and preference fine-tuning for web agents, improving over baselines without isolating harness contributions.
- **Evidence:** full text not read (status: pending).

### Zhuge, M., Zhao, C., Ashley, D., Wang, W., Khizbullin, D., Xiong, Y., Liu, Z., Chang, E., Krishnamoorthi, R., Tian, Y., Shi, Y., Chandra, V., & Schmidhuber, J. (2024). Agent-as-a-Judge: Evaluate Agents with Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2410.10934

- **Decision:** supporting [preprint] — Agent-as-a-Judge evaluation framework plus DevAI benchmark; benchmarks three agentic systems without controlling their harnesses.
- **Evidence:** full text not read (status: pending).

### Ma, C., Zhang, J., Zhu, Z., Yang, C., Yang, Y., Jin, Y., Lan, Z., Kong, L., & He, J. (2024). AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2401.13178

- **Decision:** supporting [preprint] — Benchmark and open-source evaluation framework for multi-turn LLM agents introducing a fine-grained progress-rate metric beyond final success rate.
- **Evidence:** full text not read (status: pending).

### Dong, L., Lu, Q., & Zhu, L. (2024). AgentOps: Enabling Observability of LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2411.05285

- **Decision:** supporting [preprint] — Taxonomy of the artifacts and traces that must be recorded for LLM agent observability, derived from a mapping study of AgentOps tools.
- **Evidence:** full text not read (status: pending).

### Gioacchini, L., Siracusano, G., Sanvito, D., Gashteovski, K., Friede, D., Bifulco, R., & Lawrence, C. (2024). AgentQuest: A Modular Benchmark Framework to Measure Progress and Improve LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2404.06411

- **Decision:** supporting [preprint] — Modular benchmark framework contributing two progress metrics beyond overall success rate, then using them to locate failure points and refine agent architecture.
- **Evidence:** full text not read (status: pending).

### Aggarwal, P., Parno, B., & Welleck, S. (2024). AlphaVerus: Bootstrapping Formally Verified Code Generation through Self-Improving Translation and Treefinement. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2412.06176

- **Decision:** supporting [preprint] — Verifier-feedback tree refinement and misalignment filtering let an unmodified LLaMA model produce formally verified code; scaffold-side gain.
- **Evidence:** full text not read (status: pending).

### Chen, Y., Wang, W., Lobry, S., & Kurtz, C. (2024). An LLM Agent for Automatic Geospatial Data Analysis. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2410.18792

- **Decision:** supporting [preprint] — Geospatial LLM agent combining interpreter, static analysis and RAG within MCTS, contributing a new benchmark for agent tool use.
- **Evidence:** full text not read (status: pending).

### Hua, Y., Qu, L., & Haf, R. (2024). Assistive Large Language Model Agents for Socially-Aware Negotiation Dialogues. arXiv (Cornell University), 8047-8074. https://doi.org/10.18653/v1/2024.findings-emnlp.473

- **Decision:** supporting [preprint] — In-context exemplar selection for a remediator agent is varied and evaluated, but the rest of the role-play harness is uncontrolled.
- **Evidence:** full text not read (status: pending).

### Zhang, Y., Ruan, H., Fan, Z., & Roychoudhury, A. (2024). AutoCodeRover: Autonomous Program Improvement. arXiv (Cornell University), 1592-1604. https://doi.org/10.1145/3650212.3680384

- **Decision:** supporting [preprint] — Coding agent combining LLMs with code-search tools, compared against other agent approaches without equalising their scaffolds.
- **Evidence:** full text not read (status: pending).

### Lai, H., Liu, X., Iong, I. L., Yao, S., Chen, Y., Shen, P., Yu, H., Zhang, H., Zhang, X., Dong, Y., & Tang, J. (2024). AutoWebGLM: A Large Language Model-based Web Navigating Agent. https://doi.org/10.1145/3637528.3671620

- **Decision:** supporting — Web agent trained with HTML simplification plus a new bilingual benchmark, compared against GPT-4 agents without holding the harness constant; RQ2 evidence.
- **Evidence:** full text not read (status: pending).

### Choudhury, S., & Sodhi, P. (2024). Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2410.05434

- **Decision:** supporting [preprint] — Fine-tuning method compared against ReAct and behavior-cloning baselines across three agent benchmarks with no harness control.
- **Evidence:** full text not read (status: pending).

### Ulmer, D., Mansimov, E., Lin, K., Sun, L., Gao, X., & Zhang, Y. (2024). Bootstrapping LLM-based Task-Oriented Dialogue Agents via Self-Talk. IT University Of Copenhagen (IT University of Copenhagen), 9500-9522. https://doi.org/10.18653/v1/2024.findings-acl.566

- **Decision:** supporting — Self-talk data generation for dialogue agents paired with an automated dialogue-success metric used to filter training data.
- **Evidence:** full text not read (status: pending).

### Paul, S. K. (2024). Continually Learning Planning Agent for Large Environments guided by LLMs. https://doi.org/10.1109/cai59869.2024.00076

- **Decision:** supporting — Hybrid search-plus-LLM planning agent compared with Reflexion, CLIN and SayCan without holding scaffolds or memory formats constant.
- **Evidence:** full text not read (status: pending).

### Piatti, G., Jin, Z., Kleiman‐Weiner, M., Schölkopf, B., Sachan, M., & Mihalcea, R. (2024). Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2404.16698

- **Decision:** supporting [preprint] — Multi-agent commons simulation whose ablations show inter-agent communication drives cooperation, an uncontrolled configuration comparison.
- **Evidence:** full text not read (status: pending).

### Yang, Z., Chen, G., Li, X., Wang, W., & Yang, Y. (2024). DoraemonGPT: Toward Understanding Dynamic Scenes with Large Language Models (Exemplified as A Video Agent). arXiv (Cornell University). https://doi.org/10.48550/arxiv.2401.08392

- **Decision:** supporting [preprint] — Video agent combining symbolic memory, plug-in tools and an MCTS planner, evaluated on three benchmarks without harness control.
- **Evidence:** full text not read (status: pending).

### Bärmann, L., DeChant, C., Plewnia, J., Peller-Konrad, F., Bauer, D., Asfour, T., & Waibel, A. (2024). Episodic Memory Verbalization using Hierarchical Representations of Life-Long Robot Experience. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2409.17702

- **Decision:** supporting [preprint] — Hierarchical episodic memory searched by an LLM agent, evaluating a memory-layer design across robot and video datasets.
- **Evidence:** full text not read (status: pending).

### Zhang, F., Tian, S., Huang, Z., Qiao, Y., & Liu, Z. (2024). Evaluation Agent: Efficient and Promptable Evaluation Framework for Visual Generative Models. arXiv preprint, 7561-7582. https://doi.org/10.18653/v1/2025.acl-long.374

- **Decision:** supporting [preprint] — Agentic, promptable multi-round evaluation framework for generative models that cuts evaluation cost while matching results.
- **Evidence:** full text not read (status: pending).

### Akkiraju, R., Xu, A., Bora, D., Tan, Y., An, L., Seth, V., Shukla, A., Gundecha, P., Mehta, H., Jha, A., Raj, P., Balasubramanian, A., Maram, M., Muthusamy, G., Annepally, S. R., Knowles, S., Du, M., Burnett, N., Javiya, S., ... Boitano, J. (2024). FACTS About Building Retrieval Augmented Generation-based Chatbots. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2407.07858

- **Decision:** supporting [preprint] — Enumerates fifteen RAG pipeline control points and reports accuracy-latency trade-offs between large and small LLMs in production chatbots.
- **Evidence:** full text not read (status: pending).

### Dainese, N., Merler, M., Alakuijala, M., & Marttinen, P. (2024). Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2405.15383

- **Decision:** supporting [preprint] — Code-generation strategy with unit-test and environment feedback plus tree search, benchmarked against baselines; refinement-loop method evidence.
- **Evidence:** full text not read (status: pending).

### Liu, H., Chen, S., Zhang, Y., & Wang, H. (2024). GenoTEX: An LLM Agent Benchmark for Automated Gene Expression Data Analysis. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2406.15341

- **Decision:** supporting [preprint] — Benchmark for LLM agents on gene-expression analysis with a self-correcting multi-agent baseline and error analysis, useful as agent measurement evidence.
- **Evidence:** full text not read (status: pending).

### Yoon, J., Feldt, R., & Yoo, S. (2024). Intent-Driven Mobile GUI Testing with Autonomous Large Language Model Agents. https://doi.org/10.1109/icst60714.2024.00020

- **Decision:** supporting — LLM GUI-testing agent with memory mechanisms compared against non-LLM testing tools on activity coverage, leaving harness effects uncontrolled.
- **Evidence:** full text not read (status: pending).

### Jiang, J., Zhou, K., Zhao, W. X., Song, Y., Zhu, C., Zhu, H., & Wen, J.-R. (2024). KG-Agent: An Efficient Autonomous Agent Framework for Complex Reasoning over Knowledge Graph. arXiv preprint, 9505-9523. https://doi.org/10.18653/v1/2025.acl-long.468

- **Decision:** supporting [preprint] — LLM agent framework with toolbox and knowledge memory reporting a tuned 7B model beating larger LLMs, an uncontrolled framework-versus-baseline comparison.
- **Evidence:** full text not read (status: pending).

### Wang, R., Li, H., Han, X., Zhang, Y., & Baldwin, T. (2024). Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents. arXiv preprint. https://doi.org/10.48550/arxiv.2402.11651

- **Decision:** supporting [preprint] — Fine-tunes LLM agents on failed tool-use trajectories using prefix/suffix labels and analyses the information-versus-error trade-off.
- **Evidence:** full text not read (status: pending).

### Ma, Z., Kim, D. J., & Chen, T.-H. (2024). LibreLog: Accurate and Efficient Unsupervised Log Parsing Using Open-Source Large Language Models. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2408.01585

- **Decision:** supporting [preprint] — Unsupervised log parser composed of retrieval and self-reflection components with accuracy and cost reporting; refinement-loop method evidence.
- **Evidence:** full text not read (status: pending).

### Chiang, Y., Hsieh, E., Chou, C.-H., & Riebesell, J. (2024). LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval and Distillation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2401.17244

- **Decision:** supporting [preprint] — Evaluates a hierarchical ReAct agent framework against vanilla LLMs using a self-consistency metric, an agent-versus-no-agent comparison with uncontrolled harness.
- **Evidence:** full text not read (status: pending).

### Liu, Z., Chen, C., Wang, J., Chen, M., Wu, B., Che, X., Wang, D., & Wang, Q. (2024). Make LLM a Testing Expert: Bringing Human-like Interaction to Mobile GUI Testing via Functionality-aware Decisions. https://doi.org/10.1145/3597503.3639180

- **Decision:** supporting — LLM-driven GUI testing loop with a functionality-aware memory prompting mechanism evaluated against baselines on 93 apps, with the rest of the harness uncontrolled.
- **Evidence:** full text not read (status: pending).

### Motwani, S. R., Smith, C., Das, R. J., Rafailov, R., Laptev, I., Torr, P. H. S., Pizzati, F., Clark, R. J., & Witt, C. (2024). MALT: Improving Reasoning with Multi-Agent LLM Training. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2412.01928

- **Decision:** supporting [preprint] — Multi-agent post-training pipeline compared with a single chain-of-thought baseline; the topology change is confounded with training and the harness is uncontrolled.
- **Evidence:** full text not read (status: pending).

### Yang, D., Wei, J., Li, M., Liu, J., Liu, L., Hu, M., He, J., Ju, Y., Zhou, W., Liu, Y., & Zhang, L. (2024). MedAide: Information Fusion and Anatomy of Medical Intents via LLM-based Agent Collaboration. arXiv preprint, 127, 103743-103743. https://doi.org/10.1016/j.inffus.2025.103743

- **Decision:** supporting [preprint] — Medical multi-agent collaboration framework evaluated against baselines; an agent-topology comparison with no stated harness control.
- **Evidence:** full text not read (status: pending).

### Yin, G., Bai, H., Ma, S., Feng, N., Sun, Y., Xu, Z., Ma, S., Lu, J., Kong, X., Zhang, A., Yap, D. A., zhang, Y., Ahnert, K., Kamath, V., Berglund, M., Walsh, D., Gindele, T., Wiest, J., Lai, Z., ... Wang, Z. (2024). MMAU: A Holistic Benchmark of Agent Capabilities Across Diverse Domains. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2407.18961

- **Decision:** supporting [preprint] — Offline agent benchmark built to remove unreliable environment setup and decompose failures into five capabilities, addressing measurement validity.
- **Evidence:** full text not read (status: pending).

### Sun, L., Tao, Z., Li, Y., & Arakawa, H. (2024). ODA: Observation-Driven Agent for integrating LLMs and Knowledge Graphs. arXiv preprint, 7417-7431. https://doi.org/10.18653/v1/2024.findings-acl.442

- **Decision:** supporting [preprint] — Observation-action-reflection agent for knowledge graphs reporting state-of-the-art gains, an agent comparison with an uncontrolled harness.
- **Evidence:** full text not read (status: pending).

### Yang, L., Yang, C., Gao, S., Wang, W., Wang, B., Zhu, Q., Xiao, C., Zhou, J., Liang, G., Wang, Q., & Chen, J. (2024). On the Evaluation of Large Language Models in Unit Test Generation. https://doi.org/10.1145/3691620.3695529

- **Decision:** supporting — Empirical study over 17 Java projects and five open-source LLMs showing prompt factors significantly influence unit test generation results; non-agentic ablation.
- **Evidence:** full text not read (status: pending).

### Xie, T., Zhang, D., Chen, J., Li, X., Zhao, S., Cao, R., Hua, T. J., Cheng, Z., Shin, D., Lei, F., Liu, Y., Xu, Y., Zhou, S., Savarese, S., Xiong, C., Zhong, V. W., & Yu, T. (2024). OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2404.07972

- **Decision:** supporting [preprint] — Real-OS agent benchmark with scripted initial states and execution-based graders for reproducible evaluation, plus failure analysis of GUI grounding.
- **Evidence:** full text not read (status: pending).

### Shen, W., Li, C., Chen, H., Yan, M., Quan, X., Chen, H., Zhang, J., & Huang, F. (2024). Small LLMs Are Weak Tool Learners: A Multi-LLM Agent. arXiv preprint, 16658-16680. https://doi.org/10.18653/v1/2024.emnlp-main.929

- **Decision:** supporting [preprint] — Decomposes a monolithic tool-using agent into planner, caller and summariser and compares against single-LLM agents without equalising training or prompts.
- **Evidence:** full text not read (status: pending).

### Feuer, B., Goldblum, M., Datta, T., Nambiar, S., Besaleli, R., Dooley, S., Cembalest, M., & Dickerson, J. P. (2024). Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2409.15268

- **Decision:** supporting [preprint] — Shows LLM-judge preferences do not correlate with concrete alignment metrics and carry style bias; large reproducible meta-benchmark.
- **Evidence:** full text not read (status: pending).

### Wei, H., He, S., Xia, T., Liu, F., Wong, A., Lin, J., & Han, M. (2024). Systematic Evaluation of LLM-as-a-Judge in LLM Alignment Tasks: Explainable Metrics and Diverse Prompt Templates. arXiv preprint. https://doi.org/10.48550/arxiv.2408.13006

- **Decision:** supporting [preprint] — Shows prompt templates significantly shift LLM-judge reliability, making comparisons between alignment methods inconsistent unless the template is fixed.
- **Evidence:** full text not read (status: pending).

### Cheng, S., & Ng, P. H. F. (2024). The PDC30 Chatbot—Development of a Psychoeducational Resource on Dementia Caregiving Among Family Caregivers: Mixed Methods Acceptability Study. JMIR Aging, 8, e63715-e63715. https://doi.org/10.2196/63715

- **Decision:** supporting — Compares three GPT-4o chatbots where one keeps the architecture fixed and swaps only the knowledge base, an evaluation varying a single context component.
- **Evidence:** full text not read (status: pending).

### Cheng, X., Mayya, R., & Sedoc, J. (2024). To Err Is Human; To Annotate, SILICON? Toward Robust Reproducibility in LLM Annotation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2412.14461

- **Decision:** supporting [preprint] — Decomposes LLM annotation measurement error into guideline, baseline, prompt and model sources and prescribes a workflow for robust reproducibility.
- **Evidence:** full text not read (status: pending).

### Lu, Q., Zhu, L., Xu, X., Xing, Z., Harrer, S., & Whittle, J. (2024). Towards Responsible Generative AI: A Reference Architecture for Designing Foundation Model Based Agents. https://doi.org/10.1109/icsa-c63560.2024.00028

- **Decision:** supporting — Pattern-oriented reference architecture for foundation-model agents, evaluated by mapping onto two real agents; a combinable harness design.
- **Evidence:** full text not read (status: pending).

### Li, K., Jing, X., & Jing, C. (2024). Vector Storage Based Long-term Memory Research on LLM. International Journal of Advanced Network, Monitoring and Controls, 9(3), 69-79. https://doi.org/10.2478/ijanmc-2024-0029

- **Decision:** supporting — Vector-store long-term memory for LLM agents reporting 10-20% success-rate gain and 23% cost reduction versus other agents, with no stated control of the surrounding harness.
- **Evidence:** full text not read (status: pending).

### Chae, H., Kim, N., Ong, K. T.-I., Gwak, M., Song, G., Kim, J., Kim, S., Lee, D., & Yeo, J. (2024). Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2410.13232

- **Decision:** supporting [preprint] — Adds a learned world model to a web agent and reports accuracy plus cost advantages over tree-search agents, with harness differences uncontrolled.
- **Evidence:** full text not read (status: pending).

### He, H., Yao, W., Ma, K., Yu, W., Dai, Y., Zhang, H., Lan, Z., & Yu, D. (2024). WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2401.13919

- **Decision:** supporting [preprint] — Web agent plus benchmark and GPT-4V-as-judge protocol; compares its setup against GPT-4 (All Tools) and a text-only variant without controlling harness differences.
- **Evidence:** full text not read (status: pending).

### Bonatti, R., Zhao, D., Bonacci, F., Dupont, D., Abdali, S., Li, Y., Lu, Y., Wagle, J., Koishida, K., Bucker, A., Jang, L., & Hui, Z. (2024). Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2409.08264

- **Decision:** supporting [preprint] — Reproducible OS-agent environment with parallelised evaluation and a baseline multi-modal agent; standardises the evaluation environment.
- **Evidence:** full text not read (status: pending).

### 池谷, 裕., Deng, X., & Su, Y. (2023). Don’t Generate, Discriminate: A Proposal for Grounding Language Models to Real-World Environments. https://doi.org/10.18653/v1/2023.acl-long.270

- **Decision:** supporting — Grounded agent that scores candidate plans instead of generating them, reporting that this scaffold choice lets a BERT-base LM set a KBQA record over larger models.
- **Evidence:** full text not read (status: pending).

### Deng, X., 池谷, 裕., Zheng, B., Chen, S., Stevens, S., Wang, B., Sun, H., & Su, Y. (2023). Mind2Web: Towards a Generalist Agent for the Web. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2306.06070

- **Decision:** supporting [preprint] — Web agent benchmark whose evaluation shows that filtering raw HTML with a small LM before the LLM materially changes effectiveness and efficiency.
- **Evidence:** full text not read (status: pending).

### Yang, J., Zhang, H., Li, F., Zou, X., Li, C., & Gao, J. (2023). Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2310.11441

- **Decision:** supporting [preprint] — Ablation showing that overlaying segmentation marks on the input image, a pure observation-format change at fixed model, sharply alters GPT-4V grounding performance.
- **Evidence:** full text not read (status: pending).
