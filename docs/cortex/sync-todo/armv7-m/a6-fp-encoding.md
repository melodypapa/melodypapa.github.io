# Sync todo: Group ARMv7-M — A6 The Floating-point Instruction Set Encoding

> Source: DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅) · Part A ch A6 · parse L8272–8634 (362)
> Steps: S1 source · S2 translate · S3 figures · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR — defined in the [group index](index.md).

## Queue row

- [x] A6 → new article (The Floating-point Instruction Set Encoding, 362 ln; `m7_processor/fp_instruction_set_encoding/`)
  - S1 result: A6 = PDF pp. 160–170; structure fixed to 7 chapters — §1 概述, §2 浮点指令语法 (2.1 数据类型说明符, 2.2 寄存器说明符, 2.3 寄存器列表), §3 寄存器编码, §4 浮点数据处理指令 (4.1 修改立即数常量的运算), §5 扩展寄存器加载或存储指令, §6 32 位传送, §7 64 位传送. Census: 9 tables (A6-1 … A6-9) + 5 unnumbered encoding bars.
  - S2 result: article written in place; numbering restarts at 1; source typo `{<Dd[x]>,<Dd+2[x]}` preserved; table A6-5 rebuilt from the PDF cell grid (merged opc/instruction cells expanded per block).
  - S3 result: 5 encoding bars cropped at 3× — `EncodingA6-4.png` (p164 register encoding), `EncodingA6-5.png` (p165 data-processing), `EncodingA6-7.png` (p167 load/store), `EncodingA6-8.png` (p168 32-bit transfer), `EncodingA6-9.png` (p169 64-bit transfer).
  - S4 result: nav entry added after `thumb_instruction_set_encoding`; landing item inserted as Cortex-M7 no. 6 with 6–19 renumbered to 7–20.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (0 broken links); `check_heading_lang.py` OK.
  - S6 result: all 9 tables (A6-1 … A6-9) rendered as GFM; Table A6-5 expanded to 22 rows from the merged-cell grid; footnotes as `a.` lines; cross-references phrased as `VSEL（第 A7-497 页）`.
  - S7 result: confirmed by the user; shipped as PR #334 (issue #333).
  - S8 result: merged as `6c283e6` (PR #334).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
