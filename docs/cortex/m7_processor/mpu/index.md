---
title: "内存保护单元（Memory Protection Unit）"
---



本章介绍内存保护单元（MPU）。

## 1. 关于 MPU

**MPU** 是用于内存保护的可选组件。处理器支持标准的 ARMv7 受保护内存系统架构（**Protected Memory System Architecture**）模型。MPU 完全支持：

* 八个或十六个保护区域。
* 具有递增区域优先级的重叠保护区域：

  * 15 为最高优先级（实现 16 个区域时）。
  * 7 为最高优先级（实现 8 个区域时）。
  * 0 为最低优先级。

* 访问权限。
* 向系统输出内存属性。

MPU 失配和权限违规会调用可编程优先级的 MemManage 故障处理程序。更多信息请参见 Arm®v7-M 架构参考手册。

可以使用 MPU 实现：

* 强制特权规则。
* 隔离进程。
* 强制访问规则。

## 2. MPU 功能描述

区域属性与大小寄存器 **MPU_RASR** 的访问权限位 **TEX**、**C**、**B**、**AP** 和 **XN** 控制对相应内存区域的访问。如果对没有所需权限的内存区域进行访问，则会引发 MemManage 故障。更多信息请参见 Arm®v7-M 架构参考手册。

## 3. MPU 编程模型

下表给出了 MPU 寄存器。这些寄存器在 Arm®v7-M 架构参考手册中描述。

**注意：** MPU 寄存器仅支持对齐的字访问。字节访问和半字访问为 UNPREDICTABLE。

| 地址 | 名称 | 类型 | 复位值 | 描述 |
| --- | --- | --- | --- | --- |
| 0xE000ED90 | MPU_TYPE | RO | 0x00000800ᵃ | MPU 类型寄存器 |
| 0xE000ED94 | MPU_CTRL | RW | 0x00000000 | MPU 控制寄存器 |
| 0xE000ED98 | MPU_RNR | RW | 未知 | MPU 区域编号寄存器 |
| 0xE000ED9C | MPU_RBAR | RW | 未知 | MPU 区域基址寄存器 |
| 0xE000EDA0 | MPU_RASR | RW | 未知 | MPU 区域属性与大小寄存器 |
| 0xE000EDA4 | MPU_RBAR_A1 | RW | 未知 | MPU 别名寄存器 |
| 0xE000EDA8 | MPU_RASR_A1 | RW | 未知 | MPU 别名寄存器 |
| 0xE000EDAC | MPU_RBAR_A2 | RW | 未知 | MPU 别名寄存器 |
| 0xE000EDB0 | MPU_RASR_A2 | RW | 未知 | MPU 别名寄存器 |
| 0xE000EDB4 | MPU_RBAR_A3 | RW | 未知 | MPU 别名寄存器 |
| 0xE000EDB8 | MPU_RASR_A3 | RW | 未知 | MPU 别名寄存器 |

a. 复位值取决于实现的区域数量：0x00000000 表示 0 个区域；0x00000800 表示 8 个区域；0x00001000 表示 16 个区域。
