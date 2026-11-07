# Source resolution — `private-docs/ARM`

The Arm corpus is a local mirror of the ima knowledge base export (2026-11-03).
It lives at the repo root in `private-docs/ARM/` (a private git submodule, outside the parent repo's content) and is read-only.

## Layout

| Directory | Documents |
| --- | --- |
| `M7/` | `DDI0489F_cortex_m7_trm_r1p2.md` + `DDI0489F_cortex_m7_trm.pdf` (Cortex-M7 TRM r1p2); `DDI0403E_e_armv7m_arm.md` + `.pdf` (Armv7-M ARM E.e); `cortex_m7_at610_at611_sden_1068427_v11_0_en.md` + `cortex_m7_at610_and_cortex_m7_with_fpu_at611_software_developer_errata_notice_sden_1068427_v11_0_en.pdf` (SDEN-1068427 v11.0) |
| `R52/` | `cortex_r52_trm_100026_0100_00_en.md` + `.pdf` (Cortex-R52 TRM r1p0); `DDI0553B_y_armv8m_arm.md` + `.pdf` (Armv8-M ARM B.y) |
| `README.md` | Doc ID, revision, media size, completeness status per file |

`README.md` is the record of truth for which pairs are complete; check it
before relying on a file, and never edit either the README or the sources.
Note that `.md` and `.pdf` names do not always match — the TRM PDF drops the
revision suffix and the SDEN PDF carries a long descriptive name.

## Selecting the source

1. **Topic → document**: TRM chapters describe one core's implementation
   (registers, interfaces, cache, MPU, address map). The architecture reference
   manual (Armv7-M for M7, Armv8-M for R52) describes architectural behaviour
   (exception model, memory model, PMSA, instruction set). A page may legitimately
   come from either — `references/mapping.md` records the observed source per
   existing article.
2. **Text**: the `.md` parse. Its shape:
   - front matter is the cover, proprietary notice, release history and contents;
   - chapters are flattened (`# Chapter 8`, `## 8.1.2 …`), some parser
     artefacts split a heading into two `##` lines;
   - figures appear as `![...](2/<hash>/tmp_zip_img/<uuid>.png)` — the path
     does not resolve inside `private-docs/ARM`, it is a parse artefact;
   - merged table cells arrive as HTML `<table>` markup (sometimes inside the
     image alt text): read it as the cell grid, then rebuild the table as text
     (GFM by default; HTML only when the structure qualifies) — the parse's
     `<table>` is a source, not something to paste.
3. **Figures**: crop from the sibling `.pdf` (PyMuPDF `fitz` is installed),
   expanding the clip by a margin (~4% of the larger dimension per side, min
   6pt — never flush with the content; see `article-format.md`).
   Do not screenshot or re-create a diagram by hand. Tables are never cropped —
   when the parse flattened one, read the cell grid from the PDF to rebuild it
   as text (see `article-format.md`).

## Verify the pairing

- Figure/table numbers **inside the source text** are the fastest proof:
  a caption `Table 8-1` sits in chapter 8 of the same document. A file name is
  not proof of the same thing (see the next bullet).
- Legacy article images can carry numbers from an older revision that no longer
  match the current PDF (the MPU page's `Table9-*` files illustrate `Table 8-*`,
  and the memory-system page's `Figure8_*` files illustrate chapter 7).
  Confirm by the figure/table caption text in the `.md`, not by a file name.
- When the parse lost the number, match the section heading against the
  chapter's section list before translating.
- If two documents carry the same section (TRM and ARM both describe the PSR),
  prefer the TRM for implementation details and the ARM for architectural
  rules, and state the choice in the queue note or PR text.

## Constraints

- Do not translate from the PDF text layer when a `.md` exists.
- The PDF is also the source for revision-sensitive content; record the
  revision (`r1p0`, `r1p2`, `B.y`, `E.e`) in the PR text when it matters.
- `private-docs/` is a private submodule: never commit a source file or a PDF to the parent repo; its own content is pushed to `melodypapa/private-docs`.
