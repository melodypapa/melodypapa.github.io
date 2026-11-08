# Sync todo: Group ARMv7-M — B2 System Memory Model

> Source: DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅) · Part B ch B2 · parse L32964–34504 (1,540)
> Steps: S1 source · S2 translate · S3 figures · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR — defined in the [group index](index.md).

## Queue row

- [x] B2 → new article (System Memory Model — caches, branch predictors, memory-system pseudocode, 1,540 ln; `m7_processor/system_memory_model/`)
  - S1 result: B2 = PDF pp. 570–590; structure fixed to 3 chapters — §1 关于系统内存模型, §2 缓存与分支预测器 (2.1–2.9, with 2.3/2.5/2.6/2.7 unnumbered source headings kept as bold sub-headings), §3 通用内存系统操作的伪代码细节 (3.1–3.11). Census: 1 table (B2-1) + 1 set/way format bar (unnumbered) + Example B2-1.
  - S2 result: article written in place; §3 keeps every pseudocode block verbatim in `arm` fences; terminology fixed as 一致性点 PoC / 统一化点 PoU / 按 MVA / 按 set/way.
  - S3 result: 1 bar cropped at 3× — `EncodingB2-1.png` (p580 set/way register format); Example B2-1 is an assembly listing, not a figure.
  - S4 result: nav entry added before `system_address_map` (source chapter B2 precedes B3); landing item inserted as Cortex-M7 no. 10 with 10–20 renumbered to 11–21.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK; `check_heading_lang.py` OK.
  - S6 result: Table B2-1 rendered as GFM (13 address rows incl. the three reserved entries), footnote `a.` kept; set/way fields A/B/L/S derived lines kept as in source.
  - S7 result: confirmed by the user; shipped as PR #334 (issue #333).
  - S8 result: merged as `6c283e6` (PR #334).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
