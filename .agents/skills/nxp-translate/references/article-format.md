# NXP article format

Derived from the translated pages under `docs/nxp/s32g2/` and the
`arm-translate` conventions. There is **no `STANDARD.md` for `docs/nxp/`**: this
file plus the neighbouring article (read for syntax) are the law.

## Reading the neighbouring article (syntax only)

Read one `docs/nxp/s32g2/<topic>/index.md` before writing so the new page matches
its front matter, numbering and figure filenames. Use it **for syntax only**.
The legacy S32G2 pages are partial translations; do **not** copy their defects:

- empty section bodies (`## 3. RTC 寄存器说明` with nothing under it);
- `![Table_1](Table_1.png)` — a table cropped as an image;
- whole register-description chapters dropped;
- untranslated English paragraphs left in the body.

A faithful chapter translation has none of these.

## Front matter

Only `title`. Chinese title with the English term bolded in half-width
parentheses, separated by a space:

```yaml
---
title: "周期性中断定时器 (**PIT**)"
---
```

Chapters whose title has no acronym use Chinese only
(`"存储器映射（Memory Map）"` is also acceptable when the English term is a
proper term). Never add `spec:`, `release:` or tags — that convention belongs to
`docs/autosar/`. Never add a table of contents, document history, proprietary
notice or footer banner to the body.

## Body structure and numbering

- One or two intro sentences mirroring the chapter's opening, then the
  translated sections in **source order**. Do not invent overview or summary
  sections; keep the source's own overview section on the chapter page.
- **Never write `# ` in the body** — the front-matter `title` is the only h1.
- **Numbering restarts at 1 for every article.** Drop the chapter number, keep
  the remaining components, and set heading level = (number of remaining
  numeric components) + 1:

  | Source | Article |
  | --- | --- |
  | `45.1 Chip-specific RTC information` | `## 1. 芯片特定的 RTC 信息` |
  | `45.1.1 RTC clocking` | `### 1.1. RTC 时钟` |
  | `31.3.1.1 End-of-line programming` | `#### 3.1.1. End-of-line 编程` |
  | `44.4.3.2 Status And Control (SC)` | `#### 4.3.2. 状态与控制（SC）` |

  `scripts/extract_chapter.py`'s `heading_label()` computes this. Keep the
  relative structure; numbering is contiguous — a jump (`## 3.` with no `## 2.`,
  `### 7.10` with no `### 7.9`) is a defect, not a style choice.
- **Clamp at `######`.** The S32G3 RM outline reaches level 10 (103 entries
  deeper than h6, e.g. `78.8.2.3.2.3.1.3.1 Lock`). For a source level whose
  article level would exceed 6, do **not** write `#######`. Render the full
  number and title as a bold paragraph instead:

  ```markdown
  **8.2.3.2.3.1.3.1. 锁定（Lock）**
  ```

  It still carries the number, still translates, and still counts in the gap
  analysis. Deep levels are common in register and debug chapters.
- Update any internal `#anchor` links when renumbering.

## Wording and markup

- Faithful translation of NXP's wording, not a summary. Keep technical
  identifiers, register names, field names, instruction/register syntax and hex
  values untranslated: `PIT_0`, `MCR[MDIS]`, `CR[TEN]`, `4400_C000h`,
  `0000_0000h`, `位 [5:3]`, `0h`.
- Bold the English term on first mention with a Chinese gloss in parentheses:
  `自由运行计数器（**free-running counter**）`; acronyms and register names stay
  bold (`**PIT**`, `**SC**`). Later mentions may drop the parentheses.
- Numbers and encodings as printed. Repair the PDF text layer's underscore
  splits (`PIT 0 _` → `PIT_0`) before writing.
- Lists mirror the source's bullets and numbering. Source `NOTE` → `**注意：**`,
  `CAUTION` → `**警告：**`, followed by the translated body.
- No `**说明**:` + `C` blocks — that is the AUTOSAR API convention.

## Tables

- **Every table is text.** GFM is the default: a header row and `| --- |`
  separator, translated cell by cell. Tables are **never** cropped as images —
  the one legacy `Table_1.png` in `docs/nxp/s32g2/system_timer_module/` is a
  defect, not a precedent.
- A table numbered in the source (`Table 279.`) carries its number in the
  paragraph that introduces it, not in a caption line and not in a filename.
- Tables split across pages (`Table continued...` / `Table continues...`) are
  **one** table: stitch the data rows, drop the repeated header, and keep the
  whole grid together.
- In GFM tables, merged cells are expanded, not mirrored: repeat the spanning
  value in each row of the block so every row reads on its own. Multi-tier
  headers flatten into one header row naming each column.
- **HTML exception (narrow, exhaustive).** A raw `<table>` is allowed only when
  GFM cannot carry the structure: cells with block content (lists, code blocks,
  multiple paragraphs), a multi-tier header whose flattened form is ambiguous,
  or merged cells whose spanning semantics carry meaning. A plain wide grid
  stays GFM. HTML tables use `<table>/<thead>/<tbody>`, `<th scope="col">`, real
  `rowspan`/`colspan`, and **raw HTML inline markup** (`<strong>`, `<code>`,
  `<a href>`) — Markdown is not parsed inside HTML cells, so `**bold**` and
  `[text](url)` would render literally.

## Figures

- Every content figure of the chapter embeds where the source has it:
  `![Figure_256](Figure_256.png)`. No caption text; the alt text is the source
  figure number. Keep the source's **global** number — do not renumber per
  chapter.
- The PNG sits in the article directory next to `index.md`; no shared `images/`
  tree. Crop from the PDF with PyMuPDF at ≥ 2× zoom (see
  `references/source-resolution.md`). Never screenshot or redraw by hand.
- Bit-field bars, block diagrams and timing diagrams stay images. A register's
  unnumbered bit-field `Diagram` is also a figure; name it
  `Diagram_<slug>.png` where `<slug>` is the register name lower_snake_cased
  (`Diagram_sc.png`, `Diagram_tctrl0_tctrl6.png`). Add a numeric suffix on a
  name collision (`Diagram_sc_2.png`). Never name a figure `Table_<n>.png`.
- Anything with rows and columns is a table, not a figure.

## Register subsections

Keep the source skeleton in source order:

1. Register name and offset (`**SC** 偏移：**0h**`).
2. The `Function` prose.
3. The `Diagram` bit-field bar as a cropped figure.
4. The `Fields` table (`Field | Function`, with bit ranges).

The memory-map table (`Offset | Register | Width | Access | Reset value`) heads
the register-description section. Access values (`RW`, `RO`), bit ranges, reset
values and offsets match the source exactly — a dropped row is a defect.

## Landing pages and navigation

- One chapter = one article directory:
  `docs/nxp/s32g3/chNN_<slug>/index.md` (`ch03_memory_map`,
  `ch43_periodic_interrupt_timer_pit`). Never split a chapter across files.
- `mkdocs.yml`, group `NXP` → `S32G3:` — add
  `- "<中文标题>": nxp/s32g3/chNN_<slug>/index.md` at the chapter's **source
  position** (nav is ordered by chapter number, not arrival time). Every page
  must be registered or `--strict` fails.
- `docs/nxp/s32g3/index.md` is the section landing, registered as the unlabeled
  first entry of the `S32G3:` group (`navigation.indexes`). Front-matter title,
  one intro sentence, `## 文章` link list grouped by the 11 source group
  headers, then `## 相关内容`.
- `docs/nxp/index.md`: add a `## S32G3` link list under the existing `## S32G2`.
- `docs/index.md`: refresh the NXP tab description when the S32G3 pages land.

## Quality rules

- No untranslated English paragraph in the body; proper nouns and quoted
  standard wording are the only exceptions.
- No placeholder text, no `TODO`, no empty section bodies.
- Row sets, bit ranges, register offsets and reset values match the source.
- No `![Table…]` image, no `# ` in the body, every `![](...)` target exists in
  the article directory.
- The WeChat QR footer, where present, uses `<section id="wechat">` + `<h4>`,
  never a markdown heading.
