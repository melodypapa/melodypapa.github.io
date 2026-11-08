# Sync todo: Group ARMv7-M — B5 System Instruction Details

> Source: DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅) · Part B ch B5 · parse L39914–40432 (518)
> Steps: S1 source · S2 translate · S3 figures · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR — defined in the [group index](index.md).

## Queue row

- [x] B5 → new article (System Instruction Details, 518 ln; `m7_processor/system_instructions/`)
  - S1 result: B5 = PDF pp. 670–678; structure fixed to 2 chapters — §1 关于 Armv7-M 系统指令 (1.1 特殊寄存器编码), §2 系统指令描述 (2.1 CPS, 2.2 MRS, 2.3 MSR). Census: 2 tables (B5-1, B5-2) + 3 encoding bars (T1 for CPS/MRS/MSR) + assembler-syntax and operation pseudocode.
  - S2 result: article written in place; each instruction keeps the source order 汇编器语法 → 操作 → 异常 → 备注 → 编码 T1; pseudocode and assembler syntax verbatim in `arm` fences.
  - S3 result: 3 bars cropped at 3× — `EncodingB5-1.png` (CPS), `EncodingB5-2.png` (MRS), `EncodingB5-3.png` (MSR).
  - S4 result: nav entry added after `cpuid_scheme` (source chapter B5 follows B4); landing item inserted as Cortex-M7 no. 14 with 14–22 renumbered to 15–23.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (332 nav targets); `check_heading_lang.py` OK.
  - S6 result: Tables B5-1 and B5-2 rendered as GFM; the two-bullet Note under §2 kept as a `**注意：**` block.
  - S7 result: confirmed by the user; shipped as PR #334 (issue #333).
  - S8 result: merged as `6c283e6` (PR #334).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
