# Candidate Topics — 20260905-ideation-llm-agents-for-business-process-automati-plus-1

Scanned 2026-09-05 from `landscape.json`; scored per
`.github/skills/topic-ideation/references/RUBRIC.md`.

Two seed areas were scanned. They behave very differently, and that difference
drives most of the scoring below.

*LLM agents for business process automation* is an established area: 143
on-topic works since 2022, growing from 15 (2024) to 38 (2025) with 87 already
in a partial 2026, and — critically — a refereed spine that includes *British
Journal of Management*, *Lecture Notes in Business Information Processing*,
*Lecture Notes in Computer Science*, *IEEE Access*, *Information*, and
*Algorithms*. Criterion 4 is scoreable here.

*LLM agent evaluation and observability in production* is a genuinely new area
rather than a growing one: zero on-topic works in 2022 and 2023, one in 2024,
three in 2025, then 103 in a partial 2026. The scanner withholds a momentum
ratio because a jump from one work to three is an origin, not a trend. Its
venue list is dominated by Zenodo, Research Square, and Preprints.org, and its
most-cited on-topic paper carries five citations. Every candidate drawn from
this area therefore scores high on novelty and low on refereed anchors, and no
amount of enthusiasm changes that.

Candidates are ordered by total score.

## Candidate 1: Process-model constraints as a control on agent autonomy

**Research question.** In compliance-critical business processes, does binding
an LLM agent to an explicit process model reduce policy violations without a
corresponding loss in task completion, compared with an agent given the same
policy as natural-language instructions?

**Why now.** The on-topic literature grew 2.53x between 2024 and 2025 (15 to 38
works) and has already produced 87 works in a partial 2026, so the practices
are being invented right now. Two 2026 papers propose opposite ends of the
control spectrum without comparing them: Pacella and Papadia argue for a
"floor-safety guarantee" that constrains compliance-critical LLM routing
(10.3390/a19080627), while Boinapalli's GALENA architecture enforces compliance
through a governance layer wrapped around autonomous multi-agent workflow
automation (10.64971/j.cph.eijtem.v13.i3.12.2026). Monti and Leotta take the
process-model-first route by generating executable process code from natural
language (10.1007/978-3-031-70418-5_8), and Tebourbi and Nouzri drive
multi-agent systems directly from BPMN (10.3390/info16090809). Schwartz and
Yaeli named trust in business-process automation agents as an open problem in
2023 and it has not been settled since (10.48550/arxiv.2308.05391).

**Expected experiment shape.** Three conditions over a fixed set of business
processes: unconstrained agent with the policy in the prompt, agent constrained
by an explicit process model, and a deterministic rule baseline. Each process
runs with injected variability (missing fields, out-of-policy requests,
ambiguous routing) across repeated trials per condition to support significance
testing. Primary outcome is policy-violation rate per run, secondary outcomes
are task completion, token cost, and wall-clock latency. Infrastructure is a
hosted model API, an off-the-shelf process engine, and a violation checker
written against the policy — buildable by one student without proprietary data.

**Business relevance.** This is the build/buy decision every enterprise faces
when replacing a rule engine with an agent. The answer changes whether a
regulated firm can deploy an agent at all, and whether the process model that
firms already maintain is a legacy artifact or a safety control worth keeping.

**Rubric scores.**

| Criterion | Score | Justification (cite DOIs) |
|---|---:|---|
| Problem clarity | 4/5 | Multiple refereed and archival papers take opposing positions on where control belongs — constrained routing (10.3390/a19080627) versus governed autonomy (10.64971/j.cph.eijtem.v13.i3.12.2026) versus model-generated execution (10.1007/978-3-031-70418-5_8) — and none compares them head to head. Falsifiable in one sentence, but no paper stages the disagreement explicitly, which holds it below 5. |
| Experimental tractability | 4/5 | Treatment/control design over public process definitions with a hosted API; the violation checker must be built, which keeps it off 5. Precedent for the harness exists in the BPMN-driven multi-agent design of 10.3390/info16090809. |
| Measurable outcomes | 4/5 | Violation rate, completion rate, cost, and latency are all directly countable, and 10.47852/bonviewaia52026307 reports a comparable case-study outcome set. No single accepted benchmark exists, which holds it below 5. |
| Refereed anchors | 4/5 | A steady refereed stream: *Algorithms* (10.3390/a19080627), *Information* (10.3390/info16090809), LNBIP (10.1007/978-3-031-70418-5_8), LNCS (10.1007/978-3-031-70239-6_2), *IEEE Access* (10.1109/access.2025.3549312). No systematic review yet anchors Chapter 2, so not 5. |
| Practitioner alignment | 5/5 | Sits inside enterprise agent practice and is visibly being asked: 10.1007/978-3-031-70239-6_2 studies ERP process automation, and 10.47852/bonviewaia52026307 is a corporate expense-processing deployment. |
| Novelty window | 4/5 | On-topic volume grew 2.53x (15 to 38) with 87 in partial 2026, and the specific three-way comparison is unclaimed in the scan. Scale does not settle it because the question is about control design, not model capability. |
| **Total** | **25/30** | |

**Next step.**

    S=.github/skills/publications-search/scripts
    RUN=$(uv run $S/protocol.py init "process model constraints versus natural language policy for compliance critical LLM business process agents" | tail -1)
    # RQ1 verbatim goes in $RUN/protocol.md section 1
    uv run $S/search.py "LLM agents for business process automation compliance" --run-dir "$RUN" \
      --sources openalex,crossref,scholar,acm,ieee --from-year 2023

## Candidate 2: The agent harness as an uncontrolled variable

**Research question.** How much of the reported performance difference between
LLM agent configurations is attributable to the harness — scaffold, retry
policy, and tool schema — rather than to the model or the agent topology under
study?

**Why now.** The observability area produced zero on-topic works in 2022 and
2023, one in 2024, three in 2025, and 103 in a partial 2026, so the vocabulary
for talking about harnesses is being fixed right now. Meng and Wang's survey
treats the harness as a first-class object of study rather than plumbing
(10.20944/preprints202604.0428.v3), and production harness papers are appearing
in parallel — Argos generates anomaly-detection rules autonomously
(10.48550/arxiv.2501.14170) and LATS-RCA applies tree search to microservice
root-cause analysis in LNCS (10.1007/978-3-032-36590-3_14). The freshest arXiv
submissions in the same scan show the harness becoming an attack surface and a
control surface at once, with hook updates steering agent harnesses toward
malicious behavior (2026-09-03) and error-dependency graphs attributing faults
across multi-agent systems (2026-09-01).

**Expected experiment shape.** Hold the model and the task suite fixed and vary
the harness along named axes — retry count, tool-schema verbosity, reflection
depth — across repeated runs, then decompose outcome variance by axis. A second
arm re-runs a published topology comparison under two different harnesses to
test whether the published direction of effect survives. Outcomes are task
success, variance explained per axis, and cost per success. Public agent
harnesses and public benchmarks make the matrix enumerable in advance, which is
what makes a power analysis possible before anything is built.

**Business relevance.** Enterprises select agent frameworks on benchmark claims.
If harness choice explains more variance than topology, procurement criteria
and internal build standards are both measuring the wrong thing, and the
finding transfers directly into framework-selection guidance.

**Rubric scores.**

| Criterion | Score | Justification (cite DOIs) |
|---|---:|---|
| Problem clarity | 4/5 | The harness survey (10.20944/preprints202604.0428.v3) names the harness as an under-examined determinant of agent behavior, and the question is falsifiable in one sentence. It is not 5 because the disagreement is implicit in inconsistent setups rather than staged between named papers. |
| Experimental tractability | 5/5 | Conditions x tasks x repetitions are enumerable today from public harnesses and public benchmarks, so a power analysis is possible before building; the comparison needs no proprietary access. |
| Measurable outcomes | 5/5 | Task success, variance decomposition, and cost per success are orthogonal and interpretable, and results compare number-for-number against the published baselines being re-run. |
| Refereed anchors | 2/5 → **4/5**, corrected 2026-09-05 | Scored 2/5 from the scan: only LATS-RCA was archival (10.1007/978-3-032-36590-3_14), the survey was a preprint (10.20944/preprints202604.0428.v3), the most-cited on-topic paper had five citations (10.48550/arxiv.2501.14170), and the venue list was led by Zenodo, Research Square, and Preprints.org. The deep-dive run refutes that score — see the correction note below. |
| Practitioner alignment | 4/5 | Framework selection is a live enterprise decision and sits in the student's domain; it is not 5 because the question is posed to researchers first and buyers second. |
| Novelty window | 5/5 | The scan shows the area rising from one on-topic work in 2024 to 103 in a partial 2026 while remaining almost entirely unrefereed — a rising, under-published niche where a careful solo study stays citable regardless of frontier-model progress. |
| **Total** | **25/30 → 27/30** | |

**Correction, 2026-09-05.** The 2/5 above was wrong, and the deep-dive run is
what found it wrong — which is the reason the rubric hands its weakest criterion
to a review rather than settling it from a scan. Screening 786 abstracts in
`results/20260905-agent-harness-as-a-confounding-variable` surfaced a substantial
harness-attribution literature that the seed area's narrow query never reached,
including a position paper arguing that agent comparisons should not be published
without disclosing the harness, a survey of agent system and harness design, a
study attributing coding-agent quality shifts to scaffolding evolution rather
than the model, and controlled decompositions such as HAL (model × scaffold ×
benchmark), CORE-Bench, AblationBench, BrowserGym, and AFlow. Ninety-nine
records were screened core. The criterion is re-scored to 4/5: a steady stream
with benchmark and survey anchors, held below 5 only because the archival
conversation is young enough that replications and documented disagreements are
still thin.

The original 2/5 is left in place rather than overwritten. It is evidence of how
the topic was chosen, and the scan's error is itself a finding: an ideation query
tight enough to keep the key-papers table on topic can be too tight to see a
literature that names the same problem in different words.

**Next step.**

    S=.github/skills/publications-search/scripts
    RUN=$(uv run $S/protocol.py init "agent harness as a confounding variable in LLM agent performance comparisons" | tail -1)
    # RQ1 verbatim goes in $RUN/protocol.md section 1
    uv run $S/search.py "LLM agent harness scaffold tool schema evaluation" --run-dir "$RUN" \
      --sources openalex,crossref,arxiv,scholar,acm,ieee --from-year 2024

## Candidate 3: The variability threshold where agents beat rules

**Research question.** At equal task success, how does the total cost of an
LLM-agent implementation of a business process compare with a deterministic
rule implementation, and at what level of process variability does the agent
become the cheaper option?

**Why now.** Deployment case studies are arriving with cost framed as the
deciding factor — corporate expense processing (10.47852/bonviewaia52026307),
ERP process automation (10.1007/978-3-031-70239-6_2), and data-warehouse
delivery at Tencent (10.48550/arxiv.2608.09185) — but each reports a single
operating point rather than a curve. Brown and Davison call for theory-driven
rather than anecdotal accounts of generative AI in business and management
(10.1111/1467-8551.12788), and a cost-versus-variability curve is exactly the
kind of transferable result that answers them.

**Expected experiment shape.** Implement the same process twice, once as rules
and once as an agent, then sweep a variability parameter — proportion of inputs
requiring judgment, schema drift rate, exception frequency — measuring cost per
successfully completed case at each level. The crossing point, if one exists,
is the result. Repetitions at each level give confidence intervals.

**Business relevance.** This is the automation-portfolio question: which
processes should stay deterministic. It changes sequencing decisions for every
firm holding a backlog of candidate processes.

**Rubric scores.**

| Criterion | Score | Justification (cite DOIs) |
|---|---:|---|
| Problem clarity | 3/5 | The gap is real and named — single-operating-point case studies (10.47852/bonviewaia52026307, 10.1007/978-3-031-70239-6_2) with no curve — but stated as a broad economics question rather than a documented disagreement between papers. |
| Experimental tractability | 4/5 | A clear sweep design on a modest API budget; building two complete implementations of the same process is real work but bounded. |
| Measurable outcomes | 5/5 | Cost per successful case, success rate, and a defined variability index are orthogonal, and the crossing point is interpretable without appeal to judgment. |
| Refereed anchors | 3/5 | Several refereed anchors exist (10.1111/1467-8551.12788, 10.1007/978-3-031-70239-6_2, 10.47852/bonviewaia52026307) but there is no benchmark paper or review to anchor Chapter 2, and the Tencent account is a preprint (10.48550/arxiv.2608.09185). |
| Practitioner alignment | 5/5 | Practitioners are visibly asking this in deployment write-ups, and the answer is a procurement and sequencing criterion. |
| Novelty window | 3/5 | Active and growing (2.53x, 15 to 38 on-topic works), with the curve unclaimed in the scan — but a well-resourced group could publish the same sweep quickly. |
| **Total** | **23/30** | |

**Next step.**

    S=.github/skills/publications-search/scripts
    RUN=$(uv run $S/protocol.py init "cost of LLM agent versus deterministic rule implementations of business processes" | tail -1)
    # RQ1 verbatim goes in $RUN/protocol.md section 1
    uv run $S/search.py "LLM agent versus rule based process automation cost" --run-dir "$RUN" \
      --sources openalex,crossref,scholar,acm,ieee --from-year 2024

## Candidate 4: Whether agent traces can carry an audit

**Research question.** Do the execution traces emitted by LLM-agent business
processes contain sufficient evidence for an independent reviewer to reconstruct
why a compliance-relevant decision was made, and does trace-schema design change
reconstruction accuracy?

**Why now.** This candidate fuses the two scanned areas: the governance thread
in the business-process card and the observability thread in the evaluation
card. Governance architectures now assume an auditable trail exists
(10.64971/j.cph.eijtem.v13.i3.12.2026, 10.3390/a19080627) and privacy
frameworks assume context is recoverable after the fact
(10.1109/access.2025.3549312), while the observability card's freshest arXiv
work is still arguing about what a live trace model for long-horizon agents and
their observers should even contain (2026-09-01). Schwartz and Yaeli's trust
considerations sit directly on this seam (10.48550/arxiv.2308.05391).

**Expected experiment shape.** Generate traces from agent runs under two or
three trace schemas, then have independent reviewers reconstruct the decision
rationale for sampled cases, scored against ground truth recorded during
generation. Outcome is reconstruction accuracy per schema plus time to
reconstruct.

**Business relevance.** Regulated deployments stand or fall on auditability.
A schema that measurably improves reconstruction is directly adoptable.

**Rubric scores.**

| Criterion | Score | Justification (cite DOIs) |
|---|---:|---|
| Problem clarity | 3/5 | Governance work assumes auditable traces (10.3390/a19080627, 10.64971/j.cph.eijtem.v13.i3.12.2026) while trace-model work is unsettled, but no paper states the gap as an open problem, so the framing is broad rather than falsifiable as stated. |
| Experimental tractability | 2/5 | Reconstruction requires independent human reviewers, and reviewer variance is the dominant confound for a solo researcher without a rater pool. This is the criterion to reframe before investing. |
| Measurable outcomes | 3/5 | Reconstruction accuracy and time are measurable, but ground truth is constructed by the same student who designs the schemas, and no established benchmark applies. |
| Refereed anchors | 3/5 | Refereed governance anchors exist (10.3390/a19080627, 10.1109/access.2025.3549312) but the observability half rests on arXiv and Zenodo, so the spine is one-sided. |
| Practitioner alignment | 5/5 | Auditability is a procurement gate in finance, healthcare, and insurance, and the student's domain access is a real advantage. |
| Novelty window | 4/5 | The fusion is unclaimed in either card, and trace-schema design is a methodology question that scale does not close. |
| **Total** | **20/30** | |

Workable but not yet fundable: reframe experimental tractability — for example
by replacing human reconstruction with an automated reconstruction agent scored
against recorded ground truth — before this candidate is worth a deep dive.

## Candidate 5: Blame assignment in multi-agent business workflows

**Research question.** In multi-agent business workflows, can automated error
attribution localize the responsible step with accuracy comparable to a human
analyst reviewing the same trace?

**Why now.** Error attribution is emerging as a named sub-problem: the scan's
freshest arXiv submissions include error-dependency-graph-guided multi-error
attribution in multi-agent LLM systems (2026-09-01) and counterfactual
evaluation of agent recovery from ambiguous tool outcomes
(10.21203/rs.3.rs-10730245/v1), alongside archival root-cause work in
microservices (10.1007/978-3-032-36590-3_14).

**Expected experiment shape.** Inject known faults into multi-agent workflow
runs, apply attribution methods to the resulting traces, and score localization
against the injected ground truth, with a human-analyst arm for comparison.

**Business relevance.** Operating an agent workflow means answering "which step
broke" under time pressure; attribution accuracy is an operations-cost question.

**Rubric scores.**

| Criterion | Score | Justification (cite DOIs) |
|---|---:|---|
| Problem clarity | 3/5 | Named as an active sub-problem in current arXiv work and in 10.21203/rs.3.rs-10730245/v1, but not yet a documented disagreement between refereed papers. |
| Experimental tractability | 4/5 | Fault injection gives free ground truth, so the design is clean and repeatable on public workflows; the human-analyst arm adds cost without dominating it. |
| Measurable outcomes | 4/5 | Localization accuracy against injected faults is exact, with time-to-attribution as a secondary outcome; no standard benchmark exists yet. |
| Refereed anchors | 2/5 | Only 10.1007/978-3-032-36590-3_14 is archival; the rest of the on-topic evidence is arXiv, Research Square, and Zenodo, consistent with an area holding zero on-topic works before 2024. |
| Practitioner alignment | 3/5 | Directly relevant to operating agent workflows, but closer to platform engineering than to the business-process decisions the student owns. |
| Novelty window | 5/5 | A clear open niche: rising sharply (one on-topic work in 2024 to 103 in partial 2026) and almost entirely unrefereed. |
| **Total** | **21/30** | |

## Candidate 6: Specialist decomposition for structured enterprise workflows

**Research question.** For structured enterprise workflow execution, does
decomposing work across role-specialized agents improve end-to-end task success
over a single generalist agent given the same tools and token budget?

**Why now.** The scan surfaces specialist-versus-generalist framings appearing
directly in titles (10.48550/arxiv.2607.14456), alongside deployed workflow
systems (10.1145/3731545.3743644) and domain-agnostic copilots
(10.1109/etis64005.2025.10961403), with role-specialized agents applied to
agile project management in *Electronics* (10.3390/electronics14010087).

**Expected experiment shape.** Matched-budget comparison of a specialized
multi-agent configuration against a single generalist agent across structured
enterprise workflows, with token budget and tool access held constant.

**Business relevance.** Determines whether the added operational complexity of
a multi-agent deployment is repaid in task success.

**Rubric scores.**

| Criterion | Score | Justification (cite DOIs) |
|---|---:|---|
| Problem clarity | 4/5 | The comparison is explicitly framed in the literature (10.48550/arxiv.2607.14456) and falsifiable in one sentence. |
| Experimental tractability | 4/5 | Matched-budget designs are standard and buildable, though holding budget genuinely constant across topologies takes care. |
| Measurable outcomes | 4/5 | Task success and cost apply directly, with published baselines available for comparison. |
| Refereed anchors | 4/5 | *Electronics* (10.3390/electronics14010087), ACM (10.1145/3731545.3743644), and IEEE (10.1109/etis64005.2025.10961403) give a workable spine. |
| Practitioner alignment | 4/5 | Sits in the student's domain and informs deployment architecture. |
| Novelty window | 1/5 | Parked here. This is the question the student has already reviewed to saturation in `results/20260904-specialized-multi-agent-versus-single-ag`, and multiple groups are publishing the same comparison. A single criterion at 0-1 sinks the candidate regardless of total. |
| **Total** | **21/30** | |

Parked on criterion 6 per the rubric's stopping rule, and retained here only to
record that the overlap with prior work was checked rather than missed.

## Handoff

Candidates 1 and 2 tie at 25/30 and are taken forward to
`publications-search`, one from each scanned area. They fail in opposite
directions, which is the useful part: Candidate 1 has the refereed spine and
the weaker methodological novelty, Candidate 2 has the open niche and a
refereed-anchor score of 2/5 that the deep-dive run must either repair or
confirm. If Candidate 2's review cannot find archival anchors beyond this
scan's narrow query, its rubric score stands and the candidate should be
parked, whatever the topic's appeal.

**Outcome, 2026-09-05.** Both reviews were run. Candidate 1 completed all nine
stages and produced a rendered document; its review found that the research
question as posed contains a confound, because the studies reporting large
violation reductions each bind a different artefact at a different enforcement
site, and the strongest ablation attributes the effect to tool mediation rather
than to process structure. Candidate 2's review repaired its own weakest
criterion, as recorded above, so neither candidate should be parked; Candidate 2
is now the higher-scoring of the two at 27/30.
