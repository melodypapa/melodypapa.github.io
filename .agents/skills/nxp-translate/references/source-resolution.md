# Source resolution — `reference-docs/nxp`

The NXP corpus is a local mirror of vendor reference manuals. It lives at the
repo root under `reference-docs/nxp/<chip>/reference_manual/` and is **read-only**.

Unlike the Arm corpus (`reference-docs/arm/`, which ships ima-parsed `.md`
files), **NXP documents have no parsed Markdown mirror**. The PDF is the sole
source for both text and figures. Never look for a `.md` beside it, and never
create one from the PDF text layer for the corpus — the dump produced by
`scripts/extract_chapter.py` is a per-run working file, not a source.

## Corpus

| Path | Document |
| --- | --- |
| `reference-docs/nxp/s32g3/reference_manual/RMS32G3.pdf` | S32G3 Reference Manual, `S32G3RM` Rev. 5, 2025-09-17, 5101 pages |

`.gitattributes` tracks `reference-docs/**/*.pdf` through Git LFS. A freshly
cloned repo may therefore hold a ~130-byte LFS **pointer** instead of the 28 MB
PDF. Before relying on the file, confirm it is materialised:

```bash
file reference-docs/nxp/s32g3/reference_manual/RMS32G3.pdf   # must say "PDF document"
git lfs pull                                                 # if it is a pointer
```

`scripts/extract_chapter.py` exits 2 when the file is missing or is a pointer.

**Interpreter.** PyMuPDF (`import pymupdf`, `fitz`) is required. It is installed
in the system `python3` but is **not** in the repo's `requirements.txt` — the
mkdocs venv does not have it. Run the helper with system `python3` (or
`pip install pymupdf` into the venv). Do not add `pymupdf` to
`requirements.txt`: CI builds never read the corpus.

## The outline is the structural source

`doc.get_toc()` gives 5334 entries at levels **1–10**. It is the authority for
chapter boundaries and the section tree; page text is the authority for wording.

- Numbered chapters are exactly **81**, contiguous 1–81. Detect them as outline
  entries at **level ≤ 2** whose title matches `^(\d+)\s+`.
  - Chapters **1–4** are level-1 entries.
  - Chapters **5–81** are level-2 entries nested under 11 unnumbered level-1
    **group headers** (`Chapter 5-23: System Modules`, `Chapter 24-28:
    Clocking`, …). The `Debug` header lacks the `Chapter NN-NN:` prefix and
    shares page 4924 with `78 Debug`; it is still a group header, not a chapter.
- Group headers, `Contents`, `A General Changes` (p5083), `B Release notes`
  (p5084) and `Legal information` (p5098) are document chrome.
- Chapter page range = outline start page → (next chapter's start − 1). Chapter
  81 ends at p5082, before appendix A. `parse_chapters()` asserts 81 contiguous
  chapters — a changed revision must be re-checked, not silently consumed.
- Section headings are chapter-scoped (`44.1`, `44.1.1`, `44.4.3.2`). The
  outline goes down to level 10; `references/article-format.md` clamps those
  deep levels to h6.

Use the helper instead of re-deriving any of this:

```bash
python3 .agents/skills/nxp-translate/scripts/extract_chapter.py \
  reference-docs/nxp/s32g3/reference_manual/RMS32G3.pdf 43 --out /tmp/ch43.txt
python3 .agents/skills/nxp-translate/scripts/extract_chapter.py <pdf> 43 --sections-only
python3 .agents/skills/nxp-translate/scripts/extract_chapter.py <pdf> 43 --json
```

The dump carries the section tree, cleaned page text with page markers, detected
table grids and the caption index. It never writes to the corpus or the site.

## Reading page text

Every page repeats a running header and a four-line footer. The helper strips
blocks outside the content area (`y0 < 62`, `y0 > 740`) plus these lines
wherever they appear:

```
NXP Semiconductors
S32G3 Reference Manual, Rev. 5, 2025-09-17
Reference Manual
General Business Information
2259 / 5101
```

The running chapter title in the header varies per chapter, so match it by
position, not by a fixed string. **Preserve** `Table continued from the previous
page...` and `Table continues on the next page...` — they sit near those bands
but carry table state.

The PDF text layer splits identifiers at underscores: `PIT_0` arrives as
`PIT 0 _`, `0000_0000h` as `0000 0000h _`. Repair these back to their source
form before translating; never paste the split form into an article. A dropped
or misplaced `_` in a register name, bit range or hex value is a fidelity defect.

Tables sometimes appear in the raw text as a vertical list of cell values
(one cell per line). Do not read that as prose — use `page.find_tables()` (the
helper already emits the row grids) and, when the detector misses a table, read
the cell grid from the PDF layout and rebuild it as text.

## Tables

- Numbered **globally** (`Table 279.`, `Table 280.`), not per chapter. The number
  is only an identifier in the introducing paragraph; it does not appear in the
  article title or as a caption line.
- `page.find_tables()` works on this document (verified on p2253, p2259). Merge
  continuation pages: drop the repeated header row, append the data rows, and
  keep the whole table in one place. A table split across pages is one table.
- **Every table becomes text** — GFM by default, raw HTML only for the narrow
  exception in `references/article-format.md`. Never crop a table as a PNG.

## Figures

- Numbered **globally** (`Figure 256.`, `Figure 260.`). The caption sits **below**
  the drawing (`Figure 260. FTM global time base configuration`).
- Figures are **vector drawings**, not embedded images: `page.get_images()` is
  empty on figure pages while `page.get_drawings()` returns ~100 objects. Extract
  embedded XObjects and you get nothing. Crop by rendering a clip rect:

```python
import pymupdf
page = doc[pno - 1]
drawings = page.get_drawings()
box = pymupdf.Rect()
for d in drawings:
    box |= d["rect"]
# restrict to the region above the caption, then render at >= 2x zoom
clip = pymupdf.Rect(54, box.y0 - 6, 558, caption_y0 - 4)
pix = page.get_pixmap(matrix=pymupdf.Matrix(3, 3), clip=clip, alpha=False)
pix.save("Figure_260.png")
```

Trim the clip to the figure's own band — a whole-page render is not a figure.
Bit-field bars inside register descriptions carry an unnumbered `Diagram` label
rather than a `Figure N.` caption; they are still figures and use
`Diagram_<slug>.png` (see `references/article-format.md`).

Block diagrams, bit-field bars and timing diagrams stay images. Anything with
rows and columns is a table.

## Register descriptions

NXP register descriptions have a fixed shape. Keep it:

1. A memory-map table: `Offset | Register | Width (In bits) | Access | Reset value`.
2. One subsection per register: `Offset`, prose under `Function`, the `Diagram`
   bit-field bar, then a `Fields` table (`Field | Function`, with bit ranges like
   `31-28`).
3. Access information comes from the memory map; bit ranges, reset values and
   offsets stay exactly as printed (`0h`, `98h`, `0000_0000h`, `位 [5:3]`).

Register subsections can be very long (ch67 = 464 pages, ch76 = 498 pages).
They are part of the chapter and translate; they are not droppable chrome.

## Notes and cautions

`NOTE` renders as `**注意：**` + translated body, `CAUTION` as `**警告：**`.
Both carry content and translate.

## Recording the revision

Record `S32G3RM Rev. 5, 2025-09-17` in the PR text and in the header of
`references/chapter-map.md`. NXP articles carry **no** `spec:` / `release:`
front matter (that convention belongs to `docs/autosar/`). When a new revision
lands, re-run the chapter inventory before translating against it: chapter
numbers, page ranges and global figure/table numbers all move.

## Constraints

- The corpus is read-only. Never edit a PDF, never add a `.md` parse to
  `reference-docs/`, never commit a PDF as site content.
- `reference-docs/` is part of the parent repo (tracked via LFS); it is not the
  `private-docs` submodule. Article output goes to `docs/nxp/s32g3/`.
- One run consumes one chapter. Do not read the whole 5101-page document to
  translate one chapter.
