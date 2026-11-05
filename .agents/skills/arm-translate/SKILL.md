---
name: arm-translate
description: >
  Use when translating, completing, verifying, or inventorying the Arm
  technical-reference articles under docs/cortex/ of the melodypapa.github.io
  MkDocs site; when syncing a Cortex-M7 or Cortex-R52 Arm document (TRM,
  Armv7-M/Armv8-M architecture reference manual, SDEN errata) from the local
  `.private/ARM` mirror into a docs/cortex page; or when asked about coverage of
  a Cortex core chapter such as MPU, cache, memory system, programmers model,
  exception model, instruction set, or system address map; or when merging split
  chapter pages and registering a document glossary.
---

# Arm Document → Cortex Article Sync

Translate or complete the Chinese articles under `docs/cortex/` from the Arm
documents mirrored in `.private/ARM/`. Follow the steps in order; the
conventions live in `references/`, not in this file.

## Step 0 — Read the law of the land

There is no `STANDARD.md` for `docs/cortex/`. The law is the existing articles
plus `references/article-format.md`. Read that reference before writing, and
read at least one neighbouring article in the same `docs/cortex/<core>_processor/`
tree so the new page matches its tone and structure.

## Step 1 — Resolve the source document

Read `references/source-resolution.md`. Summary:

1. Primary source is the ima-parsed Markdown in `.private/ARM/<core>/`
   (`M7/`, `R52/`), paired with the original PDF of the same doc ID and
   revision. Use the `.md` for text, the `.pdf` for figures, and the `.pdf` to
   read the cell grid of a table the parse flattened.
2. Confirm the pairing from `.private/ARM/README.md` — it records the doc ID,
   revision, media size and which pairs are complete. Filenames do not always
   match between `.md` and `.pdf` (the M7 TRM PDF drops `_r1p2`; the SDEN PDF
   carries the long `cortex_m7_at610_and_...` name).
3. The `.md` files are read-only; never edit them. Never translate from the PDF
   text layer when a `.md` exists — the parse is the structural source.

## Step 2 — Map source → target article

Read `references/mapping.md` for the article ↔ source-chapter table. The
evidence is the figure/table number in the source (`Figure8-*` ⇒ chapter 8,
`TableB3-*` ⇒ Armv7-M ARM appendix B3); when the numbering does not prove it,
match section headings before writing.

A source chapter becomes one article at
`docs/cortex/<core>_processor/<topic>/index.md` (`m7_processor/`,
`r52p_processor/`). Propose the directory name to the user when a topic
straddles two chapters or could be split.

## Step 3 — Gap analysis before any writing
Compare the article's `## ` headings against the source chapter's section list:

- **Missing article** → plan a full translation of that chapter.
- **Partial / stub** → plan in-place completion; insert translations where the
  source has them, in source order, and renumber the sections that follow.
- **Covered elsewhere** → before writing off a section as "another article has
  it", confirm the sibling page actually carries it and record the mapping.
  Overview, modes and monitor sections stay on the chapter page even when the
  sibling page covers the deeper topic.
- **Complete** → report alignment; check for sections the article dropped.

The droppable set is the document chrome only: cover page, proprietary notice,
contents, document history, feedback and index. Everything else that carries
content — including notes, register descriptions and "Related references" —
translates. For a source chapter longer than ~1500 lines, present the plan and
get confirmation before translating.

Gap analysis is text-only: compare Markdown headings, never open figures.
Count the chapter's figures and tables from the source heading/text before
writing and record the count; if the requester's description of the chapter
contradicts the source (wrong length, "no figures", "one table"), say so and
follow the source.

## Step 4 — Create the work todo list

One run consumes one article. Emit an explicit checklist before writing:
chapter sections in source order, figures to crop, tables to rebuild as text
(GFM by default; HTML only for qualified complex structures), register entries,
nav registration, landing-page update, verification commands.
If the user names an article with no target directory, create the directory
first.

## Step 5 — Translate in place

- **The main session translates — never a subagent**, sequentially, regardless
  of chapter length. Read-only subagents may do censuses or verification.
- Faithful translation of Arm's own wording, not a summary. Keep technical
  identifiers, register names, bit-field names and instruction syntax
  untranslated; bold the English term on first mention, Chinese gloss in
  parentheses.
- Renumber the source chapter to `## 1.` and mirror its relative structure
  (`### 1.1.`, `#### 1.1.1.`). Numbering restarts at 1 in every article.
- Never write `# ` in the body (front-matter `title` is the only h1).
- Keep code and instruction snippets in fenced blocks tagged `arm`
  (`MCR p15, 0, <Rt>, c6, CRm, op2`), verbatim from the source.
- Source notes render as `**注意：**` paragraphs.
- Register subsections keep the source's order: name, description,
  `**使用限制**`, access table (`| EL0 | EL1 | EL2 |`), field table.
- Tables: every table translates to text. GFM is the default (header row +
  `| --- |`), including bit-field, access-rights, encoding and register-summary
  tables. Never crop a table as an image, merged cells included. In GFM tables,
  expand a merged cell by repeating the spanning value in each row of the block,
  so every row reads on its own; leave a cell blank only where the blank is
  unambiguous. A table the parse flattened is rebuilt from the PDF layout, still
  as text.
  A narrow HTML exception applies when GFM cannot carry the structure (block
  content in cells, an ambiguous multi-tier header, or meaningful spanning
  cells) — see `references/article-format.md` §Tables for the exhaustive
  criteria and the raw-HTML inline-markup requirement.
- Figures: every content figure in the chapter embeds, cropped and referenced
  without caption text (`![Figure8-2](Figure8-2.png)`).

**Precedence.** The conventions in `references/` are the default. When the
requester waives one — keep source numbering, skip figures, summarise tables,
"add nav later", "I'll check the build" — say what the waiver costs and take it
only as an explicit instruction; never silently drop a figure, a table row, a
register, the nav entry or the landing link, and never copy a section from a
neighbouring article to fill a gap.

## Step 6 — Produce the figures

Read `references/article-format.md` for naming. Figures only: crop from the
source PDF with PyMuPDF into the article directory (`Figure<chapter>-<n>.png`),
keeping source numbering so the figure can be traced back. Figures that are
bit-field bars, block diagrams or timing diagrams stay images; anything with
rows and columns is a table and goes through Step 5 as text.

Legacy directories mix `Figure4_77.png` and `FigureA3-1.png` — never rename
existing files, only keep new ones consistent. A legacy `Table<chapter>-<n>.png`
in a directory you are already editing is converted to a text table (GFM by
default, HTML when the structure qualifies) in the same run: delete the PNG and
its reference once the translated table is verified against the source, and only
if nothing else links to it.

## Step 7 — Register the page

- `mkdocs.yml`: add the page under the `ARM Cortex` group of the right core
  (`Cortex-M7 内核` / `Cortex-R52+ 内核`).
- `docs/cortex/index.md`: add the numbered link under the matching core section.
- Insert both entries at the page's **source chapter position** — the nav group
  and the landing list are ordered by chapter number (ch1 → ch14 → appendix),
  not by arrival time. Never append a new page at the end of the group; a
  concept article takes the position of the closest chapter it supports. See
  `references/article-format.md`.
- **One source chapter = one article.** When a chapter is currently split across
  two directories (the PSR/exception split under TRM ch2, the TRM ch6 MPU and
  the Armv7-M PMSAv7 extract), merge them into a single `index.md`: keep the
  first article's directory and title, append the second article's sections
  with their numbers shifted by the first article's last chapter number, move
  its images with `git mv`, delete the retired directory, and add
  `redirect_maps` entries in `mkdocs.yml` for every retired `…/index.md`.
  Internal `#anchor` links inside moved sections must be renumbered with the
  new heading number. Fix any reference to the old paths in the article tree and
  in `docs/cortex/sync-todo/`.
- A merged chapter page must still be **chapter-complete**: the source's
  overview, mode/state and monitor sections (TRM 2.1, 2.2, 2.5) belong on the
  chapter page even when the chapter also points at sibling pages for other
  topics (2.3 instruction set → `instruction_set`, 2.4 address map →
  `system_address_map`). Insert them at their source position and renumber
  every later section, or the page silently drops the chapter's own front
  matter.
- The document glossary is its own page: `docs/cortex/<core>_processor/glossary/index.md`,
  `title: "术语表（Glossary）"`, no local word list, one link to the Arm
  Glossary, registered last in the core group (appendix position).
- Concept articles that cite external sources stay outside this skill.

## Step 8 — Verify (two-phase gate)

Phase A (mechanical, all must pass):

```
/tmp/mkdocs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/mkdocs-check
python3 .agents/skills/autosar-translate/scripts/check_indexes.py
python3 .agents/skills/autosar-translate/scripts/check_heading_lang.py <article>
```

Plus: every `![](...)` target exists in the article directory; no `![Table…]`
table image left in the article (each table is either a GFM table with a header
row and `| --- |`, or an HTML `<table>` with `<thead>`/`<th>` headers); HTML
table cells must contain no unprocessed Markdown (`**…**`, `[…](…)`); no `# `
in the body; every `## ` heading is Chinese with the source number; no
untranslated English paragraph left behind.

Phase B (fidelity): walk the chapter section by section — each source section
has a translation, each register/figure/table is present, row sets and bit
ranges match the source, and deprecated Chinese-only wording is not used where
the source is a proper noun. Also check **numbering continuity**: every numbered
heading has its predecessor (`### 7.10` implies `### 7.9`, `## 3.` implies
`## 2.`); a jump is a defect even when the text reads fine.

Report both phases with concrete evidence; do not claim completion without the
build output. Run the gate even when the requester says they will verify it
themselves — Phase A is the author's responsibility, not a hand-off.

## Step 9 — Repository workflow

Feature branch (`feature/cortex-<core>-<topic>`), English issue and PR text,
`docs:` commit with `Closes #N`, strict build before commit, no co-work
attribution. Merge through a PR; `master` is protected.

## Common mistakes

- Renumbering the article to the source chapter number (must restart at 1).
- Cropping a table as `Table<ch>-<n>.png` because the cells are merged, or
  leaving a legacy table image in place while editing the article — tables are
  text (GFM with spans expanded row by row, or HTML for qualified complex
  structures).
- Using an HTML table for a plain grid GFM can carry, or leaving `**bold**` /
  Markdown links inside HTML cells — they render literally.
- Pasted PDF text with broken table cells or hyphen splits left unrepaired.
- Figures skipped "because the parse has no caption" — the figure still embeds.
- Translating the proprietary notice or document history.
- Adding the page without the nav entry (strict build passes, page is orphaned).
