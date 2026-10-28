# AUTOSAR Article Translation Progress

> Maintained by the autosar-translate skill per [STANDARD.md](STANDARD.md); update the touched entry and the `Last updated` date after every sync.
> Execution queue (the one-article-at-a-time order): [sync-todo/index.md](sync-todo/index.md) — this file is the status ledger, the queue is the execution order.
> Status: ✅ Type A-compliant · 🔶 Translated pending alignment · ⚠️ Partial · ⛔ Stub · ❌ Missing · 📖 Guide/topic (exempt from the skeleton)
> Baseline: R23-11 (`~/Workspace/autosar_standard/markdown/`) · Last updated: 2026-10-29

## Backlog

**Placeholder-section sweep (user decision 2026-10-28 — STANDARD.md §1 placeholder exception: a source section whose entire content is `None.`/`N.A.` is omitted entirely, no heading + lone 无/不适用 body; KeyM precedent, generalized to every section class)**

- [x] Sweep executed 2026-10-28, every omission verified against its R23-11 source before dropping; inbound anchors swept site-wide (zero cross-article inbound links to any renumbered anchor). Dropped: keym (`## 已知限制` 无。), crypto_driver (`### 4.1. 限制` 不适用 — source 4.1 "n.a."; `## 8. 时序图` 不适用。 — source ch.9 "n/a"; `## 9. 配置规范`→`## 8.` with 9.1.1–9.2 renumbered, `](#9`→`](#8` anchors), crypto_interface (`## 8. 时序图`; `## 9.`→`## 8.` + 9.x), memory_mapping (`#### 5.1.1. 代码文件结构` — source "Not applicable."; `## 8. 时序图`; `## 9.`→`## 8.` + 9.x; the 5 `[5.1.2]` links → `[5.1.1]`), platform_types (`#### 5.1.1. 代码文件结构` — source "None"; `### 7.1. 导入的类型` — source 8.1 "Not applicable."; `### 7.4`–`7.7` — source 8.4–8.7; `## 8. 时序图`; `## 9.`→`## 8.`; §7 renumbered 7.2→7.1/7.3→7.2 with all `#7xx` anchors shifted), standard_types (`### 7.3. 函数定义`, `## 8. 时序图`, `## 9. 配置规范` — all "Not applicable." in source), communication_stack_types (`### 7.2. 函数定义`, `## 8. 时序图`; `## 9.`→`## 8.` — source ch.10 real), watchdog_manager (`### 7.4. 回调通知` — source 8.4 "Not Applicable."; `#### 7.6.3. 可配置接口` — source 8.6.3; 7.5→7.4/7.6→7.5/7.7→7.6 renumbered incl. ##### depth, `#751-wdgm_mainfunction`→`#741-…` ×57), gpt_driver + icu_driver (`### 7.5. 调度函数` 无。 — source 8.5 "None."; 7.6→7.5 renumbered), iohwab (`### 3.2. 相关标准和规范` 无 — source "None"; `#### 7.8.3. 作业结束通知` 无; 3.3→3.2), port_driver (`#### 7.6.1. 强制接口` + `7.6.3. 可配置接口` 无 — source 8.6.1/8.6.3 "None"; 7.6.2→7.6.1), dio_driver (`#### 7.6.1. 强制接口` — source "None"; 7.6.2→7.6.1), operating_system (`#### 7.5.2. 类型定义` 无 — source 8.5.2 "None"; 7.5.3→7.5.2/7.5.4→7.5.3 renumbered, `#7541-iocinit`→`#7531-…`), time_service (`### 7.4. 回调通知` + `### 7.5. 调度函数` 无。 — source 8.4/8.5 "None."; 7.6→7.4 renumbered). Kept after source verification — NOT placeholders: adc_driver `#### 6.5.3–6.5.5` 无。 (source 7.5.3–5 are real prose "There are no transient faults." etc.); gpt/icu 7.4 回调通知 prose; platform_types `## 5` body 无。 (source ch.5 "None." intro under a chapter with real content); time_service `#### 7.4.3. 可配置接口` (source 8.6.3 = intro sentence + "None." — not a pure placeholder; article already carries both); memory_mapping/`## 7. API规范` 不适用 statements (mandatory skeleton chapter, STANDARD.md §3); all appendix-B 无 values (sanctioned form). Lone rte L14182 无。 left as-is (not a heading pattern). Bonus fix surfaced by the sweep: crypto_driver's two `RFC5280 第 [4.1](#41-限制) 节` links were external RFC5280 §4.1 references mistranslated into internal anchors — unlinking to plain text (an EXTERNAL link to RFC5280 §4.1 stays a user decision, check-8 class). Strict build: exit 0 / 0 WARNING / 0 anchor notices in touched files (26 pre-existing INFO notices in untouched files unchanged).

**TODO.md Overview count table drift (measured 2026-10-26)**

- [ ] The status-count table above does not match the per-section rows it summarizes: the rows hold 16 ✅ / 9 🔶 / 16 ⚠️ / 4 ⛔ / 7 📖, the table claims 14 / 10 / 17 / 4 / 8. The ✅ / ❌ counts were maintained per run (each new article bumps ✅ and lowers ❌ Missing), but the OS sync (ca7ecda) and the RTE run added rows without touching the table. Regenerate the table from the rows — a program-level fix, deliberately not folded into a single-article run.

**OS follow-up PR (user decision 2026-10-26 — deferred from the full-sync PR)**

- [ ] glossary.md: add the OS article's 46 §2.1 术语表 terms with 来源 attribution (one-term-once rule — check existing entries first); deferred because a parallel session was actively editing glossary.md during the run
- [ ] prose `[n]` citation link decisions for operating_system (census 2026-10-26): [3] Glossary → site glossary ×2 (SITE class); [1] SRS_OS, [2] ISO 17356-3, [4] SWS_BSWGeneral, [5] EXP_VFB, [6] SRS_BSWGeneral, [7] ISO 17356-6 → EXTERNAL class, need curated official URLs (check 8) before linking

- [x] ~~communication/index.md dead link~~ — fixed in this run (2026-10-27): the leftover link to can_network_management/r21_11 (page removed in 3e2fa4c) was deleted, clearing the strict-build WARNING

**Fill depth (existing articles)**

- [ ] 2026-10-25 tables-as-images retired (STANDARD.md §4 decision — source tables translate as GFM tables): 5 `![Table*.png]` refs remain — bswm 1 (Table7-1 BswMRuleInitState), dcm 1, data_distribution 1, time_service 2; EcuM ✅ (all 7 translated/deleted 2026-10-25), operating_system ✅ (Table7_1 deleted 2026-10-26, GFM table already present)
- [ ] 4 ⚠️ articles missing only the 「API规范」 chapter: pdu_router, can_interface, ethernet_interface, lin_interface (operating_system ✅ 2026-10-26; crypto_driver ✅ 2026-10-27 — its real gap was source 7.1.2–ch.10, not just the API chapter)
- [ ] The other 9 ⚠️ articles: complete their respective missing chapters (com_based_transformer, data_distribution, e2e_transformer, sec_oc, SoAd, mirror, dem, fee, dcm) — iohwab ✅ 2026-10-27; memory_access ✅ 2026-10-27
- [ ] 3 ⛔ stubs: full translation (ethernet_switch_driver, service_discovery, platform_types — platform_types also needs its front-matter title and nav label fixed in the same change); memory_mapping ✅ 2026-10-28
- [ ] 12 🔶 articles: align to Type A — flash_driver/time_service translate their legacy 「配置规范」 chapters in place (allowed since 2026-10-24; source ch.10 → article `## 8. 配置规范`); nvram drops the 「需求追踪」 chapter and fixes 「功能说明」; unify remaining legacy wording to STANDARD.md terms
- [ ] IO section ✅ articles' heading-wording alignment (DIO/Port/PWM/OCU/ICU done 2026-10-24; same-class deviations remain): adc 4.2 「适用车型域」→「汽车域的适用性」
- [ ] 4.2 「适用于汽车领域」→「汽车域的适用性」 (named in STANDARD.md 2026-10-24): bswm, ecu_state_manager, data_distribution (crypto_driver + crypto_service_manager ✅ 2026-10-27); 「对汽车领域的适用性」: ethernet_driver, can_interface; 「汽车领域的适用性」: nvram_manager
- [ ] *Scheduled functions* unified to 「调度函数」 (named in STANDARD.md 2026-10-24): bswm 7.3, crypto_service_manager 7.12 「Scheduled 函数」; can_network_management ✅ (2026-10-28, now 7.5)
- [ ] §3.1 translated in full as 「输入文件和相关标准与规范」 (direct translation, named in STANDARD.md 2026-10-25 — the short form 「输入文件」 is no longer canonical): dio ✅ (2026-10-25); remaining — exact 「输入文件」: adc, crypto_service_manager, ecu_state_manager, ethernet_interface, can_network_management (+ r21_11 snapshot), udp_network_management, flash_driver, flash_eeprom_emulation, pwm, port, icu, ocu, lin_interface, function_inhibition_manager, time_service; — iohwab removed 2026-10-27: its R23-11 source 3.1 heading is literally "Input documents", so 「输入文件」 IS the direct translation and stays 「输入文件及相关标准规范」: bulk_nv_data_manager, nvram_manager; 「输入文件及相关标准和规范」: bswm, pdu_router, operating_system
- [ ] Acronym chapters unified to 「粗体术语 + 引用块」 + row-set alignment (STANDARD.md §1; 2026-10-24 census 21:5): format — dio/port/pwm ✅ (reflowed 2026-10-24); lin_driver — 1 article still GFM tables; row sets (check line by line against the R23-11 sources) — adc restore API/HW/SW, DEM→DET source order, re-merge Conversion Mode into one entry (18 rows→16), lin_driver missing 14 rows (40→26); udp_network_management ✅ (2026-10-28, 25 entries); icu verified equal (12:12)
- [ ] Hygiene fixes: udp_network_management WeChat footer → `<h4>` ✅ (2026-10-28); dem numbering gap; rename the `data_distribution service` directory to drop the space; SoAd/mirror → index.md layout; `timimg_extension/indx.md` spelling (nav change in the same commit)
- [ ] BswM ch.10 → `## 9. 配置规范` (rule-lift follow-up, issue #71): 91 containers across ~3600 source lines (10.2.1–10.2.90) — dedicated run needed; bswm alignment + 时序图 lands first
- [ ] ch.10 → `## 8. 配置规范` for pre-ban articles whose R23-11 source has a Configuration specification (rule lifted 2026-10-24): io — dio/port/pwm ✅ (2026-10-24, issue #62), ocu ✅ (issue #61); remaining: audit every non-io ✅/🔶 article program-wide (bswm, ecu, crypto_*, memory_*, mode_management, system_services …); icu/adc rows already scope it in Group-io (iohwab ✅ 2026-10-27)
- [ ] Link-audit fixes (2026-10-24 first site-wide external-URL curl; rule in STANDARD.md §4 / skill Phase A check 8): ethernet_driver §3.2 IEEE `getieee802` PDF 403 (directory retired; verify the ieeexplore number for 802.1AS-2011 in a browser before re-linking — note ethernet_interface's ieeexplore 8585421 is 802.1AE MACsec, a different document); data_distribution §3 OMG `DDS/1.4` http 500 (https same path 200 → upgrade to https); `https://www.iso.org` 403 (likely anti-bot, verify in a browser before acting); port.de timed out once then returned 200 on retry (lesson recorded in check 8: retry before declaring a link dead)
- [ ] WdgM potential-link decisions (census 2026-10-26, report-only classes — apply is a user decision): cross-article module mentions — DEM ×6 → `../../diagnostics/diagnostic_event_manager/`, EcuM ×1 → `../ecu_state_manager/`, BswM ×1 → `../basic_software_mode_manager/` (Mcu ×14 and Det ×2 have no article yet); prose `[n]` citations — [4] *ECU 状态管理器规范* → SITE (EcuM article), [3] *基础软件模块通用规范* ×4 / [8] *MCU 驱动规范* / [9] *RTE 软件规范* / [1] IEC 61508 / [2] ISO 26262 → EXTERNAL, need curated official URLs (check 8) before linking
- [ ] DIO potential-link decisions (improved census 2026-10-25, report-only classes — apply is a user decision): 10 × PORT-driver module mentions (§1/§5.1/§6 prose, rendered **PORT**/**Port**) → `../port_driver/`; [1] Glossary → site glossary (§2 intro; SITE class); [2] SWS_BSWGeneral → EXTERNAL, needs a curated official URL (cited in §3.2 and §6.6 intro); 11 × STD_HIGH/STD_LOW mentions stay prose (no corpus precedent for enum-value links); Det ×6 mentions unlinked — no Det article yet (see fill-breadth below)
- [ ] EcuM PDF ground-truth census (2026-10-27, `link_candidates.py --list --pdf` — the source PDF's own hyperlinks read back; report-only classes, apply is a user decision): anchor-less targets — six §8.8 service-interface data types with 42 source links (`EcuM_UserType` ×11, `EcuM_TimeType` ×10, `EcuM_ShutdownTargetType` ×6, `EcuM_ShutdownModeType` ×6, `EcuM_ShutdownCauseType` ×5, `EcuM_BootTargetType` ×4; defined in the `§7.8.x.2 数据类型` tables, no identifier-titled heading — decide: promote to headings or leave unlinked), 14 config parameters (31 links; 配置规范 table rows, anchor-less by rule), port-interface codes E_OK/E_NOT_OK (37 links; table cells stay plain). ~~Content checks — 图7.15 / 图7.17 / 表7.9 … `EcuM_WakeupSourceType` 31 vs 29~~ → RESOLVED 2026-10-27 (mode_management census-fix run): 表7.7/7.8/7.9 captions added, 图7.15/7.17 numbers restored, leftover Table7-7.png ref + 9 orphan Table PNGs removed; the 31-vs-29 was a census counting bug (fixed). Citations: every `[n]` is `registry MATCH` ([23] = known source typo). BswM: ch.10 deferral explains all 33 anchor-less container/parameter targets (see the ch.10 row above); §6.8.2 [2]→[6] wrong-document citation FIXED. Corpus-wide: run `--pdf` on each ✅ row at its next touch — Gpt: `Gpt_Notification_<channel>` placeholder is anchor-less by nature, source §10.3 → 9.3 is the known renumbering artifact, Glossary `[1]` number inferred from the registry (link box misses the digits); DIO: clean
- [ ] Angle-bracket placeholder sweep (2026-10-27, STANDARD.md §4 + skill Phase A check 3): replace the broken `\<…\>` escaping with HTML entities `&lt;…&gt;` corpus-wide — python-markdown consumes `\>` but not `\<`, so every rendered `\<X\>` shows a stray `\` (found via `EcuM_SlaveCore\<X\>_Task`; EcuM article already fixed, 7 occurrences). Remaining 15 files / ~122 occurrences — iohwab ×53 (grew from ×23 when the R23-11 realignment PR #120 landed), pdu_router ×23, crypto_service_manager ×11, guide_to_mode_management ×9, pwm ×7, adc ×6, nvram ×4, gpt ×2, icu ×2, ethernet_interface ×2, com_based_transformer ×2, udp_nm/sec_oc/lin/SoAd ×1 each; **17 are in headings** (iohwab 6.1.x API names, com_based_transformer 5.x, udp_nm 7.3.1) — changing heading text changes Material slugs, so grep inbound `](…#…)` anchors site-wide and fix them in the same commit; never touch occurrences inside code fences/inline code

**Fill breadth (new articles)**

- [ ] Communication backbone: Com, CanSM, CanTp, TcpIp, Nm, EthSM, IpduM, SomeIpXf/SomeIpTp
- [ ] System services: ComM, Det (small; Det first)
- [ ] Global time cluster: StbM + CanTSyn/EthTSyn/FrTSyn
- [ ] Storage wrap-up: Ea, Eep
- [ ] Libraries: Crc, E2E
- [x] ~~Safety: WdgIf, Wdg~~ — done 2026-10-27 (wdgif + wdg run)
- [x] ~~Landing pages to add: crypto, memory, system_services, general, methodology_templates~~ — all present 2026-10-27 (general, system_services, methodology_templates plus foundation and template added in the Group-crypto batch run; crypto/memory earlier)

## Overview

| Status | Count | Note |
| --- | ---: | --- |
| ✅ Type A-compliant | 21 | ready to use |
| 🔶 Translated pending alignment | 8 | seven chapters present; legacy wording / forbidden-chapter residue |
| ⚠️ Partial | 16 | missing ≥1 chapter (most miss the 「API规范」 chapter) |
| ⛔ Stub | 4 | 9–19 lines only |
| ❌ Missing (SWS) | 78 | R23-11 has 127 SWS docs in total; 49 covered (38.6%) |
| ❌ Missing (EXP) | 16 | R23-11 has 22 EXP docs in total; 6 covered |
| 📖 Guide/topic | 8 | exempt from the Type A skeleton |

## communication

- ✅ [SPI Handler/Driver（SPI 处理器/驱动程序）](spi_handler_driver/) — SWS_SPIHandlerDriver (new article 2026-10-28, full Type A: ch.2 3 缩写+4 定义, §6 三级可扩展功能/IB-EB/错误分类, §7 11 types/14 functions/2 configurable callbacks/错误检测, §8 时序图 12 figures, §9 10 containers + 配置概念, §10 附录 example table; 22 figures; links applied)
- ✅ [CAN 网络管理](can_network_management/) — SWS_CANNetworkManagement (R23-11 realigned 2026-10-28: full §3.1 registry, §5/§6.11/§6.14–6.18/§7 completion, new §8 时序图/§9 配置规范/§10 示例)
- ✅ [UDP 网络管理](udp_network_management/) — SWS_UDPNetworkManagement (R23-11 realigned 2026-10-28: footer fixed, ch.2/§3 rebuild, §5/§6.8/§6.10–6.17/§7 completion, new §8 时序图和转换表/§9 配置规范, appendix B)
- ✅ [CAN 驱动](can_driver/) — SWS_CANDriver (R23-11 realigned 2026-10-28: former topic chapters folded into §2.1/2.2 per R23-11 structure; full §5–§9 completion)
- ✅ [CAN 收发器驱动](can_transceiver_driver/) — SWS_CANTransceiverDriver (R23-11 realigned 2026-10-28: ch.1 renamed 简介和功能概述 + §1.3 SAE J2411, §3 rebuilt to the R23-11 registry (6 refs) + §3.2 相关规范, §3.1 canonical heading, §4.1 rewritten/§4.2 汽车域的适用性 added, §5 依赖表 (7 modules) + §5.1 文件结构, §6.6 错误分类 (dev/runtime/transient/production/extended production) + §6.7–6.12 renumbering with new CAN XL 扩展 and 安全事件, §7 API rebuilt (7.1 导入的类型, 7.2 6 types, 7.3 15 functions, 7.4 2 scheduled functions, 7.5 回调通知, 7.6 必需/可选/可配置接口))
- 🔶 [以太网驱动](ethernet_driver/) — SWS_EthernetDriver (legacy wording)
- 🔶 [LIN 驱动](lin_driver/) — SWS_LINDriver (legacy wording)
- ⚠️ [CAN 接口](can_interface/) — SWS_CANInterface (missing 「API规范」)
- ⚠️ [COM 基转换器](com_based_transformer/) — SWS_COMBasedTransformer (missing 缩略语/dependencies)
- ⚠️ [数据分发服务](data_distribution%20service/) — SWS_DataDistributionService (missing 「API规范」; directory name contains a space, pending rename)
- ⚠️ [E2E 转换器](e2e_transformer/) — SWS_E2ETransformer (missing 缩略语/constraints/API)
- ⚠️ [以太网接口](ethernet_interface/) — SWS_EthernetInterface (missing 「API规范」)
- ⚠️ [LIN 接口](lin_interface/) — SWS_LINInterface (missing 「API规范」)
- ⚠️ [PDU 路由器](pdu_router/) — SWS_PDURouter (missing 「API规范」)
- ⚠️ [SecOC](sec_oc/) — SWS_SecureOnboardCommunication (missing 相关文档/API)
- ⚠️ [SoAd](SoAd/SoAd.md) — SWS_SocketAdaptor (missing 缩略语; directory capitalized, file name is not index.md)
- ⚠️ [Bus Mirror](mirror/mirror.md) — SWS_BusMirroring (missing 缩略语/API; file name is not index.md)
- ⛔ [以太网交换机驱动](ethernet_switch_driver/) — SWS_EthernetSwitchDriver (stub)
- ⛔ [服务发现](service_discovery/) — SWS_ServiceDiscovery (stub)
- 📖 [FvM 专题](fvm/fvm.md) — topic derived from SecOC appendix A (no standalone spec)
- 📖 [Full-CAN vs Basic-CAN](can_driver/full_can_vs_basic_can.md) — topic subpage
- 📖 [CanNm R21-11 历史版](can_network_management/r21_11/index_r21_11.md) — historical snapshot

❌ Missing (46): SWS_COM (Com), SWS_CANStateManager (CanSM), SWS_CANTransportLayer (CanTp), SWS_CANXLDriver, SWS_CANXLTransceiverDriver, SWS_TcpIp (TcpIp), SWS_SOMEIPTransformer (SomeIpXf), SWS_SOMEIPTransportProtocol (SomeIpTp), SWS_IPDUMultiplexer (IpduM), SWS_LargeDataCOM (LdCom), SWS_LSduRouter (LsDu), SWS_DiagnosticLogAndTrace (Dlt), SWS_DiagnosticOverIP (DoIp), SWS_XCP (XCP), SWS_EthernetStateManager (EthSM), SWS_EthernetTransceiverDriver (EthTrcv), SWS_WirelessEthernetDriver, SWS_WirelessEthernetTransceiverDriver, SWS_NetworkManagementInterface (Nm), SWS_FlexRayDriver, SWS_FlexRayInterface, SWS_FlexRayNetworkManagement, SWS_FlexRayStateManager, SWS_FlexRayTransceiverDriver, SWS_FlexRayARTransportLayer, SWS_FlexRayISOTransportLayer, SWS_LINStateManager (LinSM), SWS_LINTransceiverDriver (LinTrcv), SWS_TTCANDriver, SWS_TTCANInterface, SWS_SAEJ1939NetworkManagement (J1939Nm), SWS_SAEJ1939RequestManager (J1939Rm), SWS_SAEJ1939TransportLayer (J1939Tp), SWS_IEEE1722TransportLayer, SWS_MACsecKeyAgreement, SWS_CellularV2XDriver, SWS_ChargingManager, SWS_ChineseV2XManagement, SWS_ChineseV2XMessage, SWS_ChineseV2XNetwork, SWS_ChineseV2XSecurity, SWS_V2XBasicTransport, SWS_V2XDataManager, SWS_V2XFacilities, SWS_V2XGeoNetworking, SWS_V2XManagement

## crypto

- ⚠️ [Csm 加密服务管理器](crypto_service_manager/) — SWS_CryptoServiceManager (2026-10-27 wording alignment: 4.2 「汽车域的适用性」, 7.12 duplicate number fixed — Scheduled 函数 → 7.13 调度函数 (7.13.1 Csm_MainFunction); citation-marker anchors + identifier links applied; observation: API chapter still legacy-structured vs source ch.8 — realignment candidate for a future row; 2026-10-28 review: reopened as incomplete — source 7.3/7.4, 8.2 (14 types), 8.3.12, 8.4, 8.5, ch.9 and ch.10 (50 containers) are missing; mechanical defects fixed in place — see the Group-crypto.md row)
- ✅ [KeyM 密钥管理器](key_manager/) — SWS_KeyManager (new article 2026-10-28, full Type A: 已知限制 无, ch.2 7 entries, §3 [1]–[9], §5 三依赖小节, §6 加密密钥/证书子模块/自定义处理/安全事件/错误分类, §7 6 types/20 functions in 3 groups/2 scheduled/11 configurable interfaces + §7.8 服务接口 (10 data types, 8 C/S interfaces, 8 ports, EcuM house tables), §8 时序图 5 figures, §9 15 containers, appendix B 规范条目历史 as GFM tables with ids as data; 20 figures; links applied)
- ✅ [CryIf 加密接口](crypto_interface/) — SWS_CryptoInterface (new article 2026-10-27, full Type A: ch.2 9 acronyms + 12 terms, §6 多核/错误分类/错误检测, §7 2 types/18 functions in the source's 5 groups/1 callback/expected interfaces, §8 不适用 (source N/A), §9 5 containers incl. 变体; 5 figures; identifier/citation links applied)
- ✅ [Crypto 驱动](crypto_driver/) — SWS_CryptoDriver (2026-10-27 full R23-11 completion: the ⚠️ tag understated the gap — article stopped inside source 7.1.1; translated 7.1.2–7.5, ch.8 API (2 types/19 functions/4 NvBlock callbacks/MainFunction/expected interfaces), ch.9 n/a → §8 不适用, ch.10 16 containers → §9; §3 registry realigned to the R23-11 six entries; 17 figures; identifier/chapter-ref/citation links applied)

## diagnostics

- ⚠️ [Dcm 诊断通信管理器](diagnostic_communication_manager/) — SWS_DiagnosticCommunicationManager (intro + 缩略语 only; source ~24k lines)
- ⚠️ [Dem 诊断事件管理器](diagnostic_event_manager/) — SWS_DiagnosticEventManager (missing constraints/dependencies/API; has an unnumbered heading gap)

❌ Missing (1): SWS_SAEJ1939DiagnosticCommunicationManager (J1939Dcm)

## general

- 📖 [AUTOSAR 术语表（TR Glossary）](foundation/general/tr_glossary/) — AUTOSAR_FO_TR_Glossary（Foundation · R23-11）（2026-10-24 翻译中：ch.2 缩略语 206 条 ✅；ch.4 术语定义 343 条分批进行；内容并入术语表页）

- ✅ [Standard Types](../general/standard_types/) — SWS_StandardTypes (2026-10-27 full Type A translation from R23-11 replacing the 9-line stub: title fixed from the wrong "ECU State Manager" + mkdocs.yml nav label "EcuM" → "Standard Types"; §7 API = 7 type definitions + 5 symbol definitions + 函数定义 不适用, prose folds + literal bullets per the mcu/gpt style, Table 8.1 error codes as GFM; §8/§9 = 不适用 per source ch.9/10; appendix B 需求历史 with verbatim item-ID fences; Figure8-1 bit-layout extracted; source ch.5 "Software Architecture" → §5 软件架构 direct translation, empty 5.1 kept)
- ✅ [ComStack Types 通信栈类型](general/communication_stack_types/index.md) — SWS_CommunicationStackTypes (2026-10-27 full Type A translation from R23-11: new article + nav `"ComStack Types"`; ch.6 Requirements Tracing + appendix A dropped per mandate; ch.2 two tables → 13 blockquote entries (incl. the long OSEK/VDX row); ch.7 → §6 功能规格 (3 general reqs + 6.2 错误分类 5×"none" + 6.3 安全事件); ch.8 → §7 API规范 (14 types 7.1.1–7.1.14, 8.2 不适用 → §7.2); ch.9 不适用 → §8 时序图; ch.10 → §9 配置规范 (9.1 发布信息); 0 figures — all source images are page-chrome strips; glossary +13 terms incl. an API 来源 line)
- ✅ [BSW General（基础软件模块通用规范）](general/bsw_general/) — SWS_BSWGeneral (2026-10-27 full Type A translation from R23-11: new article — the foundation document cited as an input document by every module article; ch.6 Requirements Tracing dropped per mandate; source appendix "A Change History" is a change-history annex (not the droppable NA-requirements appendix) and translates as `## B. AUTOSAR 可追溯项变更历史` with item-ID lists verbatim in fences; ch.9 → `## 8. 时序图` (one-sentence chapter per source); ch.10 → `## 9. 配置规范` (template tables, no containers); 1 content figure; OS-services table (66 rows) kept as parsed from R23-11; check_api_sync 0==0)

- ✅ [Platform Types（平台类型）](general/platform_types/) — SWS_PlatformTypes (2026-10-27 full Type A translation from R23-11: new article in the directory the StandardTypes run vacated; §4 carries the source's third subsection 4.3 安全相关环境的适用性; §5 对其他模块的依赖 incl. 5.1 文件结构; §6 功能规格 = 6.1 一般问题 / 6.2 CPU类型 / 6.3 字节序 (6.3.1 位序 + 6.3.2 字节序, 3 endian figures extracted) / 6.4 优化的整数数据类型 / 6.5 布尔数据类型 (C99 _Bool usage fences) / 6.6 错误分类; §7 API = 7.1 导入的类型 不适用 / 7.2 类型定义 19 entries (boolean, uint8..sint64, *_least ×6, float32/64 IEEE 754-2008, VoidPtr/ConstVoidPtr) / 7.3 符号定义 4 entries (CPU_TYPE, CPU_BIT_ORDER, CPU_BYTE_ORDER, TRUE/FALSE #ifndef fences) / 7.4–7.7 不适用; §8/§9 = 不适用 per source ch.9/10.1; appendix B 可追溯项变更历史 with verbatim ID fences; reconstructions flagged: TRUE/FALSE fence tail + VoidPtr Description truncated in source)

## io

- ✅ [ADC 驱动](io/adc_driver/) — SWS_ADCDriver (pending wording alignment: 4.2 「适用车型域」)
- ✅ [DIO 驱动](io/dio_driver/) — SWS_DIODriver (2026-10-24 aligned 3.1/4.2 wording + acronym chapter reflowed to blockquotes; ch.10 → `## 9. 配置规范` translated (issue #62); ch.9 → `## 8. 时序图` translated + §9 config-class cells repaired 2026-10-24 (issue #65))
- ✅ [OCU 驱动](io/ocu_driver/) — SWS_OCUDriver (2026-10-24: 3.1 「输入文件」, §2 acronyms reflowed to blockquotes (13:13, source order incl. the duplicate MCU), source 4.1 Assumptions folded into the §4 intro (user decision); ch.10 → `## 9. 配置规范` translated (issue #61), §9 config-class cells repaired (issue #64); ch.9 → `## 8. 时序图` translated 2026-10-24 per the lifted sequence-diagram ban)
- ✅ [Port 驱动](io/port_driver/) — SWS_PortDriver (2026-10-24: translated the source ch.1 mapping table, §2 acronyms reflowed to blockquotes, 4.2 「汽车域的适用性」; content matches the R23-11 source chapter by chapter; ch.10 → `## 8. 配置规范` translated 2026-10-24, issue #62)
- ✅ [PWM 驱动](io/pwm_driver/) — SWS_PWMDriver (2026-10-24: acronym chapter reflowed to blockquotes (12:12, source order), 4.2 「汽车域的适用性」, removed the §7.2.8 `PWM_FULL_POWER (0x00)` row absent from the source table (user decision, issue #56); content matches the R23-11 source chapter by chapter; ch.10 → `## 8. 配置规范` translated 2026-10-24, issue #62; §8 config-class cells repaired 2026-10-24 (Post-build X + variant annotations restored, issue #64))
- ✅ [ICU 驱动](io/icu_driver/) — SWS_ICUDriver (2026-10-24 realigned to R23-11: 4.2 「汽车域的适用性」, 3.2/3.3 renamed to the site pattern; ## 8. 时序图 kept per the lifted ban; ## 9. 配置规范 translated (28 params); front-matter release R22-11 → R23-11 + glossary regenerated)
- ✅ [I/O 硬件抽象](io/iohwab/) — SWS_IOHardwareAbstraction (2026-10-27 full Type A realignment from R23-11: new §4 约束和假设, §3.2 相关标准和规范, §5.5 文件结构, §6.6 错误分类, §6.7 其他需求, §7.1 导入的类型, §7.2 类型定义, §7.5 调度函数, §7.8 期望接口, §9 配置规范; API chapter regrouped to source ch.8 (7.3–7.7) with every missing requirement paragraph translated; §2 rows restored 17/11/5 + 2.2 reordered; 功能规格 restructured 背景与原理/需求 with source nesting restored; sourceless 5.7 电源模式 dissolved into §8.2 per source ch.9; Figure5_1_1 table-as-image → GFM; 33 ch.2 terms to glossary)

## mcal

- ✅ [MCU 驱动](mcal/mcu_driver/) — SWS_MCUDriver (2026-10-26 full Type A translation from R23-11: new article + new MCAL section landing page + nav; ch.6 traceability dropped per mandate; ch.9 → `## 8. 时序图` (4 figures), ch.10 → `## 9. 配置规范` (10 containers, SWS 条目 cells filled with [ECUC_Mcu_*] per EcuM style); first inline cross-article prose links — Dem/Port)
- ✅ [GPT 驱动](mcal/gpt_driver/) — SWS_GPTDriver (2026-10-26 full Type A translation from R23-11: ch.6 tracing + appendix A dropped per mandate; ch.7 state diagrams → §6 (5 figures); ch.9 → `## 8. 时序图` (4 figures); ch.10 → `## 9. 配置规范` (7 containers); first real use of the 可配置接口 chapter 8.6.3; one source typo corrected — GptWakeupConfiguration included-cell → 唤醒通知 per gate decision)
- ✅ [CoreTest 内核测试](mcal/core_test/) — SWS_CoreTest (2026-10-26 full Type A translation from R23-11: ch.6 + ch.11 dropped per mandate; source 8.2/8.3/10.2.x unnumbered headings numbered by PDF-TOC order; ch.9 → `## 8. 时序图` (4 figures); ch.10 → `## 9. 配置规范` (7 containers); check_api_sync N/A — one of the 7 known `!` unparseable sources, verified manually against the R22-11 PDF)

## memory

- 🔶 [BndM](bulk_nv_data_manager/) — SWS_BulkNvDataManager (ch.1 is "介绍和功能概述")
- 🔶 [Flash 驱动](flash_driver/) — SWS_FlashDriver (contains "错误处理"; carries a legacy 「配置规范」 chapter — allowed since 2026-10-24, align per the config-spec rules)
- 🔶 [NvM](nvram_manager/) — SWS_NVRAMManager (contains the forbidden "需求追踪" chapter; "功能说明" legacy wording)
- ⚠️ [Fee](flash_eeprom_emulation/) — SWS_FlashEEPROMEmulation (missing constraints/dependencies)
- ✅ [AUTOSAR Memory Access（存储访问）](memory_access/) — SWS_MemoryAccess · R23-11 (2026-10-27 full Type A sync: §7 API规范 (31 types, 19 functions), §8 时序图 (7 diagrams), §9 配置规范, appendix B; 17 glossary terms added; source requirement tracing and Not applicable requirements omitted per STANDARD.md)
- ✅ [AUTOSAR Memory Mapping（AUTOSAR 内存映射）](memory_mapping/) — SWS_MemoryMapping · R23-11 (2026-10-28 full Type A sync: §1 简介和功能概述 + 5 用例, §2 缩略语 (4 terms), §3 相关文档 (13 inputs), §4 约束和假设, §5 对其他模块的依赖, §6 功能规格 (16 source tables 7.1–7.16), §7 API规范 (不适用), §8 时序图 (不适用), §9 配置规范 (7 containers), §10 分析 (3 tables 11.1–11.3), §11 引用的元类 (26 meta classes), appendix B; 14 figures; source requirement tracing and Not applicable requirements omitted per STANDARD.md)
- 📖 [NV 数据处理指南](nv_data_handling_guideline/) — EXP_NVDataHandling (exempt)

❌ Missing (6): SWS_EEPROMAbstraction (Ea), SWS_EEPROMDriver (Eep), SWS_MemoryAbstractionInterface, SWS_MemoryDriver, SWS_FlashTest (FlsTst), SWS_RAMTest (RamTst)

## mode_management

- ✅ [BswM](basic_software_mode_manager/) — SWS_BSWModeManager (2026-10-24: 4.2 → 「汽车域的适用性」, 7.3 → 「调度函数」, new ## 8. 时序图 (2 figures); ch.10 → `## 9. 配置规范` pending — 91 containers, issue #71)
- ✅ [EcuM](ecu_state_manager/) — SWS_ECUStateManager (2026-10-24: §4.2 → 汽车域的适用性, ## 8. 时序图 (16 figures) + ## 9. 配置规范 (~40 parameter tables); 2026-10-25 completion: ch.2 → 定义和缩略语 (2.1 定义 + 2.2 缩略语, mirrors the source split), new ## 已知限制, ## 7 completed with 7.1 导入的类型 / 7.2 类型定义 / 7.7 期望接口 / 7.8 端口接口规范 (source 8.1/8.2/8.7/8.8 had been missing), 调度表函数 → 调度函数, appendix B 可追溯项变更历史, §3.1 → 输入文件和相关标准与规范)
- 📖 [模式管理指南](guide_to_mode_management/) — EXP_ModeManagementGuide (exempt)

## system_services

- ✅ [Default Error Tracer（默认错误跟踪器）](default_error_tracer/) — SWS_DefaultErrorTracer (new article 2026-10-28, full Type A: 1 entry ch.2, §5.1 文件结构, §6 初始化/错误钩子/错误报告/错误分类, §7 API (1 type/6 functions/3 configurable callouts) + 服务接口 (DETService CSI + Det_<Name> 端口), §8 时序图 7 figures, §9 6 containers + 双 10.3/10.4 发布信息 (source quirk, both translated), appendix B 需求历史 with R22-11/R23-11 ID fences; identifier/citation links applied)
- ✅ [FiM（功能禁止管理器）](function_inhibition_manager/) — SWS_FunctionInhibitionManager (2026-10-28 realignment+completion: 功能规格 heading, 4.2 汽车域的适用性, §5 realigned to source ch.5 (bullets + 5.1 需求/5.1.1 用例), §7 API realigned to source ch.8 groups (导入的类型/FiM_ConfigType/3 interface groups with all requirement bodies/回调/调度/期望接口) + §7.4 服务接口 (2 CSIs, FiM_FunctionIdType, 2 ports, internal behavior), 6.5 错误分类 + 6.6 配置约束 added, §8 时序图 (figures moved from §6 to their source positions + 9.2 prose), §9 配置规范 6 containers + Figure10_1–10_4 config overviews, appendix B; 9 citation links; legacy ECUC_FiM_00037 prose mention kept)
- ✅ [时间服务](time_service/) — SWS_TimeService (2026-10-28 realignment+completion: §3 registry realigned to R23-11's 4 entries ([11]/[8] prose citations renumbered, stale [12]-[16] standards removed — release drift); 4.1 假设/4.2 限制 (renumbered)/4.3 汽车域的适用性; 6.4 got the 00063 intro + 6.4.3–6.4.5 + GFM error tables; 6.5 版本检查; Table 7.1 Predef-Timer characteristics converted from Table3.png to GFM (tables rule; Table3_1.png was a duplicate of an existing GFM table — dropped); §7 API realigned (7.1 导入的类型, 7.2 4 type entries, flat 7.3.1–7.3.20 kept = source 8.3 shape, 7.4 回调通知 无, 7.5 调度函数 无, 7.6 期望接口 2+1+None); ## 8. 时序图 (Figure9_1) + ## 9. 配置规范 (legacy per-param chapter replaced by the container-table house style, Tm+TmGeneral 6 params, Figure10_1) + appendix B; ch.2 heading 首字母缩略词、缩略语和术语 KEPT as the direct translation of the source heading (stale queue note wanted 缩略语 — decision recorded)
- ✅ [OS](operating_system/) — SWS_OS · R23-11 (2026-10-26 full sync: §2.1 术语表 46 terms added, ch.7 completed to source end (7.7.2–7.17 incl. multi-core/IOC/ARTI), new ## 7. API规范 (22 types + 39 functions + IOC/期望接口/钩子/服务接口), ## 8. 时序图 (8 figures), ## 9. 配置规范 (Os×35 + IOC×5 + ARTI×20 containers + 发布信息), ## 10–13 (生成/应用说明/服务/展望 — ch.11–14 顺延 per user decision), ## B. 约束和规格项的历史; §3.1 realigned to source's 11-entry list; spec: → AUTOSAR_CP_SWS_OS; Table7_1.png retired; 55 figures; glossary.md OS terms pending — parallel-session conflict)

❌ Missing (4): SWS_COMManager (ComM), SWS_DefaultErrorTracer (Det), SWS_HWTestManager, SWS_SoftwareClusterConnection (SwCluC)

## safety

- ✅ [WdgM 看门狗管理器](safety/watchdog_manager/index.md) — SWS_WatchdogManager (2026-10-26 full Type A translation from R23-11: new article + new safety section landing page + nav; ch.6 Requirements Tracing dropped per mandate, src ch.B *Not applicable requirements* dropped (the second droppable item); src ch.7 → §6 功能规格 (12 diagrams), src ch.8 → §7 API规范 (1 type + 10 functions + 期望接口 + 服务接口), src ch.9 → §8 时序图, src ch.10 → §9 配置规范 (21 containers, SWS 条目 cells filled with [ECUC_WdgM_*]); src annex A → §10 存活监督算法示例实现 (numbered continuation, 7 formulas restored from the R22-11 PDF); 35 figures; glossary.md extended by 36 terms + 6 来源 lines)
- ✅ [WdgIf 看门狗接口](safety/watchdog_interface/index.md) — SWS_WatchdogInterface (2026-10-27 full Type A translation from R23-11: new article + nav `"WdgIf"` + safety landing row; src ch.7 → §6 功能规格 (2 dev errors WDGIF_E_PARAM_DEVICE/POINTER), src ch.8 → §7 API规范 (1 type WdgIf_ModeType + 3 functions + 2 implementation-hint code fences), src ch.9 → §8 时序图 (bare cross-ref to the watchdog driver spec), src ch.10 → §9 配置规范 (3 containers, SWS 条目 cells filled with [ECUC_WdgIf_*]); 1 figure (Figure10-1 config tree); no glossary additions — source ch.2 is a no-local-acronyms note; WdgIf_SetMode error-code section links to the wdg article once both merged)
- ✅ [Wdg 看门狗驱动](safety/watchdog_driver/index.md) — SWS_WatchdogDriver (2026-10-27 full Type A translation from R23-11: new article + nav `"Wdg"` + safety landing row; src ch.7 → §6 功能规格 (5 subsections incl. 触发概念以支持窗口看门狗; 扩展生产错误 WDG_E_MODE_FAILED / WDG_E_DISABLE_REJECTED after mcu_driver house), src ch.8 → §7 API规范 (1 type Wdg_ConfigType + 4 functions), src ch.9 → §8 时序图 (Figure9-1/9-2), src ch.10 → §9 配置规范 (faithful source order incl. module table at the end + 9.2.2 WdgSettingsFast group; 17 ECUC tables with [ECUC_Wdg_*] cells); garbled WdgMaxTimeout description restored from the R22-11 PDF p.38; src app. B → ## B. fence-style per EcuM precedent; src ch.7.4 「(see Figure 2)」 kept as prose — Figure 2 absent in R22-11 PDF too; glossary.md +6 terms (DIP/Fast-Mode/Off-Mode/Slow-Mode/SPI/WDG) + DEM/DET 来源 lines)

## methodology_templates / template

- 📄 [BSW 模块描述模板](../methodology_templates/basic_software_module_description_template/) — TPS_BSWModuleDescriptionTemplate (exempt)
- 📖 [时序扩展示例](../template/timimg_extension/indx.md), [通用结构示例](../template/generic_structure/) — template examples (not synced)

## Missing sections (no articles at all)

- **GlobalTime (4)**: SWS_SynchronizedTimeBaseManager (StbM), SWS_TimeSyncOverCAN (CanTSyn), SWS_TimeSyncOverEthernet (EthTSyn), SWS_TimeSyncOverFlexRay (FrTSyn)
- **Libraries (9)**: SWS_CRCLibrary (Crc), SWS_E2ELibrary (E2E), SWS_BFXLibrary (Bfx), SWS_BSWMulticoreLibrary (Bmc), SWS_MFLLibrary (Mfl), SWS_MFXLibrary (Mfx), SWS_IFLLibrary (Ifl), SWS_IFXLibrary (Ifx), SWS_EFXLibrary (Efx)
- **RTE / SWArch (2)**: SWS_RTE, SWS_ARTI
- ~~**Safety (2)**: SWS_WatchdogInterface (WdgIf), SWS_WatchdogDriver (Wdg)~~ — both translated 2026-10-27
- **Security (2)**: SWS_Firewall, SWS_IntrusionDetectionSystemManager (IdsM)

## Missing EXP guides (15)

Translated 2026-10-28: LayeredSoftwareArchitecture → [general/layered_software_architecture](general/layered_software_architecture/) (📖 guide).

ApplicationInterfaces 1 (UserGuide), BSWGeneral 0, General 1 (VFB), SWArch 1 (ARTI), Safety 2 (FunctionalSafetyMeasures, SafetyUseCase), SystemServices 1 (SwClusterDesignAndIntegration)

Translated 2026-10-29: AIChassis → [application_interfaces/chassis](application_interfaces/chassis/) and AIHMIMultimediaAndTelematics → [application_interfaces/hmi](application_interfaces/hmi/), AIOccupantAndPedestrianSafety → [application_interfaces/occupant_safety](application_interfaces/occupant_safety/), AIPowertrain → [application_interfaces/powertrain](application_interfaces/powertrain/) (📖 guides).

## Suggested priority (2026-10-23 snapshot)

1. **Small-effort completions**: among the 17 ⚠️ articles, those missing only the 「API规范」 chapter (pdu_router, can_interface, crypto_driver, ethernet_interface, lin_interface, operating_system, …)
2. **Full stub translations**: the 4 ⛔ (platform_types also needs title + nav label fixed)
3. **Communication backbone**: Com, CanSM, CanTp, TcpIp, Nm, EthSM, IpduM, the SomeIp family
4. **System services**: ComM, Det (small)
5. **Alignment cleanup**: the 12 🔶 articles' legacy wording / forbidden chapters + known hygiene issues (space in a directory name, SoAd/mirror file names, indx.md spelling, platform_types title)
