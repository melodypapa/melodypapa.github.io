# Sync todo: Group io — IO section wrap-up

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [x] dio_driver (SWS_DIODriver · R23-11 markdown · done 2026-10-24 incl. reopen for acronym reformat · commits de11d8a/493ed12/e21067f · PR #53 · 🔁 reopen commits de11d8a/493ed12/e21067f + a5e12c2)
  - Note: 🔁 reopen 2026-10-24 (rule-update audit): source ch.10 Configuration specification (360 lines) was deliberately omitted pre-ban; now translates as `## 8. 配置规范` per the lifted 配置规范 ban — this reopen covers ch.10 only
  - Note: 🔁 reopen run 2026-10-24 (issue #62, commit a5e12c2): ch.10 → `## 8. 配置规范` translated (8.1 容器与配置参数 + 8.1.1 变体 + containers 8.1.2-8.1.7 Dio/DioGeneral/DioPort/DioChannel/DioChannelGroup/DioConfig with 10 param tables + 3 included-container tables + 6 partition constraints; 8.2 发布信息; IDs dropped, merged cells collapsed; DioPortOffset keeps its Link-time x — consistent with VARIANT-LINK-TIME; truncated calculationFormula reconstructed minimally — flagged). Phase A: strict build 0 WARNING; headings ## 1-8; ch.2 15:15 unchanged; no requirement IDs/links
  - Note: 2026-10-24 rule-update audit: dio — source ch.10 Configuration specification (360 lines) deliberately omitted pre-ban → now a gap under the lifted 配置规范 ban (2026-10-24); reopen decision pending
  - Note: 2026-10-24 finished the 3.1/4.2/6.7/7.4 alignment (commits de11d8a/493ed12 · PR #53); the same-day acronym census found §2 still a GFM table (row set 15:15 identical) → reformatted as blockquotes per STANDARD.md §1
  - Note: reopen 2026-10-24 for the acronym-chapter format → finished in commit e21067f; the earlier per-article audit trail is [dio_driver.md](dio_driver.md)
  - Note: 2026-10-24 review (user named dio): source ch.1–8 checked chapter by chapter, no gaps; acronyms 15:15 in source order; `gen_glossary/gen_api_list --check` both exit 0 → no edits, no reopen. The newer R25-11 source differs structurally (7.1.2 expanded, 7.6.3 Transient Faults removed) — following a newer release needs its own reopen row
  - [x] Step 1 — Source resolution + gap analysis (source §2 table 15 rows; article 15:15; gap = format only)
  - [x] Step 2 — In-place translation/completion (table → 15 bold-term + blockquote entries, source order; English full names bolded; intro "下表"→"以下")
  - [x] Step 3 — Phase A mechanical checks (0 table rows, 15 term lines, source order preserved, no h1/requirement IDs, strict build 0 WARNING)
  - [x] Step 4 — Phase B coverage map + fidelity (15↔15 same order; content reuses the already-verified translation, layout only)
  - [x] Step 5 — User confirmation gate (user instruction "run skill to find and fix it" authorised this run; evidence presented in the report, PR #53 could veto)
  - [x] Step 6 — TODO.md row + commit/PR (commit e21067f · PR #53)
- [x] port_driver (SWS_PortDriver · R23-11 markdown · done 2026-10-24 · commit ee486aa · PR #53 / issue #54 · 🔁 reopen commits ee486aa + e2a1e4a)
  - Note: 🔁 reopen 2026-10-24 (rule-update audit): source ch.10 Configuration specification (424 lines) was deliberately omitted pre-ban; now translates as `## 8. 配置规范` per the lifted 配置规范 ban — this reopen covers ch.10 only
  - Note: 🔁 reopen run 2026-10-24 (issue #62): ch.10 → `## 8. 配置规范` translated (8.1 如何阅读本章 / 8.2 容器与配置参数 (PortConfigSet→PortPin, 9 param tables incl. the 11-literal PortPinMode list) / 8.3 约束 (own Constraints section) / 8.4 发布信息; two source-truncated tables (PortVersionInfoApi, PortPinId) recovered from PDF spillover fragments — flagged). Phase A: strict build 0 WARNING; headings ## 1-8; ch.2 unchanged; no requirement IDs/links
  - Note: 2026-10-24 rule-update audit: port — source ch.10 Configuration specification (424 lines) deliberately omitted pre-ban → now a gap; reopen decision pending
  - Note: acronym chapter was a GFM table → blockquotes (row set 7:7 verified); 4.2 "对汽车域的适用性" → "汽车域的适用性"
  - Note: 2026-10-24 Step 1 gap analysis (issue #54): new gap = §1 missing the source ch.1 mapping table (Driver / Port Pin / Channel Group, 2 rows × 4 columns); §4.2 wording and §2 format as noted; §7.6.3 "可配置接口" conflicted with STANDARD.md's "可配置的接口" (5 site articles use the former) → user decision; the rest of §3/§5/§6/§7 matches the source item by item
  - Note: user decision (2026-10-24): keep "可配置接口" in 7.6.3; STANDARD.md §2 and its decision log updated to that term
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion (§1 mapping table translated; §2 table → 7 bold-term + blockquote entries in source order; §4.2 → 汽车域的适用性)
  - [x] Step 3 — Phase A mechanical checks (strict build exit 0 / 0 WARNING; 7-chapter skeleton; ch.2 zero table rows, 7 term lines; no h1/requirement IDs/forbidden chapters; glossary regenerated, `--check` 0, api `--check` 0)
  - [x] Step 4 — Phase B coverage map + fidelity (source ch.1–8 mapped section by section; ch.6/9/10/A deliberately omitted; §1 table translated 4 columns × 2 rows verbatim; ch.2 7:7 same order)
  - [x] Step 5 — User confirmation gate (2026-10-24 confirmed: Phase A/B evidence + TODO.md row; 7.6.3 decision keeps "可配置接口")
  - [x] Step 6 — TODO.md row + commit/PR (commit ee486aa · PR #53 · Closes #54)
- [x] pwm_driver (SWS_PWMDriver · R23-11 markdown · done 2026-10-24 · commit 1b5e44b · PR #57 / issue #56 · 🔁 reopen commits 1b5e44b + d8e6e56)
  - Note: 🔁 reopen 2026-10-24 (rule-update audit): source ch.10 Configuration specification (567 lines) was deliberately omitted pre-ban; now translates as `## 8. 配置规范` per the lifted 配置规范 ban — this reopen covers ch.10 only
  - Note: 🔁 reopen run 2026-10-24 (issue #62): ch.10 → `## 8. 配置规范` translated (8.1-8.3 with containers Pwm/PwmGeneral/PwmPowerStateConfig/PwmChannel/PwmChannelConfigSet/PwmConfigurationOfOptApiServices, 20 param tables; truncated boolean descriptions reconstructed to standard phrasing per the garbled-text policy (PwmDevErrorDetect, PwmDutycycleUpdatedEndperiod — flagged); '--' placeholders kept verbatim; hyphenated container name normalized; rows missing from the source (PwmPowerState M/Type, PwmChannelClass full literal list) not invented — flagged). Phase A: strict build 0 WARNING; headings ## 1-8; ch.2 unchanged; no requirement IDs/links
  - Note: 2026-10-24 rule-update audit: pwm — source ch.10 Configuration specification (567 lines) deliberately omitted pre-ban → now a gap; reopen decision pending
  - Note: acronym chapter table → blockquotes (row set 13:13 verified); 4.2 "对汽车域的适用性" → "汽车域的适用性"
  - Note: 2026-10-24 Step 1 gap analysis (issue #56): the source ch.2 has **12** data rows (6 acronyms + 6 abbreviations), not 13 — the earlier 13:13 note counted a header; §2 is still a GFM table → convert to blockquotes; §4.2 heading is a §2 forbidden variant; §7.2.1 Pwm_ChannelType wrongly carries "8..32 位" (source Range is `- -`; 8..32 bit belongs to Pwm_PeriodType); §7.2.8 Pwm_PowerStateType carries a PWM_FULL_POWER (0x00) row absent from the R23-11 table (it exists in R25-11) → user decision; §1/§3–§7 otherwise match the source section by section
  - Note: user decision (2026-10-24, issue #56): delete the §7.2.8 `PWM_FULL_POWER（0x00）` bullet — strict R23-11 alignment (the value is only defined from R25-11 on)
  - [x] Step 1 — Source resolution + gap analysis (source 1962 lines; article 736; gaps as noted)
  - [x] Step 2 — In-place translation/completion (§2 two tables + "缩略语：/缩写：" lead-ins → 12 bold-term + blockquote entries in source order; §4.2 → 汽车域的适用性; §7.2.1 range corrected; §7.2.8 FULL_POWER bullet removed per decision)
  - [x] Step 3 — Phase A mechanical checks (strict build exit 0 / 0 WARNING; 7-chapter skeleton; ch.2 zero table rows, 12 term lines + 12 blockquotes; no h1/requirement IDs/forbidden heading variants; §3.1–7.7 numbering continuous; 4.2 rename has no inbound anchor links; glossary regenerated + `--check` 0, api `--check` 0)
  - [x] Step 4 — Phase B coverage map + fidelity (source ch.1–8 ↔ §1–§7 section by section; ch.6 requirements tracing / ch.9 sequence diagrams / ch.10 configuration specification / ch.11 not-applicable requirements deliberately omitted; the "duplicated" configurable On/Off sentences in §7.3.2–7.3.8 are two distinct source requirements — pre-compile-time (10xx) + configurable (20xx) with macro; §5.1.2 source-garbled "Pwm.h, Det.h and ." reconstructed as "Pwm.h和Det.h"; §7.2.1/§7.2.8 fidelity fixes as decided)
  - [x] Step 5 — User confirmation gate (2026-10-24 confirmed: Phase A/B evidence + TODO.md row; §7.2.8 decision = delete PWM_FULL_POWER (0x00))
  - [x] Step 6 — TODO.md row + commit/PR (commit 1b5e44b · PR #57 · Closes #56)
- [ ] ocu_driver (SWS_OCUDriver · R23-11 markdown · ✅ alignment + row set)
  - Note: STANDARD.md lifted the 配置规范 ban (2026-10-24) — if the source has ch.10 Configuration specification, it translates as the optional article `## 8. 配置规范` (skill Step 5 config-spec rules); measure it in Step 1
  - Note: acronym chapter table → blockquotes, restore the MCU row (source 14 rows → article 13 entries), drop the "Term definition:" pseudo-row; 3.1 "输入文档与相关标准和规范" → "输入文件"
  - Note: 2026-10-24 Step 1 (issue #61): source 2419 lines; verified §2 = 13 data rows (9 acronyms incl. the duplicate MCU + 4 terms; "Term definition:" is a table header); §4 finding — article had 4.1 假设/4.2 限制/4.3 对汽车领域的适用性 vs skeleton 4.1 限制/4.2 汽车域的适用性 (no aligned precedent: adc/port/pwm/dio sources lack Assumptions); ch.10 = 810 lines, 32 SWS Item tables, 6 containers + 10.3 Published Information
  - Note: DECISION TO RATIFY at Step 5: source 4.1 Assumptions folded into the 约束和假设 chapter intro (bolded lead-ins 时钟/资源/计数和比较, both figures kept); 限制→4.1, 适用性→4.2 汽车域的适用性 — alternative would need a STANDARD.md amendment for a third §4 subsection
  - [x] Step 1 — Source resolution + gap analysis (issue #61)
  - [x] Step 2 — In-place translation/completion (§3.1 renamed; §2 → 13 blockquote entries in source order, duplicate MCU restored, 术语定义 lead-in kept; §4 restructured; new §8. 配置规范: 10.1 + 8.1.1-8.1.3 legend tables, containers 8.2.1-8.2.6 with 26 parameter tables + 3 included-container tables, 8.3 发布信息; [SWS_*/ECUC_*] IDs dropped, merged cells collapsed, config-class rows collapsed per class with applicability marks)
  - [x] Step 3 — Phase A mechanical checks (strict build 0 WARNING; headings exactly ## 1-8 with ## 8. 配置规范; ch.2 0 table rows, 13 term lines == 13 source rows; no h1/requirement IDs; renamed headings have no inbound anchor links; glossary regenerated + --check 0; api --check 0; check 8 link audit: article has zero links, images only)
  - [x] Step 4 — Phase B coverage map + fidelity (source ch.1-8 ↔ §1-§7 pre-existing ✅ untouched; ch.9 时序图 omitted (forbidden); ch.10 → §8 mapped section by section incl. all 10.2.x containers and 10.3; appendices A/B omitted (forbidden); UML-dump/figure-caption PDF garbage omitted; OcuMaxCounterValue's truncated source sentence reconstructed minimally — flagged for gate; OcuChannel param order kept as source (ECUC_00160 before 00159))
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [x] icu_driver (SWS_ICUDriver · R23-11 markdown · 🔶→✅ alignment · done 2026-10-24 (realigned to R23-11: 4.2 rename, 3.2/3.3 naming, ch.10 → ## 9. 配置规范, release bump + glossary))
  - Note: STANDARD.md lifted the 配置规范 ban (2026-10-24) — if the source has ch.10 Configuration specification, it translates as the optional article `## 8. 配置规范` (skill Step 5 config-spec rules); measure it in Step 1
  - Note: delete the forbidden "时序图" chapter; 4.2 "适用车型域" → "汽车域的适用性"; acronym row set 12:12 already verified
  - Note: 2026-10-24 Step 1 (issue #67): row source = R23-11 markdown (no fallback needed); the ARTICLE's front-matter still says R22-11 → bumped to R23-11 as part of this Group-io realignment. Gaps measured: (1) 4.2 「适用车型域」→「汽车域的适用性」; (2) source ch.10 Configuration specification present (657 lines: 10.1 + 10.2.1-10.2.9 containers Icu/IcuGeneral/IcuOptionalApis/IcuChannel/IcuSignalEdgeDetection/IcuSignalMeasurement/IcuTimestampMeasurement/IcuWakeup/IcuConfigSet with 28 params + 10.3) → article has no 配置规范 chapter → translate as `## 9. 配置规范` (§8 is the 时序图 chapter); (3) naming — article 3.3 「相关规格说明」 is a 1-off (site majority: 15 articles use 相关规范 for the source's "Related specification"; icu's 相关规范 sits on the IEC standards subsection) → user decision at the gate. Verified aligned: ch.2 12:12 source order; API 12 types/26 functions names+order; §5 5.1-5.5; 时序图 8.1-8.17 ↔ source 9.1-9.17 complete; §3.1 12 items incl. [8]; §4.1 限制. Observation (out of scope): §6.1 headings are R22-11-flavoured (重入性/模块模式 vs R23-11 7.1.1/7.1.2 Background&Rationale/Requirements) — content covered
  - [x] Step 1 — Source resolution + gap analysis (R23-11 `AUTOSAR_CP_SWS_ICUDriver.md`, 2700 lines; gaps as noted above)
  - [x] Step 2 — In-place translation/completion (4.2 适用车型域 → 汽车域的适用性; front-matter release R22-11 → R23-11 (Group-io realignment); source ch.10 → new `## 9. 配置规范`: 9.1 如何阅读本章, 9.2 容器与配置参数 with 9.2.1-9.2.9 (Icu/IcuGeneral 4 params/IcuOptionalApis 13 params/IcuChannel 5 params + 4 included containers/IcuSignalEdgeDetection/IcuSignalMeasurement/IcuTimestampMeasurement 2 params/IcuWakeup/IcuConfigSet), 9.3 发布信息; 28 param tables; [SWS_*/ECUC_*] IDs dropped, merged cells collapsed, class rows collapsed per class with the source's exact values + VARIANT/All-Variants annotations — all 34 verified programmatically; glossary regenerated for the release bump; 3.2/3.3 renamed 相关规范/相关规格说明 → 相关标准和规范/相关规范 per the site majority (port/fee/crypto precedent, matches the source numbering) — user decision 2026-10-24)
  - [x] Step 3 — Phase A mechanical checks (strict build exit 0 / 0 WARNING / no icu notices; headings ## 1-9 with ## 8. 时序图 + ## 9. 配置规范, sub-numbering continuous; ch.2 0 table rows, 12 term lines unchanged; no h1/requirement IDs/forbidden variants; no external links; glossary regenerated + --check 0; api --check 0; api sync 12 types/26 functions OK; param set 28:28 vs source)
  - [x] Step 4 — Phase B coverage map + fidelity (source ch.1-8 ↔ §1-§7 pre-existing (R22-11-translated), measured aligned: ch.2 12:12 source order, API 12 types/26 functions names+order, §5 5.1-5.5, §3 3.1-3.3 incl. [8], §4 4.1/4.2 renamed; ch.9 ↔ §8 时序图 kept (mermaid, 8.1-8.17 ↔ 9.1-9.17 complete — the site's 时序图 precedent; its intro cites R22-11, the release the diagrams were drawn from, per-chapter citation kept while the article baseline moved to R23-11); ch.10 → §9 mapped section by section (9.1, 9.2.1-9.2.9, 9.3); ch.6 requirements traceability + ch.11 not-applicable requirements omitted (forbidden). Fidelity: all 34 §9 class rows verified programmatically against the source (values + VARIANT/All-Variants annotations); 28 params 1:1 source order; enum ranges with per-literal descriptions (IcuMeasurementMode ×4, IcuSignalMeasurementProperty ×4, IcuTimestampMeasurementProperty ×2, IcuDefaultStartEdge ×3); included-container tables (Icu ×3, IcuChannel ×4, IcuConfigSet ×1); 4 partition constraints at source positions. Reconstructions flagged: IcuDevErrorDetect + IcuEdgeCountApi descriptions (source merged-cell garbling), IcuDefaultStartEdge description (beginning lost in the source), IcuMaxChannel description (garbled source English), ICU_MODE_EDGE_COUNTER's range description (truncated mid-sentence). Observation: §6.1 headings are R22-11-flavoured (重入性/模块模式 vs R23-11 7.1.1/7.1.2) — content covered, out of scope)
  - [x] Step 5 — User confirmation gate (2026-10-24 confirmed: Phase A/B evidence + TODO.md row; decisions — 3.2/3.3 content kept in source order with headings renamed to the site pattern (相关标准和规范 / 相关规范), 时序图 intro keeps its per-chapter R22-11 citation)
  - [x] Step 6 — TODO.md row + commit/PR (commits d11d759/9cb8764 · PR #68 · Closes #67)
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] adc_driver (SWS_ADCDriver · R23-11 markdown · ✅ alignment + deep completion)
  - Note: STANDARD.md lifted the 配置规范 ban (2026-10-24) — if the source has ch.10 Configuration specification, it translates as the optional article `## 8. 配置规范` (skill Step 5 config-spec rules); measure it in Step 1
  - Note: acronym row-set repair — source 18 rows → article 16 entries: restore API/HW/SW, restore the DEM→DET source order, merge Conversion Mode back into one entry, keep aliases on the term line (ADC Result Buffer (…,…)); 4.2 "适用车型域" → "汽车域的适用性"; deep completion (gaps measured by eval-2): ~78 SWS requirement texts in the API chapter untranslated, §3.1 stale 13-item list to be replaced by the two R23-11 items, §7.4.1 Background untranslated
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] iohwab (SWS_IOHardwareAbstraction · R23-11 markdown · ⚠️ gaps)
  - Note: STANDARD.md lifted the 配置规范 ban (2026-10-24) — if the source has ch.10 Configuration specification, it translates as the optional article `## 8. 配置规范` (skill Step 5 config-spec rules); measure it in Step 1
  - Note: missing "约束和假设" chapter; delete the forbidden "时序图" chapter; 3.1 is already "输入文件"
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none — all 7 IO SWS documents are queued)
