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
- Preserve the source's section order and nesting; do not invent overview or
  summary sections.
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

- Every table is text: a GFM table with a header row and `| --- |` separator,
  translated cell by cell. Tables are never cropped as images — merged cells
  included.
- Merged cells are expanded, not mirrored: repeat the spanning value in each
  row of the block so every row reads on its own, e.g. three regions sharing
  one attribute each repeat `RW` instead of one `RW` cell spanning three rows.
- Multi-tier headers flatten into one header row that names each column
  (`| 位 | 名称 | 类型 | 复位值 | 描述 |`); the source's two-tier `位 / 名称`
  header becomes two columns.
- Access tables keep the source's three columns:
  `| EL0 | EL1 | EL2 |` with `-` / `RW` values.
- Bit-field bars (`Figure7-1`), block diagrams and timing diagrams are figures,
  not tables — they stay as cropped images.
- No visible `Table x-y:` caption line; the paragraph that introduces the table
  carries it. Legacy `Table<chapter>-<n>.png` images in older directories are
  converted to GFM tables as those articles are touched.

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

## Landing pages and navigation

- `docs/cortex/<core>_processor/<topic>/index.md` — one directory per topic.
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
