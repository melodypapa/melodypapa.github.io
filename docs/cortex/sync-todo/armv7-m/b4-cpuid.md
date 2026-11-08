# Sync todo: Group ARMv7-M — B4 The CPUID Scheme

> Source: DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅) · Part B ch B4 · parse L38282–39914 (1,632)
> Steps: S1 source · S2 translate · S3 figures · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR — defined in the [group index](index.md).

## Queue row

- [x] B4 → new article (The CPUID Scheme, 1,632 ln; `m7_processor/cpuid_scheme/`)
  - S1 result: B4 = PDF pp. 644–668; structure fixed to 8 chapters — §1 关于 CPUID 方案 (1.1 约定, 1.2 汇总), §2 处理器特性 ID (2.1–2.2), §3 调试特性 ID (3.1), §4 辅助特性 ID (4.1), §5 内存模型特性 (5.1–5.4), §6 指令集属性 (6.1 描述约定 + 6.2–6.6, 含 同步原语支持), §7 浮点特性标识 (7.1–7.4), §8 缓存控制标识 (8.1–8.4). Census: 4 tables (B4-1 … B4-4) + 19 register bit bars.
  - S2 result: article written in place; register subsections follow the M7 house pattern (**用途** / **使用限制** / **配置** / **属性** + bar + 位/名称/值/功能 table); §1.2 Table B4-1 covers 19 register rows.
  - S3 result: 19 bars cropped at 3× — `FigureB4-1.png` … `FigureB4-19.png` (PFR0, PFR1, DFR0, AFR0, MMFR0–2, ISAR0–4, MVFR0–2, CLIDR, CCSIDR, CSSELR, CTR); ID_MMFR3 has no bar in the source and is rendered as a table only.
  - S4 result: nav entry added after `mpu` (source chapter B4 follows B3.5); landing item inserted as Cortex-M7 no. 13 with 13–21 renumbered to 14–22.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (331 nav targets); `check_heading_lang.py` OK.
  - S6 result: Tables B4-1 … B4-4 rendered as GFM; every register field table uses the four-column `位 / 名称 / 值 / 功能` grid with one row per field value.
  - S7 result: confirmed by the user; shipped as PR #334 (issue #333).
  - S8 result: merged as `6c283e6` (PR #334).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
