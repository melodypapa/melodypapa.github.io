# AUTOSAR translation queue — index

> Generated: 2026-10-24 · Foundation batch added 2026-11-02 · CP methodology batch added 2026-11-06 · Base: R23-11 (`~/Workspace/autosar_standard/markdown/` — `Classic_Platform/` for Groups 1–16 and 19, `Foundation/` for Groups 17–18)
> Model: Group queue modelled on py-armodel `sync-autosar-class` — one `Group-<section>.md`
> per batch, one row per document, each row carrying a 6-step sub-checklist;
> **resume = the first row still `[ ]` in the chosen batch file**; all rows `[x]` =
> batch complete. Format and tick rules: `references/todo-format.md` (autosar-translate skill).
> The status ledger (what each article currently IS) is [`../TODO.md`](../TODO.md); this
> directory is the execution queue (what to do next).

## Batch order (recommended)

| # | Batch file | Rows | Content |
| --- | --- | ---: | --- |
| 1 | [Group-io.md](Group-io.md) | 7 | IO wrap-up — **batch complete 2026-10-27 (7/7)** (1 done + wording/acronym alignment + iohwab gaps + adc deep completion) |
| 2 | [Group-general.md](Group-general.md) | 4 | **batch complete 2026-11-02 (4/4)** — platform_types stub repair + BSWGeneral + communication_stack_types; the tr_glossary row moved to Group-foundation (Foundation document) |
| 3 | [Group-crypto.md](Group-crypto.md) | 4 | **batch complete 2026-10-28 (4/4)** — Csm alignment (PR #133) + crypto_driver full completion + CryIf/KeyM new articles; Csm reopened 2026-10-28 (incomplete) → full R23-11 re-sync complete 2026-10-31 |
| 4 | [Group-system_services.md](Group-system_services.md) | 7 | **5/7 done 2026-11-01** (operating_system + det + FiM + time_service + comm PR #230) — remaining: SwCluC (24.7k-line source, giant), HwTestManager |
| 5 | [Group-mode_management.md](Group-mode_management.md) | 2 | EcuM alignment + BswM alignment (small) |
| 6 | [Group-diagnostics.md](Group-diagnostics.md) | 3 | **batch complete 2026-11-01 (3/3)** — Dem near-full build + j1939dcm new article + Dcm 24k-line sync (PR #225) |
| 7 | [Group-memory.md](Group-memory.md) | 12 | **5/12 done 2026-11-01** (memory_access, memory_mapping, bulk_nv_data_manager + flash_driver PR #223, nvram_manager) — next: flash_eeprom_emulation; remaining: Ea/Eep/MemIf/MemDriver/FlsTst/RamTst new articles |
| 8 | [Group-communication.md](Group-communication.md) | 27 | 18 existing articles completed/aligned + 9 backbone documents (Com/CanSM/CanTp/TcpIp/Nm/EthSM/IpduM/SomeIp×2) |
| 9 | [Group-mcal.md](Group-mcal.md) | 3 | Mcu, Gpt, CoreTest |
| 10 | [Group-globaltime.md](Group-globaltime.md) | 4 | **batch complete 2026-10-31 (4/4)** — StbM + CanTSyn/EthTSyn/FrTSyn |
| 11 | [Group-libraries.md](Group-libraries.md) | 9 | Crc, E2E library and 7 more |
| 12 | [Group-safety.md](Group-safety.md) | 3 | WdgM/WdgIf/Wdg |
| 13 | [Group-security.md](Group-security.md) | 2 | Firewall, IdsM |
| 14 | [Group-rte-swarch.md](Group-rte-swarch.md) | 2 | RTE, ARTI |
| 15 | [Group-communication-2.md](Group-communication-2.md) | 38 | **18/38 done 2026-11-01** (Spi/LdCom/LsDu/Dlt/DoIp/XCP/CanXL×2/EthTrcv/WEth×2/FlexRay×7 + flexray_iso_tp this branch) — remaining: LinSM/LinTrcv/TTCAN×2/J1939×3/IEEE1722/MACsec/CellularV2X/ChargingManager/ChineseV2X×4/V2X×5 |
| 16 | [Group-exp.md](Group-exp.md) | 20 | 20 missing EXP guides (the TPS template is exempt and not queued, same flow) |
| 17 | [Group-foundation-exp.md](Group-foundation-exp.md) | 20 | **Foundation guides/templates/reports** (EXP 5 / TR 6 / TPS 8 / ASWS 1) — document-type counterpart of CP's Group-exp; 1 in-flight (TR Glossary, ch.4 14/343 terms); size-ascending |
| 18 | [Group-foundation-rs-prs.md](Group-foundation-rs-prs.md) | 32 | **Foundation requirement/protocol specifications** (RS 23 / PRS 9) — size-ascending; the RS/PRS item-ID keep-or-drop decision is recorded in the file header |
| 19 | [Group-cp-methodology.md](Group-cp-methodology.md) | 17 | **CP 方法论与模板** — the `MethodologyAndTemplates` folder (RS 6 / TPS 7 / TR 4), size-ascending; 1 existing-article alignment row (BSWMDT) + 16 new articles; the item-ID decision proposed in the file header is confirmed at the first run's Step 1 |

Total 217 documents = CP 165 + Foundation 52. CP 165 = all **127 R23-11 SWS** (io 7 + general 4 + crypto 4 + system_services 7 + mode_management 2 + diagnostics 3 + memory 12 + communication 65 + globaltime 4 + libraries 9 + mcal 3 + rte-swarch 2 + safety 3 + security 2, 1 of them already done) + **20 missing EXP** + **17 MethodologyAndTemplates documents** (Group 19, added 2026-11-06 — the original 2026-10-24 bootstrap scoped the CP batch to SWS + EXP and left the whole folder unqueued with only the BSWMDT exempt line in Group-exp; the user asked to close that gap). Foundation 52 = every `AUTOSAR_FO_*` document of R23-11 (`Foundation/Releases/R23-11/`, 10 topics), all skeleton-exempt, 1 partially translated (TR Glossary) — split by document type on 2026-11-03 (user request, CP Group-exp model): Group 17 = 20 guide/template/report documents, Group 18 = 32 requirement/protocol specifications. Batch order is adjustable; row order inside a batch = suggested execution order (small/alignment work first, giant sources last).

## Rules

- **One document per run**: take one row, run all 6 steps (including the user confirmation gate), flip the row + its sub-checklist, record the commit hash, then stop (autosar-translate SKILL.md Steps 7/8).
- **A `[x]` row is never reopened** unless the user changes the baseline or a drift review is requested (add `- Note: reopen <reason> <date>` and reset the row to `[ ]`).
- If an already-aligned article carries unfixed gaps, they live in the row's Note — Step 1 only verifies them, it does not re-derive scope.
- When a batch completes → update the counts in this index and the overview in [`../TODO.md`](../TODO.md).
