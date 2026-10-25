# Sync todo: dio_driver

Article: `docs/autosar/io/dio_driver/index.md` · Source: `AUTOSAR_CP_SWS_DIODriver.md` (R23-11 markdown, 1321 lines) ·
Generated: 2026-10-24 · Issue: #52
(Resume = the first item still `[ ]`; all `[x]` + the TODO.md row updated = this sync is finished)

## Rule checks (STANDARD.md expanded)
- [x] Seven-chapter skeleton complete, numbering 1–7 continuous
- [x] Forbidden chapters omitted (source ch.6 Requirements Tracing, appendix A) — ch.9/ch.10 were translated back in later per the lifted bans: `## 8. 时序图` (reopen #65) and `## 9. 配置规范` (reopen #62, commits a5e12c2/04a009f)
- [x] front-matter title is the only h1; no `# ` in the body; no `[SWS_Dio_xxxxx]` requirement IDs left
- [x] WeChat footer `<section id="wechat">` + `<h4>`; nav registered
- [x] §3.1 heading is the direct translation "输入文件和相关标准与规范" (reverted 2026-10-25)
  - Note: had been renamed to "输入文件" per the then-canonical STANDARD.md §1; user decision 2026-10-25 — translate the source heading directly → STANDARD.md §1/§2 updated, "输入文件" now a forbidden variant
- [x] §4.2 heading changed to "汽车域的适用性"
  - Note: first changed to STANDARD.md's then-listed "适用于汽车领域"; the user settled on "汽车域的适用性" during PR review → STANDARD.md §2 updated accordingly (commit 493ed12)
- [x] §7.5 heading kept as "调度函数"
  - Note: had been changed to the then-listed "周期函数"; the user kept "调度函数" (7 site articles vs 2 for BswM/CanNm) → STANDARD.md §2/§3 updated and the decision recorded (commit de11d8a)

## Content gaps (vs the source document)
- [x] All source content of ch.1–7 translated — no gaps
  - Note: 15 acronyms, 2 input documents, 2 dependency modules, functional spec 7.1–7.7 (incl. MaskedWritePort / output-pin readback), 5 type definitions, 9 API functions (description + C signature + requirement text), development-error table, callbacks/scheduled functions/expected interfaces
- [x] §6.7 "安全事件" body "无。" → "本模块不报告安全事件。"
  - Note: source *The module does not report security events.*, faithful translation
- [x] §7.4 typo "下层层" → "下层"

## Verification and wrap-up
- [x] Phase A mechanical checks
  - Note: `mkdocs build --strict` exit 0, 0 WARNING, 0 ERROR; rendered anchors `31-输入文件` / `42-汽车域的适用性` / `67-安全事件` / `75-调度函数` / `76-期望接口`; no inbound site links to the renamed headings
- [x] Phase B coverage map + fidelity spot check
  - Note: source §1–§8 sections ↔ article §1–§7 one-to-one; forbidden chapters listed as deliberate omissions; the SWS was the verification baseline
- [x] User confirmation gate (Step 7)
  - Note: both wording decisions were given by the user during the run (see the decision log); revisions took effect after the gate
- [x] `docs/autosar/TODO.md` row + last-updated date
  - Note: DIO row annotated as aligned; io section split per specification; similar deviations (adc/icu/ocu/port/pwm 3.1·4.2, bswm/cannm/csm scheduled functions) added to the todo list
- [x] Commit + PR
  - Note: commits de11d8a + 493ed12 · PR #53 · Closes #52

## Decision log (append-only)
- 2026-10-24 user: *Scheduled functions* named "调度函数" (not "周期函数") → STANDARD.md §2/§3, BswM/CanNm/Csm queued
- 2026-10-24 user: *Applicability to car domains* named "汽车域的适用性" (not "适用于汽车领域") → STANDARD.md §2, 9 variant articles queued
- 2026-10-25 user: §3.1 heading reverted to the direct translation "输入文件和相关标准与规范" (no canonical renames — headings translate the source directly) → STANDARD.md §1/§2 + skill updated; site-wide realignment queued in TODO.md Backlog
- 2026-10-25 session: stale rule-check line corrected — `## 8. 时序图` / `## 9. 配置规范` were re-added by reopens #62/#65 (commits a5e12c2/04a009f) after this file was completed

## Out of scope (deliberately skipped)
- Source ch.6 Requirements Tracing / appendix A — STANDARD.md-forbidden chapters, omitted as required (ch.9 → `## 8. 时序图` and ch.10 → `## 9. 配置规范` were translated in afterwards — see reopens #62/#65)
- The same wording deviations in port/pwm/adc/icu/ocu/bswm/cannm/csm — outside the DIO scope, tracked in the TODO.md todo list
