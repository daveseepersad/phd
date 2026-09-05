# PRISMA 2020 Flow — specialized multi-agent versus single-agent LLM software engineering: comparative performance, coordination failures, verification, reliability, sustainability, and future work

Generated 2026-09-05 from persisted run artifacts only.

```mermaid
flowchart TD
    A["Identification<br/>Database records: 598<br/>acm: 150<br/>arxiv: 70<br/>crossref: 100<br/>ieee: 102<br/>openalex: 100<br/>scholar: 76"]
    B["Citation chaining (3 rounds)<br/>Records discovered: 318"]
    C["Unique records after merge: 417<br/>Duplicates removed: 135"]
    D["Records screened: 417"]
    E["Records excluded: 116<br/>context: 66<br/>unresolved: 32"]
    F["Reports sought for retrieval: 203"]
    G["Reports not retrieved: 100"]
    H["Reports assessed for eligibility: 103"]
    I["Reports excluded:<br/>none recorded"]
    J["Studies included in synthesis: 103"]
    A --> C
    B --> C
    C --> D
    D --> E
    D --> F
    F --> G
    F --> H
    H --> I
    H --> J
```

| Phase | Measure | Value |
|---|---|---|
| Identification | Search runs | 4 |
| Identification | Database records (raw) | 598 |
| Identification | Sources used | acm, arxiv, crossref, ieee, openalex, scholar |
| Identification | Citation-chaining records | 318 |
| Identification | Unique records after merge | 417 |
| Deduplication | Duplicates removed | 135 |
| Screening | Records screened | 417 |
| Screening | Decisions | context: 66, core: 73, exclude: 116, supporting: 130, unresolved: 32 |
| Retrieval | Reports sought | 203 |
| Retrieval | Reports retrieved | 103 |
| Full-text | Reports assessed | 103 |
| Full-text | Excluded with reasons | none recorded |
| Included | Studies in synthesis | 103 |
