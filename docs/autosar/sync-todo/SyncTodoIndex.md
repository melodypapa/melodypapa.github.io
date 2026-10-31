# All Sync Todo Articles by Group

Generated from all Group files in `docs/autosar/sync-todo/` — articles ordered by group, then by appearance order within each group. Regenerate with `python .agents/skills/autosar-translate/scripts/gen_sync_todo_index.py`.

Status `Done` = all 6 queue steps complete (translation merged). Status `Aligned` = the article already exists on the site but the queue steps are not ticked — the remaining steps are an alignment pass, not a fresh translation (the row's ✅/🔶/⚠️/📖 marker is kept). Status `Pending` = the article does not exist yet. Commit ID = the translation commit sha(s) or PR recorded on the queue row (falling back to the commit that added the article); `N/A` = work not started.

## Group communication-2 — communication section — remaining missing documents (38)

Status: **11/38** completed

| Article                    | Status | Commit ID |
| --------------------------- | -------- | ---------- |
| `spi`                        | [x] Done | PR #141 |
| `ldcom`                      | [x] Done | PR #177 |
| `lsdu`                       | [x] Done | PR #177 |
| `dlt`                        | [x] Done | PR #177 |
| `doip`                       | [x] Done | PR #177 |
| `xcp`                        | [x] Done | PR #177 |
| `canxl_driver`               | [ ] Aligned | PR #190 |
| `canxl_transceiver_driver`   | [ ] Aligned | PR #190 |
| `eth_trcv`                   | [ ] Aligned | PR #190 |
| `wlan_driver`                | [ ] Aligned | PR #190 |
| `wlan_transceiver_driver`    | [ ] Aligned | PR #190 |
| `flexray_driver`             | [ ] Aligned | PR #190 |
| `flexray_interface`          | [x] Done | PR #208 |
| `flexray_nm`                 | [x] Done | PR #208 |
| `flexray_sm`                 | [x] Done | PR #208 |
| `flexray_trcv`               | [x] Done | PR #208 |
| `flexray_ar_tp`              | [x] Done | PR #208 |
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

Status: **4/24** completed

| Article                  | Status | Commit ID |
| ------------------------- | -------- | ---------- |
| `can_network_management`   | [ ] Aligned ✅ | PR #139 |
| `udp_network_management`   | [ ] Aligned ✅ | PR #139 |
| `can_driver`               | [ ] Aligned 🔶 | PR #139 |
| `can_transceiver_driver`   | [ ] Aligned 🔶 | e48b58e |
| `pdu_router`               | [x] Done | f915d45 |
| `ethernet_interface`       | [ ] Aligned ⚠️ | a08b183 |
| `lin_interface`            | [ ] Aligned ⚠️ | c6dd02b |
| `com_based_transformer`    | [ ] Aligned ⚠️ | 3562899 |
| `e2e_transformer`          | [ ] Aligned ⚠️ | 4d5ff96 |
| `data_distribution`        | [x] Done | b2c1ffb |
| `sec_oc`                   | [x] Done | 3d584a2 |
| `soad`                     | [x] Done | 1b9bf69 |
| `mirror`                   | [ ] Aligned ⚠️ | c3e84ef |
| `ethernet_switch_driver`   | [ ] Aligned | 7f5fc5e |
| `service_discovery`        | [ ] Aligned | 23b20e5 |
| `com`                      | [ ] Aligned | 17cdb70 |
| `cansm`                    | [ ] Aligned | a803400 |
| `cantp`                    | [ ] Aligned | 5e2624d |
| `tcpip`                    | [ ] Aligned | bcbd61e |
| `nm`                       | [ ] Aligned | 5036abf |
| `ethsm`                    | [ ] Aligned | 37c98ec |
| `ipdum`                    | [ ] Aligned | 5cef2ca |
| `someipxf`                 | [ ] Aligned | e411562 |
| `someiptp`                 | [ ] Aligned | af4d193 |

## Group crypto — crypto section

Status: **3/4** completed

| Article                  | Status | Commit ID |
| ------------------------- | -------- | ---------- |
| `crypto_service_manager`   | [ ] Aligned ⚠️ | PR #133 |
| `crypto_driver`            | [x] Done | 8b73b6f |
| `cryif`                    | [x] Done | c2cba4b |
| `keym`                     | [x] Done | 6e52dca |

## Group diagnostics — diagnostics section

Status: **1/3** completed

| Article                            | Status | Commit ID |
| ----------------------------------- | -------- | ---------- |
| `diagnostic_event_manager`           | [x] Done | c5b4a25 |
| `j1939dcm`                           | [ ] Pending | 8795b71 |
| `diagnostic_communication_manager`   | [ ] Aligned ⚠️ | 24c7a36 |

## Group exp — missing EXP guides (20)

Status: **21/21** completed

| Article                                          | Status | Commit ID |
| ------------------------------------------------- | -------- | ---------- |
| `exp vfb`                                          | [x] Done | d6cf2ec |
| `exp layered_software_architecture`                | [x] Done | f60d11a |
| `exp vfb`                                          | [x] Done | PR #158 |
| `exp bsw_distribution_guide`                       | [x] Done | 668adfc |
| `exp application_level_error_handling`             | [x] Done | 52d4d5c |
| `exp error_description`                            | [x] Done | 9088a60 |
| `exp cdd_design_and_integration`                   | [x] Done | 4e5d294 |
| `exp utilization_of_crypto_services`               | [x] Done | bcbaf51 |
| `exp macro_encapsulation_of_interpolation_calls`   | [x] Done | f385e42 |
| `exp firmware_over_the_air`                        | [x] Done | 30ee49d |
| `exp adas_vmc`                                     | [x] Done | a8f5273 |
| `exp body_and_comfort`                             | [x] Done | 9055f25 |
| `exp chassis`                                      | [x] Done | b1f1d8a |
| `exp hmi`                                          | [x] Done | 29ee0f3 |
| `exp occupant_safety`                              | [x] Done | ed312b3 |
| `exp powertrain`                                   | [x] Done | 7909111 |
| `exp user_guide`                                   | [x] Done | 2453865 |
| `exp arti`                                         | [x] Done | 89cd317 |
| `exp functional_safety_measures`                   | [x] Done | c1ed1da |
| `exp safety_use_case`                              | [x] Done | 5fa1e61 |
| `exp sw_cluster_design_and_integration`            | [x] Done | 26625e4 |

## Group general — general/base specifications

Status: **4/5** completed

| Article                     | Status | Commit ID |
| ---------------------------- | -------- | ---------- |
| `platform_types`              | [x] Done | PR #120 |
| `bsw_general`                 | [x] Done | 2bc57c2 |
| `platform_types_2`            | [x] Done | PR #123 |
| `communication_stack_types`   | [x] Done | faa0806 |
| `tr_glossary`                 | [ ] Aligned 📖 | c19bc75 |

## Group globaltime — global time cluster (new section)

Status: **3/4** completed

| Article    | Status | Commit ID |
| ----------- | -------- | ---------- |
| `stbm`       | [x] Done | 53cd591 |
| `can_tsyn`   | [x] Done | 364c4fd |
| `eth_tsyn`   | [x] Done | 8f01771 |
| `fr_tsyn`    | [ ] Pending | N/A |

## Group io — IO section wrap-up

Status: **7/7** completed

| Article       | Status | Commit ID |
| -------------- | -------- | ---------- |
| `dio_driver`    | [x] Done | de11d8a/493ed12/e21067f |
| `port_driver`   | [x] Done | ee486aa |
| `pwm_driver`    | [x] Done | 1b5e44b |
| `ocu_driver`    | [x] Done | b156916 |
| `icu_driver`    | [x] Done | d11d759/9cb8764 |
| `adc_driver`    | [x] Done | 3d8dd12/625d437 |
| `iohwab`        | [x] Done | 72a103c |

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
| `mcu`        | [x] Done | 2f0e714 |
| `gpt`        | [x] Done | 065baee |
| `coretest`   | [x] Done | 1abff90 |

## Group memory — memory section

Status: **2/12** completed

| Article                        | Status | Commit ID |
| ------------------------------- | -------- | ---------- |
| `memory_access`                  | [x] Done | PR #131 |
| `memory_mapping`                 | [x] Done | PR #144 |
| `bulk_nv_data_manager`           | [ ] Aligned 🔶 | df7fb88 |
| `flash_driver`                   | [ ] Aligned 🔶 | df7fb88 |
| `nvram_manager`                  | [ ] Aligned 🔶 | df7fb88 |
| `flash_eeprom_emulation`         | [ ] Aligned ⚠️ | df7fb88 |
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
| `basic_software_mode_manager`   | [ ] Aligned ✅ | PR #70 |
| `ecu_state_manager`             | [x] Done | 37ee564 |

## Group rte-swarch — RTE / SWArch section (new section)

Status: **0/2** completed

| Article | Status | Commit ID |
| ------- | -------- | ---------- |
| `rte`    | [ ] Aligned | 67b0783 |
| `arti`   | [ ] Aligned | 89cd317 |

## Group safety — safety section (new section)

Status: **3/3** completed

| Article | Status | Commit ID |
| -------- | -------- | ---------- |
| `wdgm`    | [x] Done | 24c7a36 |
| `wdgif`   | [x] Done | 24c7a36 |
| `wdg`     | [x] Done | 24c7a36 |

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
| `det`                           | [x] Done | 30510c9 |
| `function_inhibition_manager`   | [x] Done | 534d5d1 |
| `time_service`                  | [x] Done | 5c57d0a |
| `comm`                          | [ ] Pending | N/A |
| `swcluc`                        | [ ] Pending | N/A |
| `hwtestmanager`                 | [ ] Pending | N/A |
| `operating_system`              | [x] Done | ca7ecda |

**Total: 67/146 queue rows complete.**

