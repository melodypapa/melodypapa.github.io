# Sync todo: Group ARMv7-M — A5 The Thumb Instruction Set Encoding

> Source: DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅) · Part A ch A5 · parse L7082–8272 (1,190)
> Steps: S1 source · S2 translate · S3 figures · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR — defined in the [group index](index.md).

## Queue row

- [x] A5 → new article (The Thumb Instruction Set Encoding, 1,190 ln; e.g. `m7_processor/thumb_instruction_set_encoding/`)
  - Note: encoding tables are textual — GFM by default; raw HTML only when the structure qualifies (see .agents/skills/arm-translate/references/article-format.md §Tables). A7 instruction-by-instruction details are NOT in this row (deferred tail).
  - S1 result: A5 = PDF pp. 125–158; structure fixed to 3 chapters — §1 Thumb 指令集编码 (1.1 UNDEFINED/UNPREDICTABLE 空间, 1.2 0b1111 寄存器说明符, 1.3 0b1101/SP 支持 1.3.1–1.3.3), §2 16 位编码 (2.1–2.6, 2.5.1 If-Then 与提示), §3 32 位编码 (3.1–3.18, 3.4.1 提示, 3.4.2 杂项控制, 3.11.1 移动寄存器和立即数移位).
  - S2 result: article `m7_processor/thumb_instruction_set_encoding/index.md` written in place; numbering restarts at 1; source typos preserved.
  - S3 result: 30 encoding-bar crops at 3× (`EncodingA5-2.png`, `EncodingA5-2-1`…`EncodingA5-2-6`, `EncodingA5-2-5-1`, `EncodingA5-3.png`, `EncodingA5-3-1`…`EncodingA5-3-18`, `EncodingA5-3-4-1`, `EncodingA5-3-4-2`, `EncodingA5-3-11-1`); p143/p150/p152/p156 each yield two bars.
  - S4 result: nav entry added after the instruction-set page; landing item inserted as Cortex-M7 no. 5 with 5–18 renumbered to 6–19.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py` OK (324 nav targets, 0 broken links); `check_heading_lang.py` OK.
  - S6 result: all 30 tables (A5-1 … A5-30) rendered as GFM with merged cells expanded by repeating the spanning value; footnotes as `a.` / `b.` lines; cross-references phrased as `MOV（立即数）（第 A7-291 页）`.
  - S8 result: merged as `de13acc` (PR #327).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
