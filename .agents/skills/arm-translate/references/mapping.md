# Source → article mapping

Evidence column = the figure/table numbers inside the translated page, which
carry the source chapter number. Rows marked *(verify)* were inferred without a
numbered figure; confirm against the source heading before translating.

## Cortex-R52+ (`docs/cortex/r52p_processor/`)

Source: `R52/cortex_r52_trm_100026_0100_00_en.md` (TRM r1p0), plus
`R52/DDI0553B_y_armv8m_arm.md` (Armv8-M ARM) for architecture rules.

| Article | Source chapter | Evidence |
| --- | --- | --- |
| `programmers_model/` | TRM ch3 Programmers Model | `Table3-1` |
| `system_control/` | TRM ch4 System Control | `Figure4-7`…`Figure4-10`, `Table4-48` |
| `memory_system/` | TRM ch7 Memory System | chapter heading; legacy images named `Figure8_*` |
| `memory_protection_unit/` | TRM ch8 Memory Protection Unit | chapter heading; source tables are `Table 8-1`…`Table 8-7`, legacy images named `Table9-*` |

**Legacy image numbering does not follow the current PDF revision.** In
`memory_protection_unit/` the images are named `Table9-*`, but they illustrate
the chapter-8 tables (`Table 8-1 EL1-controlled MPU background region - …`) —
chapter 9 in this revision is the Generic Interrupt Controller. Confirm a
chapter by its heading and table text, never by a legacy file name, and do not
rename existing files.

Not yet translated from the R52 TRM (coverage backlog): clocking and resets,
power management, initialization, generic interrupt controller, generic timer,
debug, performance monitor unit, and the multi-core/implementation chapters.

## Cortex-M7 (`docs/cortex/m7_processor/`)

Sources: `M7/DDI0489F_cortex_m7_trm_r1p2.md` (TRM r1p2) and
`M7/DDI0403E_e_armv7m_arm.md` (Armv7-M ARM E.e); `M7/cortex_m7_at610_at611_sden_1068427_v11_0_en.md`
is the errata notice.

| Article | Source | Evidence |
| --- | --- | --- |
| `arm_architecture_memory_mode/` | Armv7-M ARM appendix A3 | `FigureA3-1`…`FigureA3-5` |
| `exception_model/` | Armv7-M ARM exceptions chapter | `Figure2-1`, `Figure2-2`, `Table2-14-1` *(verify)* |
| `program_status_register/` | M7 TRM programmers model (cross-check ARM B1.2) | `Table2-3`…`Table2-6A` *(verify)* |
| `nested_vectored_interrupt_controller/` | M7 TRM NVIC chapter | no figures *(verify)* |
| `instruction_set/` | Armv7-M ARM instruction-set chapters | no figures *(verify)* |
| `protected_memory_system_archi_pmsav7/` | Armv7-M ARM appendix B3 | `TableB3-1`…`TableB3-11` |
| `system_address_map/` | M7 TRM address-map chapter | `TableB3-3` *(verify)* |

Not yet translated (coverage backlog): M7 TRM clocking/reset, power control,
debug/trace chapters, the SDEN errata notice, and the Armv8-M ARM (R52 pairs
with `DDI0553B` but no article cites it yet).

## Naming new articles

- Directory = lower_snake_case topic name (`memory_protection_unit`, `system_control`),
  not the chapter number.
- One source chapter per article; split a chapter only when the user asks, and
  then state the split in the PR.
- A topic present in both the TRM and the ARM manual (e.g. exceptions) takes
  the architectural source for behaviour and cites TRM differences inline.
