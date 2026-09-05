# Annotated Bibliography — specialized multi-agent versus single-agent LLM software engineering: comparative performance, coordination failures, verification, reliability, sustainability, and future work

Generated 2026-09-05 from screening decisions, evidence-ledger notes, and quality scores. Working material and audit evidence — not submission text.

## Core (73)

### Lima, I., Linhares, V., Gomes, A. M., & Maia, P. H. (2026). A Catalogue of Evaluation Metrics for LLM-Based Multi-Agent Frameworks in Software Engineering. AGENT '26: Proceedings of the 2026 International Workshop on Agentic Engineering, 120-124. https://doi.org/10.1145/3786167.3788430

- **Decision:** core — A metrics catalogue for LLM multi-agent frameworks in SE speaks directly to RQ3's 'how are they measured' clause and supplies the measurement vocabulary needed to compare architectures across studies.
- **Evidence:** full text not read (status: unavailable).

### Lai, J., & Li, Z. (2026). A Comparative Empirical Evaluation of Single-Agent and Multi-Agent LLM Prompting Strategies for Automated Formative Feedback in Education. Journal of Intelligence and Engineering Technology, 1(2), 29-38. https://doi.org/10.70393/6a696574.343135

- **Decision:** core — Controlled four-way comparison over 200 essays with a role-count ablation (zero-shot single, chain-of-thought single, dual-role draft-critique, tri-role draft-critique-revise) showing tri-role wins on quality and hallucination rate while chain-of-thought single-agent reaches near-parity at a fraction of inference cost. The quality-versus-cost parity boundary is exactly the RQ2 condition question, transferable despite the education domain.
- **Evidence:** A tri-role multi-agent pipeline (Evaluator, Student Simulator, Reviewer) produced the highest composite quality (CQS 4.21/5) and lowest over-praise and hallucination rates, but consumed roughly 4.6x the tokens of a zero-shot single agent, while a chain-of-thought single agent reached 86.5% of the top score at 32.5% of its token cost.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, reliability-nondeterminism, role-specialization, verification-testing
- **Quality:** rigor 0.71 (12/12 items scored)

### Ravindran, A., Patra, A., Babaey, V., & Purini, S. (2026). A Critical Review and Evaluation of LLMs for RTL Generation. IEEE Access, 14, 28522-28539. https://doi.org/10.1109/access.2026.3665894

- **Decision:** core — Combines a 31-study synthesis that classifies multi-agent orchestration as one methodological dimension with a fresh benchmark evaluation showing frontier models under a lightweight reflection loop match or exceed specialized domain pipelines, plus a concrete failure taxonomy (FSM mis-sequencing, handshake drift, blocking/non-blocking misuse) for generated code.
- **Evidence:** Across VerilogEvalV2 and RTLLM-v2.0, frontier models paired with a single-agent ReAct reflection loop and simulator feedback reached 89.74% and 96.08%, matching or exceeding prior multi-agent orchestration and fine-tuned RTL pipelines; the authors read this as benchmark saturation rather than as evidence that multi-agent specialization is unnecessary in general.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, reliability-nondeterminism, verification-testing
- **Quality:** rigor 0.83 (12/12 items scored)

### Grabowski, H. (2026). A Modular Multi-Agent {LLM} Architecture for Text-to-Diagram Generation and User-Guided Refinement. e-Informatica Software Engineering Journal, 20(1), 260109. https://doi.org/10.37190/e-inf260109

- **Decision:** core — Published in a software engineering journal and argues directly the RQ2 claim: a pipeline of interpretation, synthesis, validation, and correction agents with deterministic validation loops outperforms monolithic single-pass LLM generation on a design-artifact task. The structured abstract reports no numeric comparison, so full text is needed to establish whether the superiority claim is empirically backed.
- **Evidence:** A deterministic validation agent wrapped in a bounded generate-validate-regenerate loop acts as a robustness amplifier that homogenizes output quality across ten heterogeneous LLM backends, so models differ mainly in first-attempt stability and latency rather than in ultimate ability to satisfy the specification.
- **Domains:** code-generation-repair, cost-latency, orchestration, reliability-nondeterminism, role-specialization, verification-testing
- **Quality:** rigor 0.46 (12/12 items scored)

### Li, Y. (2026). A Multi-Agent LLM Framework for Automated Software Testing. Transactions on Computing Science, 2(2), 1-25. https://doi.org/10.63808/tcs.v2i2.447

- **Decision:** core — Four-agent test-generation framework evaluated on QuixBugs with a same-model single-agent ablation that attributes the gain to role decomposition rather than the diagnostic agent, plus a 35-point detection-rate gap traced to hallucinated oracle values and signature mismatches. Hits RQ2 (where specialization pays off) and RQ3 (measured verification failure modes) simultaneously.
- **Evidence:** A four-agent testing framework reaches 55.0% differential defect detection on QuixBugs versus 37.5% for a same-model single-agent baseline, and the ablation attributes that 17.5-point advantage to role decomposition rather than to the dedicated diagnostic agent; the conventional unconditional criterion overstates detection by 35 points (90.0% vs 55.0%).
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, reliability-nondeterminism, role-specialization, verification-testing
- **Quality:** rigor 0.71 (12/12 items scored)

### Wang, J., Wang, Y., Chen, M., Xie, X., Chen, C., Mu, F., Liu, Z., & Wang, Q. (2026). A Survey for LLM Agent Trajectory Analysis: From Failure Attribution to Enhancement. IEEE Transactions on Software Engineering, 1-23. https://doi.org/10.1109/tse.2026.3717765

- **Decision:** core — Abstract text is only IEEE metadata, but the title is unambiguous: a TSE survey of agent trajectory analysis organized around failure attribution, which is exactly the failure-mode taxonomy and measurement question in RQ3.
- **Evidence:** Surveying 55 papers on LLM agent trajectory analysis, the authors show automated failure attribution remains weak: step-level attribution accuracy on the Who&When benchmark spans only about 25-52%, with agent-level accuracy substantially higher, and benchmark diversity is the field's bottleneck. Multi-agent failure taxonomies (MAST) attribute failures to specification issues, inter-agent misalign…
- **Domains:** benchmarks-evaluation, observability-fault-injection, orchestration, reliability-nondeterminism, verification-testing
- **Quality:** rigor 0.62 (12/12 items scored)

### Bass, T. (2026). A Validation and Governance Framework for Multi-Agent LLM Scientific Software Development. IAIT '26: Proceedings of the 14th International Conference on Advances in Information Technology, 1-6. https://doi.org/10.1145/3816713.3818807

- **Decision:** core — Targets run-to-run non-determinism in multi-agent LLM development and critiques synthetic-test benchmarks as inadequate validation, addressing RQ3's verification and reliability measurement problem head-on.
- **Evidence:** full text not read (status: unavailable).

### Kumar, R., Ali, W., Ahmed, J., Ali, N. I., & Usman, S. (2026). AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering. arXiv preprint. https://doi.org/10.48550/arxiv.2604.13120

- **Decision:** core [preprint] — Reports 40.0% resolution on SWE-Bench Lite with a 26-28 point margin over single-agent baselines plus ablations isolating execution feedback from role decomposition, supplying quantified RQ2 evidence and an explicit verification-by-sandboxed-execution mechanism for RQ3.
- **Evidence:** A five-role pipeline (Planner, Coder, Tester, Debugger, Critic) with mandatory sandboxed execution of every patch resolves 40.0% of SWE-bench Lite tasks versus 14.0% for a same-model single-agent baseline and 12.0% for ReAct. Ablations attribute the gain jointly to execution feedback (Tester-Debugger loop) and role decomposition, at roughly 2.7x the per-task API cost.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, cost-latency, orchestration, reliability-nondeterminism, role-specialization, verification-testing
- **Quality:** rigor 0.54 (12/12 items scored)

### Agha, M., & Miqdad, A. (2026). An empirical comparison of multi-agent LLM architectural patterns for automated unit test generation. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.5281/zenodo.20309242

- **Decision:** core — Promoted well above its rank 53 position because it runs a controlled experiment comparing three patterns including an explicit Single-Agent Baseline on unit test generation, and reports a decomposition penalty where splitting into specialized workers eliminates environmental context.
- **Evidence:** In a controlled 270-execution comparison on TestEval unit-test generation with one model held constant, the Sequential pipeline beat the Single-Agent baseline (92.2% vs 81.1% success) while the Hierarchical supervisor-worker pattern underperformed the single agent badly (54.4% success, 28.54% test failure rate, 3.7x the cost); every hierarchical failure was attributed to a 'supervisor information…
- **Domains:** communication, comparative-single-vs-multi, cost-latency, orchestration, topology, verification-testing
- **Quality:** rigor 0.96 (12/12 items scored)

### Shafin, W. I., Rafi, M. N., Li, Z., & Chen, T.-H. (2026). An Empirical Study of Waterfall-style Multi-Agent Workflows for Class-Level Code Generation. PROMISE '26: Proceedings of the 22nd International Conference on Predictive Models and Data Analytics in Software Engineering, 11-20. https://doi.org/10.1145/3803846.3807461

- **Decision:** core — Explicitly criticizes prior evaluation of isolated single-agent generation and empirically studies staged multi-agent workflows for class-level code with maintainability and structure outcomes, making it a direct RQ2 comparison despite its low rank.
- **Evidence:** full text not read (status: unavailable).

### Kim, D.-K. (2026). Artifact validity under varying agent configurations in LLM-assisted software development: A comparative analysis. Information and Software Technology, 192, 108022. https://doi.org/10.1016/j.infsof.2026.108022

- **Decision:** core — Abstract is truncated but title and opening explicitly frame a comparative analysis of artifact validity across differing LLM agent configurations over the development lifecycle, which is exactly the single-agent versus multi-agent configuration question in RQ2. Journal venue (Information and Software Technology) indicates an empirical software engineering study.
- **Evidence:** full text not read (status: unavailable).

### Arnaudo, A., Coppola, R., Giobergia, F., Morisio, M., Nguyen, V.-T., Chen, E., Ma, X., Ji, X., & Mai, M.-T. (2026). Automated Black-Box Testing: A Comparative Study of LLM Agent Architectures and Prompt Engineering. 2026 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW), 29-36. https://doi.org/10.1109/icstw72326.2026.00018

- **Decision:** core — No abstract was retrieved, but a comparative study of LLM agent architectures for black-box testing is a direct architecture-versus-architecture experiment in an SE activity, and it additionally isolates prompt engineering as a confound for RQ2.
- **Evidence:** On HumanEval black-box unit-test generation, prompt engineering rather than architecture is the primary driver: multi-agent collaborative and competitive configurations achieve marginally higher coverage (peak 99.54%) but statistically comparable execution success to a single agent (96.98% vs 96.89%) while consuming 3-4x the tokens.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, debate-consensus, verification-testing
- **Quality:** rigor 0.88 (12/12 items scored)

### Qi, S., Ma, J., Xing, R., Guo, W., Huang, X., Gao, Z., Deng, J., Liu, J., Zhang, L., Wei, B., Yang, B., Wang, P., Sun, J., Tao, J., Wu, Y., Liu, H., Yao, Y., & Liu, T. (2026). Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems. arXiv preprint. https://arxiv.org/abs/2605.14892

- **Decision:** core [preprint] — Failure attribution across collaborating specialized agents is precisely the RQ3 target, and the snippet notes that tighter coordination introduces conflicts a single agent never encounters, giving a direct account of coordination-induced failure modes.
- **Evidence:** Role heterogeneity buys division of labour but raises interdependence, so specialized multi-agent systems become more sensitive to interface mismatches, cascading error propagation, and coordination overhead; the survey argues failure attribution is unsettled because the point where an anomaly becomes observable rarely coincides with its origin.
- **Domains:** communication, memory-context, orchestration, reliability-nondeterminism, role-specialization, topology
- **Quality:** rigor 0.54 (12/12 items scored)

### Akshathala, S., Adnan, B., Ramesh, M., Vaidhyanathan, K., Muhammed, B., & Parthasarathy, K. (2026). Beyond Task Completion: An Assessment Framework for Evaluating Agentic AI Systems. AGENT '26: Proceedings of the 2026 International Workshop on Agentic Engineering, 9-17. https://doi.org/10.1145/3786167.3788414

- **Decision:** core — Explicitly targets evaluation of integrated multi-agent LLM architectures beyond task-completion metrics, which is exactly the measurement question in RQ3; promoted above its rank 178 position because the abstract commits to an assessment framework for coordinated agent systems.
- **Evidence:** In a production CloudOps deployment, binary task-completion metrics were identical between baseline and framework evaluation while pillar-specific metrics exposed substantial hidden behavioural failures (S1 had 100% tool sequencing but 33% policy adherence; S2 completed the task with 13.1% memory recall), and the multi-agent scenario S3 had by far the worst tool-orchestration failure rate (7.67 a…
- **Domains:** benchmarks-evaluation, cost-latency, end-to-end-sdlc, governance-accountability, memory-context, observability-fault-injection, orchestration, reliability-nondeterminism, verification-testing
- **Quality:** rigor 0.92 (12/12 items scored)

### Zhu, X., Wu, J., Zhang, X., Li, T., Mu, Y., Zhai, J., Shen, C., Fang, C., & Liu, Y. (2026). Bugs in Modern LLM Agent Frameworks: An Empirical Study. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering, 1588-1592. https://doi.org/10.1145/3803437.3805536

- **Decision:** core — An empirical bug study of the frameworks handling lifecycle execution and multiagent coordination gives measured, categorized coordination and reliability failures, answering RQ3 head-on.
- **Evidence:** full text not read (status: unavailable).

### Radeva, I., Noncheva, T., Doukovska, L., & Popchev, I. (2026). Comparing Single-Agent and Multi-Agent Strategies in LLM-Based Title-Abstract Screening. https://doi.org/10.20944/preprints202603.2107.v1

- **Decision:** core [preprint] — Rare quantified negative result: across five coordination strategies (single-agent, majority voting, recall-focused ensemble, confidence-weighted aggregation, two-stage debate) on a 200-paper gold standard, the single-agent few-shot configuration beat every multi-agent alternative and confidence weighting added no discriminative value. Direct evidence for the RQ2 underperformance condition where coordination overhead outweighs model selection.
- **Evidence:** Across five coordination strategies and four 7-8B open-source models, a single-agent baseline with the best-matched model in few-shot mode outperformed every multi-agent alternative (recall 100%, precision 70.4%, F1 82.6%, WSS@95 43.4%), indicating model selection outweighs coordination strategy at this parameter scale.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, debate-consensus, governance-accountability
- **Quality:** rigor 0.83 (12/12 items scored)

### Kehkashan, T., Abdullah, M., Al-Shamayleh, A. S., Ivković, N., Ismail, N. A., Ahmad, S. S. S., Rehman, A., & Akhunzada, A. (2026). From benchmarks to deployment: a comprehensive review of agentic AI evaluation. Artificial Intelligence Review, 59(8). https://doi.org/10.1007/s10462-026-11571-0

- **Decision:** core — Systematically dissects 15 agent benchmarks (SWE-bench, HumanEval, Terminal-Bench) with software development as the primary case study, quantifying that 0/15 score safety or cost and 13/15 use binary success, which directly addresses how agentic failure and reliability are (mis)measured under RQ3. Also names the benchmark-to-deployment ecological-validity gap central to RQ1.
- **Evidence:** A critical review of 15 agent benchmarks finds evaluation methodology, not model capability, is the binding constraint on deployment: 0/15 score safety or security, 0/15 include cost-efficiency in the primary protocol, 13/15 rely solely on binary success, and no benchmark exceeds 50% on the authors' deployment-readiness rubric.
- **Domains:** benchmarks-evaluation, cost-latency, end-to-end-sdlc, governance-accountability, observability-fault-injection, reliability-nondeterminism, security
- **Quality:** rigor 0.50 (12/12 items scored)

### Xu, Q., Wang, G., Briand, L., & Liu, K. (2026). Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3803418

- **Decision:** core — Targets hallucination as the failure mode and consensus among agents as the mitigation for end-to-end JUnit generation, combining an SE verification task with an explicit reliability mechanism relevant to RQ3.
- **Evidence:** CANDOR decomposes JUnit test generation across specialized agents (Initializer, Planner, Tester, Inspector, Requirement Engineer, Panelist, Interpreter, Curator) and shows that a panel-discussion consensus over multiple reasoning LLMs is what suppresses oracle hallucination: ablating the panel costs 0.067-0.086 oracle correctness, and consensus-by-reasoning beats plain majority voting.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, debate-consensus, reliability-nondeterminism, role-specialization, verification-testing
- **Quality:** rigor 1.00 (12/12 items scored)

### Is Collaboration Worth It? A Decision-Oriented Survey in Multi-Agent Systems. (2026). https://www.techrxiv.org/doi/abs/10.36227/techrxiv.176978654.41579706

- **Decision:** core — The framing question is literally when multi-agent collaboration is worth its cost relative to a comparable single-agent pipeline, including latency overheads and specialized-role designs, which is RQ2 stated as a survey.
- **Evidence:** full text not read (status: unavailable).

### Calboreanu, E. (2026). Iterative Audit Convergence in LLM-Managed Multi-Agent Systems: A Case Study in Prompt-Engineering Quality Assurance. Software, 5(2), 26. https://doi.org/10.3390/software5020026

- **Decision:** core — Measures verification failure in a production seven-lane LLM multi-agent pipeline: 51 consistency defects across nine audit rounds with a seven-category defect taxonomy, non-monotonic convergence, and inter-rater reliability (Cohen's kappa 0.80/0.46). Directly answers RQ3 on how coordination and specification-consistency failure modes are detected and quantified.
- **Evidence:** Iterative full-scope LLM auditing of a seven-lane multi-agent prompt-specification surface surfaced 51 defects over nine non-monotonic rounds; cross-lane data-contract defects were undetectable by single-file review by construction and only appeared once multi-file context loading was enabled.
- **Domains:** governance-accountability, reliability-nondeterminism, requirements-design, verification-testing
- **Quality:** rigor 0.88 (12/12 items scored)

### Tang, Y., & Runkler, T. (2026). Llm-based agentic systems for software engineering: Challenges and opportunities. arXiv preprint. https://doi.org/10.18420/se2026-ws_15

- **Decision:** core [preprint] — SE-scoped survey that contrasts single-agent systems such as AUTOFL against multi-agent designs and enumerates open challenges, matching the comparative-performance and future-work strands of RQ1.
- **Evidence:** A concept-paper review across the SDLC argues multi-agent specialization improves modularity, tool use, and parallelism, but that current SE benchmarks measure isolated tasks and therefore cannot assess the cooperative capabilities that multi-agent systems are supposed to provide.
- **Domains:** benchmarks-evaluation, cost-latency, end-to-end-sdlc, human-in-loop, orchestration, role-specialization
- **Quality:** rigor 0.38 (12/12 items scored)

### Rasheeda, Z., Waseema, M., Kemella, K.-K., Saari, M., & Abrahamsson, P. (2026). LLM-Based Multi-Agent Systems for Code Generation: A Multi-Vocal Literature Review. arXiv preprint. https://doi.org/10.5281/zenodo.21487935

- **Decision:** core [preprint] — A multi-vocal review focused on the specific claim that multiple agents beat single-agent approaches for code generation, giving both an SE-task synthesis for RQ1 and a grey-literature evidence base that a purely academic search would miss.
- **Evidence:** A multi-vocal review of 114 academic and grey-literature sources finds that reliability, security, cost and verification problems in LLM multi-agent code generation are systemic architectural weaknesses rather than isolated model failures, and that current benchmarks provide insufficient evaluation of multi-agent collaboration and coordination. The authors conclude the field is shifting from a mo…
- **Domains:** benchmarks-evaluation, cost-latency, governance-accountability, memory-context, orchestration, reliability-nondeterminism, security
- **Quality:** rigor 0.67 (12/12 items scored)

### Otoum, N., & Elkhalili, N. (2026). Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review. IEEE Access, 14, 7443-7465. https://doi.org/10.1109/access.2026.3652325

- **Decision:** core — An SLR of agentic SE methods and techniques covers the primary-study population underlying RQ1, and its inclusion set and categorization should be read in full to check coverage of this review's own corpus.
- **Evidence:** This SLR of 61 studies (2022-2025) documents a field-wide migration from single-agent to role-specialized multi-agent architectures and asserts reliability and performance gains, but its own challenge analysis reports that inter-agent protocols are informal and non-standardised, conflict resolution is immature, and token cost scales disproportionately with system complexity.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, end-to-end-sdlc, governance-accountability, orchestration, reliability-nondeterminism, role-specialization
- **Quality:** rigor 0.75 (12/12 items scored)

### Liu, S., Guo, Q., Liu, X., & Liu, Y. (2026). Mitigating Cognitive Vulnerabilities in Code Generation via Multi-Agent Adversarial Debate. WWW '26: Proceedings of the ACM Web Conference 2026, 7412-7420. https://doi.org/10.1145/3774904.3792557

- **Decision:** core — Argues that the monolithic, correlation-driven single LLM is systematically biased and uses adversarial multi-agent debate as the remedy for code generation, which is precisely the mechanism-level answer RQ2 seeks for when specialization helps.
- **Evidence:** full text not read (status: unavailable).

### MOSAIC: A Pattern Catalog and Formal Framework for Multi-Agent LLM Orchestration in Software Engineering. (2026). https://www.researchgate.net/profile/Son-Nguyen-386/publication/413630654_MOSAIC_A_Pattern_Catalog_and_Formal_Framework_for_Multi-Agent_LLM_Orchestration_in_Software_Engineering/links/6a8e6bbd7e8edd1da26f648b/MOSAIC-A-Pattern-Catalog-and-Formal-Framework-for-Multi-Agent-LLM-Orchestration-in-Software-Engineering.pdf

- **Decision:** core — Frames the shift from single-agent code generation to specialized-agent orchestration in SE and formalizes it as a pattern catalog benchmarked against three established frameworks, directly serving the orchestration-conditions question in RQ2.
- **Evidence:** full text not read (status: unavailable).

### Mitrović, S., Giuffrida, V., Barth, F., Bonet-Jover, A., López, L., Barua, S., Massé, S., Saquete, E., Delgado, A., Ahmed, M. U., Begum, S., Rehm, G., & Salani, M. (2026). Multi-Agent Systems for Software Development: a Multi-Faceted Research Question-driven Reference Guide. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.6507135

- **Decision:** core [preprint] — The snippet contrasts specialised coordinated agents against a single-agent backbone system (SWE-agent style) and catalogues capabilities, limitations, and design trade-offs, giving direct RQ2 comparative material despite its low rank.
- **Evidence:** full text not read (status: unavailable).

### Seyedghorban, Z., Klimov, E., van Deursen, A., Panichella, A., & Ozkan, B. K. (2026). Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering. 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST), 211-215. https://doi.org/10.1109/icst69053.2026.00037

- **Decision:** core — Only bibliographic metadata is present, but fault injection plus observability for LLM MAS at ICST is the rare paper that both induces and instruments coordination failures, which is exactly the how-are-they-measured half of RQ3.
- **Evidence:** Trace-aligned fault injection shows perturbations at inter-agent communication boundaries propagate more damagingly than equivalent perturbations at single LLM calls: in ChatDev a 1000 ms A2A delay produced 59.2x mean runtime amplification versus 48.1x for an LLM delay, and 1.295x vs 1.053x in a minimal two-agent demo.
- **Domains:** communication, governance-accountability, observability-fault-injection, reliability-nondeterminism
- **Quality:** rigor 0.75 (12/12 items scored)

### Watanabe, M., Li, H., Kashiwa, Y., Reid, B., Iida, H., & Hassan, A. E. (2026). On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3798166

- **Decision:** core — Measures real-world outcomes of a single agentic coding tool across 567 pull requests in 157 open-source projects, reporting 83.8% merge acceptance with 45.1% still requiring human revision especially for bug fixes and project-specific standards, which is high ecological-validity baseline evidence for what one agent achieves unaided.
- **Evidence:** full text not read (status: unavailable).

### Li, J., & Storhaug, A. (2026). Reproducible, Explainable, and Effective Evaluations of Agentic AI for Software Engineering. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering, 1501-1506. https://doi.org/10.1145/3803437.3805548

- **Decision:** core — Directly attacks how agentic SE systems are evaluated when the underlying LLMs behave as black boxes, addressing RQ3's measurement question and the reproducibility threats that affect every reported agent comparison.
- **Evidence:** full text not read (status: unavailable).

### Alenezi, M. (2026). Rethinking software engineering for agentic ai systems. arXiv preprint. https://arxiv.org/abs/2604.10599

- **Decision:** core [preprint] — Combines systematic verification and multi-agent orchestration within an SE framing, and the snippet reports the conditional finding that no single agent configuration was universally optimal, which is the exact contingency RQ2 asks about.
- **Evidence:** As LLM and agentic code generation becomes abundant, verification rather than authorship becomes the rate-limiting activity; AI-generated defects are syntactically plausible but semantically flawed, so they evade superficial review and require layered hybrid verification pipelines plus accountable human oversight.
- **Domains:** end-to-end-sdlc, formal-verification, governance-accountability, human-in-loop, orchestration, verification-testing
- **Quality:** rigor 0.50 (12/12 items scored)

### Chebolu, I., Mallick, A., & Rana, H. (2026). SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing. arXiv preprint. https://doi.org/10.48550/arxiv.2602.04418

- **Decision:** core [preprint] — Empirically compares a specialized multi-agent design against centralized and pipeline alternatives under controlled failure scenarios while measuring coordination, recovery behavior, and resource use, hitting RQ2 and RQ3 simultaneously in an SE verification and security workflow.
- **Evidence:** In smart-contract auditing, a decentralized multi-agent design outperformed a centralized scheduler that implemented identical risk-aware planning and repair logic (F1 0.87 vs 0.83), with the advantage concentrated under injected failures rather than under normal conditions, at a measured coordination overhead of 4.2%.
- **Domains:** code-generation-repair, cost-latency, debate-consensus, governance-accountability, observability-fault-injection, orchestration, reliability-nondeterminism, security, topology, verification-testing
- **Quality:** rigor 0.79 (12/12 items scored)

### Shang, Y., Zhang, Q., Zhan, Z., Huang, K., Fang, C., & Chen, Z. (2026). TestAgent: A Multi-Agent LLM Framework for Repository-Level Unit Test Generation. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering, 242-246. https://doi.org/10.1145/3803437.3806428

- **Decision:** core — A named multi-agent framework for repository-level unit test generation that is motivated by the limited context and rigid workflows of existing single-agent LLM test tools, putting it directly on RQ2's specialization-versus-monolith question in a verification task.
- **Evidence:** full text not read (status: unavailable).

### Naqvi, S., Baqar, M., & Mohammad, N. A. (2026). The Rise of Agentic Testing: Multi-Agent Systems for Robust Software Quality Assurance. arXiv preprint. https://doi.org/10.48550/arxiv.2601.02454

- **Decision:** core [preprint] — Positions multi-agent testing explicitly against the limitations of single-agent automation and reports comparative coverage and test-quality results against static LLM baselines, giving RQ2 evidence inside the SE testing and QA activity.
- **Evidence:** A three-agent closed loop (generation, execution/analysis, review/optimization) with sandboxed execution feedback raises statement coverage from 72.8% to 94.9% and valid executable tests from 64.1% to 89.3% over a single-pass LLM baseline, but the authors report non-deterministic LLM behavior, coordination latency, and context drift as persistent reliability threats.
- **Domains:** comparative-single-vs-multi, cost-latency, governance-accountability, orchestration, reliability-nondeterminism, verification-testing
- **Quality:** rigor 0.25 (12/12 items scored)

### Basu, S., Kjellberg, V., Sun, S., Haraldsson, B., Babu, M. A. A., Meding, W., Fotrousi, F., & Staron, M. (2026). Understanding Conversational Patterns in Multi-agent Programming: A Case Study on Fibonacci Game Development. AIware '26: Proceedings of the 3rd ACM International Conference on AI-Powered Software, 238-247. https://doi.org/10.1145/3805760.3814914

- **Decision:** core — Explicitly studies how LLM agents coordinate and maintain role adherence during a programming task, which is exactly the coordination-failure evidence RQ3 asks for even though the case study is small.
- **Evidence:** Across 12 Designer:Programmer agent pairs from 7 open-source LLMs on a single C programming task, convergence, role alignment and compilation success were not correlated: only DeepSeek-R1:DeepSeek-R1 converged and sustained a correct solution, several pairs achieved 100% compilation while never reaching a correct solution, and pairs that diverged after 3, 21 or 69 iterations never recovered.
- **Domains:** code-generation-repair, communication, orchestration, reliability-nondeterminism, role-specialization
- **Quality:** rigor 0.67 (12/12 items scored)

### Orogat, A., Rostam, A., & Mansour, E. (2026). Understanding multi-agent LLM frameworks: A unified benchmark and experimental analysis. arXiv preprint. https://arxiv.org/abs/2602.03128

- **Decision:** core [preprint] — Holds the underlying model fixed while systematically comparing single-agent against multi-agent settings across frameworks, which is the cleanest available controlled design for isolating the orchestration effect asked about in RQ2.
- **Evidence:** Under a fixed LLM and identical tasks, framework-level architectural choices alone drive over 100x latency differences, up to 30% planning accuracy loss, and coordination success collapsing from above 90% to below 30%, indicating multi-agent behavior is governed by execution semantics and interface design rather than model quality.
- **Domains:** benchmarks-evaluation, cost-latency, debate-consensus, memory-context, orchestration, role-specialization, topology
- **Quality:** rigor 0.79 (12/12 items scored)

### Xue, Z., Zhao, Y., Wang, S., Chen, K., & Wang, H. (2025). A Characterization Study of Bugs in LLM Agent Workflow Orchestration Frameworks. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 3369-3380. https://doi.org/10.1109/ase63991.2025.00278

- **Decision:** core — A characterization of defects in the orchestration frameworks that implement agent workflows is exactly the reliability and coordination failure-mode evidence RQ3 requires, and its empirical bug taxonomy warrants full-text extraction.
- **Evidence:** Across 1,026 manually annotated bugs in LangChain, LlamaIndex, and Haystack, agent orchestration frameworks depart from traditional software bug profiles: Incorrect Functionality (315) nearly matches Crash (326), a new Unexpected Output category accounts for 16.5%, and the authors conclude that deterministic testing and static analysis are structurally inadequate for these probabilistic, heavily…
- **Domains:** code-generation-repair, cost-latency, orchestration, reliability-nondeterminism, verification-testing
- **Quality:** rigor 0.88 (12/12 items scored)

### Guo, J., Huang, S., Li, M., Huang, D., Chen, X., Zhang, R., Guo, Z., Yu, H., Yiu, S.-M., Lio, P., & Lam, K.-Y. (2025). A comprehensive survey on benchmarks and solutions in software engineering of llm-empowered agentic system. arXiv preprint. https://arxiv.org/abs/2510.09721

- **Decision:** core [preprint] — Catalogs the benchmarks used to evaluate LLM agentic systems in SE alongside the increasingly apparent limitations of single-agent systems, which directly serves the measurement half of RQ3 and anchors the evaluation instruments used across the corpus.
- **Evidence:** Connecting 50+ benchmarks to prompt-based, fine-tuning-based and agent-based solution paradigms across 150+ papers, the survey argues that existing multi-agent SE frameworks rely on simplistic coordination (sequential pipelines or centralized orchestration) that cannot express real development workflows, and that no benchmarks measure coordination efficiency or communication overhead.
- **Domains:** benchmarks-evaluation, cost-latency, formal-verification, governance-accountability, orchestration, role-specialization, verification-testing
- **Quality:** rigor 0.42 (12/12 items scored)

### Rotar, C., & Zhang, Q. (2025). A design science research approach to Large Language Model-Based Agents for Requirements Specification (LLMBA4RS) in low-code applications. Requirements Engineering, 30(4), 399-422. https://doi.org/10.1007/s00766-025-00450-9

- **Decision:** core — Presents a named LLM agent method (LLMBA4RS) built on RAG and the CrewAI multi-agent framework for generating and refining user stories, demonstrated and evaluated by practitioners across three low-code applications. Combines a software engineering activity, a named multi-agent architecture, and practitioner evaluation.
- **Evidence:** full text not read (status: unavailable).

### Sami, M., Zhang, Z., Waseem, M., Kemell, K., Rasheed, Z., Herda, T., Hasan, M. T., Rasku, J., & Abrahamsson, P. (2025). A Multi-agent LLM System for Automated Requirements Analysis: A Study on User Story Generation and Prioritization. Lecture notes in computer science, 178-187. https://doi.org/10.1007/978-3-032-04200-2_12

- **Decision:** core — Investigates a role-based multi-agent LLM system for a requirements engineering activity (user story generation and prioritization), matching the SE activity plus named architecture inclusion rule. Role assignment across agents is the exact specialization mechanism under study in RQ2.
- **Evidence:** full text not read (status: unavailable).

### Di Sipio, C., De Oliveira, M. C. S., Di Ruscio, D., Nguyen, P. T., & Rubei, R. (2025). Agentware in software engineering: A taxonomy for leveraging llms-based multi-agent systems. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.5273078

- **Decision:** core [preprint] — Provides an SE-specific taxonomy for LLM multi-agent systems and counts the literature by configuration (it notes 34 papers proposing single-agent systems), giving the architectural landscape and single-versus-multi framing that anchors RQ1.
- **Evidence:** full text not read (status: unavailable).

### Tawosi, V., Ramani, K., Alamir, S., & Liu, X. (2025). ALMAS: an Autonomous LLM-based Multi-Agent Software Engineering Framework. 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW), 287-290. https://doi.org/10.1109/asew67777.2025.00059

- **Decision:** core — Only IEEE metadata is available, but the title names a concrete autonomous multi-agent SE framework, i.e. the role-specialized orchestration architecture class that RQ1 and RQ2 are about; the full text is needed for its role decomposition and evaluation.
- **Evidence:** A vision paper proposing ALMAS, a tiered multi-agent framework aligning agents with agile roles across the full SDLC, in which a Supervisor Agent routes sub-tasks to cheaper or stronger LLMs by complexity and Meta-RAG code summaries mitigate context limits; the framework is demonstrated only on one illustrative application-generation use case, with end-to-end evaluation explicitly deferred.
- **Domains:** cost-latency, end-to-end-sdlc, memory-context, orchestration, role-specialization, topology, verification-testing
- **Quality:** rigor 0.33 (12/12 items scored)

### Owotogbe, J. (2025). Assessing and Enhancing the Robustness of LLM-Based Multi-Agent Systems Through Chaos Engineering. 2025 IEEE/ACM 4th International Conference on AI Engineering – Software Engineering for AI (CAIN), 250-252. https://doi.org/10.1109/cain66642.2025.00039

- **Decision:** core — Applies chaos engineering to LLM multi-agent systems, which yields both an injection-based measurement method and observed robustness breakdowns; this is a direct source for RQ3's failure modes and how they are measured.
- **Evidence:** This doctoral-symposium research plan argues that LLM-based multi-agent systems fail in production through emergent, cascading modes (hallucination, agent failure, inter-agent communication failure) that conventional testing does not surface, and proposes chaos engineering as the systematic robustness-testing and certification method for them.
- **Domains:** communication, end-to-end-sdlc, governance-accountability, observability-fault-injection, reliability-nondeterminism
- **Quality:** rigor 0.42 (12/12 items scored)

### Zeng, Z., Li, Y., Xie, R., Ye, W., & Zhang, S. (2025). Benchmarking and Studying the LLM-based Agent System in End-to-End Software Development. arXiv preprint. https://doi.org/10.48550/arxiv.2511.04064

- **Decision:** core [preprint] — Explicitly builds a benchmark for end-to-end software development and isolates the effect of configuration choices, naming 'single-agent versus multi-agent' as a studied factor, which is the direct empirical comparison RQ2 asks for.
- **Evidence:** With three agent architectures implemented on a unified toolset to remove engineering confounds, a Dev-Test multi-agent workflow beat a single agent (49.48% vs 45.72% requirement implementation rate) while a Design-Dev-Test workflow collapsed to 27.71%, showing multi-agent decomposition helps only when well structured; 55.8% of all failures originated in planning (requirement omission 27.9%, misi…
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, end-to-end-sdlc, orchestration, reliability-nondeterminism, requirements-design, verification-testing
- **Quality:** rigor 0.92 (12/12 items scored)

### Haseeb, M. (2025). Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code. arXiv preprint. http://arxiv.org/abs/2508.08322v1

- **Decision:** core [preprint] — Reports higher single-shot success and better project-context adherence than baseline single-agent approaches on a real Next.js repository, and attributes the gain jointly to context injection and agent role decomposition, which is the confound RQ2 needs disentangled.
- **Evidence:** On five non-trivial tasks in a ~180K-line Next.js repository, a context-engineered hub-and-spoke multi-agent Claude Code system succeeded on 4/5 tasks (80%) without human correction versus 2/5 (40%) for a single-agent Claude baseline, at roughly 3-5x the token cost; the baseline's failures were dominated by missed cross-file edits and hallucinated APIs.
- **Domains:** comparative-single-vs-multi, cost-latency, memory-context, orchestration, reliability-nondeterminism, role-specialization, verification-testing
- **Quality:** rigor 0.17 (12/12 items scored)

### Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2025). Demystifying LLM-Based Software Engineering Agents. Proceedings of the ACM on Software Engineering (PACMSE), Volume 2, Issue FSE, 2(FSE), 801-824. https://doi.org/10.1145/3715754

- **Decision:** core — A dedicated review of LLM SE agents spanning code synthesis, repair, and test generation across both research and industry practice, which is the closest match in this chunk to RQ1's survey-of-the-landscape framing.
- **Evidence:** full text not read (status: unavailable).

### Cai, Y., Li, R., Liang, P., Shahin, M., & Li, Z. (2025). Designing LLM-based multi-agent systems for software engineering tasks: Quality attributes, design patterns and rationale. arXiv preprint. https://arxiv.org/abs/2511.08475

- **Decision:** core [preprint] — Studies the transition from single-agent to a four-specialized-agent design for SE tasks using Open Coding and Constant Comparison, tying design patterns to quality attributes and documented rationale, which addresses both the conditions in RQ2 and design-level reliability concerns.
- **Evidence:** Across 94 papers on LLM-based multi-agent systems for SE, Role-Based Cooperation is the dominant design pattern (44 systems, 47.4%) among 16 identified patterns, chosen mainly to improve functional correctness and modularity, while performance efficiency (51.1%) and maintainability (50.0%) are traded off against each other.
- **Domains:** cost-latency, end-to-end-sdlc, orchestration, requirements-design, role-specialization, topology
- **Quality:** rigor 0.75 (12/12 items scored)

### Koduri, S. K. A. (2025). Efficiency-First Design for LLM-Based Multi-Agent Systems: A Framework and Empirical Analysis. https://doi.org/10.13140/rg.2.2.13238.15689

- **Decision:** core — The snippet frames the move from single-agent tools to specialized multi-agent systems and argues that missing efficiency measures make cross-system comparison impossible, hitting RQ1's sustainability strand and RQ2's overhead-driven underperformance case directly.
- **Evidence:** full text not read (status: unavailable).

### Zhang, S., Xing, Z., Guo, R., Xu, F., Chen, L., Zhang, Z., Zhang, X., Feng, Z., & Zhuang, Z. (2025). Empowering Agile-Based Generative Software Development through Human-AI Teamwork. ACM Transactions on Software Engineering and Methodology, 34(6), 1-46. https://doi.org/10.1145/3702987

- **Decision:** core — AgileGen contrasts agile iterative human-AI teamwork against top-down waterfall multi-agent generation, attributing cumulative error to the waterfall handoff chain, and uses Gherkin acceptance criteria as a testable consistency bridge between requirements and code; directly evidences requirement drift and verification mechanisms for RQ2 and RQ3.
- **Evidence:** full text not read (status: unavailable).

### Mandal, I., Soni, J., Zaki, M., Smedskjær, M. M., Wondraczek, K., Wondraczek, L., Gosvami, N. N., & Krishnan, N. M. A. (2025). Evaluating large language model agents for automation of atomic force microscopy. Nature Communications, 16(1), 9104-9104. https://doi.org/10.1038/s41467-025-64105-7

- **Decision:** core — Explicitly ablates multi-agent against single-agent frameworks on the AFMBench suite and finds multi-agent superiority yet high sensitivity to prompt and instruction formatting, plus a named 'sleepwalking' instruction-deviation failure mode; qualifies under the any-domain single-versus-multi inclusion rule and supplies measured coordination failures for RQ2 and RQ3.
- **Evidence:** On AFMBench the multi-agent AILA configuration beat direct single-agent tool integration for GPT-4o (70% vs 58% success) but made no measurable difference for weaker models, and the authors document 'sleepwalking', where agents take unauthorised actions beyond their instructions, as a distinct instruction-adherence failure mode separate from code-generation errors.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, cost-latency, governance-accountability, orchestration, reliability-nondeterminism, role-specialization
- **Quality:** rigor 0.88 (12/12 items scored)

### Tomic, S., Alégroth, E., & Isaac, M. (2025). Evaluation of the Choice of LLM in a Multi-Agent Solution for GUI-Test Generation. 2025 IEEE Conference on Software Testing, Verification and Validation (ICST), 487-497. https://doi.org/10.1109/icst62969.2025.10989038

- **Decision:** core — PathFinder assigns perception, decision, input-handling, and validation roles for exploratory web GUI testing and sweeps 27 LLM permutations across four e-commerce sites, finding that a uniform LLM across agents gives the best F1 and hypothesizing reduced task-coordination discrepancies as the cause. Empirical software testing evidence that heterogeneous model-per-role pairing introduces coordination cost, answering RQ2 and RQ3.
- **Evidence:** Testing 27 permutations of three local LLMs across three agent roles in the PathFinder GUI-testing multi-agent system, the hypothesis that heterogeneous specialist LLMs beat a single shared LLM was rejected per-site (homogeneous constellations won on specific websites) and only weakly supported across sites (best mixed 0.703 F1 vs 0.660 for all-Gemma2), a marginal difference.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, orchestration, role-specialization, verification-testing
- **Quality:** rigor 0.92 (12/12 items scored)

### Lu, R., Li, Y., & Huo, Y. (2025). Exploring Autonomous Agents: A Closer Look at Why They Fail When Completing Tasks. https://doi.org/10.1109/ase63991.2025.00330

- **Decision:** core — Builds a 34-task benchmark, measures three open-source agent frameworks across two LLM backbones at roughly 50% completion, and derives a three-tier failure taxonomy covering planning, execution, and response generation while explicitly analysing interaction and communication mechanisms. This directly answers RQ3 on what failure modes are reported and how they are measured.
- **Evidence:** Three popular planner/code-generator/executor agent frameworks completed only about half of 34 programmable tasks, and a 19-cause three-tier failure taxonomy (planning, execution, response generation) derived from 104 failures across 204 runs showed the most common problems were improper task decomposition, failed self-refinement loops, and context/format issues rather than raw model weakness; th…
- **Domains:** benchmarks-evaluation, orchestration, reliability-nondeterminism
- **Quality:** rigor 0.75 (12/12 items scored)

### Takerngsaksiri, W., Pasuksmit, J., Thongtanunam, P., Tantithamthavorn, C., Zhang, R., Jiang, F., Li, J., Cook, E., Chen, K., & Wu, M. (2025). Human-In-The-Loop Software Development Agents. 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP), 342-352. https://doi.org/10.1109/icse-seip66354.2025.00036

- **Decision:** core — An ICSE-SEIP industrial account of where autonomous development agents require human intervention, which is exactly the boundary condition RQ2 asks about and a well-cited source of practitioner-observed agent failure modes.
- **Evidence:** A three-role human-in-the-loop agent pipeline (AI Planner, AI Coding, Human) deployed inside Atlassian JIRA performed far worse on proprietary enterprise issues than on SWE-bench Verified (30% vs 86% file-localization recall; 30% vs 45% code similarity), showing that open-source benchmark results do not transfer to enterprise contexts. Human feedback at each stage recovered usefulness: 82% of gen…
- **Domains:** benchmarks-evaluation, end-to-end-sdlc, human-in-loop, orchestration, role-specialization
- **Quality:** rigor 0.83 (12/12 items scored)

### Kataria, V. (2025). Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination. International Journal of Intelligent Engineering and Systems, 18(11), 450-466. https://doi.org/10.22266/ijies2025.1231.28

- **Decision:** core — Operations and incident response is an in-scope SE activity, and the paper measures a hierarchical master-plus-five-specialist architecture against 350 systematically injected failure scenarios using chaos engineering tooling, giving concrete fault-injection methodology and accuracy figures for RQ3's measurement question.
- **Evidence:** full text not read (status: unavailable).

### He, J., Treude, C., & Lo, D. (2025). LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead. ACM Transactions on Software Engineering and Methodology (TOSEM), Volume 34, Issue 5, 34(5), 1-30. https://doi.org/10.1145/3712003

- **Decision:** core — Abstract is truncated but the title is unambiguous: a dedicated literature review of LLM-based MAS scoped to software engineering with an explicit forward-looking research agenda, which covers the review scope, open challenges, and future-work component of RQ1.
- **Evidence:** full text not read (status: unavailable).

### Llm-based multi-agent systems: Frameworks, evaluation, open challenges, and research frontiers. (2025). https://link.springer.com/chapter/10.1007/978-3-032-15632-7_9

- **Decision:** core — Secondary study covering LMAS frameworks, evaluation practice, open challenges, and frontiers, and the snippet references a direct architectural comparison; this maps onto RQ1's coverage of evaluation, reliability, and future work.
- **Evidence:** full text not read (status: unavailable).

### Wang, S., Zhong, Z., Wen, S., & Liu, Y. (2025). Multi-Agent Assisted Automatic Test Generation for Java JSON Libraries. https://doi.org/10.1109/apsec66846.2025.00064

- **Decision:** core — JsonATG is a role-specialized multi-agent test-generation system (code summarization agent plus test validation agent) benchmarked against two state-of-the-art LLM-based ATG methods on coverage, with 59 confirmed bugs and an explicit $25 budget, giving comparative and cost evidence for RQ2 on a real SE task.
- **Evidence:** JSONATG's three-role decomposition (Code Summarizer, Test Programmer, Test Validator) with domain-specific mutation rules outperformed ChatTester and ChatUnitest on the large, complex fastjson classes and found 59 real bugs for $25, but the ablation shows the agent-written mutation rules actually reduced coverage on four of six classes because more generated tests failed to compile, and the Test…
- **Domains:** code-generation-repair, cost-latency, reliability-nondeterminism, role-specialization, verification-testing
- **Quality:** rigor 0.92 (12/12 items scored)

### Drammeh, P. (2025). Multi-Agent LLM Orchestration Achieves Deterministic, High-Quality Decision Support for Incident Response. arXiv preprint. http://arxiv.org/abs/2511.15755v3

- **Decision:** core [preprint] — 348 controlled trials directly contrasting single-agent copilot against multi-agent orchestration on identical incident scenarios, with a new Decision Quality metric and a latency-versus-quality finding; this is exactly the operations-side evidence and measurement instrument RQ2 and RQ3 need, notwithstanding implausibly extreme headline ratios that warrant full-text scrutiny.
- **Evidence:** full text not read (status: unavailable).

### Premasundera, S. (2025). MULTI-AGENT SYSTEM FOR AUTOMATED CODE REVIEWS. Tampere University Institutional Repository (Tampere University). https://trepo.tuni.fi/bitstream/handle/10024/232334/PremasunderaSavidya.pdf?sequence=2

- **Decision:** core [preprint] — Proposes a multi-agent LLM code review system motivated explicitly by single-agent limitations and closes with a comparative synthesis of gaps, placing it squarely on RQ2 for the code review activity; grey-literature thesis status is flagged, not disqualifying.
- **Evidence:** Four domain-specialized review agents (Readability, Refactoring, Performance, Security) plus a Consensus Agent produced broader category coverage, higher semantic diversity, lower internal redundancy, and more stable confidence than a single monolithic LLM on the same pull request, with only moderate inter-agent agreement indicating complementary rather than duplicated coverage.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, debate-consensus, reliability-nondeterminism, role-specialization, security, verification-testing
- **Quality:** rigor 0.54 (12/12 items scored)

### Mao, Z., Keung, J., Zhang, F., Liu, S., Wang, Y., & Li, J. (2025). Towards Engineering Multi-Agent LLMs: A Protocol-Driven Approach. https://doi.org/10.1109/apsec66846.2025.00100

- **Decision:** core — Names under-specification, coordination misalignment, and inappropriate verification as the three core deficiencies of multi-agent LLM systems for SE, then measures failure reduction against the MAST taxonomy across function-level and deployment-level code development plus Python and C/C++ vulnerability detection, answering RQ3 on both mechanism and measurement.
- **Evidence:** SEMAP treats multi-agent LLM failure as a classical software-engineering design defect (missing contracts, untyped interfaces, ungated transitions) and shows that adding behavioural contracts, typed messaging, and verification-gated lifecycle FSMs cuts MAST-classified failures by up to 69.6% on function-level development and 47.4% on Python vulnerability detection relative to a MetaGPT baseline.
- **Domains:** communication, end-to-end-sdlc, orchestration, reliability-nondeterminism, requirements-design, security, topology, verification-testing
- **Quality:** rigor 0.62 (12/12 items scored)

### Barrak, A. (2025). Traceability and Accountability in Role-Specialized Multi-Agent LLM Pipelines. 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW), 315-322. https://doi.org/10.1109/asew67777.2025.00064

- **Decision:** core — Metadata only, yet the title targets role-specialized pipelines specifically on traceability and accountability, which is the attribution mechanism RQ3 requires for locating coordination failures, and its six citations suggest it is already an anchor for this subtopic.
- **Evidence:** Across 8 pipeline configurations of 3 frontier LLMs on 3 benchmarks, an unstructured Planner-Executor-Critic pipeline fell below a competent monolithic model, while adding a structured accountable handoff raised accuracy by up to 36.22 points; blame attribution showed the Planner dominates failure (error rate 7.35% for the best model vs 40.49% for the worst) at a cost of 2-3x spend and 8-10x late…
- **Domains:** communication, comparative-single-vs-multi, cost-latency, governance-accountability, orchestration, reliability-nondeterminism, role-specialization, verification-testing
- **Quality:** rigor 0.92 (12/12 items scored)

### Yu, Z., Fang, A., Ma, M., Walia, J. S., Zhang, C., Chi, S., Li, Z., Chintalapati, M., Zhang, X., Wang, R., Bansal, C., Rajmohan, S., Lin, Q., Zhang, S., Pei, D., & He, P. (2025). Triangle: Empowering Incident Triage with Multi-Agent. https://doi.org/10.1109/ase63991.2025.00062

- **Decision:** core — Named multi-role LLM multi-agent framework with an explicit negotiation mechanism for cloud incident triage, validated in a real production environment with up to 97% triage accuracy and 91% Time-to-Engage reduction; supplies ecologically valid evidence on when role-specialized orchestration pays off in software operations for RQ2.
- **Evidence:** In a production cloud deployment, Triangle's multi-role negotiation is the single most load-bearing component: removing multi-agent negotiation costs about 12 points of hop-1 accuracy (54.7% -> 42.8%) and 21 points at hop 5 (91.7% -> 70.4%), more than removing semantic distillation, while automated team-information enrichment matters most at higher hop counts.
- **Domains:** communication, debate-consensus, end-to-end-sdlc, memory-context, orchestration, role-specialization
- **Quality:** rigor 0.88 (12/12 items scored)

### Bouzenia, I., & Pradel, M. (2025). Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 2846-2857. https://doi.org/10.1109/ase63991.2025.00234

- **Decision:** core — An ASE study that dissects SE agent execution trajectories, which is the most direct evidence in this chunk for characterizing and measuring agent reasoning and action failures under RQ3; its citation count reinforces its standing despite its rank 191 position.
- **Evidence:** Across 120 trajectories and 2,822 LLM interactions from three single-agent SE systems, failed runs are distinguished by repetitive non-adaptive action cycles, result-insensitive next actions, and rare but costly thought-action misalignments; even a single misalignment correlated with failure or greatly increased cost (one bug extended from iteration 6 to iteration 38).
- **Domains:** benchmarks-evaluation, code-generation-repair, cost-latency, governance-accountability, observability-fault-injection, reliability-nondeterminism, verification-testing
- **Quality:** rigor 0.96 (12/12 items scored)

### Zhang, H., Cheng, W., Wu, Y., & Hu, W. (2024). A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement. https://doi.org/10.1145/3691620.3695506

- **Decision:** core — PairCoder instantiates role specialization as a Navigator planner and Driver implementer and benchmarks the two-agent workflow against directly prompted single-LLM baselines across code generation benchmarks, reporting 12.00%-162.43% relative pass@1 gains. This is a direct role-specialized multi-agent versus single-agent comparison on a software engineering task, answering RQ2.
- **Evidence:** full text not read (status: unavailable).

### Zhang, Y., Ruan, H., Fan, Z., & Roychoudhury, A. (2024). AutoCodeRover: Autonomous Program Improvement. https://doi.org/10.1145/3650212.3680384

- **Decision:** core — Canonical AST-aware single-agent SE pipeline for GitHub issue resolution, reporting 19% on SWE-bench-lite against SWE-agent with per-issue time and cost figures; establishes the structured single-agent baseline against which role-specialized multi-agent claims in RQ2 must be judged.
- **Evidence:** full text not read (status: unavailable).

### Jin, H., Huang, L., Cai, H., Yan, J., Li, B., & Chen, H. (2024). From llms to llm-based agents for software engineering: A survey of current, challenges and future. arXiv preprint. https://arxiv.org/abs/2408.02479

- **Decision:** core [preprint] — An SE-scoped survey that explicitly organizes the field into single-agent and multi-agent branches and offers a comparative overview together with limitations, covering the comparative-performance and future-work parts of RQ1 from a 2024 baseline.
- **Evidence:** Surveying 139 papers across six SE topics, the authors argue LLM-based agents extend single LLMs through role specialization, iterative refinement and tool integration, but that multi-agent workflow complexity introduces synchronization, state-consistency and cascading-misunderstanding problems that single LLM pipelines do not exhibit, with no unified agent definition or evaluation protocol avail…
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, end-to-end-sdlc, memory-context, reliability-nondeterminism, requirements-design, role-specialization, verification-testing
- **Quality:** rigor 0.38 (12/12 items scored)

### Wang, H., Liu, Z., Wang, S., Cui, G., Ding, N., Liu, Z., & Ge, Y. (2024). INTERVENOR: Prompting the Coding Ability of Large Language Models with the Interactive Chain of Repair. https://doi.org/10.18653/v1/2024.findings-acl.124

- **Decision:** core — Assigns distinct Code Learner and Code Teacher roles with compiler feedback and reports ~18% and 4.3% gains over the undifferentiated GPT-3.5 baseline on generation and translation, giving direct evidence on when role specialization beats a single agent on code tasks.
- **Evidence:** Splitting repair into a Code Teacher that reads compiler bug reports and a Code Learner that applies the resulting Chain-of-Repair beat GPT-3.5 by roughly 18% on code generation and 4.3% on translation, and outperformed both self-repair (Self-Debug, Self-Refine) and multi-agent Self-Collaboration, showing external compiler grounding matters more than agent count.
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, role-specialization, verification-testing
- **Quality:** rigor 0.88 (12/12 items scored)

### Liu, J., Wang, K., Chen, Y., Peng, X., Chen, Z., Zhang, L., & Lou, Y. (2024). Large Language Model-Based Agents for Software Engineering: A Survey. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3796507

- **Decision:** core — The anchor survey mapping LLM-based agents onto software engineering activities, contrasting agents against standalone LLMs; it is the reference frame for RQ1's landscape and must be read in full to align this review's categories.
- **Evidence:** Surveying 124 papers, this review classifies multi-agent SE collaboration into layered, circular, star-like, tree-like, and mesh structures with unidirectional-transfer or bidirectional-chat information flow, and reports that all of these structures hit performance bottlenecks as agent count grows, with prior work showing benchmark performance saturating regardless of collaboration structure.
- **Domains:** benchmarks-evaluation, communication, cost-latency, orchestration, role-specialization, topology
- **Quality:** rigor 0.79 (12/12 items scored)

### Shen, W., Li, C., Chen, H., Yan, M., Quan, X., Chen, H., Zhang, J., & Huang, F. (2024). Small LLMs Are Weak Tool Learners: A Multi-LLM Agent. arXiv preprint, 16658-16680. https://doi.org/10.18653/v1/2024.emnlp-main.929

- **Decision:** core [preprint] — Decomposes an agent into planner, caller, and summarizer roles and shows the multi-LLM configuration surpasses the equivalently trained single-LLM agent, especially for smaller models; that is a concrete condition under which role specialization wins, which is the mechanism RQ2 targets, so it is promoted despite its low rank and non-SE benchmarks.
- **Evidence:** Decomposing a tool-use agent into separately fine-tuned planner, caller, and summarizer LLMs raises the ceiling of a single LLM: alpha-UMi with a 7B backbone outperforms the 13B single-LLM baseline, and hallucination on ToolBench drops from about 2.3% to 0.37-0.57%, but the gain requires a two-stage global-to-local fine-tuning strategy, since naive per-subtask multi-LLM training underperforms the…
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, orchestration, reliability-nondeterminism, role-specialization
- **Quality:** rigor 0.96 (12/12 items scored)

### Shu, R., Das, N., Yuan, M., Sunkara, M., & Zhang, Y. (2024). Towards Effective GenAI Multi-Agent Collaboration: Design and Evaluation for Enterprise Applications. arXiv preprint. https://doi.org/10.48550/arxiv.2412.05449

- **Decision:** core [preprint] — Benchmarks coordination and routing protocols with quantified deltas over single-agent approaches, a 23% gain specifically on code-intensive tasks, and an orchestration-bypass latency tradeoff; that combination speaks directly to RQ2 conditions and RQ3 coordination measurement.
- **Evidence:** A hierarchical supervisor/specialist collaboration framework reached 90% goal success rate across three enterprise domains, while an equivalently tool-equipped single agent regressed by up to 37 absolute points (0.53 vs 0.90 in the software-development domain), with single-agent trajectories showing more tool-parameter hallucination and incorrect tool choice; the gain was bought with substantiall…
- **Domains:** benchmarks-evaluation, communication, comparative-single-vs-multi, cost-latency, orchestration, reliability-nondeterminism, topology
- **Quality:** rigor 0.71 (12/12 items scored)

### Ramírez-Rueda, R., Benítez–Guerrero, E., Mezura-Godoy, C., & Bárcenas, E. (2024). Transforming Software Development: A Study on the Integration of Multi-Agent Systems and Large Language Models for Automatic Code Generation. 2024 12th International Conference in Software Engineering Research and Innovation (CONISOFT), 11-20. https://doi.org/10.1109/conisoft63288.2024.00013

- **Decision:** core — Only venue metadata was retrieved, but the title is unambiguous: a study of MAS-plus-LLM integration for automatic code generation sits squarely on RQ1 and RQ2 and needs full text to extract its comparative claims.
- **Evidence:** Repeating one identical prompt ten times through ChatDev's seven-role waterfall chat chain produced working code only 70% of the time, with 30% failing on compilation errors and three hallucination cases surviving multi-agent review, showing that cross-agent verification does not guarantee code quality.
- **Domains:** code-generation-repair, cost-latency, governance-accountability, orchestration, reliability-nondeterminism, role-specialization
- **Quality:** rigor 0.38 (12/12 items scored)

### Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2303.17760

- **Decision:** core [preprint] — Introduces the role-playing communicative-agent framework with inception prompting and studies cooperative multi-agent instruction following, documenting conversational breakdown modes (role flipping, instruction repetition, non-terminating dialog) that directly inform RQ2 role specialization and RQ3 coordination failures.
- **Evidence:** Two role-playing agents driven by inception prompting beat a gpt-3.5-turbo single-shot solution in 76.3% of human comparisons and 73-76% of GPT-4 comparisons, but autonomous cooperation exhibited four recurring coordination failures: role flipping, instruction repetition, flake replies, and infinite message loops.
- **Domains:** benchmarks-evaluation, communication, comparative-single-vs-multi, reliability-nondeterminism, role-specialization
- **Quality:** rigor 0.83 (12/12 items scored)

### Demystifying LLM-Based Software Engineering Agents: A Review of Capabilities, Benchmarks, and Failure Modes. (n.d.). https://journal.duc.edu.iq/index.php/djst/article/view/828

- **Decision:** core — The snippet quantitatively compares resolution rate, cost, and failure modes and states that multi-agent frameworks overcome single-agent limitations through roles, hitting RQ2 and RQ3 simultaneously; it may be the extended version of 10.1145/3715754 and should be checked for duplication at full-text retrieval.
- **Evidence:** A critical review of 20+ primary studies frames an 'Agentless Paradox': structured non-agentic pipelines match or beat autonomous single- and multi-agent systems on SWE-bench at up to an order of magnitude lower cost (Agentless 1.0 27.3% at $0.34/issue vs SWE-search MCTS 23.0% at ~$4.00), and base-model choice explains more variance than architecture; the review also warns that multi-agent debate…
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, reliability-nondeterminism, security, verification-testing
- **Quality:** rigor 0.42 (12/12 items scored)

### Ashrafi, N., Bouktif, S., & Mediani, M. (n.d.). Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Accuracy, Reliability, and Latency. 2025 IEEE 19th International Conference on Application of Information and Communication Technologies (AICT). https://ieeexplore.ieee.org/document/11268754/

- **Decision:** core — Promoted above its rank because the title states a systematic empirical evaluation of multi-agent collaboration measured on accuracy, reliability, and latency, which is precisely the cost-versus-benefit trade-off RQ2 poses.
- **Evidence:** Across 19 LLMs, runtime execution debugging alone captured almost all of the accuracy benefit (63.86% vs 64.82% for the full Analyst-Coder-Tester plus debugger chain, a statistically insignificant 0.96% gap), while adding agents multiplied latency (7.68 to 68.42 minutes) and degraded robustness under expanded test coverage, leading the authors to recommend simple agentic systems with debugging ov…
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, cost-latency, reliability-nondeterminism, verification-testing
- **Quality:** rigor 0.83 (12/12 items scored)


## Supporting (130)

### Thakur, H., & Moin, A. (2026). "ENERGY STAR" LLM-Enabled Software Engineering Tools. arXiv preprint. https://doi.org/10.48550/arxiv.2601.19260

- **Decision:** supporting [preprint] — Measures real-time energy consumption and inference time of LLM code generation across model sizes with a RAG plus prompt-engineering pipeline, supplying the sustainability measurement method RQ1 mentions, though it studies single models rather than agent orchestration.
- **Evidence:** Measuring real-time energy and inference time for RAG-augmented code generation across four LLMs (125M-7B), the effect of retrieval augmentation on energy is model-dependent rather than size-dependent: two models got cheaper, two got more expensive.
- **Domains:** benchmarks-evaluation, code-generation-repair, cost-latency

### MAJ, M. (2026). A multi-agent ensemble framework for enhancing task performance using specialized LLM. PRZEGLĄD ELEKTROTECHNICZNY, 1(3), 80-85. https://doi.org/10.15199/48.2026.3.13

- **Decision:** supporting — The recovered text is NOT an abstract: it is Polish-language marketing boilerplate describing the SIGMA-NOT publishing house and its technical journals, with no connection to the paper. Judged from the title alone, a named multi-agent ensemble framework built on specialized LLMs is plausibly relevant to role specialization, so it is retained at supporting pending full-text confirmation of the domain and evaluation.
- **Evidence:** full text not read (status: unavailable).

### Shih, P.-A., Wang, S.-H., Li, Y.-C., Tu, C.-H., & Chang, C.-H. (2026). A Multi-Agent LLM Framework for Design Space Exploration in Autonomous Driving Systems. SAC '26: Proceedings of the 41st ACM/SIGAPP Symposium on Applied Computing, 609-618. https://doi.org/10.1145/3748522.3779714

- **Decision:** supporting — Design space exploration over hardware/software configurations is a design activity and the paper names a multi-agent LLM framework for it, but the evaluation target is ADS configuration quality rather than agent-topology tradeoffs.
- **Evidence:** full text not read (status: unavailable).

### Amalfitano, D., Metzger, A., Autili, M., Fulcini, T., Hey, T., Keim, J., Pelliccione, P., Scotti, V., Koziolek, A., Mirandola, R., & Vogelsang, A. (2026). A Research Roadmap for Augmenting Software Engineering Processes and Software Products with Generative AI. ACM Transactions on Software Engineering and Methodology (TOSEM), Volume 35, Issue 9, 35(9), 1-52. https://doi.org/10.1145/3788879

- **Decision:** supporting — A design-science research roadmap for GenAI across SE processes and products feeds RQ1's future-work strand and helps position agentic approaches within the broader agenda, but it is not itself a multi-agent study.
- **Evidence:** The roadmap classifies GenAI augmentation into four forms (Copilot, GenAIware, Teammate, Robot) and finds that the agentic 'GenAI Teammate' form enhances speed, prototyping and time-to-market but reverses Git versioning semantics, environmental sustainability, accountability and code ownership, and code comprehension. Inter-agent communication overhead is identified as a direct driver of energy c…
- **Domains:** cost-latency, end-to-end-sdlc, governance-accountability, human-in-loop, orchestration, role-specialization

### Spieser, J., Balapour, A., Meller, J., Patra, K., & Shamsaei, B. (2026). A Review of Multi-Agent AI Systems for Biological and Clinical Data Analysis. Methods and Protocols, 9(2), 33-33. https://doi.org/10.3390/mps9020033

- **Decision:** supporting — Quantifies an "unreliability tax" of 15-50x higher token consumption for multi-agent systems relative to standalone LLMs and describes cascading amplification of initial hallucinations across the agent collective, which is directly transferable evidence on multi-agent cost and error propagation despite the biomedical setting.
- **Evidence:** full text not read (status: unavailable).

### Mohamed, N., Chakrabarti, P., & Gupta, S. K. (2026). A Systematic Survey of LLM-Based Agentic AI Frameworks for Multi-Agent Coordination and Interoperability. Journal of Smart Algorithms and Applications (JSAA), 5(1), 1-23. https://doi.org/10.66279/y29vex64

- **Decision:** supporting — Surveys coordination and interoperability across agentic frameworks and includes a comparative study of representative systems, which informs RQ3 coordination structures, but the snippet argues for multi-agent architectures rather than testing when they win.
- **Evidence:** A PRISMA review of 121 studies concludes that the binding constraints on LLM multi-agent systems are architectural rather than model-level: evaluation standardization, long-horizon reliability, communication security, interoperability, cost-efficient orchestration, governance, and system-level interpretability. It argues agent systems must be evaluated as holistic architectures rather than by ben…
- **Domains:** benchmarks-evaluation, communication, cost-latency, governance-accountability, orchestration, reliability-nondeterminism, security, topology

### Nageshwaran, V., & Ezekiel, S. (2026). Agentic AI and Large Language Models for Autonomous IoT Cybersecurity: A Systematic Survey, Taxonomy, and Research Roadmap. Electronics, 15(12), 2740-2740. https://doi.org/10.3390/electronics15122740

- **Decision:** supporting — A PRISMA review of 153 studies whose first taxonomy pillar is explicitly agent architecture as single- versus multi-agent, with consolidated benchmarks and an open-challenge analysis spanning hallucination, prompt-injection robustness, latency, and governance for vulnerability discovery and response.
- **Evidence:** full text not read (status: unavailable).

### Damarched, M. K. (2026). Agentic AI Modernization: Transforming Institutional Infrastructure Through Orchestrated Multi-Agent LLM Framework. Journal of Computer Science and Technology Studies, 8(4), 01-24. https://doi.org/10.32996/jcsts.2026.8.4.1

- **Decision:** supporting — Targets a genuine software engineering activity (COBOL/MUMPS/PL-I legacy code analysis, migration, and validation) with a specialized multi-agent architecture mapped onto institutional governance structures and reports modernization and manual-intervention rates, though its claim that single-agent approaches are inadequate is asserted rather than measured against a single-agent baseline.
- **Evidence:** A seven-agent, on-premises AutoGen pipeline applied to 2.12M lines of COBOL, MUMPS, and PeopleSoft legacy code across three universities achieved 87% behavioural equivalence with 35% manual intervention, versus a cited single-LLM GPT-4 COBOL study where 72% of function-level translations succeeded but only 34% achieved end-to-end behavioural equivalence.
- **Domains:** code-generation-repair, cost-latency, end-to-end-sdlc, governance-accountability, orchestration, role-specialization, security, verification-testing

### Yang, G. H., Venkit, P. N., Sedghamiz, H., Santus, E., Dibia, V., & Baldini, I. (2026). Agents in the Wild: Where Research Meets Deployment. KDD '26: Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2, 13387-13391. https://doi.org/10.1145/3770855.3816449

- **Decision:** supporting — Frames the gap between agentic research prototypes and production deployments for systems that coordinate with tools and other agents, which supports the reliability and sustainability discussion in RQ1 without supplying measured failure rates.
- **Evidence:** full text not read (status: unavailable).

### Ullasci, M., Rondina, M., Coppola, R., Giobergia, F., Bellanca, R., Pasi, G. M., Prato, L., Spinoso, F., & Tagliente, S. (2026). Analysis Of Linguistic Stereotypes in Single and Multi-Agent Generative AI Architectures. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering, 1656-1666. https://doi.org/10.1145/3803437.3805544

- **Decision:** supporting — This explicitly contrasts single-agent against multi-agent generative architectures, which the protocol admits in any domain, but the measured outcome is dialect-triggered stereotype bias rather than task performance or coordination reliability.
- **Evidence:** full text not read (status: unavailable).

### Pranoto, D. C. Y., Hussien, S. B., Sabariah, S., Bandono, A., & Bahrawi, A. (2026). Architectural Transparency in LLM-Based Cognitive Assessment: A Multidimensional TRACE-ED Evaluation of Single-Agent and Multi-Agent Systems. Research Square. https://doi.org/10.21203/rs.3.rs-8985839/v1

- **Decision:** supporting [preprint] — The recovered abstract is a genuine abstract but truncated mid-sentence after the Purpose statement, so only the framing is visible: a multidimensional TRACE-ED transparency evaluation contrasting single-agent and multi-agent architectures beyond accuracy and score agreement. Retained because architecture-level transparency and traceability criteria are a transferable evaluation instrument for RQ3.
- **Evidence:** Across 900 Monte Carlo runs, splitting scoring from explanation into two agents preserved reliability (ICC(1,k) = 0.9921) and sharply raised grounding and coherence, but introduced a small statistically significant contradiction rate (0.031, d = 0.43) between the scoring and explanation agents, evidencing a measurable coordination cost of decomposition.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, debate-consensus, governance-accountability, reliability-nondeterminism, verification-testing

### Vella, S., Ferworn, A., & Sharieh, M. (2026). ATeam: Governance-Aware LLM-Assisted Software Sustaining Engineering for Enterprise Systems. 2026 6th International Conference on Electrical, Computer and Energy Technologies (ICECET), 1-6. https://doi.org/10.1109/icecet65726.2026.11633274

- **Decision:** supporting — A named LLM-assisted framework for enterprise software sustaining engineering with explicit governance controls, which speaks to the verification/sustainability strand of RQ1; the abstract is unavailable so the depth of any multi-agent comparison cannot be confirmed.
- **Evidence:** In a controlled comparison on 24 IEEE 14764 maintenance tasks over a seven-service microservice testbed, governed template-driven execution beat both an AutoGPT-style structured-reasoning agent and unconstrained prompting with huge effect sizes, while the difference between the agentic baseline and plain prompting was statistically negligible. This is direct evidence that agentic orchestration by…
- **Domains:** comparative-single-vs-multi, governance-accountability, orchestration, reliability-nondeterminism, verification-testing

### Nguyen, D. S. H., Nguyen, M. T., Nguyen, P. T., Di Rocco, J., & Di Ruscio, D. (2026). Automated Summarization of Software Documents: An LLM-based Multi-Agent Approach. arXiv preprint, 33(2). https://doi.org/10.1007/s10515-025-00588-4

- **Decision:** supporting [preprint] — Metagente contributes a named Teacher-Student multi-agent architecture evaluated on real-world software documentation and requirements artifacts, but the reported baselines are not characterized as single-agent configurations, so it supplies an architecture pattern rather than RQ2 comparative evidence.
- **Evidence:** A four-agent teacher-student prompt-refinement system consistently outperformed single-LLM baselines (Mixtral-8x7B, Llama-2-7b, GPT-4o, Gemma-2-2b) on ROUGE and cosine similarity for software document summarization, and an adaptive stopping strategy cut training from 620 to 260 iterations with comparable quality, though the authors note multi-agent orchestration still adds computational overhead.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, role-specialization

### Arora, K., Naim, A., & Sharma, S. (2026). Benchmarking Multi-Agent LLM and Single Agent LLM Efficiency for Contextual Text Generation. 2026 International Conference on Intelligent Systems in Engineering, Secured Systems and Cybersecurity (ICISESSC), 741-745. https://doi.org/10.1109/icisessc68634.2026.11542788

- **Decision:** supporting — Head-to-head single-agent versus retrieval/reasoning/summarization multi-agent comparison on one model (Gemini-Flash) scored with BLEU, ROUGE, METEOR, and BERTScore, concluding multi-agent wins. Qualifies under the any-domain comparison criterion, but the surface-similarity metrics and absence of reported effect sizes or cost accounting keep it below core.
- **Evidence:** A three-agent retriever/reasoner/summarizer pipeline outscored a monolithic single-agent Gemini setup on every reference-overlap metric, but the single-agent arm answered without access to the supporting explanation documents that the multi-agent retriever consumed, so the reported gap confounds retrieval augmentation with multi-agent decomposition.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, orchestration, reliability-nondeterminism, role-specialization

### Moreno-Lumbreras, D., Kula, R. G., & Treude, C. (2026). BonsAIDE: An Extended Vision for Human–AI Interaction in IDEs. ACM Transactions on Software Engineering and Methodology, 35(9), 1-25. https://doi.org/10.1145/3793681

- **Decision:** supporting — BonsAIDE is a named IDE prototype with a 10-participant study on branching and pruning AI-generated code to contain hallucination and track provenance; informs verification and human-oversight aspects of RQ3 but studies a single assistant, not agent teams.
- **Evidence:** full text not read (status: unavailable).

### Rizk, C., Khatoonabadi, S., & Shihab, E. (2026). Bridging Design and Implementation: A Study of Multi-Agent LLM Architectures for Automated Front-End Generation. MSR '26: Proceedings of the 23rd International Conference on Mining Software Repositories, 446-457. https://doi.org/10.1145/3793302.3793371

- **Decision:** supporting — Compares multi-agent architectures for multimodal design-to-code generation, contributing architectural variants for one SE task; the stated gap is modality coverage rather than the conditions under which specialization pays off.
- **Evidence:** full text not read (status: unavailable).

### Blege, A. (2026). Can AI Close the Grant Funding Gap? A Multi-Agent LLM System for Automated Grant Application Generation with Blind Expert Evaluation, Single-Agent Baseline Comparison, and Design Science Research Framework. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.7264680

- **Decision:** supporting [preprint] — The recovered text is a real abstract cut off after one sentence about grant application barriers, so the design must be read from the title: a multi-agent system judged against a single-agent baseline by blinded expert raters within a design science framework. The blinded-expert comparison design is methodologically useful for RQ2 even though grant writing is outside software engineering.
- **Evidence:** full text not read (status: unavailable).

### Becattini, M., Caselli, N., Minin, M., Verdecchia, R., & Vicario, E. (2026). CAPRA: Scaling Feedback on Software Architecture Deliverables with a Multi-Agent LLM System. arXiv preprint. http://arxiv.org/abs/2606.18976v1

- **Decision:** supporting [preprint] — Applies specialized agents to architecture-deliverable review and contributes concrete hallucination-control machinery (deterministic Evidence Anchoring plus a cross-verifying ConsistencyManager agent) plus an eight-criterion evaluation taxonomy, but it reports no single-agent comparison.
- **Evidence:** Adding a deterministic Evidence Anchoring step (normalized Levenshtein fuzzy matching) plus a ConsistencyManager agent to a multi-agent LLM reviewer let CAPRA satisfy 88.8% of eight rubric criteria under strict two-rater aggregation, but reliability collapsed on the interpretive 'Grounded Issues' criterion (50% strict pass, kappa 0.348), so human oversight remains necessary for subjective dimensi…
- **Domains:** benchmarks-evaluation, cost-latency, governance-accountability, human-in-loop, reliability-nondeterminism, requirements-design, verification-testing

### Mohammad, F., Kakar, J. K., Ndong, D. R. B. B., Chas, M., & Ryu, D. (2026). CodeQual-Agent: An Intelligent LLM-Agent Framework for Automated Software Quality Assessment with Explainable Predictions and Real-Time Analysis. 2026 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW), 123-128. https://doi.org/10.1109/icstw72326.2026.00035

- **Decision:** supporting — Neural-symbolic LLM-agent framework anchoring model reasoning on static-analysis metrics, distilled from GPT-4 and Gemini Pro teachers to a Gemini 2.5 Flash student, with 450ms latency, 150,000 evaluated samples, and deployment evidence of a 14% drop in production defect escape. Supplies an ecologically valid architecture and cost/latency data for the RQ1 verification and sustainability strand, but runs no multi-agent comparison.
- **Evidence:** An ablation shows that removing the agent's symbolic/RAG orchestration layer collapses it to a plain LLM and costs 10 F1 points, the same magnitude as removing class balancing, evidencing that grounding LLM reasoning in deterministic static-analysis metrics is what produces the quality gain rather than the LLM alone.
- **Domains:** benchmarks-evaluation, code-generation-repair, cost-latency, orchestration, role-specialization, verification-testing

### Yazdanian, P., Liu, Y., & Li, Z. (2026). Complexity-Ranked Iterative Refactoring from Microservices to LLM-based Multi-Agent Systems. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering, 1557-1564. https://doi.org/10.1145/3803437.3805531

- **Decision:** supporting — Documents an iterative migration method from deterministic microservices to LLM agent orchestration, contributing a refactoring procedure and a candid view of the determinism loss that accompanies agentic transition.
- **Evidence:** full text not read (status: unavailable).

### Issa, K. (2026). Developing and Evaluating an LLM-based Agent for ExplorViz Using CopilotKit. Kiel Software Engineering Research. https://doi.org/10.38071/2026-00397-5

- **Decision:** supporting — A single-agent assistant for program comprehension evaluated in a controlled 11-participant usability study, where deterministic tool-based actions scored 4.82/5 while open-ended agent-driven editing scored only 3.00/5 on expectation match, giving concrete evidence that unconstrained agentic action needs guardrails.
- **Evidence:** A controlled usability study of an LLM assistant embedded in a software visualization tool found a sharp reliability split: deterministic tool-grounded actions were rated near-perfect, while open-ended agent-driven editing scored only 3.00/5 for expectation match with high variance, motivating guardrails such as staged previews, explicit edit scoping and undo support.
- **Domains:** benchmarks-evaluation, cost-latency, human-in-loop, reliability-nondeterminism, requirements-design, verification-testing

### De Oliveira, M. C. S., Ibiyo, M. O., Gianrusso, M., Di Sipio, C., Di Ruscio, D., & Nguyen, P. T. (2026). Developing LLM-based Multi-Agent Systems in Software Engineering: A Mixed-Method Experience Report. arXiv preprint. https://doi.org/10.48550/arxiv.2608.11965

- **Decision:** supporting [preprint] — The empirical comparison is across MAS frameworks on a README summarization task rather than multi-agent versus single-agent, but the null ROUGE result, the missing agent telemetry finding, and the coordination-rule and role-design difficulties are combinable inputs for the verification and observability discussion.
- **Evidence:** A mixed-method comparison of open-source MAS frameworks found good coverage of foundational MAS concepts (roles, coordination rules, message handling) but immature telemetry, benchmarking, and human-in-the-loop support; on a README summarization task no framework dominated statistically (Dify ROUGE-L 0.479 vs Semantic Kernel 0.472, p>0.05) while completion time varied significantly.
- **Domains:** benchmarks-evaluation, communication, memory-context, observability-fault-injection, orchestration

### Di Ruscio, D., Nguyen, P. T., Di Sipio, C., Rubei, R., & Di Rocco, J. (2026). Engineering LLM-based Multi-Agent Systems: A Taxonomy of Emerging Frameworks. IEEE Software, 1-8. https://doi.org/10.1109/ms.2026.3694089

- **Decision:** supporting — Metadata only, but an IEEE Software taxonomy of emerging LLM MAS frameworks provides a practitioner-facing classification scheme for organizing the architecture landscape, which supports synthesis without answering a research question itself.
- **Evidence:** A five-dimension taxonomy derived from 18 systematic studies and 14 frameworks finds that architectural primitives (agents, tools, memory, roles) are mature while monitoring, KPI/value-addition modelling, human feedback, continual evolution, benchmarking, and agent discovery are largely unimplemented, making the robustness of agentic software-engineering solutions hard to justify or reproduce.
- **Domains:** benchmarks-evaluation, communication, governance-accountability, memory-context, observability-fault-injection, orchestration, requirements-design, role-specialization

### Yang-Smith, C., Santos, R. D. S., & Abdellatif, A. (2026). Fairness in Multi-Agent Systems for Software Engineering: An SDLC-Oriented Rapid Review. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering, 1692-1699. https://doi.org/10.1145/3803437.3806715

- **Decision:** supporting — A rapid review mapping LLM/MAS use across the SDLC, which yields a useful phase-by-phase inventory; the fairness lens is a non-functional concern adjacent to, rather than part of, the coordination and reliability questions.
- **Evidence:** full text not read (status: unavailable).

### Zhou, C., Tang, Y., Chen, K., Bai, X., Qi, S., Shen, L., & Zhang, M. (2026). From fragmentation to systematic design: Architecting llm-based multi-agent systems. https://doi.org/10.36227/techrxiv.176827304.41872996/v2

- **Decision:** supporting [preprint] — Contributes architectural guidance on cross-agent memory that extends beyond single-agent state and on shared-versus-competing specialized agent selection, which is a design-level input to RQ2 conditions without itself reporting an SE benchmark.
- **Evidence:** full text not read (status: unavailable).

### Ayon, R. S. (2026). From Helpful to Trustworthy: LLM Agents for Pair Programming. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering, 39-40. https://doi.org/10.1145/3803437.3804875

- **Decision:** supporting — States an explicit limitation of coding agents, that outputs are plausible yet misaligned with developer intent and supply little review evidence, which is a usable framing of the verification gap even though no measurement study is reported.
- **Evidence:** This doctoral research plan argues that a driver/navigator multi-agent pair only earns trust over a single-agent setup when the navigator's critique is constrained to machine-checkable contracts and formal specifications validated by deterministic verifiers, rather than free-form LLM judgment. Preliminary verifier-guided specification synthesis (AutoReSpec, AutoJML) is offered as evidence that it…
- **Domains:** comparative-single-vs-multi, formal-verification, governance-accountability, requirements-design, role-specialization, verification-testing

### Sergeyuk, A., Zakharov, I., Koshchenko, E., & Izadi, M. (2026). Human-AI experience in integrated development environments: a systematic literature review. Empirical Software Engineering, 31(3). https://doi.org/10.1007/s10664-025-10793-0

- **Decision:** supporting — Systematic review of 90 studies on AI-assisted coding inside IDEs that quantifies verification overhead, over-reliance, and correctness/maintainability/security risks, supplying single-assistant baseline evidence for RQ1's verification and reliability strand. It is not multi-agent, so it informs the comparison rather than answering it.
- **Evidence:** A PRISMA systematic review of 90 in-IDE human-AI experience studies finds that productivity gains from AI coding assistance are consistently accompanied by a verification tax: developers spend more time checking output, and reliance miscalibrates in both directions (novices over-rely and under-verify, professionals under-rely and reject correct output lacking a rationale). Research is heavily con…
- **Domains:** benchmarks-evaluation, end-to-end-sdlc, governance-accountability, human-in-loop, verification-testing

### Wang, P., Liu, R., Huang, K., & Du, X. (2026). iRUC: Reducing Inter-Microservice Data Communication in Data-Intensive Systems via Unified Computation. IEEE Transactions on Software Engineering, 52(4), 1198-1214. https://doi.org/10.1109/tse.2026.3656819

- **Decision:** supporting — Employs an LLM-based multi-agent system to parse microservice code and synthesize GraphQL+ models, with throughput and latency measurements across nine open-source projects on a cloud deployment; the agents perform genuine code comprehension and synthesis but the paper evaluates system performance rather than agent topology.
- **Evidence:** full text not read (status: unavailable).

### Youwai, S., Phim, D., Murcia, V. G., & Onas, R. C. (2026). Large language model-based multi-agent systems for automated foundation design: router-driven task classification and expert selection framework. AI in Civil Engineering, 5(1). https://doi.org/10.1007/s43503-026-00088-8

- **Decision:** supporting — Runs an explicit three-way head-to-head of single-agent processing, a designer-checker multi-agent pair, and router-based expert selection across four base models, which is exactly the single-vs-multi contrast RQ2 asks about, but the task domain is geotechnical foundation calculation rather than software engineering and the sample is only 27 cases.
- **Evidence:** Router-driven dispatch to domain-expert agents beat both a single strong agent (95.00% vs 86.25% shallow foundations; 90.63% vs 87.50% pile design with Grok 3) and conventional fixed designer-checker multi-agent workflows by 10.0-43.75 points, while the fixed sequential multi-agent workflows actually underperformed the plain single agent, and the router configuration also had the lowest run-to-ru…
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, governance-accountability, orchestration, reliability-nondeterminism, role-specialization, topology

### Liu, D., Zhou, X., & Li, Y. (2026). Large language model-driven multi-agent framework for fault detection and diagnostics of variable air volume boxes. Architectural Engineering and Design Management, 22(3), 791-808. https://doi.org/10.1080/17452007.2026.2647805

- **Decision:** supporting — Explicitly benchmarks a Planner/Executor/Reporter role-specialized team against a monolithic LLM baseline and reports gains in task completeness and execution reliability, an on-point single-versus-multi comparison weakened by the HVAC diagnostics domain and a 29-unit case study.
- **Evidence:** full text not read (status: unavailable).

### Arumalla, R. K. R. (2026). Leveraging Large Language Model Agents for Autonomous Software Testing and Intelligent Automation. 2026 5th International Conference on Computer Networks, Big Data and IoT (ICCBI), 1013-1017. https://doi.org/10.1109/iccbi68589.2026.11619891

- **Decision:** supporting — Titles an LLM-agent approach to autonomous testing, a targeted SE activity, so it qualifies as an agent application; the absent abstract and minor venue mean it is unlikely to carry comparative evidence.
- **Evidence:** full text not read (status: unavailable).

### He, J., Shi, J., Zhuo, T. Y., Treude, C., Sun, J., Du, X., Xing, Z., & Lo, D. (2026). LLM-as-a-Judge for Software Engineering: Literature Review, Vision, and the Road Ahead. ACM Transactions on Software Engineering and Methodology (TOSEM), Volume 35, Issue 9, 35(9), 1-30. https://doi.org/10.1145/3797276

- **Decision:** supporting — A review of LLM-as-a-judge specifically for SE artifacts supplies the verification and measurement instrumentation that RQ3 asks about, but it evaluates artifacts rather than comparing agent topologies.
- **Evidence:** full text not read (status: unavailable).

### Xu, Z.-G., & Qin, G. (2026). LLM-assisted development of Rust for high-performance bioinformatics software: practices, workflows, and boundaries. Genomics Communications, 3(1), 0-0. https://doi.org/10.48130/gcomm-0026-0018

- **Decision:** supporting — Reports concrete agentic-coding failure modes from building a real Rust tool, naming layer misidentification, semantic drift during script migration, and goal substitution inside agentic loops, which map to RQ3 failure-mode categories. Also documents a tiered workflow (specification-driven design, test-driven development, multi-model parallel exploration) and compiler-based verification as mitigation.
- **Evidence:** Across three real Rust migration projects the authors observed three recurring agentic-coding failure modes — layer misidentification, semantic drift in script migration, and goal substitution in agentic loops — all sharing the structure that the agent optimises observable surface features while the true defect sits one abstraction level below. The countermeasure is process rather than model: eve…
- **Domains:** comparative-single-vs-multi, governance-accountability, human-in-loop, reliability-nondeterminism, requirements-design, verification-testing

### LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns. (2026). https://www.preprints.org/manuscript/202604.2147

- **Decision:** supporting — Its survey of inter-agent communication protocols and emerging orchestration patterns supplies a coordination-mechanism vocabulary for RQ3, but the snippet indicates it deliberately treats single-agent LLM surveys only peripherally and reports no SE-task outcomes.
- **Evidence:** The survey identifies an evaluation vacuum: no widely adopted benchmark targets multi-agent orchestration itself, so coordination quality, communication efficiency, delegation appropriateness, and cost are unmeasured while only task outcomes are scored. It names task duplication, contradictory outputs, and convergence failure as the three canonical coordination failure modes whose frequency rises…
- **Domains:** benchmarks-evaluation, communication, cost-latency, debate-consensus, orchestration, reliability-nondeterminism, security, topology

### Mantzouranidis, S., & Britto, R. (2026). MAS-SRE: A Multi-Agent System for Security Requirements Engineering. PROMISE '26: Proceedings of the 22nd International Conference on Predictive Models and Data Analytics in Software Engineering, 101-110. https://doi.org/10.1145/3803846.3807470

- **Decision:** supporting — Applies a named multi-agent system to standards-grounded security requirements derivation, contributing a role-specialized architecture for an in-scope SE activity, though the abstract signals no single-agent baseline comparison.
- **Evidence:** full text not read (status: unavailable).

### Li, H., Zhang, L., Zhou, H., & Hong, T. (2026). MCP-enabled agentic AI workflow for building energy modelling: framework and use cases. Journal of Building Performance Simulation, 1-27. https://doi.org/10.1080/19401493.2026.2653969

- **Decision:** supporting — Directly contrasts conversational single-assistant MCP tool use against an agentic workflow of coordinating specialized agents on the same EnergyPlus tasks, which satisfies the any-domain single-versus-multi comparison clause even though the domain is building energy modelling.
- **Evidence:** full text not read (status: unavailable).

### Park, G., Lee, S. C., & Park, Y. (2026). Minimizing Response Latency in LLM-Based Agent Systems: A Comprehensive Survey. IEEE Access, 14, 26140-26168. https://doi.org/10.1109/access.2026.3664226

- **Decision:** supporting — Decomposes end-to-end agent latency into a four-layer taxonomy with a dedicated layer on mitigating communication and coordination overhead in collaborative agent ensembles, giving structured evidence for the cost and latency penalty side of multi-agent orchestration.
- **Evidence:** A MetaGPT-versus-ChatDev case study shows that replacing dialogue-driven coordination with a hierarchical SOP pipeline using structured document handoffs cuts end-to-end latency by roughly 29% and simultaneously improves output executability, so coordination topology is a first-order determinant of both speed and reliability.
- **Domains:** benchmarks-evaluation, communication, cost-latency, orchestration, topology

### Xu, X., & Wu, J. (2026). Mitigating LLM Hallucination Snowballing in Multiagent Systems via Context-Aware Semantic Consistency Reasoning. IEEE Transactions on Neural Networks and Learning Systems, 37(8), 3782-3796. https://doi.org/10.1109/tnnls.2026.3655508

- **Decision:** supporting — Formalizes and empirically validates hallucination amplification across sequential multi-agent handoffs with token-level disruption detection and an entailment-clustering mitigation, characterizing a propagation failure mode that RQ3 targets although the tasks are not software engineering.
- **Evidence:** full text not read (status: unavailable).

### Wang, Y., Zhao, Y., Yu, S., Chen, Z., & Gu, Q. (2026). More than a Judge: An Empirical Study of Agent-Human Interaction in Crowdsourced Testing Assessment. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3828168

- **Decision:** supporting — Empirical study of agentic AI in crowdsourced test-report review, which supplies evidence about where agent judgment needs human oversight in a testing workflow; the unit of study is agent-human interaction rather than multi-agent orchestration.
- **Evidence:** full text not read (status: unavailable).

### Abdalla, A. S., Thie, V., Schaub, J., Eisenbarth, M., Lee, S. H., & Andert, J. (2026). Multi-Agent Software Development for Automotive Model-Based Graphical Programming. IEEE Access. https://doi.org/10.2139/ssrn.6253838

- **Decision:** supporting [preprint] — Extends multi-agent software development into model-based graphical programming for automotive systems, a useful specialization case for RQ1's scope even though the journal metadata gives no comparative or failure-mode signal.
- **Evidence:** On a new 38-requirement automotive Simulink benchmark, a role-specialized multi-agent pipeline with an automated test-diagnose-fix loop lifts absolute pass rate from 47.4% for a rulebook-equipped single-agent baseline (and 15.8% for raw prompting) to 73.7%, isolating iterative verification as the dominant contributor.
- **Domains:** benchmarks-evaluation, code-generation-repair, cost-latency, orchestration, reliability-nondeterminism, requirements-design, role-specialization, verification-testing

### Fan, G., Liu, D., Pan, L., Zhang, R., & Guo, Q. (2026). Multi-LLM Persona Generation for Virtual Focus Groups in Software Engineering: A Controlled, Multi-domain Study of Emotional Requirements Elicitation. Proceedings of the ACM on Software Engineering (PACMSE), Volume 3, Issue FSE, 3(FSE), 2027-2048. https://doi.org/10.1145/3808098

- **Decision:** supporting — A controlled multi-domain study using multiple LLM personas for emotional requirements elicitation gives empirical evidence on role-differentiated agents in an SE requirements task, though the contrast is persona configurations rather than single versus multi-agent orchestration.
- **Evidence:** full text not read (status: unavailable).

### Liu, K., Pan, Y., Du, Y., Zhang, L., He, D., & Xiang, Y. (2026). ProjectEvalPlus: An Agentic Software Engineering Benchmark with Automatic Language Extension and User Simulated Evaluation. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3817119

- **Decision:** supporting — Contributes a project-level agentic SE benchmark with user-simulated evaluation, a directly reusable measurement instrument for comparing agent configurations, though the abstract does not claim a single-agent versus multi-agent contrast itself.
- **Evidence:** full text not read (status: unavailable).

### Pham, A. B. B., Nguyen, H. T., & Usman, M. (2026). QBugLM: An Agentic Benchmarking Framework for LLM-based Quantum Software Debugging. 2026 IEEE International Conference on Quantum Software (QSW). https://ieeexplore.ieee.org/document/11662247/

- **Decision:** supporting [preprint] — Named agentic benchmarking framework for debugging, an SE activity, so it contributes a measurement harness; the quantum-software niche limits how far its results transfer to mainstream agent comparisons.
- **Evidence:** In a multi-agent quantum debugging pipeline that separates detection (QBugFind) from repair (QBugFix) and validates with simulation-based total variation distance, iterative feedback dominates every other design choice: a single retry lifts Pass@1 from below 25% to above 80%. Elaborate prompting is not the lever — simple structured prompting beat Chain-of-Thought and ReAct for reasoning-capable m…
- **Domains:** benchmarks-evaluation, code-generation-repair, cost-latency, observability-fault-injection, orchestration, verification-testing

### Xiao, Y.-A., Gao, P., Peng, C., & Xiong, Y. (2026). Reducing Cost of LLM Agents with Trajectory Reduction. Proceedings of the ACM on Software Engineering (PACMSE), Volume 3, Issue FSE, 3(FSE), 1241-1263. https://doi.org/10.1145/3797084

- **Decision:** supporting — Quantifies and reduces the growing input-token cost of multi-turn LLM agent systems on SE tasks, supplying the efficiency and sustainability accounting that RQ1 needs when weighing added agents and turns.
- **Evidence:** Coding-agent trajectories accumulate useless, redundant and expired content that dominates cost; removing it at inference time via a separate reflection module cuts input tokens 39.9-59.7% and total cost 21.1-35.9% while holding resolve rate within -1.0% to +2.0%, contradicting the assumed token-efficiency versus performance trade-off.
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, cost-latency, memory-context, reliability-nondeterminism

### Hossain, E., Nipu, M. H. B., Mahmood, M. S., Hossen, M. J., & Mridha, M. F. (2026). Safe and Scalable Collaboration in Multiagent LLM Systems: A Comprehensive Review. IEEE Transactions on Systems Man and Cybernetics Systems, 1-17. https://doi.org/10.1109/tsmc.2026.3704902

- **Decision:** supporting — Reviews safety and scalability of multiagent LLM collaboration and flags that comparative analysis is hampered by missing baselines, which is a generalizable measurement critique for RQ3 even though the review is not SE-specific.
- **Evidence:** A four-pillar review (coordination, communication, safety, alignment) that synthesises documented multi-agent deployment failures into a cross-system taxonomy, including a coordination-overhead threshold at which added modularity becomes net-negative, semantic drift and herding in long-running systems, and collective harms absent from any individual agent.
- **Domains:** communication, debate-consensus, governance-accountability, orchestration, reliability-nondeterminism, security, topology

### Yuan, T. (2026). Safety-aware AI for oncology trial pre-screening: a comparative study of rule-based, single-agent, and multi-agent approaches. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.6427640

- **Decision:** supporting [preprint] — The recovered abstract is genuine but truncated after the Background sentence on matching eligibility criteria to heterogeneous records; the title establishes a three-arm comparison of rule-based, single-agent, and multi-agent approaches under safety constraints. The deterministic-baseline arm alongside the single/multi arms is a design worth borrowing for high-stakes reliability comparisons.
- **Evidence:** full text not read (status: unavailable).

### Stepin, A., Tolstokulakov, B., Kulikov, V., Kabanov, A., Kubasov, V., Mozikov, M., Gusev, I., & Makarov, I. (2026). ScholForge: A Multi-Agent LLM System for Autonomous Software Engineering Research. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering, 1418-1419. https://doi.org/10.1145/3803437.3807394

- **Decision:** supporting — A named hierarchical multi-agent system whose stage-specialized agents illustrate role decomposition, but the target activity is conducting research rather than the SE lifecycle tasks the RQs center on.
- **Evidence:** full text not read (status: unavailable).

### Zhang, Q., Gao, C., Han, Y., Shang, Y., Fang, C., Chen, Z., & Xiao, L. (2026). SGAgent: Suggestion-Guided LLM-Based Multi-Agent Framework for Repository-Level Software Repair. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3818617

- **Decision:** supporting — A named multi-agent repair framework operating at repository scale, likely benchmarked on SWE-bench-style tasks; valuable as an architecture and results source but the abstract promises no single-agent ablation.
- **Evidence:** full text not read (status: unavailable).

### Jiang, C., Wang, D., Liu, D., Xu, Z., Wen, C., Ming, Z., Liu, Y., Wan, X., & Huang, L. (2026). StarVerus: LLM-Powered Multi-Agent Collaboration for Industrial Rust Code Verification Automation. KDD '26: Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2, 7444-7455. https://doi.org/10.1145/3770855.3818485

- **Decision:** supporting — An industrial multi-agent system for generating Rust/Verus specifications gives a concrete verification-oriented architecture, but the abstract shows no single-agent contrast or coordination failure analysis to answer an RQ directly.
- **Evidence:** full text not read (status: unavailable).

### Haataja, J. (2026). THE CAPABILITIES AND LIMITATIONS OF AI AGENTS IN SOFTWARE DEVELOPMENT. Tampere University Institutional Repository (Tampere University). https://trepo.tuni.fi/bitstream/handle/10024/238728/HaatajaJustus.pdf?sequence=2

- **Decision:** supporting [preprint] — The fragmentary snippet does discuss specialized LMAs and multi-agent versus single-agent architectures in software development, but it reads as a secondary overview with no identifiable venue or original evidence, so it supports rather than settles RQ2.
- **Evidence:** A literature review concluding that multi-agent role specialization buys scalability and parallelism over single agents but introduces coordination overhead and new failure modes, and that benchmark success rates systematically overstate real-world engineering value.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, human-in-loop, reliability-nondeterminism, role-specialization, security

### Hoda, R. (2026). Toward Agentic Software Engineering Beyond Code: Framing Vision, Values, and Vocabulary. AGENT '26: Proceedings of the 2026 International Workshop on Agentic Engineering, 181-185. https://doi.org/10.1145/3786167.3788422

- **Decision:** supporting — A framing paper that defines the vocabulary and research agenda for agentic SE, useful for the future-work and terminology portions of RQ1, but it contributes no empirical comparison or measured failure modes.
- **Evidence:** The paper argues that current agentic SE visions (agentic AI software engineer, USEagent, SASE, AIDev) are almost entirely code-centric, while early empirical evidence shows AI acts as a 'personal accelerator' that does not fix teamwork, coordination, accountability or culture. It proposes a 'whole of process' vision spanning ethical alignment, requirements, design, development and operations, pl…
- **Domains:** end-to-end-sdlc, governance-accountability, human-in-loop, requirements-design, role-specialization

### Lee, Y., & Park, E. (2026). Toward Sustainable Agentic AI Systems: A Survey of Architectures and Methodologies. Sustainable Development. https://doi.org/10.1002/sd.70942

- **Decision:** supporting — Provides a taxonomy of agentic architectures with an explicit resource-efficiency and sustainability dimension plus comparative analysis of open-source framework design patterns, which supports the sustainability and overhead strand of RQ1 without offering SE-task or single-versus-multi evidence.
- **Evidence:** full text not read (status: unavailable).

### Kim, Y., Gu, K., Park, C., Park, C., Schmidgall, S., Heydari, A. A., Yan, Y., Zhang, Z., Zhuang, Y., Liu, Y., Malhotra, M., Liang, P., Park, H. W., Yang, Y., Xu, X., Du, Y., Patel, S., Althoff, T., McDuff, D., & Liu, X. (2026). Towards a Science of Scaling Agent Systems. Research Square. https://doi.org/10.21203/rs.3.rs-8414536/v1

- **Decision:** supporting [preprint] — Studies the principles that determine performance of LM-based agent systems as they scale, which bears directly on RQ2's conditions where adding agents helps or hurts, though the truncated text does not confirm a software engineering task setting. Preprints are eligible under the protocol.
- **Evidence:** A controlled 180-configuration comparison of single-agent versus four multi-agent topologies across four agentic benchmarks derives quantitative scaling principles: a tool-coordination trade-off, a capability saturation point around 45% single-agent accuracy beyond which coordination gives negative returns, and topology-dependent error amplification of 17.2x (independent) versus 4.4x (centralized…
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, orchestration, reliability-nondeterminism, topology

### Dong, T., Shi, S., Sampath, H., & Macvean, A. (2026). Towards AI as a Collaborative Partner: A Taxonomy of AI Agent Behavior in Software Engineering. AIware '26: Proceedings of the 3rd ACM International Conference on AI-Powered Software, 228-237. https://doi.org/10.1145/3805760.3814913

- **Decision:** supporting — Addresses the missing definition and measurement of success as LLMs shift from one-shot generators to agentic SE partners, giving RQ3 a behavioral taxonomy and measurement framing rather than comparative results.
- **Evidence:** full text not read (status: unavailable).

### Rodriguez-Cardenas, D., Li, X., Macedo, M., Mastropaolo, A., Khati, D., Tian, Y., Shao, H., & Poshyvanyk, D. (2026). Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering. FORGE '26: Proceedings of the 2026 IEEE/ACM Third International Conference on AI Foundation Models and Software Engineering, 243-248. https://doi.org/10.1145/3793655.3793716

- **Decision:** supporting — Argues that current SE benchmarks hide robustness, fairness, and efficiency gaps and proposes broader benchmarking infrastructure, which supports the measurement-validity discussion underlying RQ3 without evaluating agent architectures.
- **Evidence:** A survey plus community workshop identifies three barriers to reliable LLM-for-SE evaluation — absent software-engineering-rich datasets, ML-centric metrics, and non-standardized data pipelines — and documents that headline benchmark scores largely reflect memorization: models exceeding 70% on SWE-bench Verified fall to 23% on SWE-bench Pro. Workshop participants concluded that agentic systems sp…
- **Domains:** benchmarks-evaluation, cost-latency, reliability-nondeterminism, security, verification-testing

### Trifković, N., & Antović, I. (2026). Towards Role-Based Multi-Agent LLM Systems for Software Requirements Analysis. 2026 30th International Conference on Information Technology (IT), 1-4. https://doi.org/10.1109/it67293.2026.11435673

- **Decision:** supporting — Role specialization applied to requirements analysis matches the review's central construct, but with no abstract available there is no evidence of a comparative baseline, so it stands as an architectural exemplar.
- **Evidence:** A conceptual role-based architecture pairs redundant small language models per SWEBOK requirements-analysis subtask under a supervisory LLM arbitrator, and its probabilistic model shows that with four independent subprocesses at per-step reliability 0.5 the overall success probability collapses to 0.0625, so acceptable end-to-end reliability requires per-step reliability above 0.90.
- **Domains:** debate-consensus, governance-accountability, reliability-nondeterminism, requirements-design, role-specialization, topology, verification-testing

### Hosseini, M.-P., Shah, A., Qureshi, S., Huang, A., Miao, C., & Wei, W. (2026). Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent LLM Systems. 2026 IEEE 50th Annual Computers, Software, and Applications Conference (COMPSAC), 179-188. https://doi.org/10.1109/compsac69091.2026.00034

- **Decision:** supporting — ReDeRef is a named training-free routing controller using Thompson sampling and judge-driven re-routing that cuts token usage 28%, agent calls 17%, and time-to-first-success 19% against random recursive delegation, and degrades gracefully when an agent or judge is impaired. Contributes a reusable coordination-overhead measurement and a robustness-under-degradation protocol rather than a single- versus multi-agent contrast.
- **Evidence:** Because the split-knowledge tasks are constructed so no single agent can solve them, the study deliberately omits any single-agent baseline and instead isolates routing: belief-guided Thompson-sampling delegation matched random delegation on success (96.65% vs 96.46%) while using 0.72x tokens, 0.83x agent calls, and 0.81x time-to-success.
- **Domains:** cost-latency, governance-accountability, memory-context, orchestration, reliability-nondeterminism, role-specialization, verification-testing

### Essam, M., Wael, K., Hassan, A., Haitham, A., Soliman, M., Saber, S., & Habib, I. (2026). Trust-Aware Multi-Agent Traceability: Confidence-Calibrated Knowledge Graphs for Consistent Software Artifact Management. 2026 15th Mediterranean Conference on Embedded Computing (MECO). https://doi.org/10.48550/arxiv.2606.17203

- **Decision:** supporting [preprint] — Confidence calibration over a traceability knowledge graph is a concrete verification and trust mechanism for multi-agent artifact management, contributing a measurable reliability technique to RQ3 without benchmarking agent counts.
- **Evidence:** In a sequential multi-agent artifact pipeline, upstream low-confidence decisions propagate downstream, so the paper turns calibrated confidence into a first-class coordination signal: threshold gating, divergence detection between derivation-time and validation-time confidence, and conflict materialization as graph nodes.
- **Domains:** communication, debate-consensus, governance-accountability, orchestration, requirements-design, verification-testing

### Elgammal, M. A., Wu, J., Liu, L., Kim, T., & Betz, V. (2026). VTR-LLM: Multi-Agent LLM Framework for Automated Debugging of FPGA CAD Flows. ACM Transactions on Reconfigurable Technology and Systems (TRETS), Just Accepted. https://doi.org/10.1145/3829373

- **Decision:** supporting — Named multi-agent debugging architecture for a complex toolchain; the debugging and configuration-failure setting transfers methodologically, but the FPGA CAD domain is adjacent to rather than inside the SE activities the RQs target.
- **Evidence:** full text not read (status: unavailable).

### Kohl, K., & Carro, L. (2026). When Code Becomes Abundant: Redefining Software Engineering Around Orchestration and Verification. arXiv preprint. https://doi.org/10.1145/3793657.3793884

- **Decision:** supporting [preprint] — Position paper arguing SE must recenter on orchestration, architectural control, and systematic verification under AI automation, and it names accountability collapse as the central risk, which frames the verification and sustainability strands of RQ1.
- **Evidence:** The paper argues the SDLC is being compressed between cheap AI code generation and hardening physical/regulatory constraints, collapsing construction and routine maintenance into two remaining poles of human responsibility: orchestration (intent articulation and architectural control) and verification. Its central named risk is 'accountability collapse' — the erosion of the link between human dec…
- **Domains:** end-to-end-sdlc, governance-accountability, orchestration, requirements-design, verification-testing

### Zabardast, E., Vieira, T., & Gorschek, T. (2025). A 3-Layer Agentic Model for Nonfunctional Requirements in Software Engineering. https://doi.org/10.1109/asew67777.2025.00020

- **Decision:** supporting — Position paper proposing a named three-layer (Data/Agent/Perspective) conceptual model for embedding LLM agents into nonfunctional-requirement assurance across the software lifecycle, framing both quality-of-agents and agents-for-quality. Conceptual only with illustrative examples, so it frames RQ1's verification and reliability dimension without supplying comparative evidence.
- **Evidence:** full text not read (status: unavailable).

### Yazdanian, P., Liu, Y., & Li, Z. (2025). A Comparative Study Towards Designing a Hybrid Architecture of Microservices and LLM-based Multi-Agent Systems. 2025 32nd Asia-Pacific Software Engineering Conference (APSEC), 761-772. https://doi.org/10.1109/apsec66846.2025.00077

- **Decision:** supporting — Compares microservice architecture against LLM multi-agent design to propose a hybrid, so it contributes architectural design guidance and coupling considerations rather than evidence on single-agent versus multi-agent task performance.
- **Evidence:** A structured architectural comparison of microservice systems against LLM-based multi-agent systems, which grounds LLM-MAS failure in design and coordination rather than model quality, and proposes microservice engineering practices (layered separation of concerns, fallback agents, CI/CD test suites, RBAC) as transferable mitigations.
- **Domains:** communication, governance-accountability, observability-fault-injection, orchestration, reliability-nondeterminism, topology, transactions-concurrency

### Rajendran, V., Besiahgari, D., Patil, S. C., Chandrashekaraiah, M., & Challagulla, V. (2025). A Multi-Agent LLM Environment for Software Design and Refactoring: A Conceptual Framework. SoutheastCon 2025, 488-493. https://doi.org/10.1109/southeastcon56624.2025.10971563

- **Decision:** supporting — A conceptual multi-agent framework covering design and refactoring, two lifecycle phases under-represented relative to code generation; conceptual-only status keeps it below core.
- **Evidence:** A conceptual framework arguing that single-agent refactoring optimises one quality attribute at the expense of others, and that domain-specialized agents (performance, security, maintainability, UI/UX) negotiating through consensus or auction protocols can reconcile conflicting objectives; the evaluation is proposed rather than executed.
- **Domains:** code-generation-repair, debate-consensus, governance-accountability, requirements-design, role-specialization, security

### Das, S., Deb, N., Chaki, N., & Cortesi, A. (2025). A Multi-Agent RAG Framework for Regulatory Compliance Checking of Software Requirements. ACM Transactions on Software Engineering and Methodology (TOSEM), Volume 35, Issue 8, 35(8), 1-33. https://doi.org/10.1145/3785472

- **Decision:** supporting — Applies a multi-agent RAG pipeline to requirements compliance checking, contributing a requirements-phase architecture and an evaluation setting, though the framing is manual-inspection replacement rather than multi- versus single-agent comparison.
- **Evidence:** full text not read (status: unavailable).

### Yi, Z., Liu, J., Albert, M. V., & Xiao, T. (2025). A Multi-Agent System for Complex Reasoning in Radiology Visual Question Answering. https://doi.org/10.1109/jcdl67857.2025.00025

- **Decision:** supporting — Evaluates a specialized LLM/MLLM multi-agent pipeline (context understanding, multimodal reasoning, answer validation) against strong single-model MLLM baselines on hard cases, qualifying under the any-domain single-versus-multi inclusion rule. The dedicated validation agent and hallucination framing are relevant to RQ3 verification mechanisms.
- **Evidence:** full text not read (status: unavailable).

### Ray, P. P. (2025). A Review on Vibe Coding: Fundamentals, State-of-the-art, Challenges and Future Directions. https://doi.org/10.36227/techrxiv.174681482.27435614/v1

- **Decision:** supporting [preprint] — Surveys multi-agent, RAG-backed end-to-end code generation platforms and enumerates twelve concrete failure and risk categories (hallucination, technical debt, security, governance) with fourteen research directions, supporting the limitations and future-work strands of RQ1 and RQ3 without primary empirical measurement.
- **Evidence:** full text not read (status: unavailable).

### Zou, H. P., Huang, W., Wu, Y., Chen, Y., Miao, C., Nguyen, H., Zhou, Y., Zhang, W., Fang, L., He, L., Li, Y., Li, D., Jiang, R., Liu, X., & Yu, P. S. (2025). A Survey on Large Language Model based Human-Agent Systems. https://doi.org/10.36227/techrxiv.174612962.26131807/v1

- **Decision:** supporting [preprint] — Surveys human-agent system components including orchestration and communication topologies and human feedback interaction types, motivated explicitly by the reliability, hallucination, and complex-task limits of fully autonomous LLM agents; supports the coordination and reliability framing of RQ3 without SE-specific measurement.
- **Evidence:** full text not read (status: unavailable).

### A Survey on Reliability, Transparency, Accountability, and Fairness in LLM-based Multi-Agent Systems through the Responsibility Lens. (2025). https://www.researchgate.net/profile/Abolfazl-Asudeh/publication/397650899_A_Survey_on_Reliability_Transparency_Accountability_and_Fairness_in_LLM-based_Multi-Agent_Systems_through_the_Responsibility_Lens/links/691933f9de8143098271909a/A-Survey-on-Reliability-Transparency-Accountability-and-Fairness-in-LLM-based-Multi-Agent-Systems-through-the-Responsibility-Lens.pdf

- **Decision:** supporting — Reliability is only one of four responsible-AI properties examined and the SE mention is incidental, so the paper supplies an auditing and accountability lens plus reliability vocabulary for RQ3 rather than measured failure modes or performance comparisons.
- **Evidence:** full text not read (status: unavailable).

### Pan, R., Zhang, H., Jiang, Z., & Hou, R. (2025). AgentDroid: A Multi-Agent Tool for Detecting Fraudulent Android Applications. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 4009-4012. https://doi.org/10.1109/ase63991.2025.00362

- **Decision:** supporting — An ASE-published named multi-agent tool for analyzing Android applications shows role decomposition applied to software analysis and security screening, but the abstract metadata gives no single-agent baseline or coordination-failure discussion.
- **Evidence:** full text not read (status: unavailable).

### Nagvekar, R. (2025). Agentic AI-Driven CI/CD Pipelines for Autonomous Software Delivery. https://doi.org/10.1109/ictbig68706.2025.11323919

- **Decision:** supporting — Presents a layered agentic architecture where goal statements trigger code and test agents through an adaptive CI/CD pipeline to production-ready delivery, discussing feedback loops and self-learning. It names an end-to-end multi-agent lifecycle architecture relevant to RQ1 but supplies no evaluation.
- **Evidence:** full text not read (status: unavailable).

### Yang, Y., Chai, H., & Zhang, W. (2025). AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems. https://doi.org/10.32388/ws0vim

- **Decision:** supporting [preprint] — The snippet confirms a named decentralized coordination architecture benchmarked against both single-agent and centralized multi-agent baselines, which is relevant to RQ2, but no software engineering task or failure-mode measurement is visible, so it contributes a coordination mechanism rather than direct SE evidence.
- **Evidence:** A decentralized DAG-structured framework with retrieval-augmented agent evolution outperformed centralized multi-agent baselines such as MetaGPT and GPTSwarm and matched or beat strong single-agent prompting, but the heterogeneity ablation showed role/model diversity actually hurts small teams and only pays off at larger scale, and several multi-agent baselines fell far below single-agent prompti…
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, memory-context, orchestration, role-specialization, topology

### Choi, S., & Yang, G. (2025). AgentReport: A Multi-Agent LLM Approach for Automated and Reproducible Bug Report Generation. Applied Sciences, 15(22), 11931-11931. https://doi.org/10.3390/app152211931

- **Decision:** supporting — Named seven-module multi-agent LLM pipeline for bug report generation with quantitative CTQRS/ROUGE/SBERT gains over a fine-tuned baseline, giving an SE maintenance data point for role-decomposed pipelines but no single-agent contrast or coordination failure analysis.
- **Evidence:** full text not read (status: unavailable).

### Chen, J., Li, X., Wang, J., Xie, H., Liu, C., Wu, Z., & Lei, Y. (2025). AgentTCP: A Collaborative Multi-Agent Framework for Change-Aware Test Case Prioritization. 2025 32nd Asia-Pacific Software Engineering Conference (APSEC), 634-645. https://doi.org/10.1109/apsec66846.2025.00066

- **Decision:** supporting — Named collaborative multi-agent framework for change-aware test case prioritization, an in-scope testing activity; with only venue metadata available it reads as an architecture-plus-benchmark contribution rather than a single-versus-multi study.
- **Evidence:** full text not read (status: unavailable).

### Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges. Information Fusion, 126(3), 103599-103599. https://doi.org/10.1016/j.inffus.2025.103599

- **Decision:** supporting — Its central contribution is precisely the single-agent versus multi-agent collaborative boundary, contrasting modular task-specific AI Agents with Agentic AI built on multi-agent collaboration and persistent memory, and it names coordination failure, brittleness, and emergent behavior as paradigm-specific failure modes relevant to RQ3.
- **Evidence:** The review separates tool-augmented single "AI Agents" from multi-agent "Agentic AI" and argues each paradigm has its own failure profile: single agents suffer hallucination, shallow planning and prompt brittleness, while multi-agent systems add inter-agent misalignment, error cascades, emergent unpredictability and debugging opacity. It explicitly warns that adding agents is not compositional an…
- **Domains:** communication, comparative-single-vs-multi, memory-context, orchestration, reliability-nondeterminism, security, topology

### Bui, T.-L., Dam, H. K., & Hoda, R. (2025). An LLM-based multi-agent framework for agile effort estimation. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 1032-1043. https://doi.org/10.1109/ase63991.2025.00090

- **Decision:** supporting — A named multi-agent framework applied to an SE planning activity (agile effort estimation) at ASE; it supplies an architecture and task-specific evaluation, but estimation is peripheral to the code generation, repair, and verification focus of the RQs.
- **Evidence:** A role-specialized LLM agent framework for planning-poker effort estimation beats deep-learning state of the art on three of four projects after project-specific fine-tuning, but the accuracy comparison deliberately isolates a single agent, so the multi-agent discussion mechanism is evaluated only through a 12-participant human study.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, debate-consensus, human-in-loop, memory-context, role-specialization

### Avgerinos, V., Ramantas, K., Alonso, L., & Verikoukis, C. (2025). ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control. IEEE Internet of Things Journal, 13(9), 18305-18315. https://doi.org/10.1109/jiot.2025.3648858

- **Decision:** supporting — ARM applies LLM agents to root-cause analysis and remediation over MCP tooling with a reproducible benchmark, reporting only 52.9% SLA-violation identification accuracy and 70.7% mitigation success, which is concrete reliability-ceiling evidence for the operations setting.
- **Evidence:** A single tool-calling LLM agent closes a detect-diagnose-remediate loop over a K3s cloud-edge cluster, but reliability is strongly model-dependent: GPT-5 identifies faults far more accurately and in roughly half the reasoning rounds of the GPT-5-mini baseline, and the binary success metric can score a run successful even when root-cause identification was 0%.
- **Domains:** cost-latency, end-to-end-sdlc, governance-accountability, observability-fault-injection, orchestration, reliability-nondeterminism

### Gandhi, A., De, S., Chećhik, M., Pandit, V., Kiehn, M., Chee, M. C., & Bedasso, Y. (2025). Automated Codebase Reconciliation using Large Language Models. 2025 IEEE/ACM Second International Conference on AI Foundation Models and Software Engineering (Forge), 1-11. https://doi.org/10.1109/forge66646.2025.00011

- **Decision:** supporting — Addresses codebase reconciliation, a real maintenance task, at the Forge venue with citations suggesting empirical grounding; it contributes an LLM technique rather than an agent-orchestration comparison.
- **Evidence:** full text not read (status: unavailable).

### Monteiro, C. E. O., Guerino, L. R., Fernandes, G., Pereira, M. F. P., de Souza-Zinader, J. P., Braga, R. D. B., Pocivi, V. C. B., & Vincenzi, A. M. R. (2025). Automated Generation of End-to-End Web Test Cases via a Generic AI Agent: A Comparative Study of DeepSeek V3 and Claude Sonnet 5. https://doi.org/10.5753/webmedia.2025.16046

- **Decision:** supporting — Empirical SE testing study measuring end-to-end Selenium/JUnit test generation success rates (34.3% vs 70.1%) and per-test cost across two backing models in one agent harness; informs cost and model-pairing effects on agentic SE quality but varies the model rather than the single-versus-multi topology.
- **Evidence:** Wrapping an LLM in a generic AI agent (Suna) that can clone repositories, navigate sites, compile and orchestrate prompts produced usable end-to-end Selenium tests where direct chat-based prompting of the same models had failed to even compile. Model choice dominated outcome quality: Claude Sonnet 4 reached 70.1% successful tests versus DeepSeek V3's 34.3%, but the cheaper model was faster, never…
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, orchestration, reliability-nondeterminism, verification-testing

### Gasmi, T., Guesmi, R., Belhadj, I., & Bennaceur, J. (2025). Bridging AI and Software Security: A Comparative Vulnerability Assessment of LLM Agent Deployment Paradigms. https://doi.org/10.36227/techrxiv.175339471.17113065/v1

- **Decision:** supporting [preprint] — The recovered abstract is genuine but truncated just as the Function Calling comparison arm is introduced, leaving the remaining paradigms and results unknown. Comparative security evaluation of LLM agent deployment paradigms spanning AI-specific and traditional software vulnerabilities is a usable measurement lens for architecture-level risk, though nothing visible establishes a single- versus multi-agent contrast.
- **Evidence:** full text not read (status: unavailable).

### Hou, S., Jiao, H., Shen, Z., Liang, J., Zhao, A., Zhang, X., Wang, J., & Wu, H. (2025). Chain-of-programming (CoP): empowering large language models for geospatial code generation task. International Journal of Digital Earth, 18(1). https://doi.org/10.1080/17538947.2025.2509812

- **Decision:** supporting — Chain-of-Programming decomposes geospatial code generation into five staged roles with a shared information pool and reports 3.0-48.8% gains plus ablations showing each component's necessity; relevant decomposition-versus-monolithic-prompt evidence for a code generation task.
- **Evidence:** full text not read (status: unavailable).

### Yang, G., Zhou, Y., Chen, X., Zheng, W. X., Hu, X., Zhou, X., Lo, D., & Chen, T. (2025). Code-DiTing: Automatic Evaluation of Code Generation without References or Test Cases. https://doi.org/10.1109/ase63991.2025.00021

- **Decision:** supporting — Empirically compares LLM-as-judge families across three datasets, characterises their accuracy, explainability, and compute trade-offs, then distills 1.5B and 7B judges that outperform far larger models and resist preference leakage. Provides verification and measurement machinery plus judge-reliability caveats relevant to RQ3's measurement question.
- **Evidence:** full text not read (status: unavailable).

### Kim, N., & Bae, B. (2025). Conversational AI-Powered Multi-Agent System for Mobile Application Accessibility Compliance: A RAG-Enhanced Pipeline Design. https://doi.org/10.1109/ictc66702.2025.11388949

- **Decision:** supporting — Dual-agent RAG pipeline (Problem Analysis plus Solution Support) for mobile accessibility compliance and remediation is a named role-specialized architecture applied to an SE review/repair activity, though the paper reports only a design with hedged, unmeasured benefit claims.
- **Evidence:** full text not read (status: unavailable).

### Song, H., Göknil, A., Jiang, X., Melum, E., Joe, H., Gazzotti, C., Frascolla, V., Videsjorden, A. N., & Nguyen, P. H. (2025). Developing Multi-Agent LLM Applications Through Continuous Human-LLM Co-Programming. 2025 IEEE/ACM 4th International Conference on AI Engineering – Software Engineering for AI (CAIN), 42-47. https://doi.org/10.1109/cain66642.2025.00013

- **Decision:** supporting — Addresses the engineering process for building multi-agent LLM applications with a human in the loop, contributing development-practice insight rather than performance or failure-mode evidence.
- **Evidence:** COPMA's refactoring patterns treat autonomy as a tunable dial: an autonomous group-manager agent planning workflows produces task misassignment and missing context, so the authors deliberately trade flexibility for predictability by fixing execution order, adding a moderator agent, or replacing the manager with code that orchestrates agents programmatically. Shifting implementations from the 'LLM…
- **Domains:** communication, cost-latency, human-in-loop, orchestration, reliability-nondeterminism, role-specialization

### Parthasarathy, K., Vaidhyanathan, K., Dhar, R., Krishnamachari, V., Kakran, A., Akshathala, S., Arun, S., Karan, A., Muhammed, B., Dubey, S., & Veerubhotla, M. (2025). Engineering LLM Powered Multi-Agent Framework for Autonomous CloudOps. 2025 IEEE/ACM 4th International Conference on AI Engineering – Software Engineering for AI (CAIN), 201-211. https://doi.org/10.1109/cain66642.2025.00031

- **Decision:** supporting — Metadata-only record, but the title unambiguously names an LLM multi-agent framework for cloud operations, an in-scope SE activity; the 21 citations suggest a usable architecture reference despite the missing abstract.
- **Evidence:** In an industrial CloudOps deployment, replacing a monolithic single-LLM RAG system with the six-agent MOYA framework improved every automated metric against SME gold-standard answers and cut human-reported defects from 22 to 15, with the largest gain in misclassification; despite consuming more tokens, the multi-agent system was faster end-to-end.
- **Domains:** comparative-single-vs-multi, cost-latency, end-to-end-sdlc, human-in-loop, orchestration, reliability-nondeterminism

### Li, Z., & Izadi, M. (2025). Enhancing Human-IDE Interaction in the SDLC using LLM-based Mediator Agents. FSE Companion '25: Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering, 1363-1367. https://doi.org/10.1145/3696630.3728721

- **Decision:** supporting — Proposes a mediator-agent architecture that brokers between developers, IDEs, and SDLC agents, contributing an integration and role-separation pattern relevant to orchestration design.
- **Evidence:** full text not read (status: unavailable).

### Huang, J., Jin, D., Sun, W., Liu, Y., & Jin, Z. (2025). Envisioning Intelligent Requirements Engineering via Knowledge-Guided Multi-Agent Collaboration. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 3876-3880. https://doi.org/10.1109/ase63991.2025.00334

- **Decision:** supporting — An ASE vision paper proposing knowledge-guided multi-agent collaboration for requirements engineering; it contributes an architectural proposal and research agenda for an in-scope SE phase without empirical single-versus-multi evidence.
- **Evidence:** full text not read (status: unavailable).

### Ronanki, K. (2025). Facilitating Trustworthy Human-Agent Collaboration in LLM-based Multi-Agent System oriented Software Engineering. FSE Companion '25: Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering, 1333-1337. https://doi.org/10.1145/3696630.3728717

- **Decision:** supporting — Asserts rather than demonstrates that MAS outperform singular agents in SE, and the truncated abstract points to a trust and human-oversight vision contribution, so it informs the verification and accountability discussion without supplying comparative results.
- **Evidence:** full text not read (status: unavailable).

### Wang, H., Sui, Y., Xie, Y., Liu, Y., Sun, Y., Shi, C., & Zhang, Y. (2025). Fixing Broken Graphs: LLM-Powered Automatic Code Optimization for DNN Programs. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 1718-1730. https://doi.org/10.1109/ase63991.2025.00144

- **Decision:** supporting — An ASE paper presenting an LLM-powered technique for automatically optimizing DNN program graphs, contributing a repair/optimization method with presumed empirical evaluation but no agent-orchestration dimension.
- **Evidence:** full text not read (status: unavailable).

### Treude, C., & Storey, M.-A. (2025). Generative AI and Empirical Software Engineering: A Paradigm Shift. https://doi.org/10.1109/aiware69974.2025.00033

- **Decision:** supporting — Vision paper on how LLMs and autonomous agents break empirical SE constructs, reproducibility, and threats to validity; directly informs how the review should read agent-evaluation claims and their ecological validity.
- **Evidence:** full text not read (status: unavailable).

### Nguyen‐Duc, A., Cabrero‐Daniel, B., Przybyłek, A., Arora, C., Khanna, D., Herda, T., Rafiq, U., Melegati, J., Guerra, E., Kemell, K., Saari, M., Zhang, Z., Le, H. Q., Quan, T., & Abrahamsson, P. (2025). Generative Artificial Intelligence for Software Engineering—A Research Agenda. Software Practice and Experience, 55(11), 1806-1843. https://doi.org/10.1002/spe.70005

- **Decision:** supporting — Literature review plus focus groups yielding 78 open research questions across 11 SE areas, documenting where GenAI evidence is thin (requirements, design) and which dependability, accuracy, and sustainability concerns recur, which grounds the future-work component of RQ1.
- **Evidence:** full text not read (status: unavailable).

### Wang, Z. (2025). Identifying Performance-Sensitive Configurations in Software Systems with LLM-Driven Agents. 2025 IEEE/ACM 47th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion), 222-223. https://doi.org/10.1109/icse-companion66252.2025.00069

- **Decision:** supporting — Applies LLM-driven agents to a concrete SE maintenance/performance-analysis activity (configuration sensitivity), so it contributes an agent application and likely empirical evidence, but the metadata shows no single-agent versus multi-agent comparison or coordination-failure analysis.
- **Evidence:** full text not read (status: unavailable).

### Large language model agents: A comprehensive survey on architectures, capabilities, and applications. (2025). https://www.preprints.org/manuscript/202512.2119

- **Decision:** supporting — General-purpose agent survey that explicitly performs a systematic architecture comparison and reports multi-agent gains over single-agent baselines, giving cross-domain RQ2 signal without any software engineering specificity.
- **Evidence:** The survey reports that multi-agent groups consistently outperform single agents on complex tasks needing diverse expertise (AgentVerse, DERA on MedQA, MetaGPT at 85.9%/87.7% Pass@1 on HumanEval/MBPP), while cataloguing the coordination failure modes that role-playing introduces: conversation deviation from the original objective, role flipping between assistant and user, and unreliable terminati…
- **Domains:** benchmarks-evaluation, communication, comparative-single-vs-multi, debate-consensus, memory-context, reliability-nondeterminism, role-specialization, topology

### Feischl, C., & Kern, R. (2025). Large Language Models for Code Translation: An In-Depth Analysis of Code Smells and Functional Correctness. ACM Transactions on Software Engineering and Methodology, 35(8), 1-40. https://doi.org/10.1145/3777383

- **Decision:** supporting — Large empirical study across LLMs, languages, and prompts showing code quality is largely independent of correctness, and that non-determinism exploitation, iterative repair, and LLM collaboration can each improve outcomes. The collaboration and non-determinism findings give measured signal for RQ1's performance and reliability dimensions on a translation activity.
- **Evidence:** full text not read (status: unavailable).

### Solovyeva, L., Oliveira, E. C., Fan, S., Tuncay, A., Gareev, S., & Capiluppi, A. (2025). Leveraging LLMs for Automated Translation of Legacy Code: A Case Study on PL/SQL to Java Transformation. https://doi.org/10.1145/3756681.3757007

- **Decision:** supporting — Industrial legacy-modernization case study evaluating multiple LLMs with a chain-of-guidance plus n-shot prompting strategy, and it states validation limits from the small paired-code sample and restricted test access.
- **Evidence:** full text not read (status: unavailable).

### Mamatha, G., Joshi, V. V., & Manur, P. T. (2025). LLM - Driven Autonomous Cloud Automation Agent. https://doi.org/10.1109/csitss67709.2025.11295499

- **Decision:** supporting — Named LLM-driven agent architecture for cloud/DevSecOps operations evaluated on MTTR, policy-enforcement accuracy, and responsiveness against traditional automation; supplies single-agent operations evidence for the operations end of the SE activity range.
- **Evidence:** full text not read (status: unavailable).

### Chen, B., Babikian, A. A., Feng, S., Varró, D., & Mussbacher, G. (2025). LLM-based Satisfiability Checking of String Requirements by Consistent Data and Checker Generation. https://doi.org/10.1109/re63999.2025.00030

- **Decision:** supporting — Empirically evaluates four LLMs on checking satisfiability of natural-language string requirements by generating SMT and Python checkers, doubling success rate and F1 over unchecked baselines. Gives concrete evidence on LLM-plus-external-verifier reliability for a requirements activity, though no agent configurations are compared.
- **Evidence:** full text not read (status: unavailable).

### Bin Shahid, W., Naqvi, B., & Afzal, H. (2025). LLMPathy: A Multi-Agent LLM Approach for Eliciting Inclusive Security Requirements. 2025 IEEE 33rd International Requirements Engineering Conference Workshops (REW), 243-248. https://doi.org/10.1109/rew66121.2025.00037

- **Decision:** supporting — Named multi-agent LLM approach for eliciting inclusive security requirements, an in-scope requirements activity; the workshop format and absent abstract suggest an architecture contribution rather than a comparative study.
- **Evidence:** full text not read (status: unavailable).

### Xu, Y. (2025). MUARF: Leveraging Multi-Agent Workflows for Automated Code Refactoring. 2025 IEEE/ACM 47th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion), 226-227. https://doi.org/10.1109/icse-companion66252.2025.00071

- **Decision:** supporting — Named multi-agent workflow for automated refactoring, an in-scope maintenance activity; the ICSE companion format suggests a tool or short empirical report that supplies an architecture rather than a topology comparison.
- **Evidence:** full text not read (status: unavailable).

### Li, S., Jia, X., Tam, W. F., Tabaro, L., Li, Q., Liu, G., Wang, C., & Abdelmoniem, A. M. (2025). Multi-agent collaboration mechanisms: A survey of llms. arXiv preprint. https://doi.org/10.2139/ssrn.7243979

- **Decision:** supporting [preprint] — Provides a general taxonomy of LLM collaboration mechanisms that is useful vocabulary for classifying coordination structures in RQ3, but it is domain-agnostic and the snippet shows no software engineering application or measured failure analysis.
- **Evidence:** The survey states the multi-agent advantage is conditional on collaboration design rather than intrinsic: well-designed collaboration channels let multi-agent systems beat single agents, but a poorly designed competitive multi-agent system can be beaten by a single agent given strong prompts.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, debate-consensus, orchestration, role-specialization, topology

### Muhammad, A., Mohammed, M. A., Milanova, M., Talburt, J. R., & Cakmak, M. C. (2025). Multi-Agent RAG Framework for Entity Resolution: Advancing Beyond Single-LLM Approaches with Specialized Agent Coordination. Computers, 14(12), 525. https://doi.org/10.20944/preprints202510.2382.v1

- **Decision:** supporting — Decomposes household entity resolution into four task-specialized LangGraph agents and reports 94.3% accuracy plus a 61% reduction in API calls versus monolithic single-LLM approaches. The efficiency-through-specialization result is a combinable data point on coordination cost even though the domain is record linkage rather than software engineering.
- **Evidence:** A four-agent LangGraph RAG pipeline for entity resolution beat a single-LLM GPT-4 baseline on accuracy (93.9% vs 86.9%) while simultaneously cutting tokens ~62%, API calls >60%, and runtime 52%, attributed to selective retrieval per agent and shared state memory that avoids redundant inference.
- **Domains:** comparative-single-vs-multi, cost-latency, governance-accountability, orchestration, reliability-nondeterminism, role-specialization

### Chang, E. Y. (2025). Multi-LLM Agent Collaborative Intelligence. ACM eBooks. https://doi.org/book/10.1145/3749421

- **Decision:** supporting — MACI orchestrates multiple LLM agents specifically to compensate for single-model weaknesses in long-range planning, self-critique, and context loss; the failure modes named generalize to SE coordination even though the book is domain-agnostic.
- **Evidence:** full text not read (status: unavailable).

### Li, W., Manickam, S., Chong, Y.-W., & Karuppayah, S. (2025). PhishDebate: An LLM-Based Multi-Agent Framework for Phishing Website Detection. arXiv preprint, 6606-6615. https://doi.org/10.1109/BigData66926.2025.11401440

- **Decision:** supporting [preprint] — Outside software engineering, but it reports a clean quantitative comparison of a four-role debate architecture against single-agent and chain-of-thought baselines, which is admissible cross-domain evidence for when role specialization plus debate helps under RQ2.
- **Evidence:** A four-specialist debate framework with Moderator and Judge lifted accuracy from 67.00% (single-agent direct prompting) and 90.70% (single-agent chain-of-thought) to 93.90%, largely by eliminating indecisive 'uncertain' outputs, but average inference time rose from 4.7 s to 37.5 s, roughly an eightfold latency cost.
- **Domains:** comparative-single-vs-multi, cost-latency, debate-consensus, security, verification-testing

### Yu, M. (2025). PreEduAI: A Multi-Agent Collaborative Framework for Automated Preschool Curriculum Development. IEEE Access, 14, 5255-5267. https://doi.org/10.1109/access.2025.3646282

- **Decision:** supporting — Four-role multi-agent framework benchmarked against standalone GPT-4.1, Claude-3.5-Sonnet, Llama-3-8B, and Gemini-2.5-Pro with an ablation isolating the collaboration gain (+0.95); a usable out-of-domain data point on when role specialization beats a single model, but the task is curriculum authoring, not software.
- **Evidence:** full text not read (status: unavailable).

### Spieker, H., Matricon, T., Belmecheri, N., Betten, J. E., Lyan, G., Borges, H., Mazouni, Q., Gross, D., Gotlieb, A., & Acher, M. (2025). Prompting for Performance: Exploring LLMs for Configuring Software. https://doi.org/10.1109/ictai66417.2025.00023

- **Decision:** supporting — Empirical evaluation of several LLMs on software configuration tasks (option identification, configuration ranking and recommendation) that documents hallucination and superficial reasoning as concrete limitations of prompt-only single-model use.
- **Evidence:** full text not read (status: unavailable).

### Lu, X., Sun, W., Zhang, Y., Hu, M., Tian, C., Jin, Z., & Liu, Y. (2025). Requirements Development and Formalization for Reliable Code Generation: A Multi-Agent Vision. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), 3932-3937. https://doi.org/10.1109/ase63991.2025.00345

- **Decision:** supporting — Links requirements formalization to code-generation reliability through a multi-agent vision, offering a verification-oriented pipeline proposal for RQ3 but presenting a research direction rather than measured outcomes.
- **Evidence:** full text not read (status: unavailable).

### Reid, A., O'Callaghan, S., Carroll, L., & Caetano, T. (2025). Risk analysis techniques for governed LLM-based multi-agent systems. arXiv preprint. https://doi.org/10.48550/arxiv.2508.05687

- **Decision:** supporting [preprint] — Offers risk-analysis techniques and critique-comparison metrics for interacting specialized agents, and notes that multi-agent structure can sometimes mitigate single-agent failures, but the governance and business-unit framing keeps it outside direct SE evidence.
- **Evidence:** The report argues multi-agent deployment transforms rather than merely adds to the risk landscape, naming six failure modes (cascading reliability failures, inter-agent communication failures, monoculture collapse, conformity bias, deficient theory of mind, mixed-motive dynamics), and prescribes explicit single-agent baselining to test whether coordination actually improves performance at all.
- **Domains:** communication, comparative-single-vs-multi, debate-consensus, governance-accountability, observability-fault-injection, reliability-nondeterminism

### Becattini, M., Verdecchia, R., & Vicario, E. (2025). SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems. 2025 IEEE/ACM International Workshop New Trends in Software Architecture (SATrends), 5-8. https://doi.org/10.1109/satrends66715.2025.00006

- **Decision:** supporting — Metadata-only SATrends paper, but the title names a reference software architecture for LLM multi-agent systems, making it a citable architectural contribution for the design-space discussion.
- **Evidence:** SALLMA motivates a role-specialized multi-agent architecture directly from single-agent deficiencies (no task-specific tuning, no persistent memory, no ground-truth validation, static centralized deployment) and separates an Operational Layer for runtime orchestration from a Knowledge Layer holding workflow and agent metamodels.
- **Domains:** end-to-end-sdlc, memory-context, orchestration, requirements-design, role-specialization

### Liu, E. (2025). SE-Blackboard: A Shared-State Architecture for Multi-Agent Software Engineering Pipelines. IEEE Access. https://doi.org/10.5281/zenodo.18911614

- **Decision:** supporting — A blackboard shared-state design targets the context-loss and handoff problems that plague agent pipelines, making it a directly relevant coordination mechanism; the record carries only journal metadata, so it is retained as an architecture rather than as RQ evidence.
- **Evidence:** Holding the agent pipeline fixed and varying only the communication architecture, a shared-state blackboard raises Coder-stage information fidelity by 62% and correct file targeting by 27.5 percentage points over message passing, yet end-to-end resolve rate improves only 4 points because all configurations converge to a ~22% conditional resolve rate once the right file is found. The bottleneck is…
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, cost-latency, orchestration, reliability-nondeterminism

### Nguyen, D. S. H., Truong, B. G., Nguyen, P. T., Di Rocco, J., & Di Ruscio, D. (2025). Teamwork makes the dream work: LLMs-Based Agents for GitHub README.MD Summarization. FSE Companion '25: Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering, 621-625. https://doi.org/10.1145/3696630.3728511

- **Decision:** supporting — Applies a collaborating team of LLM agents to a repository documentation task, giving a concrete multi-agent design point for an SE artefact; the truncated abstract does not indicate a single-agent baseline, which would otherwise make it core.
- **Evidence:** full text not read (status: unavailable).

### Gröpler, R., Klepke, S., Johns, J., Dreschinski, A., Schmid, K., Dornauer, B., Tüzün, E., Noppen, J., Mousavi, M. R., Tang, Y., Viehmann, J., Aslangül, S. Ş., Lee, B. S., Ziolkowski, A., & Zie, E. (2025). The Future of Generative AI in Software Engineering: A Vision From Industry and Academia in the European Genius Project. https://doi.org/10.1109/aiware69974.2025.00026

- **Decision:** supporting — Consortium vision paper from 30+ European industry and academic partners structuring current GenAI adoption challenges across the full SDLC around reliability, accountability, security, and privacy, plus anticipated role shifts; supplies practitioner-grounded future-work input for RQ1 but no empirical comparison.
- **Evidence:** full text not read (status: unavailable).

### Kennedy, D. (2025). The Operational Protocol Method: Systematic LLM Specialization Through Collaborative Persona Engineering and Agent Coordination. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.5397903

- **Decision:** supporting [preprint] — The recovered abstract is real but truncated after the opening problem statement, which nonetheless names three concrete specialization failure modes: context drift, personality inconsistency, and failure to prioritize curated knowledge. Those named degradation modes plus a protocol-based persona-engineering method are combinable with RQ3's failure-mode taxonomy, though no software engineering evaluation is visible.
- **Evidence:** full text not read (status: unavailable).

### Dam, H. K. (2025). Towards Multi-Agentic AI for automated software design and modelling: challenges and opportunities. https://doi.org/10.1109/asew67777.2025.00063

- **Decision:** supporting — Proposes a conceptual multi-agentic framework for design and modelling and enumerates coordination hazards including requirement ambiguity, intra- and inter-model consistency, and conflict resolution when merging design model versions. These named failure modes inform RQ3 even though no measurement or empirical study is reported.
- **Evidence:** full text not read (status: unavailable).

### Yazdanian, P., & Liu, Y. (2025). Towards Scenario-Driven Reference Architecture for Integrating Microservices and LLM-Based Multi-Agent Systems. 2025 IEEE International Conference on Collaborative Advances in Software and COmputiNg (CASCON), 607-608. https://doi.org/10.1109/cascon66301.2025.00107

- **Decision:** supporting — Proposes a reference architecture for embedding LLM multi-agent systems into microservice landscapes, which supplies architectural vocabulary for the design and operations side of RQ1 without measuring agent-count effects.
- **Evidence:** full text not read (status: unavailable).

### Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). Vibe Coding vs. Agentic Coding: Fundamentals and Practical Implications of Agentic AI. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2505.19443

- **Decision:** supporting [preprint] — Review contrasting human-in-the-loop prompt-driven coding against autonomous goal-driven agentic coding, with a taxonomy of execution models, feedback loops, safety mechanisms, and 20 use cases indicating where each paradigm succeeds. Provides conditions-for-autonomy framing relevant to RQ2 but compares interaction paradigms rather than single-agent versus multi-agent configurations.
- **Evidence:** A taxonomic review contrasting human-in-the-loop 'vibe coding' with autonomous 'agentic coding', arguing that agentic scalability will come from orchestrator-coordinated specialized sub-agents rather than a monolithic agent, while cataloguing agentic failure modes of overdependence, silent error propagation across modules, and expanded runtime privilege as security surface.
- **Domains:** comparative-single-vs-multi, end-to-end-sdlc, governance-accountability, human-in-loop, observability-fault-injection, orchestration, reliability-nondeterminism, role-specialization, security

### Baresi, L., Camilli, M., Dolci, T., & Quattrocchi, G. (2024). A Conceptual Framework for Quality Assurance of LLM-based Socio-critical Systems. 2024 39th IEEE/ACM International Conference on Automated Software Engineering (ASE), 2314-2318. https://doi.org/10.1145/3691620.3695306

- **Decision:** supporting — Offers a QA conceptualization for LLM-based systems in high-stakes settings, which is combinable with the verification strand of RQ3, though it targets deployed LLM systems generally rather than multi-agent SE pipelines.
- **Evidence:** full text not read (status: unavailable).

### Sun, Z., Du, X., Yang, Z., Li, L., & Lo, D. (2024). AI Coders Are among Us: Rethinking Programming Language Grammar towards Efficient Code Generation. https://doi.org/10.1145/3650212.3680347

- **Decision:** supporting — Empirical code-generation study quantifying 10-13% token reduction from an AI-oriented Python grammar, providing evidence on token/inference cost that bears on the efficiency side of orchestration overhead.
- **Evidence:** Human-oriented programming grammar imposes a measurable token tax on LLM inference; an AI-oriented grammar (SimPy) that preserves the Python AST cuts token usage by 13.5% (CodeLlama) and 10.4% (GPT-4) while models trained Python-then-SimPy match or exceed their Python baselines.
- **Domains:** benchmarks-evaluation, code-generation-repair, cost-latency

### Mandal, I., Soni, J., Zaki, M., Smedskjær, M. M., Wondraczek, K., Wondraczek, L., Gosvami, N. N., & Krishnan, N. M. A. (2024). Autonomous Microscopy Experiments through Large Language Model Agents. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2501.10385

- **Decision:** supporting [preprint] — AFMBench evaluates GPT-4o and GPT-3.5 agents across an experimental workflow and reports a significant performance decline specifically in multi-agent coordination scenarios plus instruction non-adherence and task divagation. The multi-agent degradation and drift evidence speaks to RQ2's underperformance conditions, but the domain is microscopy rather than software engineering.
- **Evidence:** In a controlled ablation on the same task subset, the role-specialized multi-agent configuration beat direct single-agent tool integration only for the strongest model (GPT-4o, 70% vs 58% success); weaker models showed minimal difference because they failed the cross-domain coordination the topology was meant to exploit, and single-agent architectures retained the compute and latency advantage.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, orchestration, reliability-nondeterminism, role-specialization, topology

### Taeb, M., Swearngin, A., Schoop, E., Cheng, R., Jiang, Y., & Nichols, J. (2024). AXNav: Replaying Accessibility Tests from Natural Language. https://doi.org/10.1145/3613904.3642777

- **Decision:** supporting — Builds an LLM plus pixel-based UI system that executes natural-language accessibility test instructions and flags issues, validated in a 10-participant study with accessibility QA professionals. Supplies single-agent capability evidence on a realistic testing activity with unusually strong ecological validity for RQ1.
- **Evidence:** full text not read (status: unavailable).

### Kang, S., Chen, B., Yoo, S., & Lou, J. (2024). Explainable automated debugging via large language model-driven scientific debugging. Empirical Software Engineering, 30(2). https://doi.org/10.1007/s10664-024-10594-x

- **Decision:** supporting — AutoSD couples an LLM with a debugger in a hypothesis-test loop, reports results on three repair benchmarks against baselines, and adds a 20-participant study on explanation-aided patch judgment, giving verification and human-oversight evidence for single-agent repair.
- **Evidence:** Wrapping a single LLM in a debugger-grounded hypothesis-experiment-observation loop yields repair performance competitive with direct LLM patch generation while producing explanations that improved developer patch-correctness judgments in five of six real-world bugs, at a cost of 4.66x longer runtime and a regression on Defects4J v1.2.
- **Domains:** benchmarks-evaluation, code-generation-repair, cost-latency, governance-accountability, human-in-loop, observability-fault-injection, verification-testing

### Yoon, J., Feldt, R., & Yoo, S. (2024). Intent-Driven Mobile GUI Testing with Autonomous Large Language Model Agents. https://doi.org/10.1109/icst60714.2024.00020

- **Decision:** supporting — DroidAgent is a named autonomous LLM testing agent with long- and short-term memory that reaches 61% activity coverage against 51% for state-of-the-art GUI testing baselines on the Themis benchmark. It is a measured single-agent architecture on a testing activity, useful as a single-agent reference point rather than a multi-agent comparison.
- **Evidence:** full text not read (status: unavailable).

### Zhou, X., Cao, S., Sun, X., & Lo, D. (2024). Large Language Model for Vulnerability Detection and Repair: Literature Review and the Road Ahead. ACM Transactions on Software Engineering and Methodology, 34(5), 1-31. https://doi.org/10.1145/3708522

- **Decision:** supporting — Systematic review of 58 papers on LLMs for vulnerability detection and repair with an explicit limitations and roadmap section; strong background for the verification and security dimension of RQ3 but not agent-architecture focused.
- **Evidence:** full text not read (status: unavailable).

### Hou, X., Zhao, Y., Liu, Y., Yang, Z., Wang, K., Li, L., Luo, X., Lo, D., Grundy, J., & Wang, H. (2024). Large Language Models for Software Engineering: A Systematic Literature Review. ACM Transactions on Software Engineering and Methodology, 33(8), 1-79. https://doi.org/10.1145/3695988

- **Decision:** supporting — The canonical LLM4SE synthesis of 395 articles establishing the SE task taxonomy, dataset practices, and performance optimization and evaluation strategies that later agentic work builds on, though its window closes in January 2024 and it predates the multi-agent comparison question.
- **Evidence:** full text not read (status: unavailable).

### Lubos, S., Felfernig, A., Tran, T. N. T., Garber, D., Mansi, M. E., Erdeniz, S. P., & Le, V.-M. (2024). Leveraging LLMs for the Quality Assurance of Software Requirements. https://doi.org/10.1109/re59067.2024.00046

- **Decision:** supporting — Empirical RE 2024 study where a single LLM assesses requirements against ISO 29148 quality characteristics, explains its decisions, and proposes rewrites, validated with practising software engineers. Provides a single-agent quality-assurance baseline for the requirements-side comparison in RQ2.
- **Evidence:** A single LLM instructed against the ISO 29148 quality characteristics achieves high recall but low precision when human software engineers are treated as ground truth, so it works as a reviewer aid that surfaces candidate flaws with plausible explanations rather than as an autonomous quality gate.
- **Domains:** benchmarks-evaluation, governance-accountability, human-in-loop, requirements-design, verification-testing

### Abrahamyan, D., & Fard, F. H. (2024). StackRAG Agent: Improving Developer Answers with Retrieval-Augmented Generation. 2024 IEEE International Conference on Software Maintenance and Evolution (ICSME), 893-897. https://doi.org/10.1109/icsme58944.2024.00098

- **Decision:** supporting — A named single-agent RAG architecture for developer question answering that documents a grounding/retrieval design pattern reusable in agent pipelines; it offers no multi-agent condition to compare against.
- **Evidence:** full text not read (status: unavailable).

### Cinkusz, K., & Chudziak, J. A. (2024). Towards LLM-augmented multiagent systems for agile software engineering. ASE '24: Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering, 2476-2477. https://doi.org/10.1145/3691620.3695336

- **Decision:** supporting — Sketches a cognitive MAS+LLM ecosystem mapped onto Agile practice; it contributes an architectural proposal for role-based SE agents but the truncated abstract shows no evaluation or single-agent baseline.
- **Evidence:** full text not read (status: unavailable).

### Chen, C., Su, J., Chen, J., Wang, Y., Bi, T., Yu, J., Wang, Y., Lin, X., Chen, T., & Zheng, Z. (2024). When ChatGPT Meets Smart Contract Vulnerability Detection: How Far Are We?. ACM Transactions on Software Engineering and Methodology, 34(4), 1-30. https://doi.org/10.1145/3702973

- **Decision:** supporting — Empirical evaluation of a single LLM on a security-analysis SE task with precision/recall breakdown, false-positive root-cause categories, and an explicit robustness limitation (uncertainty, code-length limits), which supplies a single-agent baseline reference point.
- **Evidence:** full text not read (status: unavailable).

### Fu, M. C., Tantithamthavorn, C., Nguyen, V., & Le, T. (2023). ChatGPT for Vulnerability Detection, Classification, and Repair: How Far Are We?. https://doi.org/10.1109/apsec60848.2023.00085

- **Decision:** supporting — Large-scale empirical comparison of a single ChatGPT agent against specialized code models on prediction, classification, severity and repair over 190k C/C++ functions, establishing where an unaugmented single LLM underperforms on SE tasks.
- **Evidence:** full text not read (status: unavailable).

### Liu, J., Xia, C. S., Wang, Y., & Zhang, L. (2023). Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2305.01210

- **Decision:** supporting [preprint] — EvalPlus augments HumanEval test cases 80x and shows pass@k drops of 19.3-28.9% plus outright mis-ranking of models under insufficient tests. This is direct evidence that benchmark weakness can manufacture apparent performance differences, which bears on how single-agent versus multi-agent gains in RQ1 should be trusted.
- **Evidence:** Test insufficiency in the standard HumanEval suite inflates measured correctness and, more damagingly for comparative claims, reorders model rankings: augmenting tests 80x drops pass@k by up to 19.3-28.9% and flips which models appear best.
- **Domains:** benchmarks-evaluation, code-generation-repair, verification-testing

### Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2303.11366

- **Decision:** supporting [preprint] — Foundational single-agent architecture that replaces weight updates with verbal self-reflection stored in an episodic memory buffer, reaching 91% pass@1 on HumanEval with ablations over feedback signals and agent types. It defines the strong self-improving single-agent baseline that multi-agent claims in RQ2 must beat.
- **Evidence:** Verbal self-reflection over an episodic memory buffer lifts a single agent to 91.0 pass@1 on HumanEval versus 80.1 for GPT-4, but the gain is bounded by the quality of the agent's self-generated tests: on MBPP Python a 16.3% false-positive test rate makes Reflexion underperform its own baseline, and ablating test generation drops accuracy below baseline (52% vs 60%).
- **Domains:** benchmarks-evaluation, code-generation-repair, memory-context, reliability-nondeterminism, verification-testing

### Garlapati, A., Parmesh, M. N. V. S. S. M., Savitha, & S, J. (n.d.). AI-Powered Multi-Agent Framework for Automated Unit Test Case Generation: Enhancing Software Quality through LLM’s. 2024 5th IEEE Global Conference for Advancement in Technology (GCAT). https://ieeexplore.ieee.org/document/10923987/

- **Decision:** supporting — A multi-agent framework for unit test generation covers the testing activity in scope and supplies an application data point, though the metadata-only record shows no comparative or failure-mode analysis.
- **Evidence:** full text not read (status: unavailable).
