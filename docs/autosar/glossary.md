---
title: "AUTOSAR 术语表（缩略语与缩写）"
---

本页汇总各 AUTOSAR 模块文章以及 AUTOSAR TR 术语表（Foundation）的术语，按字母排序。

**Assembly Connector**
> 组装连接器。在 VFB 层级把一个组件的 RPort/PRPort 与另一个组件的 PPort/PRPort 连接起来的连接器；恰好连接一个提供端口与一个要求端口。
> 来源：[虚拟功能总线（VFB）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB · R23-11）

## A

**Accuracy**
> 精度（**Accuracy**）取决于用于采样或者生成的硬件外围设备。如：**ADC**转换器可以是 8/10/12/16 位转换器
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**AEB**
> 自主紧急制动（**Autonomous Emergency Braking**）。
> 来源：[ADAS 与车辆运动控制接口](application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC · R23-11）

**ACC**
> 自适应巡航控制（**Adaptive Cruise Control**）。
> 来源：[ADAS 与车辆运动控制接口](application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC · R23-11）


**Acquisition Time**
> 采集时间 = 采样时间（**Sample Time**）+ 转换时间（**Conversion Time**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**Activity state**
> 活动状态：软件组件正在执行时的状态。活动状态以许可状态为前提条件，并叠加物理使能条件。它不由 **FiM** 计算，也不作为状态变量提供，只能通过观察或测量确定。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**ADC**
> 模数转换器（**Analogue Digital Converter**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Channel**
> **ADC**通道是指绑定到一个端口引脚的逻辑**ADC**实体。同时多个**ADC**实体也可以映射到同一个端口引脚。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Channel Group**
> **ADC**通道组是指由一组**ADC**通道链接到同一个**ADC**硬件单元（**ADC HW Unit**）。例如：一个采样保持器（**Sample & Hold**）和一个**A/D**转换器。整个组的转换由一个触发源触发。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC HW Unit**
> 微控制器的输入电子设备，包括执行模拟到数字转换所需的所有部件。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Module**
> ADC的基础软件模块ADC驱动模块（**ADC Driver**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Result Buffer**（**ADC Streaming Buffer**，**ADC Stream Buffer**）
> **ADC**驱动程序的用户必须为每个组提供一个缓冲区。如果选择流式访问模式（**streaming access mode**），此缓冲区可以保存同一组通道的多个样本。如果选择单一访问模式（**Single Access Mode**），每个组通道的一个样本将保存在缓冲区中。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**Address Area**
> 地址区（**Address Area**）是指逻辑地址空间中连续的存储区域。通常，多个物理存储扇区组合成一个逻辑地址区。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**AI**
> 存活指示（**Alive Indication**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Alive Counter**
> **WdgM** 中在**检查点**上下文内的独立数据资源，用于跟踪和处理该**检查点**的**存活指示**数量。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Alive Indication**
> 由**被监督实体**的**检查点**提供的指示，用于向**WdgM** 标识其存活状态。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Alive Supervision**
> 一种监督，用于检查**被监督实体**的执行是否足够频繁且不过于频繁（包括容差）。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**API**
> 应用编程接口（**Application Programming Interface**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
> 来源：[AUTOSAR Standard Types（标准类型）](general/standard_types/index.md)（SWS_StandardTypes · R23-11）

**ASN.1**
> 抽象语法标记一号（**Abstract Syntax Notation One**）：一种描述数据结构的标准记法，常与 DER 编码规则一起用于证书等密码学数据的编码。
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**Atomic sequence/ atomic piece**
> 原子序列是一段不得被中断的测试。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Attributes**
> 属性（**Attributes**）是**ECU**中存在的每个**ECU**信号所包含的软件或者硬件特性。一些属性是固定的，由端口定义决定。还有一些属性是可以在**I/O**硬件抽象中进行配置的。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**AUTOSAR**
> 汽车开放系统架构（**AUTomotive Open System ARchitecture**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

## B

**Background test**
> 后台测试由 **SW** 调度器/**RTOS** 周期性调用。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Bank**
> 存储 **Bank** 是一组扇区批次（**Sector Batch**）的集合。如果存储技术支持按扇区分段，则存储 **Bank** 是不允许边读边写操作的扇区批次组实例。对于闪存设备，**Bank** 通常映射到单独的闪存控制器。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**BIST**
> 内建自测试（**Built in Self Test**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**BndM**
> 大容量非易失性数据管理器（**Bulk Non-Volatile Data Manager**）
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**ATWS**
> 防盗警告系统（**Anti-Theft Warning System**）。可借助光学与声学信号警示未授权进入尝试、并可防止发动机被起动的防盗系统。
> 来源：[车身与舒适域应用接口](application_interfaces/body_and_comfort/index.md)（AUTOSAR_CP_EXP_AIBodyAndComfort · R23-11）

**BSW**
> 基础软件（**Basic Software**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**BSW driver**
> 有关 BSW 驱动（**BSW driver**）的列表，请参阅基础软件模块列表中 "AUTOSAR SW layer" 列。
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**BswM**
> 基础软件模式管理器（**Basic Software Mode Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Bus Off**
> CAN 总线的错误状态：CAN 控制器因错误计数达到上限而与总线脱离。CAN 状态管理器（CanSM）通过 Bus Off 恢复状态机进行恢复。
> 来源：[错误描述](general/error_description/index.md)（AUTOSAR_CP_EXP_ErrorDescription · R23-11）

**BSWMD**
> 基础软件模块描述（**Basic Software Module Description**）
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**CDD**
> 复杂驱动（**Complex Driver**）。未被 AUTOSAR 标准化的软件实体，可以访问 AUTOSAR 接口和/或基础软件模块 API，或经由它们被访问；位于分层软件架构的复杂驱动层。
> 来源：[CDD 设计与集成指南](general/cdd_design_and_integration/index.md)（AUTOSAR_CP_EXP_CDDDesignAndIntegrationGuideline · R23-11）

**Crypto Primitive**
> 加密原语。在加密驱动对象中实现的一个已配置加密算法的实例。
> 来源：[加密服务使用指南](crypto/utilization_of_crypto_services/index.md)（AUTOSAR_CP_EXP_UtilizationOfCryptoServices · R23-11）

**Crypto Driver Object**
> 加密驱动对象。一个加密驱动实现一个或多个加密驱动对象；每个对象可提供不同加密原语，且只有一个工作区（同一时刻只能执行一个加密原语）。
> 来源：[加密服务使用指南](crypto/utilization_of_crypto_services/index.md)（AUTOSAR_CP_EXP_UtilizationOfCryptoServices · R23-11）

## C

**Callback**
> 术语回调函数（**Callback**）主要用于**API**服务，实现通知其他**BSW**模块。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Caller/calling entity**
> 调用者/调用实体位于较高的 **AUTOSAR** 或 **ISO** 层。它是 **API** 调用的用户。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Camel case**
> 驼峰命名法：书写短语时不带空格或标点符号、以单个大写字母指示单词之间分隔的书写方式，第一个单词以大写或小写开头。示例：GetVersionInfo。
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**Callout**
> **Callout**是一种函数**Stub**。主要在配置时进行填写，目的是向提供**Callout**函数的模块添加功能。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**CDD**
> 复杂设备驱动程序（**Complex Device Driver**）。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）

**Channel**
> 通道：从加密服务管理器队列经由加密接口到特定加密驱动程序对象的路径。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）

**Class**
> 一个类（**Class**）代表一组具有相似电气特性的信号。如：模拟类（**Analogue class**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Client-Server communication**
> 客户端-服务器通信（**Client-Server communication**）涉及两个实体。客户端是要求服务的一方，服务器是提供服务的一方。客户端发起通信，请求服务器执行服务，必要时传输参数集合。服务器以**RTE**的形式，等待来自客户端的传入通信请求，执行请求的服务并发送对客户端请求的响应。因此服务启动的方向是用来对**AUTOSAR**软件组件是客户端还是服务器分类的主要标识。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Checkpoint**
> **被监督实体**控制流中的一个点，在该处向**WdgM** 报告活动。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Com**
> 通信（**Communication**）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**Conversion Mode**
> One-Shot：**ADC**通道组的转换在触发后执行一次，结果写入所分配的结果缓冲区。触发可以是软件**API**调用或硬件事件。Continuous：**ADC**通道组的转换在软件**API**调用（启动）后连续执行，结果写入所分配的结果缓冲区。转换本身自动运行（由硬件/中断控制）。连续转换可通过软件**API**调用（停止）停止。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**Conversion Time**
> 转换时间是指将采样的模拟值转换为数值所需的时间。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**Core**
> **CPU** 及其紧邻的功能资源。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**CPU**
> 中央处理器（**Central Processing Unit**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Cross-Cluster External Graph**
> 一种特殊的**外部图**，在集群式软件架构下跨越多个**软件集群**（**Software Cluster**）。其配置依赖于模式（由**宿主软件集群**（**Host Software Cluster**）控制），并且另外具有专门的配置结构。注意：单个**软件集群**内的**外部图**可以在不使用集群式软件架构专门配置结构的情况下建模。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**C/S**
> 客户端/服务器（**Client/Server**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**CRYIF**
> 加密接口（**Crypto Interface**）。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**CRYPTO**
> 加密驱动程序（**Crypto Driver**）。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）

**Crypto Driver Object**
> 加密驱动程序对象：加密驱动程序实现一个或多个加密驱动程序对象，每个对象可以在硬件或软件中提供不同的加密原语；同一加密驱动程序的各加密驱动程序对象彼此独立，每个对象只有一个工作区（即同一时刻只能执行一个加密原语），独立性的唯一例外是默认随机数生成器的使用。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）

**Crypto Primitive**
> 加密原语：在加密驱动程序对象中实现的已配置加密算法的实例；它指向 **CSM** 向应用程序提供的功能、具体的底层算法家族（如 **AES**、**MD5**、**RSA**）以及算法模式（如 **ECB**、**CBC**）。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**CS**
> 片选（**Chip Select**）。
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）

**CSM**
> 加密服务管理器（**Crypto Service Manager**）。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**CSUM/Checksum/signature**
> 测试执行结果的数值表示。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**CVC**
> 卡片可验证证书（**Card Verifiable Certificate**）。
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）


## D

**&lt;DstLo&gt;**
> 作为 L-SDU 目标的下层通信接口模块。DstLo 可以是一对多。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）

**Data frame**
> 数据帧：**SPI** 总线上与 SpiDataWidth 相关的位的物理帧。
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）

**DCM**
> 诊断通信管理器（**Diagnostic Communication Manager**）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**Deadline End Checkpoint**（**Deadline Stop Checkpoint**）
> 为其配置了**截止时间监督**、并且是某个特定**截止时间监督**终点的**检查点**。一个**检查点**可以同时是**截止时间起始检查点**和**截止时间结束检查点**——即当**截止时间监督**被串联时。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Deadline Start Checkpoint**
> 为其配置了**截止时间监督**、并且是某个特定**截止时间监督**起点的**检查点**。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Deadline Supervision**
> 一种监督，用于检查两个**检查点**之间的执行时间是否小于给定的执行时间上限。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**DEM**
> 诊断事件管理器（**Diagnostic Event Manager**）。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）
> 来源：[AUTOSAR Large Data COM（大数据 COM）](communication/large_data_com/index.md)（SWS_LargeDataCOM · R23-11）

**DET**
> 默认错误跟踪器（**Default Error Tracer**），实现报告开发错误的模块。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）
> 来源：[AUTOSAR Default Error Tracer（默认错误跟踪器）](system_services/default_error_tracer/index.md)（SWS_DefaultErrorTracer · R23-11）
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）
> 来源：[AUTOSAR Large Data COM（大数据 COM）](communication/large_data_com/index.md)（SWS_LargeDataCOM · R23-11）

**DIP**
> 数字输入/输出（**Digital Input/Output**）
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

## E

**EAI**
> 期望存活指示（**Expected Alive Indications**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**EB**
> 外部缓冲通道（**Externally buffered channels**）：包含待传输数据的缓冲区位于 SPI 处理器/驱动程序之外。
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）

**ECC**
> 纠错码（**Error Correction Code**）
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**ECU**
> 电子控制单元（**Electronic Control Unit**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**ECU pin**
> ECU引脚（**ECU pin**）是**ECU**与电子系统其余部分的电气硬件连接。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**ECU Signal**
> ECU信号（**ECU Signal**）是电信号的软件表示。一个**ECU**信号具有一些属性（**Attribute**）和一个符号名称（**Symbolic name**）。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**ECU Signal Group**
> ECU信号组（**ECU Signal Group**）是一组电信号的软件表示。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**EcuC**
> **ECU** 配置（**ECU Configuration**）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**EcuM**
> **ECU** 状态管理器（**ECU State Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**e.g.**
> （拉丁语）exempli gratia =（英语）for example，即「例如」。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**i.e.**
> （拉丁语）id est =（英语）that is，即「也就是说」。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**Electrical Signal**
> 电信号（**Electrical Signal**）代表**ECU**引脚上的物理信号。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Expired Supervision Cycle**
> 一个**监督周期**，其中**存活监督**已失败其两个升级步骤（**存活计数器**失败的**期望存活指示**数量（包括容差）超过允许的失败参考周期次数）。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**External device**
> 物理外部实体；例如另一个微控制器。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**External Graph**
> 可能涉及多于一个**被监督实体**的**图**。其配置依赖于模式。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**External Transition**
> **外部转换**是两个**检查点**之间的**转换**，其中这两个**检查点**属于不同的**被监督实体**。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[应用层错误处理](general/application_level_error_handling/index.md)

**FDIR**
> 故障检测、隔离与恢复（**Fault Detection, Isolation and Recovery**）。系统运行期间处理故障的过程：检测→隔离→恢复。
> 来源：[应用层错误处理](general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling · R23-11）

## F

**Fast-Mode**
> 对看门狗硬件的触发必须以较短的超时期限完成。例如，该模式可用于 **ECU** 的正常运行。例如，看门狗硬件被配置为窗口模式（触发看门狗必须发生在超时期限内的特定最小/最大边界中）且超时期限为 5 毫秒。
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**Failed Supervision Reference Cycle**
> 一个**监督参考周期**，其结束时刻检测到**存活计数器**与**期望存活指示**数量之间存在偏差（包括容差）。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**FID**
> 功能标识符（**Function Identifier**）：在 **FiM** 中标识一个应用程序功能及其相关禁止条件的标识符。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**FiM**
> 功能抑制管理器（**Function Inhibition Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**Foreground test**
> 前台测试是同步测试，不得被中断。它通过用户应用程序调用。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**FOTA**
> 固件远程升级（**Firmware Over The Air**），通过无线通信进行固件远程更新。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）
> 来源：[固件远程升级指南（FOTA）](memory/firmware_over_the_air/index.md)（AUTOSAR_CP_EXP_FirmwareOverTheAir · R23-11）

**Functionality**
> 功能：涵盖系统用户可见和用户不可见的功能方面（见 [2]）。在 **FiM** 上下文中，一个功能可以由一个或多个可运行实体的全部或部分内容、以同一组许可/禁止条件构成。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**Fault**
> 故障。系统的瞬态或永久性变化，使其完整性偏离预期的正确完整性；被激活并传播后成为错误（error）。
> 来源：[应用层错误处理](general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling · R23-11）

**Error**
> 错误。系统中的错误（软）状态，即该状态不同于若故障不存在时系统应有的状态；传播越过系统屏障即转变为失效（failure）。
> 来源：[应用层错误处理](general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling · R23-11）

**Failure**
> 失效。错误传播越过系统屏障、对系统环境可见后的结果：系统不再提供其规定的功能。
> 来源：[应用层错误处理](general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling · R23-11）

## G

**Global Supervision Status**
> 汇总所有**被监督实体****局部监督状态**的状态。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Golden (Ref.) Value**
> 用于与先前计算出的测试结果值进行比较的参考值（例如校验和/签名）。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Good Case**
> 执行完成且未报告错误。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**GPT**
> 通用定时器（**General Purpose Timer**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**GPT Predef Timer**
> **GPT Predef Timer** 是 **GPT** 驱动程序提供的自由运行递增计数器。哪些 **GPT Predef Timer** 可用取决于硬件（时钟、硬件定时器、预分频器、定时器寄存器宽度等）和配置。**GPT Predef Timer** 具有预定义的物理时间单位和范围。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)（SWS_TimeService · R23-11）

**Graph**
> 控制流图（**Control Flow Graph**）。一组通过**转换**相连的**检查点**，其中至少有一个**检查点**是**初始检查点**。在该**图**的任意两个**检查点**之间都存在一条（通过**转换**的）路径。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

## H

**Hardware Trigger**
> 硬件触发是**ADC**内部触发信号，用于启动ADC通道组的一次转换。**ADC**硬件触发在ADC硬件内部生成（例如：基于**ADC**定时器或触发沿信号）。触发硬件是强耦合或者直接集成在**ADC**的硬件中。当检测到硬件触发后，无需软件即可启动**ADC**通道组转换。**注意：**即使**ADC**硬件不支持硬件触发，也可以通过软件触发结合**GPT/ICU**驱动程序来实现类似的行为。（例如：在GPT定时器通知函数中，启动软件触发的**ADC**通道组的转换）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**HSM**
> 硬件安全模块（**Hardware Security Module**），专用安全 **MCU** 的内核。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）

**IFX**
> 定点插值库（**Fixed Point Interpolation Routines**）的模块 ID 前缀；整数插值例程名称以 Ifx 开头。
> 来源：[插值调用宏封装](libraries/macro_encapsulation_of_interpolation_calls/index.md)（AUTOSAR_CP_EXP_MacroEncapsulationofInterpolationCalls · R23-11）

**IFL**
> 浮点插值库（**Floating Point Interpolation Routines**）的模块 ID 前缀；浮点插值例程名称以 Ifl 开头。
> 来源：[插值调用宏封装](libraries/macro_encapsulation_of_interpolation_calls/index.md)（AUTOSAR_CP_EXP_MacroEncapsulationofInterpolationCalls · R23-11）

**HW**
> 硬件（**Hardware**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）

## I

**I-PDU**
> 交互层 **PDU**（**Interaction Layer PDU**）。在 **AUTOSAR** 中，交互层等价于通信服务层。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）
**I-PDU ID**
> I-PDU 标识符（**I-PDU Identifier**）。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）

**IB**
> 内部缓冲通道（**Internally buffered channels**）：包含待传输数据的缓冲区位于 SPI 处理器/驱动程序之内。
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）

**ICC**
> 实现一致性等级（**Implementation Conformance Class**）。AUTOSAR 对基础软件实现合规程度的分级（ICC1–ICC3）：ICC3 要求逐模块符合 AUTOSAR 规范，ICC2 允许项目定义的集群，ICC1 为专有基础软件（对外行为仍须符合 ICC3 模块规范）。
> 来源：[分层软件架构（Layered Software Architecture）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture · R23-11）

**ICU**
> 输入捕获单元（**Input Capture Unit**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**ID**
> 标识符（**Identifier**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**&lt;Ie&gt;**
> 实现特定文件名扩展名（**implementation specific file name extension**）
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**IdsM**
> 入侵检测系统管理器（**Intrusion Detection System Manager**）。
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**Inhibition Condition**
> 禁止条件：一个 **FID**、一个禁止掩码与 **Dem** 事件/组件状态之间的关系（见 FiMInhibitionConfiguration）。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**Internal Graph**
> 不跨越若干**被监督实体**的**图**。其配置与模式无关，并且可以通过禁用对应的**被监督实体**而被禁用。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Internal Transition**
> **内部转换**是同一个**被监督实体**内两个**检查点**之间的**转换**。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Inversion**
> 物理值与逻辑值的反转（**Inversion**）。此属性不可见，但可以由**I/O**硬件抽象来实现，并向用户传递预期值。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**IoHwAb**
> 输入/输出硬件抽象（**Input/Output Hardware Abstraction**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**int**
> 整数（**Integer**）
> 来源：[AUTOSAR Platform Types（平台类型）](general/platform_types/index.md)（SWS_PlatformTypes · R23-11）

**IRQ**
> 中断请求（**Interrupt Request**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**ISR**
> 中断服务程序（**Interrupt Service Routine**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
> 来源：[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping · R23-11）

**IUMPR**
> 在使用中的监控性能比（**In-Use-Monitor Performance Ratio**）。
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）


**Job**
> 作业。一个已配置的加密原语与一个被引用的密钥的组合；不包含实际密钥数据本身。
> 来源：[加密服务使用指南](crypto/utilization_of_crypto_services/index.md)（AUTOSAR_CP_EXP_UtilizationOfCryptoServices · R23-11）

## J

**Job**
> 作业：一个已配置的 **CsmJob**，它引用一个密钥、一个加密原语和一个参考通道。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）

**Job Request**
> 作业请求（**Job Request**）是指上层模块对地址区的存储访问请求。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

## K

**Key**
> 密钥：密钥可以被 **Csm** 中的作业引用；在加密驱动程序中，每个密钥引用一种特定的密钥类型。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**Key Element**
> 密钥元素：用于存储数据（例如 **AES** 加密所需的密钥材料或 **IV**），也可用于配置密钥管理功能的行为；不同密钥的密钥元素拥有不同的存储区域（**NV** 区域和 **RAM** 区域）。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**Key Type**
> 密钥类型：由对密钥元素的引用组成，通常由加密驱动程序的供应商预先配置。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

## L

**&lt;Lo&gt;**
> 下层通信接口模块。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）

**L-PDU**
> 数据链路层 **PDU**（**Data Link Layer PDU**）。在 **AUTOSAR** 中，数据链路层等价于通信硬件抽象和微控制器抽象层。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）
**L-PDU ID**
> L-PDU 标识符（**L-PDU Identifier**）。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）
**L-SDU**
> 链路层服务数据单元（**Data link layer service data unit**）。一个 L-SDU 由数据（缓冲区）、长度、L-SDU ID 以及可能经由元数据传输的 L-PDU 特定信息组成。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）
**L-SDU ID**
> L-SDU 标识符（**L-SDU identifier**）。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）
**L-SDU Router**
> 在模块之间传输 L-SDU 的模块。L-SDU Router 模块可用于内部路由目的。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）

**L1**
> 第一级存储器（**1st level memory**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**L2**
> 第二级存储器（**2nd level memory**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**LKA**
> 车道保持辅助（**Lane Keep Assist**）。
> 来源：[ADAS 与车辆运动控制接口](application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC · R23-11）

**Local Supervision Status**
> 表示单个**被监督实体**当前存活监督结果的状态。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Logical Supervision**
> 一种对软件的在线监督，用于检查软件（**被监督实体**或一组**被监督实体**）是否按程序员（即已开发的代码）定义的顺序执行。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
**Lower Layer Modules（Lo）**
> 位于 L-SDU Router 之下的模块。该层包括以太网通信接口模块。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）

## M

**MAKW**
> 内存分配关键字（**Memory Allocation Key Word**）
> 来源：[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping · R23-11）

**Master**
> 主。分布式 BSW 模块中协调卫星请求、并可过滤或监控进入的卫星请求的部分。
> 来源：[BSW 分布指南](general/bsw_distribution_guide/index.md)（AUTOSAR_CP_EXP_BSWDistributionGuide · R23-11）

**MCAL**
> 微机抽象层（**Microcomputer Abstraction Layer**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**&lt;Ma&gt;**
> 模块缩写（**Module abbreviation**）
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**&lt;MA&gt;**
> 大写模块缩写（**Capitalized module abbreviation**），即完全以大写形式书写的模块缩写 &lt;Ma&gt;
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**MCU**
> 微控制器单元（**Microcontroller Unit**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Memory Device**
> 存储设备（**Memory Device**）是指一组存储 **Bank** 的组合。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**&lt;Mip&gt;**
> 模块实现前缀（**Module implementation prefix**）
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**&lt;MIP&gt;**
> 大写模块实现前缀（**Capitalized module implementation prefix**），即完全以大写形式书写的模块实现前缀 &lt;Mip&gt;
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**MIL**
> 故障指示灯（**Malfunction Indication Light**）。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**MISO**
> Master Input Slave Output（主入从出）。
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）

**Mode**
> 模式是车辆中运行的各个状态机的特定状态集合，这些状态与某个特定实体相关，例如 **SW-C**、**BSW** 模块、应用或整个车辆。在其生命周期内，一个实体在一组互斥的模式之间切换。这些切换由环境数据触发，例如信号接收、操作调用。在**看门狗管理器**的上下文中，一个模式由一组配置选项定义。被监督的**被监督实体**集合可以随模式而变化。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Module abbreviation**
> 模块缩写（**Module abbreviation**）
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**Module implementation prefix**
> 模块实现前缀（**Module implementation prefix**），用于构成 BSW 模块实现的工作成果中使用的各种标识符（例如 API 名称、参数名称、符号和文件名），主要由模块缩写构成，必要时加上额外的厂商特定信息
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**Monitoring function**
> 监控功能：软件组件的一部分；用于监控并最终检测某个传感器、执行器故障或进行合理性检查的机制；报告来自 **SW-C** 内部处理或来自其他块返回值进一步处理的事件状态。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**MOSI**
> Master Output Slave Input（主出从入）。
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）

**MPU**
> 内存保护单元（**Memory Protection Unit**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）



**Master**
> 主。分布式 BSW 模块中协调卫星请求、并可过滤或监控进入的卫星请求的部分。
> 来源：[BSW 分布指南](general/bsw_distribution_guide/index.md)（AUTOSAR_CP_EXP_BSWDistributionGuide · R23-11）
## N

**N-PDU**
> 网络层 **PDU**（**Network Layer PDU**）。在 **AUTOSAR** 中，网络层等价于传输协议。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**nop**
> 无操作（**No Operation**）。
> 来源：[AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)（SWS_TimeService · R23-11）

**NOP, nop**
> 空操作（**Null Operation**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**NVRAM**
> 非易失性 RAM（**Non-Volatile RAM**）
> 来源：[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping · R23-11）

**OSEK/VDX**
> 汽车电子开放系统及其接口（**Offene Systeme und deren Schnittstellen fuer die Elektronik im Kraftfahrzeug**）
> 来源：[AUTOSAR Standard Types（标准类型）](general/standard_types/index.md)（SWS_StandardTypes · R23-11）

## O

**OBD**
> 车载诊断（**On-board Diagnostics**）。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**OBDII**
> 排放相关车载诊断（**Emission-related On-board Diagnostics**）。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**Off-Mode**
> 看门狗硬件被禁用/关闭。这样做可能是为了关闭整个 **ECU**，而不遭受仍在运行的外部看门狗的周期性复位。对于安全关键系统，该模式可能不被允许。在这种情况下，必须将 **Wdg** 模块配置为禁止切换到此模式。
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**OID**
> 对象标识符（**Object Identifier**）。
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**Operation**
> 操作：加密原语的操作声明应执行加密原语的哪一部分，共有 **START**、**UPDATE**、**FINISH** 三种操作模式；通过拼接操作模式参数的相应位可以一次执行多个操作。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）

**OSEK/VDX**
> 1993 年 5 月，**OSEK** 作为德国汽车工业的一个联合项目创立，旨在为车辆内分布式控制单元的开放式架构建立一个行业标准。**OSEK** 是德语术语「Offene Systeme und deren Schnittstellen für die Elektronik im Kraftfahrzeug」（英语：Open Systems and the Corresponding Interfaces for Automotive Electronics）的缩写。初始项目合作伙伴为 **BMW**、**Bosch**、**Daimler Chrysler**、**Opel**、**Siemens**、**VW** 以及作为协调方的卡尔斯鲁厄大学 **IIIT**。法国汽车制造商 **PSA** 和 **Renault** 于 1994 年加入 **OSEK**，引入了他们的 **VDX**（**Vehicle Distributed eXecutive**）方案——法国汽车工业内的一个类似项目。在 1995 年 10 月的第一次研讨会上，**OSEK/VDX** 小组展示了 **OSEK** 与 **VDX** 之间协调一致的规范成果。1997 年 10 月第 2 届国际 **OSEK/VDX** 研讨会之后，发布了规范的第二版。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**OS**
> 操作系统（**Operating System**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**OTA**
> 远程升级（**Over The Air**），OEM 后台（**backend**）与车辆之间无线通信的总称。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

## P

**Page Burst**
> 通过聚合访问存储页面来提高性能。在存储设备技术支持物理分段的情况下，一些存储设备可以提供一次读取或写入多个页面的优化访问方式。页面突发（**Page Burst**）表示用于访问优化的存储页面聚合。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**Port-Interface**
> 端口接口。定义提供或要求该接口的端口必须履行的契约；AUTOSAR 支持客户端-服务器、发送者-接收者、参数、非易失性数据、触发与模式切换六种端口接口。
> 来源：[虚拟功能总线（VFB）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB · R23-11）

**Prototype**
> 原型。组件类型在一个组合（Composition）中的使用；组合经由相互连接的原型定义。
> 来源：[虚拟功能总线（VFB）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB · R23-11）

**PASE**
> 无源进入（**Passive Entry**）。帮助用户无需物理使用钥匙即可进入汽车的锁定系统。
> 来源：[车身与舒适域应用接口](application_interfaces/body_and_comfort/index.md)（AUTOSAR_CP_EXP_AIBodyAndComfort · R23-11）

**Partial test**
> 部分测试定义为一个或多个「硬件资源」的测试。（部分测试是可中断的，因为它在后台模式下执行。）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**PCI**
> 协议控制信息（**Protocol Control Information**）。把一个 SDU 从协议层的一个实例传递到另一个实例所需的信息，例如源与目标信息。PCI 由发送侧的协议层添加，在接收侧移除。PDU 包含 SDU 和 PCI。
> 来源：[分层软件架构（Layered Software Architecture）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture · R23-11）

**PDU**
> 协议数据单元（**Protocol Data Unit**）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）
> 来源：[分层软件架构（Layered Software Architecture）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture · R23-11）
> 来源：[虚拟功能总线（VFB）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB · R23-11）
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）

**PNC**
> 部分网络集群（**Partial Network Cluster**）。一组系统信号，用于支持分布在车辆网络多个 ECU 上的一个或多个车辆功能；表示把一组总线映射到一个或多个虚拟功能集群（VFC）的系统视图。
> 来源：[分层软件架构（Layered Software Architecture）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture · R23-11）

**Permission state**
> 许可状态：包含由其 **FID** 表示的功能是否可以执行的信息。该状态由 **FiM** 基于已报告的事件控制。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**PKI**
> 公钥基础设施（**Public Key Infrastructure**）。
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**Primitive**
> 原语：在加密驱动程序对象中实现的已配置加密算法的实例；它指向 **CSM** 向应用程序提供的功能、具体的底层算法家族（如 **AES**、**MD5**、**RSA**）以及算法模式（如 **ECB**、**CBC**）。
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）

**Priority**
> 优先级：作业的优先级定义其重要性，优先级（数值）越高，作业越需立即执行；加密作业的优先级是配置的一部分。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）

**Processing**
> 处理：指示作业处理的类型。异步（**Asynchronous**）：调用相应函数时作业不会被立即处理，通常由后续的调度函数处理并通过回调通知结果；同步（**Synchronous**）：调用相应函数时作业被立即处理，函数返回时结果已可用。
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）


## R

**Runnable**
> 可运行体。原子软件组件实现中的一段可由 RTE 启动的指令序列；在任务的上下文中运行。
> 来源：[虚拟功能总线（VFB）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB · R23-11）



**Range**
> 范围（**Range**）在这里是一个功能范围（**functional range**），而不是电气范围（**electrical range**）。所有范围都用于功能的需要或者诊断的检测。对于模拟**ECU**信号，可以定义上下限值 [lowerLimit...upperLimit]（电压、电流）。对于电阻信号和时序信号（周期）的特殊情况，下限值（**lowerLimit**）不能为负。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Reference time**
> 参考时间：为每个计时器实例存储的时间值，是 **API** 数据类型 Tm_PredefTimer...bitType 所对应的实现特定元素。
> 来源：[AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)（SWS_TimeService · R23-11）

**Resolution**
> 分辨率（**Resolution**）属性适用于依赖于范围和数据类型的许多类别。如：(upperLimit - lowerLimit) / (2<sup>datatypelength</sup> -1)。 对于其他类别，它可能是已知和被定义的。如：[-12 Volts…+12Volts]，数据类型: 16 bits，**Resolution** 为 24 / 65535。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Resource**
> 「硬件资源」是 **CoreTest** 驱动程序用户可以选择的最小单元（实例）。它可以在一个或多个原子序列中被测试。它是执行特定功能（例如 **IRQ** 控制器）的内核内部单元。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**RTE**
> 运行时环境（**Runtime Environment**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Runnable entity**
> 可运行实体：原子软件组件的一部分，可以独立于该原子软件组件的其他可运行实体被执行和调度。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）

**RWW**
> 并行读写（**Read While Write**）。指存储设备在一个存储 **Bank** 中执行读取操作，同时在另一个存储 **Bank** 中执行写入或擦除操作的能力。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**RKE**
> 遥控无钥匙进入（**Remote Keyless Entry**）。设计用于远程锁定或解锁汽车进入的系统；单向广播无线电波，实现加密与滚动码算法。
> 来源：[车身与舒适域应用接口](application_interfaces/body_and_comfort/index.md)（AUTOSAR_CP_EXP_AIBodyAndComfort · R23-11）

## S

**&lt;SrcLo&gt;**
> 作为 L-SDU 源的下层通信接口模块。SrcLo 始终只有一个。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）

**Satellite**
> 卫星。分布式 BSW 模块的一部分；主与卫星之间的工作分配是实现特定的，卫星一般不能在没有主的情况下工作。
> 来源：[BSW 分布指南](general/bsw_distribution_guide/index.md)（AUTOSAR_CP_EXP_BSWDistributionGuide · R23-11）

**Sampling rate**
> 采样率（**Sampling rate**）是获得信号值所需的时间段。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Sampling Time, Sample Time**
> 采样时间是指对模拟值进行采样的时间（例如：加载电容器，……）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**SC**
> 监督周期（**Supervision Cycle**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Rollover mechanism**
> 下面的示例序列被称为"回绕"（**rollover**）：一个无符号字符（**unsigned char**）的值为 255；将其加 1；结果为 0。
> 来源：[AUTOSAR Platform Types（平台类型）](general/platform_types/index.md)（SWS_PlatformTypes · R23-11）

**SDU**
> 服务数据单元（**Service Data Unit**）——**PDU** 的载荷。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）
> 来源：[AUTOSAR Platform Types（平台类型）](general/platform_types/index.md)（SWS_PlatformTypes · R23-11）
> 来源：[分层软件架构（Layered Software Architecture）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture · R23-11）
> 来源：[虚拟功能总线（VFB）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB · R23-11）
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）

**SE**
> 被监督实体（**Supervised Entity**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Sector**
> 扇区（**Sector**）是指最小的可擦除存储单元（以字节为单位）。某些存储设备技术在写入存储前需要显式执行物理擦除操作。扇区定义了此类擦除单元的最小大小。根据存储设备的不同，扇区可以为统一大小或可变大小。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**Sector Batch**
> 扇区批次（**Sector Batch**）是大小统一的扇区集合，即大小相同且连续的扇区的逻辑集合。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**Sector Burst**
> 扇区突发（**Sector Burst**）是聚合扇区以提高擦除性能。如果存储技术需要物理擦除操作，一些设备会通过一步擦除一组扇区来优化擦除性能。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**Sender-receiver communication**
> 发送方-接收方通信涉及原子数据元素组成的信号的发送和接收，这些原子数据元素由一个组件发送给另一个或多个组件。发送方-接收方接口可以包含多个数据元素。发送方-接收方通信是单向的 接收方发送的任何回复都可以视为一个单独的发送方-接收方通信。接收方组件的端口可以读取接口描述定义的数据元素，而提供方组件的端口可以按照接口描述定义写入数据元素。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Sequence**
> 序列：若干个待传输的连续作业，但可以使用优先级机制在作业之间重新调度；序列传输是否可被中断取决于静态配置。
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver · R23-11）

**Service**
> 服务：按 **TR_Glossary** 文档的定义理解——服务是一种具有已发布的接口和行为规范的操作，涉及功能提供者与潜在客户之间的合同。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**SFR**
> 特殊功能寄存器（**Special Function Register**），**MCU** 寄存器
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）

**SHE**
> 安全硬件扩展（**Security Hardware Extension**）。
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）

**Slow-Mode**
> 对看门狗硬件的触发可以以较长的超时期限完成。例如，该模式可用于系统启动/初始化阶段。例如，看门狗硬件被配置为翻转模式（对触发的时间点没有约束）且超时期限为 20 毫秒。
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**Software Trigger**
> 软件触发是一个软件**API**调用，用于启动转换一个**ADC**通道组或一系列连续**ADC**通道组转换的。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**SOTA**
> 软件远程升级（**Software Over The Air**），使用无线通信进行软件远程更新。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**S/R**
> 发送方/接收方（**Sender/Receiver**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**SPI**
> 串行外设接口（**Serial Peripheral Interface**）
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**SRC**
> 监督参考周期（**Supervision Reference Cycle**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Sub Address Area**
> 子地址区（**Sub Address Area**）是指逻辑地址空间中的连续存储区域，并映射到一个存储设备的一个扇区批次（**Sector Batch**）。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

**Supervised Entity**
> 被纳入**WdgM** 监督的软件实体。每个**被监督实体**恰好具有一个标识符。**被监督实体**表示软件组件类型或基础软件模块某个实例内的一组**检查点**。在一个软件组件类型或基础软件模块的实例中，可以有零个、一个或多个**被监督实体**。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Supervised Entity Identifier**
> 在一个应用内唯一标识某个**被监督实体**的**标识符**。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Supervision Counter**
> 在**被监督实体**上下文内的独立数据资源，由**WdgM** 在每个**监督周期**期间更新，并被**存活监督**算法用于执行对已计数**存活指示**的检查。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Supervision Cycle**
> **WdgM****监督参考周期**的时基，在其中执行周期性的**存活监督**。它同时也是更新**全局监督状态**以及执行由此产生的恢复动作的间隔。这在所属 **WdgM** 的主函数每次被调用时完成，并且依赖于模式（在切换模式时可能变化）。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Supervision Reference Cycle**
> **存活监督**用于执行已计数**存活指示**检查所使用的**监督周期**数量（对每个**被监督实体**分别确定），并且依赖于模式。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**SW**
> 软件（**Software**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver · R23-11）
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface · R23-11）

**SW-C**
> 软件组件（**Software Component**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**SWC**
> 软件组件（**SoftWare Component**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**SWCD**
> 软件组件描述（**Software Component Description**）
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**Symbolic name**
> ECU信号的符号名称（**Symbolic name**）在**I/O**硬件抽象模块中是用来建立链接的。（包括：功能、引脚等）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**STD**
> 标准（**Standard**）
> 来源：[AUTOSAR Standard Types（标准类型）](general/standard_types/index.md)（SWS_StandardTypes · R23-11）



**Satellite**
> 卫星。分布式 BSW 模块的一部分；主与卫星之间的工作分配是实现特定的，卫星一般不能在没有主的情况下工作。
> 来源：[BSW 分布指南](general/bsw_distribution_guide/index.md)（AUTOSAR_CP_EXP_BSWDistributionGuide · R23-11）
## T

**Target time**
> 目标时间：到达该值时应有某事发生。其行为取决于配置和已启用的功能。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**test interval**
> **CoreTest** 测试间隔：在配置为构成一个完整内核测试的硬件资源上（后台模式下执行的）所有部分测试的总和。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Test Interval Id**
> 测试间隔的标识符，每开始一个新的测试间隔时应递增。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Tick**
> 定义定时器分辨率，即定时器一次递增的持续时间。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**Time Service Predef Timer**
> 时间服务预定义定时器：一种自由运行的计数器，具有预定义的物理时间单位和范围；硬件定时器的功能基于相应的 **GPT** 预定义定时器。时间服务模块为每个预定义定时器提供一组 **API** 服务，用户可以实例化任何计时器（仅受可用内存限制）并完全独立地使用这些实例。
> 来源：[AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)（SWS_TimeService · R23-11）

**Timer channel**
> 表示分配给一个定时器硬件的逻辑定时器实体。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**Timer instance**
> 定时器实例：由 **API** 数据类型 Tm_PredefTimer...bitType 所对应的一个数据对象，即用户软件级别上的时间服务预定义定时器的实例化。
> 来源：[AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)（SWS_TimeService · R23-11）

**TP**
> 传输协议（**Transport Protocol**）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

## U

**uC**
> 微控制器（**Microcontroller**）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）

**UDS**
> 统一诊断服务（**Unified Diagnostic Services**）。
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager · R23-11）
**&lt;Up&gt;**
> 上层通信接口模块。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）
**Upper Layer Modules（Up）**
> 位于 L-SDU Router 之上的模块。该层通常包括 **IEEE1722Tp**。
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter · R23-11）

## V


**VMC**
> 车辆运动控制（**Vehicle Motion Control**）。
> 来源：[ADAS 与车辆运动控制接口](application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC · R23-11）

**VFB**
> 虚拟功能总线（**Virtual Functional Bus**）。AUTOSAR 中允许组件相互交互的通信机制；应用被建模为相互连接的组件的组合，组件经由端口与端口接口交互。
> 来源：[虚拟功能总线（VFB）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB · R23-11）

**Variation Point**
> 变体点。设计中在 2 个或更多变体之间给出选择的位置；必须做出选择的时间称为最晚绑定时间。
> 来源：[虚拟功能总线（VFB）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB · R23-11）

**VFC**
> 虚拟功能集群（**Virtual Function Cluster**）。把实现一个或多个车辆功能所需的 SW 组件之间端口层面的通信分组；逻辑视图，允许可复用的、独立于总线/ECU 的设计。在部分组网（Partial Networking）中，VFC 映射到一个或多个部分网络集群（PNC）。
> 来源：[分层软件架构（Layered Software Architecture）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture · R23-11）

## W

**WCET**
> 最坏情况执行时间（**Worst case execution time**）
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral · R23-11）

**WDG**
> 看门狗（**Watchdog**，模块特定前缀）
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**WdgM**
> 看门狗管理器（**Watchdog Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Write Page**
> 写入页面（**Write Page**）是指存储设备的最小可写单元（以字节为单位）。某些存储设备技术的访问必须考虑物理分段，因此并非所有存储设备技术都支持按字节访问。该术语定义了单次访问所需写入的最小大小。
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess · R23-11）

## X

**X.509**
> 定义公钥证书格式的 **ITU-T** 标准。
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager · R23-11）

**XML**
> 可扩展标记语言（**eXtensible Markup Language**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
