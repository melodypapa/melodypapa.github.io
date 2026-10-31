# All Sync Todo Articles by Group

Generated from all Group files in `docs/autosar/sync-todo/` — articles ordered by group, then by appearance order within each group. Regenerate with `python .agents/skills/autosar-translate/scripts/gen_sync_todo_index.py`.

Status `Done` = all 6 queue steps complete (translation merged). Status `Aligned` = the article already exists on the site but the queue steps are not ticked — the remaining steps are an alignment pass, not a fresh translation (the row's ✅/🔶/⚠️/📖 marker is kept). Status `Pending` = the article does not exist yet. Commit ID = the translation commit sha(s) or PR recorded on the queue row, resolved to 10-character commit ids (PR numbers are resolved to the PR's merge commit, or head commit while open; falling back to the commit that added the article); `N/A` = work not started.

## Group communication-2 — communication section — remaining missing documents (38)

Status: **17/38** completed

| Article                    | Status | Commit ID |
| --------------------------- | -------- | ---------- |
| `spi`                        | [x] Done | be171a1b1c |
| `ldcom`                      | [x] Done | 6e4865a2a5 |
| `lsdu`                       | [x] Done | 6e4865a2a5 |
| `dlt`                        | [x] Done | 6e4865a2a5 |
| `doip`                       | [x] Done | 6e4865a2a5 |
| `xcp`                        | [x] Done | 6e4865a2a5 |
| `canxl_driver`               | [x] Done | fa81322ae9 |
| `canxl_transceiver_driver`   | [x] Done | fa81322ae9 |
| `eth_trcv`                   | [x] Done | fa81322ae9 |
| `wlan_driver`                | [x] Done | fa81322ae9 |
| `wlan_transceiver_driver`    | [x] Done | fa81322ae9 |
| `flexray_driver`             | [x] Done | fa81322ae9 |
| `flexray_interface`          | [x] Done | 51bd5a4c8f |
| `flexray_nm`                 | [x] Done | 51bd5a4c8f |
| `flexray_sm`                 | [x] Done | 51bd5a4c8f |
| `flexray_trcv`               | [x] Done | 51bd5a4c8f |
| `flexray_ar_tp`              | [x] Done | 51bd5a4c8f |
| `flexray_iso_tp`             | [ ] Pending | N/A |
| `linsm`                      | [ ] Pending | N/A |
| `lintrcv`                    | [ ] Pending | N/A |
| `ttcan_driver`               | [ ] Pending | N/A |
| `ttcan_interface`            | [ ] Pending | N/A |
| `j1939nm`                    | [ ] Pending | N/A |
| `j1939rm`                    | [ ] Pending | N/A |
| `j1939tp`                    | [ ] Pending | N/A |
| `ieee1722tp`                 | [ ] Pending | N/A |
| `macsec`                     | [ ] Pending | N/A |
| `cellularv2x_driver`         | [ ] Pending | N/A |
| `chargingmanager`            | [ ] Pending | N/A |
| `chinesev2x_mgmt`            | [ ] Pending | N/A |
| `chinesev2x_msg`             | [ ] Pending | N/A |
| `chinesev2x_net`             | [ ] Pending | N/A |
| `chinesev2x_sec`             | [ ] Pending | N/A |
| `v2x_basictp`                | [ ] Pending | N/A |
| `v2x_datamgr`                | [ ] Pending | N/A |
| `v2x_facilities`             | [ ] Pending | N/A |
| `v2x_geonet`                 | [ ] Pending | N/A |
| `v2x_mgmt`                   | [ ] Pending | N/A |

## Group communication — communication section — existing articles + backbone

Status: **24/24** completed

| Article                  | Status | Commit ID |
| ------------------------- | -------- | ---------- |
| `can_network_management`   | [x] Done | 3a7fa89890 |
| `udp_network_management`   | [x] Done | 3a7fa89890 |
| `can_driver`               | [x] Done | 3a7fa89890 |
| `can_transceiver_driver`   | [x] Done | e48b58e604 |
| `pdu_router`               | [x] Done | f915d45a5d |
| `ethernet_interface`       | [x] Done | a08b183bbd |
| `lin_interface`            | [x] Done | c6dd02bec7 |
| `com_based_transformer`    | [x] Done | 3562899b14 |
| `e2e_transformer`          | [x] Done | 4d5ff96f15 |
| `data_distribution`        | [x] Done | b2c1ffb46a |
| `sec_oc`                   | [x] Done | 3d584a281f |
| `soad`                     | [x] Done | 1b9bf69034 |
| `mirror`                   | [x] Done | c3e84ef8da |
| `ethernet_switch_driver`   | [x] Done | 7f5fc5ecc6 |
| `service_discovery`        | [x] Done | 23b20e5f63 |
| `com`                      | [x] Done | 17cdb70608 |
| `cansm`                    | [x] Done | a803400f8b |
| `cantp`                    | [x] Done | 5e2624deac |
| `tcpip`                    | [x] Done | bcbd61e4de |
| `nm`                       | [x] Done | 5036abf611 |
| `ethsm`                    | [x] Done | 37c98ecaf5 |
| `ipdum`                    | [x] Done | 5cef2ca1e3 |
| `someipxf`                 | [x] Done | e4115620c1 |
| `someiptp`                 | [x] Done | af4d193edc |

## Group crypto — crypto section

Status: **3/4** completed

| Article                  | Status | Commit ID |
| ------------------------- | -------- | ---------- |
| `crypto_service_manager`   | [ ] Aligned ⚠️ | 82efc1391e |
| `crypto_driver`            | [x] Done | 8b73b6f312 |
| `cryif`                    | [x] Done | c2cba4b51d |
| `keym`                     | [x] Done | 6e52dcabd4 |

## Group diagnostics — diagnostics section

Status: **1/3** completed

| Article                            | Status | Commit ID |
| ----------------------------------- | -------- | ---------- |
| `diagnostic_event_manager`           | [x] Done | c5b4a2573a |
| `j1939dcm`                           | [ ] Pending | 8795b71e19 |
| `diagnostic_communication_manager`   | [ ] Aligned ⚠️ | 24c7a36bc4 |

## Group exp — missing EXP guides (20)

Status: **21/21** completed

| Article                                          | Status | Commit ID |
| ------------------------------------------------- | -------- | ---------- |
| `exp vfb`                                          | [x] Done | d6cf2ec55c |
| `exp layered_software_architecture`                | [x] Done | f60d11a303 |
| `exp vfb`                                          | [x] Done | d6cf2ec55c |
| `exp bsw_distribution_guide`                       | [x] Done | 668adfc728 |
| `exp application_level_error_handling`             | [x] Done | 52d4d5c646 |
| `exp error_description`                            | [x] Done | 9088a60a46 |
| `exp cdd_design_and_integration`                   | [x] Done | 4e5d294ed6 |
| `exp utilization_of_crypto_services`               | [x] Done | bcbaf51a17 |
| `exp macro_encapsulation_of_interpolation_calls`   | [x] Done | f385e42b04 |
| `exp firmware_over_the_air`                        | [x] Done | 30ee49dcbe |
| `exp adas_vmc`                                     | [x] Done | a8f5273bc0 |
| `exp body_and_comfort`                             | [x] Done | 9055f2593a |
| `exp chassis`                                      | [x] Done | b1f1d8aff6 |
| `exp hmi`                                          | [x] Done | 29ee0f30c0 |
| `exp occupant_safety`                              | [x] Done | ed312b3ecd |
| `exp powertrain`                                   | [x] Done | 790911157f |
| `exp user_guide`                                   | [x] Done | 2453865a8c |
| `exp arti`                                         | [x] Done | 89cd317758 |
| `exp functional_safety_measures`                   | [x] Done | c1ed1dacae |
| `exp safety_use_case`                              | [x] Done | 5fa1e61af2 |
| `exp sw_cluster_design_and_integration`            | [x] Done | 26625e4b1b |

## Group general — general/base specifications

Status: **4/5** completed

| Article                     | Status | Commit ID |
| ---------------------------- | -------- | ---------- |
| `platform_types`              | [x] Done | 439597529a |
| `bsw_general`                 | [x] Done | 2bc57c2cd4 |
| `platform_types_2`            | [x] Done | d773247410 |
| `communication_stack_types`   | [x] Done | faa08069ee |
| `tr_glossary`                 | [ ] Aligned 📖 | c19bc75dd6 |

## Group globaltime — global time cluster (new section)

Status: **3/4** completed

| Article    | Status | Commit ID |
| ----------- | -------- | ---------- |
| `stbm`       | [x] Done | 53cd591142 |
| `can_tsyn`   | [x] Done | 364c4fd73b |
| `eth_tsyn`   | [x] Done | 8f01771012 |
| `fr_tsyn`    | [ ] Pending | N/A |

## Group io — IO section wrap-up

Status: **7/7** completed

| Article       | Status | Commit ID |
| -------------- | -------- | ---------- |
| `dio_driver`    | [x] Done | de11d8ac0f/493ed125e3/e21067fbde |
| `port_driver`   | [x] Done | ee486aa54f |
| `pwm_driver`    | [x] Done | 1b5e44b812 |
| `ocu_driver`    | [x] Done | b156916583 |
| `icu_driver`    | [x] Done | d11d759ec8/9cb876443e |
| `adc_driver`    | [x] Done | 3d8dd128be/625d4371a6 |
| `iohwab`        | [x] Done | 72a103c0ff |

## Group libraries — libraries section (new section)

Status: **0/9** completed

| Article | Status | Commit ID |
| ------ | -------- | ---------- |
| `crc`   | [ ] Pending | N/A |
| `e2e`   | [ ] Pending | N/A |
| `bfx`   | [ ] Pending | N/A |
| `bmc`   | [ ] Pending | N/A |
| `mfl`   | [ ] Pending | N/A |
| `mfx`   | [ ] Pending | N/A |
| `ifl`   | [ ] Pending | N/A |
| `ifx`   | [ ] Pending | N/A |
| `efx`   | [ ] Pending | N/A |

## Group mcal — MCAL section (new section)

Status: **3/3** completed

| Article    | Status | Commit ID |
| ----------- | -------- | ---------- |
| `mcu`        | [x] Done | 2f0e714db9 |
| `gpt`        | [x] Done | 065baee97a |
| `coretest`   | [x] Done | 1abff90a9d |

## Group memory — memory section

Status: **2/12** completed

| Article                        | Status | Commit ID |
| ------------------------------- | -------- | ---------- |
| `memory_access`                  | [x] Done | 922364777e |
| `memory_mapping`                 | [x] Done | 89900677f4 |
| `bulk_nv_data_manager`           | [ ] Aligned 🔶 | df7fb88a82 |
| `flash_driver`                   | [ ] Aligned 🔶 | df7fb88a82 |
| `nvram_manager`                  | [ ] Aligned 🔶 | df7fb88a82 |
| `flash_eeprom_emulation`         | [ ] Aligned ⚠️ | df7fb88a82 |
| `ea`                             | [ ] Pending | N/A |
| `eep`                            | [ ] Pending | N/A |
| `memory_abstraction_interface`   | [ ] Pending | N/A |
| `memory_driver`                  | [ ] Pending | N/A |
| `flstst`                         | [ ] Pending | N/A |
| `ramtst`                         | [ ] Pending | N/A |

## Group mode_management — mode management section

Status: **1/2** completed

| Article                       | Status | Commit ID |
| ------------------------------ | -------- | ---------- |
| `basic_software_mode_manager`   | [ ] Aligned ✅ | de15f9833e |
| `ecu_state_manager`             | [x] Done | 37ee564d4a |

## Group rte-swarch — RTE / SWArch section (new section)

Status: **0/2** completed

| Article | Status | Commit ID |
| ------- | -------- | ---------- |
| `rte`    | [ ] Aligned | 67b0783783 |
| `arti`   | [ ] Aligned | 89cd317758 |

## Group safety — safety section (new section)

Status: **3/3** completed

| Article | Status | Commit ID |
| -------- | -------- | ---------- |
| `wdgm`    | [x] Done | 24c7a36bc4 |
| `wdgif`   | [x] Done | 24c7a36bc4 |
| `wdg`     | [x] Done | 24c7a36bc4 |

## Group security — security section (new section)

Status: **0/2** completed

| Article    | Status | Commit ID |
| ----------- | -------- | ---------- |
| `firewall`   | [ ] Pending | N/A |
| `idsm`       | [ ] Pending | N/A |

## Group system_services — system services section

Status: **4/7** completed

| Article                       | Status | Commit ID |
| ------------------------------ | -------- | ---------- |
| `det`                           | [x] Done | 30510c9c38 |
| `function_inhibition_manager`   | [x] Done | 534d5d1099 |
| `time_service`                  | [x] Done | 5c57d0ae39 |
| `comm`                          | [ ] Pending | N/A |
| `swcluc`                        | [ ] Pending | N/A |
| `hwtestmanager`                 | [ ] Pending | N/A |
| `operating_system`              | [x] Done | ca7ecda991 |

**Total: 93/146 queue rows complete.**

