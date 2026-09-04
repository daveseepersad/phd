---
title: Publication Source Reference
description: Query syntax, citation chaining, selectors, and access behavior for publication sources
---

## Source Reference

Query syntax, DOM selectors, and known quirks per source. Selectors on
publisher sites drift; when a source returns zero results, check here first,
then inspect the live page.

## OpenAlex

Endpoint: `https://api.openalex.org/works`

The metadata backbone. No key, no rate-limit drama, and it carries
`cited_by_count`, which is the ranking signal Scholar is otherwise needed for.

| Field | Maps to |
|---|---|
| `display_name` | title |
| `authorships[].author.display_name` | authors |
| `cited_by_count` | citations |
| `primary_location.source.display_name` | venue |
| `best_oa_location.pdf_url` | direct PDF when open access |
| `abstract_inverted_index` | abstract |

Abstracts arrive as an inverted index (`{"word": [positions]}`) and must be
rebuilt into reading order; `_common.reconstruct_abstract` does this.

Set `CONTACT_EMAIL` to join the polite pool and get more consistent latency.

### Citation snowballing

OpenAlex provides both directions needed for auditable snowballing:

* Resolve an anchor with `/works/doi:<doi>` or `/works/<OpenAlex-ID>`
* Retrieve forward citations with `/works?filter=cites:<OpenAlex-ID>`
* Read `referenced_works` from an anchor, then retrieve those records in batches
	with `/works?filter=openalex_id:<ID1>|<ID2>`

The scripts record every citation edge and preserve keyword, forward-citation,
and backward-reference discovery methods through deduplication.

## Crossref

Endpoint: `https://api.crossref.org/works`

Broadest DOI coverage and useful for verifying a citation before it goes in a
bibliography. Citation counts (`is-referenced-by-count`) run lower than
OpenAlex or Scholar because they only count Crossref-deposited references.

Filter ACM specifically with `filter=member:320`.

Abstracts are frequently absent, and present ones are JATS XML needing tag
stripping.

Useful bibliographic fields beyond the basics: `type` (work type;
`posted-content` marks preprints), `volume`, `issue`, `page`, `publisher`.

## arXiv

Endpoint: `https://export.arxiv.org/api/query`

The grey-literature backbone (cs.SE / cs.AI / cs.MA preprints appear here
months before any publisher indexes them). Keyless Atom-XML API; parseable
with stdlib `xml.etree.ElementTree`.

Query: `search_query=all:<terms>&sortBy=relevance&sortOrder=descending&max_results=<n>`

| Atom element | Maps to |
|---|---|
| `entry/title` | title (collapse internal whitespace) |
| `entry/author/name` | authors |
| `entry/summary` | abstract |
| `entry/published` | year (first four characters) |
| `entry/id` | abs-page URL |
| `entry/link[@title="pdf"]` | pdf_url (all arXiv PDFs are open) |
| `entry/arxiv:doi` | DOI, present only when the author registered one |

Namespaces: Atom `http://www.w3.org/2005/Atom`, arXiv extensions
`http://arxiv.org/schemas/atom`.

Quirks:

- No publication-date filter parameter; filter on `published` client-side.
- Every record is a preprint by definition: `venue = "arXiv preprint"`, `work_type = "preprint"`, `is_preprint = true`.
- No citation counts; records lean on OpenAlex enrichment for the citation term.
- The published-version DOI usually differs from the `10.48550/arXiv.*` DOI; title-merge reconciles them at dedup time.
- arXiv asks for a 3-second gap between calls; a single search stays well within that.

## Google Scholar

Endpoint: `https://scholar.google.com/scholar?q=...&start=<n>&as_ylo=<year>`

Best coverage and the most generous citation counts. No API, no stable markup,
and aggressive bot detection.

| Element | Selector |
|---|---|
| Result block | `div.gs_ri` |
| Title and link | `h3.gs_rt a` |
| Author, venue, year line | `div.gs_a` |
| Snippet | `div.gs_rs` |
| Cited-by link | `div.gs_fl a` with text `Cited by N` |

Quirks:

- Paging is `start=0,10,20,...`; beyond roughly 40 results the CAPTCHA risk climbs sharply.
- Headless Chromium returns zero results. Headed works; verified 2026-08-29.
- `div.gs_a` is a single dash-separated string; the year is parsed positionally and is occasionally wrong.
- The `/citations?user=` endpoint triggers CAPTCHAs far sooner than search does. Avoid it.
- Scraping is against Google's terms. Keep volume low and treat this source as optional.

## ACM Digital Library

Search: `https://dl.acm.org/action/doSearch?AllField=<query>&pageSize=<n>`

Cloudflare blocks plain HTTP clients with a 403 challenge, so ACM is only
reachable through the Playwright profile. Institutional access shows as
"Nova Southeastern University" in the header.

The challenge also blocks headless Chromium, and blocks headed Chromium unless
`--disable-blink-features=AutomationControlled` is set. With that flag the
interstitial clears in roughly six seconds; `wait_past_challenge` polls for it.

| Element | Selector |
|---|---|
| Result block | `li.search__item` |
| Title and link | `h5.issue-item__title a` |
| Authors | `ul.rlist--inline.loa li a` (fallback: `a[href*="/profile/"]`) |
| Abstract | `.issue-item__abstract` |
| Venue | `.issue-item__detail a` |
| Citation count | `span.citation` and its descendants |

PDF pattern: `https://dl.acm.org/doi/pdf/<doi>`. Fetch it through the
Playwright request context so session cookies apply.

Quirks:

- Result links appear as `/doi/`, `/doi/abs/`, or `/doi/full/`; strip the prefix to recover the bare DOI.
- The author list is `ul.rlist--inline.loa`; the bare `ul.rlist--inline` also matches the result-item toolbar and injects "Highlights"/"AI Summary"/"Get Access" as authors. Author names always link to `/profile/` pages, which is the drift-proof fallback.
- Bare digits inside `.issue-item__detail span` include the publication year, so citation counts must be read only from `span.citation` markup.
- FAccT, CHI, and CSCW proceedings are often gold open access and fetchable without a session.
- The `AfterYear` parameter is honored, `BeforeYear` inconsistently.

## IEEE Xplore

Search: `https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=<query>`

Angular-rendered, so results need `wait_for_selector` rather than a raw HTML
parse. Institutional access shows as "Access provided by: Nova Southeastern
University".

| Element | Selector |
|---|---|
| Result block | `xpl-results-item` |
| Title and link | `h3 a` |
| Authors | `xpl-authors-name-list a` |
| Abstract | `.description` |

PDFs live behind a stamp URL (`/stamp/stamp.jsp?arnumber=<n>`) discovered from
the article page, usually inside an iframe.

Quirks:

- Component tag names change between Xplore releases; `.List-results-items` is the fallback selector.
- Year filtering uses `ranges=<from>_<to>_Year`.
- Citation counts are not reliably present in search markup, so IEEE records lean on OpenAlex for the citation term.

## The IEEE Metadata API is not a substitute

`developer.ieee.org` offers a free Xplore Metadata API. It returns abstracts
only, never full text, even with an institutional subscription. It adds nothing
over OpenAlex plus Crossref for this workflow.

## Coverage summary

| Source | Auth | Citations | Abstracts | Full text |
|---|---|---|---|---|
| OpenAlex | none | yes | usually | OA links only |
| Crossref | none | low counts | sometimes | no |
| arXiv | none | no | yes | yes, always OA |
| Google Scholar | none | yes, highest | snippets | links out |
| ACM DL | institutional | yes | yes | yes |
| IEEE Xplore | institutional | no | yes | yes |
