# 已完成译文核验清单 (Finished Translation Verification Checklist)

> Working file — excluded from the site build (`exclude_docs: autosar/sync-todo/` in `mkdocs.yml`). This is a verification worklist, **not** a status ledger; [`../TODO.md`](../TODO.md) remains the single source of truth for article status, doc IDs and per-article sync notes.
> Collected: 2026-11-06 from `../TODO.md`; regenerated after the `origin/master` sync (HEAD `458e6d5`, PR #295 rte-swarch-batch).
> Scope (user choice): every row marked ✅ Type A-compliant or 📖 Guide/topic — **166 finished articles** (162 ✅ + 4 📖), all unique and all paths resolving. Regenerated 2026-11-06 after the F1–F4 ledger cleanup and the `origin/master` sync (PR #295 added the RTE / ARTI SWS rows).
> The ledger is a moving target (a parallel translation session keeps syncing) — regenerate from `../TODO.md` if the counts change again.
> Paths below carry a `../` prefix (relative to this `sync-todo/` directory); in `../TODO.md` the same paths are relative to `docs/autosar/`.

## How to use

Each article line has three boxes: the leading `- [ ]` = article fully verified; `内容 [ ]` = goal 1; `链接 [ ]` = goal 2. Tick `[ ]` → `[x]` and record every defect in the Findings log at the bottom with the article path.

## Goal 1 — verify the content is completed and consistent

Per article. The chapter-skeleton checks apply to CP module articles only; `foundation/` articles and 📖 pages are skeleton-exempt per STANDARD.md §7.

- [ ] 7-chapter skeleton present with continuous numbering: `## 1. 简介和功能概述` … `## 7. API规范`, plus optional `## 8. 时序图` / `## 9. 配置规范` / `## 10.+` numbered continuation chapters (STANDARD.md §1)
- [ ] No forbidden content: 需求可追溯性 / 需求追踪 chapter, droppable appendix A (*Not applicable requirements*), placeholder-only sections (`None.` / `N.A.`) — every omission is reported in the queue row and PR text, never silent
- [ ] Canonical chapter wording (STANDARD.md §2): 简介和功能概述 · 缩略语 / 定义和缩略语 · 相关文档 → 输入文件和相关标准与规范 + 相关规范 · 约束和假设 → 限制 + 汽车域的适用性 · 对其他模块的依赖 · 功能规格 · API规范 → 函数定义 / 调度函数 / 回调通知 / 可配置接口
- [ ] `## 7. API规范` never missing; each function `#### 7.1.x. <name>` + `**说明**:` + ```C block; `服务 ID 0xNN` retained; one-sentence no-callback statement instead of an omitted chapter
- [ ] Formatting (STANDARD.md §4): front-matter `title` is the only h1 (no `# ` in body); heading level = numeric depth + 2; English terms bolded; code identifiers untranslated; every `###`+ heading title translated; `<…>` placeholders as `&lt;…&gt;`; no source requirement IDs / `{DRAFT}`; source tables as GFM (never `![Table*.png]`); WeChat footer as `<section id="wechat">` + `<h4>`
- [ ] Faithful to the R23-11 source (`~/Workspace/autosar_standard/markdown/Classic_Platform/...` for CP, `.../Foundation/...` for FO) — check the **SWS**, not the SRS, before flagging a translation as wrong
- [ ] Cross-cutting consistency: new terms carry 来源 attribution in [`../glossary.md`](../glossary.md) (one term translated once); front-matter `spec:` / `release:` consistent; `cp/api/` regenerated after API-chapter changes
- [ ] Automated helpers (`.agents/skills/autosar-translate/scripts/`): `check_heading_lang.py --site` → 0 violations; `check_indexes.py` (+ `--titles`) → 0 violations; `check_api_sync.py` per article

## Goal 2 — check potential link problems

- [ ] Strict build is the gate: `/tmp/mkdocs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/mkdocs-check` must exit 0 with **zero WARNINGs**. Pre-existing INFO-level anchor notices do not fail `--strict` — read them explicitly from the build log.
- [ ] Same-page broken anchors surface only as INFO — enumerate them from the build log rather than assuming a green build means no broken anchors.
- [ ] "Unrecognized relative link `dir/`" INFO notices are left as-is by MkDocs — decide per case whether to append `index.md`.
- [ ] External URLs curl-checked (2xx/3xx pass; a 4xx from a known anti-bot host is verified manually in a browser, never auto-removed); links come only from the source document or the site itself — no invented references.
- [ ] Cross-article anchors after heading renames / chapter renumbering; landing-page link lists complete (`check_indexes.py`); `redirect_maps` covers old pre-move URLs.
- [ ] Every finished article registered in `mkdocs.yml` nav; no stale nav entries pointing at deleted pages.

## Pre-check findings (baseline 2026-11-06, strict build exit 0 / zero WARNINGs)

Automated checks already run. Work these first — they are the concrete "potential links" and ledger inconsistencies.

### Build INFO notices (4)

- [x] `foundation/communication_management/index.md` — unrecognized relative link `exp_time_sensitive_network_features/` (did you mean `exp_time_sensitive_network_features/index.md`?) — **resolved 2026-11-06**
- [x] `foundation/release_documentation/index.md` — unrecognized relative link `tr_release_overview/` — **resolved 2026-11-06**
- [x] `foundation/security/index.md` — unrecognized relative link `tr_list_of_known_issues_secure_hardware_extensions/` — **resolved 2026-11-06**
- [x] `cp/communication/v2x_datamgr/index.md` — link `#774-v2xdm_callback_stack_msg_type` has no such anchor on that page (broken intra-page link) — **resolved 2026-11-06**

### Ledger inconsistencies (4)

- [x] **F1** Duplicate `## security` section in `../TODO.md` — `Firewall（防火墙）` / `cp/security/firewall/` listed twice; deduped to one row below, ledger still needs the duplicate removed. — **resolved 2026-11-06**
- [x] **F2** `CanNm R21-11 历史版` (📖) links to `cp/communication/can_network_management/r21_11/index_r21_11.md` — the file does not exist anywhere under `docs/`; the page was removed in `3e2fa4c` (see Backlog note). Remove or re-point the row. — **resolved 2026-11-06**
- [x] **F3** `时序扩展示例 / 通用结构示例` (📖) links to `cp/template/timimg_extension/` and `cp/template/generic_structure/` — both deleted 2026-11-04; `cp/template/` now holds only `index.md`. Remove the stale row. — **resolved 2026-11-06**
- [x] **F4** Overview count table in `../TODO.md` (line 82) is stale: claims 27 ✅, actual 161 ✅; already flagged in Backlog line 18 — regenerate the table from the rows. — **resolved 2026-11-06**

## Verification results (2026-11-06, read-only pass)

> This table and the A/B/C findings below record the **original** read-only pass, before the F1–F4 / B1 / A4 fixes and before the `origin/master` sync. For the current state see **Post-sync verification** below.

Scope: 166 finished articles, all paths resolving. 114 CP module articles are subject to the Type A skeleton; 52 are skeleton-exempt (`foundation/`, guides, templates). Per-article boxes below stay unticked until each article is read against its source; the program-wide results are recorded here.

| Check | Tool | Result |
| --- | --- | --- |
| Strict build | `mkdocs build --strict` | EXIT 0, zero WARNINGs, 4 INFO notices |
| Index / nav integrity | `check_indexes.py` | OK — 330 nav targets, 238 tab pages, 32 landing pages, 0 broken links |
| Title structure | `check_indexes.py --titles` | 5 violations (report-only, exit 0) |
| Heading language | `check_heading_lang.py --site` | 1 flagged → **false positive** (identifier-titled API heading, exempt §4); effectively 0 defects |
| Front-matter `title` | program scan | 166/166 present |
| `# ` h1 in body | program scan | 0 |
| Forbidden chapters (需求可追溯性 / appendix A / placeholders) | program scan | 0 |
| Tables as images (`![Table*.png]`) | program scan | 0 |
| `{DRAFT}` markers | program scan | 0 |
| Chapter skeleton (7 core chapters + canonical wording) | program scan | 13 deviations |
| Chapter numbering continuity | program scan | 2 gaps |
| File existence | path scan | 166/166 resolve |
| External URLs | curl | 175 checked (+8 XML-namespace identifiers excluded); 43 remain non-pass |

`check_api_sync.py` was **not** run — it is a per-document-pair Phase B check (`<source.markdown> <article-index.md>`); the R23-11 source corpus is present at `~/Workspace/autosar_standard/markdown/`, so it is queued for the per-article pass.

## Post-sync verification (2026-11-06)

Re-run after fast-forwarding to `origin/master` (`458e6d5`, PR #295 rte-swarch-batch) and reconciling the derived files:

| Check | Result |
| --- | --- |
| Strict build | **EXIT 0, zero WARNINGs, zero INFO link notices** (all 4 original notices resolved) |
| `check_indexes.py` | OK — 331 nav targets, 239 tab pages, 32 landing pages, 0 broken links |
| `check_indexes.py --titles` | **0 violations** |
| `check_heading_lang.py --site` | 1 flagged → `Mfl` identifier false positive (A5), unchanged |
| Front-matter `title` | 166/166 present |
| `# ` h1 in body | 0 — the 3 matches in `sw_arch/arti_sws/index.md` are `# define` C preprocessor lines inside code fences, not headings |
| Forbidden chapters / tables-as-images / `{DRAFT}` | 0 / 0 / 0 |
| File existence | 166/166 resolve |
| Chapter deviations | **14** (13 original + RTE, below) |
| Numbering gaps | **3** (2 original + RTE, below) |

**New from PR #295 (2 articles, both marked ✅ in the ledger):**

- `cp/rte/rte/index.md` — no `## 7. API规范` chapter; chapters are `[1,2,3,4,5,6,8]`. This is a **documented, gated deviation** in `../TODO.md`: "ch.5/6 material sits at `#### 7.1/7.2` inside the §6.3 tree with no `## 7. API规范` chapter — original run kept all headings ≤ h6". Not a regression introduced by this sync; recorded here so the per-article pass knows about it.
- `cp/sw_arch/arti_sws/index.md` — clean apart from the 3 C-preprocessor false positives above.

`cp/api/` was regenerated from the merged state (2679 function entries preserved; also fixed the stale `cp/api/index.md` count from 2677 → 2679 / 118 → 119 articles, which PR #295 had left behind). F4 ✅ recounted 160 → 162.

### A. Content consistency findings (Goal 1)

**A1/A2 — chapter heading deviations (14 articles, 16 headings; the 14th is RTE, added by the post-sync re-audit).** All need source verification per STANDARD.md §5 before being called wrong: most ch.2 titles are *direct translations of the source heading* (e.g. *Acronyms and abbreviations* → 缩略语和简称), which conflicts with the canonical `缩略语` rule in §2. This needs a site-wide wording decision, not a mechanical edit.

| Article | Deviation |
| --- | --- |
| `cp/communication/can_driver/index.md` | `## 6. 功能规范` (canonical 功能规格) |
| `cp/communication/com/index.md` | `## 2. 缩略语、缩写和定义` |
| `cp/communication/ieee1722tp/index.md` | `## 2. 缩略语和定义` |
| `cp/communication/flexray_interface/index.md` | `## 2. 缩略语和简称` |
| `cp/communication/flexray_network_management/index.md` | `## 2. 缩略语和简称` |
| `cp/communication/flexray_state_manager/index.md` | `## 2. 缩略语和简称` |
| `cp/communication/flexray_transceiver_driver/index.md` | `## 2. 缩略语和简称` |
| `cp/communication/flexray_ar_transport_layer/index.md` | `## 2. 缩略语和缩写`; `## 6. 对其他模块的依赖`; `## 7. 功能规格`; ch.5 absent |
| `cp/communication/flexray_iso_transport_layer/index.md` | `## 2. 缩略语和缩写` |
| `cp/general/standard_types/index.md` | `## 5. 软件架构` (canonical 对其他模块的依赖) |
| `cp/system_services/time_service/index.md` | `## 2. 首字母缩略词、缩略语和术语` |
| `cp/system_services/comm/index.md` | `## 2. 缩略语和定义` |
| `cp/system_services/software_cluster_connection/index.md` | `## 2. 缩略语和缩写` |
| `cp/rte/rte/index.md` | `## 7. API规范` **missing** (post-sync; documented gated deviation, PR #295) |

**A3 — numbering gaps (3).** `flexray_ar_transport_layer`: chapters `[1,2,3,4,6,7,8,9,10]` — ch.5 dropped without renumbering (§1 placeholder rule requires the surviving chapter to take the lower number). `memory_mapping`: `[1..8,10,11]` — ch.9 dropped without renumbering. `rte/rte`: `[1,2,3,4,5,6,8]` — ch.7 absent (post-sync; documented gated deviation, PR #295).

**A4 — title structure (5).** `check_indexes.py --titles` flags Chinese-first bilingual titles, against the site-wide `English（中文）` rule (TODO.md Backlog 2026-10-29): `flexray_interface`, `flexray_network_management`, `flexray_state_manager`, `flexray_transceiver_driver`, `flexray_ar_transport_layer`. Renaming ripples to nav labels, index pages, glossary 来源 lines and `cp/api/` entries — do not edit without that sweep.

**A5 — script false positive (1, no action).** `check_heading_lang.py --site` flags `cp/libraries/mfl/index.md:2501` `##### 7.5.18.3. Mfl`, but `Mfl` is the **function name** (C signature `<OutType> Mfl ( float32 ValFloat )`) — identifier-titled headings are exempt (STANDARD.md §4). The script's exemption regex should be widened to module-prefix identifiers; the article is correct.

### B. Link findings (Goal 2)

**B1 — the 4 build INFO notices have exact, low-risk fixes:**

| File | Fix |
| --- | --- |
| `foundation/communication_management/index.md:9` | `(exp_time_sensitive_network_features/)` → `(exp_time_sensitive_network_features/index.md)` |
| `foundation/release_documentation/index.md:9` | `(tr_release_overview/)` → `(tr_release_overview/index.md)` |
| `foundation/security/index.md:11` | `(tr_list_of_known_issues_secure_hardware_extensions/)` → `(tr_list_of_known_issues_secure_hardware_extensions/index.md)` |
| `cp/communication/v2x_datamgr/index.md:399,476` | `#774-v2xdm_callback_stack_msg_type` → `#774-v2xdm_callback_stackmsgtype` (actual Material slug, confirmed in built HTML) |

Every other Foundation landing page already uses `slug/index.md` — the 3 above are the outliers.

**B2 — external URLs.** 183 unique URLs (8 XML-namespace / `&lt;` placeholders excluded as non-links). Markdown `\_` escapes and parenthesised URLs were normalised before a second curl pass; 4 were extraction artifacts and now pass. 43 remain non-pass:

- **18 × `000` connection failures** — mostly live hosts (wikipedia, wikibooks, nist.gov, source.android.com, arb.ca.gov); almost certainly sandbox/network restrictions, **not confirmed dead links**. `en.wikipedia.org/wiki/Redundancy_(engineering` was truncated by the extractor, not by the article.
- **10 × `403` + 3 × `418`** — anti-bot hosts (`iso.org`, `ieeexplore.ieee.org`, `doi.org`, `acm.org`, `standards.ieee.org`, `community.arm.com`, `community.infineon.com`, `researchgate.net`, `avnu.org`, `1.ieee802.org`). Per STANDARD.md §4 these must be **verified manually in a browser and never auto-removed**.
- **7 × `404`** — `dslab.epfl.ch/proj/cpi/`, `bsi.bund.de` ×2, `www.grammatech.com/products/codesonar`, `www.autosar.org/fileadmin/ABOUT/AUTOSAR_Introduction.pdf`, `www.iana.org/.../bootp-dhcpparameters.xhtml`, `www.msr-wg.de/.../msrsw_v230-eadoc-`. The last two are **source-faithful truncations/typos in the standard's reference list** (`tps_xml_schema_production_rules`, `tcpip`) — links come only from the source, so verify against R23-11 before any change.
- **5 × `500`** — legacy `www.omg.org/cgi-bin/apps/doc?formal/...` / `?ptc/...` endpoints in `tps_xml_schema_production_rules` and `tps_arxml_serialization_rules` reference lists — server-side errors, manual browser verification.

Raw per-URL results: `/tmp/url-check.tsv`. Run-to-run variance (a few URLs flip `000` ↔ `200`) means treat this as advisory, not authoritative.

**B3 — ledger link defects** are F2/F3 above; F1 and F4 are count/duplicate hygiene.

### C. Verified NOT defects

- `mfl` `Mfl` heading (A5) — exempt identifier.
- 403/418 anti-bot responses and 000 connection failures — not reasons to delete a link.
- Truncated reference-list URLs (`msr-wg.de`, `svn3.autosar.org`) — preserved verbatim from the R23-11 source.
- 0 h1 / 0 forbidden chapters / 0 tables-as-images / 0 DRAFT across all 166 articles checked in the read-only pass.

## Source-check results (2026-11-06, A1–A3)

Method: for each of the 13 articles the R23-11 SWS source (`~/Workspace/autosar_standard/markdown/Classic_Platform/Releases/R23-11/**/<spec>.md`) was read and its `## N <title>` chapter list compared with the article's `## N. <title>`.

**Numbering caveat:** every source drops ch.6 *Requirements Tracing* (mandate) and the article renumbers source 7→6, 8→7, 9→8, 10→9. A naive chapter-number alignment therefore looks "shifted" but is correct; only wording and genuine gaps matter.

### 11 × source-faithful ch.2 titles — a rule conflict, not drift

Each is a direct translation of its own source chapter-2 heading:

| Article | Source ch.2 | Article ch.2 |
| --- | --- | --- |
| `com` | Acronyms, Abbreviations, and Definitions | 缩略语、缩写和定义 |
| `ieee1722tp` | Acronyms, Abbreviations and Definitions | 缩略语和定义 |
| `flexray_interface` | Acronyms and Abbreviations | 缩略语和简称 |
| `flexray_network_management` | Acronyms and Abbreviations | 缩略语和简称 |
| `flexray_state_manager` | Acronyms and Abbreviations | 缩略语和简称 |
| `flexray_transceiver_driver` | Acronyms and Abbreviations | 缩略语和简称 |
| `flexray_iso_transport_layer` | Acronyms and abbreviations | 缩略语和缩写 |
| `time_service` | Acronyms, abbreviations and terms | 首字母缩略词、缩略语和术语 |
| `comm` | Acronyms and definitions | 缩略语和定义 |
| `software_cluster_connection` | Acronyms and abbreviations | 缩略语和缩写 |
| `flexray_ar_transport_layer` | *(source heading corrupted — see below)* | 缩略语和缩写 |

`can_driver` is the counter-example: source "Acronyms and Abbreviations" → canonical `缩略语`. STANDARD.md §2 fixes `缩略语` / `定义和缩略语` site-wide, while §4 requires every heading to be a direct translation of its source heading — **the two rules conflict**. Recommended resolution: amend STANDARD.md §2 with a decision-log entry to permit source-faithful ch.2 titles as a sanctioned variant, **or** align all 11 to canonical wording with an inbound-anchor sweep. Awaiting the user's decision; no article was changed.

### 2 × genuine drift / skeleton conflict

- `can_driver` `## 6. 功能规范` — source "Functional Specification"; §2 explicitly forbids 功能规范 and requires 功能规格. Fix: rename + anchor sweep.
- `standard_types` `## 5. 软件架构` — source ch.5 is literally "Software Architecture" (this SWS has no *Dependencies to other modules* chapter). Faithful to source but conflicts with the mandatory ch.5 in §1. Needs a documented §7-style exemption or a decision, not a mechanical rename.

### 2 × genuine renumbering failures (A3)

Both keep source chapter numbers after dropping a source chapter, so the article numbering is not continuous:

- `flexray_ar_transport_layer`: source ch.6 *Requirements traceability* dropped, source ch.5 *Dependencies to other modules* rendered as article `## 6.`, and source ch.7–10 kept as article 7–10 → gap at 5. Should be 5/6/7/8/9.
- `memory_mapping`: source ch.6 *Requirements traceability* and ch.9 *Sequence diagrams* both dropped, but source ch.11 *Analysis* / ch.12 *Referenced metaclasses* kept as article 10/11 → gap at 9. Should be 9/10.

Both require an intra-page anchor sweep (STANDARD.md §4) — do not renumber without it.

**Corrupted source heading:** `flexray_ar_transport_layer` ch.1/ch.2 extract as "Byte Addressing Not compliant to ISO 15765-2" (a PDF-extraction artifact), so its ch.2 wording cannot be source-verified.

## Resolution log (2026-11-06)

Applied in this session:

- **B1** — 3 Foundation landing pages now link `…/index.md`; `v2x_datamgr` anchors re-pointed to `#774-v2xdm_callback_stackmsgtype`. All 4 build INFO notices should now be gone.
- **F1–F3** — duplicate `## security` section and the 2 stale 📖 rows removed from `../TODO.md`.
- **F4** — Overview status rows regenerated from the rows (✅ 160 / 🔶 6 / ⚠️ 1 / ⛔ 0 / 📖 4); the 3 queue-derived Missing rows documented rather than fabricated; Backlog item marked done.
- **A4** — 5 FlexRay titles renamed to `English（中文）`; propagated to `cp/index.md`, `cp/communication/index.md`, `../TODO.md` and this checklist; `cp/api/` regenerated via `gen_api_list.py`. `check_indexes.py --titles` → 0 violations.
- Checklist regenerated from the merged ledger: **166 articles, 24 sections, all paths resolving**; F4 ✅ recounted to 162; `cp/api/` regenerated from the merged state.

Deferred / awaiting a decision:

- **A1–A3** — the source-check classification above; no article changed (user chose "check sources first").
- **B2** — 43 external URLs need manual browser verification; anti-bot 403/418 must never be auto-removed; 7×404 / 5×500 are source-faithful legacy references.
- **A5** — widen `check_heading_lang.py`'s identifier exemption for module-prefix function names (`Mfl`).
- **Per-article read-through** — the 166 `- [ ]` boxes remain unticked; `check_api_sync.py` is a per-document-pair Phase B check and is queued for that pass.

## Articles (166)

### communication（61 篇）

- [ ] [V2X Management（V2X管理）](../cp/communication/v2x_mgmt/) — 内容 [ ] · 链接 [ ]
- [ ] [V2X GeoNetworking（V2X地理网络）](../cp/communication/v2x_geonet/) — 内容 [ ] · 链接 [ ]
- [ ] [V2X Facilities（V2X设施层）](../cp/communication/v2x_facilities/) — 内容 [ ] · 链接 [ ]
- [ ] [V2X Data Manager（V2X数据管理器）](../cp/communication/v2x_datamgr/) — 内容 [ ] · 链接 [ ]
- [ ] [V2X Basic Transport（V2X基本传输协议）](../cp/communication/v2x_basictp/) — 内容 [ ] · 链接 [ ]
- [ ] [Chinese V2X Security（中国V2X安全）](../cp/communication/chinesev2x_sec/) — 内容 [ ] · 链接 [ ]
- [ ] [Chinese V2X Network（中国V2X网络）](../cp/communication/chinesev2x_net/) — 内容 [ ] · 链接 [ ]
- [ ] [Chinese V2X Message（中国V2X消息）](../cp/communication/chinesev2x_msg/) — 内容 [ ] · 链接 [ ]
- [ ] [Chinese V2X Management（中国V2X管理）](../cp/communication/chinesev2x_mgmt/) — 内容 [ ] · 链接 [ ]
- [ ] [Charging Manager（充电管理器）](../cp/communication/chargingmanager/) — 内容 [ ] · 链接 [ ]
- [ ] [Cellular V2X Driver（蜂窝V2X驱动程序）](../cp/communication/cellularv2x_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [FlexRay Driver（FlexRay 驱动程序）](../cp/communication/flexray_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](../cp/communication/wlan_transceiver_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [Wireless Ethernet Driver（无线以太网驱动程序）](../cp/communication/wlan_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [Ethernet Transceiver Driver（以太网收发器驱动程序）](../cp/communication/eth_trcv/) — 内容 [ ] · 链接 [ ]
- [ ] [CAN XL Transceiver Driver（CAN XL 收发器驱动程序）](../cp/communication/canxl_transceiver_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [CAN XL Driver（CAN XL 驱动程序）](../cp/communication/canxl_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [XCP（通用校准协议）](../cp/communication/xcp/) — 内容 [ ] · 链接 [ ]
- [ ] [DoIP（基于 IP 的诊断）](../cp/communication/diagnostic_over_ip/) — 内容 [ ] · 链接 [ ]
- [ ] [Dlt（诊断日志与跟踪）](../cp/communication/diagnostic_log_and_trace/) — 内容 [ ] · 链接 [ ]
- [ ] [L-SDU Router（链路层 SDU 路由模块）](../cp/communication/lsdu_router/) — 内容 [ ] · 链接 [ ]
- [ ] [Large Data COM（大数据 COM）](../cp/communication/large_data_com/) — 内容 [ ] · 链接 [ ]
- [ ] [SPI Handler/Driver（SPI 处理器/驱动程序）](../cp/communication/spi_handler_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [CAN 网络管理](../cp/communication/can_network_management/) — 内容 [ ] · 链接 [ ]
- [ ] [UDP 网络管理](../cp/communication/udp_network_management/) — 内容 [ ] · 链接 [ ]
- [ ] [CAN 驱动](../cp/communication/can_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [CAN 收发器驱动](../cp/communication/can_transceiver_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [COM 基转换器](../cp/communication/com_based_transformer/) — 内容 [ ] · 链接 [ ]
- [ ] [数据分发服务](../cp/communication/data_distribution/) — 内容 [ ] · 链接 [ ]
- [ ] [E2E 转换器](../cp/communication/e2e_transformer/) — 内容 [ ] · 链接 [ ]
- [ ] [以太网接口](../cp/communication/ethernet_interface/) — 内容 [ ] · 链接 [ ]
- [ ] [LIN 接口](../cp/communication/lin_interface/) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR LinSM（LIN 状态管理器）](../cp/communication/linsm/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR LinTrcv（LIN 收发器驱动程序）](../cp/communication/lintrcv/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR TTCAN Driver（TTCAN 驱动程序）](../cp/communication/ttcan_driver/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR TTCAN Interface（TTCAN 接口）](../cp/communication/ttcan_interface/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR J1939Nm（SAE J1939 网络管理）](../cp/communication/j1939nm/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR J1939Rm（SAE J1939 请求管理器）](../cp/communication/j1939rm/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR J1939Tp（SAE J1939 传输层）](../cp/communication/j1939tp/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](../cp/communication/ieee1722tp/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR Mka（MACsec 密钥协商）](../cp/communication/macsec/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [PDU 路由器](../cp/communication/pdu_router/) — 内容 [ ] · 链接 [ ]
- [ ] [SecOC](../cp/communication/sec_oc/) — 内容 [ ] · 链接 [ ]
- [ ] [SoAd](../cp/communication/soad/) — 内容 [ ] · 链接 [ ]
- [ ] [FvM 专题](../cp/communication/fvm/fvm.md) — 内容 [ ] · 链接 [ ]
- [ ] [Full-CAN vs Basic-CAN](../cp/others/full_can_vs_basic_can/) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR COM（COM模块）](../cp/communication/com/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR CanSM（CAN状态管理器）](../cp/communication/cansm/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR CanTp（CAN传输层）](../cp/communication/cantp/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR TcpIp（TCP/IP协议栈）](../cp/communication/tcpip/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR Nm（网络管理接口）](../cp/communication/nm/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR EthSM（以太网状态管理器）](../cp/communication/ethsm/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR IpduM（I-PDU多路复用器）](../cp/communication/ipdum/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR SomeIpXf（SOME/IP转换器）](../cp/communication/someipxf/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR SomeIpTp（SOME/IP传输协议）](../cp/communication/someiptp/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR FlexRay Interface（FlexRay 接口）](../cp/communication/flexray_interface/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR FlexRay Network Management（FlexRay 网络管理）](../cp/communication/flexray_network_management/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR FlexRay State Manager（FlexRay 状态管理器）](../cp/communication/flexray_state_manager/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR FlexRay Transceiver Driver（FlexRay 收发器驱动）](../cp/communication/flexray_transceiver_driver/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR FlexRay AUTOSAR Transport Layer（FlexRay AUTOSAR 传输层）](../cp/communication/flexray_ar_transport_layer/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR FlexRay ISO 传输层（FlexRay ISO Transport Layer）](../cp/communication/flexray_iso_transport_layer/) — 内容 [ ] · 链接 [ ]

### crypto（4 篇）

- [ ] [Csm 加密服务管理器](../cp/crypto/crypto_service_manager/) — 内容 [ ] · 链接 [ ]
- [ ] [KeyM 密钥管理器](../cp/crypto/key_manager/) — 内容 [ ] · 链接 [ ]
- [ ] [CryIf 加密接口](../cp/crypto/crypto_interface/) — 内容 [ ] · 链接 [ ]
- [ ] [Crypto 驱动](../cp/crypto/crypto_driver/) — 内容 [ ] · 链接 [ ]

### diagnostics（3 篇）

- [ ] [Dcm 诊断通信管理器](../cp/diagnostics/diagnostic_communication_manager/) — 内容 [ ] · 链接 [ ]
- [ ] [Dem 诊断事件管理器](../cp/diagnostics/diagnostic_event_manager/) — 内容 [ ] · 链接 [ ]
- [ ] [SAE J1939 Dcm 诊断通信管理器](../cp/diagnostics/j1939dcm/) — 内容 [ ] · 链接 [ ]

### general（4 篇）

- [ ] [Standard Types](../cp/general/standard_types/) — 内容 [ ] · 链接 [ ]
- [ ] [ComStack Types 通信栈类型](../cp/general/communication_stack_types/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [BSW General（基础软件模块通用规范）](../cp/general/bsw_general/) — 内容 [ ] · 链接 [ ]
- [ ] [Platform Types（平台类型）](../cp/general/platform_types/) — 内容 [ ] · 链接 [ ]

### globaltime（4 篇）

- [ ] [AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](../cp/globaltime/eth_tsyn/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR Time Synchronization over CAN（CAN 时间同步）](../cp/globaltime/can_tsyn/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](../cp/globaltime/stbm/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](../cp/globaltime/fr_tsyn/index.md) — 内容 [ ] · 链接 [ ]

### io（7 篇）

- [ ] [ADC 驱动](../cp/io/adc_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [DIO 驱动](../cp/io/dio_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [OCU 驱动](../cp/io/ocu_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [Port 驱动](../cp/io/port_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [PWM 驱动](../cp/io/pwm_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [ICU 驱动](../cp/io/icu_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [I/O 硬件抽象](../cp/io/iohwab/) — 内容 [ ] · 链接 [ ]

### libraries（9 篇）

- [ ] [Specification of CRC Routines（CRC 例程规范）](../cp/libraries/crc/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [Specification of SW-C End-to-End Communication Protection Library（SW-C 端到端通信保护库规范）](../cp/libraries/e2e/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [Specification of Bit Handling Routines（位处理例程规范）](../cp/libraries/bfx/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [Specification of Basic Software Multicore Library（基础软件多核库规范）](../cp/libraries/bmc/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [Specification of Floating Point Math Routines（浮点数学例程规范）](../cp/libraries/mfl/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [Specification of Fixed Point Math Routines（定点数学例程规范）](../cp/libraries/mfx/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [Specification of Floating Point Interpolation Routines（浮点插值例程规范）](../cp/libraries/ifl/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [Specification of Fixed Point Interpolation Routines（定点插值例程规范）](../cp/libraries/ifx/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [Specification of Extended Fixed Point Routines（扩展定点例程规范）](../cp/libraries/efx/index.md) — 内容 [ ] · 链接 [ ]

### mcal（3 篇）

- [ ] [MCU 驱动](../cp/mcal/mcu_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [GPT 驱动](../cp/mcal/gpt_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [CoreTest 内核测试](../cp/mcal/core_test/) — 内容 [ ] · 链接 [ ]

### memory（6 篇）

- [ ] [AUTOSAR BndM（非易失性大容量数据管理器）](../cp/memory/bulk_nv_data_manager/) — 内容 [ ] · 链接 [ ]
- [ ] [Flash 驱动](../cp/memory/flash_driver/) — 内容 [ ] · 链接 [ ]
- [ ] [NvM](../cp/memory/nvram_manager/) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR Memory Access（存储访问）](../cp/memory/memory_access/) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR Memory Mapping（AUTOSAR 内存映射）](../cp/memory/memory_mapping/) — 内容 [ ] · 链接 [ ]
- [ ] [NV 数据处理指南](../cp/memory/nv_data_handling_guideline/) — 内容 [ ] · 链接 [ ]

### mode_management（3 篇）

- [ ] [BswM](../cp/mode_management/basic_software_mode_manager/) — 内容 [ ] · 链接 [ ]
- [ ] [EcuM](../cp/mode_management/ecu_state_manager/) — 内容 [ ] · 链接 [ ]
- [ ] [模式管理指南](../cp/mode_management/guide_to_mode_management/) — 内容 [ ] · 链接 [ ]

### system_services（7 篇）

- [ ] [Default Error Tracer（默认错误跟踪器）](../cp/system_services/default_error_tracer/) — 内容 [ ] · 链接 [ ]
- [ ] [FiM（功能禁止管理器）](../cp/system_services/function_inhibition_manager/) — 内容 [ ] · 链接 [ ]
- [ ] [时间服务](../cp/system_services/time_service/) — 内容 [ ] · 链接 [ ]
- [ ] [OS](../cp/system_services/operating_system/) — 内容 [ ] · 链接 [ ]
- [ ] [ComM（通信管理器）](../cp/system_services/comm/) — 内容 [ ] · 链接 [ ]
- [ ] [Software Cluster Connection（软件集群连接）](../cp/system_services/software_cluster_connection/) — 内容 [ ] · 链接 [ ]
- [ ] [Hardware Test Management startup shutdown（硬件测试管理启动和关闭）](../cp/system_services/hw_test_manager/) — 内容 [ ] · 链接 [ ]

### safety（3 篇）

- [ ] [WdgM 看门狗管理器](../cp/safety/watchdog_manager/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [WdgIf 看门狗接口](../cp/safety/watchdog_interface/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [Wdg 看门狗驱动](../cp/safety/watchdog_driver/index.md) — 内容 [ ] · 链接 [ ]

### security（2 篇）

- [ ] [Firewall（防火墙）](../cp/security/firewall/) — 内容 [ ] · 链接 [ ]
- [ ] [Intrusion Detection System Manager（入侵检测系统管理器）](../cp/security/idsm/) — 内容 [ ] · 链接 [ ]

### foundation/general (General)（7 篇）

- [ ] [TR Glossary（AUTOSAR 术语表）](../foundation/general/tr_glossary/) — 内容 [ ] · 链接 [ ]
- [ ] [Explanation of Software Architectural Decisions（软件架构决策说明）](../foundation/general/exp_sw_architectural_decisions/) — 内容 [ ] · 链接 [ ]
- [ ] [Safety Overview（功能安全概览）](../foundation/general/exp_safety_overview/) — 内容 [ ] · 链接 [ ]
- [ ] [Security Overview（信息安全概览）](../foundation/general/exp_security_overview/) — 内容 [ ] · 链接 [ ]
- [ ] [Main Requirements（主需求规范）](../foundation/general/rs_main/) — 内容 [ ] · 链接 [ ]
- [ ] [Project Objectives（项目目标）](../foundation/general/rs_project_objectives/) — 内容 [ ] · 链接 [ ]
- [ ] [Predefined Names in AUTOSAR（AUTOSAR 预定义名称）](../foundation/general/tr_predefined_names/) — 内容 [ ] · 链接 [ ]

### foundation/communication_management (Communication Management)（6 篇）

- [ ] [Explanation of Time Sensitive Networking Features（时间敏感网络特性说明）](../foundation/communication_management/exp_time_sensitive_network_features/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Debug Trace Profile（调试跟踪配置文件需求）](../foundation/communication_management/rs_debug_trace_profile/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on E2E（端到端通信保护需求）](../foundation/communication_management/rs_e2e/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Log and Trace（日志与跟踪需求）](../foundation/communication_management/rs_log_and_trace/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on MACsec（MACsec 需求）](../foundation/communication_management/rs_macsec/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Network Management（网络管理需求）](../foundation/communication_management/rs_network_management/) — 内容 [ ] · 链接 [ ]

### foundation/diagnostics (Diagnostics)（1 篇）

- [ ] [Requirements on Diagnostics（诊断需求）](../foundation/diagnostics/rs_diagnostics/) — 内容 [ ] · 链接 [ ]

### foundation/health_monitoring (Health Monitoring)（3 篇）

- [ ] [Specification of Health Monitoring（健康监控规范）](../foundation/health_monitoring/asws_health_monitoring/) — 内容 [ ] · 链接 [ ]
- [ ] [Explanation of System Health Monitoring（系统健康监控说明）](../foundation/health_monitoring/exp_system_health_monitoring/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Health Monitoring（健康监控需求）](../foundation/health_monitoring/rs_health_monitoring/) — 内容 [ ] · 链接 [ ]

### foundation/methodology_templates (Methodology and Templates)（12 篇）

- [ ] [Requirements on Feature Model Exchange Format（特征模型交换格式需求）](../foundation/methodology_templates/rs_feature_model_exchange_format/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Methodology（方法论需求）](../foundation/methodology_templates/rs_methodology/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Security Extract Template（安全提取模板需求）](../foundation/methodology_templates/rs_security_extract_template/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Standardization Template（标准化模板需求）](../foundation/methodology_templates/rs_standardization_template/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Timing Extensions（时序扩展需求）](../foundation/methodology_templates/rs_timing_extensions/) — 内容 [ ] · 链接 [ ]
- [ ] [ARXML Serialization Rules（ARXML 序列化规则）](../foundation/methodology_templates/tps_arxml_serialization_rules/) — 内容 [ ] · 链接 [ ]
- [ ] [Abstract Platform Specification（抽象平台规范）](../foundation/methodology_templates/tps_abstract_platform_specification/) — 内容 [ ] · 链接 [ ]
- [ ] [Feature Model Exchange Format（特征模型交换格式）](../foundation/methodology_templates/tps_feature_model_exchange_format/) — 内容 [ ] · 链接 [ ]
- [ ] [Log and Trace Extract Template（日志与跟踪提取模板）](../foundation/methodology_templates/tps_log_and_trace_extract/) — 内容 [ ] · 链接 [ ]
- [ ] [Security Extract Template（安全提取模板）](../foundation/methodology_templates/tps_security_extract_template/) — 内容 [ ] · 链接 [ ]
- [ ] [Standardization Template（标准化模板）](../foundation/methodology_templates/tps_standardization_template/) — 内容 [ ] · 链接 [ ]
- [ ] [XML Schema Production Rules（XML 模式生成规则）](../foundation/methodology_templates/tps_xml_schema_production_rules/) — 内容 [ ] · 链接 [ ]

### foundation/protocols (Protocols)（12 篇）

- [ ] [Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](../foundation/protocols/prs_intrusion_detection_system/) — 内容 [ ] · 链接 [ ]
- [ ] [Network Management Protocol Specification（网络管理协议规范）](../foundation/protocols/prs_network_management_protocol/) — 内容 [ ] · 链接 [ ]
- [ ] [SOME/IP Protocol Specification（SOME/IP 协议规范）](../foundation/protocols/prs_someip_protocol/) — 内容 [ ] · 链接 [ ]
- [ ] [SOME/IP Service Discovery Protocol Specification（SOME/IP 服务发现协议规范）](../foundation/protocols/prs_someip_service_discovery_protocol/) — 内容 [ ] · 链接 [ ]
- [ ] [Secure Onboard Communication Protocol Specification（安全车载通信协议规范）](../foundation/protocols/prs_secoc_protocol/) — 内容 [ ] · 链接 [ ]
- [ ] [Time Synchronization Protocol Specification（时间同步协议规范）](../foundation/protocols/prs_time_sync_protocol/) — 内容 [ ] · 链接 [ ]
- [ ] [V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](../foundation/protocols/prs_v2x_remote_access_layer/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Data Distribution Service（数据分发服务需求）](../foundation/protocols/rs_data_distribution_service/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on IPsec Protocol（IPsec 协议需求）](../foundation/protocols/rs_ipsec_protocol/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on SOME/IP Protocol（SOME/IP 协议需求）](../foundation/protocols/rs_someip_protocol/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](../foundation/protocols/rs_someip_service_discovery_protocol/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Time Synchronization（时间同步需求）](../foundation/protocols/rs_time_sync/) — 内容 [ ] · 链接 [ ]

### foundation/release_documentation (Release Documentation)（1 篇）

- [ ] [Release Overview（发布概览）](../foundation/release_documentation/tr_release_overview/) — 内容 [ ] · 链接 [ ]

### foundation/safety (Safety)（1 篇）

- [ ] [Requirements on Safety（功能安全需求）](../foundation/safety/rs_safety/) — 内容 [ ] · 链接 [ ]

### foundation/security (Security)（4 篇）

- [ ] [Requirements on Firewall（防火墙需求）](../foundation/security/rs_firewall/) — 内容 [ ] · 链接 [ ]
- [ ] [Requirements on Intrusion Detection System（入侵检测系统需求）](../foundation/security/rs_intrusion_detection_system/) — 内容 [ ] · 链接 [ ]
- [ ] [List of Known Issues of Secure Hardware Extensions（安全硬件扩展已知问题清单）](../foundation/security/tr_list_of_known_issues_secure_hardware_extensions/) — 内容 [ ] · 链接 [ ]
- [ ] [Specification of Secure Hardware Extensions（安全硬件扩展规范）](../foundation/security/tr_secure_hardware_extensions/) — 内容 [ ] · 链接 [ ]

### foundation/system_services (System Services)（1 篇）

- [ ] [Timing Analysis（时序分析）](../foundation/system_services/tr_timing_analysis/) — 内容 [ ] · 链接 [ ]

### rte (RTE / SWArch)（2 篇）

- [ ] [AUTOSAR RTE（运行时环境）](../cp/rte/rte/index.md) — 内容 [ ] · 链接 [ ]
- [ ] [AUTOSAR ARTI（运行时接口）](../cp/sw_arch/arti_sws/index.md) — 内容 [ ] · 链接 [ ]

## Findings log

| Article (path) | Goal | Finding | Resolution |
| --- | --- | --- | --- |
| `docs/autosar/TODO.md` (F1) | 2 | Duplicate `## security` section — Firewall row listed twice | **Resolved 2026-11-06** — duplicate section removed |
| `docs/autosar/TODO.md` (F2) | 2 | `CanNm R21-11 历史版` links to a removed file | **Resolved 2026-11-06** — stale 📖 row removed |
| `docs/autosar/TODO.md` (F3) | 2 | `cp/template/` example row links to deleted dirs | **Resolved 2026-11-06** — stale 📖 row removed |
| `docs/autosar/TODO.md` (F4) | 1/2 | Overview count table stale (27 ✅ vs 160 ✅) | **Resolved 2026-11-06** — status rows regenerated; queue-derived Missing rows documented |
| `foundation/communication_management/index.md:9` | 2 | Landing link `dir/` without `index.md` (build INFO) | **Resolved 2026-11-06** — `/index.md` appended |
| `foundation/release_documentation/index.md:9` | 2 | Landing link `dir/` without `index.md` (build INFO) | **Resolved 2026-11-06** — `/index.md` appended |
| `foundation/security/index.md:11` | 2 | Landing link `dir/` without `index.md` (build INFO) | **Resolved 2026-11-06** — `/index.md` appended |
| `cp/communication/v2x_datamgr/index.md:399,476` | 2 | Broken intra-page anchor `#774-v2xdm_callback_stack_msg_type` | **Resolved 2026-11-06** — re-pointed to `#774-v2xdm_callback_stackmsgtype` |
| 13 CP articles (A1/A2 table) | 1 | Chapter-2 wording deviations + 3 other chapter deviations | Source check done — 11 are source-faithful (rule conflict), 2 genuine drift/skeleton conflict; decision pending |
| `flexray_ar_transport_layer`, `memory_mapping` | 1 | Numbering gaps (ch.5 / ch.9 dropped without renumber) | Source check done — both are genuine renumbering failures; renumber + anchor sweep pending |
| 5 FlexRay articles (A4) | 1 | Chinese-first bilingual titles | **Resolved 2026-11-06** — renamed + full ripple sweep; `--titles` 0 violations |
| `cp/libraries/mfl/index.md:2501` | 1 | `check_heading_lang.py` false positive on `Mfl` | No article change; widen script identifier exemption — deferred |
| 43 external URLs (B2) | 2 | 403/418 anti-bot, 000 connection failures, 7×404, 5×500 | Manual browser verification; never auto-remove — pending |
