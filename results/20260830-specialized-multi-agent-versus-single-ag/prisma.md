# PRISMA 2020 Flow — specialized multi-agent versus single-agent LLM software engineering: comparative performance, coordination failures, verification, reliability, sustainability, and future work

Generated 2026-09-04 from persisted run artifacts only.

```mermaid
flowchart TD
    A["Identification<br/>Database records: not recorded<br/>not recorded"]
    B["Citation chaining (3 rounds)<br/>Records discovered: 250"]
    C["Unique records after merge: 522<br/>Duplicates removed: not recorded"]
    D["Records screened: 522"]
    E["Records excluded: 177<br/>context: 90<br/>unresolved: 48"]
    F["Reports sought for retrieval: 207"]
    G["Reports not retrieved: 159"]
    H["Reports assessed for eligibility: 48"]
    I["Reports excluded:<br/>not recorded"]
    J["Studies included in synthesis: 48"]
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
| Identification | Search runs | not recorded |
| Identification | Database records (raw) | not recorded |
| Identification | Sources used | openalex, crossref, scholar, acm, ieee |
| Identification | Citation-chaining records | 250 |
| Identification | Unique records after merge | 522 |
| Deduplication | Duplicates removed | not recorded |
| Screening | Records screened | 522 |
| Screening | Decisions | context: 90, core: 44, exclude: 177, supporting: 163, unresolved: 48 |
| Retrieval | Reports sought | 207 |
| Retrieval | Reports retrieved | 48 |
| Full-text | Reports assessed | 48 |
| Full-text | Excluded with reasons | not recorded |
| Included | Studies in synthesis | 48 |

## Not recorded

- No fulltext-exclusions.json; full-text exclusions (if any) were not recorded.
- Per-source hit counts were not persisted (no usable search-log.json).
- Duplicate-removal counts were not persisted (no dedup-log.json).
