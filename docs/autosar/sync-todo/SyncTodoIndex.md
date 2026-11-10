# All Sync Todo Articles by Group

Generated from all Group files in the corpus's `sync-todo/` — articles ordered by group, then by appearance order within each group. Regenerate with `gen_sync_todo_index.py` (autosar-translate scripts).

Status `Done` = all 6 queue steps complete (translation merged). Status `Aligned` = the article already exists on the site but the queue steps are not ticked — the remaining steps are an alignment pass, not a fresh translation (the row's ✅/🔶/⚠️/📖 marker is kept). Status `Pending` = the article does not exist yet. Commit ID = the translation commit sha(s) or PR recorded on the queue row, resolved to 10-character commit ids (PR numbers are resolved to the PR's merge commit, or head commit while open; falling back to the commit that added the article); `N/A` = work not started.

## finished rows — condensed archive

Status: **206/206** completed

| Article                                              | Status | Commit ID |
| ----------------------------------------------------- | -------- | ---------- |
| `dio_driver`                                           | [x] Done | de11d8ac0f/493ed125e3/e21067fbde/04a009f814/a5e12c26cc |
| `port_driver`                                          | [x] Done | ee486aa54f |
| `pwm_driver`                                           | [x] Done | 1b5e44b812/b156916583 |
| `ocu_driver`                                           | [x] Done | b156916583/05418fb56d |
| `icu_driver`                                           | [x] Done | d11d759ec8/9cb876443e |
| `adc_driver`                                           | [x] Done | 3d8dd128be/625d4371a6 |
| `iohwab`                                               | [x] Done | 72a103c0ff |
| `platform_types`                                       | [x] Done | 439597529a |
| `bsw_general`                                          | [x] Done | 2bc57c2cd4 |
| `platform_types_2`                                     | [x] Done | d773247410 |
| `communication_stack_types`                            | [x] Done | faa08069ee |
| `crypto_service_manager`                               | [x] Done | fd2aecd11c |
| `crypto_driver`                                        | [x] Done | 8b73b6f312 |
| `cryif`                                                | [x] Done | c2cba4b51d |
| `keym`                                                 | [x] Done | 6e52dcabd4 |
| `det`                                                  | [x] Done | 30510c9c38 |
| `function_inhibition_manager`                          | [x] Done | 534d5d1099 |
| `time_service`                                         | [x] Done | 5c57d0ae39 |
| `comm`                                                 | [x] Done | bcf713dc1e |
| `swcluc`                                               | [x] Done | f1a0b2aacb |
| `hwtestmanager`                                        | [x] Done | 04ea38b015 |
| `operating_system`                                     | [x] Done | ca7ecda991/fb8e565e59 |
| `basic_software_mode_manager`                          | [x] Done | e7b893ebd0 |
| `ecu_state_manager`                                    | [x] Done | 37ee564d4a |
| `diagnostic_event_manager`                             | [x] Done | c5b4a2573a/1f4ef620ea/c9eb3709fa/3b24e95ff4/bef51d2d9f/e0a20f35f2/b53d64314d/7a0055d779 |
| `j1939dcm`                                             | [x] Done | 8795b71e19 |
| `diagnostic_communication_manager`                     | [x] Done | 24c7a36bc4 |
| `memory_access`                                        | [x] Done | 702c88d1ac/afacc025ee |
| `memory_mapping`                                       | [x] Done | fc5a540d1b |
| `bulk_nv_data_manager`                                 | [x] Done | 6cfad2ce54 |
| `flash_driver`                                         | [x] Done | 34fa711bc1 |
| `nvram_manager`                                        | [x] Done | afba0fe5cc |
| `flash_eeprom_emulation`                               | [x] Done | b440607173 |
| `ea`                                                   | [x] Done | b19e4a8438 |
| `eep`                                                  | [x] Done | 75b9fcfe56 |
| `memory_abstraction_interface`                         | [x] Done | df003cd278 |
| `memory_driver`                                        | [x] Done | 04145b57b0 |
| `flstst`                                               | [x] Done | 1040e9ecb1 |
| `ramtst`                                               | [x] Done | 95babf9d9d |
| `can_network_management`                               | [x] Done | 3a7fa89890 |
| `udp_network_management`                               | [x] Done | 3a7fa89890 |
| `can_driver`                                           | [x] Done | 3a7fa89890 |
| `can_transceiver_driver`                               | [x] Done | e48b58e604/3a7fa89890 |
| `pdu_router`                                           | [x] Done | f915d45a5d/3a7fa89890 |
| `ethernet_interface`                                   | [x] Done | a08b183bbd/3a7fa89890 |
| `lin_interface`                                        | [x] Done | c6dd02bec7/aad6b219b2/3a7fa89890 |
| `com_based_transformer`                                | [x] Done | 3562899b14/3a7fa89890 |
| `e2e_transformer`                                      | [x] Done | 4d5ff96f15/3a7fa89890 |
| `data_distribution`                                    | [x] Done | b2c1ffb46a/3a7fa89890 |
| `sec_oc`                                               | [x] Done | 3d584a281f/3a7fa89890 |
| `soad`                                                 | [x] Done | 1b9bf69034 |
| `mirror`                                               | [x] Done | c3e84ef8da |
| `ethernet_switch_driver`                               | [x] Done | 7f5fc5ecc6/3a7fa89890 |
| `service_discovery`                                    | [x] Done | 23b20e5f63/3a7fa89890 |
| `com`                                                  | [x] Done | 17cdb70608/3a7fa89890 |
| `cansm`                                                | [x] Done | a803400f8b/3a7fa89890 |
| `cantp`                                                | [x] Done | 5e2624deac/3a7fa89890 |
| `tcpip`                                                | [x] Done | bcbd61e4de/3a7fa89890 |
| `nm`                                                   | [x] Done | 5036abf611/3a7fa89890 |
| `ethsm`                                                | [x] Done | 37c98ecaf5/3a7fa89890 |
| `ipdum`                                                | [x] Done | 5cef2ca1e3/3a7fa89890 |
| `someipxf`                                             | [x] Done | e4115620c1/3a7fa89890 |
| `someiptp`                                             | [x] Done | af4d193edc/3a7fa89890 |
| `mcu`                                                  | [x] Done | 2f0e714db9 |
| `gpt`                                                  | [x] Done | 065baee97a |
| `coretest`                                             | [x] Done | 1abff90a9d |
| `stbm`                                                 | [x] Done | 53cd591142 |
| `can_tsyn`                                             | [x] Done | 364c4fd73b |
| `eth_tsyn`                                             | [x] Done | 8f01771012 |
| `fr_tsyn`                                              | [x] Done | N/A |
| `crc`                                                  | [x] Done | 209cfc516e |
| `e2e`                                                  | [x] Done | cd14a65a1f |
| `bfx`                                                  | [x] Done | b11a2267b0 |
| `bmc`                                                  | [x] Done | 18f9ee615e |
| `mfl`                                                  | [x] Done | f47a7eedbd |
| `mfx`                                                  | [x] Done | 71821da882 |
| `ifl`                                                  | [x] Done | da855e37e2 |
| `ifx`                                                  | [x] Done | 1089ec8205 |
| `efx`                                                  | [x] Done | bed2f8cc85 |
| `wdgm`                                                 | [x] Done | 24c7a36bc4 |
| `wdgif`                                                | [x] Done | 24c7a36bc4 |
| `wdg`                                                  | [x] Done | 24c7a36bc4 |
| `firewall`                                             | [x] Done | 4bed1dd8b2 |
| `idsm`                                                 | [x] Done | 4bed1dd8b2 |
| `rte`                                                  | [x] Done | 67b0783783/bc7d8e6ba7/585938bd00/278e287f00/8f94429a1c/b4861ac7df/9143a4a8cc/011c5992f1 |
| `arti`                                                 | [x] Done | b4861ac7df |
| `spi`                                                  | [x] Done | be171a1b1c |
| `ldcom`                                                | [x] Done | 6e4865a2a5 |
| `lsdu`                                                 | [x] Done | 6e4865a2a5 |
| `dlt`                                                  | [x] Done | 6e4865a2a5 |
| `doip`                                                 | [x] Done | 6e4865a2a5 |
| `xcp`                                                  | [x] Done | 6e4865a2a5 |
| `canxl_driver`                                         | [x] Done | fa81322ae9 |
| `canxl_transceiver_driver`                             | [x] Done | fa81322ae9 |
| `eth_trcv`                                             | [x] Done | fa81322ae9 |
| `wlan_driver`                                          | [x] Done | fa81322ae9 |
| `wlan_transceiver_driver`                              | [x] Done | fa81322ae9 |
| `flexray_driver`                                       | [x] Done | fa81322ae9 |
| `flexray_interface`                                    | [x] Done | 51bd5a4c8f |
| `flexray_nm`                                           | [x] Done | 51bd5a4c8f |
| `flexray_sm`                                           | [x] Done | 51bd5a4c8f |
| `flexray_trcv`                                         | [x] Done | 51bd5a4c8f |
| `flexray_ar_tp`                                        | [x] Done | 51bd5a4c8f |
| `flexray_iso_tp`                                       | [x] Done | a65bdecb4d |
| `linsm`                                                | [x] Done | N/A |
| `lintrcv`                                              | [x] Done | N/A |
| `ttcan_driver`                                         | [x] Done | N/A |
| `ttcan_interface`                                      | [x] Done | N/A |
| `j1939nm`                                              | [x] Done | N/A |
| `j1939rm`                                              | [x] Done | N/A |
| `j1939tp`                                              | [x] Done | N/A |
| `ieee1722tp`                                           | [x] Done | N/A |
| `macsec`                                               | [x] Done | N/A |
| `cellularv2x_driver`                                   | [x] Done | 634ea53841 |
| `chargingmanager`                                      | [x] Done | 634ea53841 |
| `chinesev2x_mgmt`                                      | [x] Done | 634ea53841 |
| `chinesev2x_msg`                                       | [x] Done | 634ea53841 |
| `chinesev2x_net`                                       | [x] Done | 634ea53841 |
| `chinesev2x_sec`                                       | [x] Done | 634ea53841 |
| `v2x_basictp`                                          | [x] Done | 634ea53841 |
| `v2x_datamgr`                                          | [x] Done | 634ea53841 |
| `v2x_facilities`                                       | [x] Done | 634ea53841 |
| `v2x_geonet`                                           | [x] Done | 634ea53841 |
| `v2x_mgmt`                                             | [x] Done | 634ea53841 |
| `exp vfb`                                              | [x] Done | d6cf2ec55c |
| `exp layered_software_architecture`                    | [x] Done | f60d11a303 |
| `exp vfb`                                              | [x] Done | d6cf2ec55c |
| `exp bsw_distribution_guide`                           | [x] Done | 668adfc728 |
| `exp application_level_error_handling`                 | [x] Done | 52d4d5c646 |
| `exp error_description`                                | [x] Done | 9088a60a46 |
| `exp cdd_design_and_integration`                       | [x] Done | 4e5d294ed6 |
| `exp utilization_of_crypto_services`                   | [x] Done | bcbaf51a17 |
| `exp macro_encapsulation_of_interpolation_calls`       | [x] Done | f385e42b04 |
| `exp firmware_over_the_air`                            | [x] Done | 30ee49dcbe |
| `exp adas_vmc`                                         | [x] Done | a8f5273bc0 |
| `exp body_and_comfort`                                 | [x] Done | 9055f2593a |
| `exp chassis`                                          | [x] Done | b1f1d8aff6 |
| `exp hmi`                                              | [x] Done | 29ee0f30c0 |
| `exp occupant_safety`                                  | [x] Done | ed312b3ecd |
| `exp powertrain`                                       | [x] Done | 790911157f |
| `exp user_guide`                                       | [x] Done | 2453865a8c |
| `exp arti`                                             | [x] Done | 89cd317758 |
| `exp functional_safety_measures`                       | [x] Done | c1ed1dacae |
| `exp safety_use_case`                                  | [x] Done | 5fa1e61af2 |
| `exp sw_cluster_design_and_integration`                | [x] Done | 26625e4b1b |
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
| `rs_project_objectives`                                | [x] Done | N/A |
| `rs_ieee1722`                                          | [x] Done | N/A |
| `rs_debug_trace_profile`                               | [x] Done | N/A |
| `rs_someip_service_discovery_protocol`                 | [x] Done | N/A |
| `prs_v2x_remote_access_layer`                          | [x] Done | N/A |
| `rs_ipsec_protocol`                                    | [x] Done | N/A |
| `rs_security_extract_template`                         | [x] Done | N/A |
| `rs_feature_model_exchange_format`                     | [x] Done | N/A |
| `prs_secoc_protocol`                                   | [x] Done | N/A |
| `rs_data_distribution_service`                         | [x] Done | N/A |
| `prs_network_management_protocol`                      | [x] Done | N/A |
| `rs_e2e`                                               | [x] Done | N/A |
| `rs_intrusion_detection_system`                        | [x] Done | 9633fc6c49 |
| `rs_firewall`                                          | [x] Done | N/A |
| `rs_health_monitoring`                                 | [x] Done | N/A |
| `rs_someip_protocol`                                   | [x] Done | N/A |
| `rs_macsec`                                            | [x] Done | N/A |
| `rs_methodology`                                       | [x] Done | N/A |
| `prs_intrusion_detection_system`                       | [x] Done | N/A |
| `rs_timing_extensions`                                 | [x] Done | N/A |
| `rs_safety`                                            | [x] Done | 54a40d4c97 |
| `rs_network_management`                                | [x] Done | 54a40d4c97 |
| `rs_main`                                              | [x] Done | 54a40d4c97 |
| `rs_log_and_trace`                                     | [x] Done | 54a40d4c97 |
| `rs_time_sync`                                         | [x] Done | 54a40d4c97 |
| `rs_standardization_template`                          | [x] Done | 54a40d4c97 |
| `prs_time_sync_protocol`                               | [x] Done | 54a40d4c97 |
| `prs_someip_protocol`                                  | [x] Done | 54a40d4c97 |
| `rs_diagnostics`                                       | [x] Done | 54a40d4c97 |
| `prs_someip_service_discovery_protocol`                | [x] Done | 54a40d4c97 |
| `prs_log_and_trace_protocol`                           | [x] Done | 0ee8268610 |
| `prs_e2e_protocol`                                     | [x] Done | 2d7fe61a89 |
| `rs_ecu_resource_template`                             | [x] Done | 79587d7a2f |
| `rs_ecu_configuration`                                 | [x] Done | 5d8eb30676 |
| `rs_bsw_module_description_template`                   | [x] Done | fc72209304 |
| `rs_system_template`                                   | [x] Done | 2ab72497dd |
| `tps_ecu_resource_template`                            | [x] Done | ffe57b8b33 |
| `rs_diagnostic_extract_template`                       | [x] Done | da4d88ee67 |
| `rs_software_component_template`                       | [x] Done | 0afb28def3 |
| `tr_franca_integration`                                | [x] Done | 8498905825 |
| `tr_general_blueprints_supplement`                     | [x] Done | b3f31e42eb |
| `tr_modeling_show_cases`                               | [x] Done | d1f2094f72 |

## unfinished rows — open work

Status: **0/8** completed

| Article                                      | Status | Commit ID |
| --------------------------------------------- | -------- | ---------- |
| `tps_timing_extensions`                        | [ ] Pending | N/A |
| `tps_ecu_configuration`                        | [ ] Pending | N/A |
| `basic_software_module_description_template`   | [ ] Pending | N/A |
| `tr_methodology`                               | [ ] Pending | N/A |
| `tps_diagnostic_extract_template`              | [ ] Pending | N/A |
| `tps_software_component_template`              | [ ] Pending | N/A |
| `tps_system_template`                          | [ ] Pending | N/A |
| `tps_generic_structure_template`               | [ ] Pending | 59a89a8fa4 |

**Total: 206/214 queue rows complete.**

