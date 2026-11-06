# All Sync Todo Articles by Group

Generated from all Group files in `docs/autosar/sync-todo/` — articles ordered by group, then by appearance order within each group. Regenerate with `python .agents/skills/autosar-translate/scripts/gen_sync_todo_index.py`.

Status `Done` = all 6 queue steps complete (translation merged). Status `Aligned` = the article already exists on the site but the queue steps are not ticked — the remaining steps are an alignment pass, not a fresh translation (the row's ✅/🔶/⚠️/📖 marker is kept). Status `Pending` = the article does not exist yet. Commit ID = the translation commit sha(s) or PR recorded on the queue row, resolved to 10-character commit ids (PR numbers are resolved to the PR's merge commit, or head commit while open; falling back to the commit that added the article); `N/A` = work not started.

## Group communication-2 — communication section — remaining missing documents (38)

Status: **38/38** completed

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
| `flexray_iso_tp`             | [x] Done | b48b925ab3 |
| `linsm`                      | [x] Done | f303f4733c |
| `lintrcv`                    | [x] Done | 5796ad8a4b |
| `ttcan_driver`               | [x] Done | eec321065b |
| `ttcan_interface`            | [x] Done | f4c87c4d03 |
| `j1939nm`                    | [x] Done | b859ebfeee |
| `j1939rm`                    | [x] Done | b5e4e61ae3 |
| `j1939tp`                    | [x] Done | 983f3f3fd1 |
| `ieee1722tp`                 | [x] Done | 862dfbd774 |
| `macsec`                     | [x] Done | 70cf6ad088 |
| `cellularv2x_driver`         | [x] Done | 6c135f8841 |
| `chargingmanager`            | [x] Done | a466cf5646 |
| `chinesev2x_mgmt`            | [x] Done | 26c6677958 |
| `chinesev2x_msg`             | [x] Done | 716cb79d04 |
| `chinesev2x_net`             | [x] Done | c71e12219d |
| `chinesev2x_sec`             | [x] Done | 17badba165 |
| `v2x_basictp`                | [x] Done | 87d8b401e7 |
| `v2x_datamgr`                | [x] Done | 6fb566cf9f |
| `v2x_facilities`             | [x] Done | 18b886ce9d |
| `v2x_geonet`                 | [x] Done | ee33b94065 |
| `v2x_mgmt`                   | [x] Done | 87179488b5 |

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

## Group cp-methodology — CP R23-11 methodology and template documents (17)

Status: **0/17** completed

| Article                                      | Status | Commit ID |
| --------------------------------------------- | -------- | ---------- |
| `rs_ecu_resource_template`                     | [ ] Pending | N/A |
| `rs_ecu_configuration`                         | [ ] Pending | N/A |
| `rs_bsw_module_description_template`           | [ ] Pending | N/A |
| `rs_system_template`                           | [ ] Pending | N/A |
| `tps_ecu_resource_template`                    | [ ] Pending | N/A |
| `rs_diagnostic_extract_template`               | [ ] Pending | N/A |
| `rs_software_component_template`               | [ ] Pending | N/A |
| `tr_franca_integration`                        | [ ] Pending | N/A |
| `tr_general_blueprints_supplement`             | [ ] Pending | N/A |
| `tr_modeling_show_cases`                       | [ ] Pending | N/A |
| `tps_timing_extensions`                        | [ ] Pending | N/A |
| `tps_ecu_configuration`                        | [ ] Pending | N/A |
| `basic_software_module_description_template`   | [ ] Aligned 🔶 | 05b2b4d283 |
| `tr_methodology`                               | [ ] Pending | N/A |
| `tps_diagnostic_extract_template`              | [ ] Pending | N/A |
| `tps_software_component_template`              | [ ] Pending | N/A |
| `tps_system_template`                          | [ ] Pending | N/A |

## Group crypto — crypto section

Status: **4/4** completed

| Article                  | Status | Commit ID |
| ------------------------- | -------- | ---------- |
| `crypto_service_manager`   | [x] Done | fd2aecd11c |
| `crypto_driver`            | [x] Done | 8b73b6f312 |
| `cryif`                    | [x] Done | c2cba4b51d |
| `keym`                     | [x] Done | 6e52dcabd4 |

## Group diagnostics — diagnostics section

Status: **3/3** completed

| Article                            | Status | Commit ID |
| ----------------------------------- | -------- | ---------- |
| `diagnostic_event_manager`           | [x] Done | c5b4a2573a |
| `j1939dcm`                           | [x] Done | 8795b71e19 |
| `diagnostic_communication_manager`   | [x] Done | 24c7a36bc4 |

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

## Group foundation exp — Foundation R23-11 guide/template/report documents (20)

Status: **19/20** completed

| Article                                              | Status | Commit ID |
| ----------------------------------------------------- | -------- | ---------- |
| `tr_glossary`                                          | [x] Done | 2304e430af |
| `tr_list_of_known_issues_secure_hardware_extensions`   | [x] Done | 4f4954edaf |
| `exp_system_health_monitoring`                         | [x] Done | 4320445302 |
| `tr_predefined_names`                                  | [x] Done | 912e70e784 |
| `exp_time_sensitive_network_features`                  | [x] Done | 442b230f28 |
| `exp_security_overview`                                | [x] Done | 510d645cab |
| `tr_release_overview`                                  | [x] Done | 55e2c9981a |
| `exp_sw_architectural_decisions`                       | [x] Done | f3fd5cdd27 |
| `tps_log_and_trace_extract`                            | [x] Done | 61cda1da7e |
| `exp_safety_overview`                                  | [x] Done | 123e21b1d7 |
| `tps_arxml_serialization_rules`                        | [x] Done | b1ec226151 |
| `asws_health_monitoring`                               | [x] Done | e956feb4ea |
| `tps_abstract_platform_specification`                  | [x] Done | 510c6d7fdf |
| `tps_xml_schema_production_rules`                      | [x] Done | 07a9324cd2 |
| `tr_secure_hardware_extensions`                        | [x] Done | 7b7ea04490 |
| `tps_security_extract_template`                        | [x] Done | 2329c2d702 |
| `tps_feature_model_exchange_format`                    | [x] Done | 2c5f4f13fd |
| `tr_timing_analysis`                                   | [x] Done | 66da8d4b1e |
| `tps_standardization_template`                         | [x] Done | ceefe4f4c5 |
| `tps_generic_structure_template`                       | [ ] Pending | N/A |

## Group foundation rs-prs — Foundation R23-11 requirement/protocol specifications (32)

Status: **0/32** completed

| Article                                 | Status | Commit ID |
| ---------------------------------------- | -------- | ---------- |
| `rs_project_objectives`                   | [ ] Aligned 📖 | 95d7986cd1 |
| `rs_ieee1722`                             | [ ] Aligned 📖 | 028dd7ea88 |
| `rs_debug_trace_profile`                  | [ ] Aligned 📖 | f28eafa078 |
| `rs_someip_service_discovery_protocol`    | [ ] Aligned 📖 | 0e536fd13a |
| `prs_v2x_remote_access_layer`             | [ ] Aligned 📖 | 6e51384804 |
| `rs_ipsec_protocol`                       | [ ] Aligned 📖 | 863e7bbaf1 |
| `rs_security_extract_template`            | [ ] Aligned 📖 | 514a98594f |
| `rs_feature_model_exchange_format`        | [ ] Aligned 📖 | 51b6edc43c |
| `prs_secoc_protocol`                      | [ ] Aligned 📖 | 31f19c6170 |
| `rs_data_distribution_service`            | [ ] Aligned 📖 | d4fc9c84a9 |
| `prs_network_management_protocol`         | [ ] Aligned 📖 | e697220422 |
| `rs_e2e`                                  | [ ] Aligned 📖 | 98449031eb |
| `rs_intrusion_detection_system`           | [ ] Aligned 📖 | 9633fc6c49 |
| `rs_firewall`                             | [ ] Aligned 📖 | 3eee29aad4 |
| `rs_health_monitoring`                    | [ ] Aligned 📖 | 8963b6b02e |
| `rs_someip_protocol`                      | [ ] Aligned 📖 | 192ba3b317 |
| `rs_macsec`                               | [ ] Aligned 📖 | 869f13413b |
| `rs_methodology`                          | [ ] Aligned 📖 | 7d20050f40 |
| `prs_intrusion_detection_system`          | [ ] Aligned 📖 | 6f90eac477 |
| `rs_timing_extensions`                    | [ ] Aligned 📖 | 234e015dcc |
| `rs_safety`                               | [ ] Pending | N/A |
| `rs_network_management`                   | [ ] Pending | N/A |
| `rs_main`                                 | [ ] Pending | N/A |
| `rs_log_and_trace`                        | [ ] Pending | N/A |
| `rs_time_sync`                            | [ ] Pending | N/A |
| `rs_standardization_template`             | [ ] Pending | N/A |
| `prs_time_sync_protocol`                  | [ ] Pending | N/A |
| `prs_someip_protocol`                     | [ ] Pending | N/A |
| `rs_diagnostics`                          | [ ] Pending | N/A |
| `prs_someip_service_discovery_protocol`   | [ ] Pending | N/A |
| `prs_log_and_trace_protocol`              | [ ] Pending | N/A |
| `prs_e2e_protocol`                        | [ ] Pending | N/A |

## Group general — general/base specifications

Status: **4/4** completed

| Article                     | Status | Commit ID |
| ---------------------------- | -------- | ---------- |
| `platform_types`              | [x] Done | 439597529a |
| `bsw_general`                 | [x] Done | 2bc57c2cd4 |
| `platform_types_2`            | [x] Done | d773247410 |
| `communication_stack_types`   | [x] Done | faa08069ee |

## Group globaltime — global time cluster (new section)

Status: **4/4** completed

| Article    | Status | Commit ID |
| ----------- | -------- | ---------- |
| `stbm`       | [x] Done | 53cd591142 |
| `can_tsyn`   | [x] Done | 364c4fd73b |
| `eth_tsyn`   | [x] Done | 8f01771012 |
| `fr_tsyn`    | [x] Done | 05b2b4d283 |

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

Status: **9/9** completed

| Article | Status | Commit ID |
| ------ | -------- | ---------- |
| `crc`   | [x] Done | 209cfc516e |
| `e2e`   | [x] Done | cd14a65a1f |
| `bfx`   | [x] Done | b11a2267b0 |
| `bmc`   | [x] Done | 18f9ee615e |
| `mfl`   | [x] Done | f47a7eedbd |
| `mfx`   | [x] Done | 71821da882 |
| `ifl`   | [x] Done | da855e37e2 |
| `ifx`   | [x] Done | 1089ec8205 |
| `efx`   | [x] Done | bed2f8cc85 |

## Group mcal — MCAL section (new section)

Status: **3/3** completed

| Article    | Status | Commit ID |
| ----------- | -------- | ---------- |
| `mcu`        | [x] Done | 2f0e714db9 |
| `gpt`        | [x] Done | 065baee97a |
| `coretest`   | [x] Done | 1abff90a9d |

## Group memory — memory section

Status: **12/12** completed

| Article                        | Status | Commit ID |
| ------------------------------- | -------- | ---------- |
| `memory_access`                  | [x] Done | 922364777e |
| `memory_mapping`                 | [x] Done | 89900677f4 |
| `bulk_nv_data_manager`           | [x] Done | 05b2b4d283 |
| `flash_driver`                   | [x] Done | 05b2b4d283 |
| `nvram_manager`                  | [x] Done | 0358128113 |
| `flash_eeprom_emulation`         | [x] Done | 05b2b4d283 |
| `ea`                             | [x] Done | b19e4a8438 |
| `eep`                            | [x] Done | 75b9fcfe56 |
| `memory_abstraction_interface`   | [x] Done | df003cd278 |
| `memory_driver`                  | [x] Done | 04145b57b0 |
| `flstst`                         | [x] Done | 1040e9ecb1 |
| `ramtst`                         | [x] Done | 95babf9d9d |

## Group mode_management — mode management section

Status: **1/2** completed

| Article                       | Status | Commit ID |
| ------------------------------ | -------- | ---------- |
| `basic_software_mode_manager`   | [ ] Aligned ✅ | e7b893ebd0 |
| `ecu_state_manager`             | [x] Done | 37ee564d4a |

## Group rte-swarch — RTE / SWArch section (new section)

Status: **0/2** completed

| Article | Status | Commit ID |
| ------- | -------- | ---------- |
| `rte`    | [ ] Aligned | 67b0783783 |
| `arti`   | [ ] Aligned | 05b2b4d283 |

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

Status: **7/7** completed

| Article                       | Status | Commit ID |
| ------------------------------ | -------- | ---------- |
| `det`                           | [x] Done | 30510c9c38 |
| `function_inhibition_manager`   | [x] Done | 534d5d1099 |
| `time_service`                  | [x] Done | 5c57d0ae39 |
| `comm`                          | [x] Done | bcf713dc1e |
| `swcluc`                        | [x] Done | f1a0b2aacb |
| `hwtestmanager`                 | [x] Done | 04ea38b015 |
| `operating_system`              | [x] Done | ca7ecda991 |

**Total: 159/197 queue rows complete.**

