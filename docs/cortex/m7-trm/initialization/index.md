---
title: "初始化（Initialization）"
---



本章介绍如何初始化处理器，以及在使用处理器特性之前需要访问哪些寄存器来使能功能。

## 1. 关于初始化

在运行应用程序之前，可能需要：

* 向各种寄存器编程特定值，例如堆栈指针。
* 使能各种处理器特性，例如错误纠正。
* 向内存编程特定值，例如紧密耦合内存（**TCM**）。

其他初始化要求包括：

* 初始化 MPU。
* 初始化 FPU。
* 初始化并使能 L1 缓存。
* 禁用缓存错误检查与纠正。
* 使能 TCM。
* 预加载 TCM。
* 使能 TCM 重试与读-改-写。
* 使能 AHBP 接口。

根据 Cortex-M7 处理器中实现的功能，其中一些初始化要求是可选的。

**注意：** 处理器中的分支预测器始终使能，因此 **CCR.BP** 为 RAO/WI。有关配置与控制寄存器的更多信息，请参见 Arm®v7-M 架构参考手册。

### 1.1. 初始化 MPU

如果处理器实现了内存保护单元（**MPU**），则在使用之前必须在 **MPU_CTRL** 寄存器中使能 MPU。更多信息请参见 Arm®v7-M 架构参考手册。

在设置 MPU 时，如果 MPU 之前已经编程过，则应禁用未使用的区域，以防止之前的区域设置影响新的 MPU 设置。

### 1.2. 初始化 FPU

如果处理器实现了浮点单元（**FPU**），则必须在执行浮点指令之前使其使能。以下代码给出了使能该特性的示例。

```arm
CPACR   EQU 0xE000ED88

LDR r0, =CPACR
LDR r1, [R0]            ; 读取 CPACR
ORR r1, R1, #(0xF << 20) ; 将位 20-23 置位，使能 CP10 和 CP11 协处理器
STR r1, [R0]            ; 将修改后的值写回 CPACR
DSB
ISB
```

更多信息请参见 Arm®v7-M 架构参考手册。

**注意：** 浮点逻辑仅在带有 FPU 的 Cortex-M7 处理器中可用。

### 1.3. 初始化并使能 L1 缓存

如果处理器实现了 L1 数据缓存或指令缓存，则必须在软件使能之前将其无效化，否则可能出现 UNPREDICTABLE 行为。

#### 1.3.1. 无效化整个数据缓存

如果处理器包含数据缓存，软件可以使用以下代码示例无效化整个数据缓存。该操作通过遍历缓存的每一行，并使用私有外设总线（**PPB**）内存区域中的 **DCISW** 寄存器无效化该行来完成。缓存的路数和组数通过读取 **CCSIDR** 寄存器确定。

```arm
CCSIDR  EQU 0xE000ED80  ; 缓存大小 ID 寄存器地址
CSSELR  EQU 0xE000ED84  ; 缓存大小选择寄存器地址
DCISW   EQU 0xE000EF60  ; 缓存维护操作地址：按组/路清理并无效化数据缓存

MOV r0, #0x0            ; 选择要在 CCSIDR 中显示的缓存
LDR r11, =CSSELR        ; 0 = 选择 "L1 数据缓存"
STR r0, [r11]
DSB                     ; 确保对 CSSELR 的写已完成后再继续

LDR r11, =CCSIDR        ; 从 CCSIDR 读取
LDR r2, [r11]           ; 读取数据缓存大小信息
AND r1, r2, #0x7        ; r1 = 缓存行大小
ADD r7, r1, #0x4        ; r7 = 一个缓存行中的字数

UBFX r4, r2, #3, #10    ; r4 = 数据缓存的 "路数"-1
UBFX r2, r2, #13, #15   ; r2 = 数据缓存的 "组数"-1

CLZ r6, r4              ; 计算 "way" 在 DCISW 中的位偏移
LDR r11, =DCISW         ; 按组/路无效化缓存

inv_loop1               ; 对每个 "组"
MOV r1, r4              ; r1 = "路数"-1
LSLS r8, r2, r7         ; 将 "set" 值移位到 r8 的位 5

inv_loop2               ; 对每个 "路"
LSLS r3, r1, r6         ; 将 "way" 值移位到 r6 的位 30
ORRS r3, r3, r8         ; 合并 DCISW 所需的 "way" 和 "set" 值
STR r3, [r11]           ; 无效化 D-cache 行
SUBS r1, r1, #0x1       ; 递减 "way"
BGE inv_loop2           ; 结束 "路" 循环

SUBS r2, r2, #0x1       ; 递减 "set"
BGE inv_loop1           ; 结束 "组" 循环

DSB                     ; 无效化缓存后的数据同步屏障
ISB                     ; 无效化缓存后的指令同步屏障
```

#### 1.3.2. 无效化指令缓存

如果处理器包含指令缓存，可以使用以下代码示例无效化整个指令缓存。该操作通过向 PPB 内存区域中的 **ICIALLU** 寄存器写入来完成。

```arm
ICIALLU EQU 0xE000EF50

MOV r0, #0x0
LDR r11, =ICIALLU
STR r0, [r11]
DSB
ISB
```

#### 1.3.3. 使能数据缓存与指令缓存

在数据缓存和指令缓存初始化完成后，可以使用以下代码示例使其使能。该操作通过修改 PPB 内存区域中的 **CCR.IC** 和 **CCR.DC** 字段来完成。

```arm
CCR EQU 0xE000ED14

LDR r11, =CCR
LDR r0, [r11]
ORR r0, r0, #0x1:SHL:16 ; 置位 CCR.DC 字段
ORR r0, r0, #0x1:SHL:17 ; 置位 CCR.IC 字段
STR r0, [r11]
DSB
ISB
```

### 1.4. 禁用缓存错误检查与纠正

如果处理器包含缓存错误检查与纠正功能，则复位后该功能默认使能。可以使用以下代码示例禁用该功能。该操作通过修改 PPB 内存区域中的 **CM7_CACR.ECCDIS** 位来完成。

```arm
CM7_CACR EQU 0xE000EF9C

LDR r11, =CM7_CACR
LDR r0, [r11]
BFC r0, #0x1, #0x1   ; 清除 CM7_CACR.ECCDIS
STR r0, [r11]
DSB
ISB
```

软件修改 **CM7_CACR** 中的错误检查字段时必须格外小心。如果在缓存中包含数据时修改这些字段，缓存中的 ECC 信息可能不符合新设置，从而导致意外错误和数据丢失。因此，只能在两个缓存均关闭时修改 **CM7_CACR** 中的字段，并且修改后必须无效化整个缓存。

### 1.5. 使能 TCM

TCM 接口可以在复位时由系统通过处理器上的外部信号使能。如果复位时被禁用，则可以使用以下代码示例在软件中使能指令 TCM 和数据 TCM 接口：

```arm
CM7_ITCMCR EQU 0xE000EF90
CM7_DTCMCR EQU 0xE000EF94

LDR r11, =CM7_ITCMCR
LDR r0, [r11]
ORR r0, r0, #0x1     ; 置位 CM7_ITCMCR.EN 字段
STR r0, [r11]

LDR r11, =CM7_DTCMCR
LDR r0, [r11]
ORR r0, r0, #0x1     ; 置位 CM7_DTCMCR.EN 字段
STR r0, [r11]

DSB
ISB
```

### 1.6. 预加载 TCM

预加载 TCM 的方法包括：

#### 1.6.1. 使用启动代码进行内存复制

如果启动代码包含内存复制例程，从 ROM 读取数据并写入相应的 TCM，则必须使能 TCM 才能执行此操作。该启动代码必须从 TCM 区域之外的地址运行。

#### 1.6.2. 通过 DMA 写入 TCM

系统中的 DMA 设备从 ROM 读取数据，并通过 AHB 从接口写入 TCM。该方法可用于预加载 TCM，使处理器在复位后即可使用。

#### 1.6.3. 从复位开始使用 TCM

如果 TCM 接口配置为在复位时使能 TCM，且复位向量地址位于 TCM 内存区域内，则处理器从 TCM 启动。系统必须确保启动代码软件在执行开始前已存在于相应内存区域。这可以通过在复位前初始化内存来实现，也可以通过复位后使用 AHB 从接口传输数据并利用 **CPUWAIT** 输入信号来实现。断言该信号会阻止处理器在复位后取指或执行指令。**CPUWAIT** 信号去断言后，处理器以常规方式从复位向量地址开始取指。

**注意：** 在 **CPUWAIT** 去断言以启动处理器取指后，不得再次断言 **CPUWAIT**，除非处理器处于处理器复位或上电复位状态，即 nSYSRESET 或 nPORESET 已断言。处理器运行时断言 **CPUWAIT** 不会使处理器暂停。

### 1.7. 使能 TCM 重试与读-改-写

如果连接到处理器的 TCM 支持错误检测与纠正，则 TCM 接口必须配置为支持重试（retry）和读-改-写（**RMW**）特性。这些特性可以在复位时由系统通过处理器上的外部信号使能。如果复位时被禁用，则可以使用以下代码示例在软件中使能它们：

```arm
CM7_ITCMCR EQU 0xE000EF90
CM7_DTCMCR EQU 0xE000EF94

LDR r11, =CM7_ITCMCR
LDR r0, [r11]
ORR r0, r0, #0x1:SHL:1  ; 置位 CM7_ITCMCR.RMW 字段
ORR r0, r0, #0x1:SHL:2  ; 置位 CM7_ITCMCR.RETEN 字段
STR r0, [r11]

LDR r11, =CM7_DTCMCR
LDR r0, [r11]
ORR r0, r0, #0x1:SHL:1  ; 置位 CM7_DTCMCR.RMW 字段
ORR r0, r0, #0x1:SHL:2  ; 置位 CM7_DTCMCR.RETEN 字段
STR r0, [r11]

DSB
ISB
```

### 1.8. 使能 AHBP 接口

AHBP 接口可以在复位时由系统通过处理器上的外部信号使能。如果复位时被禁用，则可以使用以下代码示例在软件中使能 AHBP 接口：

```arm
CM7_AHBPCR EQU 0xE000EF98

LDR r11, =CM7_AHBPCR
LDR r0, [r11]
ORR r0, r0, #0x1     ; 置位 CM7_AHBPCR.EN 字段
STR r0, [r11]

DSB
ISB
```
