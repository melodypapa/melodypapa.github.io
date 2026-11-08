---
name: nxp-translate
description: >
  Use when translating, completing, verifying or inventorying the Chinese NXP
  S32G3 articles under docs/nxp/s32g3/ of the melodypapa.github.io MkDocs site;
  when a chapter of the NXP S32G3 Reference Manual (S32G3RM) in
  reference-docs/nxp/ needs a one-chapter-one-file page; when asked about S32G3
  chapter coverage or a module chapter (PIT, FlexCAN, XRDC, MC_CGM, MC_ME,
  FCCU, ERM, EIM, Debug); or when the task involves NXP register tables,
  globally numbered figures, or cropping diagrams from an NXP manual PDF.
---

# NXP Reference Manual → Chapter Article Sync

Translate or complete the Chinese articles under `docs/nxp/s32g3/` from the NXP
S32G3 Reference Manual mirrored in `reference-docs/nxp/`. **One numbered chapter
= one markdown file.** Follow the steps in order; the conventions live in
`references/`, not in this file.

The source is a **PDF with no parsed Markdown mirror**. Everything structural
comes from the PDF outline; everything textual comes from the PDF. Unlike
`arm-translate`, there is no `.md` parse to lean on.

## Step 0 — Read the law of the land

There is no `STANDARD.md` for `docs/nxp/`. Read
`references/article-format.md`, `references/source-resolution.md` and
`references/chapter-map.md` before writing, and read at least one neighbouring
`docs/nxp/s32g2/<topic>/index.md`.

Read the S32G2 page **for syntax only**: front matter, numbering, figure
filenames. The legacy pages are partial translations and carry defects — do not
copy them:

- empty section bodies (`## 3. RTC 寄存器说明` with nothing under it);
- `![Table_1](Table_1.png)` — a table cropped as an image;
- whole register-description sections dropped;
- untranslated English paragraphs.

A faithful chapter translation has none of these. When a neighbouring page and
`references/article-format.md` disagree, the reference wins.

## Step 1 — Resolve the source document

Read `references/source-resolution.md`. Summary:

1. Primary source is
   `reference-docs/nxp/s32g3/reference_manual/RMS32G3.pdf`
   (`S32G3RM Rev. 5, 2025-09-17`, 5101 pages). It is Git-LFS tracked and
   **read-only**. Confirm it is materialised (not a pointer) with `file` /
   `git lfs pull` before relying on it.
2. Use system `python3` with PyMuPDF (`pymupdf` is **not** in
   `requirements.txt`, so the mkdocs venv does not have it).
3. `doc.get_toc()` is the structural source: 81 contiguous numbered chapters,
   section tree down to level 10, chapter start pages. Page text is the source
   for wording. Never re-derive chapter boundaries from a page-text search.
4. Run `scripts/extract_chapter.py <pdf> <chapter> --out /tmp/chNN.txt` for the
   chapter dump (section tree, chrome-stripped page text, table grids, caption
   index). `--sections-only` for a fast outline-only census.
5. Record the revision (`S32G3RM Rev. 5, 2025-09-17`) in the PR text. NXP
   articles carry no `spec:` / `release:` front matter.

Never edit a PDF, never add a `.md` parse to `reference-docs/`, never commit a
PDF as site content.

## Step 2 — Map chapter → target article

Read `references/chapter-map.md`. A source chapter becomes exactly one article:

```
docs/nxp/s32g3/chNN_<slug>/index.md
```

e.g. chapter 43 → `docs/nxp/s32g3/ch43_periodic_interrupt_timer_pit/index.md`.
Use the **explicit table**, not a filename invented from the title. Zero-padded
`chNN`; slug rule is in the map. One run consumes one chapter. Never split a
chapter across files, never merge two chapters into one file, and never append
a new page at the end of its nav group.

Chapters 1–4 are level-1 outline entries; chapters 5–81 are level-2 under 11
unnumbered group headers. Group headers, `Contents`, appendices A/B and
`Legal information` are chrome, not chapters.

## Step 3 — Gap analysis before any writing

Compare the article's headings against the chapter's outline section tree:

- **Missing article** → plan a full translation of that chapter.
- **Partial / stub** → plan in-place completion; insert translations where the
  source has them, in source order, and renumber the sections that follow.
- **Covered elsewhere** → confirm the sibling page actually carries it before
  writing a section off; record the mapping.
- **Complete** → report alignment; check for sections the article dropped.

Compare **all heading levels** (`##` through `######`) plus the bold-paragraph
labels used for outline levels deeper than h6. The outline reaches level 10 —
register and debug chapters have dozens of deep sections; comparing only `##`
silently drops them. Do not open figures during gap analysis; it is text-only.

Count the chapter's figures and tables from the caption index in the dump and
record the count. If the requester's description contradicts the source (wrong
length, "no figures", "one table"), say so and follow the source.

The droppable set is document chrome only: cover, contents, revision/release
notes, legal notice, appendices A/B. Everything else that carries content —
including notes, register descriptions, memory maps and field tables —
translates. For a chapter whose dump exceeds ~1500 lines (ch67, ch76, ch37,
ch25 and others do), present the plan and get confirmation before translating.

## Step 4 — Create the work todo list

Emit an explicit checklist before writing: chapter sections in source order,
figures to crop, tables to rebuild as text (GFM by default; HTML only for
qualified complex structures), register entries, nav registration, landing-page
update, verification commands. If the target directory does not exist, create
it first.

81 full-chapter articles cannot land in one session. On the first run create the
persistent ledger described at the end of `references/chapter-map.md`
(`docs/nxp/s32g3/TODO.md`, `sync-todo/`), add it to `exclude_docs` in
`mkdocs.yml`, and record each chapter's status. **Resume rule:** take the first
unfinished row in chapter order; do not re-derive scope or re-ask decisions
already recorded in the row.

## Step 5 — Translate in place

- **The main session translates — never a subagent**, sequentially, regardless
  of chapter length. Read-only subagents may do censuses or verification.
- Faithful translation of NXP's own wording, not a summary. Translate the full
  chapter: chip-specific information, overview, memory map, register
  descriptions, functional description, initialization and application
  information.
- Keep technical identifiers, register names, bit-field names and hex values
  untranslated; bold the English term on first mention, Chinese gloss in
  parentheses. Repair the PDF text layer's underscore splits (`PIT 0 _` →
  `PIT_0`) before writing.
- **Numbering:** drop the chapter number, keep the remaining components, heading
  level = (number of remaining numeric components) + 1. `45.1` → `## 1.`,
  `45.1.1` → `### 1.1.`, `44.4.3.2` → `#### 4.3.2.`. **Clamp at `######`** —
  deeper outline levels become a bold paragraph `**8.2.3.2.3.1.3.1. 锁定**`,
  never `#######`. Numbering is contiguous.
- **Never write `# ` in the body** (front-matter `title` is the only h1).
- Source `NOTE` → `**注意：**`, `CAUTION` → `**警告：**`.
- **Tables: every table becomes text.** GFM by default (header row + `| --- |`),
  including memory maps, field tables and register summaries. Never crop a table
  as an image. Expand merged cells by repeating the spanning value in each row
  of the block. Stitch tables split across pages (`Table continued...` /
  `Table continues...`) into one grid, dropping the repeated header. A table the
  detector flattened is rebuilt from the PDF layout, still as text. The narrow
  HTML exception (block content in cells, ambiguous multi-tier header,
  meaningful spanning cells) is in `references/article-format.md` §Tables.
- Register subsections keep the source order: name + offset, `Function` prose,
  `Diagram` bit-field bar, `Fields` table. Bit ranges, reset values and offsets
  match the source exactly.
- Figures: every content figure embeds, cropped and referenced without caption
  text (`![Figure_256](Figure_256.png)`).

**Precedence.** The conventions in `references/` are the default. When the
requester waives one — keep source numbering, skip figures, summarise tables,
"add nav later", "I'll check the build" — say what the waiver costs and take it
only as an explicit instruction; never silently drop a figure, a table row, a
register, an empty section, the nav entry or the landing link, and never copy a
section from a neighbouring article to fill a gap.

## Step 6 — Produce the figures

Read `references/article-format.md` for naming. Figures only: crop from the
source PDF with PyMuPDF into the article directory, keeping the source's
**global** figure number (`Figure_256.png`, `Figure_260.png`) so the figure can
be traced back. Figures are vector drawings — render a clip rect at ≥ 2× zoom
from `get_drawings()` bboxes, do not extract embedded images. Bit-field bars,
block diagrams and timing diagrams stay images; anything with rows and columns
is a table.

Unnumbered register `Diagram` bit-field bars use `Diagram_<slug>.png`
(`Diagram_sc.png`), with a numeric suffix on collision. Never name a figure
`Table_<n>.png`. Legacy `Table_1.png` in a directory you are already editing is
converted to a text table in the same run: delete the PNG and its reference once
the translated table is verified against the source, and only if nothing else
links to it.

## Step 7 — Register the page

- `mkdocs.yml`: add a `S32G3:` subgroup under `NXP:`, with the section landing
  `nxp/s32g3/index.md` as the **unlabeled first entry** (`navigation.indexes`),
  then `- "<中文标题>": nxp/s32g3/chNN_<slug>/index.md` at the chapter's source
  position. The nav group is ordered by chapter number, not arrival time.
- `docs/nxp/s32g3/index.md`: front matter, one intro sentence, `## 文章` link
  list grouped by the 11 source group headers, then `## 相关内容`.
- `docs/nxp/index.md`: add a `## S32G3` link list under the existing `## S32G2`.
- `docs/index.md`: refresh the NXP tab description when the S32G3 pages land.
- Every page must be registered or `--strict` fails. A strict build passing
  with an unregistered page means the page is orphaned.

**Offline / output-dir mode.** When the requester asks for output to a directory,
for an inventory, or explicitly says "don't modify the repo", produce only the
articles/dumps there and **skip Steps 7–9**. Evals use this mode. Never claim
the site was updated when it was not.

## Step 8 — Verify (two-phase gate)

Phase A (mechanical, all must pass):

```
/tmp/mkdocs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/mkdocs-check
python3 .agents/skills/autosar-translate/scripts/check_indexes.py
python3 .agents/skills/autosar-translate/scripts/check_heading_lang.py <article>
```

Plus: every `![](...)` target exists in the article directory; no `![Table…]`
image left; no `# ` in the body; every `## ` heading is Chinese with the source
number; numbering continuity at every level (`### 7.10` implies `### 7.9`,
`## 3.` implies `## 2.`); no untranslated English paragraph; no empty section
body; and a **file → nav orphan check** for all `docs/nxp/s32g3/ch*/index.md`
pages (strict build only checks nav → file, not the reverse).
`check_heading_lang.py` is AUTOSAR-tuned and blind to bold-paragraph deep
labels, so it is a tripwire, not the whole check.

Phase B (fidelity): walk the chapter section by section — each outline section
has a translation, each register/figure/table is present, row sets, bit ranges,
register offsets and reset values match the source, and deprecated Chinese-only
wording is not used where the source is a proper noun.

Report both phases with concrete evidence; do not claim completion without the
build output. Run the gate even when the requester says they will verify it
themselves — Phase A is the author's responsibility, not a hand-off.

## Step 9 — Repository workflow

Feature branch (`feature/nxp-s32g3-<topic>`), English issue and PR text,
`docs:` commit with `Closes #N`, strict build before commit, no co-work
attribution (never add `Co-Authored-By:` / "Generated with …" footers or any
mention of the agent/session). PR body: lead with a summary, group changes per
area (article / skill+script / other), end with a verification list including
the strict-build result. Merge through a PR; `master` is protected. A PR that
creates or changes the skill itself is `feat:`, not `docs:`.

## Common mistakes

- Inventing a filename from the chapter title instead of using
  `references/chapter-map.md`, or omitting the `chNN_` prefix.
- Keeping the source chapter number (`## 43.1.`) instead of restarting at 1.
- Writing `#######` for an outline level deeper than h6 instead of a bold
  paragraph.
- Cropping a table as `Table_<n>.png`, or leaving a legacy table image in
  place while editing the article — tables are text.
- Pasting PDF text with split identifiers (`PIT 0 _`, `0000 0000h _`) or broken
  table cells unrepaired.
- Treating the S32G2 stub pages as the standard and leaving empty sections or
  dropping register descriptions.
- Using Arm conventions: `Figure<ch>-<n>.png`, chapter-scoped table numbers,
  `docs/cortex/` targets, `spec:` front matter, or cropping register `Diagram`
  bars as tables.
- Translating the cover, contents, release notes or legal notice.
- Adding the page without the nav entry, or adding it at the end of the group
  instead of its chapter position.
- Claiming the site was updated in offline mode.

## Red flags — stop and start over

- "One chapter is small, I'll skip the outline" — the outline is structural.
- "I'll summarise the register tables" — a dropped row is a defect.
- "The S32G2 pages do it this way" — they are partial stubs.
- "Tables are easier as images" — never.
- "I'll check the build later" — Phase A is the author's job.
- "This is different because it's an NXP doc" — it is exactly what this skill
  is for.
