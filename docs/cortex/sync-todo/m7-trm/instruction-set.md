# Sync todo: Group M7-TRM — instruction_set heading repair

> Source: DDI0489F Cortex-M7 TRM r1p2 (`M7/DDI0489F_cortex_m7_trm_r1p2.md`, 8,778 ln, PDF ✅) · no source chapter — article `m7_processor/instruction_set/index.md`, 139 ln
> Steps: S1 source · S2 translate · S3 figures · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR — defined in the [group index](index.md).

## Queue row

- [x] instruction_set — repair the corrupted heading (article `m7_processor/instruction_set/index.md`, 139 ln)
  - Note: live defect — `## ARM=-0987654321   yhn 4esx1` under §1 指令集总结; replace with a proper heading (or drop if it duplicates §1). Content alignment to the Armv7-M instruction chapters is tracked in [ARMv7-M](../armv7-m/index.md); this row is the 1-line hygiene fix only, can ride any other M7 row's PR.
  - S8 result: shipped as `d160f99`.
  - [x] S1 (heading target) [x] S2 [x] S3 (N/A: no figures) [x] S4 (N/A: page already registered) [x] S5 [x] S6 (N/A: one-line hygiene fix) [x] S7 [x] S8
