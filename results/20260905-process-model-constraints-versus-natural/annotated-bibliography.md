# Annotated Bibliography — BPMN process model driven multi-agent workflow automation

Generated 2026-09-05 from screening decisions, evidence-ledger notes, and quality scores. Working material and audit evidence — not submission text.

## Core (47)

### Begum, S., & Rosenzweig, M. (2026). A Privacy-Preserving On-Device Multi-Agent Architecture for AI PC (POMA) Workflow Automation. 2026 IEEE International Conference on AI and Data Analytics (ICAD), 1-8. https://doi.org/10.1109/icad69378.2026.11608651

- **Decision:** core — Enterprise workflow agents governed by a Policy Verifier, least-privilege action primitives, risk-aware gating and audit traces, with a safety/utility metric suite.
- **Evidence:** POMA interposes a runtime Policy Verifier between an LLM-driven computer-use agent and the desktop, restricting it to a typed set of least-privilege primitives whose invocation envelopes carry plan-step binding, evidence provenance, sensitivity tags and destination trust, then scoring each action on impact times evidence-uncertainty and returning ALLOW, ESCALATE or DENY. The design articulates RQ…
- **Domains:** autonomy-control, benchmarks-evaluation, human-in-loop, orchestration, policy-compliance, security-privacy, tool-integration
- **Quality:** rigor not yet scored

### Kaltenpoth, S., Skolik, A., Müller, O., & Beverungen, D. (2026). A Step Towards Cognitive Automation: Integrating LLM Agents with Process Rules. Lecture Notes in Computer Science, 308-324. https://doi.org/10.1007/978-3-032-02867-9_19

- **Decision:** core — Integrates LLM agents with explicit process rules for business process automation, the exact binding-versus-free-prompting mechanism RQ1 tests.
- **Evidence:** full text not read (status: unavailable).

### Veli, E. (2026). A stigmergy-driven multi-agent framework for intelligent task orchestration. UPCommons institutional repository (Universitat Politècnica de Catalunya). https://hdl.handle.net/2117/463237

- **Decision:** core [preprint] — Argues LLM orchestrators lack formal task-constraint models and treat compliance ad hoc, then evaluates a semantic validation layer plus ethics gate for violation recall in a commercial scenario.
- **Evidence:** This master's thesis carries the strongest evaluation design in the batch: 790 controlled runs across nine ablation configurations in a warehouse-brokerage scenario with expert-defined ground truth, effect sizes reported as Cliff's delta because the paired tests are underpowered, and a 2x2 factorial analysis of the two validation layers. For RQ2 it separately ablates five distinct control mechani…
- **Domains:** benchmarks-evaluation, conformance-violation, exception-handling, governance-accountability, multi-agent-topology, orchestration, policy-compliance
- **Quality:** rigor not yet scored

### Schnepf, J., Schwarz, M., Scheuermann, B., & Anderer, S. (2026). A Study on Multi-agent Collaboration for Business Process Automation in Enterprise Resource Planning Systems. Communications in computer and information science, 118-138. https://doi.org/10.1007/978-3-032-15632-7_7

- **Decision:** core — Multi-agent LLM collaboration for business process automation in ERP, directly the agentic organizational-process automation object of RQ2.
- **Evidence:** full text not read (status: unavailable).

### Dutta, P. (2026). Accountable Multi-Agent AI Systems: Orchestration Frameworks for Enterprise Workflow Automation with Human-in-the-Loop Verification. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.19845387

- **Decision:** core — Reports the exact RQ1 trade-off: HITL gating and audit trails cut unauthorized autonomous actions 94.7% while retaining 87.3% throughput versus a fully-autonomous baseline.
- **Evidence:** AMAOS makes human verification an architectural primitive rather than a configuration flag: the orchestrator decomposes a task into a DAG, computes a risk score from agent confidence, business impact, irreversibility and novelty, and inserts typed advisory, mandatory-approval or supervisor-escalation gates wherever that score crosses a threshold, backed by a hash-chained audit ledger. The reporte…
- **Domains:** autonomy-control, cost-latency, governance-accountability, human-in-loop, multi-agent-topology, orchestration, task-completion
- **Quality:** rigor not yet scored

### Calvanese, D., Casciani, A., De Giacomo, G., Dumas, M., Fournier, F., Kampik, T., La Malfa, E., Limonad, L., Marrella, A., Metzger, A., Montali, M., Amyot, D., Fettke, P., Polyvyanyy, A., Rinderle-Ma, S., Sardiña, S., Tax, N., & Weber, B. (2026). Agentic Business Process Management: A research manifesto. Information Systems, 140, 102738-102738. https://doi.org/10.1016/j.is.2026.102738

- **Decision:** core — Manifesto for governing autonomous agents via explicit process frames with framed autonomy, the central RQ1 construct of binding agents to process models.
- **Evidence:** full text not read (status: unavailable).

### Vu, H., Klievtsova, N., Leopold, H., Rinderle-Ma, S., & Kampik, T. (2026). Agentic Business Process Management: Practitioner Perspectives on Agent Governance in Business Processes. Lecture Notes in Business Information Processing, 29-43. https://doi.org/10.1007/978-3-032-02936-2_3

- **Decision:** core — Practitioner study of governance mechanisms for stochastic generative-AI agents deployed in business processes, squarely RQ2's control-mechanism question.
- **Evidence:** full text not read (status: unavailable).

### Kumar, K. (2026). Agentic Implementation in Business Processes with Guardrails. DigitalCommons - Kennesaw State University (Kennesaw State University). https://digitalcommons.kennesaw.edu/cognoconproceedings/7

- **Decision:** core [preprint] — Splits probabilistic LLM interpretation from deterministic RPA execution with guardrails and audit trails in a regulated invoicing use case.
- **Evidence:** full text not read (status: unavailable).

### Gatta, V. S. (2026). Compliance Digital Twins for Autonomous Financial Agents: Reliability-Aware Scenario Assurance via Calibrated LLM Evaluation. Journal of International Crisis and Risk Communication Research, 168-181. https://doi.org/10.63278/jicrcr.vi.3783

- **Decision:** core — Compliance digital twin exercises financial agents against control policies and segregation-of-duties scenarios with a calibrated LLM-as-judge evaluator.
- **Evidence:** The Compliance Digital Twin proposes a synchronized machine-readable model of financial process graphs, control mappings, segregation-of-duties rules and IAM entitlements, against which agents are exercised on injected routine, degraded and adversarial scenarios before deployment. Two elements matter for RQ1: the explicit process model (process graphs with decision points, handoffs and exception…
- **Domains:** autonomy-control, governance-accountability, human-in-loop, multi-agent-topology, policy-compliance, process-modeling
- **Quality:** rigor not yet scored

### Kölbel, L. M., Poss, L., & Schönig, S. (2026). Context is key for cybersecurity: leveraging external knowledge for process model explanation via LLMs. International Journal of Information Security, 25(4). https://doi.org/10.1007/s10207-026-01245-x

- **Decision:** core — Combines BPMN process models with ISO 27001/IEC 62443 via modular prompting for LLM compliance checking, evaluated on two IIoT cases with a compliance error typology.
- **Evidence:** This peer-reviewed study runs RQ1's relationship in the opposite direction: instead of constraining an agent with a process model, it hands a BPMN model plus an unstructured standard to an LLM and measures how well the model can decide compliance. Across two real-world cases (an ISO 27001 incident-response process and a SIREN-annotated IEC 62443-3-3 production process) it shows that supplying the…
- **Domains:** benchmarks-evaluation, conformance-violation, policy-compliance, process-modeling, prompting-instruction, security-privacy
- **Quality:** rigor not yet scored

### Wang, X., Shu, R., Dan, C., Xu, T., Luo, M., Mai, Y., & Wan, B. (2026). FRAMES: Guarded and Dual-Objective Skill Evolution for Agents in Policy-Governed Enterprise Workflows. arXiv preprint. https://doi.org/10.48550/arxiv.2608.01772

- **Decision:** core [preprint] — LLM agents in policy-governed enterprise workflows where the natural-language procedure is the guarded edit unit; directly targets RQ1's comparison and RQ2.
- **Evidence:** This is the strongest RQ1 evidence in my batch: it directly contrasts an agent given the policy as natural-language instructions in its prompt (B1 Raw LLM) against the same agent bound to explicit, structured, step-ordered skill procedures derived from the same policy, on a deployed financial document-auditing system and on tau-bench. The measured gap is large and asymmetric by risk category: the…
- **Domains:** benchmarks-evaluation, conformance-violation, cost-latency, governance-accountability, policy-compliance, prompting-instruction, task-completion
- **Quality:** rigor not yet scored

### Zhu, H., Liang, J., Hou, M., Tang, R., Zhu, X., Yang, J., Mao, Y., & Wu, F. (2026). From Business Events to Auditable Decisions: Ontology-Governed Graph Simulation for Enterprise AI. arXiv (Cornell University). https://arxiv.org/abs/2604.08603

- **Decision:** core [preprint] — Binds enterprise LLM decisions to a deterministic ontology-driven simulation graph with audit trail and measures F1 against unconstrained frontier baselines.
- **Evidence:** LOM-action argues explicitly against the natural-language-instruction arm of RQ1: business scenario conditions injected as prompt instructions are treated by the model as soft preferences, so it may still act on the unrestricted graph. The proposed alternative binds the agent to a mandatory three-phase pipeline (scenario parsing, sandbox graph mutation, decision derivation on the evolved graph) w…
- **Domains:** benchmarks-evaluation, explainability-rationale, governance-accountability, policy-compliance, process-modeling, prompting-instruction, tool-integration
- **Quality:** rigor not yet scored

### Boinapalli, N. R. (2026). GALENA: A Governance-Aware LLM Enterprise Navigation Architecture for Autonomous Multi-Agent Workflow Automation with Compliance Enforcement. https://doi.org/10.64971/j.cph.eijtem.v13.i3.12.2026

- **Decision:** core — Embeds a formal constraint set as a per-transition governance gate and reports 72.7% lower governance violation rate with 97% task completion against a named agent baseline.
- **Evidence:** GALENA encodes regulatory obligations as a formal constraint set carried inside every workflow object and enforces a hard governance gate before each agent action and again before any response is delivered, with three-valued PASS/REVISE/ROLLBACK verdicts and a drift monitor that re-opens deployed workflows when policy or data distributions shift. Of everything in this batch it maps most directly…
- **Domains:** conformance-violation, cost-latency, governance-accountability, multi-agent-topology, orchestration, policy-compliance, reliability-nondeterminism, task-completion
- **Quality:** rigor not yet scored

### Pacella, M., Papadia, G., & Giliberti, V. (2026). Governed Agentic Process Automation: A Floor-Safety Guarantee for Compliance-Critical LLM Routing. Algorithms, 19(8), 627. https://doi.org/10.3390/a19080627

- **Decision:** core — Directly tests RQ1: deterministic baseline versus ungoverned versus floor-guarded LLM on a compliance-critical onboarding process, reporting HITL recall and run-to-run stability.
- **Evidence:** full text not read (status: unavailable).

### Dumitriu, F., Greavu-Şerban, V., Necula, S.-C., & FĂTU, V.-C. (2026). Integrating LLM in Business Process Management: A Conceptual Framework for Augmenting the Process Lifecycle. Systems, 14(9), 1076-1076. https://doi.org/10.3390/systems14091076

- **Decision:** core — Lifecycle governance framework allocating LLM use by risk with NIST/EU AI Act controls, plus a BPI-2017 stress test exposing control-flow mismatch against an event-log referent.
- **Evidence:** full text not read (status: unavailable).

### Anand, A., Chatzi, I., Raha, R., & Schmuck, A.-K. (2026). MANTRA: Synthesizing SMT-Validated Compliance Benchmarks for Tool-Using LLM Agents. arXiv preprint. https://arxiv.org/abs/2605.06334

- **Decision:** core [preprint] — Synthesizes SMT-validated compliance benchmarks for tool-using agents in compliance-critical settings, contrasting natural-language policy with formal specification.
- **Evidence:** MANTRA addresses the measurement problem behind RQ1: how to decide, deterministically and at scale, whether an agent's tool-call trace actually followed a natural-language procedural manual. The pipeline chunks a manual into a dependence graph, samples subgraphs to control task difficulty, and then generates two artefacts independently from the same region: LLM-generated trace-level checks (requi…
- **Domains:** benchmarks-evaluation, conformance-violation, governance-accountability, policy-compliance, process-modeling, reliability-nondeterminism, tool-integration
- **Quality:** rigor not yet scored

### Rabinovich, E., Boaz, D., Zwerdling, N., & Anaby-Tavor, A. (2026). Near-Miss: Latent Policy Failure Detection in Agentic Workflows. arXiv (Cornell University), 296-308. https://doi.org/10.48550/arxiv.2603.29665

- **Decision:** core [preprint] — Detects latent policy failures where agents bypass required checks, measuring 8-17% near-miss rates on the tau-squared airline benchmark.
- **Evidence:** This paper attacks a measurement assumption that RQ1 depends on: if policy adherence is scored by comparing the final system state against a gold state, agents that skip a mandatory verification step but still land on the right outcome are counted as compliant. The authors define a 'near-miss' or latent failure as a mutating tool call that was not adequately informed, operationalize it by replayi…
- **Domains:** benchmarks-evaluation, conformance-violation, governance-accountability, policy-compliance, reliability-nondeterminism, task-completion, tool-integration
- **Quality:** rigor not yet scored

### Wang, L. (2026). Open-Rosalind: Tool-First Biomedical LLM Agents with Process-Aware Benchmarking. https://doi.org/10.64898/2026.05.06.722404

- **Decision:** core [preprint] — Tests whether workflow-constrained, tool-mediated execution beats unconstrained autonomy, reporting accuracy, failure rate and trace completeness against no-tool baselines.
- **Evidence:** This is the most directly informative study in the batch for RQ1 because it isolates the constraint itself as an experimental variable. Open-Rosalind binds the agent to pre-declared workflow templates under a hard step bound with mandatory tool mediation and mandatory traces, then ablates each constraint separately (full, react, no_tool, no_cite, no_template) over 1,770 runs across six model fami…
- **Domains:** autonomy-control, benchmarks-evaluation, explainability-rationale, governance-accountability, process-modeling, reliability-nondeterminism, task-completion, tool-integration
- **Quality:** rigor not yet scored

### Wu, J., & Gong, M. (2026). Policy-Invisible Violations in LLM-Based Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2604.12177

- **Decision:** core [preprint] — Defines policy-invisible violations, ships a compliance benchmark, and compares graph-grounded enforcement against a content-only DLP baseline: direct RQ1 and RQ2 evidence.
- **Evidence:** This paper isolates the failure class that makes natural-language policy specification insufficient in principle: violations whose decisive facts (recipient status, document audience label, session scope) are absent from the agent-visible context, in a cooperative non-adversarial setting. It contributes PhantomPolicy (60 violation and 60 matched safe cases across eight categories, with all tool r…
- **Domains:** autonomy-control, benchmarks-evaluation, conformance-violation, governance-accountability, policy-compliance, prompting-instruction, security-privacy, tool-integration
- **Quality:** rigor not yet scored

### Qasim, H. F., & Kadim, S. A. (2026). PolicyFaultBench: Mutation-Based Assurance of Policy Mediation and Proposal-Interface Conformance for Tool- Using AI Agents. Research Square. https://doi.org/10.21203/rs.3.rs-10502893/v1

- **Decision:** core [preprint] — Mutation-based benchmark for fail-closed policy mediation and proposal-interface conformance in tool-using agents, directly an evaluated control mechanism for RQ2.
- **Evidence:** This paper deliberately removes the agent's planning freedom in order to test the control mechanism itself: the prompt supplies a frozen synthetic operation so the model merely transcribes it, and what is measured is whether the deterministic fail-closed mediator between proposal and side effect authorises correctly. Its distinctive contribution to RQ2 is turning the policy into an object of assu…
- **Domains:** autonomy-control, benchmarks-evaluation, conformance-violation, governance-accountability, policy-compliance, reliability-nondeterminism, security-privacy, tool-integration
- **Quality:** rigor not yet scored

### Wu, B., Zhang, W., Chen, K., Fang, H., & Yu, N. (2026). Provably Secure Agent Guardrail. arXiv (Cornell University). https://arxiv.org/abs/2605.29251

- **Decision:** core [preprint] — ePCA replaces natural-language semantic guardrails with first-order logic constraints on agent actions and reports zero violations empirically: RQ1's contrast exactly.
- **Evidence:** The ePCA framework refuses natural-language intent at the enforcement boundary: agents must serialize each action into a strongly typed payload that is deterministically compiled into first-order logic and checked by an SMT solver against hard-coded safety axioms, so unsafe transitions become UNSAT rather than blocked by judgement. For RQ2 the useful part is the head-to-head against the two contr…
- **Domains:** autonomy-control, conformance-violation, cost-latency, policy-compliance, security-privacy, tool-integration
- **Quality:** rigor not yet scored

### Wang, S., Zhu, S., & Li, R. (2026). Runtime Policy Enforcement for MCP-Based LLM Agents. Electronics, 15(13), 2829. https://doi.org/10.3390/electronics15132829

- **Decision:** core — Deterministic policy enforcement at the tool-call boundary cuts attack success from 40% to 5% against a prompt-only baseline while reporting the task-level false-positive cost.
- **Evidence:** full text not read (status: unavailable).

### Besanson, G. (2026). SARC: A Governance-by-Architecture Framework for Agentic AI Systems. arXiv (Cornell University). https://arxiv.org/abs/2605.07728

- **Decision:** core [preprint] — Runtime constraint enforcement for tool-using agents benchmarked on a procurement task against post-hoc audit, output filtering, workflow rules and policy-as-code.
- **Evidence:** SARC adds an explicit constraint primitive to the reinforcement-learning tuple and compiles each constraint declaration into one of four enforcement sites in the agent loop, with placement determined by constraint class (hard before dispatch, soft over completed actions, escalation through a router bounded by the action's reversibility window). For RQ1 the paper supplies both an argument and a ca…
- **Domains:** autonomy-control, benchmarks-evaluation, cost-latency, governance-accountability, human-in-loop, multi-agent-topology, orchestration, policy-compliance
- **Quality:** rigor not yet scored

### Winston, C., Winston, C., & Just, R. (2026). Solver-Aided Verification of Policy Compliance in Tool-Augmented LLM Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2603.20449

- **Decision:** core [preprint] — Translates natural-language tool-use policies into SMT constraints checked at runtime, cutting violations while holding task accuracy on TauBench.
- **Evidence:** This is the most direct RQ1 test in this batch: the same airline operational policy is given to one agent as a natural-language policy document in context and to another as SMT-LIB-2.0 constraints checked by Z3 as a pre-condition on every planned tool call, with blocked calls returned to the agent alongside a minimum unsatisfiable core for replanning. The result is a precision/recall trade-off ra…
- **Domains:** benchmarks-evaluation, conformance-violation, policy-compliance, prompting-instruction, task-completion, tool-integration
- **Quality:** rigor not yet scored

### Menezes, V. P., Chowdhury, M. J. M., & Mahmood, A. N. (2025). An Agentic Framework for Compliant, Ethical and Trustworthy GenAI Applications in Healthcare. https://doi.org/10.1145/3727166.3727191

- **Decision:** core — Proposes a Compliance Agentic Model translating EU AI Act and WHO requirements into operational compliance mechanisms for agentic GenAI; a named control mechanism (RQ2).
- **Evidence:** full text not read (status: unavailable).

### Tebourbi, H., Nouzri, S., Mualla, Y., Fatimi, M. E., Najjar, A., Abbas-Turki, A., & Dridi, M. (2025). BPMN-Based Design of Multi-Agent Systems: Personalized Language Learning Workflow Automation with RAG-Enhanced Knowledge Access. Information, 16(9), 809. https://doi.org/10.20944/preprints202507.1291.v1

- **Decision:** core — Binds an LLM multi-agent system to explicit BPMN workflows for auditable, HITL-validated execution and reports outcome metrics; the RQ1 treatment condition, albeit in an education domain.
- **Evidence:** This paper treats a BPMN diagram as an executable specification rather than documentation: pools, lanes, tasks, gateways and message flows are compiled one-to-one into LangGraph agent nodes, tool nodes, routers and message edges, so the agents' branching logic is fixed by the model instead of by free-form prompting. That transformation is the mechanism RQ1 cares about, but the domain is Luxembour…
- **Domains:** explainability-rationale, human-in-loop, multi-agent-topology, orchestration, process-modeling, prompting-instruction, task-completion
- **Quality:** rigor not yet scored

### Park, J. H., & Madisetti, V. K. (2025). CAPRI: A Context-Aware Privacy Framework for Multi-Agent Generative AI Applications. IEEE Access, 13, 43168-43177. https://doi.org/10.1109/access.2025.3549312

- **Decision:** core — Named gatekeeper control inserted into multi-agent LLM business process workflows that enforces PII policy while preserving utility, the violations-versus-completion trade-off RQ1 poses.
- **Evidence:** CAPRI inserts a local 'gatekeeper' LLM between an enterprise and a cloud LLM agent, converting user input into typed entity structures whose PII values are contextually pseudonymized and reversibly mapped via UUIDs before a ReAct agent reasons over them. Its relevance to RQ1 is indirect but structurally analogous: it measures what happens to task completion when an agent is forced to operate over…
- **Domains:** benchmarks-evaluation, prompting-instruction, security-privacy, task-completion, tool-integration
- **Quality:** rigor not yet scored

### Jeong, C., Sim, S., Cho, H., Kim, S., & Shin, B. (2025). E2E Process Automation Leveraging Generative AI and IDP-Based Automation Agent: A Case Study on Corporate Expense Processing. Artificial Intelligence and Applications. https://doi.org/10.47852/bonviewaia52026307

- **Decision:** core — Deployed case study binding a GenAI automation agent to a policy database with HITL exception handling in corporate expense processing, reporting compliance-rate and error-rate gains.
- **Evidence:** This is an industrial deployment report from Samsung SDS describing a four-stage expense-processing pipeline in which an explicit policy database, not the language model, carries the compliance decision on the routine path. IDP extracts receipt fields, a whitelist/blacklist policy database performs the first classification, and the LLM is invoked only for unclassified or ambiguous items where it…
- **Domains:** deployment-case-study, exception-handling, human-in-loop, organizational-adoption, policy-compliance, task-completion, tool-integration
- **Quality:** rigor not yet scored

### Santos, W. D. S., Coutinho, J. R., Baião, F., Spyrides, G. M., & Lopes, H. (2025). Enhancing declarative business process management availability through generative AI. Process Science, 2(1). https://doi.org/10.1007/s44311-025-00029-1

- **Decision:** core — Constrained LLM generation with automated validation produces MP-Declare models supporting conformance checking; a control mechanism evaluated across 2000 models and two generation approaches.
- **Evidence:** This paper is upstream of RQ1: rather than binding an agent to a process model, it uses LLMs to manufacture the process models themselves, addressing the scarcity of multi-perspective declarative (MP-Declare) models caused by commercial confidentiality. Terpsichora combines role-play prompting, knowledge injection and few-shot examples with two constrained-generation mechanisms, Function Calling…
- **Domains:** benchmarks-evaluation, governance-accountability, policy-compliance, process-mining, process-modeling, prompting-instruction, reliability-nondeterminism, security-privacy
- **Quality:** rigor not yet scored

### Iyenghar, P., Mansour, Z., & Wuebbelmann, J. (2025). Evaluation of Automated Machinery Functional Safety Risk Assessment Using LLMs. IEEE Access, 13, 203648-203669. https://doi.org/10.1109/access.2025.3632528

- **Decision:** core — Directly contrasts zero-shot natural-language prompting with prompts bound to the ISO 13849-1 decision graph, lifting safety-classification accuracy from under 50 percent to 99 percent.
- **Evidence:** This is not an agent study, but it is the cleanest controlled ablation in the set of the RQ1 contrast between an explicit decision model and unstructured natural language. The task is classifying the Required Performance Level from a free-text machinery hazard description; the explicit model is the ISO 13849-1 Annex A risk graph, injected verbatim into the prompt as deterministic S/F/P mapping ru…
- **Domains:** benchmarks-evaluation, cost-latency, explainability-rationale, governance-accountability, policy-compliance, prompting-instruction, reliability-nondeterminism, security-privacy
- **Quality:** rigor not yet scored

### Unterschütz, S., & Hansen, B. (2025). Leveraging LLM-Based AI Agents for Boosting Vehicle Testing Process. SAE Technical Paper Series, 1. https://doi.org/10.4271/2025-01-0300

- **Decision:** core — LLM agent embedded in a regulated Euro 7 homologation validation workflow that generates test plans from regulation and performs software-based constraint verification.
- **Evidence:** full text not read (status: unavailable).

### Pulikonda, N. K. M. (2025). Real-Time Regulatory Intelligence Framework: LLM-powered compliance automation for financial services. World Journal of Advanced Engineering Technology and Sciences, 15(2), 3106-3115. https://doi.org/10.30574/wjaets.2025.15.2.0784

- **Decision:** core — LLM compliance automation for financial services with policy orchestration and human oversight, evaluated against traditional approaches and in case studies (RQ2).
- **Evidence:** Proposes a five-layer architecture (ingestion, processing, LLM interpretation, policy orchestration, human-in-the-loop governance) that turns financial regulatory text into infrastructure-as-code controls, and reports many performance figures against manual and rule-based compliance. For RQ1 the useful signal is directional rather than evidential: the paper repeatedly reports that prescriptive, r…
- **Domains:** deployment-case-study, explainability-rationale, governance-accountability, human-in-loop, organizational-adoption, policy-compliance, security-privacy
- **Quality:** rigor not yet scored

### Mishra, L. N., & Senapati, B. (2025). Retail Resilience Engine: An Agentic AI Framework for Building Reliable Retail Systems With Test-Driven Development Approach. IEEE Access, 13, 50226-50243. https://doi.org/10.1109/access.2025.3552592

- **Decision:** core — Agentic retail framework whose test-driven and input-filtering guardrails are empirically measured against a human expert baseline.
- **Evidence:** This paper proposes the Retail Resilience Engine, a layered agentic-AI framework that fine-tunes a transformer on retail and test-driven-development corpora and wraps it in a keyword-similarity prompt filter plus a test-first validation loop. Its contribution to RQ2 is a control mechanism of a different kind from formal constraints: generated test cases and pass/fail gates used as the reliability…
- **Domains:** autonomy-control, benchmarks-evaluation, explainability-rationale, governance-accountability, organizational-adoption, reliability-nondeterminism, task-completion
- **Quality:** rigor not yet scored

### 2025, A. F. C. L., Anaby Tavor, A., Boaz, D., Rabinovich, E., Uziel, G., & Zwerdling, N. (2025). Towards Enforcing Company Policy Adherence in Agentic Workflows. Underline Science Inc., 595-606. https://doi.org/10.18653/v1/2025.emnlp-industry.41

- **Decision:** core — Compiles company policy documents into deterministic guard code enforced before each agent action and evaluates it on tau-bench Airlines: direct RQ1 evidence.
- **Evidence:** This is the closest direct test of RQ1 in the set: it holds the agent, tools and task fixed and swaps natural-language policy in the prompt for compiled, deterministic pre-conditions. An offline buildtime stage maps a free-form policy document onto the 14 tau-bench Airlines tools and generates executable ToolGuards via test-driven development; at runtime each guard runs immediately before its too…
- **Domains:** benchmarks-evaluation, conformance-violation, human-in-loop, policy-compliance, prompting-instruction, task-completion, tool-integration
- **Quality:** rigor not yet scored

### Ait, A., Izquierdo, J. L., & Cabot, J. (2025). Towards Modeling Human-Agentic Collaborative Workflows: A BPMN Extension. Lecture notes in computer science, 367-382. https://doi.org/10.1007/978-3-032-04190-6_22

- **Decision:** core — BPMN extension for modelling human-agentic collaborative workflows, the explicit process-model binding for LLM agents that RQ1 contrasts with prompt-only instruction.
- **Evidence:** This paper is the clearest statement in my batch of the RQ1 mechanism itself: it shows that standard BPMN can only express agent collaboration, reflection strategies and agent uncertainty through free-text annotations, and argues this reliance on natural language produces ambiguity and misinterpretation. The authors then extend the BPMN metamodel with AgenticLane (role plus trust score), AgenticT…
- **Domains:** autonomy-control, governance-accountability, human-in-loop, multi-agent-topology, orchestration, process-modeling, reliability-nondeterminism
- **Quality:** rigor not yet scored

### Wahab, M. B. A., Mazen, S. A., & Helal, I. M. A. (2025). Utilizing Large Language Models in Business Process Management: Applications and Challenges. Journal of Computer Science, 21(8), 1921-1932. https://doi.org/10.3844/jcssp.2025.1921.1932

- **Decision:** core — Systematic review of 42 studies on LLMs across the BPM lifecycle, mapping which process tasks have been automated and the open interpretability and scalability gaps.
- **Evidence:** A literature review of 42 peer-reviewed studies mapping LLM use across the five BPM lifecycle stages, accompanied by a Streamlit demonstrator that runs the lifecycle zero-shot. For RQ1 its relevant contribution is the framing of a trade-off the authors leave unresolved: LLM adaptability versus the structured requirements of formal BPM systems, with hybrid LLM-plus-formal-verification pipelines pr…
- **Domains:** benchmarks-evaluation, explainability-rationale, governance-accountability, organizational-adoption, process-mining, process-modeling, prompting-instruction, reliability-nondeterminism, security-privacy
- **Quality:** rigor not yet scored

### Rao, K., Coviello, G., Mellone, G., De Vita, C. G., & Chakradhar, S. (2025). XPF: Agentic AI System for Business Workflow Automation. https://doi.org/10.1145/3731545.3743644

- **Decision:** core — Compares human-authored explicit step plans against LLM auto-generated plans on real business workflows, finding near-100% versus rarely-100% accuracy; the RQ1 contrast in plan form.
- **Evidence:** full text not read (status: unavailable).

### Duesterwald, E., Isahagian, V., Jayaram, K. R., Kumar, R., Muthusamy, V., Oum, P., Thomas, G., & Venkateswaran, P. (2024). A Conversational Assistant Framework for Automation. https://doi.org/10.1145/3700824.3701093

- **Decision:** core — LLM assistant turns natural-language instructions into explicit workflows, decision rules and data models in watsonx Orchestrate, with empirical accuracy results.
- **Evidence:** full text not read (status: unavailable).

### Onyekaonwu, C. B., Igba, E., & Anyebe, A. C. P. (2024). Agentic AI for Regulatory Intelligence: Designing Scalable Compliance Lifecycle Systems in Multinational Tech Enterprises. International Journal of Scientific Research and Modern Technology., 205-222. https://doi.org/10.38124/ijsrmt.v3i12.934

- **Decision:** core — Proposes an agentic AI compliance-lifecycle architecture with distributed agents, auditability, and human oversight, naming control mechanisms for regulated organizational processes.
- **Evidence:** A narrative review that proposes a multi-agent compliance lifecycle architecture in which specialised agents handle horizon scanning, risk scoring, control mapping and remediation under a coordinator, with sentinel agents supervising peers and federated edge deployment for data sovereignty. For RQ2 its most transferable idea is an externalised control layer: Governance-as-a-Service that intercept…
- **Domains:** autonomy-control, deployment-case-study, explainability-rationale, governance-accountability, human-in-loop, multi-agent-topology, orchestration, policy-compliance
- **Quality:** rigor not yet scored

### Kampik, T., Warmuth, C., Rebmann, A., Agam, R., Egger, L., Gerber, A., Hoffart, J., Kolk, J., Herzig, P., Decker, G., van der Aa, H., Polyvyanyy, A., Rinderle‐Ma, S., Weber, I., & Weidlich, M. (2024). Large Process Models: A Vision for Business Process Management in the Age of Generative AI. K&uuml;nstliche Intell., 39(2), 81-95. https://doi.org/10.1007/s13218-024-00863-8

- **Decision:** core — States the RQ1 thesis directly, proposing Large Process Models that pair LLM correlation with symbolic process knowledge and automated reasoning for safety and trustworthiness.
- **Evidence:** This is an industry-academic vision paper that argues the correlation power of LLMs must be fused with symbolic process models, knowledge graphs and automated reasoning rather than replacing them, which is the conceptual core of RQ1. Its most directly useful claim for RQ1 is architectural: the authors deliberately exclude LLMs from orchestration because of their stochasticity, keeping control flo…
- **Domains:** governance-accountability, human-in-loop, orchestration, policy-compliance, process-mining, process-modeling, reliability-nondeterminism, tool-integration
- **Quality:** rigor not yet scored

### Monti, F., Leotta, F., Mangler, J., Mecella, M., & Rinderle‐Ma, S. (2024). NL2ProcessOps: Towards LLM-Guided Code Generation for Process Execution. Lecture notes in business information processing, 127-143. https://doi.org/10.1007/978-3-031-70418-5_8

- **Decision:** core — LLM-guided code generation for executing business processes, a preregistered known item binding language models to process definitions for execution.
- **Evidence:** full text not read (status: unavailable).

### Schnepf, J., Engin, T., Anderer, S., & Scheuermann, B. (2024). Studies on the Use of Large Language Models for the Automation of Business Processes in Enterprise Resource Planning Systems. Lecture notes in computer science, 16-31. https://doi.org/10.1007/978-3-031-70239-6_2

- **Decision:** core — Preregistered known item studying LLM automation of business processes inside ERP systems, the organizational agentic automation setting central to both questions.
- **Evidence:** full text not read (status: unavailable).

### Lins, L. F., Nascimento, N., Alencar, P., Oliveira, T., & Cowan, D. (2023). Comparing Generative Chatbots Based on Process Requirements: A Case Study. https://doi.org/10.1109/bigdata59044.2023.10386251

- **Decision:** core — Case study testing whether GPT and PaLM understand BPMN constructs well enough to support process execution, the exact model-binding question in RQ1.
- **Evidence:** This case study tests the weakest possible form of the RQ1 intervention: hand the LLM the BPMN XML of a process model, tell it to act as an agent honouring BPMN restrictions, and see whether the model constrains behaviour when no process engine enforces it. Thirteen evaluation questions cover start events, forward flow, history, end events, decision points and unintended paths on a single Trip Pl…
- **Domains:** autonomy-control, benchmarks-evaluation, conformance-violation, human-in-loop, process-modeling, task-completion
- **Quality:** rigor not yet scored

### Schwartz, S., Yaeli, A., & Shlomov, S. (2023). Enhancing Trust in LLM-Based AI Automation Agents: New Considerations and Future Challenges. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2308.05391

- **Decision:** core [preprint] — Analyses trust considerations and control challenges specific to LLM-based process automation agents and assesses how current products address them (RQ2).
- **Evidence:** An early workshop position paper that ports trust constructs from human-to-human and human-automation research (reliability, openness, tangibility, immediacy, task characteristics, trust trajectory) onto LLM-based business process automation agents. Its RQ2 value is a named catalogue of control considerations rather than results: prompt mediation, content and output mediation, task grounding, kno…
- **Domains:** autonomy-control, explainability-rationale, governance-accountability, human-in-loop, organizational-adoption, reliability-nondeterminism, tool-integration
- **Quality:** rigor not yet scored

### Zeng, Z., Watson, W., Cho, N., Rahimi, S., Reynolds, S., Balch, T., & Veloso, M. (2023). FlowMind: Automatic Workflow Generation with LLMs. https://doi.org/10.1145/3604237.3626908

- **Decision:** core — LLM workflow generation grounded in vetted APIs to curb hallucination and data exposure, evaluated against baseline and ablation variants.
- **Evidence:** full text not read (status: unavailable).

### Ye, Y., Cong, X., Tian, S., Cao, J., Wang, H., Qin, Y., Lu, Y., Yu, H., Wang, H., Lin, Y., Liu, Z., & Sun, M. (2023). ProAgent: From Robotic Process Automation to Agentic Process Automation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2311.10751

- **Decision:** core [preprint] — Foundational agentic process automation paper where LLM agents construct and execute workflows in place of rigid RPA, with experiments on construction and execution.
- **Evidence:** This is the position-and-prototype paper that frames the RQ1 design space rather than testing it: it argues that rule-based RPA workflows are efficient but cannot handle dynamic decisions, while free-running LLM agents are flexible but inefficient, and proposes Agentic Process Automation as the hybrid. The concrete mechanism is an Agentic Workflow Description Language (JSON for data flow, Python…
- **Domains:** autonomy-control, governance-accountability, multi-agent-topology, orchestration, process-modeling, tool-integration
- **Quality:** rigor not yet scored

### Chaitanya, P. (n.d.). OpenMCPSpec: A Specification Framework for Robust, Governed, and Lifecycle-Managed Machine Communicable Processes in LLM-Agent Systems. 2026 Fourth International Conference on Secure Cyber Computing and Communications (ICSCCC). https://ieeexplore.ieee.org/document/11600150/

- **Decision:** core — Specification framework for governed, lifecycle-managed machine-communicable processes in LLM-agent systems directly targets RQ2 control mechanisms; no abstract, so full text is required.
- **Evidence:** Proposes an extended Model Context Protocol schema that moves governance metadata (pii, gdpr_sensitive, roles), reliability hints (nlp_hints) and lifecycle/versioning information out of middleware and into the machine-readable tool contract, so that policy can be enforced at the binding layer before business logic runs. This is a close structural analogue of RQ1 at the tool-call level: the declar…
- **Domains:** conformance-violation, cost-latency, governance-accountability, policy-compliance, prompting-instruction, security-privacy, tool-integration
- **Quality:** rigor not yet scored


## Supporting (174)

### Mai, P. T., Ngo, T. S., Le, N. H., Vu, T. G., Bui, H. V., & Dinh, T. T. (2026). A Business Process-Centric Approach for LLM-Driven Functional Test Generation. IEEE Access. https://doi.org/10.5281/zenodo.18642171

- **Decision:** supporting — Indexing record only, no abstract; the title indicates business-process models driving LLM test generation, so the method needs checking.
- **Evidence:** full text not read (status: pending).

### Sager, P., Meyer, B., Yan, P., von Wartburg-Kottler, R., Etaiwi, L., Enayati, A., Nobel, G., Abdulkadir, A., Grewe, B. F., & Stadelmann, T. (2026). A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions. Journal of Artificial Intelligence Research, 85. https://doi.org/10.1613/jair.1.19490

- **Decision:** supporting — Survey of 87 computer-use agent papers and 33 datasets identifying non-standardized evaluation and low benchmark task complexity as field-wide limitations.
- **Evidence:** full text not read (status: pending).

### Wang, S., Feng, Y., & Fang, X. (2026). A Large Language Model-Enabled Multi-Agent Collaboration Method for Complex Task Solving. Preprints.org. https://doi.org/10.20944/preprints202605.0900.v1

- **Decision:** supporting [preprint] — Role-separated multi-agent architecture with a verification stage beats a single LLM on completion and error rate, an adjacent structural-control baseline on generic tasks.
- **Evidence:** full text not read (status: pending).

### Quadri, F. E., & Bianchini, F. (2026). A Multi-Agent LLM System for Natural Language Querying of Operational Knowledge Graphs in Satellite Ground Stations. ESANN 2026 proceesdings, 463-468. https://doi.org/10.14428/esann/2026.es2026-42

- **Decision:** supporting — Deployed multi-agent LLM system with knowledge-graph grounding and operator-in-the-loop support for ground-station maintenance troubleshooting.
- **Evidence:** full text not read (status: pending).

### Nowak, M. (2026). A Multi-Criteria Decision Framework for Enterprise LLM Routing. Information, 17(6), 539-539. https://doi.org/10.3390/info17060539

- **Decision:** supporting — Enterprise LLM router with confidence margin and risk veto evaluated on 500 business prompts against seven baselines, trading cost against response sufficiency.
- **Evidence:** full text not read (status: pending).

### Cheong, A., Kassar, M., & Li, H. (2026). A Risk Assessment Framework for Cognitive Process Automation in Audit. Journal of Emerging Technologies in Accounting, 1-12. https://doi.org/10.2308/jeta-2024-031

- **Decision:** supporting — Risk framework for agentic cognitive process automation in audit that translates measured implementation risk into prescriptive human-oversight requirements; conceptual, not evaluated.
- **Evidence:** full text not read (status: pending).

### Mahmood, U., & Song, W.-C. (2026). A Self-Correcting Multi-Agent LLM Pipeline for Verified Kubernetes Network Policy. 2026 IFIP Networking Conference (IFIP Networking), 1-6. https://doi.org/10.23919/ifipnetworking70592.2026.11578993

- **Decision:** supporting — Deterministic verifier-in-the-loop multi-agent pipeline raises small-model policy correctness from 70-75% to 97-98%, an evaluated control mechanism with model-size baselines.
- **Evidence:** full text not read (status: pending).

### Shahin, D., Yasin, E., Ghaith, L., & Aref, A. (2026). A Systematic Review of Generative AI Applications in Process Mining: Techniques, Challenges, and Future Directions. https://doi.org/10.1109/icciaa68481.2026.11543805

- **Decision:** supporting — PRISMA review of 24 GenAI process-mining studies reporting fragmented evidence, limited standardized benchmarking, and trust concerns.
- **Evidence:** full text not read (status: pending).

### ISPAS, R.-L., & FLORESCU, M. (2026). Advanced Multilingual Natural Language Processing in Industrial Digitalization: A Case Study of Autonomous Document Classification and ERP Integration in Manufacturing. Proceedings of the ... International Conference on Business Excellence, 20(1), 6016-6048. https://doi.org/10.2478/picbe-2026-0445

- **Decision:** supporting — Deployed LLM document-classification system integrated with ERP, reporting a measured manual baseline error rate, per-decision rationales, and data-sanitization controls.
- **Evidence:** full text not read (status: pending).

### Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-T., Rocktäschel, T., Riedel, S., & Kiela, D. (2026). Affordance-Compiled Intelligence: Observable-Only Cognitive Impedance Matching for No-Meta LLM-Integrated Systems. arXiv (Cornell University). https://doi.org/10.5281/zenodo.20116149

- **Decision:** supporting [preprint] — Theory of world-side constraints (validators, authority scopes, conformance envelopes, rollback, audit receipts) for constraining fixed LLM policies; no empirical test.
- **Evidence:** full text not read (status: pending).

### Liu, D., Li, Y. B., Yang, Z., Wang, P., Chen, G., Xie, Y., Mao, Q., Qu, W., Zhu, Y., Zhou, T., Yuan, L., Zheng, Z., Lin, Q., Wang, Y., Luo, H., Shao, S., Qian, C., Liu, Q., Tang, L., ... Hu, X. (2026). AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2605.29801

- **Decision:** supporting [preprint] — Lightweight guardrail models deployed as a training-free online moderation layer for tool-using agents; an empirically evaluated runtime control mechanism.
- **Evidence:** full text not read (status: pending).

### Garg, N. (2026). AGENTIC AI FOR ENTERPRISE WORKFLOW AUTOMATION: IMPACT AND ARCHITECTURAL PRINCIPLES FOR MULTI-AGENT ORCHESTRATION. International Journal of Research in Commerce and Management Studies, 08(03), 122-136. https://doi.org/10.38193/ijrcms.2026.8309

- **Decision:** supporting — Names the gap between formal regulation and actual execution and proposes policy-bounded autonomy with I/O contracts and regularized HITL, but offers illustration rather than evaluation.
- **Evidence:** full text not read (status: pending).

### Patel, V., & Singh, D. (2026). AI Workflow Automation Agent &amp; Multi-Agent System using LangChain and LangGraph. INTERNATIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT, 10(04), 1-9. https://doi.org/10.55041/ijsrem60971

- **Decision:** supporting — Graph-based orchestration with checkpointers and HITL gates reports 88% task completion against rule-based systems, an agentic control mechanism with a deterministic baseline.
- **Evidence:** full text not read (status: pending).

### Venkiteela, P. (2026). An Enterprise Agentic Architecture Framework for Agentic AI Governance and Scalable Autonomy. Scientific Journal of Computer Science, 2(1), 1-17. https://doi.org/10.64539/sjcs.v2i1.2026.368

- **Decision:** supporting — Layered enterprise agentic reference architecture whose control plane enforces policy, identity, and lifecycle, tested on enterprise workflows with policy-guided safety claims.
- **Evidence:** full text not read (status: pending).

### Bennoit, C., Zamani, S., & Greff, T. (2026). Analyzing structural and semantic similarities between formal business process models using ChatGPT-5.1: a test report. Process Science, 3(1). https://doi.org/10.1007/s44311-026-00058-4

- **Decision:** supporting — Tests whether an LLM detects seeded structural and semantic deviations in BPMN models, showing accuracy depends on standardized representation and prompting.
- **Evidence:** full text not read (status: pending).

### Izev, M., & Johansson, G. (2026). Application and Impact of Large Language Model (LLM) Agents in Financial Operations and Public Policy. https://doi.org/10.14293/pr2199.004004.v1

- **Decision:** supporting [preprint] — Examines LLM agents in regulatory reporting and policy work, reporting reasoning variability and prompt-induced bias against accountability needs.
- **Evidence:** full text not read (status: pending).

### Matei, I., Zhenirovskyy, M., Sekar, P. K. M., & Wong, H. Y. (2026). Automated BPMN Model Generation from Textual Process Descriptions: A Multi-Stage LLM-Driven Approach. 2026 IEEE International Systems Conference (SysCon), 1-7. https://doi.org/10.1109/syscon66367.2026.11503535

- **Decision:** supporting — LLM pipeline that generates executable BPMN validated by SpiffWorkflow compliance checks; supplies a method and similarity metrics for producing the process-model artifact RQ1 needs.
- **Evidence:** full text not read (status: pending).

### Xuan, D. N. (2026). Autonomous SOC: A Multi-Agent LLM Architecture for Real-Time Cybersecurity Operations in Resource-Constrained Environments. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.19151333

- **Decision:** supporting [preprint] — Production deployment over 1.35M alerts reports a 91% autonomous resolution rate and cost reduction; empirical evidence on attainable autonomy levels without a policy-control mechanism.
- **Evidence:** full text not read (status: pending).

### Kim, M. H. (2026). Beyond Static Interrupts: Context-Aware Human-in-the-Loop as a Cognitive Process for Trustworthy LLM Agents. https://doi.org/10.36227/techrxiv.176857875.58164328/v1

- **Decision:** supporting [preprint] — Introduces context-aware human-in-the-loop with cognitive state freezing and traceable decisions as an architectural control for LLM agents.
- **Evidence:** full text not read (status: pending).

### Zhu, L., Li, Y., Wang, T., Chen, Z., Li, K., Liu, H., Wang, Y., Xu, L., Jiang, P., & Zhang, Z. (2026). Blockchain Empowered Trustworthy Agent Networks: Foundations, Taxonomy, and Future Directions. arXiv (Cornell University). https://arxiv.org/abs/2608.04626

- **Decision:** supporting [preprint] — Survey naming authorization, provenance and accountability trust mechanisms for agent networks; a control-mechanism taxonomy for RQ2 without empirical tests.
- **Evidence:** full text not read (status: pending).

### Licardo, J. T., Tanković, N., & Etinger, D. (2026). BPMN Assistant: An LLM-Based Approach to Business Process Modeling. Applied Sciences, 16(5), 2213-2213. https://doi.org/10.3390/app16052213

- **Decision:** supporting — Structured JSON editing operations beat direct XML for LLM BPMN authoring, with conformance-checking F1 plus latency and token results; a method and benchmark for the model artifact.
- **Evidence:** full text not read (status: pending).

### Kumarasinghe, A., & Kirikova, M. (2026). BPMN-Based Business Process Collaboration Modeling Using Large Language Models. Lecture Notes in Business Information Processing, 130-138. https://doi.org/10.1007/978-3-032-12063-2_9

- **Decision:** supporting — LLM role-playing approach to BPMN collaboration modelling; a method for producing process models rather than constraining an executing agent.
- **Evidence:** full text not read (status: pending).

### Lindenberg, P. P., Kumara, I., Owotogbe, J., van den Heuvel, W.-J. A. M., & Tamburri, D. A. (2026). Business Process Discovery Through Agentic Generative AI. Lecture notes in computer science, 253-267. https://doi.org/10.1007/978-981-95-5015-9_19

- **Decision:** supporting — Multi-agent LLM dialogue applied to business process discovery; an adjacent agentic BPM method rather than a control or compliance mechanism.
- **Evidence:** full text not read (status: pending).

### Diganto, A., Lohrasbi, S., Neto, E. C. P., & Iqbal, S. (2026). Can LLM Agents Replace Reinforcement Learning Agents in Cyber Defence Automation: A Case Study Using the DARPA CAGE-2 Challenge. 2026 International Conference on Smart Applications, Communications and Networking (SmartNets), 1-4. https://doi.org/10.1109/smartnets69662.2026.11604963

- **Decision:** supporting — Compares LLM agents against RL baselines on the CAGE-2 cyber-defence benchmark, an adjacent empirical result on replacing learned policies with language-driven decisions.
- **Evidence:** full text not read (status: pending).

### Soldani, D. (2026). Claude Code Complete User Handbook. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2608.26742

- **Decision:** supporting [preprint] — Names a four-layer agent control stack, distinguishes enforced from advisory controls, and maps them to governance frameworks; a control-mechanism source for RQ2.
- **Evidence:** full text not read (status: pending).

### Papacharalampopoulos, A., Karagianni, O. M., & Stavropoulos, P. (2026). Cognitive Supervisory Control with LLM Reasoning Agent for Fault-Tolerant Process Systems: A Digital Twin Perspective. Processes, 14(14), 2298. https://doi.org/10.3390/pr14142298

- **Decision:** supporting — Bounds an LLM to a verified controller bank so it only emits audit records, a bounded-autonomy pattern with explicit non-intrusiveness evidence in industrial process control.
- **Evidence:** full text not read (status: pending).

### Fassbender, P. (2026). Compliance without coherence: fluent failure and the ethics of alignment evaluation in multi-agent language models. AI and Ethics, 6(4). https://doi.org/10.1007/s43681-026-01252-7

- **Decision:** supporting — Conceptual account of fluent failure, arguing surface compliance monitoring of LLM agents is blind to structural breakdown; a named limitation of compliance scoring.
- **Evidence:** full text not read (status: pending).

### Assidiqi, M. H., Alghazzawi, D., Alarifi, S., & Cheng, L. (2026). Conversational Enterprise Management Through Agentic AI: A Five-Pillar Framework for LLM-Driven ERP Systems. Applied Artificial Intelligence, 40(1). https://doi.org/10.1080/08839514.2026.2700868

- **Decision:** supporting — LLM multi-agent ERP framework with a security pillar and preliminary validation across finance, HR, and supply-chain scenarios (28/31 criteria).
- **Evidence:** full text not read (status: pending).

### Soma, R. (2026). End-to-End Architecture for LLM-Based Business Process Automation: A Low-Code Integration Framework With Performance Benchmarking. IEEE Access, 14, 105921-105940. https://doi.org/10.1109/access.2026.3696852

- **Decision:** supporting — Low-code LLM orchestration deployed on three enterprise processes with accuracy, latency, and cost measured against traditional rule-based BPM; empirical but not violation-focused.
- **Evidence:** full text not read (status: pending).

### Sarr, L. A., Barthe‐Delanoë, A., Bork, D., Ayite, K., Macé-Ramète, G., & Bénaben, F. (2026). From chat to process: A conversational agent framework for social business process management. Information Processing & Management, 63(8), 104940-104940. https://doi.org/10.1016/j.ipm.2026.104940

- **Decision:** supporting — Conversational multi-agent framework covering the BPM lifecycle with intent detection and process memory, illustrated on a call-for-tenders use case.
- **Evidence:** full text not read (status: pending).

### Ruan, A. (2026). From Logic Monopoly to Social Contract: Separation of Power and the Institutional Foundations for Autonomous Agent Economies. arXiv (Cornell University). http://arxiv.org/abs/2603.25100

- **Decision:** supporting [preprint] — Proposes constitutional separation of planning, execution and adjudication for enterprise agents, citing attack-success and deception evidence.
- **Evidence:** full text not read (status: pending).

### Manimangalam, P. (2026). From Tools to Autonomous Agents: Rethinking AI-Driven Business Transformation. Proceedings of the AAAI Symposium Series, 8(1), 210-211. https://doi.org/10.1609/aaaiss.v8i1.42544

- **Decision:** supporting — Conceptual framework separating autonomy from automation and treating governance mechanisms as the binding constraint on agent action, useful framing for RQ2 without evaluation.
- **Evidence:** full text not read (status: pending).

### Jakkli, A., Rajamanoharan, S., & Nanda, N. (2026). How Well Do Models Follow Their Constitutions?. arXiv (Cornell University). https://arxiv.org/abs/2605.24229

- **Decision:** supporting [preprint] — Measures violation rates when models are governed by long natural-language specifications, quantifying RQ1's natural-language-instruction arm.
- **Evidence:** full text not read (status: pending).

### Kumar, S. (2026). Human-in-the-Loop Automation Patterns for Financial Services using Camunda and Modern Java UIs. https://doi.org/10.1109/icicv68925.2026.11554821

- **Decision:** supporting — BPMN-orchestrated human-in-the-loop patterns for regulated financial workflows with audit traceability and compliance enforcement, evaluated on workflow metrics.
- **Evidence:** full text not read (status: pending).

### Chengeta, K. (2026). Hyperautomation with Camunda Agentic-AI and Cloud. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.20456689

- **Decision:** supporting — Practitioner book on binding LLM agents to BPMN and DMN in Camunda with HITL governance and audit across regulated sectors; catalogues mechanisms without empirical evaluation.
- **Evidence:** full text not read (status: pending).

### Eladawi, M., Dakalbab, F., Nasir, Q., & Talib, M. A. (2026). Integrating Lightweight Large Language Models into ERP Systems: A Demonstrative Implementation in ERPNext. https://doi.org/10.1109/icetsis68266.2026.11548878

- **Decision:** supporting — Local lightweight LLM wired into ERPNext with a prompt and response-filtering pipeline, demonstrated on a sales-order procedure.
- **Evidence:** full text not read (status: pending).

### Tomašev, N., Franklin, M., & Osindero, S. (2026). Intelligent AI Delegation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2602.11865

- **Decision:** supporting [preprint] — Delegation framework specifying authority, responsibility, accountability and role boundaries between agents and humans; a conceptual control mechanism for agentic work.
- **Evidence:** full text not read (status: pending).

### Soni, K., Luthra, M., Soni, S., & Tiwary, G. (2026). Intelligent Document Workflows. https://doi.org/10.1201/9781032658056-10

- **Decision:** supporting — Reference architecture for document-centric finance and legal workflows with explainability, auditability and governance controls; adjacent deployment evidence.
- **Evidence:** full text not read (status: pending).

### Bakal, G. (2026). Knowledge Activation: AI Skills as the Institutional Knowledge Primitive for Agentic Software Development. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2603.14805

- **Decision:** supporting [preprint] — Replaces prose documentation with structured units encoding tools and constraints agents must respect; the instruction-format contrast, with a deployment survey.
- **Evidence:** full text not read (status: pending).

### Arslan, M., Munawar, S., Riaz, Z., & Cruz, C. (2026). Large language models for business and management applications: A review. Information Processing & Management, 63(7), 104864-104864. https://doi.org/10.1016/j.ipm.2026.104864

- **Decision:** supporting — Review of 84 LLM business and management applications mapping deployment patterns, retrieval grounding and governance-aware workflows plus persistent accuracy gaps.
- **Evidence:** full text not read (status: pending).

### Alsaleh, O. (2026). Large language models for DAMA-aligned data management in telecommunication systems: a review of OSS/BSS and 5G/6G applications. Telecommunication Systems, 89(2). https://doi.org/10.1007/s11235-026-01462-8

- **Decision:** supporting — PRISMA review of LLM and agentic systems in telecom operations reporting weak compliance-enforcement evidence, 82% non-production evaluation and sparse latency reporting.
- **Evidence:** full text not read (status: pending).

### Reis, D., Caldeira, J., & Jesus, M. (2026). Leveraging large language models for agentic process analytics assistants: Assessing accuracy in process mining tasks. Expert Systems with Applications, 332, 133347-133347. https://doi.org/10.1016/j.eswa.2026.133347

- **Decision:** supporting — Abstract unavailable; title indicates an empirical accuracy assessment of agentic LLM assistants on process mining tasks, relevant as method and evidence.
- **Evidence:** full text not read (status: pending).

### Na, S., & Kostunin, D. (2026). LLM-Based Agent for Standard Compliance in GitLab Merge Requests. TH Wildau Engineering and Natural Sciences Proceedings, 3. https://doi.org/10.52825/th-wildau-ensp.v3i.3518

- **Decision:** supporting — LLM agent checks merge requests against an explicit rule catalog with JSON-schema output validation, a rule-bound governance prototype.
- **Evidence:** full text not read (status: pending).

### Okamoto, R., Kusumoto, S., & Matsumoto, S. (2026). LLM-Based Structural Standardization of Software Requirements Specifications for ISO Conformance. Research Square. https://doi.org/10.21203/rs.3.rs-9560604/v1

- **Decision:** supporting [preprint] — LLM restructuring of requirements documents to conform to ISO/IEC/IEEE 29148; adjacent evidence on constraining LLM output with an explicit structural standard.
- **Evidence:** full text not read (status: pending).

### Pan, Y., Wang, M., Lu, L., Lamsal, R., Pärn, E., Zlatanova, S., & Brilakis, I. (2026). LLM-enabled multi-agent framework for natural language interaction with graph-based digital twins. Automation in Construction, 183, 106791-106791. https://doi.org/10.1016/j.autcon.2026.106791

- **Decision:** supporting — Grounding agent outputs in a structured graph rather than prompts alone cuts hallucination and beats prompt-only and LangChain baselines; adjacent structure-versus-instruction evidence.
- **Evidence:** full text not read (status: pending).

### Renney, H., Nethercott, M., Renney, N., & Hayes, P. (2026). LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms. Journal on artificial intelligence, 8(1), 231-257. https://doi.org/10.32604/jai.2026.078487

- **Decision:** supporting — Systemization and empirical assessment of LLM multi-agent design patterns across domains; abstract is a truncated scrape but the pattern catalogue is usable for RQ2.
- **Evidence:** full text not read (status: pending).

### Zaman, A., Nordby, E., & Heiding, F. (2026). Manipulation Is Task-Dependent: A Multi-Axis, Multi-Environment Evaluation of Frontier LLMs. arXiv (Cornell University). https://arxiv.org/abs/2606.25899

- **Decision:** supporting [preprint] — Shows instructional framing and incentives drive misbehaviour differently per environment and that single-axis benchmarks mislead; evidence on natural-language limits.
- **Evidence:** full text not read (status: pending).

### Wimmer, A., Costa, A., & Pufahl, L. (2026). Natural Language Processing for BPMN Model Generation with LLMs: A Systematic Literature Review. Lecture Notes in Business Information Processing, 425-437. https://doi.org/10.1007/978-3-032-13426-4_31

- **Decision:** supporting — Systematic review of LLM-based BPMN model generation, useful for characterising how process models are produced and represented for LLMs.
- **Evidence:** full text not read (status: pending).

### Dewansh, S. (2026). Policy Convergence and Explainable Stability in Orchestrated Multi-Agent LLM Trading Frameworks. International Journal of Advanced Engineering, Management and Science, 12(2), 58-64. https://doi.org/10.22161/ijaems.122.8

- **Decision:** supporting — Analytical framework naming risk-gating logic, deliberative topology, and rationale persistence as stability determinants for multi-agent LLMs in a regulated financial setting.
- **Evidence:** full text not read (status: pending).

### Agostinelli, S., del-Río-Ortega, A., Estrada-Torres, B., Goñi-Medina, R., Marrella, A., Resinas, M., & Rossi, J. (2026). PPIPilot: Automating the suggestion and computation of Process Performance Indicators from event logs. Information Systems, 142, 102765-102765. https://doi.org/10.1016/j.is.2026.102765

- **Decision:** supporting — LLM pipeline suggesting and computing process performance indicators from event logs, with a fallback mechanism empirically shown to reduce computation failures.
- **Evidence:** full text not read (status: pending).

### Gardhouse, K., Oueslati, A., & Kolt, N. (2026). Regulating AI Agents. arXiv (Cornell University). https://arxiv.org/abs/2603.23471

- **Decision:** supporting [preprint] — Legal analysis of how the EU AI Act's monitoring and enforcement structures fail autonomous agents; contributes governance limitations relevant to RQ2.
- **Evidence:** full text not read (status: pending).

### Zhang, J., Dai, X., Li, Y., Wang, S., & Wan, S. (2026). Research and practice of LLM agent for human resource business of large enterprises. 40th Annual Conference on Chinese University Society for Electric Power System and Automation (CUS-EPSA 2025), 2025(55), 303-306. https://doi.org/10.1049/icp.2026.1225

- **Decision:** supporting — Indexing record only, no abstract; the title indicates a deployed enterprise HR LLM agent that warrants a landing-page check.
- **Evidence:** full text not read (status: pending).

### Ashinze, E. C. (2026). SafetyBuddy: A Multimodal LLM-Based Safety Intelligence Platform for Regulatory Compliance in Process Industries. SPE Nigeria Annual International Conference and Exhibition. https://doi.org/10.2118/234917-ms

- **Decision:** supporting — Multimodal LLM with RAG over OSHA rules automates safety compliance monitoring and auditing, with detector metrics from a deployed platform.
- **Evidence:** full text not read (status: pending).

### Chopra, J., Manohar, H. P., Yerram, M., & Parashar, J. (2026). Scalable Autogen Multi-Agent Framework for Data Quality Validation Using Azure Open AI. 2026 13th International Conference on Computing for Sustainable Global Development (INDIACom), 1-7. https://doi.org/10.23919/indiacom70271.2026.11526716

- **Decision:** supporting — Indexing record only, no abstract; the title indicates an AutoGen multi-agent LLM validation framework worth checking as a control mechanism.
- **Evidence:** full text not read (status: pending).

### Kim, D.-K. (2026). Towards Adaptive Test Automation: JSON DSLs and LLM Agents for End-to-End Testing. International JOURNAL OF CONTENTS, 22(1), 77-95. https://doi.org/10.5392/ijoc.2026.22.1.077

- **Decision:** supporting — Directly contrasts a declarative JSON DSL with deterministic execution against a free-planning LLM agent; the same specification-versus-instruction contrast as RQ1, in software testing.
- **Evidence:** full text not read (status: pending).

### Zhu, P., Li, L., Lyu, Y., Luo, Q., Jingyi, 杨. Y., Liu, Y. C., Hui, T., Yuan, X., Sun, L., Su, S., & Shao, J. (2026). UniACE: A Unified Framework for Evaluating LLM Agentic Capabilities. arXiv (Cornell University). https://arxiv.org/abs/2605.27898

- **Decision:** supporting [preprint] — Shows agent benchmark scores are properties of harness and environment configuration, with failure attribution; a methodological caution for RQ2 baseline comparisons.
- **Evidence:** full text not read (status: pending).

### Katragadda, S. R. (2026). Utilizing LLM models for advanced automation, manufacturing operations. Journal of Mechanical Civil and Industrial Engineering, 7(2), 08-14. https://doi.org/10.32996/jmcie.2026.7.2.1

- **Decision:** supporting — Proposes an LLM orchestration layer for manufacturing with human-in-the-loop governance and validation mechanisms, but reports no evaluation.
- **Evidence:** full text not read (status: pending).

### Brissard, A., Cuppens, F., & Zouaq, A. (2026). What is the Best Process Model Representation? A Comparative Analysis for Process Modeling with Large Language Models. Lecture Notes in Business Information Processing, 55-68. https://doi.org/10.1007/978-3-032-13426-4_5

- **Decision:** supporting — Compares process model representations for LLM process modelling, informing how an explicit process model should be encoded when binding an agent.
- **Evidence:** full text not read (status: pending).

### Lin, C.-H., & Fard, A. M. (2025). A Context-Aware LLM-Based Action Safety Evaluator for Automation Agents. Proceedings of the Canadian Conference on Artificial Intelligence. https://doi.org/10.21428/594757db.96a8c2ad

- **Decision:** supporting — Context-aware LLM safety evaluator that screens automation-agent actions before execution using read-only environmental feedback; an evaluated pre-execution control mechanism.
- **Evidence:** full text not read (status: pending).

### Martino, D., Perlangeli, C., Grottoli, B., La Rosa, L., & Pacella, M. (2025). A Knowledge-Driven Framework for AI-Augmented Business Process Management Systems: Bridging Explainability and Agile Knowledge Sharing. AI, 6(6), 110-110. https://doi.org/10.3390/ai6060110

- **Decision:** supporting — Framework for AI-augmented BPM systems combining XAI, process mining, and RPA over BPMN 2.0; supplies the ABPMS framing and explainability requirements for agentic BPM.
- **Evidence:** full text not read (status: pending).

### Wei, S., Liu, Y., & Yang, Y. (2025). A Multi-Agent Automation Framework Integrating RPA, OCR, and Large Language Models for Complex Workflow Execution. 2025 6th International Symposium on Computer Engineering and Intelligent Communications (ISCEIC), 833-836. https://doi.org/10.1109/isceic67854.2025.11405500

- **Decision:** supporting — Couples LLM planning with deterministic RPA execution and reports higher success rates than traditional RPA, an explicit hybrid control mechanism with a deterministic baseline.
- **Evidence:** full text not read (status: pending).

### Yüksel, K. A., Ferreira, T. C., Al-Badrashiny, M., & Sawaf, H. (2025). A Multi-AI Agent System for Autonomous Optimization of Agentic AI Solutions via Iterative Refinement and LLM-Driven Feedback Loops. https://doi.org/10.18653/v1/2025.realm-1.4

- **Decision:** supporting — Agentic pipeline that autonomously refines agent roles and tasks via LLM feedback loops; a configuration-optimization method adjacent to control-mechanism design.
- **Evidence:** full text not read (status: pending).

### Ray, P. P. (2025). A Review of TRiSM Frameworks in Artificial Intelligence Systems: Fundamentals, Taxonomy, Use Cases, Key Challenges and Future Directions. https://doi.org/10.36227/techrxiv.174913612.20443736/v1

- **Decision:** supporting [preprint] — Taxonomy of trust, risk and security controls for LLM systems including runtime enforcement and governance workflows across regulated domains.
- **Evidence:** full text not read (status: pending).

### Ray, P. P. (2025). A Review on Agent-to-Agent Protocol: Concept, State-of-the-art, Challenges and Future Directions. https://doi.org/10.36227/techrxiv.174612014.42157096/v1

- **Decision:** supporting [preprint] — Reviews the A2A protocol for auditable, task-driven agent interoperability in enterprise automation, a coordination-layer control surface.
- **Evidence:** full text not read (status: pending).

### Ray, P. P. (2025). A Survey on Model Context Protocol: Architecture, State-of-the-art, Challenges and Future Directions. https://doi.org/10.36227/techrxiv.174495492.22752319/v1

- **Decision:** supporting [preprint] — Surveys the MCP tool-invocation protocol and its fine-grained access control, a tool-layer constraint mechanism on agent behaviour.
- **Evidence:** full text not read (status: pending).

### Romero, M. L., & Suyama, R. (2025). Agentic AI for Intent-Based Industrial Automation. https://doi.org/10.1109/induscon66435.2025.11241317

- **Decision:** supporting — Decomposes natural-language intents into expectations, conditions and targets that constrain LLM sub-agents in an industrial automation proof of concept.
- **Evidence:** full text not read (status: pending).

### Olujimi, P. A., Owolawi, P. A., Mogase, R. C., & Van Wyk, E. (2025). Agentic AI Frameworks in SMMEs: A Systematic Literature Review of Ecosystemic Interconnected Agents. Preprints.org. https://doi.org/10.20944/preprints202504.1797.v1

- **Decision:** supporting [preprint] — PRISMA review of agentic AI frameworks for task automation in SMMEs; adjacent evidence on interconnected autonomous agents and adoption barriers.
- **Evidence:** full text not read (status: pending).

### Tomasino, A., Ieva, S., Loseto, G., Scioscia, F., Ruta, M., Ingianni, A., Minoia, M., & Genchi, G. (2025). Agentic Hyperautomation: A Distributed Architecture for Scalable AI-Driven Workflows. https://doi.org/10.1109/smc58881.2025.11343345

- **Decision:** supporting — LLM orchestrator dynamically planning and delegating to specialized tool-using agents, explicitly replacing pre-defined workflows, shown via a document-management case study.
- **Evidence:** full text not read (status: pending).

### Deng, S., Zhao, H., Wang, Z., Cheng, G., Chen, P., Qian, W., Ling, Z., Yin, J., Zomaya, A. Y., & Dustdar, S. (2025). Agentic Services Computing. arXiv (Cornell University). https://doi.org/10.34726/12000

- **Decision:** supporting [preprint] — Service-centred roadmap for engineering and governing autonomous agents so they can be composed, monitored, audited and evolved as accountable services.
- **Evidence:** full text not read (status: pending).

### Deng, Z., Guo, Y., Han, C., Ma, W., Xiong, J., Wen, S., & Xiang, Y. (2025). AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways. ACM Computing Surveys, 57(7), 1-36. https://doi.org/10.1145/3716628

- **Decision:** supporting — Survey of AI agent security threats naming unpredictable multi-step inputs and untrusted external entities as failure sources relevant to agent control design.
- **Evidence:** full text not read (status: pending).

### Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges. Information Fusion, 126(3), 103599-103599. https://doi.org/10.1016/j.inffus.2025.103599

- **Decision:** supporting — Widely cited taxonomy separating AI agents from agentic AI and cataloguing failure modes and mitigations; supplies scoping definitions and a mitigation inventory for RQ2.
- **Evidence:** full text not read (status: pending).

### Zhong, Z. (2025). AI-Assisted Workflow Optimization and Automation in the Compliance Technology Field. International Journal of Advanced Computer Science and Applications, 16(10). https://doi.org/10.14569/ijacsa.2025.0161001

- **Decision:** supporting — Proposes rule engine, RPA and semantic recognition to automate auxiliary compliance workflows, naming controls for compliance-critical processes.
- **Evidence:** full text not read (status: pending).

### Srinivas, S., Kirk, B., Zendejas, J., Espino, M., Boskovich, M., Bari, A., Dajani, K., & Alzahrani, N. (2025). AI-Augmented SOC: A Survey of LLMs and Agents for Security Automation. Journal of Cybersecurity and Privacy, 5(4), 95-95. https://doi.org/10.3390/jcp5040095

- **Decision:** supporting — Survey of LLMs and agents across security operations tasks with a capability-maturity model and limitations such as hallucination and leakage.
- **Evidence:** full text not read (status: pending).

### Akter, S., Akhter, S., Rahman, M. B., & Naidu, P. (2025). AI-DRIVEN BUSINESS ANALYTICS FOR COMPETITIVE ADVANTAGE IN SERVICE-ORIENTED ENTERPRISES: CUSTOMER EXPERIENCE AND EFFICIENCY. https://doi.org/10.63125/mx0k6019

- **Decision:** supporting — PRISMA review reporting that human-in-the-loop and override governance halve experience-efficiency trade-offs, an adjacent control-versus-performance result.
- **Evidence:** full text not read (status: pending).

### Nguyen, M. K., Tran, H.-N., Ober, I., & Abualsaud, R. (2025). An AI-augmented Framework for Automated and Intelligent Process Monitoring. https://doi.org/10.1145/3672608.3707831

- **Decision:** supporting — AI framework interpreting user actions into process-management-system progress updates, demonstrated in a manufacturing case study.
- **Evidence:** full text not read (status: pending).

### Ongwae, B., & Ekanem, U. I. (2025). An Industrial Application of a Large Language Model to Enhancing Asset Integrity and Process Safety Management. Journal of Artificial Intelligence, Virtual Reality, and Human-Centered Computing, 01(01), 01-13. https://doi.org/10.20944/preprints202503.1172.v1

- **Decision:** supporting — Comparative LNG-plant study of GPT-based classification for asset integrity and process safety; a compliance-adjacent deployment result with a manual baseline.
- **Evidence:** full text not read (status: pending).

### Herrera-Poyatos, D., Peláez-González, C., Zuheros, C., Herrera-Poyatos, A., Tejedor, V., Herrera, F., & Montes, R. (2025). An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability. Frontiers in Artificial Intelligence, 8, 1609097-1609097. https://doi.org/10.3389/frai.2025.1609097

- **Decision:** supporting — Documents LLM output variability, temperature sensitivity and prompt sensitivity; a named limitation explaining why natural-language instruction alone is unreliable.
- **Evidence:** full text not read (status: pending).

### Toxtli, C., & Li, W. (2025). Automating Automation: Using LLMs to Generate BPMN Workflows for Robotic Process Automation. Communications in computer and information science, 221-229. https://doi.org/10.1007/978-3-031-86623-4_18

- **Decision:** supporting — Zero-shot LLM generation of BPMN for RPA with an evaluation of GPT-4o; a method for producing the process models an agent could be bound to.
- **Evidence:** full text not read (status: pending).

### Sharma, A. (2025). Automating Software Release Notes with AI: A Comparative Study of Agent-Based Systems vs. LLM Fine-Tuning Approaches. International Scientific Journal of Engineering and Management, 04(11), 1-15. https://doi.org/10.55041/isjem05150

- **Decision:** supporting — Compares rule-driven agent systems with fine-tuned LLMs for release-note generation, an analogue of structured versus free-form automation.
- **Evidence:** full text not read (status: pending).

### Chakraborty, S. (2025). Beyond ETL: How AI Agents Are Building Self-Healing Data Pipelines. Journal of Computer Science and Technology Studies, 7(3), 741-756. https://doi.org/10.32996/jcsts.2025.7.3.81

- **Decision:** supporting — AI agents autonomously remediating ETL pipeline failures name autonomy and exception-handling mechanisms for an organizational data process, but report no controlled evaluation.
- **Evidence:** full text not read (status: pending).

### Pothireddy, S. R. (2025). Cloud-Native AI-Driven Enterprise Automation for Scalable Digital Process Transformation in Multi-Industry Ecosystems. Journal of Applied Sciences and Modelling, 1(1), 60-60. https://doi.org/10.71426/jasm.v1.i1.pp60-74

- **Decision:** supporting — Governance-aware compliance validation inside an agentic orchestration stack, evaluated on BPI Challenge event logs with compliance-satisfaction and latency results.
- **Evidence:** full text not read (status: pending).

### Zhao, D., Ma, L., Wang, S., Wang, M., & Lv, Z. (2025). COLA: Collaborative Multi-Agent Framework with Dynamic Task Scheduling for GUI Automation. https://doi.org/10.18653/v1/2025.emnlp-main.227

- **Decision:** supporting — Multi-agent GUI automation with dynamic scheduling and an interactive backtracking repair mechanism, benchmarked on GAIA and WindowsAgentArena for task completion.
- **Evidence:** full text not read (status: pending).

### Izzi, A., Mathew, J. G., Monti, F., Firmani, D., Leotta, F., Mandreoli, F., & Mecella, M. (2025). Data Service Composition in Cyber-Physical Systems Adopting LLMs. https://doi.org/10.1109/icws67624.2025.00085

- **Decision:** supporting — LLM synthesizes data-service composition pipelines, evaluated on BIRD and a real case study; an orchestration mechanism with empirical results but no compliance arm.
- **Evidence:** full text not read (status: pending).

### Drakopoulos, P., Malousoudis, P., Nousias, N., Tsakalidis, G., & Vergidis, K. (2025). Do LLMs Speak BPMN? An Evaluation of Their Process Modeling Capabilities Based on Quality Measures. https://doi.org/10.20944/preprints202509.2350.v1

- **Decision:** supporting [preprint] — Scores five LLM BPMN tools for correctness and completeness and documents modelling-rule violations, a usable benchmark of LLM adherence to process-model rules.
- **Evidence:** full text not read (status: pending).

### Paulose, R., Neelanath, V., & George, M. (2025). Domain Agnostic Agentic AI: Enabling Autonomous Automation with SmartGenie CoPilot. https://doi.org/10.1109/etis64005.2025.10961403

- **Decision:** supporting — Deployed agentic LLM copilot resolving employee service requests for a financial client, reporting completion-time and accuracy gains but no controlled baseline.
- **Evidence:** full text not read (status: pending).

### Jamili, L. K., Kulkarni, S. S., & Goel, E. O. (2025). Dynamic Agent Orchestration: Empowering Enterprise Automation with LLMs. Journal of Quantum Science and Technology., 2(2). https://doi.org/10.63345/jqst.v2i2.262

- **Decision:** supporting — Describes LLM-driven dynamic orchestration of enterprise agents with case studies claiming compliance and downtime improvements.
- **Evidence:** full text not read (status: pending).

### Li, Z., Hu, Y., & Wang, W. (2025). Encouraging Good Processes Without the Need for Good Answers: Reinforcement Learning for LLM Agent Planning. Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track, 1654-1666. https://doi.org/10.18653/v1/2025.emnlp-industry.116

- **Decision:** supporting — Decoupled RL on tool-use completeness improves agent planning; a method and task-completion evidence relevant to the completion side of RQ1.
- **Evidence:** full text not read (status: pending).

### Chen, X., Zhang, Y., Liu, H., Wang, X., Li, C., & Tu, B. (2025). End-to-End Security Policy Automation with Multi-LLM Agents in Cloud-Native Systems. 2025 IEEE 24th International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom), 175-183. https://doi.org/10.1109/trustcom66490.2025.00027

- **Decision:** supporting — Multi-LLM agents generate machine-enforceable Istio access-control policies, benchmarked on five systems with unit tests and attack simulations; policy-as-artifact control mechanism.
- **Evidence:** full text not read (status: pending).

### Nia, N. G., Amiri, A., Luo, Y., & Kline, A. (2025). Ethical perspectives on deployment of large language model agents in biomedicine: a survey. AI and Ethics, 6(1). https://doi.org/10.1007/s43681-025-00847-w

- **Decision:** supporting — Survey cataloguing mitigation mechanisms for LLM agents including guardrailing, red-teaming and post-deployment monitoring, and their weak accountability evidence.
- **Evidence:** full text not read (status: pending).

### Kourani, H., Berti, A., Schuster, D., & van der Aalst, W. M. P. (2025). Evaluating large language models on business process modeling: framework, benchmark, and self-improvement analysis. Software & Systems Modeling, 25(4), 1151-1186. https://doi.org/10.1007/s10270-025-01318-w

- **Decision:** supporting — Benchmark of 16 LLMs generating business process models with a quality evaluation framework; measures the model-generation side rather than policy enforcement.
- **Evidence:** full text not read (status: pending).

### Mohammadi, M., Li, Y., Lo, J. C., & Yip, W. (2025). Evaluation and Benchmarking of LLM Agents: A Survey. https://doi.org/10.1145/3711896.3736570

- **Decision:** supporting — Survey taxonomy of what and how to evaluate LLM agents, explicitly flagging enterprise reliability and compliance gaps; informs RQ2 baselines and metrics.
- **Evidence:** full text not read (status: pending).

### Pfeiffer, P., Rombach, A., Majlatow, M., & Mehdiyev, N. (2025). From Theory to Practice: Real-World Use Cases on Trustworthy LLM-Driven Process Modeling, Prediction and Automation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2506.03801

- **Decision:** supporting [preprint] — Four industrial LLM-BPM projects mapping transparency-versus-efficiency and human-agency-versus-automation trade-offs; strong framing for RQ2 but no controlled baseline comparison.
- **Evidence:** full text not read (status: pending).

### Lin, C., Tsai, T.-H., & Tseng, T.-L. (2025). Generative AI for Intelligent Manufacturing Virtual Assistants in the Semiconductor Industry. IEEE Robotics and Automation Letters, 10(4), 4132-4139. https://doi.org/10.1109/lra.2025.3544506

- **Decision:** supporting — Deployed LLM agent assistant for semiconductor yield and defect analysis integrated with existing manufacturing systems; industrial evidence without compliance controls.
- **Evidence:** full text not read (status: pending).

### Aluri, G. N. C., & Manohar, V. (2025). Generative AI Integration Patterns for Enterprise Workflow Automation: A Practitioner Framework. International Journal of Emerging Research in Engineering and Technology, 6(3), 165-172. https://doi.org/10.63282/3050-922x.ijeret-v6i3p121

- **Decision:** supporting — Practitioner integration framework with a human-in-the-loop governance layer and a four-tier autonomy taxonomy for enterprise GenAI workflows; a useful mechanism taxonomy.
- **Evidence:** full text not read (status: pending).

### Deng, X., Tao, G., Wen, C., Zhang, X., Ju, Z., & Gong, J. (2025). GMATP-LLM: A General Multi-Agent Task Dynamic Planning Method using Large Language Models. 2025 44th Chinese Control Conference (CCC), 5792-5798. https://doi.org/10.23919/ccc64809.2025.11179615

- **Decision:** supporting — Binds LLM chain-of-thought output to a PDDL model solved by a symbolic planner, the constrain-the-LLM mechanism class of RQ1, but in robotics rather than business processes.
- **Evidence:** full text not read (status: pending).

### Donde, N. (2025). GuardRails-as-Code and Audit Economics: Reducing Compliance Costs Through Policy Automation. Hampton Global Business Review. https://doi.org/10.70924/uv4px7jt//qfh0iaoc

- **Decision:** supporting — Policy-as-code and compliance-as-code guardrails enforced in pipelines give continuous verifiable assurance; the machine-checkable policy alternative to natural-language rules.
- **Evidence:** full text not read (status: pending).

### Madireddy, S., Gao, L., Din, Z. U., Kim, K., Senouci, A., Han, Z., & Zhang, Y. (2025). Large Language Model-Driven Code Compliance Checking in Building Information Modeling. Electronics, 14(11), 2146-2146. https://doi.org/10.3390/electronics14112146

- **Decision:** supporting — LLMs interpret codified regulations and generate scripted checks that flag violations in BIM; an automated compliance-verification mechanism transferable to process conformance.
- **Evidence:** full text not read (status: pending).

### Schinckus, M., Simonofski, A., & Rosselló, N. B. (2025). Large Language Models for Process Knowledge Acquisition. Business & Information Systems Engineering, 68(1), 7-33. https://doi.org/10.1007/s12599-025-00976-w

- **Decision:** supporting — Empirically evaluated LLM multi-agent system for process knowledge acquisition; method and quasi-experiment for agents applied to BPM, not policy enforcement.
- **Evidence:** full text not read (status: pending).

### Wenger, S., Spahic-Bogdanovic, M., & Martin, A. (2025). Large Language Models for Democratizing Business Process Modeling: BPMN Model Generation and Style Guide Adherence. Communications in Computer and Information Science, 372-389. https://doi.org/10.1007/978-3-031-78255-8_22

- **Decision:** supporting — Measures LLM-generated BPMN against style-guide rules, giving a method for scoring adherence of model output to explicit modelling constraints.
- **Evidence:** full text not read (status: pending).

### Gill, M. S., Vyas, J., Markaj, A., Gehlhoff, F., & Mercangöz, M. (2025). Leveraging LLM Agents and Digital Twins for Fault Handling in Process Plants. 2025 IEEE 30th International Conference on Emerging Technologies and Factory Automation (ETFA), 1-8. https://doi.org/10.1109/etfa65518.2025.11205597

- **Decision:** supporting — LLM agents prompted from a Digital Twin that also validates generated corrective actions before execution; a verification-before-action control in a plant, not a business process.
- **Evidence:** full text not read (status: pending).

### Podpora, M., Baranowski, M., Chopcian, M., Kwasniewicz, L., & Radziewicz, W. (2025). LLM Firewall Using Validator Agent for Prevention Against Prompt Injection Attacks. Applied Sciences, 16(1), 85-85. https://doi.org/10.3390/app16010085

- **Decision:** supporting — Validator agent acting as an output firewall performing policy-compliance verification and redaction; a named runtime guardrail with only viability-level evidence.
- **Evidence:** full text not read (status: pending).

### Wen, T. (2025). LLM-Driven Agentic AI Multi-Agent Workflow for Visual Design within the Double Diamond Model: Framework and Prototype System. 2025 International Conference on Machine Learning, Computational Intelligence and Pattern Recognition (MLCIPR), 245-251. https://doi.org/10.1109/mlcipr68329.2025.11407347

- **Decision:** supporting — Structured stage-bound agent workflow beats freeform prompting on process controllability at a time and load cost; adjacent structure-versus-freeform evidence outside a compliance domain.
- **Evidence:** full text not read (status: pending).

### Bianchini, D., Garda, M., Melchiori, M., & Rula, A. (2025). LLM-driven Data Service Discovery in the Internet of Production. https://doi.org/10.1109/compsac65507.2025.00073

- **Decision:** supporting — RAG over a catalogue of atomic data services constrains LLM pipeline design, with preliminary smart-factory case-study evaluation.
- **Evidence:** full text not read (status: pending).

### Huang, X., Li, Q., Zhu, C., Zhu, X., Zang, Y., Chen, T., & Zhang, S. (2025). LMW: LLM-Driven Multi-Agent Workflow for Unmanned Platforms. 2025 IEEE International Conference on Systems, Man, and Cybernetics (SMC), 2752-2758. https://doi.org/10.1109/smc58881.2025.11343649

- **Decision:** supporting — Node-structured agent workflow with knowledge injection to curb cumulative hallucination, benchmarked against LLM agent baselines; adjacent evidence that workflow structure improves reliability.
- **Evidence:** full text not read (status: pending).

### Wang, Y., & Yang, X. (2025). Machine Learning-Based Cloud Computing Compliance Process Automation. Automation and Machine Learning, 6(1). https://doi.org/10.23977/autml.2025.060105

- **Decision:** supporting — Machine-learning compliance automation deployed at a securities firm reports cycle-time and accuracy gains, a non-agentic compliance-checking baseline.
- **Evidence:** full text not read (status: pending).

### Jing, H., Li, H., Hu, W., Hu, Q., Heli, X., Chu, T., Hu, P., & Song, Y. (2025). MCIP: Protecting MCP Safety via Model Contextual Integrity Protocol. https://doi.org/10.18653/v1/2025.emnlp-main.62

- **Decision:** supporting — Protocol-level integrity control for tool-using LLM agents, with an unsafe-behavior taxonomy plus benchmark and training data showing measurable safety gains.
- **Evidence:** full text not read (status: pending).

### Chirumamilla, K. R. (2025). Multi-Agent AI Assistant for Real-Time Business Insights. Journal of recent trends in computer science and engineering., 13(3), 17-36. https://doi.org/10.70589/jrtcse.2025.13.3.3

- **Decision:** supporting — Multi-agent LLM assistant producing policy-aware recommendations over enterprise event streams through structured message passing.
- **Evidence:** full text not read (status: pending).

### Venkiteela, P. (2025). n8n- An Open-Source Workflow Automation for Enterprise Integration and AI Orchestration. International Journal of Computer Applications, 187(63), 1-11. https://doi.org/10.5120/ijca2025926031

- **Decision:** supporting — Benchmarks n8n's deterministic workflow orchestration with AI steps, giving reliability and scalability figures for the orchestration baseline.
- **Evidence:** full text not read (status: pending).

### Rebmann, A., Schmidt, F. D., Glavaš, G., & van der Aa, H. (2025). On the potential of large language models to solve semantics-aware process mining tasks. Process Science, 2(1). https://doi.org/10.1007/s44311-025-00019-3

- **Decision:** supporting — Benchmarks LLMs on five semantics-aware process-mining tasks, showing out-of-the-box and in-context use fails where fine-tuning succeeds.
- **Evidence:** full text not read (status: pending).

### de Witt, C. S., Krawiecka, K., Krawczuk, I., Hagag, B., Anderson, W. L., Belcak, P., Bucknall, B., Cai, X., Chopra, A., Cohen, D., Del Rosario, R. F., Draguns, A., Gray, A., Katz, K., Mavroudis, V., Mink, J., Motwani, S. R., Petit, J., Rembeck, L.-S., ... Llewellyn, M. (2025). Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2505.02077

- **Decision:** supporting [preprint] — Defines multi-agent security threats and security-utility trade-offs across interacting agents; a governance and risk framing adjacent to agentic process control.
- **Evidence:** full text not read (status: pending).

### Berti, A., Kourani, H., & van der Aalst, W. M. P. (2025). PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining Tasks. Lecture notes in business information processing, 610-623. https://doi.org/10.1007/978-3-031-82225-4_45

- **Decision:** supporting — PM-LLM-Benchmark evaluates LLMs on process mining tasks and discusses evaluation bias; a benchmark method for LLMs over process artefacts.
- **Evidence:** full text not read (status: pending).

### Hu, J., Dong, Y., Ao, S., Li, Z., Wang, B., Singh, L., Cheng, G., Ramchurn, S. D., & Huang, X. (2025). Position: Towards a Responsible LLM-empowered Multi-Agent Systems. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2502.01714

- **Decision:** supporting [preprint] — Position paper arguing for active dynamic moderation and human-centred governance to contain compounding uncertainty in LLM multi-agent systems.
- **Evidence:** full text not read (status: pending).

### Du, H., Su, J.-D., Li, J., Ding, L.-Y., Yang, Y., Han, P., Tang, X., Zhu, K., & You, J. (2025). ProtocolBench: Which LLM MultiAgent Protocol to Choose?. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2510.17149

- **Decision:** supporting [preprint] — Benchmarks multi-agent communication protocols on task success, latency and failure recovery against single-protocol baselines; an evaluated coordination control at the infrastructure layer.
- **Evidence:** full text not read (status: pending).

### Vogt, M. W., van der Putten, P., & Reijers, H. A. (2025). Providing Domain Knowledge for Process Mining with ReWOO-Based Agents. Lecture notes in business information processing, 663-676. https://doi.org/10.1007/978-3-031-82225-4_49

- **Decision:** supporting — Proof-of-concept ReWOO agent injecting domain knowledge into process mining tool interactions across several business processes.
- **Evidence:** full text not read (status: pending).

### Pettinari, S., De Sanctis, M., & Inverardi, P. (2025). Realizing Ethical-Aware Business Processes. Lecture notes in computer science, 219-235. https://doi.org/10.1007/978-3-032-11108-1_16

- **Decision:** supporting — Positions autonomous systems guided by a process model and the monitoring needed to uphold obligations, framing the process-model-binding side of RQ1.
- **Evidence:** full text not read (status: pending).

### Kumar, P., Al Mazrouei, B. S., Fayyaz, M., Jan, S. A., & Al Maysari, J. (2025). Realizing the Need for Agentic AI for Subsurface Data and Workflows. https://doi.org/10.2118/229586-ms

- **Decision:** supporting — Industrial deployment of agentic AI over subsurface business workflows with data quality checks; a deployment case study without policy-control evaluation.
- **Evidence:** full text not read (status: pending).

### He, P., Lin, Y., Dong, S., Xu, H., Xing, Y., & Liu, H. (2025). Red-Teaming LLM Multi-Agent Systems via Communication Attacks. https://doi.org/10.18653/v1/2025.findings-acl.349

- **Decision:** supporting — Shows inter-agent message manipulation compromises LLM multi-agent systems, a threat model relevant to controlling agent communication.
- **Evidence:** full text not read (status: pending).

### Constantinescu, M., & Kaptein, M. (2025). Responsibility Gaps, LLMs & Organisations: Many Agents, Many Levels, and Many Interactions. Science and Engineering Ethics, 31(6), 36-36. https://doi.org/10.1007/s11948-025-00560-1

- **Decision:** supporting — Proposes the M3 approach for distributing responsibility across many agents and levels in LLM-deploying organisations; accountability limitation relevant to RQ2.
- **Evidence:** full text not read (status: pending).

### Neelapu, M. (2025). Retail QA Automation Framework for LLM-Generated UX: Testing Conversational  Commerce Interfaces for Compliance, Clarity, and Consistency. International Journal of Innovative Research in Engineering &amp; Multidisciplinary Physical Sciences, 13(6). https://doi.org/10.37082/ijirmps.v13.i6.232852

- **Decision:** supporting — Automated pipeline scoring LLM retail dialogue for policy adherence with violation analysis; an empirical compliance-measurement method in a business setting.
- **Evidence:** full text not read (status: pending).

### Blašković, L., Tanković, N., Lorencin, I., & Šegota, S. B. (2025). Robust Clinical Querying with Local LLMs: Lexical Challenges in NL2SQL and Retrieval-Augmented QA on EHRs. Big Data and Cognitive Computing, 9(10), 256-256. https://doi.org/10.3390/bdcc9100256

- **Decision:** supporting — Multi-model NL2SQL and RAG benchmark with a deterministic error-classification framework and cost analysis; adjacent evaluation method rather than process-agent control.
- **Evidence:** full text not read (status: pending).

### Chaudhary, A. (2025). Securing AI Integration in Business Process Automation for Compliance and Risk Management. 2025 IEEE 1st International Conference on Recent Trends in Computing and Smart Mobility (RCSM), 1-5. https://doi.org/10.1109/rcsm67767.2025.11507748

- **Decision:** supporting — Survey-based empirical study of compliance and security risk perceptions when AI is embedded in business process automation.
- **Evidence:** full text not read (status: pending).

### Wang, Y., Pan, Y., Guo, S., & Su, Z. (2025). Security of Internet of Agents: Attacks and Countermeasures. IEEE Open Journal of the Computer Society, 6, 1611-1624. https://doi.org/10.1109/ojcs.2025.3589638

- **Decision:** supporting — Survey of attacks and defence mechanisms for interacting LLM agents; adjacent control and trust mechanisms, not process compliance.
- **Evidence:** full text not read (status: pending).

### Sovrano, F., Hine, E., Anzolut, S., & Bacchelli, A. (2025). Simplifying software compliance: AI technologies in drafting technical documentation for the AI Act. Empirical Software Engineering, 30(4), 91-91. https://doi.org/10.1007/s10664-025-10645-x

- **Decision:** supporting — Empirically compares ChatGPT and DoXpert against legal expert judgments for AI Act documentation gaps; a compliance-checking method with a human baseline.
- **Evidence:** full text not read (status: pending).

### Moshkovich, D., & Zeltyn, S. (2025). Taming Uncertainty via Automation: Observing, Analyzing, and Optimizing Agentic AI Systems. arXiv (Cornell University), 3840-3844. https://doi.org/10.1109/ase63991.2025.00327

- **Decision:** supporting [preprint] — AgentOps pipeline for observing and controlling agentic systems whose fluid execution paths create uncertainty; frames runtime control and issue detection without evaluation.
- **Evidence:** full text not read (status: pending).

### Bandi, A., Kongari, B., Naguru, R., Pasnoor, S., & Vilipala, S. V. (2025). The Rise of Agentic AI: A Review of Definitions, Frameworks, Architectures, Applications, Evaluation Metrics, and Challenges. Future Internet, 17(9), 404-404. https://doi.org/10.3390/fi17090404

- **Decision:** supporting — Reviews 143 agentic AI studies and classifies architectures and evaluation metrics, useful for mapping candidate control mechanisms for RQ2.
- **Evidence:** full text not read (status: pending).

### Di Maggio, L. G. (2025). Toward Autonomous LLM-Based AI Agents for Predictive Maintenance: State of the Art, Challenges, and Future Perspectives. Applied Sciences, 15(21), 11515-11515. https://doi.org/10.3390/app152111515

- **Decision:** supporting — Review of LLM agents across the predictive-maintenance lifecycle; ties higher autonomy to needs for governance, benchmarks and safety evidence.
- **Evidence:** full text not read (status: pending).

### Schulte, M., Franzoi, S., Köhne, F., & Brocke, J. V. (2025). Toward LLM-enabled business process coherence checking based on multi-level process documentation. Process Science, 2(1). https://doi.org/10.1007/s44311-025-00024-6

- **Decision:** supporting — LLM-based coherence checking that detects incoherencies across multi-level process documentation, an adjacent automated checking mechanism validated with practitioners.
- **Evidence:** full text not read (status: pending).

### Ismail, I., Kurnia, R., Brata, Z. A., Nelistiani, G. A., Heo, S., Kim, H., & Kim, H. (2025). Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence. Information, 16(5), 365-365. https://doi.org/10.3390/info16050365

- **Decision:** supporting — Replaces rigid SOAR playbooks with agentic LLM code generation plus an explicit validation stage, a structured-versus-generative control trade-off.
- **Evidence:** full text not read (status: pending).

### Sun, S., Zhao, L., Deng, M., & Fu, X. (2025). VTS-LLM: Domain-Adaptive LLM Agent for Enhancing Awareness in Vessel Traffic Services Through Natural Language. 2025 IEEE 28th International Conference on Intelligent Transportation Systems (ITSC), 935-942. https://doi.org/10.1109/itsc60802.2025.11423850

- **Decision:** supporting — LLM agent for regulated vessel traffic services showing that linguistic style variation systematically degrades performance, evidence on natural-language instruction sensitivity.
- **Evidence:** full text not read (status: pending).

### De Nicola, A., Formica, A., Mele, I., Missikoff, M., & Taglino, F. (2024). A comparative study of LLMs and NLP approaches for supporting business process analysis. Enterprise Information Systems, 18(10). https://doi.org/10.1080/17517575.2024.2415578

- **Decision:** supporting — Empirical comparison of LLM and NLP extraction of business process knowledge elements; enriched prompts outperform, quantifying prompt effects.
- **Evidence:** full text not read (status: pending).

### Zhang, J., Xiang, J., Yu, Z., Teng, F., Chen, X., Chen, J., Zhuge, M., Cheng, X., Hong, S., Wang, J., Zheng, B., Liu, B., Luo, Y., & Wu, C. (2024). AFlow: Automating Agentic Workflow Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2410.10762

- **Decision:** supporting [preprint] — Automates agentic workflow generation by Monte Carlo tree search over code-represented workflows with benchmark gains; adjacent workflow-structure control method.
- **Evidence:** full text not read (status: pending).

### Nabben, K. (2024). AI as a constituted system: accountability lessons from an LLM experiment. Data & Policy, 6. https://doi.org/10.1017/dap.2024.58

- **Decision:** supporting — Ethnographic study of governing an organizational LLM deployment via policy creation, responsibility lines, and feedback loops; named governance mechanisms without a baseline.
- **Evidence:** full text not read (status: pending).

### -, K. V. (2024). AI-Enhanced Business Process Automation: Integrating BPMN, DMN, and CMMN Standards for Enterprise Excellence. International Journal For Multidisciplinary Research, 6(6). https://doi.org/10.36948/ijfmr.2024.v06i06.31359

- **Decision:** supporting — Argues for coupling AI decision-making to BPMN, DMN and CMMN process standards, the artifact class RQ1 tests, but reports no controlled evaluation.
- **Evidence:** full text not read (status: pending).

### LI, H. (2024). AI-Powered Negotiations: Opportunities, Challenges, and the Future of Business Strategy. Transactions on Economics Business and Management Research, 13, 148-154. https://doi.org/10.62051/dg1trh68

- **Decision:** supporting — Case-study exploration of LLM negotiation agents in procurement and hiring that stresses required human oversight; adjacent evidence on autonomy limits.
- **Evidence:** full text not read (status: pending).

### Jin, W., Chen, H., Wang, X., Gong, B., & Lin, X. (2024). An AI-native application assemble platform for easy-integrating of AIGC based services. https://doi.org/10.1145/3718751.3718843

- **Decision:** supporting — Enterprise AI-native SaaS platform combining LLMs, multi-agent systems, and abstracted business processes; adjacent orchestration architecture for enterprise workflows.
- **Evidence:** full text not read (status: pending).

### Waseem, M., Das, T., Paloniemi, T., Koivisto, M., Räsänen, E., Setälä, M., & Mikkonen, T. (2024). Artificial Intelligence Procurement Assistant: Enhancing Bid Evaluation. Lecture notes in business information processing, 108-114. https://doi.org/10.1007/978-3-031-53227-6_8

- **Decision:** supporting — Industry-developed LLM agent assistant for procurement bid evaluation with usability and real-world testing; deployed case study of agentic support in an organizational process.
- **Evidence:** full text not read (status: pending).

### Qiao, S., Fang, R., Qiu, Z., Wang, X., Zhang, N., Jiang, Y., Xie, P., Huang, F., & Chen, H. (2024). Benchmarking Agentic Workflow Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2410.07869

- **Decision:** supporting [preprint] — WorfBench and WorfEval measure how well agents generate graph-structured workflows; a benchmark for structured process representation, not for compliance.
- **Evidence:** full text not read (status: pending).

### Arslan, M., Munawar, S., & Cruz, C. (2024). Business insights using RAG–LLMs: a review and case study. Journal of Decision System, 1-30. https://doi.org/10.1080/12460125.2024.2410040

- **Decision:** supporting — Review plus case study where retrieval augmentation grounds LLM extraction in business documents, an adjacent accuracy-control mechanism without compliance or process-model evaluation.
- **Evidence:** full text not read (status: pending).

### Kurz, A. F., Kampik, T., Pufahl, L., & Weber, I. (2024). Business process improvement with AB testing and reinforcement learning: grounded theory-based industry perspectives. Software & Systems Modeling, 24(1), 87-109. https://doi.org/10.1007/s10270-024-01229-2

- **Decision:** supporting — Grounded-theory industry study of AB testing and RL for process improvement; finds expert control over autonomous production experiments necessary.
- **Evidence:** full text not read (status: pending).

### Cinkusz, K., Chudziak, J. A., & Niewiadomska‐Szynkiewicz, E. (2024). Cognitive Agents Powered by Large Language Models for Agile Software Project Management. Electronics, 14(1), 87-87. https://doi.org/10.3390/electronics14010087

- **Decision:** supporting — LLM cognitive agents embedded in SAFe roles and simulated, reporting task completion and quality gains; adjacent empirical result on process-framework-bound agents.
- **Evidence:** full text not read (status: pending).

### Casciani, A., Bernardi, M. L., Cimitile, M., & Marrella, A. (2024). Conversational Systems for AI-Augmented Business Process Management. Lecture notes in business information processing, 183-200. https://doi.org/10.1007/978-3-031-59465-6_12

- **Decision:** supporting — Conversational systems for AI-augmented BPM systems that autonomously unfold and adapt process execution; conceptual grounding for agentic process control with human interaction.
- **Evidence:** full text not read (status: pending).

### Xia, C., Xing, C., Du, J., Yang, X., Feng, Y., Xu, R., Yin, W., & Xiong, C. (2024). FOFO: A Benchmark to Evaluate LLMs’ Format-Following Capability. https://doi.org/10.18653/v1/2024.acl-long.40

- **Decision:** supporting — Benchmark measuring how reliably LLMs follow format instructions; adjacent method for quantifying natural-language instruction adherence, the RQ1 comparison arm.
- **Evidence:** full text not read (status: pending).

### Cherukuri, R., & Yarram, V. K. (2024). From Intelligent Automation to Agentic AI: Engineering the Next Generation of Enterprise Systems. International Journal of Emerging Research in Engineering and Technology, 5. https://doi.org/10.63282/3050-922x.ijeret-v5i4p114

- **Decision:** supporting — Reference architecture for agentic enterprise systems with autonomy and governance dimensions, AgentOps controls, and claimed gains over conventional intelligent automation.
- **Evidence:** full text not read (status: pending).

### Hörner, L. F., & Reichert, M. (2024). Generating Process Models by Interacting with Chatbots—A Literature Review. Future Internet, 16(10), 353-353. https://doi.org/10.3390/fi16100353

- **Decision:** supporting — Review of chatbot-driven process model generation, mapping the natural-language to process-model interface that RQ1 depends on.
- **Evidence:** full text not read (status: pending).

### Xu, W., Huang, Z., Hu, W., Fang, X., Cherukuri, R., Nayyar, N., Malandri, L., & Sengamedu, S. (2024). HR-MultiWOZ: A Task Oriented Dialogue (TOD) Dataset for HR LLM Agent. Proceedings of the First Workshop on Natural Language Processing for Human Resources (NLP4HR 2024), 59-72. https://doi.org/10.18653/v1/2024.nlp4hr-1.5

- **Decision:** supporting — Task-oriented dialogue dataset for HR LLM agents supplies a benchmark for agent task completion in an organizational process, though the record carries no substantive abstract.
- **Evidence:** full text not read (status: pending).

### Zhan, Q., Liang, Z., Ying, Z., & Kang, D. (2024). InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents. https://doi.org/10.18653/v1/2024.findings-acl.624

- **Decision:** supporting — Benchmark of indirect prompt injection over 30 tool-using agents; quantifies instruction-following failure as a reliability limitation.
- **Evidence:** full text not read (status: pending).

### Allam, H. (2024). Intelligent Automation: Leveraging LLMs in DevOps Toolchains. International Journal of AI BigData Computational and Management Studies, 5, 81-94. https://doi.org/10.63282/3050-9416.ijaibdcms-v5i4p109

- **Decision:** supporting — LLM automation across DevOps toolchains with a CI/CD case study reporting reduced manual intervention; adjacent deployed process-automation evidence.
- **Evidence:** full text not read (status: pending).

### Yang, Y., Peng, Q., Wang, J., Wen, Y., & Zhang, W. (2024). LLM-based Multi-Agent Systems: Techniques and Business Perspectives. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2411.14033

- **Decision:** supporting [preprint] — Frames operational processes as LLM multi-agent systems and proposes a protocol covering data privacy and incentives; an architectural and governance contribution.
- **Evidence:** full text not read (status: pending).

### Pasquadibisceglie, V., Appice, A., & Malerba, D. (2024). LUPIN: A LLM Approach for Activity Suffix Prediction in Business Process Event Logs. 2024 6th International Conference on Process Mining (ICPM), 1-8. https://doi.org/10.1109/icpm63005.2024.10680620

- **Decision:** supporting — Fine-tuned LLM predicting activity suffixes from event logs with integrated-gradient explanations; adjacent LLM-in-BPM empirical result rather than agent control.
- **Evidence:** full text not read (status: pending).

### Agarwal, P., Dave, H., Bandlamudi, J., Sindhgatta, R., & Mukherjee, K. (2024). Multi-Stage Prompting for Next Best Agent Recommendations in Adaptive Workflows. Proceedings of the AAAI Conference on Artificial Intelligence, 38(21), 22843-22849. https://doi.org/10.1609/aaai.v38i21.30319

- **Decision:** supporting — Uses LLM prompting over encoded process knowledge and agent metadata to recommend next steps in adaptive business workflows.
- **Evidence:** full text not read (status: pending).

### Chaleshtori, F. H., Ghosal, A., Gill, A., Bambroo, P., & Marasović, A. (2024). On Evaluating Explanation Utility for Human-AI Decision Making in NLP. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2407.03545

- **Decision:** supporting [preprint] — Application-grounded human-AI study on contract verification finds explanations add no speed gain and argues for automated deferral; adjacent human-in-loop control evidence.
- **Evidence:** full text not read (status: pending).

### Mukherjee, S., Gamble, P., Ausin, M. S., Kant, N., Aggarwal, K., Manjunath, N., Datta, D., Liu, Z., Ding, J., Busacca, S., Bianco, C., Sharma, S., Lasko, R., Voisard, M., Harneja, S., Filippova, D., Meixiong, G., Cha, K., Youssefi, A., ... Miller, A. (2024). Polaris: A Safety-focused LLM Constellation Architecture for Healthcare. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2403.13313

- **Decision:** supporting [preprint] — Multi-agent LLM constellation using specialist support agents for safety, with clinical evaluation; adjacent empirical safety-control architecture in a regulated domain.
- **Evidence:** full text not read (status: pending).

### Tripathi, A., Jadhav, S., Singh, S., Nandan, S. K., Vyas, R., & Vyas, O. P. (2024). ProM-Ex: An Explainable Framework for Anomaly Detection in Process Mining Using Large Language Models. https://doi.org/10.1109/cict64037.2024.10899435

- **Decision:** supporting — LLM-explained control-flow anomaly detection on BPI event logs; a deviation-detection mechanism with empirical evaluation adjacent to conformance checking.
- **Evidence:** full text not read (status: pending).

### Zhao, H., Liu, Z., Wu, Z., Li, Y., Yang, T., Shu, P., Xu, S., Dai, H., Zhao, L., Jiang, H., Pan, Y., Chen, J., Zhou, Y., Zhang, Z., Zhang, Z., Sun, R., Mai, G., Liu, N., & Tian-ming, L. (2024). Revolutionizing Finance with LLMs: An Overview of Applications and Insights. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2401.11641

- **Decision:** supporting [preprint] — Reports that GPT-4 follows natural-language prompt instructions across financial tasks, an adjacent empirical result for the natural-language instruction arm of RQ1.
- **Evidence:** full text not read (status: pending).

### Cuconasu, F., Trappolini, G., Siciliano, F., Filice, S., Campagnano, C., Maarek, Y., Tonellotto, N., & Silvestri, F. (2024). The Power of Noise: Redefining Retrieval for RAG Systems. https://doi.org/10.1145/3626772.3657834

- **Decision:** supporting — Empirical study of how retrieved context relevance and noise change LLM accuracy; a limitation for grounding policy text in prompts.
- **Evidence:** full text not read (status: pending).

### Lu, Q., Zhu, L., Xu, X., Xing, Z., Harrer, S., & Whittle, J. (2024). Towards Responsible Generative AI: A Reference Architecture for Designing Foundation Model Based Agents. https://doi.org/10.1109/icsa-c63560.2024.00028

- **Decision:** supporting — Pattern-oriented reference architecture for foundation-model agents covering accountability and security, validated by mapping to two real agents.
- **Evidence:** full text not read (status: pending).

### Zhou, R., Yang, Y., Wen, M., Wen, Y., Wang, W., Xi, C., Xu, G., Yu, Y., & Zhang, W. (2024). TRAD: Enhancing LLM Agents with Step-Wise Thought Retrieval and Aligned Decision. https://doi.org/10.1145/3626772.3657788

- **Decision:** supporting — Step-level thought retrieval improving LLM agent decisions, evaluated on ALFWorld and Mind2Web; adjacent agent-control method with benchmark evidence.
- **Evidence:** full text not read (status: pending).

### Feretzakis, G., & Verykios, V. S. (2024). Trustworthy AI: Securing Sensitive Data in Large Language Models. AI, 5(4), 2773-2800. https://doi.org/10.3390/ai5040134

- **Decision:** supporting — RBAC/ABAC adaptive output control is a policy-binding constraint mechanism for LLMs, but it governs data disclosure rather than process conformance and is explicitly untested.
- **Evidence:** full text not read (status: pending).

### Dumas, M., Fournier, F., Limonad, L., Marrella, A., Montali, M., Rehse, J.-R., Accorsi, R., Calvanese, D., De Giacomo, G., Fahland, D., Gal, A., La Rosa, M., Völzer, H., & Weber, I. (2023). AI-augmented Business Process Management Systems: A Research Manifesto. ACM Transactions on Management Information Systems, 14(1), 1-19. https://doi.org/10.1145/3576047

- **Decision:** supporting — Manifesto defining AI-augmented BPM systems and their lifecycle, adaptability, and explainability challenges; frames the control agenda underlying RQ2.
- **Evidence:** full text not read (status: pending).

### Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiāng, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., & Wang, C. (2023). AIKernel Semantic DSL Compiler and Deterministic Agent Execution Architecture. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2308.08155

- **Decision:** supporting [preprint] — Abstract describes the AutoGen multi-agent framework, where conversation patterns are programmed in natural language or code with human and tool steps.
- **Evidence:** full text not read (status: pending).

### Mökander, J., Schuett, J., Kirk, H. R., & Floridi, L. (2023). Auditing large language models: a three-layered approach. AI and Ethics, 4(4), 1085-1115. https://doi.org/10.1007/s43681-023-00289-2

- **Decision:** supporting — Proposes a three-layered governance, model, and application audit procedure for LLMs; a named accountability mechanism relevant to RQ2's control landscape.
- **Evidence:** full text not read (status: pending).

### Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2303.17760

- **Decision:** supporting [preprint] — Role-playing and inception prompting keep cooperating LLM agents aligned with human intent; foundational prompting-level control for multi-agent instruction following.
- **Evidence:** full text not read (status: pending).

### Tian, L., He, Z., Jiao, W., Wang, X., Wang, Y., Wang, R., Yang, Y., Shi, S., & Tu, Z. (2023). Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2305.19118

- **Decision:** supporting [preprint] — Multi-agent debate with a judge as a generic reliability control for LLM reasoning, evaluated against self-reflection baselines on two datasets.
- **Evidence:** full text not read (status: pending).

### Saka, A. B., Taiwo, R., Saka, N., Salami, B. A., Ajayi, S., Akande, K. O., & Kazemi, H. (2023). GPT models in construction industry: Opportunities, limitations, and a use case validation. Developments in the Built Environment, 17, 100300-100300. https://doi.org/10.1016/j.dibe.2023.100300

- **Decision:** supporting — Critical review with use-case validation documenting GPT opportunities and limitations across a construction project lifecycle; adjacent evidence on LLM limits in an organizational process.
- **Evidence:** full text not read (status: pending).

### Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I. (2023). Improving Factuality and Reasoning in Language Models through Multiagent Debate. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2305.14325

- **Decision:** supporting [preprint] — Multi-agent debate as a reliability control mechanism evaluated against single-model baselines, though on reasoning tasks rather than business processes.
- **Evidence:** full text not read (status: pending).

### Wu, J., Xue, X., & Zhang, J. (2023). Invariant Signature, Logic Reasoning, and Semantic Natural Language Processing (NLP)-Based Automated Building Code Compliance Checking (I-SNACC) Framework. Journal of Information Technology in Construction, 28, 1-18. https://doi.org/10.36680/j.itcon.2023.001

- **Decision:** supporting — Empirical automated building-code compliance checking via logic reasoning and NLP (95.2% precision) supplies a deterministic rule-checking baseline, though no LLM agent is involved.
- **Evidence:** full text not read (status: pending).

### Vidgof, M., Bachhofner, S., & Mendling, J. (2023). Large Language Models for Business Process Management: Opportunities and Challenges. Lecture Notes in Business Information Processing, 107-123. https://doi.org/10.1007/978-3-031-41623-1_7

- **Decision:** supporting — Agenda-setting paper on opportunities and challenges of large language models across the BPM lifecycle, framing the mechanisms this review catalogues.
- **Evidence:** full text not read (status: pending).

### Sänger, M., De Mecquenem, N., Lewińska, K. E., Bountris, V., Lehmann, F., Leser, U., & Kosch, T. (2023). Large Language Models to the Rescue: Reducing the Complexity in Scientific Workflow Development Using ChatGPT. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2311.01825

- **Decision:** supporting [preprint] — User studies of ChatGPT comprehending, adapting, and extending explicit scientific workflows, with characterized failure modes on component exchange.
- **Evidence:** full text not read (status: pending).

### Berti, A., & Qafari, M. S. (2023). Leveraging Large Language Models (LLMs) for Process Mining (Technical Report). arXiv (Cornell University). https://doi.org/10.48550/arxiv.2307.12701

- **Decision:** supporting [preprint] — Empirical assessment of prompting strategies for LLM interpretation of declarative and procedural process models with GPT-4 and Bard.
- **Evidence:** full text not read (status: pending).

### Tsao, W.-K. (2023). Multi-Agent Reasoning with Large Language Models for Effective Corporate Planning. https://doi.org/10.1109/csci62032.2023.00065

- **Decision:** supporting — LLM multi-agent reasoning staged across a five-step corporate sales planning process; adjacent evidence on agents executing a predefined process sequence.
- **Evidence:** full text not read (status: pending).

### Cámara, J., Troya, J., Burgueño, L., & Vallecillo, A. (2023). On the assessment of generative AI in modeling tasks: an experience report with ChatGPT and UML. Software & Systems Modeling, 22(3), 781-793. https://doi.org/10.1007/s10270-023-01105-5

- **Decision:** supporting — Empirical assessment of ChatGPT on modeling tasks reporting syntactic, semantic, and consistency deficiencies; a limitation on LLMs handling explicit models.
- **Evidence:** full text not read (status: pending).

### Beheshti, A., Yang, J., Sheng, Q. Z., Benatallah, B., Casati, F., Dustdar, S., Nezhad, H. R. M., Zhang, X., & Xue, S. (2023). ProcessGPT: Transforming Business Process Management with Generative Artificial Intelligence. https://doi.org/10.1109/icws60048.2023.00099

- **Decision:** supporting — Position paper proposing GPT-generated process models for BPM; frames LLM-driven process automation but reports no evaluation.
- **Evidence:** full text not read (status: pending).

### Fan, G., Xie, X., Zheng, X., Liang, Y., & Di, P. (2023). Static Code Analysis in the AI Era: An In-depth Exploration of the Concept, Function, and Potential of Intelligent Code Analysis Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2310.08837

- **Decision:** supporting [preprint] — LLM agent detecting code and business-logic inconsistencies reports false-positive, recall, and token-cost figures; adjacent empirical result on agentic rule checking and its cost.
- **Evidence:** full text not read (status: pending).

### Wu, T., Terry, M., & Cai, C. J. (2022). AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts. CHI Conference on Human Factors in Computing Systems, 1-22. https://doi.org/10.1145/3491102.3517582

- **Decision:** supporting — User study showing chained LLM prompt steps improve outcome quality, transparency, and controllability versus unchained monolithic use.
- **Evidence:** full text not read (status: pending).
