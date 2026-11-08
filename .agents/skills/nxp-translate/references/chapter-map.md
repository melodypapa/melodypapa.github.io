# Chapter map — S32G3 Reference Manual

Baseline: `S32G3RM Rev. 5, 2025-09-17`, 5101 pages,
`reference-docs/nxp/s32g3/reference_manual/RMS32G3.pdf`.

**One numbered chapter = one article** at
`docs/nxp/s32g3/chNN_<slug>/index.md`. The table below is the source of truth
for the target directory and nav title; do not derive a filename from a chapter
title on the fly. Chapters are zero-padded (`ch01`…`ch81`) so lexical file
order equals chapter order.

## Outline shape

`doc.get_toc()` has 5334 entries at levels 1–10. Numbered chapters are exactly
**81**, contiguous 1–81:

- Chapters **1–4** are level-1 outline entries.
- Chapters **5–81** are level-2 entries nested under 11 unnumbered level-1
  **group headers** (used to group the `## 文章` list on the landing page):

  | Group header | Chapters | Start page |
  | --- | --- | --- |
  | `Chapter 5-23: System Modules` | 5–23 | 115 |
  | `Chapter 24-28: Clocking` | 24–28 | 872 |
  | `Chapter 29-31: Reset and Boot` | 29–31 | 1230 |
  | `Chapter 32-35: Power Management` | 32–35 | 1372 |
  | `Chapter 36-40: Memories and Memory I/Fs` | 36–40 | 1602 |
  | `Chapter 41-45: Timers` | 41–45 | 2209 |
  | `Chapter 46-57: Communication Modules` | 46–57 | 2393 |
  | `Chapter 58-60: Analog Modules` | 58–60 | 3321 |
  | `Chapter 61-65: Security` | 61–65 | 3552 |
  | `Chapter 66-77: Safety` | 66–77 | 3644 |
  | `Debug` | 78–81 | 4924 |

  The `Debug` header has no `Chapter NN-NN:` prefix and shares p4924 with
  `78 Debug`; it is still a group header, not a chapter.

- Chapter page range = outline start → (next chapter's start − 1). Chapter 81
  ends at **p5082**, before appendix A.
- **Droppable chrome** (never an article): cover, `Contents` (p2),
  `A General Changes` (p5083), `B Release notes` (p5084), `Legal information`
  (p5098), and the group headers themselves.

Regenerate the inventory after any revision change. Assert 81 contiguous
chapters before consuming it:

```bash
python3 - <<'PY'
import pymupdf, re
d = pymupdf.open('reference-docs/nxp/s32g3/reference_manual/RMS32G3.pdf')
ch = [(int(m.group(1)), m.group(2).strip(), p)
      for lvl, title, p in d.get_toc()
      if lvl <= 2 and (m := re.match(r'^(\d+)\s+(.+)$', title))]
assert [n for n, _, _ in ch] == list(range(1, 82)), 'chapter inventory drifted'
for n, title, start in ch:
    end = (next(p for k, _, p in ch if k == n + 1) - 1) if n < 81 else 5082
    print(f'| {n} | {title} | {start}-{end} |')
PY
```

`scripts/extract_chapter.py` uses the same `parse_chapters()` / `chapter_range()`
logic and fails loudly when the outline no longer has 81 contiguous chapters.

## Chapters

| Ch | Source chapter title | PDF pages | Article directory | Nav title |
| --- | --- | --- | --- | --- |
| 1 | About This Manual | 96-105 | `ch01_about_this_manual` | 关于本手册 (**About This Manual**) |
| 2 | Introduction | 106-112 | `ch02_introduction` | 简介 (**Introduction**) |
| 3 | Memory Map | 113-113 | `ch03_memory_map` | 存储器映射 (**Memory Map**) |
| 4 | Signal Description | 114-114 | `ch04_signal_description` | 信号描述 (**Signal Description**) |
| 5 | Arm Modules | 115-129 | `ch05_arm_modules` | Arm 模块 (**Arm Modules**) |
| 6 | Network-on-Chip (NoC) | 130-133 | `ch06_network_on_chip_noc` | 片上网络 (**NoC**) |
| 7 | Ncore | 134-250 | `ch07_ncore` | Ncore |
| 8 | Miscellaneous System Control Module (MSCM) | 251-318 | `ch08_miscellaneous_system_control_module_mscm` | 杂项系统控制模块 (**MSCM**) |
| 9 | Miscellaneous Control Module (MCM) | 319-336 | `ch09_miscellaneous_control_module_mcm` | 杂项控制模块 (**MCM**) |
| 10 | A53 Cluster General Purpose Registers (A53_GPR) | 337-371 | `ch10_a53_cluster_general_purpose_registers_a53_gpr` | A53 簇通用寄存器 (**A53_GPR**) |
| 11 | CORTEXM7 Cluster General Purpose Registers (CM7_GPR) | 372-373 | `ch11_cortexm7_cluster_general_purpose_registers_cm7_gpr` | CM7 簇通用寄存器 (**CM7_GPR**) |
| 12 | Enhanced Direct Memory Access (eDMA) | 374-430 | `ch12_enhanced_direct_memory_access_edma` | 增强型直接存储器访问 (**eDMA**) |
| 13 | DMA CRC Module (DMA_CRC) | 431-440 | `ch13_dma_crc_module_dma_crc` | DMA CRC 模块 (**DMA_CRC**) |
| 14 | Direct Memory Access Multiplexer (DMAMUX) | 441-450 | `ch14_direct_memory_access_multiplexer_dmamux` | 直接存储器访问多路复用器 (**DMAMUX**) |
| 15 | Extended Resource Domain Controller (XRDC) | 451-599 | `ch15_extended_resource_domain_controller_xrdc` | 扩展资源域控制器 (**XRDC**) |
| 16 | System Integration Unit Lite2 (SIUL2) | 600-772 | `ch16_system_integration_unit_lite2_siul2` | 系统集成单元 Lite2 (**SIUL2**) |
| 17 | Semaphores2 (SEMA42) | 773-780 | `ch17_semaphores2_sema42` | 信号量 2 (**SEMA42**) |
| 18 | System Resource Controller (SRC_0) | 781-803 | `ch18_system_resource_controller_src_0` | 系统资源控制器 (**SRC_0**) |
| 19 | System Resource Controller (SRC_1) | 804-829 | `ch19_system_resource_controller_src_1` | 系统资源控制器 (**SRC_1**) |
| 20 | System Resource Controller GPR TOP (SRC_GPR_TOP) | 830-839 | `ch20_system_resource_controller_gpr_top_src_gpr_top` | 系统资源控制器 GPR TOP (**SRC_GPR_TOP**) |
| 21 | Standby General Purpose Registers (STDBY GPR) | 840-841 | `ch21_standby_general_purpose_registers_stdby_gpr` | 待机通用寄存器 (**STDBY GPR**) |
| 22 | Register Protection (REG_PROT) | 842-853 | `ch22_register_protection_reg_prot` | 寄存器保护 (**REG_PROT**) |
| 23 | Wakeup Unit (WKPU) | 854-871 | `ch23_wakeup_unit_wkpu` | 唤醒单元 (**WKPU**) |
| 24 | Clocking | 872-943 | `ch24_clocking` | 时钟 (**Clocking**) |
| 25 | Clock Generation Module (MC_CGM) | 944-1174 | `ch25_clock_generation_module_mc_cgm` | 时钟生成模块 (**MC_CGM**) |
| 26 | Digital Frequency Synthesizer (DFS) | 1175-1183 | `ch26_digital_frequency_synthesizer_dfs` | 数字频率合成器 (**DFS**) |
| 27 | PLL Digital Interface (PLLDIG) | 1184-1222 | `ch27_pll_digital_interface_plldig` | PLL 数字接口 (**PLLDIG**) |
| 28 | Fast Crystal Oscillator Digital Controller (FXOSC) | 1223-1229 | `ch28_fast_crystal_oscillator_digital_controller_fxosc` | 快速晶体振荡器数字控制器 (**FXOSC**) |
| 29 | Reset | 1230-1271 | `ch29_reset` | 复位 (**Reset**) |
| 30 | Reset Generation Module (MC_RGM) | 1272-1319 | `ch30_reset_generation_module_mc_rgm` | 复位生成模块 (**MC_RGM**) |
| 31 | Boot | 1320-1371 | `ch31_boot` | 引导 (**Boot**) |
| 32 | Power Management | 1372-1396 | `ch32_power_management` | 电源管理 (**Power Management**) |
| 33 | Mode Entry Module (MC_ME) | 1397-1572 | `ch33_mode_entry_module_mc_me` | 模式进入模块 (**MC_ME**) |
| 34 | Power Control Unit (MC_PCU) | 1573-1575 | `ch34_power_control_unit_mc_pcu` | 电源控制单元 (**MC_PCU**) |
| 35 | Power Management Controller (PMC) | 1576-1601 | `ch35_power_management_controller_pmc` | 电源管理控制器 (**PMC**) |
| 36 | System RAM Controller (SRAMC) | 1602-1616 | `ch36_system_ram_controller_sramc` | 系统 RAM 控制器 (**SRAMC**) |
| 37 | DDR Subsystem | 1617-1921 | `ch37_ddr_subsystem` | DDR 子系统 (**DDR Subsystem**) |
| 38 | DDR General Purpose Registers (DDR_GPR) | 1922-1930 | `ch38_ddr_general_purpose_registers_ddr_gpr` | DDR 通用寄存器 (**DDR_GPR**) |
| 39 | Quad Serial Peripheral Interface (QuadSPI) | 1931-2058 | `ch39_quad_serial_peripheral_interface_quadspi` | 四线串行外设接口 (**QuadSPI**) |
| 40 | Ultra Secured Digital Host Controller (uSDHC) | 2059-2208 | `ch40_ultra_secured_digital_host_controller_usdhc` | 超高安全数字主机控制器 (**uSDHC**) |
| 41 | System Timer Module (STM) | 2209-2217 | `ch41_system_timer_module_stm` | 系统定时器模块 (**STM**) |
| 42 | Software Watchdog Timer (SWT) | 2218-2234 | `ch42_software_watchdog_timer_swt` | 软件看门狗定时器 (**SWT**) |
| 43 | Periodic Interrupt Timer (PIT) | 2235-2252 | `ch43_periodic_interrupt_timer_pit` | 周期性中断定时器 (**PIT**) |
| 44 | FlexTimer (FTM) | 2253-2380 | `ch44_flextimer_ftm` | 灵活定时器 (**FTM**) |
| 45 | Real Time Clock (RTC) | 2381-2392 | `ch45_real_time_clock_rtc` | 实时时钟 (**RTC**) |
| 46 | Inter-Integrated Circuit (I2C) | 2393-2440 | `ch46_inter_integrated_circuit_i2c` | 集成电路总线 (**I2C**) |
| 47 | Gigabit Ethernet Media Access Controller (GMAC) | 2441-2450 | `ch47_gigabit_ethernet_media_access_controller_gmac` | 千兆以太网媒体访问控制器 (**GMAC**) |
| 48 | Packet Forwarding Engine (PFE) | 2451-2456 | `ch48_packet_forwarding_engine_pfe` | 包转发引擎 (**PFE**) |
| 49 | LINFlexD | 2457-2536 | `ch49_linflexd` | LINFlexD |
| 50 | Serial Peripheral Interface (SPI) | 2537-2594 | `ch50_serial_peripheral_interface_spi` | 串行外设接口 (**SPI**) |
| 51 | CAN (FlexCAN) | 2595-2764 | `ch51_can_flexcan` | CAN (**FlexCAN**) |
| 52 | Timestamp | 2765-2766 | `ch52_timestamp` | 时间戳 (**Timestamp**) |
| 53 | SerDes Subsystem | 2767-2771 | `ch53_serdes_subsystem` | SerDes 子系统 |
| 54 | SerDes General Purpose Registers (SERDES_GPR) | 2772-2773 | `ch54_serdes_general_purpose_registers_serdes_gpr` | SerDes 通用寄存器 (**SERDES_GPR**) |
| 55 | Low Latency Communication Engine (LLCE) | 2774-2937 | `ch55_low_latency_communication_engine_llce` | 低延迟通信引擎 (**LLCE**) |
| 56 | Universal Serial Bus On-The-Go Controller (USBOTG) | 2938-3098 | `ch56_universal_serial_bus_on_the_go_controller_usbotg` | USB On-The-Go 控制器 (**USBOTG**) |
| 57 | FlexRay Communication Controller (FlexRay) | 3099-3320 | `ch57_flexray_communication_controller_flexray` | FlexRay 通信控制器 |
| 58 | Cross-Triggering Unit (CTU) | 3321-3380 | `ch58_cross_triggering_unit_ctu` | 交叉触发单元 (**CTU**) |
| 59 | Analog-to-Digital Converter (SAR_ADC) | 3381-3512 | `ch59_analog_to_digital_converter_sar_adc` | 模数转换器 (**SAR_ADC**) |
| 60 | Thermal Monitoring Unit (TMU) | 3513-3551 | `ch60_thermal_monitoring_unit_tmu` | 温度监测单元 (**TMU**) |
| 61 | Security | 3552-3558 | `ch61_security` | 信息安全 (**Security**) |
| 62 | Field Analysis Mechanisms | 3559-3560 | `ch62_field_analysis_mechanisms` | 现场分析机制 (**Field Analysis Mechanisms**) |
| 63 | Messaging Unit (MU) | 3561-3611 | `ch63_messaging_unit_mu` | 消息单元 (**MU**) |
| 64 | On-Chip One Time Programmable (OCOTP) Controller | 3612-3641 | `ch64_on_chip_one_time_programmable_ocotp_controller` | 片上一次性可编程控制器 (**OCOTP**) |
| 65 | Fusebox Controller (FBXC) | 3642-3643 | `ch65_fusebox_controller_fbxc` | 熔丝盒控制器 (**FBXC**) |
| 66 | Safety | 3644-3644 | `ch66_safety` | 功能安全 (**Safety**) |
| 67 | Error Reporting Module (ERM) | 3645-4108 | `ch67_error_reporting_module_erm` | 错误报告模块 (**ERM**) |
| 68 | Fault Collection and Control Unit (FCCU) | 4109-4170 | `ch68_fault_collection_and_control_unit_fccu` | 故障收集与控制单元 (**FCCU**) |
| 69 | RCCU Debug Unit (RDU) | 4171-4219 | `ch69_rccu_debug_unit_rdu` | RCCU 调试单元 (**RDU**) |
| 70 | Clock Monitoring Unit-Frequency Check (CMU_FC) | 4220-4240 | `ch70_clock_monitoring_unit_frequency_check_cmu_fc` | 时钟监测单元 - 频率检查 (**CMU_FC**) |
| 71 | Clock Monitoring Unit - Frequency Meter (CMU_FM) | 4241-4247 | `ch71_clock_monitoring_unit_frequency_meter_cmu_fm` | 时钟监测单元 - 频率测量 (**CMU_FM**) |
| 72 | Selftest Top General Purpose Registers (SELFTEST_GPR_TOP) | 4248-4250 | `ch72_selftest_top_general_purpose_registers_selftest_gpr_top` | 自测顶层通用寄存器 (**SELFTEST_GPR_TOP**) |
| 73 | Selftest General Purpose Registers (SELFTEST_GPR) | 4251-4256 | `ch73_selftest_general_purpose_registers_selftest_gpr` | 自测通用寄存器 (**SELFTEST_GPR**) |
| 74 | Self-Test Control Unit (STCU2) | 4257-4361 | `ch74_self_test_control_unit_stcu2` | 自测试控制单元 (**STCU2**) |
| 75 | Safety by Software (SBSW) | 4362-4412 | `ch75_safety_by_software_sbsw` | 软件功能安全 (**SBSW**) |
| 76 | Error Injection Module (EIM) | 4413-4910 | `ch76_error_injection_module_eim` | 错误注入模块 (**EIM**) |
| 77 | Cyclic Redundancy Check (CRC) Unit | 4911-4923 | `ch77_cyclic_redundancy_check_crc_unit` | 循环冗余校验单元 (**CRC**) |
| 78 | Debug | 4924-5014 | `ch78_debug` | 调试 (**Debug**) |
| 79 | JTAG Controller (JTAGC) | 5015-5023 | `ch79_jtag_controller_jtagc` | JTAG 控制器 (**JTAGC**) |
| 80 | JTAG Data Communication (JDC) | 5024-5032 | `ch80_jtag_data_communication_jdc` | JTAG 数据通信 (**JDC**) |
| 81 | Aurora Trace Port (ATP) Subsystem | 5033-5082 | `ch81_aurora_trace_port_atp_subsystem` | Aurora 跟踪端口子系统 (**ATP**) |

Slug rule (`slugify()` in `scripts/extract_chapter.py`): lowercase, every run of
non-alphanumeric characters → `_`, collapse repeats, trim. Identifier
underscores survive (`SRC_0` → `src_0`, `SELFTEST_GPR_TOP` →
`selftest_gpr_top`); hyphens and slashes become separators
(`Network-on-Chip (NoC)` → `network_on_chip_noc`).

## Progress ledger

81 full-chapter articles cannot be produced in one session. On the **first**
translation run create a persistent ledger so a resumed session never re-asks
scope decisions:

```
docs/nxp/s32g3/TODO.md            # one row per chapter: ❌ missing / ⚠️ partial / ✅ complete
docs/nxp/s32g3/sync-todo/index.md # batch order + resume rule (first unfinished row in chapter order)
docs/nxp/s32g3/sync-todo/Group-<group>.md  # one row per chapter with a 6-step sub-checklist
```

Add `nxp/s32g3/sync-todo/` and `nxp/s32g3/TODO.md` to `exclude_docs` in
`mkdocs.yml` (see the existing `autosar/sync-todo/` and `cortex/sync-todo/`
entries) — links to chapter pages not yet written would otherwise emit
`--strict` WARNINGs. Ledger files are written in English; quoted Chinese strings
only when they name an article heading. Tick a row only after its commit exists.
This map file is the chapter inventory; the ledger is the **status** record.
