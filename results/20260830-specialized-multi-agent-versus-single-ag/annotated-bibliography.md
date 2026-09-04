# Annotated Bibliography — specialized multi-agent versus single-agent LLM software engineering: comparative performance, coordination failures, verification, reliability, sustainability, and future work

Generated 2026-09-04 from screening decisions, evidence-ledger notes, and quality scores. Working material and audit evidence — not submission text.

## Core (44)

### [No author listed] (2026). An empirical comparison of multi-agent LLM architectural patterns for automated unit test generation. https://gupea.ub.gu.se/items/fef996e4-da73-462a-98cc-3cb1eaffd966

- **Decision:** core — This empirical software-testing study compares a single-agent baseline with multiple specialist multi-agent patterns for unit-test generation.
- **Evidence:** Sequential achieved 92.2% success (83/90), 91.6% line coverage, 90.6% branch coverage, and 83% cross-run consistency (25/30 tasks). Single-agent achieved 81.1% (73/90), 80.6% line, 79.7% branch, and 67% consistency (20/30). Hierarchical achieved 54.4% (49/90), about 54% coverage, and 47% consistency (14/30). No paired statistical test establishes uncertainty on the 11.1-point sequential advantage.
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, comparative-single-vs-multi, cost-latency, governance-accountability, human-in-loop, memory-context, orchestration, reliability-nondeterminism, role-specialization, security, topology, verification-testing

### Nguyen, D. S. H., Nguyen, M. T., Nguyen, P. T., Di Rocco, J., & Di Ruscio, D. (2026). Automated summarization of software documents: an LLM-based multi-agent approach. Automated Software Engineering. https://doi.org/10.1007/s10515-025-00588-4

- **Decision:** core — This empirical SE study compares a Teacher-Student multi-agent architecture with independent single LLMs for requirements and technical-document summarization and reports better baseline performance.
- **Evidence:** full text not read (status: unavailable).

### Radeva, I., Noncheva, T., Doukovska, L., & Popchev, I. (2026). Comparing Single-Agent and Multi-Agent Strategies in LLM-Based Title-Abstract Screening. https://doi.org/10.20944/preprints202603.2107.v1

- **Decision:** core — This controlled screening study finds a few-shot single agent outperforms voting, ensemble, confidence-weighted, and debate strategies, supplying direct negative evidence on coordination value.
- **Evidence:** The best reported configuration was single-agent Qwen 2.5 7B few-shot: recall 100.0%, precision 70.4%, F1 82.6%, WSS@95 43.4%, with 69 TP, 29 FP, 0 FN, and 92 TN on N = 190. The best multi-agent configuration, two-stage Qwen to Mistral+LLaMA few-shot, obtained recall 100.0%, precision 61.6%, F1 76.2%, and WSS@95 36.0% (43 FP).
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, debate-consensus, governance-accountability, human-in-loop, memory-context, orchestration

### Huang, J., Ye, W., Sun, W., Feng, Y., & Liu, Y. (2026). Cross-Model Collaboration for Enhancing LLM-Based Code Generation. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3840382

- **Decision:** core — CMCS directly compares collaborative LLM handoffs with constituent single models across eight code benchmarks and quantifies accuracy, scaling, and cost trade-offs.
- **Evidence:** CodeQwen plus DeepSeek CMCS achieved 93.29% HumanEval and 91.83% MBPP Pass@1. On MBPP it exceeded same-model CMCS with CodeQwen (75.09%) and DeepSeek (80.93%), giving the clearest evidence that complementary model errors matter.
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, comparative-single-vs-multi, cost-latency, governance-accountability, memory-context, orchestration, reliability-nondeterminism, topology, verification-testing

### Kehkashan, T., Abdullah, M., Al-Shamayleh, A. S., Ivković, N., Ismail, N. A., Ahmad, S. S. S., Rehman, A., & Akhunzada, A. (2026). From benchmarks to deployment: a comprehensive review of agentic AI evaluation. Artificial Intelligence Review. https://doi.org/10.1007/s10462-026-11571-0

- **Decision:** core — This systematic audit of 15 agent benchmarks uses software development as its primary case and directly exposes security, cost, and deployment-evaluation gaps.
- **Evidence:** Across the 15 reviewed benchmarks, security is absent in 15/15 primary evaluation schemes; cost is only partially represented by action counts in 2/15 and absent in 13/15; safety is partial in 1/15; robustness is partial in 3/15. The conclusion summarizes that 13/15 rely on binary success as the sole criterion and 14/15 do not measure trajectory quality.
- **Domains:** benchmarks-evaluation, cost-latency, end-to-end-sdlc, governance-accountability, human-in-loop, memory-context, orchestration, reliability-nondeterminism, security, verification-testing

### Wang, P., Liu, R., Huang, K., & Du, X. (2026). iRUC: Reducing Inter-Microservice Data Communication in Data-Intensive Systems via Unified Computation. IEEE Transactions on Software Engineering. https://doi.org/10.1109/tse.2026.3656819

- **Decision:** core — This nine-project study uses an LLM multi-agent system to parse microservice code and synthesize executable cross-service models with measured system gains.
- **Evidence:** All 606 normal, boundary, and exceptional tests passed for the generated GraphQL+ documents. Functionality checking took at most four iterations and syntax checking at most three, with averages of 2.0 and 2.3 iterations.
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, comparative-single-vs-multi, cost-latency, governance-accountability, memory-context, orchestration, reliability-nondeterminism, role-specialization, security, verification-testing

### Calboreanu, E. (2026). Iterative Audit Convergence in LLM-Managed Multi-Agent Systems: A Case Study in Prompt-Engineering Quality Assurance. Software. https://doi.org/10.3390/software5020026

- **Decision:** core — This SE production-pipeline case study empirically tests iterative multi-agent auditing, defect convergence, cross-model coverage, and inter-rater reliability.
- **Evidence:** Nine rounds surfaced 51 defects with per-round counts 15, 8, 12, 2, 8, 1, 4, 1, and 0; the observed trend was non-monotonic and ended after one clean pass.
- **Domains:** benchmarks-evaluation, communication, governance-accountability, human-in-loop, orchestration, reliability-nondeterminism, requirements-design, verification-testing

### Rasheeda, Z., Waseema, M., Kemella, K.-K., Saari, M., & Abrahamsson, P. (2026). LLM-Based Multi-Agent Systems for Code Generation: A Multi-Vocal Literature Review. arXiv preprint. https://doi.org/10.2139/ssrn.6332149

- **Decision:** core [preprint] — This multi-vocal review directly synthesizes the use of LLM multi-agent systems for software code generation.
- **Evidence:** Only 29 of 114 studies (25.4%) reported reasons for using agents; performance enhancement appeared in 12 (10.5%), complex-task handling in 9 (7.9%), operational efficiency/scalability in 7 (6.1%), and team collaboration in 6 (5.3%).
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, comparative-single-vs-multi, cost-latency, end-to-end-sdlc, governance-accountability, human-in-loop, memory-context, orchestration, reliability-nondeterminism, role-specialization, security, verification-testing

### Jia, J., Deng, Z., Chen, Z., Wang, Y., & Zheng, Z. (2026). MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems. arXiv (Cornell University). http://arxiv.org/abs/2602.19843

- **Decision:** core [preprint] — MAS-FIRE directly evaluates coordination faults across architectures and shows that closed-loop topology neutralizes failures that collapse linear workflows.
- **Evidence:** MetaGPT's shared message pool was associated with more than 90% robustness under critical-information loss versus about 67% for Camel, and Table-Critic retained more than 89% under planning faults versus MetaGPT as low as 43.84%; these cross-system differences are also task- and implementation-confounded.
- **Domains:** benchmarks-evaluation, communication, debate-consensus, governance-accountability, human-in-loop, memory-context, observability-fault-injection, orchestration, reliability-nondeterminism, role-specialization, security, topology, verification-testing

### Seyedghorban, Z., Klimov, E., van Deursen, A., Panichella, A., & Ozkan, B. K. (2026). Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering. 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST). https://doi.org/10.1109/icst69053.2026.00037

- **Decision:** core — This SE-specific tool directly validates trace-aligned observability and controlled fault injection on a real software-development multi-agent system.
- **Evidence:** In the demo, a 1-second LLM delay produced mean/median amplification of 1.053/1.036, while the A2A delay produced 1.295/1.390.
- **Domains:** benchmarks-evaluation, communication, cost-latency, end-to-end-sdlc, governance-accountability, observability-fault-injection, orchestration, reliability-nondeterminism, verification-testing

### Ao, R., Gao, S., & Simchi-Levi, D. (2026). On the Reliability Limits of LLM-Based Multi-Agent Planning. arXiv (Cornell University). https://doi.org/10.2139/ssrn.6490578

- **Decision:** core [preprint] — This theoretical and experimental contrary result shows that delegated multi-agent planning is dominated by a centralized decision maker with the same information.
- **Evidence:** The formal ceiling is conditional: without new exogenous signals, internal messages and randomization cannot improve on a centralized Bayes decision maker with all available signals. In common-evidence serial chains, each communication step contributes nonnegative information loss under log loss unless it preserves the relevant posterior.
- **Domains:** benchmarks-evaluation, communication, comparative-single-vs-multi, cost-latency, governance-accountability, human-in-loop, memory-context, orchestration, reliability-nondeterminism, topology, verification-testing

### Sanabria, D. (2026). OpenAI single-agent LLM architecture reduces computational overhead relative to multi-agent orchestration in a simulated mars rover decision-support benchmark. Frontiers in Robotics and AI. https://doi.org/10.3389/frobt.2026.1877762

- **Decision:** core — This controlled contrary study finds that multi-agent orchestration adds substantial latency and token cost without reliable quality gains for short-context tool-less tasks.
- **Evidence:** GPT-4o single versus multi: decision accuracy 0.810 versus 0.734; exact hazard F1 0.081 versus 0.043; semantic hazard F1 0.131 versus 0.106; mean latency 2.32 s versus 11.83 s; mean tokens 458 versus 2,273.
- **Domains:** benchmarks-evaluation, communication, comparative-single-vs-multi, cost-latency, governance-accountability, orchestration, reliability-nondeterminism, role-specialization

### Gokbulut, B. (2026). Preventing Wrong Work Item Retrieval in LLM-Based MCP Systems Through Multi-Agent Validation. 2026 4th Cognitive Models and Artificial Intelligence Conference (AICCONF). https://doi.org/10.1109/aicconf69182.2026.11600651

- **Decision:** core — This empirical SE-tooling study evaluates specialized Executor-Validator-Refiner middleware on 120 GitHub MCP queries, reporting zero wrong retrievals with negligible measured overhead.
- **Evidence:** Under the paper's definition, the middleware produced 0 confident wrong items in 120 trials and all 50 semantic queries triggered clarification. This measures ambiguity detection, not eventual retrieval of the user's intended item; the paper says that end-to-end semantic retrieval requires a user study with intent labels.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, governance-accountability, human-in-loop, memory-context, orchestration, reliability-nondeterminism, role-specialization, security, verification-testing

### Orogat, A., Rostam, A., & Mansour, E. (2026). Understanding multi-agent LLM frameworks: A unified benchmark and experimental analysis. arXiv preprint. https://arxiv.org/abs/2602.03128

- **Decision:** core [preprint] — This unified benchmark experimentally compares single-agent and multi-agent framework settings while controlling the underlying model.
- **Evidence:** For the trivial fixed query, direct calls had 0.38-second median latency and 8.88 requests/second, while Concordia had 44.47-second median latency and 0.089 requests/second, approximately 117 times the median latency.
- **Domains:** benchmarks-evaluation, communication, comparative-single-vs-multi, cost-latency, governance-accountability, memory-context, orchestration, reliability-nondeterminism, role-specialization, topology, verification-testing

### Rotar, C., & Zhang, Q. (2025). A design science research approach to Large Language Model-Based Agents for Requirements Specification (LLMBA4RS) in low-code applications. Requirements Engineering. https://doi.org/10.1007/s00766-025-00450-9

- **Decision:** core — This empirical requirements-engineering study evaluates a CrewAI-and-RAG agent method across three low-code applications with practitioner assessment.
- **Evidence:** full text not read (status: unavailable).

### Di Sipio, C., De Oliveira, M. C. S., Di Ruscio, D., Nguyen, P. T., & Rubei, R. (2025). Agentware in software engineering: A taxonomy for leveraging llms-based multi-agent systems. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.5273078

- **Decision:** core [preprint] — This taxonomy directly examines LLM-based multi-agent systems and framework selection in software engineering.
- **Evidence:** full text not read (status: unavailable).

### Tawosi, V., Ramani, K., Alamir, S., & Liu, X. (2025). ALMAS: an Autonomous LLM-based Multi-Agent Software Engineering Framework. 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW). https://doi.org/10.1109/asew67777.2025.00059

- **Decision:** core — This primary SE multi-agent framework maps agile roles across the SDLC and demonstrates end-to-end application generation and feature addition with human-team integration.
- **Evidence:** The prototype completes one Streamlit application-generation workflow and one subsequent feature augmentation using common task-management and version-control tools. This establishes feasibility only.
- **Domains:** code-generation-repair, cost-latency, end-to-end-sdlc, formal-verification, human-in-loop, memory-context, orchestration, requirements-design, role-specialization, verification-testing

### Bui, T.-L., Dam, H. K., & Hoda, R. (2025). An LLM-based multi-agent framework for agile effort estimation. 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE). https://doi.org/10.1109/ase63991.2025.00090

- **Decision:** core — This empirical SE multi-agent framework uses coordinated discussion and human participation for agile effort estimation and reports superior benchmark results plus positive practitioner findings.
- **Evidence:** The fine-tuned standalone SEEAgent is best across all three metrics on DM, ME, and US, but not TD. On ME it records MAE 1.217, MMRE 0.414, and PRED(50) 0.747; on US it records 0.350, 0.085, and 1.000.
- **Domains:** benchmarks-evaluation, communication, debate-consensus, human-in-loop, memory-context, requirements-design, role-specialization

### Zeng, Z., Li, Y., Xie, R., Ye, W., & Zhang, S. (2025). Benchmarking and Studying the LLM-based Agent System in End-to-End Software Development. arXiv preprint. https://arxiv.org/abs/2511.04064

- **Decision:** core [preprint] — This end-to-end software-development benchmark directly studies single-agent versus multi-agent architecture effects under a specialized codebase toolset.
- **Evidence:** Table 3 reports mean requirement implementation rates of 49.48% for SDAgent-DT, 45.72% for SDAgent-Single, and 27.71% for SDAgent-DDT. With Gemini-2.5-Pro specifically, DT reaches 53.50%, versus 42.97% for Single and 32.79% for DDT. With Flash, however, Single reaches 48.46% and DT 45.47%, a negative result against any universal multi-agent advantage.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, cost-latency, end-to-end-sdlc, governance-accountability, memory-context, orchestration, reliability-nondeterminism, requirements-design, role-specialization, verification-testing

### Cai, Y., Li, R., Liang, P., Shahin, M., & Li, Z. (2025). Designing LLM-based multi-agent systems for software engineering tasks: Quality attributes, design patterns and rationale. arXiv preprint. https://arxiv.org/abs/2511.08475

- **Decision:** core [preprint] — This SE-specific study examines a four-specialist transition from single-agent design and derives quality attributes, patterns, and design rationale.
- **Evidence:** Code generation accounts for 45 of 94 studies (47.9%); only 7 cover end-to-end development (7.4%) and 8 end-to-end maintenance (8.5%).
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, cost-latency, debate-consensus, end-to-end-sdlc, governance-accountability, human-in-loop, memory-context, orchestration, reliability-nondeterminism, requirements-design, role-specialization, security, topology, verification-testing

### Tomic, S., Alégroth, E., & Isaac, M. (2025). Evaluation of the Choice of LLM in a Multi-Agent Solution for GUI-Test Generation. 2025 IEEE Conference on Software Testing, Verification and Validation (ICST). https://doi.org/10.1109/icst62969.2025.10989038

- **Decision:** core — This empirical GUI-testing study evaluates 27 model-to-agent assignments and finds homogeneous model use can outperform heterogeneous specialization by reducing coordination inconsistency.
- **Evidence:** For individual fixed websites, a homogeneous constellation is among the best: Gemma2/Gemma2/Gemma2 reaches F1 0.889 on demo1, Llama/Llama/Llama reaches 0.947 on Ikea, and both reach 0.667 on Netonnet. The authors reject H1 that mixed models outperform on a specific site.
- **Domains:** benchmarks-evaluation, communication, cost-latency, governance-accountability, memory-context, orchestration, reliability-nondeterminism, role-specialization, verification-testing

### Lu, R., Li, Y., & Huo, Y. (2025). Exploring Autonomous Agents: A Closer Look at Why They Fail When Completing Tasks. https://doi.org/10.1109/ase63991.2025.00330

- **Decision:** core — A benchmark across agent frameworks and LLM backbones exposes roughly 50 percent completion and a phase-based failure taxonomy for robust agent engineering.
- **Evidence:** With GPT-4o, overall success was 50.00% for TaskWeaver, 47.06% for MetaGPT, and 38.24% for AutoGen. With GPT-4o-mini it was 58.82%, 50.00%, and 50.00%, respectively.
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, cost-latency, governance-accountability, human-in-loop, memory-context, observability-fault-injection, orchestration, reliability-nondeterminism, topology, verification-testing

### Feischl, C., & Kern, R. (2025). Large Language Models for Code Translation: An In-Depth Analysis of Code Smells and Functional Correctness. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3777383

- **Decision:** core — The empirical code-translation study tests collaborative LLMs alongside single-model, prompt, and repair strategies and reports conditional quality gains.
- **Evidence:** full text not read (status: unavailable).

### He, J., Treude, C., & Lo, D. (2025). LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3712003

- **Decision:** core — This software-engineering-focused literature review directly synthesizes LLM multi-agent systems and their research agenda.
- **Evidence:** The review maps 71 studies across requirements engineering, code generation, quality assurance, maintenance, and end-to-end development, but does not estimate a causal multi-agent advantage over single agents.
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, comparative-single-vs-multi, cost-latency, debate-consensus, end-to-end-sdlc, governance-accountability, human-in-loop, memory-context, orchestration, reliability-nondeterminism, requirements-design, role-specialization, security, topology, verification-testing

### Mao, C., Su, Y., & Li, D. (2025). LogExpertSolver: A Multi-Agent Framework for Domain-Specialized Log Parsing. 2025 32nd Asia-Pacific Software Engineering Conference (APSEC). https://doi.org/10.1109/apsec66846.2025.00108

- **Decision:** core — This empirical software-engineering study evaluates a domain-specialized multi-agent log parser on LogHub2.0 and reports gains over two state-of-the-art parsers.
- **Evidence:** Average parsing accuracy was 0.915, versus 0.853 for LibreLog and 0.842 for LILAC, corresponding to 6.2% and 7.3% absolute-relative wording used by the paper.
- **Domains:** benchmarks-evaluation, communication, comparative-single-vs-multi, cost-latency, governance-accountability, memory-context, observability-fault-injection, orchestration, reliability-nondeterminism, role-specialization, security

### Wang, S., Zhong, Z., Wen, S., & Liu, Y. (2025). Multi-Agent Assisted Automatic Test Generation for Java JSON Libraries. https://doi.org/10.1109/apsec66846.2025.00064

- **Decision:** core — JsonATG empirically shows that specialized summarization and validation agents outperform two LLM test-generation methods and uncover confirmed library bugs.
- **Evidence:** JsonATG achieved substantially higher instruction coverage on JSON, JSONPath, JSONReader, and JSONWriter, but ChatTester/ChatUniTest were higher on JSONArray and JSONObject.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, cost-latency, governance-accountability, human-in-loop, orchestration, reliability-nondeterminism, role-specialization, security, verification-testing

### Nguyen, D. S. H., Truong, B. G., Nguyen, P. T., Di Rocco, J., & Di Ruscio, D. (2025). Teamwork makes the dream work: LLMs-Based Agents for GitHub README.MD Summarization. https://doi.org/10.1145/3696630.3728511

- **Decision:** core — The paper directly investigates cooperative LLM agents on a GitHub repository-documentation task, making it primary empirical MAS-for-SE evidence.
- **Evidence:** With 50 training examples, Metagente achieved average ROUGE-1/2/L of 0.522/0.363/0.486 versus 0.282/0.152/0.250 for single GPT-4o, gains of 85.11%, 138.82%, and 94.40%.
- **Domains:** benchmarks-evaluation, communication, comparative-single-vs-multi, cost-latency, governance-accountability, memory-context, orchestration, reliability-nondeterminism, role-specialization

### Mao, Z., Keung, J., Zhang, F., Liu, S., Wang, Y., & Li, J. (2025). Towards Engineering Multi-Agent LLMs: A Protocol-Driven Approach. https://doi.org/10.1109/apsec66846.2025.00100

- **Decision:** core — This empirical SE study directly evaluates a protocol layer that reduces multi-agent failures through behavioral contracts, structured messaging, lifecycle control, and verification.
- **Evidence:** On HumanEval, total judged failures fall from 256 to 92 with GPT-4.1-nano (64.1%) and from 112 to 34 with DeepSeek-V3 (69.6%). Under-specification falls by 71.5% and 73.0%, respectively.
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, formal-verification, governance-accountability, orchestration, reliability-nondeterminism, role-specialization, security, verification-testing

### Barrak, A. (2025). Traceability and Accountability in Role-Specialized Multi-Agent LLM Pipelines. 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW). https://doi.org/10.1109/asew67777.2025.00064

- **Decision:** core — This benchmark study tests eight Planner-Executor-Critic configurations, showing structured accountable handoffs reduce error propagation while exposing role-specific risk and task-dependent cost-latency trade-offs.
- **Evidence:** Best monolithic Gemini accuracy was 92.40% on AGIEval (median 11.84 s, $0.0112/prompt), 99.21% on PythonIO (11.20 s, $0.0120), and 84.45% on LogiQA (14.78 s, $0.0134). By Table III, the best accountable pipeline reached 93.54%, 99.21%, and 85.16%, respectively: +1.14 points, a tie, and +0.71 versus the best single model, without uncertainty estimates.
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, comparative-single-vs-multi, cost-latency, governance-accountability, orchestration, reliability-nondeterminism, role-specialization, verification-testing

### Yu, Z., Fang, A., Ma, M., Walia, J. S., Zhang, C., Chi, S., Li, Z., Chintalapati, M., Zhang, X., Wang, R., Bansal, C., Rajmohan, S., Lin, Q., Zhang, S., Pei, D., & He, P. (2025). Triangle: Empowering Incident Triage with Multi-Agent. https://doi.org/10.1109/ase63991.2025.00062

- **Decision:** core — Triangle empirically validates specialized roles, negotiation, and automated mitigation for end-to-end incident triage in a real production cloud.
- **Evidence:** Across six production services after deployment, reported triage accuracy is 92%, 82%, 96%, 64%, 96%, and 97%; before-after TTE reductions are 18%, 91%, 48%, 72%, 61%, and 67%. Team D's 64% accuracy is a negative result linked by manual inspection to sparse templated descriptions.
- **Domains:** benchmarks-evaluation, communication, cost-latency, debate-consensus, governance-accountability, human-in-loop, memory-context, orchestration, reliability-nondeterminism, role-specialization

### Zhang, H., Cheng, W., Wu, Y., & Hu, W. (2024). A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement. https://doi.org/10.1145/3691620.3695506

- **Decision:** core — PairCoder directly compares specialized Navigator and Driver agents with direct LLM prompting and reports substantial pass-at-one gains across code benchmarks.
- **Evidence:** With GPT-3.5, PairCoder reaches 87.80% pass@1 on HumanEval and 15.15% on CodeContest-test, versus 67.68% and 6.06% for direct prompting. With DeepSeek-Coder it reaches 85.37% and 14.55%, versus 76.22% and 6.67%. The reported relative gains are largest on CodeContest, where initial plans fail more often.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, cost-latency, memory-context, role-specialization, verification-testing

### Qian, C., Liu, W., Liu, H., Chen, N., Dang, Y., Li, J., Yang, C., Chen, W., Su, Y.-S., Cong, X., Xu, J., Li, D., Liu, Z., & Sun, M. (2024). ChatDev: Communicative Agents for Software Development. https://doi.org/10.18653/v1/2024.acl-long.810

- **Decision:** core — The title directly identifies an LLM multi-agent software-development system, making it a core retrieval candidate despite the metadata-only abstract.
- **Evidence:** ChatDev scored 0.5600 completeness, 0.8800 executability, 0.8021 consistency, and 0.3953 composite quality, versus GPT-Engineer's 0.5022, 0.3583, 0.7887, and 0.1419.
- **Domains:** benchmarks-evaluation, code-generation-repair, communication, comparative-single-vs-multi, cost-latency, debate-consensus, end-to-end-sdlc, governance-accountability, human-in-loop, memory-context, orchestration, reliability-nondeterminism, requirements-design, role-specialization, security, topology, verification-testing

### Wang, H., Liu, Z., Wang, S., Cui, G., Ding, N., Liu, Z., & Ge, Y. (2024). INTERVENOR: Prompting the Coding Ability of Large Language Models with the Interactive Chain of Repair. https://doi.org/10.18653/v1/2024.findings-acl.124

- **Decision:** core — INTERVENOR empirically evaluates specialized Code Learner and Code Teacher roles with compiler feedback against direct-model baselines on SE tasks.
- **Evidence:** INTERVENOR reaches 75.6% and 69.8% pass@1 on HumanEval and MBPP versus 60.3% and 39.8% for unassisted GPT-3.5. Across the reported code-generation and translation tasks, the authors summarize gains over GPT-3.5 as about 18% and 4.3%, respectively.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, cost-latency, role-specialization, security, verification-testing

### Islam, M. A., Ali, M. E., & Parvez, M. R. (2024). MapCoder: Multi-Agent Code Generation for Competitive Problem Solving. https://doi.org/10.18653/v1/2024.acl-long.269

- **Decision:** core — MapCoder empirically evaluates four specialized agents spanning retrieval, planning, generation, and debugging across eight code benchmarks, providing direct primary SE multi-agent evidence.
- **Evidence:** With GPT-4, MapCoder reached 93.9% HumanEval, 83.1% MBPP, 22.0% APPS, 45.3% xCodeEval, and 28.5% CodeContests Pass@1. Relative gains over direct prompting were largest on APPS and CodeContests.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, cost-latency, governance-accountability, memory-context, orchestration, reliability-nondeterminism, role-specialization, security, verification-testing

### Mao, Z., Li, J., Jin, D., Li, M., & Tei, K. (2024). Multi-Role Consensus Through LLMs Discussions for Vulnerability Detection. https://doi.org/10.1109/qrs-c63300.2024.00173

- **Decision:** core — This primary empirical SE study evaluates developer and tester LLM roles reaching consensus for vulnerability detection and reports sizable precision, recall, and F1 gains.
- **Evidence:** Averaged across dataset groups, vulnerability categories, and prompt variants, the paper reports multi-role relative increases of 13.48% in precision, 18.25% in recall, and 16.13% in F1 over the single-role approach.
- **Domains:** comparative-single-vs-multi, cost-latency, debate-consensus, role-specialization, security, verification-testing

### Hu, S., Huang, T., İlhan, F., Tekin, S. F., & Liu, L. (2023). Large Language Model-Powered Smart Contract Vulnerability Detection: New Perspectives. https://doi.org/10.1109/tps-isa58951.2023.00044

- **Decision:** core — GPTLens empirically compares a role-separated auditor and critic pipeline with one-stage vulnerability detection and exposes the recall and false-positive tension from stochastic sampling.
- **Evidence:** With one Auditor producing up to three candidates plus a Critic, the contract-level hit ratio rises from 38.5% for one-stage one-candidate auditing to 76.9%, and the trial-level ratio rises from 33.3% to 46.2%.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, human-in-loop, role-specialization, security, verification-testing

### Lima, I., Linhares, V., Gomes, A. M., & Maia, P. H. (n.d.). A Catalogue of Evaluation Metrics for LLM-Based Multi-Agent Frameworks in Software Engineering. AGENT '26: Proceedings of the 2026 International Workshop on Agentic Engineering. https://doi.org/10.1145/3786167.3788430

- **Decision:** core — The catalogue directly organizes evaluation metrics for LLM multi-agent frameworks performing software-engineering tasks.
- **Evidence:** The catalogue contains 38 metrics: outcome measures such as requirements met and pass@k; process measures such as duration, tokens, utterances, iterations, rework, and per-agent use; product measures such as errors, dead code, and messages per line; and framework measures for human involvement and ease of use.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, cost-latency, governance-accountability, human-in-loop, reliability-nondeterminism, security

### Shafin, W. I., Rafi, M. N., Li, Z., & Chen, T.-H. (n.d.). An Empirical Study of Waterfall-style Multi-Agent Workflows for Class-Level Code Generation. PROMISE '26: Proceedings of the 22nd International Conference on Predictive Models and Data Analytics in Software Engineering. https://doi.org/10.1145/3803846.3807461

- **Decision:** core — This empirical study directly evaluates a staged multi-agent software-development workflow for class-level code generation.
- **Evidence:** Role-specialized Waterfall processing is not uniformly better than one direct agent: full-workflow class Pass@1 falls from 0.35 to 0.21 for GPT-4o-Mini and from 0.46 to 0.32 for DeepSeek-Chat, while Claude-3.5-Haiku rises from 0.21 to 0.22.
- **Domains:** code-generation-repair, communication, comparative-single-vs-multi, orchestration, reliability-nondeterminism, role-specialization, verification-testing

### Rizk, C., Khatoonabadi, S., & Shihab, E. (n.d.). Bridging Design and Implementation: A Study of Multi-Agent LLM Architectures for Automated Front-End Generation. MSR '26: Proceedings of the 23rd International Conference on Mining Software Repositories. https://doi.org/10.1145/3793302.3793371

- **Decision:** core — The study directly examines multi-agent LLM architectures that integrate design artifacts and requirements for automated front-end implementation.
- **Evidence:** Architecture changes quality by only about 3-5 percentage points but changes generator token use substantially; the deterministic Custom workflow has the best reported cost-quality balance.
- **Domains:** code-generation-repair, comparative-single-vs-multi, cost-latency, memory-context, orchestration, reliability-nondeterminism, requirements-design, verification-testing

### Zhu, X., Wu, J., Zhang, X., Li, T., & Mu, Y. (n.d.). Bugs in Modern LLM Agent Frameworks: An Empirical Study. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering. https://doi.org/10.1145/3803437.3805536

- **Decision:** core — This empirical study directly investigates bugs in real-world LLM agent frameworks, including lifecycle execution and multi-agent coordination.
- **Evidence:** API Misuse accounts for 32.97% and API Incompatibility for 22.34% of reports, jointly 55.3%, while Documentation Desync adds 7.52%; execution semantics and changing contracts dominate framework reliability.
- **Domains:** code-generation-repair, end-to-end-sdlc, memory-context, observability-fault-injection, reliability-nondeterminism, transactions-concurrency, verification-testing

### [No author listed] (n.d.). Demystifying LLM-Based Software Engineering Agents: A Review of Capabilities, Benchmarks, and Failure Modes. https://journal.duc.edu.iq/index.php/djst/article/view/828

- **Decision:** core — This review directly compares single- and multi-agent software-engineering performance, cost, benchmarks, and failure modes.
- **Evidence:** Role specialization and cross-agent validation can provide redundant checking, but flawed upstream specifications can be faithfully propagated and same-base-model agents can reinforce correlated errors.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, cost-latency, reliability-nondeterminism, requirements-design, security, topology, verification-testing

### [No author listed] (n.d.). Efficiency-First Design for LLM-Based Multi-Agent Systems: A Framework and Empirical Analysis. https://www.researchgate.net/profile/Sivarama-Krishna-Akhil-Koduri/publication/399958237_Efficiency-First_Design_for_LLM-Based_Multi-Agent_Systems_A_Framework_and_Empirical_Analysis/links/69712fb3f5b9fd48849b200a/Efficiency-First-Design-for-LLM-Based-Multi-Agent-Systems-A-Framework-and-Empirical-Analysis.pdf

- **Decision:** core — The empirical efficiency-first analysis directly addresses measurement and comparison of LLM multi-agent system cost and operational efficiency.
- **Evidence:** full text not read (status: unavailable).

### Fan, G., Liu, D., Pan, L., Zhang, R., & Guo, Q. (n.d.). Multi-LLM Persona Generation for Virtual Focus Groups in Software Engineering: A Controlled, Multi-domain Study of Emotional Requirements Elicitation. Proceedings of the ACM on Software Engineering (PACMSE), Volume 3, Issue FSE. https://doi.org/10.1145/3808098

- **Decision:** core — This controlled study directly evaluates multi-LLM personas as a specialist virtual focus group for software requirements elicitation.
- **Evidence:** Three-model plurality raises the pooled validated AI-only requirement share by 14.7 percentage points over the iterative single-model workflow, with a 95% confidence interval of 11.2 to 18.2 points.
- **Domains:** communication, debate-consensus, governance-accountability, human-in-loop, orchestration, requirements-design, role-specialization, security, verification-testing

### Basu, S., Kjellberg, V., Sun, S., & Haraldsson, B. (n.d.). Understanding Conversational Patterns in Multi-agent Programming: A Case Study on Fibonacci Game Development. AIware '26: Proceedings of the 3rd ACM International Conference on AI-Powered Software. https://doi.org/10.1145/3805760.3814914

- **Decision:** core — This case study directly examines coordination, role maintenance, and conversational behavior during multi-agent software development.
- **Evidence:** Only DeepSeek-R1 paired with itself begins with a correct solution and sustains it to the end; three other pairs start correctly but diverge after 3, 21, or 69 iterations, and the remaining eight never reach the required solution.
- **Domains:** code-generation-repair, orchestration, reliability-nondeterminism, role-specialization, verification-testing


## Supporting (163)

### Ravindran, A., Patra, A., Babaey, V., & Purini, S. (2026). A Critical Review and Evaluation of LLMs for RTL Generation. IEEE Access. https://doi.org/10.1109/access.2026.3665894

- **Decision:** supporting — This RTL-generation review contributes compiler-and-simulator-in-the-loop verification and concrete code-generation failure modes, despite not evaluating a multi-agent system.
- **Evidence:** full text not read (status: pending).

### Damarched, M. K. (2026). A HIPAA-Aware Agentic AI Co-Pilot Framework: Orchestrating Secure Multi-Step EHR Workflows for Clinical Burden Reduction in U.S. Hospital Systems. Journal of Drug Delivery and Therapeutics. https://doi.org/10.22270/jddt.v16i3.7649

- **Decision:** supporting — The clinical framework combines RBAC, de-identification, encryption, and transaction-scale safety evaluation as transferable controls for privileged software-agent workflows.
- **Evidence:** full text not read (status: pending).

### Peykani, P., Ghanidel, S., Javadi-Sisi, I., Snåšel, V., & Mirjalili, S. (2026). A Holistic Review of Agentic AI Frameworks, Applications, and Research Trajectories. Archives of Computational Methods in Engineering. https://doi.org/10.1007/s11831-026-10675-8

- **Decision:** supporting — This review links state management, orchestration, MLOps, formal threat modeling, security, accountability, and energy use to trustworthy scalable agents.
- **Evidence:** full text not read (status: pending).

### Roumeliotis, K. I., Margaris, D., Spiliotopoulos, D., & Vassilakis, C. (2026). A Large-Scale Empirical Study of LLM Orchestration and Ensemble Strategies for Sentiment Analysis in Recommender Systems. Future Internet. https://doi.org/10.3390/fi18020112

- **Decision:** supporting — The large-scale aggregation study quantifies accuracy gains over individual models and simple voting alongside a substantial orchestration-cost penalty.
- **Evidence:** full text not read (status: pending).

### Grabowski, H. (2026). A Modular Multi-Agent {LLM} Architecture for Text-to-Diagram Generation and User-Guided Refinement. e-Informatica Software Engineering Journal. https://doi.org/10.37190/e-inf260109

- **Decision:** supporting — The modular interpretation, synthesis, validation, and correction pipeline offers a transferable verification pattern, although its diagram task is not explicitly SE-specific.
- **Evidence:** The core handoff is explicit: selection yields diagram-type metadata, generation combines semantic intent with a formal grammar and style constraints, deterministic compilation returns structured diagnostics, and optional refinement makes feasibility-checked minimal edits before revalidation.
- **Domains:** benchmarks-evaluation, communication, comparative-single-vs-multi, cost-latency, reliability-nondeterminism, requirements-design, role-specialization, verification-testing

### Li, Y. (2026). A Multi-Agent LLM Framework for Automated Software Testing. Transactions on Computing Science. https://doi.org/10.63808/tcs.v2i2.447

- **Decision:** supporting — The testing framework is directly applicable to software-agent assurance but does not establish multi-agent advantage over a matched single agent.
- **Evidence:** The full framework scores 90.0% unconditional, 55.0% differential, and 5.0% strict detection versus 72.5%, 37.5%, and 2.5% for the same-model combined-role single agent; the differential advantage is 17.5 percentage points.
- **Domains:** benchmarks-evaluation, cost-latency, memory-context, reliability-nondeterminism, role-specialization, verification-testing

### Spieser, J., Balapour, A., Meller, J., Patra, K., & Shamsaei, B. (2026). A Review of Multi-Agent AI Systems for Biological and Clinical Data Analysis. Methods and Protocols. https://doi.org/10.3390/mps9020033

- **Decision:** supporting — Although biomedical, this review quantifies transferable token-cost and cascading-error risks and identifies deterministic orchestration and expert oversight as mitigations.
- **Evidence:** full text not read (status: pending).

### [No author listed] (2026). A survey for llm agent trajectory analysis: From failure attribution to enhancement. https://www.researchgate.net/profile/Mengzhuo-Chen/publication/401193207_A_Survey_for_LLM_Agent_Trajectory_Analysis_From_Failure_Attribution_to_Enhancement/links/699ed0c6ca66ef6ab9979188/A-Survey-for-LLM-Agent-Trajectory-Analysis-From-Failure-Attribution-to-Enhancement.pdf

- **Decision:** supporting — This survey synthesizes trajectory-level failure attribution and enhancement methods across single-agent and multi-agent systems that can support SE-agent diagnosis.
- **Evidence:** full text not read (status: pending).

### Chen, J. B., Pedrycz, W., Wang, F., Wu, J., Wu, G., Xing, L., Chen, Y., & Song, Y. (2026). A Tri-Stage LLM-Coordinated Framework for Order-Driven Scheduling of Earth Observation Satellite Tasks. IEEE Transactions on Geoscience and Remote Sensing. https://doi.org/10.1109/tgrs.2026.3700605

- **Decision:** supporting — This non-SE framework demonstrates transferable staged specialization with external validation to preserve operational feasibility.
- **Evidence:** full text not read (status: pending).

### Nageshwaran, V., & Ezekiel, S. (2026). Agentic AI and Large Language Models for Autonomous IoT Cybersecurity: A Systematic Survey, Taxonomy, and Research Roadmap. Electronics. https://doi.org/10.3390/electronics15122740

- **Decision:** supporting — The IoT survey contributes an agentic threat taxonomy and evaluation harness covering prompt injection, privacy, latency, governance, and single-versus-multi loops.
- **Evidence:** full text not read (status: pending).

### Toudas, K., Roumeliotis, K. I., Nasiopoulos, D. Κ., & Georgakopoulos, G. (2026). An Explainable AI Multi-Agent Recommender System for Financial Document Access Control. Information Systems Frontiers. https://doi.org/10.1007/s10796-026-10742-2

- **Decision:** supporting — The finance experiment finds orchestration merely comparable overall while unanimous specialist agreement isolates a substantially more accurate subset.
- **Evidence:** full text not read (status: pending).

### Cassola-Bacallao, J., Morales-Donaire, J., Hernández-Montoya, P., & Keith-Norambuena, B. (2026). Benchmarking LLM-as-a-Judge Models for 5W1H Extraction Evaluation. Electronics. https://doi.org/10.3390/electronics15030659

- **Decision:** supporting — The expert-validated judge comparison supplies transferable evidence on agreement, evaluator choice, and computational-cost tradeoffs for verification pipelines.
- **Evidence:** full text not read (status: pending).

### [No author listed] (2026). Beyond More Agents: A Survey of Collaboration Mechanisms in Multi-Agent LLM Systems. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7243979

- **Decision:** supporting — This survey synthesizes collaboration mechanisms beyond merely adding agents and is directly transferable to SE-agent coordination design.
- **Evidence:** full text not read (status: pending).

### Moreno-Lumbreras, D., Kula, R. G., & Treude, C. (2026). BonsAIDE: An Extended Vision for Human–AI Interaction in IDEs. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3793681

- **Decision:** supporting — The evaluated IDE prototype uses branching, comparison, pruning, and provenance to make AI-generated code easier for humans to validate and govern.
- **Evidence:** full text not read (status: pending).

### Gülmez, B. (2026). Code generation with large language models: a survey from neural program synthesis to autonomous software development. Applied Intelligence. https://doi.org/10.1007/s10489-026-07230-0

- **Decision:** supporting — This code-generation survey contributes transferable verification, security, and benchmark cautions but does not directly evaluate multi-agent versus single-agent systems.
- **Evidence:** The strongest specialist-versus-single-agent statement in the survey is GeoColab's reported 7.59-26.09% improvement in geospatial-code executability and accuracy from product-manager, algorithm-engineer, and programmer roles; the survey explicitly says multi-agent effectiveness depends on specialization, communication, and coordination mechanisms.
- **Domains:** benchmarks-evaluation, code-generation-repair, comparative-single-vs-multi, human-in-loop, memory-context, role-specialization, security, verification-testing

### Mohammad, F., Kakar, J. K., Ndong, D. R. B. B., Chas, M., & Ryu, D. (2026). CodeQual-Agent: An Intelligent LLM-Agent Framework for Automated Software Quality Assessment with Explainable Predictions and Real-Time Analysis. 2026 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW). https://doi.org/10.1109/icstw72326.2026.00035

- **Decision:** supporting — This large-scale SE quality-assessment study combines deterministic static metrics, distilled LLM reasoning, explainability, and human feedback, offering complementary production assurance rather than a multi-agent comparison.
- **Evidence:** full text not read (status: pending).

### Gunasekaran, T. S., Lim, S., Gupta, K., Bai, H., Pai, Y. S., & Billinghurst, M. (2026). Cognitive Bridge: AI-Generated Boundary Objects for Cross-Functional Collaboration. https://doi.org/10.1145/3772318.3791399

- **Decision:** supporting — Controlled designer-developer trials show adaptive AI boundary objects improve alignment but can cause premature convergence, a transferable coordination trade-off.
- **Evidence:** full text not read (status: pending).

### Saadi, A., & Hammal, Y. (2026). Consistency Checking of Functional and Non‐Functional Requirements in Self‐Adapting Systems. Software Practice and Experience. https://doi.org/10.1002/spe.70050

- **Decision:** supporting — The UML-to-timed-automata method uses UPPAAL model checking to preserve functional and nonfunctional consistency during autonomous software adaptation.
- **Evidence:** full text not read (status: pending).

### Issa, K. (2026). Developing and Evaluating an LLM-based Agent for ExplorViz Using CopilotKit. Kiel Software Engineering Research. https://doi.org/10.38071/2026-00397-5

- **Decision:** supporting — The software-visualization study shows how deterministic tools, privacy-aware context, and explicit user confirmation constrain risky agent-initiated edits.
- **Evidence:** full text not read (status: pending).

### Sharma, A. (2026). Emergent Misinformation Genesis in Multi-Agent LLM Clinical Pipelines. Zenodo (CERN European Organization for Nuclear Research). https://doi.org/10.22541/au.177499233.37732392/v1

- **Decision:** supporting — Clinical emergent misinformation is strong contrary evidence about collaboration-induced risk, but its direct domain is not software engineering.
- **Evidence:** full text not read (status: pending).

### Di Ruscio, D., Nguyen, P. T., Di Sipio, C., Rubei, R., & Di Rocco, J. (2026). Engineering LLM-based Multi-Agent Systems: A Taxonomy of Emerging Frameworks. IEEE Software. https://doi.org/10.1109/ms.2026.3694089

- **Decision:** supporting — This framework taxonomy structures specialist collaboration and reproducible evaluation concerns that transfer to SE agents, but offers no direct SE comparison.
- **Evidence:** full text not read (status: pending).

### Yadav, T., & Masum, M. (2026). Explainable Multi-Agent LLM Framework for Phishing Email Detection via Role-Specialized Evidence Decomposition. Electronics. https://doi.org/10.3390/electronics15122606

- **Decision:** supporting — This controlled phishing study attributes significant gains over a single-model baseline mainly to role-specialized evidence decomposition, with schema-governed aggregation improving auditability.
- **Evidence:** full text not read (status: pending).

### [No author listed] (2026). From fragmentation to systematic design: Architecting llm-based multi-agent systems. https://www.techrxiv.org/doi/abs/10.36227/techrxiv.176827304.41872996

- **Decision:** supporting — This system-design synthesis contributes transferable memory, specialist selection, and coordination patterns without a direct SE evaluation.
- **Evidence:** full text not read (status: pending).

### Loureiro, T., Ferrada, F., & Baldissera, T. (2026). From Model to Agent: A Modular LLM-Based Framework for Multi-Agent Systems. 2026 10th International Young Engineers Forum on Electrical and Computer Engineering (YEF-ECE). https://doi.org/10.1109/yef-ece70590.2026.11614663

- **Decision:** supporting — This evaluated modular agent framework provides pluggable reasoning, memory, tools, local deployment, and built-in observability, addressing transferable privacy and recurring-cost constraints.
- **Evidence:** full text not read (status: pending).

### Liu, D., Zhou, X., & Li, Y. (2026). Large language model-driven multi-agent framework for fault detection and diagnostics of variable air volume boxes. Architectural Engineering and Design Management. https://doi.org/10.1080/17452007.2026.2647805

- **Decision:** supporting — This non-SE comparison supplies transferable planner-executor-reporter specialization, iterative self-correction, and verified-results integration against a monolithic LLM baseline.
- **Evidence:** full text not read (status: pending).

### Zhu, Y., Liu, L., Yu, J., & Zhang, D. (2026). LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns. Future Internet. https://doi.org/10.3390/fi18060326

- **Decision:** supporting — This survey catalogs orchestration frameworks, communication protocols, and specialist patterns that can be transferred to software-development agents.
- **Evidence:** full text not read (status: unavailable).

### More, R., Varma, S., & Varma, N. (2026). MACV: A Specialized Multi-Agent and Consensus Framework for Reliable LLM Outputs. 2026 7th International Conference on Mobile Computing and Sustainable Informatics (ICMCSI). https://doi.org/10.1109/icmcsi67283.2026.11412804

- **Decision:** supporting — MACV supplies a benchmarked cross-verification and consensus method that reduces hallucinations against single-LLM baselines with measured compute overhead.
- **Evidence:** Full MACV is reported at 72.7% accuracy versus 50.0% for the single-LLM baseline and at a 27.3% hallucination rate versus 50.0%, both described as 45% relative improvements; only ten items per dataset make these illustrative estimates.
- **Domains:** benchmarks-evaluation, comparative-single-vs-multi, cost-latency, debate-consensus, governance-accountability, reliability-nondeterminism, role-specialization, verification-testing

### Li, H., Zhang, L., Zhou, H., & Hong, T. (2026). MCP-enabled agentic AI workflow for building energy modelling: framework and use cases. Journal of Building Performance Simulation. https://doi.org/10.1080/19401493.2026.2653969

- **Decision:** supporting — The cross-domain comparison demonstrates standardized MCP tool orchestration, visible actions, and retained professional authority as transferable production controls.
- **Evidence:** full text not read (status: pending).

### Park, G., Lee, S. C., & Park, Y. (2026). Minimizing Response Latency in LLM-Based Agent Systems: A Comprehensive Survey. IEEE Access. https://doi.org/10.1109/access.2026.3664226

- **Decision:** supporting — This survey identifies multi-agent communication and coordination overhead plus stack-level remedies for latency and economic viability.
- **Evidence:** full text not read (status: pending).

### Xu, X., & Wu, J. (2026). Mitigating LLM Hallucination Snowballing in Multiagent Systems via Context-Aware Semantic Consistency Reasoning. IEEE Transactions on Neural Networks and Learning Systems. https://doi.org/10.1109/tnnls.2026.3655508

- **Decision:** supporting — The experiments establish hallucination snowballing in sequential LLM collaboration and evaluate an entailment-based mitigation strategy.
- **Evidence:** full text not read (status: pending).

### Foundjem, A., Tidjon, L. N., Da Silva, L., & Khomh, F. (2026). Multi-Agent AI Framework for Threat Mitigation and Resilience in Machine Learning Systems. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3780095

- **Decision:** supporting — This empirical ML-security study contributes transferable prompt-injection, supply-chain, dependency, and continuous-monitoring failure mechanisms, though it does not evaluate software-development agents.
- **Evidence:** full text not read (status: pending).

### Hu, X., & Shen, Y. (2026). Multi-Agent Social Simulation: Protocolizing LLM-Driven Agent-Based Modeling as a Quantitative Research Method. Preprints.org. https://doi.org/10.20944/preprints202606.1832.v1

- **Decision:** supporting [preprint] — The protocol supplies transferable role clustering, bounded information, structured outputs, harness checks, reason-action logs, and replication manifests.
- **Evidence:** full text not read (status: pending).

### Prause, M. (2026). No skin in the game: why agentic AI requires principal-agent governance. AI and Ethics. https://doi.org/10.1007/s43681-026-01067-6

- **Decision:** supporting — The abstract supplies a concrete governor-layer architecture for screening, monitoring, constraints, and accountability but no software-engineering evaluation.
- **Evidence:** full text not read (status: pending).

### Watanabe, M., Li, H., Kashiwa, Y., Reid, B., Iida, H., & Hassan, A. E. (2026). On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3798166

- **Decision:** supporting — The real-world Claude Code pull-request study quantifies where agent-produced changes still require human revision and oversight.
- **Evidence:** full text not read (status: pending).

### Wang, Y., Keung, J., Ma, X., Mao, Z., Chen, K., & Li, Y. (2026). R2Code: A Self-Reflective LLM Framework for Requirements-to-Code Traceability. https://doi.org/10.1109/compsac69091.2026.00057

- **Decision:** supporting — R2Code empirically combines reflective consistency checks with adaptive retrieval to improve requirements-to-code traceability while reducing token use.
- **Evidence:** full text not read (status: pending).

### Jain, S., Piplotia, S., Shrivastava, A., & Prajapati, B. (2026). Reliability-Weighted Multi-Agent Annotation Workflow for Quality-Controlled LLM Labeling. International Journal For Multidisciplinary Research. https://doi.org/10.36948/ijfmr.2026.v08i03.77244

- **Decision:** supporting — The reliability-weighted consensus and disagreement-triggered human review mechanism is transferable to quality control for software-agent outputs.
- **Evidence:** full text not read (status: pending).

### Alenezi, M. (2026). Rethinking software engineering for agentic ai systems. arXiv preprint. https://arxiv.org/abs/2604.10599

- **Decision:** supporting [preprint] — This position paper reframes software engineering around verification and orchestration but does not provide a matched single-versus-multi experiment.
- **Evidence:** The review's central conclusion is that abundant generation moves the bottleneck from code authorship to intent specification, semantic verification, orchestration, and accountable human judgment.
- **Domains:** comparative-single-vs-multi, cost-latency, end-to-end-sdlc, governance-accountability, human-in-loop, orchestration, verification-testing

### Zhang, H., Cheng, W., & Hu, W. (2026). Self-Improving Code Generation via Semantic Entropy and Behavioral Consensus. https://doi.org/10.1145/3794763.3794798

- **Decision:** supporting — ConSelf uses semantic uncertainty and behavioral consensus to reduce noisy self-supervision without teachers or test oracles, a transferable reliability mechanism for code agents.
- **Evidence:** full text not read (status: pending).

### [No author listed] (2026). Specialized multi-agent autonomous coordination for complex project execution using balanced cooperation, dynamic virtualized playgrounds, and extensible tool …. https://dione.lib.unipi.gr/xmlui/handle/unipi/19178

- **Decision:** supporting — The abstract describes specialist orchestration and comparison with a monolithic loop, but it does not establish an SE-specific matched evaluation.
- **Evidence:** For the described complex deployment, the thesis reports 94% total task-completion success for SandBot versus 42% for the monolithic baseline and attributes the difference to domain partitioning, isolated state, and a registry check that prevents completion while delegated work remains pending; the unreported number of runs and bundled interventions prevent a specialist-only causal conclusion.
- **Domains:** comparative-single-vs-multi, cost-latency, memory-context, orchestration, role-specialization, topology

### Naqvi, S., Baqar, M., & Mohammad, N. A. (2026). The Rise of Agentic Testing: Multi-Agent Systems for Robust Software Quality Assurance. arXiv preprint. https://arxiv.org/abs/2601.02454

- **Decision:** supporting [preprint] — This testing survey contributes assurance methods but is not itself comparative evidence for specialist-agent superiority.
- **Evidence:** The main quantitative table reports statement coverage rising from 72.8% to 94.9%, branch coverage from 61.5% to 91.7%, valid executable tests from 64.1% to 89.3%, per-module runtime falling from 3.5 to 1.1 hours, and QA effort falling from 11.8 to 3.4 person-hours.
- **Domains:** benchmarks-evaluation, cost-latency, human-in-loop, memory-context, reliability-nondeterminism, verification-testing

### Trifković, N. M., & Antović, I. D. (2026). Towards Role-Based Multi-Agent LLM Systems for Software Requirements Analysis. 2026 30th International Conference on Information Technology (IT). https://doi.org/10.1109/it67293.2026.11435673

- **Decision:** supporting — This conceptual requirements-analysis architecture proposes hierarchical supervision, structured cross-checking, and uncertainty arbitration but has no empirical validation.
- **Evidence:** The proposed mechanism assigns each requirements-analysis role to two parallel specialized SLMs, accepts sufficiently similar reports, and sends disagreements to a higher-level LLM for contextual arbitration.
- **Domains:** governance-accountability, reliability-nondeterminism, requirements-design, role-specialization, topology

### Hosseini, M.-P., Shah, A., Qureshi, S., Huang, A., Miao, C., & Wei, W. (2026). Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent LLM Systems. 2026 IEEE 50th Annual Computers, Software, and Applications Conference (COMPSAC). https://doi.org/10.1109/compsac69091.2026.00034

- **Decision:** supporting — REDEREF offers a training-free delegation controller that measurably reduces tokens, calls, and latency while remaining robust to agent or judge degradation.
- **Evidence:** full text not read (status: pending).

### Zabardast, E., Vieira, T., & Gorschek, T. (2025). A 3-Layer Agentic Model for Nonfunctional Requirements in Software Engineering. https://doi.org/10.1109/asew67777.2025.00020

- **Decision:** supporting — The three-layer model supplies a lifecycle-wide structure for assuring agent security, compliance, and maintainability, although it is conceptual rather than empirical.
- **Evidence:** full text not read (status: pending).

### Yazdanian, P., Liu, Y., & Li, Z. (2025). A Comparative Study Towards Designing a Hybrid Architecture of Microservices and LLM-based Multi-Agent Systems. 2025 32nd Asia-Pacific Software Engineering Conference (APSEC). https://doi.org/10.1109/apsec66846.2025.00077

- **Decision:** supporting — The available fragment contrasts a hybrid microservice and LLM-MAS architecture with a single-agent paradigm but reports no empirical metrics.
- **Evidence:** full text not read (status: pending).

### Ray, P. P. (2025). A Comprehensive Introspection on AI Risks: Taxonomy, Challenges and Future Directions. https://doi.org/10.36227/techrxiv.175339321.17050891/v1

- **Decision:** supporting [preprint] — The agent-focused risk taxonomy proposes monitoring, schema-guided tool use, policy-as-code governance, and resource-aware mitigations transferable to development agents.
- **Evidence:** full text not read (status: pending).

### Guo, J., Huang, S., Li, M., Huang, D., Chen, X., Zhang, R., Guo, Z., Yu, H., Yiu, S.-M., Lio, P., & Lam, K.-Y. (2025). A comprehensive survey on benchmarks and solutions in software engineering of llm-empowered agentic system. arXiv preprint. https://arxiv.org/abs/2510.09721

- **Decision:** supporting [preprint] — This broader survey contributes SE-agent benchmarks and engineering solutions relevant to multi-agent production readiness without directly comparing architectures.
- **Evidence:** full text not read (status: pending).

### Ray, P. P. (2025). A Review on Agent-to-Agent Protocol: Concept, State-of-the-art, Challenges and Future Directions. https://doi.org/10.36227/techrxiv.174612014.42157096/v1

- **Decision:** supporting [preprint] — The A2A protocol supplies concrete discovery, task, artifact, authentication, event, durable-state, and observability mechanisms for interoperable agent workflows.
- **Evidence:** full text not read (status: pending).

### Ray, P. P. (2025). A Review on Vibe Coding: Fundamentals, State-of-the-art, Challenges and Future Directions. https://doi.org/10.36227/techrxiv.174681482.27435614/v1

- **Decision:** supporting [preprint] — The review covers multi-agent end-to-end software creation, benchmarked platforms, and production risks without isolating matched single-versus-multi evidence.
- **Evidence:** full text not read (status: pending).

### Ge, Y., Mei, L., Duan, Z., Li, T., Zheng, Y., Wang, Y., Wang, L., Yao, J., Liu, T., Cai, Y., Bi, B., Guo, F., Guo, J., Liu, S., & Cheng, X. (2025). A Survey of Vibe Coding with Large Language Models. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2510.12399

- **Decision:** supporting [preprint] — This software-development survey identifies test-driven workflows, context engineering, and human-agent feedback as concrete ways to stabilize coding agents.
- **Evidence:** full text not read (status: pending).

### [No author listed] (2025). A Survey on Reliability, Transparency, Accountability, and Fairness in LLM-based Multi-Agent Systems through the Responsibility Lens. https://www.researchgate.net/profile/Abolfazl-Asudeh/publication/397650899_A_Survey_on_Reliability_Transparency_Accountability_and_Fairness_in_LLM-based_Multi-Agent_Systems_through_the_Responsibility_Lens/links/691933f9de8143098271909a/A-Survey-on-Reliability-Transparency-Accountability-and-Fairness-in-LLM-based-Multi-Agent-Systems-through-the-Responsibility-Lens.pdf

- **Decision:** supporting — This responsibility-focused survey contributes reliability, transparency, and accountability criteria applicable to governed software-development agent teams.
- **Evidence:** full text not read (status: pending).

### Brown, A., Roman, M., & Devereux, B. (2025). A Systematic Literature Review of Retrieval-Augmented Generation: Techniques, Metrics, and Challenges. Big Data and Cognitive Computing. https://doi.org/10.3390/bdcc9120320

- **Decision:** supporting — This systematic review identifies retrieval, memory, uncertainty control, provenance, security, and budget-aware evaluation methods transferable to software agents.
- **Evidence:** full text not read (status: pending).

### Nagvekar, R. (2025). Agentic AI-Driven CI/CD Pipelines for Autonomous Software Delivery. https://doi.org/10.1109/ictbig68706.2025.11323919

- **Decision:** supporting — The proposed role-based agentic CI/CD architecture connects goals, coding, testing, deployment, feedback, and ethics, but lacks reported empirical validation.
- **Evidence:** full text not read (status: pending).

### Yang, Y., Chai, H., & Zhang, W. (2025). AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems. https://doi.org/10.32388/ws0vim

- **Decision:** supporting — AgentNet provides a decentralized specialist-coordination method with single-agent and centralized multi-agent baselines, but the abstract does not establish an SE evaluation.
- **Evidence:** Against the strongest listed single-agent result per task, AgentNet scores 92.86% versus 89.28% on MATH, 94% versus 92% on BBH, and 30% versus 29% on API-Bank with DeepSeek-V3; 85% versus 77.14%, 86% versus 85%, and 29% versus 24% with GPT-4o-mini; and 81.43% versus 76.43%, 92% versus 74%, and 32% versus 28% with Qwen-turbo.
- **Domains:** cost-latency, memory-context, reliability-nondeterminism, role-specialization, topology

### Choi, S., & Yang, G. (2025). AgentReport: A Multi-Agent LLM Approach for Automated and Reproducible Bug Report Generation. Applied Sciences. https://doi.org/10.3390/app152211931

- **Decision:** supporting — Automated bug-report generation is a focused software-engineering task rather than end-to-end or matched architecture evidence.
- **Evidence:** full text not read (status: pending).

### Chang, E. Y. (2025). ALAS: A Stateful Multi-LLM Agent Framework for Disruption-Aware Planning. Multi-LLM Agent Collaborative Intelligence. https://doi.org/10.1145/3749421.3749436

- **Decision:** supporting — ALAS contributes state tracking and compensating transactions that can address agent-workflow disruption, but evaluates planning rather than software development.
- **Evidence:** full text not read (status: pending).

### Avgerinos, V., Ramantas, K., Alonso, L., & Verikoukis, C. (2025). ARM: Autonomous Remediation and Management With LLM Agents for Intent-Driven Control. IEEE Internet of Things Journal. https://doi.org/10.1109/jiot.2025.3648858

- **Decision:** supporting — The evaluated closed-loop LLM agent combines fault detection, remediation, and post-action validation in cloud infrastructure, providing transferable reliability methods.
- **Evidence:** full text not read (status: pending).

### Owotogbe, J. (2025). Assessing and Enhancing the Robustness of LLM-Based Multi-Agent Systems Through Chaos Engineering. 2025 IEEE/ACM 4th International Conference on AI Engineering – Software Engineering for AI (CAIN). https://doi.org/10.1109/cain66642.2025.00039

- **Decision:** supporting — This paper proposes chaos engineering and production-like fault injection to expose hallucination, agent, and communication failures, but the abstract reports no empirical results.
- **Evidence:** full text not read (status: pending).

### Monteiro, C. E. O., Guerino, L. R., Fernandes, G., Pereira, M. F. P., de Souza-Zinader, J. P., Braga, R. D. B., Pocivi, V. C. B., & Vincenzi, A. M. R. (2025). Automated Generation of End-to-End Web Test Cases via a Generic AI Agent: A Comparative Study of DeepSeek V3 and Claude Sonnet 5. https://doi.org/10.5753/webmedia.2025.16046

- **Decision:** supporting — This empirical end-to-end test-generation study reports large model-dependent success and cost differences for a tool-using coding agent.
- **Evidence:** full text not read (status: pending).

### Sharma, A. (2025). Automating Software Release Notes with AI: A Comparative Study of Agent-Based Systems vs. LLM Fine-Tuning Approaches. International Scientific Journal of Engineering and Management. https://doi.org/10.55041/isjem05150

- **Decision:** supporting — For release-note automation, deterministic agent preprocessing plus LLM realization offers a concrete hybrid method for traceability, compliance, and fluent output.
- **Evidence:** full text not read (status: pending).

### Chen, Y. (2025). AutoReview: An LLM-based Multi-Agent System for Security Issue-Oriented Code Review. Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering. https://doi.org/10.1145/3696630.3728618

- **Decision:** supporting — Security-oriented code review is a concrete specialist-agent assurance mechanism but not a full SDLC comparison.
- **Evidence:** full text not read (status: pending).

### Treude, C., & Poskitt, C. M. (2025). Bot-Driven Development: From Simple Automation to Autonomous Software Development Bots. https://doi.org/10.1109/botse67031.2025.00012

- **Decision:** supporting — The BotDD research agenda surfaces trust, interruption, ethics, skills, and governance constraints for autonomous coding, testing, and project-management bots.
- **Evidence:** full text not read (status: pending).

### Liu, A., Hill, C. S., Jiang, J., & Zhu, Z. (2025). Can Reasoning LLMs Eliminate Conformity in Multi-Agent Systems?. https://doi.org/10.1109/icdmw69685.2025.00406

- **Decision:** supporting — Controlled multi-agent experiments identify consensus-driven conformity and show that reasoning models mitigate it only for some task types.
- **Evidence:** full text not read (status: pending).

### Hou, S., Jiao, H., Shen, Z., Liang, J., Zhao, A., Zhang, X., Wang, J., & Wu, H. (2025). Chain-of-programming (CoP): empowering large language models for geospatial code generation task. International Journal of Digital Earth. https://doi.org/10.1080/17538947.2025.2509812

- **Decision:** supporting — The evaluated staged workflow combines requirements analysis, shared context, retrieval, debugging, and user feedback to improve specialized code generation.
- **Evidence:** full text not read (status: pending).

### Yang, G., Zhou, Y., Chen, X., Zheng, W. X., Hu, X., Zhou, X., Lo, D., & Chen, T. (2025). Code-DiTing: Automatic Evaluation of Code Generation without References or Test Cases. https://doi.org/10.1109/ase63991.2025.00021

- **Decision:** supporting — Code-DiTing combines distilled reasoning with majority voting to improve code evaluation accuracy, explainability, robustness, and computational efficiency.
- **Evidence:** full text not read (status: pending).

### Zhang, S., Wang, X., MA, G., Sun, X., Wang, Y., Liu, Y. X., & Zhang, J. (2025). Cognitive Architectures for Data Science: Integrating Continual Pre-training with Agentic LLM. https://doi.org/10.1109/iccit68389.2025.11453438

- **Decision:** supporting — Structured reasoning and continual pre-training improve long-horizon stability and tool-use robustness in an adjacent agent domain with benchmark evidence.
- **Evidence:** full text not read (status: pending).

### Dong, J., Sun, J., Zhang, W., Dong, J. S., & Hao, D. (2025). ConTested: Consistency-Aided Tested Code Generation with LLM. Proceedings of the ACM on software engineering.. https://doi.org/10.1145/3728902

- **Decision:** supporting — ConTested shows that human-guided co-evolution of generated code and tests corrects unreliable majority voting with small measured overhead, providing a transferable agent assurance loop.
- **Evidence:** full text not read (status: pending).

### Kim, N., & Bae, B. (2025). Conversational AI-Powered Multi-Agent System for Mobile Application Accessibility Compliance: A RAG-Enhanced Pipeline Design. https://doi.org/10.1109/ictc66702.2025.11388949

- **Decision:** supporting — This software-compliance pipeline provides a concrete dual-agent and retrieval-grounded pattern for separating issue analysis from remediation guidance.
- **Evidence:** full text not read (status: pending).

### Aarabi, P., & Qin, Y. (2025). Cooperative Ai Agents Using Supervised Global Workspaces. https://doi.org/10.1109/cai64502.2025.00056

- **Decision:** supporting — A supervisor plus specialized agents and a shared global workspace offers a concrete orchestration and synchronization pattern transferable to SDLC agents.
- **Evidence:** full text not read (status: pending).

### Tadi, S. R. C. C. T. (2025). Developer and LLM Pair Programming: An Empirical Study of Role Dynamics and Prompt-Based Collaboration. International Journal of Advanced Research in Science Communication and Technology. https://doi.org/10.48175/ijarsct-26358

- **Decision:** supporting — This empirical human-LLM pair-programming study identifies role switching, prompt quality, context cues, and developer orchestration as practical human-oversight factors.
- **Evidence:** full text not read (status: pending).

### Zou, Y., Cheng, A. H., Aldossary, A., Bai, J., Leong, S. X., Campos-Gonzalez-Angulo, J. A., Choi, C., Ser, C. T., Tom, G., Wang, A., Zhang, Z., Yakavets, I., Han, H., Crebolder, C., Bernales, V., & Aspuru‐Guzik, A. (2025). El Agente: An autonomous agent for quantum chemistry. Matter. https://doi.org/10.1016/j.matt.2025.102263

- **Decision:** supporting — Its hierarchical memory, adaptive tool selection, in-situ recovery, and action traces are transferable controls for long-running software agents despite the chemistry domain.
- **Evidence:** full text not read (status: pending).

### Zhang, S., Xing, Z., Guo, R., Xu, F., Chen, L., Zhang, Z., Zhang, X., Feng, Z., & Zhuang, Z. (2025). Empowering Agile-Based Generative Software Development through Human-AI Teamwork. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3702987

- **Decision:** supporting — AgileGen combines testable Gherkin requirements, iterative human decisions, and reusable scenario memory to align generated code with user intent.
- **Evidence:** full text not read (status: pending).

### Li, Z., & Izadi, M. (2025). Enhancing Human-IDE Interaction in the SDLC using LLM-based Mediator Agents. https://doi.org/10.1145/3696630.3728721

- **Decision:** supporting — The mediator-agent framework concretely unifies programmers, IDE tools, agentic tools, and external multi-agent systems across the SDLC, though it lacks evaluation.
- **Evidence:** full text not read (status: pending).

### Mandal, I., Soni, J., Zaki, M., Smedskjær, M. M., Wondraczek, K., Wondraczek, L., Gosvami, N. N., & Krishnan, N. M. A. (2025). Evaluating large language model agents for automation of atomic force microscopy. Nature Communications. https://doi.org/10.1038/s41467-025-64105-7

- **Decision:** supporting — AFMBench offers transferable controlled evidence on specialist coordination failures, but its target workflow is laboratory automation.
- **Evidence:** full text not read (status: pending).

### Wang, K., Tian, H., Wang, J., & Hou, J. (2025). Fuzzy-LLM: Multi-Agent Task Planning with Large Language Models. 2025 IEEE/ACIS 29th International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD). https://doi.org/10.1109/snpd65828.2025.11254718

- **Decision:** supporting — This multi-robot planning study provides transferable task decomposition, coalition formation, and allocation mechanisms although it is not a software-engineering or single-agent comparison.
- **Evidence:** full text not read (status: pending).

### Treude, C., & Storey, M.-A. (2025). Generative AI and Empirical Software Engineering: A Paradigm Shift. https://doi.org/10.1109/aiware69974.2025.00033

- **Decision:** supporting — This empirical-software-engineering vision identifies model and prompt drift as reproducibility threats requiring adapted instruments and validation standards.
- **Evidence:** full text not read (status: pending).

### Li, F., Jiang, J., Sun, J., & Zhang, H. (2025). Hybrid Automated Program Repair by Combining Large Language Models and Program Analysis. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3715004

- **Decision:** supporting — GiantRepair combines LLM patch skeletons with context-aware program analysis and realistic fault localization, providing a tested hybrid remedy for unreliable direct patch use.
- **Evidence:** full text not read (status: pending).

### Mao, Z., Fan, X., Wang, Y., Keung, J., & Li, J. (2025). Hybrid Privacy Policy-Code Consistency Check using Knowledge Graphs and LLMs. https://doi.org/10.1109/qrs-c65679.2025.00101

- **Decision:** supporting — This hybrid privacy check confines LLMs to semantic analysis and uses deterministic knowledge-graph checks, sharply improving accuracy, token cost, and latency.
- **Evidence:** full text not read (status: pending).

### Kataria, V. (2025). Intelligent Site Reliability Engineering: A Multi-agent LLM Framework for Automated Incident Analysis and Root Cause Determination. International Journal of Intelligent Engineering and Systems. https://doi.org/10.22266/ijies2025.1231.28

- **Decision:** supporting — Multi-agent site-reliability operations provide a transferable production-operations architecture but not a matched software-development comparison.
- **Evidence:** full text not read (status: pending).

### Shemetova, E., Smirnov, I., Alekseev, A., Shenbin, I., Rukhovich, A., Nikolenko, S., Lomshakov, V., & Piontkovskaya, I. (2025). LAMeD: LLM-generated Annotations for Memory Leak Detection. https://doi.org/10.1145/3756681.3756999

- **Decision:** supporting — LLM-generated function annotations strengthen static memory-leak analysis and reduce path explosion, offering a concrete hybrid verification method.
- **Evidence:** full text not read (status: pending).

### Yang, G., Zheng, W., Chen, X., Dong, L., Hu, P., Yang, Y. E., Peng, S., Li, Z., Feng, J., Wei, X. X., Sun, K., Ma, D., Cheng, H. P., Shen, Y., Hu, X., Zhuo, T. Y., & Lo, D. (2025). Large Language Model for Verilog Code Generation: Literature Review and the Road Ahead. Preprints.org. https://doi.org/10.20944/preprints202511.0656.v2

- **Decision:** supporting [preprint] — This software-engineering review catalogs LLM code-generation datasets, metrics, limitations, and alignment methods that can support agent evaluation and verification.
- **Evidence:** full text not read (status: pending).

### Solovyeva, L., Oliveira, E. C., Fan, S., Tuncay, A., Gareev, S., & Capiluppi, A. (2025). Leveraging LLMs for Automated Translation of Legacy Code: A Case Study on PL/SQL to Java Transformation. https://doi.org/10.1145/3756681.3757007

- **Decision:** supporting — The industrial legacy-translation case exposes scarce tests as a production validation constraint while demonstrating guided prompting for functional code conversion.
- **Evidence:** full text not read (status: pending).

### Mamatha, G., Joshi, V. V., & Manur, P. T. (2025). LLM - Driven Autonomous Cloud Automation Agent. https://doi.org/10.1109/csitss67709.2025.11295499

- **Decision:** supporting — The cloud-automation study evaluates a single LLM agent under adversarial events and contributes transferable policy, identity, and remediation controls.
- **Evidence:** full text not read (status: pending).

### Chen, B., Babikian, A. A., Feng, S., Varró, D., & Mussbacher, G. (2025). LLM-based Satisfiability Checking of String Requirements by Consistent Data and Checker Generation. https://doi.org/10.1109/re63999.2025.00030

- **Decision:** supporting — Generated SMT and Python checkers more than double key requirements-validation outcomes, providing a concrete hybrid formal-verification remedy.
- **Evidence:** full text not read (status: pending).

### Videsjorden, A. N., Song, H., Göknil, A., Roman, D., & Soylu, A. (2025). LUMEN: Enhancing IoT System Observability with Multi-Agent Large Language Models and Knowledge Graphs. ACM Transactions on Internet of Things. https://doi.org/10.1145/3772077

- **Decision:** supporting — LUMEN's industrial IoT cases show specialized LLM agents, knowledge graphs, and human oversight as a transferable observability architecture without a single-agent comparison.
- **Evidence:** full text not read (status: pending).

### Tran, K.-T., Dao, D., Nguyen, M.-D., Pham, Q.-V., O'Sullivan, B., & Nguyen, H. D. (2025). Multi-agent collaboration mechanisms: A survey of llms. arXiv preprint. https://arxiv.org/abs/2501.06322

- **Decision:** supporting [preprint] — This survey organizes LLM multi-agent collaboration mechanisms that are transferable to software-agent coordination despite not being SE-specific.
- **Evidence:** full text not read (status: pending).

### Muhammad, A., Mohammed, M. A., Milanova, M., Talburt, J. R., & Cakmak, M. C. (2025). Multi-Agent RAG Framework for Entity Resolution: Advancing Beyond Single-LLM Approaches with Specialized Agent Coordination. Computers. https://doi.org/10.20944/preprints202510.2382.v1

- **Decision:** supporting — This non-SE entity-resolution study reports that task-specific agents and RAG improve accuracy, transparency, and API efficiency over a single-LLM approach, providing a transferable specialization mechanism.
- **Evidence:** full text not read (status: pending).

### [No author listed] (2025). MULTI-AGENT SYSTEM FOR AUTOMATED CODE REVIEWS. https://trepo.tuni.fi/bitstream/handle/10024/232334/PremasunderaSavidya.pdf?sequence=2

- **Decision:** supporting — Automated code review contributes a specialist verification role but does not test the complete research hypothesis.
- **Evidence:** full text not read (status: pending).

### Yu, M. (2025). PreEduAI: A Multi-Agent Collaborative Framework for Automated Preschool Curriculum Development. IEEE Access. https://doi.org/10.1109/access.2025.3646282

- **Decision:** supporting — The controlled cross-domain study and ablations quantify gains from specialized generator, evaluator, optimizer, and advisor roles over individual models.
- **Evidence:** full text not read (status: pending).

### Gutierrez, Y., Camacho, E., Pardo, C., & Villarreal, V. (2025). Prompts Engineering Challenges in Software Code Generation. https://doi.org/10.1109/amitic68284.2025.11214606

- **Decision:** supporting — This systematic review identifies prompt sensitivity, robustness, security, plagiarism, and over-reliance as concrete code-generation failure mechanisms.
- **Evidence:** full text not read (status: pending).

### Raza, S., Sapkota, R., Karkee, M., & Emmanouilidis, C. (2025). Responsible Agentic Reasoning and AI Agents: A Critical Survey. https://doi.org/10.36227/techrxiv.175735299.97215847/v2

- **Decision:** supporting [preprint] — The survey proposes an auditable safety taxonomy, metrics, and benchmarking protocol directly transferable to responsible software-development agents.
- **Evidence:** full text not read (status: pending).

### Reid, A., O'Callaghan, S., Carroll, L., & Caetano, T. (2025). Risk analysis techniques for governed LLM-based multi-agent systems. arXiv preprint. https://arxiv.org/abs/2508.05687

- **Decision:** supporting [preprint] — This work offers risk-analysis techniques and critique-comparison metrics for governing interacting specialist LLM agents.
- **Evidence:** full text not read (status: pending).

### Jaiswal, S., Jain, K., Simmhan, Y., Parayil, A., Mallick, A., Wang, R., Amant, R. S., Bansal, C., Rühle, V., Kulkarni, A., Kofsky, S., & Rajmohan, S. (2025). SAGESERVE: Optimizing LLM Serving on Cloud Data Centers with Forecast Aware Auto-Scaling. Proceedings of the ACM on Measurement and Analysis of Computing Systems. https://doi.org/10.1145/3771576

- **Decision:** supporting — Production-scale forecast-aware routing and resource allocation provide a transferable remedy for LLM workload cost, utilization, and latency constraints.
- **Evidence:** full text not read (status: pending).

### Becattini, M., Verdecchia, R., & Vicario, E. (2025). SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems. 2025 IEEE/ACM International Workshop New Trends in Software Architecture (SATrends). https://doi.org/10.1109/satrends66715.2025.00006

- **Decision:** supporting — This deployed proof of concept addresses single-agent customization, memory, and ground-truth limits through dynamic specialist orchestration and separate operational and knowledge layers.
- **Evidence:** full text not read (status: pending).

### Wang, Q., Sun, Z., Wang, R., Huang, T., Jin, Z., Li, G., & Lyu, C. (2025). SemGuard: Real-Time Semantic Evaluator for Correcting LLM-Generated Code. https://doi.org/10.1109/ase63991.2025.00160

- **Decision:** supporting — SemGuard detects semantic drift during decoding and rolls back faulty lines, offering model-agnostic real-time verification without tests or execution.
- **Evidence:** full text not read (status: pending).

### Sun, Y., Keung, J., Yang, Z., Liu, S., & Yu, H. K. (2025). SemiRALD: A semi-supervised hybrid language model for robust Anomalous Log Detection. Information and Software Technology. https://doi.org/10.1016/j.infsof.2025.107743

- **Decision:** supporting — SemiRALD is a single-agent hybrid anomaly-detection method whose LLM parsing and low-label robustness provide transferable observability and reliability evidence.
- **Evidence:** full text not read (status: pending).

### Yoon, S. (2025). Strategic Learning Under Linguistic and Contextual Constraints: A Theoretical Framework for LLM-Based Multi-Agent Coordination. IEEE Access. https://doi.org/10.1109/access.2025.3628927

- **Decision:** supporting — The memory and linguistic-uncertainty model is a transferable coordination result outside software engineering.
- **Evidence:** full text not read (status: pending).

### Li, Y., Gu, S., & Geng, M. (2025). Symmetry-Aware Code Generation: Distilling Pseudocode Reasoning for Lightweight Deployment of Large Language Models. Symmetry. https://doi.org/10.3390/sym17081325

- **Decision:** supporting — This distillation study transfers pseudocode reasoning into smaller code models, providing empirical evidence for a lower-resource alternative to large-model deployment.
- **Evidence:** full text not read (status: pending).

### Pang, C. (2025). Toward Data Systems That Are Business Semantic Centric and AI Agents Assisted. IEEE Access. https://doi.org/10.1109/access.2025.3583260

- **Decision:** supporting — A real-world data-system architecture combines contextual knowledge, quality-assured workflows, and human alignment into an adjacent production agent pattern.
- **Evidence:** full text not read (status: pending).

### Azmi, R., Abdellahi, E. A. S., Bounabi, M., Chenal, J., Hlal, M., & Diop, E. (2025). Towards a Multi-Agent System Based on LLM and RAG for Automated and Customizable Urban Diagnostics. https://doi.org/10.1109/sita67914.2025.11273206

- **Decision:** supporting — The urban-diagnostics framework offers a transferable specialist-orchestration and handbook-grounded RAG design, although it remains theoretical and outside software engineering.
- **Evidence:** full text not read (status: pending).

### Saleh, A., Morabito, R., Dustdar, S., Tarkoma, S., Pirttikangas, S., & Lovén, L. (2025). Towards Message Brokers for Generative AI: Survey, Challenges, and Opportunities. ACM Computing Surveys. https://doi.org/10.1145/3742891

- **Decision:** supporting — The message-broker survey provides concrete communication, scalability, and latency infrastructure applicable to distributed LLM agent orchestration.
- **Evidence:** full text not read (status: pending).

### Dam, H. K. (2025). Towards Multi-Agentic AI for automated software design and modelling: challenges and opportunities. https://doi.org/10.1109/asew67777.2025.00063

- **Decision:** supporting — The conceptual framework identifies ambiguity, consistency, and merge-conflict problems and assigns collaborative agents across software design activities.
- **Evidence:** full text not read (status: pending).

### ADABARA, I., Sadiq, B. O., Shuaibu, A. N., Danjuma, Y. I., & Venkateswarlu, M. (2025). Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment. F1000Research. https://doi.org/10.12688/f1000research.169927.1

- **Decision:** supporting — This cross-layer review contributes agentic threat models and governance strategies spanning memory integrity, adversarial defense, oversight, and benchmarking.
- **Evidence:** full text not read (status: pending).

### Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). Vibe Coding vs. Agentic Coding: Fundamentals and Practical Implications of Agentic AI. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2505.19443

- **Decision:** supporting [preprint] — The review directly maps software-development agent workflows, feedback loops, testing, debugging, and safety mechanisms, offering complementary production methods.
- **Evidence:** full text not read (status: pending).

### Neves, A. L. M. D., Mantovani, D., Campelo, C., Souza, G., Souza, D., Furtado, B., Balby, L., & Araújo, E. (2025). Yuma: Geração de Workflows Multiagentes a partir de Linguagem Natural. https://doi.org/10.5753/webmedia_estendido.2025.16421

- **Decision:** supporting — Yuma coordinates requirements-engineer and software-architect agents to produce deployable workflows with human validation at each step.
- **Evidence:** full text not read (status: pending).

### Sun, Z., Du, X., Yang, Z., Li, L., & Lo, D. (2024). AI Coders Are among Us: Rethinking Programming Language Grammar towards Efficient Code Generation. https://doi.org/10.1145/3650212.3680347

- **Decision:** supporting — AI-oriented program grammar reduces code-task token usage while preserving performance, offering a concrete cost-control method for coding agents.
- **Evidence:** full text not read (status: pending).

### Zhang, Y., Ruan, H., Fan, Z., & Roychoudhury, A. (2024). AutoCodeRover: Autonomous Program Improvement. https://doi.org/10.1145/3650212.3680384

- **Decision:** supporting — AutoCodeRover demonstrates that structured code search and test-guided fault localization improve single-agent repair accuracy, speed, and cost.
- **Evidence:** full text not read (status: pending).

### Taeb, M., Swearngin, A., Schoop, E., Cheng, R., Jiang, Y., & Nichols, J. (2024). AXNav: Replaying Accessibility Tests from Natural Language. https://doi.org/10.1145/3613904.3642777

- **Decision:** supporting — AXNav combines an LLM with UI models and professional review to automate accessibility testing, supplying a transferable testing and oversight pattern.
- **Evidence:** full text not read (status: pending).

### Li, Z., Wang, Z., & Shang, J. (2024). Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step. https://doi.org/10.18653/v1/2024.findings-acl.49

- **Decision:** supporting — LDB exposes block-level runtime state to an LLM for stepwise verification and repair, yielding benchmarked debugging gains across several models.
- **Evidence:** full text not read (status: pending).

### Shin, J., Hashtroudi, S., Hemmati, H., & Wang, S. (2024). Domain Adaptation for Code Model-Based Unit Test Case Generation. https://doi.org/10.1145/3650212.3680354

- **Decision:** supporting — Project-level domain adaptation materially improves generated unit-test coverage and mutation scores over CodeT5, A3Test, and GPT-4, offering a concrete complementary testing method.
- **Evidence:** full text not read (status: pending).

### Yao, Z., Liu, J., Chen, X., Han, L., & Sun, H. (2024). Efficient Verification of Multi-Agent Systems Through Parallel. 2024 IEEE 24th International Conference on Software Quality, Reliability and Security (QRS). https://doi.org/10.1109/qrs62785.2024.00079

- **Decision:** supporting — This non-LLM multi-agent study contributes a parallel SCTL model checker that exposes multiple counterexamples as a transferable security and reliability mechanism.
- **Evidence:** full text not read (status: pending).

### Kang, S., Chen, B., Yoo, S., & Lou, J. (2024). Explainable automated debugging via large language model-driven scientific debugging. Empirical Software Engineering. https://doi.org/10.1007/s10664-024-10594-x

- **Decision:** supporting — AutoSD grounds repair in debugger observations, reports confidence, and improves human correctness judgments through explanations.
- **Evidence:** full text not read (status: pending).

### Yang, Z., Liu, F., Yu, Z., Keung, J., Li, J., Liu, S., Hong, Y., Ma, X., Jin, Z., & Li, G. (2024). Exploring and Unleashing the Power of Large Language Models in Automated Code Translation. Proceedings of the ACM on software engineering.. https://doi.org/10.1145/3660778

- **Decision:** supporting — UniTrans uses generated tests, execution feedback, and iterative repair to improve code translation, providing a concrete verification loop for agent workflows.
- **Evidence:** full text not read (status: pending).

### Xia, C. S., Paltenghi, M., Le Tian, J., Pradel, M., & Zhang, L. (2024). Fuzz4All: Universal Fuzzing with Large Language Models. https://doi.org/10.1145/3597503.3639121

- **Decision:** supporting — Fuzz4All demonstrates an LLM-driven testing loop that raises coverage and finds previously unknown bugs across diverse software systems.
- **Evidence:** full text not read (status: pending).

### Yoon, J., Feldt, R., & Yoo, S. (2024). Intent-Driven Mobile GUI Testing with Autonomous Large Language Model Agents. https://doi.org/10.1109/icst60714.2024.00020

- **Decision:** supporting — DroidAgent's measured coverage gains and long- and short-term memory design provide transferable evidence for autonomous testing, but it is single-agent.
- **Evidence:** full text not read (status: pending).

### Huang, T., Sun, Z., Jin, Z., Li, G., & Lyu, C. (2024). Knowledge-Aware Code Generation with Large Language Models. https://doi.org/10.1145/3643916.3644418

- **Decision:** supporting — KareCoder retrieves curated algorithm knowledge for unfamiliar code tasks and empirically improves Pass@1, supporting external-memory grounding for code agents.
- **Evidence:** full text not read (status: pending).

### Zhou, X., Cao, S., Sun, X., & Lo, D. (2024). Large Language Model for Vulnerability Detection and Repair: Literature Review and the Road Ahead. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3708522

- **Decision:** supporting — This review catalogs LLM vulnerability detection and repair methods and limitations that can support security assurance for agent-generated software.
- **Evidence:** full text not read (status: pending).

### Feng, K., Luo, L., Xia, Y., Luo, B., He, X., Li, K., Zha, Z., Xu, B., & Peng, K. (2024). Optimizing Microservice Deployment in Edge Computing with Large Language Models: Integrating Retrieval Augmented Generation and Chain of Thought Techniques. Symmetry. https://doi.org/10.3390/sym16111470

- **Decision:** supporting — The evaluated RAG and iterative code-generation workflow for microservice deployment offers concrete context, consistency-checking, and latency methods for software agents.
- **Evidence:** full text not read (status: pending).

### Jiang, X., Dong, Y., Wang, L. F., Fang, Z., Shang, Q., Li, G., Jin, Z., & Jiao, W. (2024). Self-Planning Code Generation with Large Language Models. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3672456

- **Decision:** supporting — Self-planning decomposes complex intent before implementation and improves correctness, readability, and robustness over direct and chain-of-thought code generation.
- **Evidence:** full text not read (status: pending).

### Chen, C., Su, J., Chen, J., Wang, Y., Bi, T., Yu, J., Wang, Y., Lin, X., Chen, T., & Zheng, Z. (2024). When ChatGPT Meets Smart Contract Vulnerability Detection: How Far Are We?. ACM Transactions on Software Engineering and Methodology. https://doi.org/10.1145/3702973

- **Decision:** supporting — Empirical smart-contract testing reveals low precision, task-dependent performance, answer uncertainty, and context-length limits in LLM vulnerability detection.
- **Evidence:** full text not read (status: pending).

### Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2303.17760

- **Decision:** supporting [preprint] — CAMEL evaluates role-playing and inception prompting for autonomous agent cooperation, providing transferable communication and specialization mechanisms outside SE.
- **Evidence:** full text not read (status: pending).

### Fu, M. C., Tantithamthavorn, C., Nguyen, V., & Le, T. (2023). ChatGPT for Vulnerability Detection, Classification, and Repair: How Far Are We?. https://doi.org/10.1109/apsec60848.2023.00085

- **Decision:** supporting — Large-scale vulnerability experiments show general ChatGPT substantially trails domain-specific models, exposing a security-relevant specialization and reliability limit.
- **Evidence:** full text not read (status: pending).

### Zheng, Q., Xia, X., Zou, X., Dong, Y., Wang, S., Xue, Y., Shen, L., Wang, Z., Wang, A., Li, Y., Su, T., Yang, Z., & Tang, J. (2023). CodeGeeX: A Pre-Trained Model for Code Generation with Multilingual Benchmarking on HumanEval-X. https://doi.org/10.1145/3580305.3599790

- **Decision:** supporting — HumanEval-X adds a concrete multilingual code benchmark and CodeGeeX supplies real-user productivity evidence, providing transferable evaluation support for coding-agent comparisons.
- **Evidence:** full text not read (status: pending).

### Ren, X., Ye, X., Zhao, D., Xing, Z., & Yang, X. (2023). From Misuse to Mastery: Enhancing Code Generation with Knowledge-Driven AI Chaining. https://doi.org/10.1109/ase56229.2023.00143

- **Decision:** supporting — KPC derives exception-handling failure modes and uses fine-grained check-rewrite prompt chains plus static and dynamic validation to reduce runtime bugs.
- **Evidence:** full text not read (status: pending).

### Liu, J., Xia, C. S., Wang, Y., & Zhang, L. (2023). Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2305.01210

- **Decision:** supporting [preprint] — EvalPlus exposes substantial hidden failure in standard code benchmarks by generating many additional tests, directly strengthening agent-output verification.
- **Evidence:** full text not read (status: pending).

### Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2303.11366

- **Decision:** supporting [preprint] — Reflexion's episodic memory and verbal feedback loop materially improve coding performance without model retraining, offering a concrete reliability remedy.
- **Evidence:** full text not read (status: pending).

### Zhang, K., Li, Z., Li, J., Li, G., & Jin, Z. (2023). Self-Edit: Fault-Aware Code Editor for Code Generation. https://doi.org/10.18653/v1/2023.acl-long.45

- **Decision:** supporting — Self-Edit uses test execution feedback and a fault-aware editor to repair generated code, producing large accuracy gains across nine models and two benchmarks.
- **Evidence:** full text not read (status: pending).

### Zeng, Z., Tan, H., Zhang, H., Li, J., Zhang, Y., & Zhang, L. (2022). An extensive study on pre-trained models for program understanding and generation. https://doi.org/10.1145/3533767.3534390

- **Decision:** supporting — Equivalent-benchmark and adversarial evaluations expose reproducibility, robustness, and model-selection risks relevant to reliable coding-agent assessment.
- **Evidence:** full text not read (status: pending).

### Mariano, B., Chen, Y., Feng, Y., Durrett, G., & Dillig, I. (2022). Automated transpilation of imperative to functional code using neural-guided program synthesis. Proceedings of the ACM on Programming Languages. https://doi.org/10.1145/3527315

- **Decision:** supporting — NGST2 couples neural search with concolic execution to prune invalid candidates and outperforms baselines in Java and Python modernization, providing a transferable hybrid verification pattern.
- **Evidence:** full text not read (status: pending).

### Liu, H., Tam, D., Muqeeth, M., Mohta, J., Huang, T., Bansal, M., & Raffel, C. (2022). Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2205.05638

- **Decision:** supporting [preprint] — The controlled PEFT-versus-context comparison demonstrates a concrete way to lower recurring compute and memory costs while improving task accuracy.
- **Evidence:** full text not read (status: pending).

### Garg, P., & Sengamedu, S. H. (2022). Synthesizing code quality rules from examples. Proceedings of the ACM on Programming Languages. https://doi.org/10.1145/3563350

- **Decision:** supporting — RhoSynth turns developer changes and feedback into deployed static-analysis rules with measured precision, providing a production-tested verification and human-refinement mechanism.
- **Evidence:** full text not read (status: pending).

### Imtiaz, N., Thorn, S., & Williams, L. (2021). A comparative study of vulnerability reporting by software composition analysis tools. https://doi.org/10.1145/3475716.3475769

- **Decision:** supporting — Divergent vulnerability reports across nine tools show why production security assurance should combine independent analyzers rather than trust one verifier.
- **Evidence:** full text not read (status: pending).

### Abcouwer, N., Daftry, S., Del Sesto, T., Toupet, O., Ono, M., Venkatraman, S., Lanka, R., Song, J., & Yue, Y. (2021). Machine Learning Based Path Planning for Improved Rover Navigation. https://doi.org/10.1109/aero50100.2021.9438337

- **Decision:** supporting — Retaining deterministic ACE safety checks while using ML only to rank candidates is a concrete transferable pattern for constraining probabilistic automation.
- **Evidence:** full text not read (status: pending).

### Chen, J., Patra, J., Pradel, M., Xiong, Y., Zhang, H., Hao, D., & Zhang, L. (2020). A Survey of Compiler Testing. ACM Computing Surveys. https://doi.org/10.1145/3363562

- **Decision:** supporting — Compiler-testing methods for input generation, test oracles, efficient execution, and bug actionability provide transferable verification infrastructure for generated code.
- **Evidence:** full text not read (status: pending).

### Bavishi, R., Lemieux, C., Fox, R., Sen, K., & Stoica, I. (2019). AutoPandas: neural-backed generators for program synthesis. Proceedings of the ACM on Programming Languages. https://doi.org/10.1145/3360594

- **Decision:** supporting — AutoPandas combines explicit API constraints with neural guidance on real-world synthesis tasks, providing an evaluated constrained-generation pattern for tool-using code agents.
- **Evidence:** full text not read (status: pending).

### Yin, P., & Neubig, G. (2018). TRANX: A Transition-based Neural Abstract Syntax Parser for Semantic Parsing and Code Generation. https://doi.org/10.18653/v1/d18-2002

- **Decision:** supporting — TRANX constrains generated formal representations with target syntax and generalizes across evaluated code tasks, offering a transferable structural reliability control.
- **Evidence:** full text not read (status: pending).

### Mendes, E., Rodríguez, P., Freitas, V., Baker, S., & Atoui, M. A. (2017). Towards improving decision making and estimating the value of decisions in value-based software engineering: the VALUE framework. Software Quality Journal. https://doi.org/10.1007/s11219-017-9360-z

- **Decision:** supporting — The industrial VALUE framework combines stakeholder elicitation with a validated Bayesian value model as a concrete human-governed method for software-development decisions.
- **Evidence:** full text not read (status: pending).

### Hu, V. C., Kuhn, D. R., Ferraiolo, D. F., & Voas, J. (2015). Attribute-Based Access Control. Computer. https://doi.org/10.1109/mc.2015.33

- **Decision:** supporting — Attribute-based access control is a concrete transferable control for limiting specialist agents' tool and data access in rapidly changing distributed environments.
- **Evidence:** full text not read (status: pending).

### Gvero, T., & Kunčak, V. (2015). Interactive Synthesis Using Free-Form Queries. https://doi.org/10.1109/icse.2015.224

- **Decision:** supporting — Interactive Synthesis enforces Java syntax, types, and scope while translating free-form developer intent and repairing expressions, providing a transferable constraint mechanism for code agents.
- **Evidence:** full text not read (status: pending).

### Crawford, K., & Schultz, J. (2013). Big Data and Due Process: Toward a Framework to Redress Predictive Privacy Harms. eYLS (Yale Law School). https://gretchen.law.nyu.edu/fac-articles/1028

- **Decision:** supporting — The proposed procedural data due-process rights provide a concrete accountability and redress framework for privacy harms from automated decisions.
- **Evidence:** full text not read (status: pending).

### Paasivaara, M., Durasiewicz, S., & Lassenius, C. (2008). Distributed Agile Development: Using Scrum in a Large Project. https://doi.org/10.1109/icgse.2008.38

- **Decision:** supporting — The distributed-software case study provides concrete coordination practices including synchronized sprints, daily communication, and scrum-of-scrums.
- **Evidence:** full text not read (status: pending).

### Hickey, A. M., & Davis, A. M. (2004). A Unified Model of Requirements Elicitation. Journal of Management Information Systems. https://doi.org/10.1080/07421222.2004.11045786

- **Decision:** supporting — The iterative elicitation model makes situational knowledge and technique selection explicit as controls for improving requirements quality.
- **Evidence:** full text not read (status: pending).

### Christel, M. G., & Kang, K. C. (1992). Issues in Requirements Elicitation. https://doi.org/10.21236/ada258932

- **Decision:** supporting — The elicitation methodology concretely structures fact-finding, evaluation, prioritization, and integration to reduce requirements failures in software development.
- **Evidence:** full text not read (status: pending).

### Aljedaani, W., Shaik, M. A., & Aljohani, A. (n.d.). A Multi-Agent Framework for Accessible Web Code Generation. W4A '26: Proceedings of the 23rd International Web for All Conference. https://doi.org/10.1145/3800424.3800453

- **Decision:** supporting — A11yAgent uses specialist agents to generate accessibility-compliant web code, a concrete requirements and verification workflow.
- **Evidence:** full text not read (status: pending).

### Shih, P.-A., Wang, S.-H., Li, Y.-C., Tu, C.-H., & Chang, C.-H. (n.d.). A Multi-Agent LLM Framework for Design Space Exploration in Autonomous Driving Systems. SAC '26: Proceedings of the 41st ACM/SIGAPP Symposium on Applied Computing. https://doi.org/10.1145/3748522.3779714

- **Decision:** supporting — The framework uses multiple LLM agents to explore hardware and software configurations, a transferable requirements and design-search method.
- **Evidence:** full text not read (status: pending).

### Das, S., Deb, N., Chaki, N., & Cortesi, A. (n.d.). A Multi-Agent RAG Framework for Regulatory Compliance Checking of Software Requirements. ACM Transactions on Software Engineering and Methodology (TOSEM), Volume 35, Issue 8. https://doi.org/10.1145/3785472

- **Decision:** supporting — The framework applies multi-agent RAG to regulatory checking of software requirements, providing a concrete compliance and verification method.
- **Evidence:** full text not read (status: pending).

### Bass, T. (n.d.). A Validation and Governance Framework for Multi-Agent LLM Scientific Software Development. IAIT '26: Proceedings of the 14th International Conference on Advances in Information Technology. https://doi.org/10.1145/3816713.3818807

- **Decision:** supporting — The governance case study identifies architect-level goal substitution and human oversight controls, directly informing production assurance.
- **Evidence:** full text not read (status: pending).

### Mondesire, S., Nsiye, E., Soykan, B., & Martin, G. (n.d.). Automating HPC Software Compilation, Deployment, and Error Resolution through an LLM-based Multi-Agent System. PEARC '25: Practice and Experience in Advanced Research Computing 2025: The Power of Collaboration. https://doi.org/10.1145/3708035.3736023

- **Decision:** supporting — The proposed LLM multi-agent workflow targets software compilation, deployment, and error resolution in HPC, but the visible abstract reports no comparative evidence.
- **Evidence:** full text not read (status: pending).

### Zhao, Y., Zhang, Z., Le, Q., Qu, L., & Xu, Z. (n.d.). Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems. KDD '26: Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2. https://doi.org/10.1145/3770855.3817590

- **Decision:** supporting — The dynamic compliance benchmark supplies a transferable method for testing procedural drift in execution-capable agent teams.
- **Evidence:** full text not read (status: pending).

### Gandhi, S., Patwardhan, M., Vig, L., & Shroff, G. (n.d.). BudgetMLAgent: A Cost-Effective LLM Multi-Agent system for Automating Machine Learning Tasks. AIMLSystems '24: Proceedings of the 4th International Conference on AI-ML Systems. https://doi.org/10.1145/3703412.3703416

- **Decision:** supporting — BudgetMLAgent proposes a cost-oriented multi-agent approach to code-heavy ML automation, but the abstract does not establish a matched single-agent comparison.
- **Evidence:** full text not read (status: pending).

### Sheng, R., Yang, Y., Shi, C., Lin, Y., Chen, Z., & Qu, H. (n.d.). DiLLS: Interactive Diagnosis of LLM-based Multi-agent Systems via Layered Summary of Agent Behaviors. CHI '26: Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems. https://doi.org/10.1145/3772318.3790815

- **Decision:** supporting — DiLLS provides layered behavioral summaries for interactive diagnosis of failures in LLM multi-agent systems, directly supporting observability and reliability.
- **Evidence:** full text not read (status: pending).

### Zhai, Y., Si, J., Wang, Y., & Lin, W. (n.d.). Engineering Practices in Open-Source Agent Frameworks: A Large-Scale Empirical Study. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering. https://doi.org/10.1145/3803437.3805533

- **Decision:** supporting — This large-scale empirical study of open-source agent frameworks can inform the engineering and reliability of multi-agent development infrastructure.
- **Evidence:** full text not read (status: pending).

### Ayon, R. S. (n.d.). From Helpful to Trustworthy: LLM Agents for Pair Programming. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering. https://doi.org/10.1145/3803437.3804875

- **Decision:** supporting — The pair-programming work targets intent alignment and review evidence for coding agents, providing transferable human oversight and verification methods.
- **Evidence:** full text not read (status: pending).

### Xu, Q., Wang, G., Briand, L., & Liu, K. (n.d.). Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3803418

- **Decision:** supporting — The approach uses multi-agent consensus for end-to-end JUnit test generation, a concrete testing method despite no visible comparative results.
- **Evidence:** full text not read (status: pending).

### Zhang, H., Shi, Y., Gu, X., Zhang, Z., & You, H. (n.d.). HyperAgent: Leveraging Hypergraphs for Topology Optimization in Multi-Agent Communication. AAMAS '26: Proceedings of the 25th International Conference on Autonomous Agents and Multiagent Systems. https://doi.org/10.65109/QTVF9552

- **Decision:** supporting — HyperAgent offers hypergraph-based communication-topology optimization for ineffective LLM multi-agent collaboration, a transferable coordination method.
- **Evidence:** full text not read (status: pending).

### Mantzouranidis, S., & Britto, R. (n.d.). MAS-SRE: A Multi-Agent System for Security Requirements Engineering. PROMISE '26: Proceedings of the 22nd International Conference on Predictive Models and Data Analytics in Software Engineering. https://doi.org/10.1145/3803846.3807470

- **Decision:** supporting — MAS-SRE uses specialist agents to turn business needs into standards-grounded software security requirements, a concrete governance method.
- **Evidence:** full text not read (status: pending).

### Li, J., & Storhaug, A. (n.d.). Reproducible, Explainable, and Effective Evaluations of Agentic AI for Software Engineering. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering. https://doi.org/10.1145/3803437.3805548

- **Decision:** supporting — Reproducible and explainable evaluation of opaque software-engineering agents is a concrete assurance approach transferable to multi-agent systems.
- **Evidence:** full text not read (status: pending).

### Stepin, A., Tolstokulakov, B., Kulikov, V., & Kabanov, A. (n.d.). ScholForge: A Multi-Agent LLM System for Autonomous Software Engineering Research. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering. https://doi.org/10.1145/3803437.3807394

- **Decision:** supporting — ScholForge presents hierarchical specialist orchestration across software-research activities, including building and evaluating software, without reported comparative results in the abstract.
- **Evidence:** full text not read (status: pending).

### Zhang, Q., Gao, C., Han, Y., Shang, Y., & Fang, C. (n.d.). SGAgent: Suggestion-Guided LLM-Based Multi-Agent Framework for Repository-Level Software Repair. ACM Transactions on Software Engineering and Methodology (TOSEM), Just Accepted. https://doi.org/10.1145/3818617

- **Decision:** supporting — SGAgent proposes suggestion-guided specialist collaboration for repository-level repair, but the abstract excerpt gives no empirical comparison or results.
- **Evidence:** full text not read (status: pending).

### Jiang, C., Wang, D., Liu, D., Xu, Z., Wen, C., & Ming, Z. (n.d.). StarVerus: LLM-Powered Multi-Agent Collaboration for Industrial Rust Code Verification Automation. KDD '26: Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2. https://doi.org/10.1145/3770855.3818485

- **Decision:** supporting — StarVerus offers specialist-agent automation for Rust specifications and verification, a concrete assurance method despite no reported comparison in the abstract.
- **Evidence:** full text not read (status: pending).

### Shen, M.-T., & Joung, Y.-J. (n.d.). TALM: Dynamic Tree-Structured Multi-Agent Framework with Long-Term Memory for Scalable Code Generation. AGENT '26: Proceedings of the 2026 International Workshop on Agentic Engineering. https://doi.org/10.1145/3786167.3788424

- **Decision:** supporting — TALM combines dynamic tree topology with long-term memory for scalable code generation, directly targeting rigidity and context-management limits.
- **Evidence:** full text not read (status: pending).

### Shang, Y., Zhang, Q., Zhan, Z., Huang, K., & Fang, C. (n.d.). TestAgent: A Multi-Agent LLM Framework for Repository-Level Unit Test Generation. FSE Companion '26: Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering. https://doi.org/10.1145/3803437.3806428

- **Decision:** supporting — TestAgent provides a repository-aware specialist workflow for unit-test generation, directly addressing context and verification limitations.
- **Evidence:** full text not read (status: pending).

### Dong, T., Shi, S., Sampath, H., & Macvean, A. (n.d.). Towards AI as a Collaborative Partner: A Taxonomy of AI Agent Behavior in Software Engineering. AIware '26: Proceedings of the 3rd ACM International Conference on AI-Powered Software. https://doi.org/10.1145/3805760.3814913

- **Decision:** supporting — The software-engineering-specific taxonomy supplies a concrete vocabulary for evaluating collaborative agent behavior, although it does not compare multi-agent architectures.
- **Evidence:** full text not read (status: pending).

### Elgammal, M. A., Wu, J., Liu, L., Kim, T., & Betz, V. (n.d.). VTR-LLM: Multi-Agent LLM Framework for Automated Debugging of FPGA CAD Flows. ACM Transactions on Reconfigurable Technology and Systems (TRETS), Just Accepted. https://doi.org/10.1145/3829373

- **Decision:** supporting — VTR-LLM applies multi-agent debugging to complex FPGA CAD software flows, offering a concrete error-resolution workflow without visible comparative results.
- **Evidence:** full text not read (status: pending).
