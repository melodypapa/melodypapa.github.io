---
title: "CP AUTOSAR"
---

**AUTOSAR** Classic Platform（**CP**）规范的中文翻译笔记：按基础、通信、加密、诊断、通用、I/O、MCAL、存储、方法论与模板、模式管理、系统服务、功能安全等类别组织，覆盖各基础软件模块（**BSW**）的功能、API、配置参数与集成约束，并收录 **RTE**、应用接口、**SW** 架构、库与模板等平台级内容。下列按导航结构列出本节全部文章，便于快速跳转。

## 文章

### 基础

* [基础（Foundation）](foundation/index.md)
  * [TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)

### 通信

* [通信（Communication）](communication/index.md)
  * [AUTOSAR CAN Driver（CAN驱动程序）](communication/can_driver/index.md)
    * [Full-CAN 与 Basic-CAN 的区别](communication/can_driver/full_can_vs_basic_can.md)
  * [AUTOSAR CAN Interface](communication/can_interface/index.md)
  * [AUTOSAR CAN NM（CAN网络管理）](communication/can_network_management/index.md)
  * [AUTOSAR CAN Transceiver Driver](communication/can_transceiver_driver/index.md)
  * [AUTOSAR CAN XL Driver（CAN XL 驱动程序）](communication/canxl_driver/index.md)
  * [AUTOSAR COM Based Transformer](communication/com_based_transformer/index.md)
  * [Data Distribution Service for Classic Platform（经典平台数据分发服务）](communication/data_distribution/index.md)
  * [AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)
  * [AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)
  * [E2E Transformer (E2E转换器)](communication/e2e_transformer/index.md)
  * [AUTOSAR Ethernet Driver（以太网驱动程序）](communication/ethernet_driver/index.md)
  * [AUTOSAR Ethernet Interface（以太网接口）](communication/ethernet_interface/index.md)
  * [AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](communication/ethernet_switch_driver/index.md)
  * [AUTOSAR FVM (Freshness Value Manager)](communication/fvm/fvm.md)
  * [AUTOSAR Large Data COM（大数据 COM）](communication/large_data_com/index.md)
  * [AUTOSAR LIN Driver](communication/lin_driver/index.md)
  * [AUTOSAR LinIf (LIN Interface)](communication/lin_interface/index.md)
  * [AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)
  * [AUTOSAR Bus Mirroring（总线镜像）](communication/mirror/mirror.md)
  * [AUTOSAR PduR (PDU Router)](communication/pdu_router/index.md)
  * [AUTOSAR SecOC (Secure Onboard Communication)](communication/sec_oc/index.md)
  * [AUTOSAR SD (Service Discovery)](communication/service_discovery/index.md)
  * [AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)
  * [AUTOSAR SoAd (Socket Adaptor)](communication/soad/index.md)
  * [AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)
  * [AUTOSAR UdpNm (UDP Network Management)](communication/udp_network_management/index.md)

### 加密（Crypto）

* [加密（Crypto）](crypto/index.md)
  * [AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)
  * [AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)
  * [AUTOSAR Crypto Service Manager（加密服务管理器）](crypto/crypto_service_manager/index.md)
  * [AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)
  * [Utilization of Crypto Services（加密服务使用指南）](crypto/utilization_of_crypto_services/index.md)

### 诊断（Diagnostics）

* [诊断（Diagnostics）](diagnostics/index.md)
  * [AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](diagnostics/diagnostic_communication_manager/index.md)
  * [AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)

### 通用（General）

* [通用（General）](general/index.md)
  * [AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)
  * [AUTOSAR Standard Types（标准类型）](general/standard_types/index.md)
  * [AUTOSAR Platform Types（平台类型）](general/platform_types/index.md)
  * [AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)
  * [Layered Software Architecture（分层软件架构）](general/layered_software_architecture/index.md)
  * [Application Level Error Handling（应用层错误处理）](general/application_level_error_handling/index.md)
  * [BSW Distribution Guide（BSW 分布指南）](general/bsw_distribution_guide/index.md)
  * [CDD Design and Integration Guideline（CDD 设计与集成指南）](general/cdd_design_and_integration/index.md)
  * [Error Description（错误描述）](general/error_description/index.md)
  * [VFB（虚拟功能总线）](general/vfb/index.md)

### I/O

* [输入输出（I/O）](io/index.md)
  * [AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)
  * [AUTOSAR DIO Driver（数字输入输出驱动）](io/dio_driver/index.md)
  * [AUTOSAR ICU Driver（输入捕获驱动）](io/icu_driver/index.md)
  * [AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)
  * [AUTOSAR OCU Driver（输出比较单元驱动）](io/ocu_driver/index.md)
  * [AUTOSAR Port Driver（端口驱动）](io/port_driver/index.md)
  * [AUTOSAR PWM Driver（脉冲宽度调制驱动）](io/pwm_driver/index.md)

### MCAL

* [微控制器抽象层（MCAL）](mcal/index.md)
  * [AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)
  * [AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)
  * [AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)

### 存储

* [存储（Memory）](memory/index.md)
  * [AUTOSAR BndM（非易失性大容量数据管理器）](memory/bulk_nv_data_manager/index.md)
  * [AUTOSAR FLS（闪存驱动程序）](memory/flash_driver/index.md)
  * [AUTOSAR FEE（闪存EEPROM仿真）](memory/flash_eeprom_emulation/index.md)
  * [AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)
  * [AUTOSAR Memory Mapping（AUTOSAR 内存映射）](memory/memory_mapping/index.md)
  * [NV数据处理指南](memory/nv_data_handling_guideline/index.md)
  * [AUTOSAR NVM（非易失性存储管理器）](memory/nvram_manager/index.md)
  * [Explanation of Firmware Over-The-Air（固件远程升级说明）](memory/firmware_over_the_air/index.md)

### 方法论与模板

* [方法论与模板（Methodology and Templates）](methodology_templates/index.md)
  * [AUTOSAR BSWMDT（基础软件模块描述模板）](methodology_templates/basic_software_module_description_template/index.md)

### 模式管理

* [模式管理（Mode Management）](mode_management/index.md)
  * [AUTOSAR Basic Software Mode Manager（BSW模式管理器）](mode_management/basic_software_mode_manager/index.md)
  * [AUTOSAR ECU State Manager（ECU状态管理器）](mode_management/ecu_state_manager/index.md)
  * [Guide to Mode Management（模式管理指南）](mode_management/guide_to_mode_management/index.md)
  * [callback 与 callout 的区别（微信公众号）](https://mp.weixin.qq.com/s/BlOXxJJ33NNNuG_RvbzF-Q)

### 电源状态管理

* [AUTOSAR ECU 电源状态管理：启动、下电、唤醒与复位流程](power/index.md)

### 系统服务

* [系统服务（System Services）](system_services/index.md)
  * [AUTOSAR Default Error Tracer（默认错误跟踪器）](system_services/default_error_tracer/index.md)
  * [AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)
  * [AUTOSAR Operating System（操作系统）](system_services/operating_system/index.md)
  * [AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)
  * [Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](system_services/sw_cluster_design_and_integration/index.md)

### 功能安全

* [安全（Safety）](safety/index.md)
  * [AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)
  * [AUTOSAR Watchdog Interface（看门狗接口）](safety/watchdog_interface/index.md)
  * [AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)
  * [Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](safety/functional_safety_measures/index.md)
  * [Safety Use Case（安全用例）](safety/safety_use_case/index.md)

### RTE

* [AUTOSAR RTE（运行时环境）](rte/index.md)

### SW 架构（SW Architecture）

* [SW 架构（SW Architecture）](sw_arch/index.md)
  * [ARTI（AUTOSAR 运行时接口）](sw_arch/arti/index.md)

### 应用接口

* [应用接口（Application Interfaces）](application_interfaces/index.md)
  * [Explanation of Application Interface of AD/ADAS Vehicle Motion Control（AD/ADAS 车辆运动控制应用接口说明）](application_interfaces/adas_vmc/index.md)
  * [Explanation of Application Interfaces of the Body and Comfort Domain（车身与舒适域应用接口说明）](application_interfaces/body_and_comfort/index.md)
  * [Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)
  * [Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](application_interfaces/hmi/index.md)
  * [Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)
  * [Explanation of Application Interfaces of the Powertrain Engine Domain（动力总成（发动机）域应用接口说明）](application_interfaces/powertrain/index.md)
  * [Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)

### 库

* [库（Libraries）](libraries/index.md)
  * [Macro Encapsulation of Interpolation Calls（插值调用宏封装）](libraries/macro_encapsulation_of_interpolation_calls/index.md)

### 模板

* [模板（Templates）](template/index.md)
  * [通用结构（Generic Structure）一段话总结](template/generic_structure/index.md)
  * [Specification of Timing Extensions for Classic Platform（经典平台时序扩展规范）](template/timimg_extension/indx.md)

## 相关内容

* [AUTOSAR 术语表](glossary.md)
* [API 清单](api_reference.md)
* [首页](../index.md)
