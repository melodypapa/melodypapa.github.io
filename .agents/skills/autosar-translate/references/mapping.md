# Mapping — AUTOSAR spec ↔ site article

## Category → site section

| Standard taxonomy dir | Site dir under `docs/autosar/` |
| --- | --- |
| `Communication` | `communication/` |
| `Crypto` | `crypto/` |
| `Diagnostics` | `diagnostics/` |
| `General`, `BSWGeneral` | `general/` |
| `IO` | `io/` |
| `Memory` | `memory/` |
| `MethodologyAndTemplates` | `methodology_templates/` and `template/` |
| `ModeManagement` | `mode_management/` |
| `SystemServices` | `system_services/` |
| `RTE`, `SWArch`, `Libraries`, `MCAL`, `ApplicationInterfaces`, `GlobalTime`, `Safety`, `Security`, `ReleaseDocumentation` | no section yet — propose one to the user before creating |

## Known mappings (curated; keep in sync with the repo)

| Spec document (any release naming) | Article |
| --- | --- |
| SWS_BSWModeManager | `mode_management/basic_software_mode_manager` |
| SWS_ECUStateManager | `mode_management/ecu_state_manager` |
| EXP_ModeManagementGuide | `mode_management/guide_to_mode_management` |
| SWS_StandardTypes | `general/platform_types` |
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
| SWS_SocketAdaptor (SoAd) | `communication/SoAd/SoAd.md` (partial, legacy numbering, non-index filename) |
| SWS_ServiceDiscovery (Sd) | `communication/service_discovery` |
| SWS_BusMirroring | `communication/mirror/mirror.md` (partial, non-index filename) |
| SWS_PduR | `communication/pdu_router` |
| SWS_SecOc | `communication/sec_oc` |
| SWS_E2ETransformer | `communication/e2e_transformer` |
| SWS_COMBasedTransformer / SWS_TransformerCOMBased | `communication/com_based_transformer` |
| SWS_UDPNetworkManagement (UdpNm) | `communication/udp_network_management` |
| SWS_DataDistribution | `communication/data_distribution service` (note: directory name contains a space) |
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

Articles that are **not** spec translations (no SWS source; never sync these):
`autosar/power` (bespoke topic article), `template/generic_structure` and
`template/timimg_extension` (template examples). Everything else in the table
above has a corresponding standard document.

## Naming new articles

- Directory: lowercase snake_case of the module's short name, mirroring the
  known rows above (e.g. `EthernetSwitchDriver` → `ethernet_switch_driver`,
  `SocketAdaptor` → `socket_adaptor`).
- Acronym-ambiguous names (SoAd, DoIp, SomeIp) → propose the directory name to
  the user before creating.
- New article file is always `index.md` with front-matter `title`, and must be
  registered in `mkdocs.yml` nav under the right section (paths relative to
  `docs/`), or `mkdocs build --strict` fails. The same commit updates the
  three derived indexes — `<section>/index.md` `## 文章`, the CP AUTOSAR
  overview `autosar/index.md`, and the site home `docs/index.md` when the
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
    `api_reference.md`) = the target's full front-matter `title`, never the
    nav's short label.
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

# Existing articles
find docs/autosar -name index.md | sort
```

Then reconcile using the known-mapping table first; anything unmatched on the
spec side is a candidate missing article (confirm with the user — some specs
are deliberately not translated).
