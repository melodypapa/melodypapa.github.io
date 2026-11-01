# AUTOSAR translation queue — index

> Generated: 2026-10-24 · Base: R23-11 (`~/Workspace/autosar_standard/markdown/`)
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
| 2 | [Group-general.md](Group-general.md) | 4 | platform_types stub repair + BSWGeneral (global base spec) and 2 more missing documents |
| 3 | [Group-crypto.md](Group-crypto.md) | 4 | **batch complete 2026-10-28 (4/4)** — Csm alignment (PR #133) + crypto_driver full completion + CryIf/KeyM new articles; Csm reopened 2026-10-28 (incomplete) → full R23-11 re-sync complete 2026-10-31 |
| 4 | [Group-system_services.md](Group-system_services.md) | 7 | **4/7 done 2026-10-28** (operating_system + det + FiM + time_service) — remaining: ComM (giant, ~5.2k-line source), SwCluC, HwTestManager |
| 5 | [Group-mode_management.md](Group-mode_management.md) | 2 | EcuM alignment + BswM alignment (small) |
| 6 | [Group-diagnostics.md](Group-diagnostics.md) | 3 | Dem gaps + J1939Dcm + Dcm (24k-line source, giant — last) |
| 7 | [Group-memory.md](Group-memory.md) | 12 | **3/12 done 2026-10-31** (memory_access, memory_mapping, bulk_nv_data_manager PR #223) — remaining: Fee/NvM/Fls alignments + Ea/Eep… |
| 8 | [Group-communication.md](Group-communication.md) | 27 | 18 existing articles completed/aligned + 9 backbone documents (Com/CanSM/CanTp/TcpIp/Nm/EthSM/IpduM/SomeIp×2) |
| 9 | [Group-mcal.md](Group-mcal.md) | 3 | Mcu, Gpt, CoreTest |
| 10 | [Group-globaltime.md](Group-globaltime.md) | 4 | **batch complete 2026-10-31 (4/4)** — StbM + CanTSyn/EthTSyn/FrTSyn |
| 11 | [Group-libraries.md](Group-libraries.md) | 9 | Crc, E2E library and 7 more |
| 12 | [Group-safety.md](Group-safety.md) | 3 | WdgM/WdgIf/Wdg |
| 13 | [Group-security.md](Group-security.md) | 2 | Firewall, IdsM |
| 14 | [Group-rte-swarch.md](Group-rte-swarch.md) | 2 | RTE, ARTI |
| 15 | [Group-communication-2.md](Group-communication-2.md) | 38 | remaining communication gaps (CAN XL/LdCom/Dlt/DoIp/XCP/Spi/FlexRay/J1939/V2X…) |
| 16 | [Group-exp.md](Group-exp.md) | 20 | 20 missing EXP guides (the TPS template is exempt and not queued, same flow) |

Total 148 documents = all **127 R23-11 SWS** (io 7 + general 4 + crypto 4 + system_services 7 + mode_management 2 + diagnostics 3 + memory 12 + communication 65 + globaltime 4 + libraries 9 + mcal 3 + rte-swarch 2 + safety 3 + security 2, 1 of them already done) + **20 missing EXP** + 1 TPS template (exempt, not queued — see Group-exp). Batch order is adjustable; row order inside a batch = suggested execution order (small/alignment work first, giant sources last).

## Rules

- **One document per run**: take one row, run all 6 steps (including the user confirmation gate), flip the row + its sub-checklist, record the commit hash, then stop (autosar-translate SKILL.md Steps 7/8).
- **A `[x]` row is never reopened** unless the user changes the baseline or a drift review is requested (add `- Note: reopen <reason> <date>` and reset the row to `[ ]`).
- If an already-aligned article carries unfixed gaps, they live in the row's Note — Step 1 only verifies them, it does not re-derive scope.
- When a batch completes → update the counts in this index and the overview in [`../TODO.md`](../TODO.md).
