# S32G3 Reference Manual Translation Progress

> Maintained by the `nxp-translate` skill; update the touched row after every sync.
> Status: ✅ complete · ⚠️ partial · ❌ missing
> Baseline: S32G3RM Rev. 5, 2025-09-17 · Last updated: 2026-11-13

## Overview

| Status | Chapters |
| --- | --- |
| ✅ | 7 |
| ⚠️ | 4 |
| ❌ | 70 |
| Total | 81 |

## Chapters

| Ch | Source chapter | Status | Article |
| --- | --- | --- | --- |
| 1 | About This Manual | ❌ | — |
| 2 | Introduction | ❌ | — |
| 3 | Memory Map | ❌ | — |
| 4 | Signal Description | ❌ | — |
| 5 | Arm Modules | ❌ | — |
| 6 | Network-on-Chip (NoC) | ❌ | — |
| 7 | Ncore | ❌ | — |
| 8 | Miscellaneous System Control Module (MSCM) | ❌ | — |
| 9 | Miscellaneous Control Module (MCM) | ❌ | — |
| 10 | A53 Cluster General Purpose Registers (A53_GPR) | ❌ | — |
| 11 | CORTEXM7 Cluster General Purpose Registers (CM7_GPR) | ❌ | — |
| 12 | Enhanced Direct Memory Access (eDMA) | ❌ | — |
| 13 | DMA CRC Module (DMA_CRC) | ❌ | — |
| 14 | Direct Memory Access Multiplexer (DMAMUX) | ❌ | — |
| 15 | Extended Resource Domain Controller (XRDC) | ❌ | — |
| 16 | System Integration Unit Lite2 (SIUL2) | ❌ | — |
| 17 | Semaphores2 (SEMA42) | ❌ | — |
| 18 | System Resource Controller (SRC_0) | ❌ | — |
| 19 | System Resource Controller (SRC_1) | ❌ | — |
| 20 | System Resource Controller GPR TOP (SRC_GPR_TOP) | ❌ | — |
| 21 | Standby General Purpose Registers (STDBY GPR) | ❌ | — |
| 22 | Register Protection (REG_PROT) | ❌ | — |
| 23 | Wakeup Unit (WKPU) | ❌ | — |
| 24 | Clocking | ✅ | [时钟（Clocking）](ch24_clocking/index.md) |
| 25 | Clock Generation Module (MC_CGM) | ✅ | [时钟生成模块（MC_CGM）](ch25_clock_generation_module_mc_cgm/index.md) |
| 26 | Digital Frequency Synthesizer (DFS) | ✅ | [数字频率合成器（DFS）](ch26_digital_frequency_synthesizer_dfs/index.md) |
| 27 | PLL Digital Interface (PLLDIG) | ✅ | [PLL 数字接口（PLLDIG）](ch27_pll_digital_interface_plldig/index.md) |
| 28 | Fast Crystal Oscillator Digital Controller (FXOSC) | ✅ | [快速晶体振荡器数字控制器（FXOSC）](ch28_fast_crystal_oscillator_digital_controller_fxosc/index.md) |
| 29 | Reset | ✅ | [复位（Reset）](ch29_reset/index.md) |
| 30 | Reset Generation Module (MC_RGM) | ✅ | [复位生成模块（MC_RGM）](ch30_reset_generation_module_mc_rgm/index.md) |
| 31 | Boot | ❌ | — |
| 32 | Power Management | ❌ | — |
| 33 | Mode Entry Module (MC_ME) | ⚠️ | [占位页（未翻译）](ch33_mode_entry_module_mc_me/index.md) |
| 34 | Power Control Unit (MC_PCU) | ❌ | — |
| 35 | Power Management Controller (PMC) | ❌ | — |
| 36 | System RAM Controller (SRAMC) | ❌ | — |
| 37 | DDR Subsystem | ❌ | — |
| 38 | DDR General Purpose Registers (DDR_GPR) | ❌ | — |
| 39 | Quad Serial Peripheral Interface (QuadSPI) | ❌ | — |
| 40 | Ultra Secured Digital Host Controller (uSDHC) | ❌ | — |
| 41 | System Timer Module (STM) | ❌ | — |
| 42 | Software Watchdog Timer (SWT) | ❌ | — |
| 43 | Periodic Interrupt Timer (PIT) | ❌ | — |
| 44 | FlexTimer (FTM) | ❌ | — |
| 45 | Real Time Clock (RTC) | ❌ | — |
| 46 | Inter-Integrated Circuit (I2C) | ❌ | — |
| 47 | Gigabit Ethernet Media Access Controller (GMAC) | ❌ | — |
| 48 | Packet Forwarding Engine (PFE) | ❌ | — |
| 49 | LINFlexD | ❌ | — |
| 50 | Serial Peripheral Interface (SPI) | ❌ | — |
| 51 | CAN (FlexCAN) | ❌ | — |
| 52 | Timestamp | ❌ | — |
| 53 | SerDes Subsystem | ❌ | — |
| 54 | SerDes General Purpose Registers (SERDES_GPR) | ❌ | — |
| 55 | Low Latency Communication Engine (LLCE) | ❌ | — |
| 56 | Universal Serial Bus On-The-Go Controller (USBOTG) | ❌ | — |
| 57 | FlexRay Communication Controller (FlexRay) | ❌ | — |
| 58 | Cross-Triggering Unit (CTU) | ❌ | — |
| 59 | Analog-to-Digital Converter (SAR_ADC) | ❌ | — |
| 60 | Thermal Monitoring Unit (TMU) | ❌ | — |
| 61 | Security | ❌ | — |
| 62 | Field Analysis Mechanisms | ❌ | — |
| 63 | Messaging Unit (MU) | ❌ | — |
| 64 | On-Chip One Time Programmable (OCOTP) Controller | ❌ | — |
| 65 | Fusebox Controller (FBXC) | ❌ | — |
| 66 | Safety | ❌ | — |
| 67 | Error Reporting Module (ERM) | ⚠️ | [占位页（未翻译）](ch067_error_reporting_module_erm/index.md) |
| 68 | Fault Collection and Control Unit (FCCU) | ❌ | — |
| 69 | RCCU Debug Unit (RDU) | ❌ | — |
| 70 | Clock Monitoring Unit-Frequency Check (CMU_FC) | ❌ | — |
| 71 | Clock Monitoring Unit - Frequency Meter (CMU_FM) | ❌ | — |
| 72 | Selftest Top General Purpose Registers (SELFTEST_GPR_TOP) | ❌ | — |
| 73 | Selftest General Purpose Registers (SELFTEST_GPR) | ❌ | — |
| 74 | Self-Test Control Unit (STCU2) | ❌ | — |
| 75 | Safety by Software (SBSW) | ❌ | — |
| 76 | Error Injection Module (EIM) | ❌ | — |
| 77 | Cyclic Redundancy Check (CRC) Unit | ❌ | — |
| 78 | Debug | ⚠️ | [占位页（未翻译）](ch078_debug/index.md) |
| 79 | JTAG Controller (JTAGC) | ❌ | — |
| 80 | JTAG Data Communication (JDC) | ❌ | — |
| 81 | Aurora Trace Port (ATP) Subsystem | ⚠️ | [占位页（未翻译）](ch081_aurora_trace_port_atp_subsystem/index.md) |

> Note: ch33 holds a registered placeholder page (not a translation) so the
> ch30 → ch33 cross-reference resolves under `--strict`; its status is ⚠️
> partial until the full chapter is translated.
