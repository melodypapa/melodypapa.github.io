# Sync todo: Group R52plus-TRM — Cortex-R52+ TRM 102199_0001_03 (`arm_cortex_r52plus_processor_trm_102199_0001_03_en.pdf`, 719 pp, PDF only)

Generated: 2026-11-07 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the same PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

**Source shape:** this document has **no ima Markdown parse** — the PDF text layer is the only source, so the "never translate from the PDF when a `.md` exists" rule does not apply here. Crops and table cells come from the same PDF. Section numbers below are the R52+ ones; the older [R52-TRM](R52-TRM.md) group follows `100026` and numbers the same chapters two lower (Programmers Model ch2, System Control ch3, Clocking ch4, Initialization ch6, Memory System ch7, MPU ch8).

Chapter span map (PDF pages): ch1 Introduction 24–27 (4) · ch2 The Cortex-R52+ processor 28–44 (17) · ch3 Programmers Model 45–53 (9) · ch4 System Control 54–218 (165) · ch5 Clocking and Resets 219–222 (4) · ch6 Power Management 223–230 (8) · ch7 Initialization 231–235 (5) · ch8 Memory System 236–275 (40) · ch9 Memory Protection Unit 276–283 (8) · ch10 Generic Interrupt Controller 284–382 (99) · ch11 Generic Timer 383–385 (3) · ch12 Debug 386–435 (50) · ch13 Performance Monitor Unit 436–462 (27) · ch14 Cross Trigger 463–479 (17) · ch15 Embedded Trace Macrocell 480–563 (84) · ch16 Advanced SIMD and floating-point support 564–575 (12) · A Signal Descriptions 576–615 (40) · B Cycle Timings and Interlock Behavior 616–638 (23) · C Processor UNPREDICTABLE Behaviors 639–652 (14) · D PMC-R52+ 653–715 (63) · E Revisions 716–719 (4).

## Queue

- [x] ch3 programmers_model — verified (article `r52plus-trm/programmers_model/index.md`, 289 ln, 2 `##` vs 9 pp, 2026-11-09)
  - Note (S6): R52+ ch3.1 About the programmers model + ch3.2 Armv8-R AArch32 architecture concepts; the article was built from R52 ch2 — compare section by section, fix only real gaps.
  - S1 result: structure matches ch3 exactly — `## 1.` ← 3.1 with 1.1 Advanced SIMD and Floating-point … 1.6 Security state, `## 2.` ← 3.2 with 2.1 Execution state … 2.13 GIC Architecture (2.4.1–2.4.3 under 2.4). Source has no figures and two tables (Table 3-1 processor modes, Table 3-2 Armv8 memory types), both already GFM.
  - S6 result: three real gaps fixed — 2.8 `相关参考` still carried the R52 numbers/pages (ch9 9-247 / ch10 10-332 / ch11 11-336 / ch12 12-383), replaced with the R52+ chapters (ch10 p284, ch11 p383, ch12 p386, ch13 p436); the `Related information` of 3.2 (`Supported standards on page 40`, i.e. 2.4) was missing, added; the `1.4 支持的标准（第 1-24 页）` reference closing 2.13 does not exist in R52+ ch3 (ch1.4 is Useful resources) and was removed. Wording aligned to r0p3: 1.4 reads `PSTATE.T` (was `CPSR.T`). Table 3-1/3-2 row sets match the source. Stray blank lines after the front matter removed.
  - S8 result: PR #350.
  - [x] S1 [x] S6 [x] S7 [x] S8
- [x] ch5 clocking_and_resets — verified (article 124 ln, 3 `##` vs 4 pp, 2026-11-09)
  - Note (S6): ch5.1 Clock and clock enables / 5.2 Reset signals / 5.3 Reset-related signals; check every signal row against the R52+ set (the R52+ adds `Clock and clock enable signals` to appendix A, which this chapter summarises).
  - S1 result: structure matches ch5.1–5.3; Tables 5-1/5-2/5-3/5-4/5-5 all present as GFM with the full R52+ signal sets (CLKIN/CLKINDCLS, eight clock enables, eight reset signals, five reset-related signals).
  - S6 result: four fixes — core name `Cortex-R52` → `Cortex®-R52+` throughout; the clock-gating pointer retargeted from R52 `5-194 5.3` to R52+ `第 223 页的 6.3 Architectural clock gating`; the unnumbered `Reset assertion sequence` / `Reset deassertion sequence` subsections of 5.2 were missing and are now `2.1`/`2.2` with full text; bullet 2.1(1) wording corrected to `冷复位（Cold reset）`.
  - S8 result: PR #352.
  - [x] S1 [x] S6 [x] S7 [x] S8
- [x] ch7 initialization — verified (article 141 ln, 3 `##` vs 5 pp, 2026-11-09)
  - Note (S6): R52+ renumbers 6.3 Booting into EL1 as **7.3 Entering EL1** — confirm the heading/section wording and that 7.1/7.2 carry no R52+-only text.
  - S1 result: structure matches ch7.1–7.3; source has one table (Table 7-1 speculation types), now present.
  - S6 result: five gaps fixed — 7.1.4 Speculation (with Table 7-1) was missing entirely; the `CFGINITREG` paragraph was out of source order, lacked the 4.2 Register summary page ref and the Integration Manual citation; FPU/MPU/TCM page refs retargeted from R52 `3-x` to R52+ 4.3.1 p82 / 4.3.76 p182 / 4.3.92 p203 / 4.3.53 p147; `CFGRAMPROTEN` corrected to `CFGTCMBOOTx` in both 7.2.2 and 7.2.3; heading `引导进入 EL1` → `进入 EL1` and the missing `编程 SPSR` bullet restored.
  - S8 result: PR #352.
  - [x] S1 [x] S6 [x] S7 [x] S8
- [x] ch8 memory_system — verified (article 1076 ln, 13 `##` vs 40 pp, 2026-11-09)
  - Note (S6): 8.12 Peripherals memory map and 8.13 On-line MBIST were already restored into the article on 2026-11-07 from this PDF (see [R52-TRM](R52-TRM.md)); confirm all other sections and tables (AXIM/LLPP/Flash/AXIS) match the R52+ text.
  - S1 result: 8.1–8.13 all present (`Error detection and handling` is the R52+ name of the old 7.9 `Fault detection and handling`, already reflected); eight figures and every table (8-1 … AXIS/LLPP limits) are GFM.
  - S6 result: four fixes — 8.1 `Related information` block added (TCM p238, AXIM p250, LLPP p256, Flash p264); 8.9.3 `相关参考` replaced the invented "第 3 章" sentence with the four record-register page refs (155/105/207/114); 8.9.4 `Related information` added (AXIM p250, AXIM signals p586, AXIS p267, AXIS signals p592); the stale `第 12 章 12.6 Events` pointer retargeted to `第 455 页的 13.6 Events`. Table 8-1 keeps the article's 32KB index `[12:6]` — the PDF prints `[10:6]`, which cannot address 128 sets and is an obvious source typo; recorded here rather than propagated.
  - S8 result: PR #352.
  - [x] S1 [x] S6 [x] S7 [x] S8
- [x] ch9 memory_protection_unit — verified (article 624 ln, 5 `##` vs 8 pp, 2026-11-09)
  - Note (S6): ch9.3 Virtualization support (EL2 MPU registers) must be present; legacy `Table9-*` images carry R52 numbers — verify row sets by caption, never rename.
  - S1 result: 9.3 with 9.3.1 attribute combining present; Tables 9-1 … 9-7 GFM and row sets match (memory-type 12 rows, cacheability 5, shareability 7).
  - S6 result: three fixes — 9.5 register summaries (Tables 9-8/9-9, 9 + 16 rows) were missing and are now at the head of §5 with the direct-access summary; five junk inline PNGs of register-bit names (`SCTLR.M`, `SCTLR.BR`, `HSCTLR.M`, `HSCTLR.BR`, `HCR.DC`) removed with their files (the chapter has no figures); the stale `第 3-148 页表 3-106/3-107` pointer retargeted to `第 174 页表 4-163/4-164`.
  - S8 result: PR #352.
  - [x] S1 [x] S6 [x] S7 [x] S8
- [ ] ⏸ ch4 system_control — completion (article 233 ln, 1 `##` vs 165 pp: 4.1 About, 4.2 Register summary, 4.3 AArch32 register descriptions)
  - Note: >1500-line rule — segment by register group (cache/MPU/EL2/timer/debug) and agree the run plan before S2.
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [x] ch11 → new article (Generic Timer) — `generic_timer/index.md`, 2026-11-09
  - S1 result: ch11.1 About the Generic Timer / 11.2 Generic Timer functional description / 11.3 Generic Timer register summary (11.3.1). One figure (Figure 11-1 Architectural counter interface) and one table (Table 11-1, 15 registers).
  - S2/S3 result: full translation; Figure 11-1 cropped from PDF p384; Table 11-1 rebuilt as GFM with the merged CRn/Op1 cells expanded per row.
  - S4 result: nav entry after 内存保护单元, landing entry 9.
  - S5/S6 result: strict build 0 WARNING; heading-language and index checks OK.
  - S8 result: PR #352.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch1 → new article (Introduction) — `introduction/index.md`, 2026-11-09
  - S1 result: ch1.1 Product revision status / 1.2 Intended audience / 1.3 Conventions (3.1 Glossary, 3.2 the conventions table, 3.3 Timing diagrams, 3.4 Signals) / 1.4 Useful resources (three document tables). One figure (Figure 1-1).
  - S2/S3 result: full translation; the convention-icon column is rendered as named rows (推荐/要求/危险/注意/提示/提醒) because the source cells hold icons only; Figure 1-1 cropped.
  - S4 result: nav entry first in the group, landing entry 1.
  - S5/S6 result: strict build 0 WARNING; checks OK.
  - S8 result: PR #352.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch6 → new article (Power Management) — `power_management/index.md`, 2026-11-09
  - S1 result: ch6.1–6.4 with 6.3.1–6.3.4 and 6.4.1–6.4.6. One figure (Figure 6-1 Processor power domains), no tables; the boxed SEI/VSEI warning at 6.4.3 rendered as `**注意：**`.
  - S2/S3 result: full translation; Figure 6-1 cropped from PDF p227.
  - S4 result: nav entry between 时钟与复位 and 初始化, landing entry 5.
  - S5/S6 result: strict build 0 WARNING; checks OK.
  - S8 result: PR #352.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch16 → new article (Advanced SIMD and floating-point support) — `asimd_floating_point/index.md`, 2026-11-09
  - S1 result: ch16.1–16.6 with 16.6.1–16.6.6. Six figures (Figures 16-1 … 16-6, bit assignments) and six bit-assignment tables plus the 16.5 register summary; the FPINST/FPINST2 note is a `**注意：**` paragraph.
  - S2/S3 result: full translation; all six bit bars cropped from PDF pp566/568/570/572/573/575; every table GFM with the multi-value Reset cells kept in one row via `<br>`.
  - S4 result: nav entry last in the group (ch16), landing entry 10.
  - S5/S6 result: strict build 0 WARNING; checks OK.
  - S8 result: PR #352.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch2 → new article (The Cortex®-R52+ processor) — `processor_overview/index.md`, 2026-11-09
  - S1 result: ch2.1 (2.1.1 Features, 2.1.2 Interfaces, 2.1.3 Configuration options with 2.1.3.1 Processor configurations → 2.1.3.1.1 DCLS / 2.1.3.1.2 Split‑Lock) / 2.2 Component blocks (2.2.1–2.2.7) / 2.3 Interfaces (2.3.1 AMBA → 2.3.1.1–2.3.1.4, 2.3.2–2.3.6) / 2.4 Supported standards (2.4.1–2.4.6) / 2.5 Documentation / 2.6 Design process. Three figures (2-1 … 2-3) and two tables (2-1 configuration options, 2-2 Split‑Lock).
  - S2/S3 result: full translation; the three block diagrams cropped from PDF pp28/30/33; Table 2-1 and 2-2 GFM; the in-table bus-protection note rendered as `**注意：**` after Table 2-1; every `Related information` block translated with the R52+ chapter and page.
  - S4 result: nav entry second in the group, landing entry 2.
  - S5/S6 result: strict build 0 WARNING; checks OK.
  - S8 result: PR #352.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch14 → new article (Cross Trigger) — `cross_trigger/index.md`, 2026-11-09
  - S1 result: ch14.1 About the cross trigger / 14.2 Trigger inputs and outputs (Tables 14-1, 14-2) / 14.3 Cortex-R52+ CTM / 14.4 Cross trigger register summary (Table 14-3, 51 rows) with 14.4.1 External register access permissions / 14.5 Cross trigger register descriptions (14.5.1 CTIDEVID, 14.5.2 CTIITCTRL, 14.5.3 PIDR0-4 + 5-7 with 14.5.3.1-6, 14.5.4 CIDR0-3 with 14.5.4.1-4). Thirteen figures (14-1 block diagram, 14-2 CTM, 14-3 … 14-13 bit bars) and Tables 14-4 … 14-27.
  - S2/S3 result: full translation; all thirteen figures cropped from PDF pp464-479; every table GFM (nested encoding rows kept in one cell via `<br>`), register sections use the 使用限制/陷阱与使能/配置/属性 skeleton.
  - S4 result: nav entry between 通用定时器 and Advanced SIMD 与浮点支持, landing entry 11.
  - S5/S6 result: strict build 0 WARNING; index and heading-language checks OK; 13 embedded figures all present.
  - S8 result: PR #352.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] D → new article (PMC-R52+) — `pmc_r52plus/index.md`, 2026-11-09
  - Note: chapter 8.12 and 8.13 both point at appendix D; the memory-system article's "第 653 页的 D.PMC-R52+" references resolve here once this page exists.
  - S1 result: D.1 Introduction (D.1.1 external integration, D.1.2 pre-integrated) / D.2 Features and benefits / D.3 MBIST usage models (3.1 production, 3.2 on-line off-line memory, 3.3 on-line on-line memory) / D.4 Short-burst software transparent algorithm (4.1 SRAM faults, 4.2 example algorithm, 4.3 Microcode) / D.5 Production test March algorithm (5.1 March algorithm + 5.1.1 notation, 5.2 March C-, 5.3 programming with 5.3.1-5.3.7) / D.6 Example test code / D.7 Functional description + 7.1 RTL constants / D.8 Programmers model (8.1 memory map, 8.2 summary, 8.3 CTRL + 8.3.1 state machine 8.3.1.1-8.3.1.5 + 8.3.2 modes, 8.4-8.15 registers, 8.16 CoreSight registers 8.16.1-8.16.14 incl. 8.16.13.1-8 and 8.16.14.1-4). Thirty-six figures (D-1 … D-36) and Tables D-1 … D-53.
  - S2/S3 result: full translation; all 36 figures cropped from PDF pp654-715; every table GFM (multi-line cells keep `<br>`, `•` list marks preserved), register sections use the 使用限制/陷阱与使能/配置/属性 skeleton. Corpus typos recorded rather than propagated: Table D-19 prints `Y0-X7` for the Y data registers (article uses `Y0-Y7`), 8.16.11 prints `0x000000000` (article `0x00000000`), 8.16.14 prints `CIDR3-CIDR3` (article `CIDR3-CIDR0`). In-appendix references cite section + English title only — the PDF's page pointers for D.8.4/D.8.6/D.8.7/D.8.8/D.8.9/D.8.10 and the 8.16 registers are off by one against the printed pages.
  - S4 result: nav entry last in the group (appendix position), landing entry 13.
  - S5/S6 result: strict build 0 WARNING; index and heading-language checks OK; 36 embedded figures all present.
  - S8 result: PR #352.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch13 → new article (Performance Monitor Unit) — `performance_monitor_unit/index.md`, 2026-11-09
  - Note: 13.6 Events and 13.8 Exporting PMU events must be present; Table 13-29 is the large event table with footnotes 78-82.
  - S1 result: 13.1 About the PMU (1.1-1.5) / 13.2 PMU register summary (Table 13-1, 24 rows) / 13.3 PMCR, PMCEID0, PMCEID1 / 13.4 memory-mapped register summary (Table 13-5, 42 rows) / 13.5 PMCFGR, PMPIDR0-7, PMCIDR0-3 / 13.6 Events (Tables 13-28/13-29, 116 event rows incl. the 26 ERREVENTx-only rows) / 13.7 Interrupts / 13.8 Exporting PMU events (8.1 external hardware, 8.2 debug trace hardware). Fourteen figures (13-1 … 13-14).
  - S2/S3 result: full translation; all 14 figures cropped (13-1 block diagram, 13-2 … 13-14 bit bars); every table GFM with merged CRn/Op1/CRm cells repeated per row in Table 13-1 and the PMIDR/CIDR summaries. Footnotes 78-82 kept as 注 lines after the event table.
  - S4 result: nav entry between 通用定时器 and 交叉触发, landing entry 11.
  - S5/S6 result: strict build 0 WARNING; index and heading-language checks OK; 14 embedded figures all present.
  - S8 result: PR #352.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch12 → new article (Debug) — `debug/index.md`, 2026-11-09
  - S1 result: ch12.1 About Debug (1.1 external debug with 1.1.1–1.1.4, 1.2 self-hosted, 1.3 debug model with 1.3.1–1.3.2) / 12.2 register interfaces (2.1–2.4) / 12.3 system register summary / 12.4 DBGDIDR + DBGDEVID + DBGDEVID1 / 12.5 memory-mapped summary / 12.6 EDCCR, EDRCR, EDDEVID, EDDEVID1, EDPIDR0-4, EDCIDR0-3, EDAA32PFR, EDPFR, EDDFR / 12.7 external debug interface (7.1–7.4) / 12.8 ROM table (8.1–8.4). 31 figures (12-1 external debug system, 12-2…12-20 bit bars, 12-21 APBv3 interface, 12-22 ROMENTRY, 12-23…12-31 PIDR/CIDR), 65 tables.
  - S2/S3 result: full translation; all 31 figures cropped from the same PDF (12-1, 12-18/19/20 needed explicit wide clips because their labels exceed the 150pt label-absorption threshold and the 64-bit bars split into two clusters); every table GFM with the summary tables' merged CRn/op1/CRm/op2 cells expanded per row.
  - S4 result: nav entry between 通用定时器 and 性能监控单元, landing entry 11 (subsequent entries renumbered).
  - S5/S6 result: strict build 0 WARNING; index and heading-language checks OK; 31 embedded figures all present.
  - Source defects (correct values written, not propagated): Table 12-1 repeats 0x830/0x828 for DBGWVR4-7/DBGWCR4-7 and 0x450/0x458 for DBGBVR6-7/DBGBCR6-7 — Table 12-5 gives the correct 0x840/0x848/0x850/0x858/0x860/0x868/0x870/0x878 and 0x460/0x468/0x470/0x478; Table 12-5 names the extended-value registers at 0x464/0x474 `DBGBVR6/7` though the description and Table 12-1 say `DBGBXVR6/7`; Table 12-1 prints JMCR in the DBGDSAR `c2,0,c0,0` group (architecturally c14,7,c0,0) and omits the op2 column for the DBGDEVID/DBGCLAIMx group; Table 12-40 describes EDDFR[15:12] BRPs as "eight watchpoints" (should be breakpoints).
  - S8 result: PR #352.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch10 → new article (Generic Interrupt Controller) — `generic_interrupt_controller/index.md`, 2026-11-09
  - S1 result: ch10.1 About the GIC / 10.2 functional description (2.1 distributor memory map with Tables 10-1/10-2, 2.2 interrupt sources with Table 10-3, 2.3 optional export interface with Figure 10-1) / 10.3 programmers model (3.1 GICD 3.1.1–3.1.15, 3.2 GICR 3.2.1–3.2.16, 3.3 ICH 3.3.1–3.3.10, 3.4 ICC 3.4.1–3.4.21, 3.5 ICV 3.5.1–3.5.16). 80 figures (10-1 block diagram, 10-2…10-64 bit bars, 10-65…10-80 ICV bit bars), 122 tables. Kept as a single article: the GICD/GICR split was rejected because the programmers-model chapter is one continuous register reference.
  - S2/S3 result: full translation; all 80 figures cropped from the same PDF (10-3 and 10-19 needed explicit clips because their bar labels sit below the bar and are not absorbed by the caption-driven cropper); every table GFM with multi-level bit tables flattened and the SGI/LR repeat groups written once with a `P<n>`/`Status<n>` row.
  - S4 result: nav entry between 内存保护单元 and 通用定时器, landing entry 10 (subsequent entries renumbered 10→16).
  - S5/S6 result: strict build 0 WARNING; index and heading-language checks OK; 80 embedded figures all present.
  - Source defects (written as in the source, since they are self-consistent page-range/label quirks): Table 10-1 labels the last row `SGIs target 4` while every other row says `SGIs and PPIs target n`; the ICH summary table omits the CRn/Op1/CRm columns for most rows (reconstructed from the MCR encodings in each register section); `ICH_HCR.TSEI` and several vGIC bits are RES0 yet still described; the `ICH_AP0R1`/`ICC_AP0R1` warnings name a register that Cortex®-R52+ does not implement; `GICR_ICFGR1` is described as read-only in the usage constraints while the summary gives it type RW.
  - S8 result: PR #352.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [ ] ⏸ ch15 → new article (Embedded Trace Macrocell — 84 pp: ETM resources, event connectivity, operation, register descriptions)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8

## Not queued (deliberately)

- A Signal Descriptions (40 pp signal tables), B Cycle Timings and Interlock Behavior, C Processor UNPREDICTABLE Behaviors, E Revisions — reference/chrome material per skill Step 3; revisit on explicit request. Appendix A overlaps `clocking_and_resets` (clock/reset signals) and the interface chapters (AXIM/AXIS/LLPP/Flash signal groups).
- The document glossary and cover/proprietary notice — chrome.
