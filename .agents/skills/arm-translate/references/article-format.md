# Cortex article format

Derived from the translated pages under `docs/cortex/`. Match the neighbouring
article in the same tree; this file records the rules that hold across them.

## Front matter

Only `title`, quoting the Chinese title with the English term in full-width
parentheses when the source chapter title is a proper term:

```yaml
---
title: "内存保护单元（Memory Protection Unit）"
---
```

Short implementation chapters may use Chinese only (`"Cortex-M7 程序状态寄存器"`).
Never add `spec:`, `release:` or tags — that convention belongs to `docs/autosar/`.

## Body structure

- One or two intro sentences mirroring the source chapter's opening
  ("本章介绍 **MPU**。"), then the translated sections.
- Chapter numbering **restarts at 1** for every article: `## 1. 关于 MPU`,
  `## 2. MPU 区域`, `### 2.1. …`, `#### 4.2.1. …`. The number reflects the
  source's relative structure, not the source's absolute chapter number.
- Never write `# ` in the body — the front-matter title is the only h1.
- Numbering is contiguous: every `## N.` and `### N.M.` has its predecessor. A
  jump (`## 3.` with no `## 2.`, or a `### 7.10` with no `### 7.9`) is a defect,
  not a style choice — fix it even when the page is otherwise complete.
- Preserve the source's section order and nesting; do not invent overview or
  summary sections. A source overview section is not invented content: keep it
  on the chapter page (TRM 2.1, 2.2, 2.5) even when a sibling page carries the
  deeper topic.
- No table of contents, no document history, no proprietary notice, no footer
  banner.

## Wording and markup

- Faithful translation of Arm's wording; technical identifiers stay in English.
- Bold the English term on first mention with a Chinese gloss in parentheses:
  `直写缓存（**Write-Through caching**）`; register names stay bold
  (`**PRBAR**`, `**SCTLR.M**`); later mentions may drop the parentheses.
- Numbers and encodings as in the source: `位 [5:3]`, `0x…`, `0b…`.
- Notes: `**注意：**` followed by the translated note body.
- Instruction and pseudo-code snippets go in fenced blocks, verbatim, tagged
  `ARM`; C snippets use `C`. Comments inside a listing translate; mnemonics and
  operands do not. (Legacy pages also use lowercase `arm`.)
- Register subsections keep the source skeleton: register name, purpose,
  `**使用限制**`, access table, then field table.

## Tables

- Every table is text, and GFM is the default: a Markdown table with a header
  row and `| --- |` separator, translated cell by cell. Tables are never
  cropped as images — merged cells included.
- **HTML exception (narrow).** A raw HTML `<table>` is allowed only when GFM
  cannot carry the structure without loss or unreadability: cells containing
  block content (lists, code blocks, multiple paragraphs), a multi-tier header
  whose flattened form is ambiguous, or merged cells whose spanning semantics
  carry meaning that repeating values would obscure. A plain row/column grid,
  however wide, stays GFM. These three cases are exhaustive; see the decision
  log below.
- HTML tables must use `<table>` with `<thead>`/`<tbody>`, `<th>` headers with
  `scope="col"` or `scope="row"`, and real `rowspan`/`colspan` for spans.
  Inline markup inside cells must be written as raw HTML (`<strong>`, `<code>`,
  `<a href="…">`) — Markdown is **not** parsed inside HTML table cells even
  with `md_in_html`, so `**bold**` and `[text](url)` would render literally.
  Never paste the source parse's `<table>` markup verbatim; write clean HTML.
- In GFM tables, merged cells are expanded, not mirrored: repeat the spanning
  value in each row of the block so every row reads on its own, e.g. three
  regions sharing one attribute each repeat `RW` instead of one `RW` cell
  spanning three rows.
- In GFM tables, multi-tier headers flatten into one header row that names each
  column (`| 位 | 名称 | 类型 | 复位值 | 描述 |`); the source's two-tier
  `位 / 名称` header becomes two columns.
- Access tables keep the source's three columns:
  `| EL0 | EL1 | EL2 |` with `-` / `RW` values.
- Bit-field bars (`Figure7-1`), block diagrams and timing diagrams are figures,
  not tables — they stay as cropped images.
- No visible `Table x-y:` caption line; the paragraph that introduces the table
  carries it. Legacy `Table<chapter>-<n>.png` images in older directories are
  converted to text tables (GFM by default, HTML when the structure qualifies)
  as those articles are touched.

## Figures

- Every content figure of the translated chapter embeds where the source has it:
  `![Figure8-2](Figure8-2.png)` — no caption text, alt text is the source
  figure number.
- The PNG sits in the same directory as `index.md`; no shared `images/` tree.
- Naming: `Figure<chapter>-<sequence>.png`, using the source document's own
  numbering (`Figure8-2`, `FigureB3-1` for an appendix). Legacy directories mix
  `Figure4_77.png`, `FigureA3-1.png` and now-unused `Table9-1.png` — never
  rename existing files.
- Crop from the sibling PDF with PyMuPDF at a resolution that keeps bitmap text
  legible (scale ≥ 2× page zoom).
- **Leave a margin when cropping (user decision 2026-11-07)** — never crop a
  figure flush to its content: expand the clip rect on all four sides by ~4% of
  the larger of (width, height), minimum 6pt, clamped to the page rect. The
  padding keeps cropped diagrams from rendering edge-to-edge (顶天立地) in the
  page. Equivalent post-processing: pad the PNG with a uniform white border of
  ~2% of its pixel width when the clip cannot be expanded (figure touching the
  page edge):

  ```python
  import fitz  # pymupdf
  page = doc[page_no]
  r = figure_bbox + (-m, -m, m, m)   # m = max(6, 0.04 * max(w, h))
  pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=r & page.rect)
  ```

  The same margin rule applies to any other figure-extraction flow (PPTX
  region crops, image truncation) — a saved figure carries visible whitespace
  around its content. **Converter-extracted PNGs are not exempt**: corpus
  artifacts (`image_*.png`) are typically flush — at review, measure the border
  whitespace of every embedded figure and replace any figure with less than
  ~1% margin by padding it in place (white border, ~2% of pixel width, min
  12px); never leave a flush figure in the article (user decision 2026-11-07).

## Landing pages and navigation

- `docs/cortex/<core>_processor/<topic>/index.md` — one directory per topic.
- One source chapter maps to exactly one article. Do not split a chapter across
  directories (two articles for ch2's PSR and exception model, a separate MPU
  page for ch6); merge the parts into one page, renumber the appended sections,
  and keep old URLs alive through `redirect_maps`.
- The document glossary goes in `docs/cortex/<core>_processor/glossary/index.md`
  with the `title: "术语表（Glossary）"`, the sentence that the manual keeps no
  local word list, and a single link to the Arm Glossary. It is registered last
  in the core group (appendix position).
- `mkdocs.yml`, group `ARM Cortex` → `Cortex-M7 内核` / `Cortex-R52+ 内核`: add
  `- "<中文标题>": cortex/<core>_processor/<topic>/index.md`.
- `docs/cortex/index.md`: numbered link under the matching core heading
  (`1. [程序员模型（Programmers Model）](r52p_processor/programmers_model/index.md)`).
- `docs/cortex/concept/` holds externally sourced explainers; they are not
  produced by this skill.

## Quality rules

- No untranslated English paragraph in the body; proper nouns and quoted
  standard wording are the only exceptions.
- No placeholder text, no `TODO`, no empty section bodies.
- Row sets, bit ranges and register addresses match the source exactly — a
  dropped row is a defect, not a style choice.

## Decision log

- 2026-11-05, issue #283 — Raw HTML `<table>` permitted as a narrow exception
  for structurally complex tables; GFM remains the default and the three
  qualification cases in §Tables are exhaustive. Lifted by user decision after
  verifying that Material styles a plain `<table>` identically to a GFM table
  (`.md-typeset table:not([class])`) but that `md_in_html` does not parse
  Markdown inside HTML cells. Supersedes the earlier unrestricted "every table
  is a GFM table" wording.
