# THESIS-TEMPLATE — structure of a run's thesis.md

`tools/render_thesis_docx.py` consumes this exact markdown subset to produce
the run's formal advisor-review Word document:

```bash
uv run tools/render_thesis_docx.py results/<run>/ \
    [--thesis thesis.md] [--out Problem-Statement-Literature-Review.docx] \
    [--author NAME] [--program TEXT] [--date TEXT] [--subtitle TEXT]
```

CLI flags override the metadata block; everything else comes from the file.

## Structural rules

1. **Title.** The file starts with a single H1 (`# ...`). It becomes the
   title page's title.
2. **Metadata block.** The first paragraph after the title carries bold
   `**Key:** value` pairs — `**Author:**`, `**Date:**`, `**Program:**`,
   `**Purpose:**`. Pairs may share a line separated by `·`, and values may
   wrap across lines. Author/Program/Date fill the title page (Program is
   split on `", "` into one line per component); Purpose renders as an italic
   note on the title page.
3. **Rules (`---`).** A horizontal rule closes the current topic scope and is
   otherwise not rendered. Place one between the metadata/intro material and
   the first topic, between topics, and before any trailing top-level `##`
   sections (otherwise those would attach to the last topic).
4. **Intro sections.** `## ...` sections before the first topic render as
   top-level headings with paragraphs and `- ` bullet lists.
5. **Topics.** Each `# Topic N — ...` H1 after the title is a topic and
   starts on a new page. Inside a topic:
   - A `**Proposed title:** *...*` paragraph directly under the H1.
   - `## The problem` → rendered as **Problem Statement**: double-spaced,
     first-line-indented paragraphs.
   - `## Evidence that this is a problem` → rendered as **Evidence That This
     Is a Problem**: a numbered list where each item is
     `N. **Bold lead** — rest of the claim:` followed by indented `> "..."`
     quote lines and a closing `> — Attribution` line (the attribution may
     wrap onto further `> ` lines). Quotes are re-wrapped in typographic
     quotation marks; keep the source quotation exact.
   - `## The experiment` → rendered as **Proposed Experiment**:
     `**Label.** text` paragraphs (bold lead, no first-line indent) and
     `- ` bullet lists.
   - `## Why this approach is viable` → rendered as **Why the Proposed
     Approach Is Viable**: same claim/quote/attribution shape as Evidence.
   - `## Assessment` → `- **Label:** text` bullets, rendered as bold-led
     labeled paragraphs rather than bullets.
   - Any other `## ...` heading renders generically (heading + paragraphs /
     bullets / numbered items / quotes) — sections are never dropped.
6. **Trailing sections.** After the final topic and a `---`:
   - `## Runner-up ...` (or similar) renders generically.
   - `## References` renders its paragraphs as body text and each `- ` bullet
     as a single-spaced, hanging-indent reference entry.
   - An optional closing paragraph after a final `---` (no heading) renders
     as body text.
7. **Inline markdown.** `**bold**`, `*italic*`, `[text](url)` → text only,
   `` `code` `` → plain text. Nothing else is interpreted; literal `**`, `#`,
   or `>` must not appear outside these constructs.
8. **Wrapping.** Bullet and numbered-item continuation lines are indented;
   paragraph continuation lines are flush left. Blank lines separate blocks.

## Skeleton

```markdown
# Dissertation Topic Candidates: <Run Theme>

**Author:** A. Student · **Date:** 2026-08-30
**Program:** Ph.D. in Computer Science, Nova Southeastern University
**Purpose:** One or two sentences on what this document distills and why.

---

## How these topics were selected

- **Corpus:** counts and stopping rule.
- **Verification:** how quotes/citations were checked.

---

# Topic 1 — Short Topic Name

**Proposed title:** *Full Dissertation Title in Italics*

## The problem

Paragraphs with **bold** and *italic* inline.

## Evidence that this is a problem

1. **Bold claim lead** — remainder of the claim:
   > "Exact verified quotation from the source paper."
   > — Author et al. (2026), p. 4 **[preprint]**

## The experiment

**Design.** Paragraph.

**Conditions:**
- C1: first condition
- C2: second condition

**Metrics.** Paragraph.

## Why this approach is viable

1. **Bold claim lead:**
   > "Supporting quotation."
   > — Author (2025), p. 9

## Assessment

- **Novelty:** ...
- **Falsifiability:** ...

---

## Runner-up and cross-cutting findings

Paragraphs and bullets.

## References

- Author, A., & Author, B. (2026). Title of the paper. *Venue*.
  https://doi.org/10.0000/xxxxx

---

*Optional closing/provenance note in italics.*
```
