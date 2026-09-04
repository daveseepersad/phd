# Seed Areas — Generative-AI / Agentic Landscape

Starter areas for `scan.py`. Each H2 heading is sent verbatim as the OpenAlex
search query, and its leading content terms form the arXiv query, so keep
headings short, descriptive, and rich in content words. The rationale under
each heading guides Stage 2 judgment; the scanner ignores it. Edit freely:
add, remove, or sharpen areas before a scan.

## LLM agents for business process automation

Enterprises are replacing brittle RPA and BPM rule engines with LLM agents
that read documents, make routing decisions, and execute multi-step processes.
The open question is when agentic automation beats deterministic workflows on
reliability and total cost, which is exactly the trade-off practitioners own.

## LLM agent evaluation and observability in production

Offline benchmarks say little about agents that run for hours against live
systems. Tracing, regression detection, and evaluation-in-the-loop for
deployed agents is where enterprise buyers feel the most pain and where
refereed methodology is still thin relative to vendor tooling.

## Cost-aware LLM agent orchestration and resource budgeting

Agent pipelines multiply token spend: reflection loops, retries, and
multi-agent debate can 10x the cost of a single call for marginal quality.
Budget-constrained orchestration — choosing model tiers, capping loops,
routing to cheaper paths — is a measurable optimization problem a solo
researcher can study with public benchmarks and an API budget.

## Agentic retrieval augmented generation for enterprise knowledge work

Static RAG is giving way to agents that plan retrieval, query multiple
systems, and verify their own citations against enterprise corpora. Knowledge
work is the largest white-collar cost center, so even small measured gains in
answer faithfulness or analyst throughput carry direct business value.

## Human-agent teaming in enterprise workflows

Real deployments interleave agent actions with human approvals, escalations,
and corrections. Where to place the handoff, how trust calibrates over time,
and what oversight actually catches are empirical questions that sit between
HCI and IS venues and map directly onto how SMEs roll agents into teams.

## LLM agent memory and continual adaptation

Agents that forget every session cannot hold an account relationship or learn
a firm's conventions. Long-horizon memory, selective retention, and
adaptation without fine-tuning are active research fronts with clear
enterprise stakes in personalization and institutional knowledge capture.

## LLM agent tool use and API integration reliability

Tool calling is the load-bearing joint of every business agent, and it fails
quietly: wrong arguments, stale schemas, silent partial success. Reliability
engineering for tool use — contracts, retries, verification layers — is
benchmarkable today and underexplored relative to its production importance.

## LLM agent governance and auditability in regulated industries

Finance, healthcare, and insurance cannot deploy agents they cannot audit.
Action logs, policy enforcement, and compliance-grade traceability for
agentic decisions connect directly to emerging AI regulation and give a
practitioner-researcher a domain-access advantage big labs lack.

## LLM multi-agent negotiation and market mechanisms

When agents transact with other agents — procurement, scheduling, pricing —
mechanism design meets language models. Emergent collusion, strategic
deception, and welfare outcomes of agent-mediated markets are measurable in
simulation and increasingly relevant as agent-to-agent commerce protocols land.

## Customer-facing conversational agent quality assurance

Customer service is the most widely deployed business agent surface, yet QA
still leans on spot checks and CSAT proxies. Systematic pre-release testing,
guardrail coverage, and failure taxonomies for conversational agents are
tractable to study and immediately transferable to industry practice.

## Prompt injection and security for enterprise agent deployments

An agent with tool access turns every retrieved document and inbound email
into a potential attack surface. Injection defenses, privilege containment,
and security evaluation for agentic systems are rising fast in both refereed
and industry literature, with enterprise deployments as the forcing function.

## Computer-use GUI agents for back-office automation

Vision-based agents that operate unmodified GUIs promise automation where no
API exists — legacy ERP screens, claims portals, spreadsheets. Reliability on
long back-office task chains is still poor, which makes measured improvement
and honest failure analysis a credible, business-adjacent research target.
