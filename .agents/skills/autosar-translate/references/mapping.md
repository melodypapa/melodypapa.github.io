# Mapping — AUTOSAR spec ↔ site article

## Platform → site tree (2026-11-02)

`docs/autosar/` holds one subtree per AUTOSAR platform, mirroring the source
corpus `~/Workspace/autosar_standard/markdown/<Platform>/Releases/R23-11/`:

| Source tree | Site tree | Content |
| --- | --- | --- |
| `Classic_Platform/…` (`AUTOSAR_CP_*`) | `docs/autosar/cp/<section>/<article>/` | SWS/EXP/TPS translations, the generated API listing `cp/api/` |
| `Foundation/…` (`AUTOSAR_FO_*`) | `docs/autosar/foundation/<topic>/<article>/` | RS/PRS/TPS/TR/EXP translations (no SWS documents exist) |
| — | `docs/autosar/index.md`, `docs/autosar/glossary.md` | platform hub and the shared 术语表 |

Paths carry no release segment; the release is recorded in each article's
front-matter `release:`. Article paths in this file are relative to the
platform tree (`cp/` or `foundation/`).

## Category → site section (Classic Platform)

| Standard taxonomy dir | Site dir under `docs/autosar/cp/` |
| --- | --- |
| `ApplicationInterfaces` | `application_interfaces/` |
| `Communication` | `communication/` |
| `Crypto` | `crypto/` |
| `Diagnostics` | `diagnostics/` |
| `General`, `BSWGeneral` | `general/` |
| `GlobalTime` | `globaltime/` |
| `IO` | `io/` |
| `Libraries` | `libraries/` |
| `MCAL` | `mcal/` |
| `Memory` | `memory/` |
| `MethodologyAndTemplates` | `methodology_templates/` and `template/` |
| `ModeManagement` | `mode_management/` |
| `RTE` | `rte/` |
| `Safety` | `safety/` |
| `SWArch` | `sw_arch/` |
| `SystemServices` | `system_services/` |
| `Security`, `ReleaseDocumentation` | no section yet — propose one to the user before creating |

## Category → site section (Foundation)

| Standard taxonomy dir | Site dir under `docs/autosar/foundation/` |
| --- | --- |
| `General` | `general/` (TR Glossary translated) |
| `CommunicationManagement` | `communication_management/` |
| `Diagnostics` | `diagnostics/` |
| `HealthMonitoring` | `health_monitoring/` |
| `MethodologyAndTemplates` | `methodology_templates/` |
| `Protocols` | `protocols/` |
| `ReleaseDocumentation` | `release_documentation/` |
| `Safety` | `safety/` |
| `Security` | `security/` |
| `SystemServices` | `system_services/` |

All ten Foundation topic directories exist with landing pages; only
`general/tr_glossary/` holds a (partially translated) article so far. Every
Foundation document is queued in `sync-todo/Group-foundation-exp.md`
(EXP/TR/TPS/ASWS guide/template/report documents — the CP `Group-exp.md`
counterpart) and `sync-todo/Group-foundation-rs-prs.md` (RS/PRS
requirement/protocol specifications).
Foundation article slug = `<type>_<snake_name>` of the source file name after
the `tr_glossary` precedent (`rs_main`, `prs_e2e_protocol`,
`tps_generic_structure_template`): the type prefix keeps the same-named RS/PRS
pairs apart (`rs_someip_protocol` vs `prs_someip_protocol`).

## Known mappings (curated; keep in sync with the repo)

Paths are relative to `docs/autosar/cp/`.

| Spec document (any release naming) | Article |
| --- | --- |
| SWS_BSWModeManager | `mode_management/basic_software_mode_manager` |
| SWS_ECUStateManager | `mode_management/ecu_state_manager` |
| EXP_ModeManagementGuide | `mode_management/guide_to_mode_management` |
| SWS_StandardTypes | `general/standard_types` |
| SWS_PlatformTypes | `general/platform_types` |
| SWS_MemoryMapping | `memory/memory_mapping` |
| SWS_ADCDriver | `io/adc_driver` |
| SWS_DIODriver | `io/dio_driver` |
| SWS_ICUDriver | `io/icu_driver` |
| SWS_OCUDriver | `io/ocu_driver` |
| SWS_PWMDriver | `io/pwm_driver` |
| SWS_PortDriver | `io/port_driver` |
| SWS_IOHardwareAbstraction / SWS_IOHWAbstraction | `io/iohwab` |
| SWS_CANDriver | `communication/can_driver` |
| SWS_CANInterface | `communication/can_interface` |
| SWS_CANNetworkManagement | `communication/can_network_management` |
| SWS_CANTransceiverDriver | `communication/can_transceiver_driver` |
| SWS_LINDriver | `communication/lin_driver` |
| SWS_LINInterface | `communication/lin_interface` |
| SWS_EthernetDriver | `communication/ethernet_driver` |
| SWS_EthernetInterface | `communication/ethernet_interface` |
| SWS_EthernetSwitchDriver (EthSwt) | `communication/ethernet_switch_driver` |
| SWS_SocketAdaptor (SoAd) | `communication/soad` |
| SWS_ServiceDiscovery (Sd) | `communication/service_discovery` |
| SWS_BusMirroring | `communication/mirror` |
| SWS_PduR | `communication/pdu_router` |
| SWS_SecOc | `communication/sec_oc` |
| SWS_E2ETransformer | `communication/e2e_transformer` |
| SWS_COMBasedTransformer / SWS_TransformerCOMBased | `communication/com_based_transformer` |
| SWS_UDPNetworkManagement (UdpNm) | `communication/udp_network_management` |
| SWS_DataDistribution | `communication/data_distribution` |
| SWS_DiagnosticCommunicationManager (Dcm) | `diagnostics/diagnostic_communication_manager` |
| SWS_DiagnosticEventManager (Dem) | `diagnostics/diagnostic_event_manager` |
| SWS_CryptoDriver | `crypto/crypto_driver` |
| SWS_CryptoInterface (CryIf) | `crypto/crypto_interface` |
| SWS_KeyManager (KeyM) | `crypto/key_manager` |
| SWS_CryptoServiceManager (Csm) | `crypto/crypto_service_manager` |
| SWS_FlashDriver (Fls) | `memory/flash_driver` |
| SWS_FlashEEPROMEmulation (Fee) | `memory/flash_eeprom_emulation` |
| SWS_MemoryAccess (MemIf) | `memory/memory_access` |
| SWS_NVRAMManager (NvM) | `memory/nvram_manager` |
| SWS_BulkNvDataManager (BndM) | `memory/bulk_nv_data_manager` |
| EXP_NVDataHandlingGuideline | `memory/nv_data_handling_guideline` |
| SWS_FunctionInhibitionManager (FiM) | `system_services/function_inhibition_manager` |
| SWS_OperatingSystem (Os) | `system_services/operating_system` |
| SWS_TimeService | `system_services/time_service` |
| TPS_BSWModuleDescriptionTemplate | `methodology_templates/basic_software_module_description_template` |
| FO_TR_Glossary | `../foundation/general/tr_glossary` (Foundation tree) |

Articles that are **not** spec translations (no SWS source; never sync these):
`template/generic_structure` and `template/timimg_extension` (template
examples). Everything else in the table above has a corresponding standard
document.

## Naming new articles

- Directory: lowercase snake_case of the module's short name, mirroring the
  known rows above (e.g. `EthernetSwitchDriver` → `ethernet_switch_driver`,
  `SocketAdaptor` → `socket_adaptor`).
- Acronym-ambiguous names (SoAd, DoIp, SomeIp) → propose the directory name to
  the user before creating.
- New article file is always `index.md` with front-matter `title`, and must be
  registered in `mkdocs.yml` nav under the right section (paths relative to
  `docs/`, e.g. `autosar/cp/io/adc_driver/index.md`), or `mkdocs build --strict`
  fails. The same commit updates the derived indexes — `<section>/index.md`
  `## 文章`, the platform overview (`autosar/cp/index.md` or
  `autosar/foundation/index.md`), and the site home `docs/index.md` when the
  article introduces a new top-level tab — then runs
  `scripts/check_indexes.py` (SKILL.md Step 6.3).
- Three naming levels (user rule 2026-10-29):
  - `mkdocs.yml` page label = **simple name** (`Powertrain`, `Chassis`, `ARTI`,
    `VFB`, `FOTA`, `SwCluC`) — never the full bilingual title.
  - article front-matter `title` = **full** `English（中文）` — English name
    first, Chinese in full-width parentheses
    (`AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）`,
    `Powertrain Engine Domain（动力总成（发动机）域）`).
  - index link labels (`## 文章`, overview, `glossary.md` 来源,
    the API listing `docs/autosar/cp/api/`) = the target's full front-matter
    `title`, never the nav's short label.
- `中文（English）` is invalid (user rule 2026-10-29): fix the title itself,
  not just the index link label, and update the derived indexes and 来源 lines
  in the same commit. `check_indexes.py --titles` lists remaining violations.
- The English and Chinese halves must name the same document/module. Check
  against the mapped `spec:` source and authoritative acronym expansions;
  acronyms may pair with their Chinese expansion (`VFB（虚拟功能总线）`). The
  title checker catches missing/empty halves and reversed order, not semantic
  mismatches, so the latter needs a source-based review.

## Coverage inventory

List what exists on either side:

```bash
# SWS/EXP docs available in a release
find ~/Workspace/autosar_standard/markdown/Classic_Platform/Releases/R23-11 \
  \( -iname "AUTOSAR_CP_SWS_*.md" -o -iname "AUTOSAR_CP_EXP_*.md" \) -not -path "*artifacts*" \
  | sed 's|.*/Releases/||' | sort

# Existing articles (CP and Foundation trees)
find docs/autosar/cp docs/autosar/foundation -name index.md | sort
```

Then reconcile using the known-mapping table first; anything unmatched on the
spec side is a candidate missing article (confirm with the user — some specs
are deliberately not translated).
