---
title: "AUTOSAR 术语表（缩略语与缩写）"
---

本页汇总各 AUTOSAR 模块文章第 2 章「缩略语」中的全部术语，按字母排序，便于查找。**由脚本自动生成，请勿手工编辑**——修改应在对应文章的第 2 章进行，然后重新生成（`python .agents/skills/autosar-translate/scripts/gen_glossary.py`）。同一术语在不同模块中的释义若有差异，分条列出并标注来源。

共 **256** 个术语，来自 **24** 篇文章。

## A

**AC**
> 闪存访问代码（**access code**）的缩写。 — 来源：[flash_driver](memory/flash_driver/index.md)（SWS_FlashDriver · R23-11）

**Accuracy**
> 精度（**Accuracy**）取决于用于采样或者生成的硬件外围设备。如：**ADC**转换器可以是 8/10/12/16 位转换器 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Acquisition Time**
> 采集时间 = 采样时间（**Sample Time**）+ 转换时间（**Conversion Time**） — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**Active Time**
> 取决于被捕获信号的起始边沿：起始边沿为下降沿时，**Active Time** = **Low Time**；起始边沿为上升沿时，**Active Time** = **High Time**；起始边沿为双边沿时，若先出现上升沿则 **Active Time** = **High Time**，若先出现下降沿则 **Active Time** = **Low Time**。 — 来源：[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）

**ADC**
> 模数转换器（**Analogue Digital Converter**） — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 模数转换器（**Analog to Digital Converter**）。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）

**ADC Channel**
> **ADC**通道是指绑定到一个端口引脚的逻辑**ADC**实体。同时多个**ADC**实体也可以映射到同一个端口引脚。 — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Channel Group**
> **ADC**通道组是指由一组**ADC**通道链接到同一个**ADC**硬件单元（**ADC HW Unit**）。例如：一个采样保持器（**Sample & Hold**）和一个**A/D**转换器。整个组的转换由一个触发源触发。 — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC HW Unit**
> 微控制器的输入电子设备，包括执行模拟到数字转换所需的所有部件。 — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Module**
> ADC的基础软件模块ADC驱动模块（**ADC Driver**） — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Result Buffer**
> 也称为**ADC Streaming Buffer**或者**ADC Stream Buffer**。**ADC**驱动程序的用户必须为每个组提供一个缓冲区。如果选择流式访问模式（**streaming access mode**），此缓冲区可以保存同一组通道的多个样本。如果选择单一访问模式（**Single Access Mode**），每个组通道的一个样本将保存在缓冲区中。 — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**Address Area**
> 地址区（Address Area）是指逻辑地址空间中连续的存储区域。通常多个物理存储扇区组合到一个逻辑地址区域。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**AEAD**
> Authenticated Encryption with Associated Data，具有关联数据的经过身份验证的加密。 — 来源：[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**API**
> 应用程序接口（**Application Programming Interface**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**AR**
> AUTOSAR — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**ARTI**
> AUTOSAR 运行时接口（**AUTOSAR Run-time interface**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**Atomic Sender/Receiver interface**
> 原子发送者/接收者接口。一个原子发送者/接收者接口，可用于将 **DID** 数据元素分组为一个记录数据元素原型。所有数据元素都可以通过单个读取或写入操作进行读取或写入。 — 来源：[diagnostic_communication_manager](diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager · R23-11）

**Attributes**
> 属性（**Attributes**）是**ECU**中存在的每个**ECU**信号所包含的软件或者硬件特性。一些属性是固定的，由端口定义决定。还有一些属性是可以在**I/O**硬件抽象中进行配置的。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

## B

**Bank**
> 存储 **Bank** 是指一组扇区批次（**Section Batch**）的集合. 如果存储器技术支持分片成扇区，则存储 **Bank** 是指一个不允许进行边写边读操作的扇区批次组（**a sector batch group**）的实例。在闪存存储设备（flash memory）概念中，**Bank** 通常是映射到一个单独的闪存控制器。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**BndM**
> 大容量非易失性数据管理器（**Bulk Non-Volatile Data Manager**） — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**BSW**
> 基础软件. — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）
> 基础软件（**Basic SoftWare**） — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
> 基础软件（**Basic Software**） — 来源：[basic_software_mode_manager](mode_management/basic_software_mode_manager/index.md)（SWS_BSWModeManager · R23-11）、[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**BswM**
> 基础软件模式管理器（**BSW Mode Manager**） — 来源：[basic_software_mode_manager](mode_management/basic_software_mode_manager/index.md)（SWS_BSWModeManager · R23-11）

**BSWMD**
> 基本软件模块说明（**Basic SoftWare Module Description**） — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
> 基础软件模块说明（**Basic Software Module Description**） — 来源：[basic_software_mode_manager](mode_management/basic_software_mode_manager/index.md)（SWS_BSWModeManager · R23-11）、[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

## C

**Callback**
> 术语回调函数（**Callback**）主要用于**API**服务，实现通知其他**BSW**模块。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Callout**
> **Callout**是一种函数**Stub**。主要在配置时进行填写，目的是向提供**Callout**函数的模块添加功能。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**CAN Channel**
> 从 CAN 控制器通过 CAN 收发器连接到 CAN 网络的物理通道。 — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）

**CAN L-PDU**
> CAN协议数据单元（**CAN Protocol Data Unit**）。由CAN驱动程序可见的标识符（**identifier**）、数据长度和数据（**SDU**）组成。 — 来源：[can_interface](communication/can_interface/index.md)（SWS_CANInterface · R23-11）

**CAN L-SDU**
> CAN服务数据单元（**Service Data Unit**）。CAN的L-PDU内的传输数据。对CAN接口的上层可见（例如：PDU路由器）。 — 来源：[can_interface](communication/can_interface/index.md)（SWS_CANInterface · R23-11）

**CanIf**
> CAN接口（**CAN Interface**）的缩写 — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**CanNm**
> CAN网络管理（**CAN Network Management**）的缩写 — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**CBR**
> Channel Busy Ratio，通道繁忙比率。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**CBV**
> 控制位向量（Control Bit Vector） — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**CDD**
> Complex Device Driver：复杂设备驱动程序 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> Complex Device Driver，复杂设备驱动程序 — 来源：[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）
> 复杂驱动程序（**Complex Driver**） — 来源：[basic_software_mode_manager](mode_management/basic_software_mode_manager/index.md)（SWS_BSWModeManager · R23-11）、[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**CF**
> 连续帧，传输协议术语。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**CIT**
> Channel Idle Time，通道空闲时间。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**Class**
> 一个类（**Class**）代表一组具有相似电气特性的信号。如：模拟类（**Analogue class**） — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Client-Server communication**
> 客户端-服务器通信（**Client-Server communication**）涉及两个实体。客户端是要求服务的一方，服务器是提供服务的一方。客户端发起通信，请求服务器执行服务，必要时传输参数集合。服务器以**RTE**的形式，等待来自客户端的传入通信请求，执行请求的服务并发送对客户端请求的响应。因此服务启动的方向是用来对**AUTOSAR**软件组件是客户端还是服务器分类的主要标识。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**COM**
> 通讯（**Communication**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**ComM**
> Communication Manager — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）
> ComM模块提供了一些功能，如**Dcm**模块可以指示“活动”和“非活动”状态，以便进行诊断通信。Dcm模块提供了处理 **Full-Communication**、**Silent-Communication** 和 **No-Communication** 通信需求的功能。此外，如果**ComM**模块要求，**Dcm**模块提供启用和禁用诊断通信的功能。（如：**UDS**的**0x28**服务） — 来源：[diagnostic_communication_manager](diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager · R23-11）

**Compare threshold（比较阈值）**
> 每次计数器增加一个单位时与计数器内容相比较的目标值。 — 来源：[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）

**Continuous Conversion Mode**
> 连续转换模式是指**ADC**通道组的转换在软件**API**调用后连续执行，结果写入分配的结果缓冲区。转换本身是自动运行的（硬件/中断控制）。连续转换的停止可以通过软件**API**调用来实现。 — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**Conversion Time**
> 转换时间是指将采样的模拟值转换为数值所需的时间。 — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**CRYIF**
> Crypto Interface：加密接口 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> Crypto Interface，加密接口 — 来源：[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**CRYPTO**
> Crypto Driver：加密驱动程序 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> Crypto Driver，加密驱动程序 — 来源：[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**CSM**
> Crypto Service Manager：加密服务管理器 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> Crypto Service Manager，加密服务管理器 — 来源：[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**CV2x**
> Cellular Vehicle to X driver，蜂窝车辆到X驱动程序。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**CWU**
> 整车唤醒（**Car Wakeup**） — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）
> 车辆唤醒 — 来源：[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

## D

**DEM**
> Diagnostic Event Manager — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）、[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）
> DEM模块提供检索与故障内存相关的所有信息的功能，以便Dcm模块能够通过从故障内存中读取数据来响应测试者的请求。 — 来源：[diagnostic_communication_manager](diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager · R23-11）
> 诊断事件管理器（**Diagnostic Event Manager**）。 — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）、[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）、[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）、[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）、[port_driver](io/port_driver/index.md)（SWS_PortDriver · R23-11）、[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）、[flash_driver](memory/flash_driver/index.md)（SWS_FlashDriver · R23-11）、[basic_software_mode_manager](mode_management/basic_software_mode_manager/index.md)（SWS_BSWModeManager · R23-11）

**DET**
> Default Error Tracer — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）
> Default Error Tracer：默认错误跟踪器 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> Default Error Tracer，默认错误跟踪器 — 来源：[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）
> 默认错误跟踪器（**Default Error Tracer**），实现报告开发错误的模块。 — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）、[flash_driver](memory/flash_driver/index.md)（SWS_FlashDriver · R23-11）
> 默认错误跟踪器（**Default Error Tracer**）。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）、[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）、[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）、[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）、[port_driver](io/port_driver/index.md)（SWS_PortDriver · R23-11）、[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）、[basic_software_mode_manager](mode_management/basic_software_mode_manager/index.md)（SWS_BSWModeManager · R23-11）

**DIO**
> Digital Input Output (SPAL module) — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）
> 数字输入输出（**Digital Input Output**）。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）

**DIO channel**
> 表示单个通用数字输入/输出引脚。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）

**DIO channel group**
> 表示由逻辑组表示的多个相邻**DIO**通道。一个**DIO**通道组应属于一个**DIO**端口。示例：8 位端口中寻址复用器的端口引脚 2..6。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）

**DIO port**
> 表示由硬件分组在一起的多个**DIO**通道（通常由一个硬件寄存器控制）。示例：Freescale HC08 的 Port A（8 位）。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）

**DMA**
> 直接内存访问（**Direct Memory Access**） — 来源：[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）

## E

**EA**
> EEPROM抽象（**EEPROM Abstraction**） — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）、[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**EB**
> 外部缓冲通道。位于SPI处理程序/驱动程序之外，包含要传输的数据的缓冲区。 — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）

**ECC**
> 纠错码（**Error Correction Code**） — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）
> 扩展一致性等级（**Extended Conformance Class**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**ECU**
> 电子控制单元（**Electronic Control Unit**） — 来源：[basic_software_mode_manager](mode_management/basic_software_mode_manager/index.md)（SWS_BSWModeManager · R23-11）、[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**ECU pin**
> ECU引脚（**ECU pin**）是**ECU**与电子系统其余部分的电气硬件连接。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**ECU Signal**
> ECU信号（**ECU Signal**）是电信号的软件表示。一个**ECU**信号具有一些属性（**Attribute**）和一个符号名称（**Symbolic name**）。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**ECU Signal Group**
> ECU信号组（**ECU Signal Group**）是一组电信号的软件表示。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**EcuM**
> ECU State Manager — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）
> **ECU**状态管理器（**ECU State Manager**）。 — 来源：[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）

**EEPROM**
> 电可擦除可编程ROM（**Electrically Erasable and Programmable ROM**）。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

**EIRA**
> 外部和内部请求数组（**External and Internal Request Array**） — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**Electrical Signal**
> 电信号（**Electrical Signal**）代表**ECU**引脚上的物理信号。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Enumeration**
> 枚举。在**C**语言中可以是**enum**或**#define**。 — 来源：[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）

**ERA**
> 外部请求数组（**External Request Array**） — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**Eth**
> Ethernet Controller Driver，以太网控制器驱动程序（AUTOSAR BSW 模块）， — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**EthIf**
> Ethernet Interface， 以太网接口（AUTOSAR BSW 模块）。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）
> 以太网接口 — 来源：[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

**EthSM**
> Ethernet State Manager，以太网状态管理器（AUTOSAR BSW 模块）。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**EthTrcv**
> Ethernet Transceiver Driver，以太网收发器驱动程序（AUTOSAR BSW 模块）。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

## F

**FCFS**
> 先到先服务（First come first served） — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**FEE**
> 闪存EEPROM仿真（**Flash EEPROM Emulation**）。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）、[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**FF**
> 第一帧，传输协议术语。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**FID**
> 功能标识符（**Function Identifier**） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**FiM**
> 功能禁止管理器（**Function Inhibition Manager**） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**Fls, FLS**
> AUTOSAR闪存驱动程序的官方缩写 — 来源：[flash_driver](memory/flash_driver/index.md)（SWS_FlashDriver · R23-11）

**FOTA**
> 固件远程升级（**Firmware Over The Air**），通过无线通信进行固件远程更新。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**Free running counter（自由运行计数器）**
> 从最小值（分别为最大值）运行到最大值（分别为最小值）的计数器，并在到达最大值（分别为最小值）后自动从最小值（分别为最大值）重新开始。 — 来源：[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）

**Functionality**
> 功能组（**Functionality**）包括系统用户可见和用户不可见的功能（**Function**）方面[2]。除此之外，在**FiM**上下文中， 功能组可以由具有相同允许/禁止条件集的一个、几个或部分可运行实体的内容构建。 通过**FiM**，这些功能组的抑制可以通过标定（**calibration**）进行配置甚至修改。每个功能组都由一个唯一的**FunctionId**表示。 与具有特定调度条件的可运行实体相比，功能组的特征在于一组特定的禁止条件。 — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

## H

**Hardware Trigger**
> 硬件触发是**ADC**内部触发信号，用于启动ADC通道组的一次转换。**ADC**硬件触发在ADC硬件内部生成（例如：基于**ADC**定时器或触发沿信号）。触发硬件是强耦合或者直接集成在**ADC**的硬件中。当检测到硬件触发后，无需软件即可启动**ADC**通道组转换。**注意：**即使**ADC**硬件不支持硬件触发，也可以通过软件触发结合**GPT/ICU**驱动程序来实现类似的行为。（例如：在GPT定时器通知函数中，启动软件触发的**ADC**通道组的转换） — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**HSM**
> Hardware Security Module：硬件安全模块 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> Hardware Security Module，硬件安全模块 — 来源：[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）
> 硬件安全模块（**Hardware Security Module**），专用的安全 **MCU** 的内核， — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**HW**
> Hardware：硬件 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> Hardware，硬件 — 来源：[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）
> 硬件（**Hardware**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

## I

**I-PDU**
> 交互层**PDU**。 一个**I-PDU**由数据（缓冲区）、长度和**I-PDU ID**组成。PDU路由器将主要I-PDU进行路由，但即时网关（**on-the-fly gatewaying**）除外。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**I-PDU ID**
> **I-PDU**标识符 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**IB**
> 内部缓冲通道。位于 SPI 处理程序/驱动程序内部，包含要传输的数据的缓冲区。 — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）

**ICU**
> 输入捕获单元（**Input Capture Unit**）。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）
> 输入捕获单元（**Input Capture Unit**），而非重症监护室（Intensive Care Unit）。 — 来源：[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）

**ICU Channel**
> 表示绑定到一个输入信号、并为所配置测量模式提供硬件资源的逻辑**ICU**实体。 — 来源：[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）

**ICU State**
> **ICU**通道的逻辑输入状态，可以是**ICU_ACTIVE**或**ICU_IDLE**。 — 来源：[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）

**ICU_ACTIVE**
> **ICU**通道的输入状态，表示已检测到激活边沿。 — 来源：[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）

**ICU_IDLE**
> **ICU**通道的输入状态，表示自上次调用**Icu_GetInputState()**或**Icu_Init()**以来未检测到激活边沿。 — 来源：[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）

**ID**
> 标识符（**Identifier**）。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）、[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**Inhibition Condition**
> 禁止条件（Inhibition Condition）是指由一个**FID**、一个禁止掩码（**Inhibition Mask**）和一个Dem事件（**Dem event**）/ 组件（**Component**）的状态之间的关系。（参见**FiMInhibitionConfiguration**） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**Inversion**
> 物理值与逻辑值的反转（**Inversion**）。此属性不可见，但可以由**I/O**硬件抽象来实现，并向用户传递预期值。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**IOC**
> 操作系统间应用程序通信器（**Inter OS-Application communicator**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**IoHwAb**
> 输入/输出硬件抽象（**Input/Output Hardware Abstraction**） — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**IP**
> Internet Protocol，网际协议。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）
> 互联网协议 — 来源：[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

**ISR**
> Interrupt Service Routine 中断服务程序 — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）
> 中断服务程序（**Interrupt Service Routine**） — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）、[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）
> 中断服务例程（**Interrupt Service Routine**） — 来源：[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）、[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）

## J

**Job**
> 作业是一个被配置的**CsmJob**。除此之外，它也可以是一个密钥、加密原语和参考通道。 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）、[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**Job Request**
> 作业请求（**Job Request**）是指上层模块对地址区的存储访问请求。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

## L

**L-PDU**
> 数据链路层 PDU。 一个或多个 I-PDU 被打包到一个 L-PDU 中。 L-PDU 是特定于总线的，例如 CAN 帧。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**LE**
> 可定位实体（**locatable entity**）是一个不同的软件，无论它位于哪个内核，都具有相同的效果。 — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**LSB**
> 最低有效位（**Least Significant Bit**）。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）
> 最低有效位（**Least significant bit**）。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

## M

**MC**
> 多核（**Multi-Core**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**MCAL**
> Micro Controller Abstraction Layer — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）
> 微控制器抽象层（MicroController Abstraction Layer） — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
> 微控制器抽象层（**Microcontroller Abstraction Layer**） — 来源：[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）

**MCG**
> Module Configuration Generator，模块配置生成器。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**MCU**
> 微控制器单元（**Microcontroller Unit**） — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）、[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）、[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）、[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）
> 微控制器单元（**MicroController Unit**） — 来源：[port_driver](io/port_driver/index.md)（SWS_PortDriver · R23-11）

**ME**
> 互斥（**Mutual exclusion**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**MemIf**
> 内存抽象接口（**Memory Abstraction Interface**）。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

**Memory Device**
> 存储设备（**Memory Device**）是指一组存储 **bank** 的组合。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**MII**
> Media Independent Interface，媒体独立接口（以太网控制器提供的用于访问以太网收发器的标准化接口）。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**MIL**
> 故障指示灯（**Malfunction Indication Light**） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**Monitoring function**
> 软件组件的一部分。一种监测并最终检测某个传感器或者执行器故障的机制，也可以是一种合理性检查。它报告SW-C的内部处理的事件状态，或者其他基础软件模块（BSW）的返回值的进一步处理的事件状态。（参见 AUTOSAR_SWS_DiagnosticEventManager[3]） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**MPU**
> 内存保护单元（**Memory Protection Unit**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**MSB**
> 最高有效位（**Most Significant Bit**）。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）
> 最高有效位（**Most significant bit**）。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

## N

**N-PDU**
> 网络层**PDU**。由传输协议模块用来对**I-PDU**进行分段。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**NM**
> 网络管理（**Network Management**） — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）
> 网络管理 — 来源：[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

**NM-Timeout Timer**
> NM超时计时器 — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**NMI**
> 不可屏蔽中断（**Non maskable interrupt**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**NV**
> 非易失性（**Non-volatile**） — 来源：[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）

**NV Block**
> **NV**块（**NV Block**）是一个基本存储对象。用来表示驻留在**NV内存**中的那部分**NVRAM**块。 — 来源：[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）

**NvM**
> NVRAM管理器（**NVRAM Manager**）。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）、[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）

**NVRAM**
> 非易失性RAM（**Non-volatile RAM**）。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）
> 非易失性随机存取存储器（**Non-volatile Random Access Memory**） — 来源：[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）
> 非易失性存储器（**Non volatile Memory**） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**NVRAM block**
> NVRAM管理器所见的管理单元。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）
> **NVRAM**块（**NVRAM Block**）是管理和存储**NV**数据块所需的整个结构。 — 来源：[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）

**NVRAM块（NVRAM Block）**
> “NVRAM块” 是管理和存储 NV 数据块所需的整个结构。 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**NV块标头（NV Block Header）**
> 如果启用 “**静态块ID**” 机制，则**NV块**中包含的附加信息。 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**NV块（NV Block）**
> “NV块”是“基本存储对象”。它代表驻留在 **NV内存** 中的 “NVRAM块” 的一部分。“**NV块**”是“**NVRAM块**”的强制性部分。 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**NV数据（NV data）**
> “NV数据” 是指要存储在非易失性存储器中的数据。 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

## O

**OA TC10**
> Open Alliance TC10，开放联盟 TC10 规格 [5]。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**OBD**
> 车载诊断（**On-board Diagnostics**） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**OBDII**
> 排放相关车载诊断（**Emission-related On-board Diagnostics**） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**OCU**
> 输出比较单元（**Output Compare Unit**） — 来源：[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）

**OCU channel（OCU 通道）**
> 表示一个逻辑实体，由自由运行计数器、比较阈值以及作为比较过程结果而执行的动作组成。 — 来源：[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）

**OEM**
> 原始设备制造商（**Original Equipment Manufacturer**） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**OIL**
> OSEK 实现语言（**OSEK Implementation Language**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**One-Shot Conversion Mode**
> One-Shot转换模式是指**ADC**通道组的转换在触发后执行一次，并将结果写入分配的结果缓冲区。触发可以是软件**API**调用或硬件事件。 — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**OS**
> 操作系统（**Operating System**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**OSEK/VDX**
> 用于机动车辆电子设备的开放系统及其接口（**Offene Systeme und deren Schnittstellen für die Elektronik im Kraftfahrzeug**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**OTA**
> 远程升级（**Over The Air**），OEM 后台（**backend**）与车辆之间无线通信的总称。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

## P

**Page Burst**
> 通过存储页面的聚合访问（**aggregated access**）来提高性能。在存储设备技术支持物理分段（**physical segmentation**）的情况下，一些存储设备可以提供优化的访问方法，支持一次读取或写入多个页面。页面突发（**Page Burst**）表示用于访问优化的存储页面的聚合。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**PDU**
> 协议数据单元. — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）、[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

**PduR**
> **PduR**模块提供诊断数据的发送和接收功能。Dcm模块的正常运行，假设PduR接口支持诊断应用层和底层传输层之间为SAP (service Access Point)定义的所有服务原语(参见ISO14229-1[2]，第5章应用层服务)。 — 来源：[diagnostic_communication_manager](diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager · R23-11）

**PDU传输能力被禁用**（**PDU transmission ability is disabled**）
> 这意味着网络管理**PDU**传输已被服务**CanNm_DisableCommunication**禁用。 — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**PDU路由器（PDU Router）**
> 将**I-PDU**从一个模块传输到另一个模块的模块。PDU路由器模块可用于网关操作和内部路由目的。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**Permission state**
> 许可状态（**Permission State**）包含了由**FID**表示的功能组是否可以执行或是否不应该运行的信息。状态根据报告的事件由**FiM**控制。 — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**Physical Level (Input)**
> 两种可能的状态：**LOW** / **HIGH**。位值'0'表示**LOW**，位值'1'表示**HIGH**。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）
> 两种可能的状态：**LOW**/**HIGH** — 来源：[port_driver](io/port_driver/index.md)（SWS_PortDriver · R23-11）

**Physical Level (Output)**
> 两种可能的状态：**LOW** / **HIGH**。位值'0'表示**LOW**，位值'1'表示**HIGH**。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）
> 两种可能的状态：**LOW**/**HIGH** — 来源：[port_driver](io/port_driver/index.md)（SWS_PortDriver · R23-11）

**PLL**
> 锁相环（**Phase Locked Loop**） — 来源：[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）

**PNC**
> 部分网络集群（**Partial Network Cluster**） — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**PNC叶节点**（**PNC leaf node**）
> PNC叶节点是一个**ECU**，在网络中根本不充当PNC协调器。它像通常的NM消息一样处理PN关闭消息。 — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**PNI**
> 部分网络信息（**Partial Network Information**） — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）
> 部分网络信息 — 来源：[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

**PNL**
> 部分网络学习（**Partial Network Learning**） — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）
> 部分网络学习 — 来源：[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

**PN关闭消息**（**PN shutdown message**）
> 顶级PNC协调器传输PN关闭消息以指示跨PN拓扑的同步PNC关闭。PN关闭消息是作为**NM**消息，它在控制位向量中具有**PNSR**位，并且所有被指示用于同步关闭的PNC都设置为**1** — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**PN过滤遮罩**（**PN filter mask**）
> 由配置容器定义的过滤器掩码字节向量**CanNmPnFilterMaskByte**。 — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**Port**
> Port module (SPAL module) — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）
> 表示**MCU**器件上整个可配置的端口。 — 来源：[port_driver](io/port_driver/index.md)（SWS_PortDriver · R23-11）

**Port Pin**
> 表示**MCU**器件上单个可配置的输入或输出引脚。 — 来源：[port_driver](io/port_driver/index.md)（SWS_PortDriver · R23-11）

**PWM**
> 脉冲宽度调制（**Pulse Width Modulation**）。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）、[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）

**PWM Channel**
> 链接到硬件**PWM**的数字标识符。 — 来源：[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）

**PWM Duty cycle**
> 定义与周期相关的起始电平（可以为高或低）的百分比。 — 来源：[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）

**PWM Idle State**
> 空闲状态表示调用**Pwm_SetOutputToIdle**或**Pwm_DeInit**后**PWM**通道的输出状态。 — 来源：[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）

**PWM Output State**
> 定义**PWM**信号的输出状态。可以是：高、低。 — 来源：[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）

**PWM period**
> 定义**PWM**信号的周期。 — 来源：[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）

**PWM Polarity**
> 定义每个**PWM**通道的起始输出状态。 — 来源：[pwm_driver](io/pwm_driver/index.md)（SWS_PWMDriver · R23-11）

## R

**RAM Block**
> **RAM Block**是一个基本存储对象。用来表示驻留在**RAM**中的那部分**NVRAM**块。 — 来源：[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）

**RAM Mirror**
> **RAM镜像**是**NvM**内部缓冲区。当NvMBlockUseSyncMechanism设置为TRUE时，用于操作读取和写入的NVRAM Block数据的**RAM Block**。 — 来源：[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）

**RAM块（RAM Block）**
> “RAM块” 是 “基本存储对象”。它代表驻留在 **RAM** 中的 “NVRAM块” 的一部分。 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**Range**
> 范围（**Range**）在这里是一个功能范围（**functional range**），而不是电气范围（**electrical range**）。所有范围都用于功能的需要或者诊断的检测。对于模拟**ECU**信号，可以定义上下限值 [lowerLimit...upperLimit]（电压、电流）。对于电阻信号和时序信号（周期）的特殊情况，下限值（**lowerLimit**）不能为负。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Read Page**
> 读取页面（**Read Page**）是指存储设备的最小可读单位（以字节为单位）。因为一些存储设备技术的访问必须考虑到物理分段（**physical segmentation**），所以并非所有存储设备技术都可以按字节访问。该术语定义了一次访问中需要读取页面最小的大小。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**Reference Interval（参考区间）**
> 由**Ocu_SetAbsoluteThreshold** **API**的调用者给出的区间（以 tick 为单位），并用作计算返回信息的基础。 — 来源：[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）

**Resolution**
> 分辨率（**Resolution**）属性适用于依赖于范围和数据类型的许多类别。如：(upperLimit - lowerLimit) / (2<sup>datatypelength</sup> -1)。 对于其他类别，它可能是已知和被定义的。如：[-12 Volts…+12Volts]，数据类型: 16 bits，**Resolution** 为 24 / 65535。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**ROM**
> 只读存储器（**Read-Only Memory**） — 来源：[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）

**ROM Block**
> **ROM Block**是一个基本存储对象。用来表示驻留在**ROM**中的那部分**NVRAM**块。 — 来源：[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）

**ROM块（ROM Block）**
> “ROM块”是“基本存储对象”。它代表驻留在 **ROM** 中的 “NVRAM块” 的一部分。“**ROM块**”是“**NVRAM块**”的可选部分。 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**RSSI**
> Received Signal Strength Indicator，接收信号强度指示器。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**RTE**
> 运行环境（**Runtime Environment**） — 来源：[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）
> 运行时环境（**Real Time Environment**） — 来源：[basic_software_mode_manager](mode_management/basic_software_mode_manager/index.md)（SWS_BSWModeManager · R23-11）
> 运行环境（**Run-Time Environment**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**RTOS**
> 实时操作系统（**Real Time Operating System**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**Runnable entity**
> 可运行实体（**Runnable entity**）是原子软件组件（**Atomic Software-Component**）的一部分，它独立于该原子软件组件的其他可运行实体的执行和调度。 它被描述为由**RTE**启动的一系列指令序列。每个可运行实体与一个**EntryPoint**相关联。 — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**RWW**
> 并行读写（**Read While Write**）。指存储设备在一个存储 **Bank** 中执行读取操作，同时也在另一个存储 **Bank** 中进行写入/擦除操作的能力。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

## S

**Sampling rate**
> 采样率（**Sampling rate**）是获得信号值所需的时间段。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Sampling Time, Sample Time**
> 采样时间是指对模拟值进行采样的时间（例如：加载电容器，……） — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**SBC**
> System Basis Chip 系统基础芯片。集成了例如 CAN 和/或 LIN 收发器、看门狗和电源控制。 — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）

**SC**
> 单核（**Single-Core**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**SDU**
> 服务数据单元 — 来源：[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

**Sector**
> 扇区（**Sector**）是指最小的可擦除存储单元（以字节为单位）。某些存储设备技术需要在写入存储之前进行明确的物理擦除操作。扇区定义了这种擦除单元的最小大小。根据存储设备的不同，扇区可以是统一大小的或可变大小的。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**Sector Batch**
> 扇区批次（**Sector Batch**）是指具有统一大小的扇区的集合。具有相同大小的连续扇区的逻辑集合。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**Sector Burst**
> 扇区突发（**Sector Burst**）是指聚合扇区以提高擦除性能。如果存储技术需要物理擦除操作，一些设备通过一步擦除扇区集合来提供擦除性能优化。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**Sender-receiver communication**
> 发送方-接收方通信涉及原子数据元素组成的信号的发送和接收，这些原子数据元素由一个组件发送给另一个或多个组件。发送方-接收方接口可以包含多个数据元素。发送方-接收方通信是单向的 接收方发送的任何回复都可以视为一个单独的发送方-接收方通信。接收方组件的端口可以读取接口描述定义的数据元素，而提供方组件的端口可以按照接口描述定义写入数据元素。 — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**SF**
> 单帧，传输协议术语。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**SHE**
> Security Hardware Extension：安全硬件扩展 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> Security Hardware Extension，安全硬件扩展 — 来源：[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**SLA**
> 软件分层架构（**Software Layered Architecture**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**SNI**
> 源节点标识符（**Source Node Identifier**） — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**Software Trigger**
> 软件触发是一个软件**API**调用，用于启动转换一个**ADC**通道组或一系列连续**ADC**通道组转换的。 — 来源：[adc_driver](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**SOTA**
> 软件远程升级（**Software Over The Air**），使用无线通信进行软件远程更新。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**SPAL**
> 标准外设抽象 — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）
> 标准外设抽象层（**Standard Peripheral Abstraction Layer**） — 来源：[ocu_driver](io/ocu_driver/index.md)（SWS_OCUDriver · R23-11）

**SPI**
> 串行外设接口（**Serial Peripheral Interface**）。 — 来源：[dio_driver](io/dio_driver/index.md)（SWS_DIODriver · R23-11）

**SPI Channel**
> 一个通道是使用相同标准定义的软件数据交换介质。请参阅SPI驱动程序规范 — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）

**SPI Job**
> 一个作业由一个或多个具有相同片选的通道组成。作业被认为是原子的，因此不能被中断。 作业也具有指定的优先级。 有关详细信息，请参阅SPI驱动程序规范。 — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）

**SPI Sequence**
> 一个序列是要传输的多个连续作业。 序列取决于静态配置。 有关详细信息，请参阅 SPI 驱动程序规范。 — 来源：[can_transceiver_driver](communication/can_transceiver_driver/index.md)（SWS_CANTransceiverDriver · R23-11）

**Sub Address Area**
> 子地址区（**Sub Address Area**）是指逻辑地址空间中的连续存储区域映射到一个存储设备的一个扇区批次（**Sector Batch**）。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

**SW**
> Software：软件 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> Software，软件 — 来源：[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）
> 软件（**Software**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**SW-C**
> 软件组件（**Software Component**） — 来源：[nv_data_handling_guideline](memory/nv_data_handling_guideline/index.md)（EXP_NVDataHandlingGuideline · R23-11）

**SWC**
> 软件组件（**SoftWare Component**） — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
> 软件组件（**Software Component**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**SWC/SW-C**
> 软件组件（**Software Component**） — 来源：[basic_software_mode_manager](mode_management/basic_software_mode_manager/index.md)（SWS_BSWModeManager · R23-11）

**SWCD**
> 软件组件说明（**Software Component Description**） — 来源：[basic_software_mode_manager](mode_management/basic_software_mode_manager/index.md)（SWS_BSWModeManager · R23-11）

**SWFRT**
> 软件自由运行定时器（**Software FreeRunningTimer**） — 来源：[operating_system](system_services/operating_system/index.md)（SWS_OperatingSystem · R23-11）

**Symbolic name**
> ECU信号的符号名称（**Symbolic name**）在**I/O**硬件抽象模块中是用来建立链接的。（包括：功能、引脚等） — 来源：[iohwab](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Symbolic name for a channel**
> 通道的符号名，是用名称对句柄的替代。通过该句柄可以在配置结构中找到每个通道及其相关属性。在**C**语言中可通过**#define**和**enum**实现。 — 来源：[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）

## T

**TCP**
> Transmission Control Protocol，传输控制协议。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）
> 传输控制协议 — 来源：[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

**TCP/IP Stack**
> Ethernet communication stack，以太网通信栈。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

## U

**UDP**
> 用户数据报协议 — 来源：[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

**UdpNm**
> UDP网络管理 — 来源：[udp_network_management](communication/udp_network_management/index.md)（SWS_UDPNetworkManagement · R23-11）

**UDS**
> 统一诊断服务（**Unified Diagnostic Services**） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

## V

**Virtual page**
> 虚拟页面可能由一个或多个物理页面组成，以便于处理逻辑块和地址计算. — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

**VLAN**
> Virtual Local Area Network，虚拟局域网。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

## W

**Wakeup event**
> 唤醒事件被理解为将导致本驱动唤醒的边沿模式。但某个模式是否有效不由本驱动判定，而应由上层判定。 — 来源：[icu_driver](io/icu_driver/index.md)（SWS_ICUDriver · R22-11）

**WEth**
> Wireless Ethernet Driver，无线以太网驱动程序。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**WEthTrcv**
> Wireless Ethernet Transceiver Driver，无线以太网收发器驱动程序。 — 来源：[ethernet_interface](communication/ethernet_interface/index.md)（SWS_EthernetInterface · R23-11）

**WP**
> Autosar 工作包（**Work Package**） — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**Write Page**
> 写入页面（**Write Page**）是指存储设备的最小可写单元（以字节为单位）。因为一些存储设备技术的访问必须考虑到物理分段，所以并非所有存储设备技术都可以按字节访问。该术语定义了一次访问中需要写入页面最小的大小。 — 来源：[memory_access](memory/memory_access/index.md)（SWS_MemoryAccess · R23-11）

## 其他

**\<SrcLo\>**
> 下层通信接口模块，作为**I-PDU**的来源。**SrcLo**始终只有一个。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**上层模块(Up)（Upper Layer Modules）**
> PDU路由器模块的上方模块。该层通常包括**Com**和诊断通信管理器 (**Dcm**)。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**下层模块(Lo)（Lower Layer Modules）**
> PDU路由器模块的下方模块。该层可能包括**CAN**、**LIN**、**FlexRay**、以太网通信接口模块和相应的**TP**模块。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**中间PNC协调器**（**Intermediate PNC coordinator**）
> 中间PNC协调器是一个**ECU**，它充当网络中的PNC网关，并在至少一个分配的通道上将至少一个PNC处理为被动协调。如果启用了同步PNC关闭，它会将收到的这些PNC的关闭请求转发到相应的主动协调通道，并相应地启动它们的关闭。 — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**作业的优先级（Priority）**
> 作业的优先级定义了它的重要性。优先级（即：数值）越高，作业更需立即执行。加密作业的优先级属于配置的一部分。 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）、[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**先进先出（FIFO）缓冲**
> 缓冲区概念，采用先进先出策略。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**内部残留物（Internal residue）**
> 内部残留物是指，如果配置的块大小不是虚拟页面大小的整数倍，则最后一个虚拟页面末尾的未使用空间（参见图 3）. — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

**冗余副本（Redundant copy）**
> NVRAM管理器的一个概念：将相同的信息存储两次以提高数据存储的可靠性. — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

**加密原语（Crypto Primitive）**
> 加密原语是在加密驱动程序对象中实现的已配置加密算法的实例。除此之外，它也可以理解为是 CSM 为应用程序提供的功能，具体强调了底层的算法家族。例如： AES、MD5、RSA 等。或者是底层的算法模式，例如：ECB、CBC 等。 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）、[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**加密驱动程序对象（Crypto Driver Object）**
> 加密驱动程序实现一个或多个加密驱动程序对象。加密驱动程序对象可以在硬件或软件中提供不同的加密原语。加密驱动程序的每个加密驱动程序对象彼此独立。每个加密驱动对象只有一个工作区（即：只能同时执行一个加密原语）加密驱动对象之间独立性的唯一例外是默认随机数生成器的使用（参见 [SWS_Crypto_00225]）。 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）、[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**即时网关（on-the-fly gatewaying）**
> 网关的能力。两个TP 模块之间的路由，其中在接收到所有数据之前（达到指定阈值时）开始转发数据。如果在两个接口之间传输大量数据，则希望能够在从源网络接收所有数据之前在目标网络上开始传输。这样可以节省内存和时间。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**地址和长度格式标识符（AddressAndLengthFormatIdentifier）**
> 定义了请求消息中用于**memoryAddress**和**memorySize**参数的字节数。 — 来源：[diagnostic_communication_manager](diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager · R23-11）

**块管理类型（Block Management Type）**
> NVRAM块的类型。它取决于 NVRAM 块在不同强制/可选基本存储对象块中的（可配置）单独组合以及此 NVRAM 块的后续处理。 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**基本存储对象（Basic Storage Object）**
> “基本存储对象” 是 **NVRAM** 块的最小实体。多个基本存储对象可用于构建 **NVRAM** 块。“基本存储对象”可以驻留在不同的内存位置，包括：**RAM**、**ROM**、NV内存（**NV memory**）中。 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**多播操作（multicast operation）**
> 将PDU同时传输到一组接收者，即：1:n路由。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**密钥元素（Key Element）**
> 密钥元素用于存储数据。该数据可以是例如 AES 加密所需的密钥材料或者 IV。它还可用于配置密钥管理功能的行为。 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）、[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**密钥类型（Key Type）**
> 密钥类型由对密钥元素的引用组成。密钥类型通常由加密驱动程序的供应商预先配置。 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）、[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**密钥（Key）**
> 密钥可以被 **Csm** 中的作业引用。在加密驱动程序中，每个密钥需要引用特定的密钥类型。 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）、[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**应用层（Application Layer）**
> 应用层位于**RTE**之上。在应用层里放了**AUTOSAR**的软件组件。 — 来源：[diagnostic_communication_manager](diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager · R23-11）

**操作（Operation）**
> 一个加密原语的操作声明了应执行加密原语的哪一部分。 共有三种不同的操作模式： — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）、[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**数据提供（data provision）**
> 向接口模块提供数据。(a)直接数据提供：需传输的数据直接在传输请求时提供。目标通信接口可能以两种方式运行：直接复制数据或将复制推迟到触发传输。(b)触发传输数据提供：需传输的数据不是在传输请求时提供，而是由通信接口模块通过回调函数获取。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**数据集（Dataset）**
> NVRAM管理器的一个概念：用户可寻址的相同大小的块数组。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

**最后最好（last-is-best——缓冲**
> 最新值覆盖最后一个值的缓冲策略。 — 来源：[pdu_router](communication/pdu_router/index.md)（SWS_PduR · R23-11）

**服务（Service）**
> 服务需按照 TR_Glossary 文档中的定义来理解：服务是一种具有已发布的接口和行为规范的操作，涉及功能提供者与潜在客户之间的合同。 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）、[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）

**活动状态（Activity state）**
> 活动状态是正在执行的软件组件的状态。活动状态也来自作为前提条件的许可状态d和物理启用条件。它不是由**FiM**模块计算的，也不能作为状态变量使用。它只能从软件组件内的本地信息中获得。 — 来源：[function_inhibition_manager](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**物理地址（Physical address）**
> 物理地址是指用于访问逻辑块的设备特定格式的地址信息，取决于底层EEPROM驱动程序和设备。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

**管理块（Administrative Block）**
> “管理块”是“基本存储对象”。它驻留在 **RAM** 中。“**管理块**”是“**NVRAM块**”的强制部分。 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**虚拟地址（Virtual address）**
> 虚拟地址是由16位逻辑块号和逻辑块内的16位偏移量组成的地址. — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

**诊断事件管理器（DEM）**
> 诊断事件管理器（**Diagnostic Event Manager**） 接受报告的相关错误的模块 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**通道（Channel）**
> 通道是从加密服务管理器队列通过加密接口到特定加密驱动程序对象的路径。 — 来源：[crypto_driver](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）、[crypto_service_manager](crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager · R23-11）
> 可以进行数据传输的链接。如果有多个通道，通常会为通道分配某种类型的 ID。 — 来源：[diagnostic_communication_manager](diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager · R23-11）

**逻辑块（Logical block）/ 块（Block）**
> 逻辑块是模块用户看到的最小可写/可擦除单元。由一个或多个虚拟页面（**Virtual page**）组成。 — 来源：[flash_eeprom_emulation](memory/flash_eeprom_emulation/index.md)（SWS_FlashEEPROMEmulation · R23-11）

**重复报文请求位指示**（**Repeat Message Request Bit Indication**）
> **CanNm_RxIndication**在收到的网络管理**PDU**的控制位向量中找到**RptMsgRequest**集。 — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**闪存扇区**
> 闪存扇区（**Flash sector**）是一次可以擦除的最小闪存量。闪存扇区的大小取决于闪存技术，因此取决于硬件。 — 来源：[flash_driver](memory/flash_driver/index.md)（SWS_FlashDriver · R23-11）

**闪存访问代码**
> 由主函数（作业处理函数）调用的内部闪存驱动程序例程，用于擦除或写入闪存硬件。 — 来源：[flash_driver](memory/flash_driver/index.md)（SWS_FlashDriver · R23-11）

**闪存页**
> 闪存页面（**Flash page**）是一次可以编程的最小闪存量。闪存页面的大小取决于闪存技术，因此取决于硬件。 — 来源：[flash_driver](memory/flash_driver/index.md)（SWS_FlashDriver · R23-11）

**非易失性（NV）**
> 非易失性（**Non volatile**） — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）

**顶级PNC协调员**（**Top-level PNC coordinator**）
> 顶级PNC协调器是一个**ECU**，它充当网络中的PNC网关，并在所有分配的通道上主动协调处理至少一个PNC。如果启用了同步PNC关闭，如果网络中没有其他ECU请求它们，顶级PNC协调器将为这些PNC触发关闭。 — 来源：[can_network_management](communication/can_network_management/index.md)（SWS_CANNetworkManagement · R23-11）

**默认错误跟踪器（DET）**
> 默认错误跟踪器（**Default Error Tracer**）报告开发错误的模块。 — 来源：[nvram_manager](memory/nvram_manager/index.md)（SWS_NVRAMManager · R23-11）
