---
title: "遗留指令助记符（Legacy Instruction Mnemonics）"
---

本附录描述 **Armv7-M Thumb** 指令集中的**遗留助记符**（**legacy mnemonics**）及其**统一汇编语言**（**Unified Assembler Language**，**UAL**）等价形式。本章包含以下小节：

* 第 D2-770 页的 **Thumb 指令助记符**。
* 第 D2-773 页的 **UAL 之前的伪指令 NOP**。
* 第 D2-774 页的 **UAL 之前的浮点指令助记符**。

## 1. Thumb 指令助记符

下表给出 **Thumb-2** 技术引入之前 **Thumb** 指令所用的 **UAL 之前**（**pre-UAL**）汇编语法，以及每条指令的等价 **UAL** 语法。该表可用于把能正确汇编的 **UAL 之前 Thumb** 汇编代码转换为 **UAL** 汇编代码。

本表不适用于从 **UAL** 汇编代码反向转换为 **UAL 之前的 Thumb** 汇编代码。

本表中的等价 **UAL** 语法使用三操作数形式，只有一处例外：该处必须使用二操作数形式，以保证 **UAL** 汇编器选择的指令编码与 **UAL 之前的 Thumb** 汇编器选择的一致。

表 D2-1 UAL 之前的汇编语法：

| UAL 之前的 Thumb 语法 | 等价的 UAL 语法 | 备注 |
| --- | --- | --- |
| `ADC <Rd>, <Rm>` | `ADCS <Rd>, <Rd>, <Rm>` | - |
| `ADD <Rd>, <Rn>, #<imm>` | `ADDS <Rd>, <Rn>, #<imm>` | - |
| `ADD <Rd>, #<imm>` | `ADDS <Rd>, #<imm>` | - |
| `ADD <Rd>, <Rn>, <Rm>` | `ADDS <Rd>, <Rn>, <Rm>` | - |
| `ADD <Rd>, SP` | `ADD <Rd>, SP, <Rd>` | - |
| `ADD <Rd>, <Rm>` | `ADDS <Rd>, <Rm>` | `<Rd>` 与 `<Rm>` 均为 R0-R7。 |
| `ADD <Rd>, <Rm>` | `ADD <Rd>, <Rd>, <Rm>` | 否则。`<Rm>` 不能为 SP。 |
| `ADD <Rd>, PC, #<imm>` | `ADD <Rd>, PC, #<imm>` | 尽可能优先使用 `ADR` 形式。 |
| `ADR <Rd>, <label>` | `ADR <Rd>, <label>` | 尽可能优先使用 `ADR` 形式。 |
| `ADD <Rd>, SP, #<imm>` | `ADD <Rd>, SP, #<imm>` | - |
| `ADD SP, #<imm>` | `ADD SP, SP, #<imm>` | - |
| `AND <Rd>, <Rm>` | `ANDS <Rd>, <Rd>, <Rm>` | - |
| `ASR <Rd>, <Rm>, #<imm>` | `ASRS <Rd>, <Rm>, #<imm>` | - |
| `ASR <Rd>, <Rs>` | `ASRS <Rd>, <Rd>, <Rs>` | - |
| `B<cond> <label>` | `B<cond> <label>` | - |
| `B <label>` | `B <label>` | - |
| `BIC <Rd>, <Rm>` | `BICS <Rd>, <Rd>, <Rm>` | - |
| `BKPT <imm>` | `BKPT <imm>` | - |
| `BL <label>` | `BL <label>` | - |
| `BLX <Rm>` | `BLX <Rm>` | `<Rm>` 可以为高寄存器。 |
| `BX <Rm>` | `BX <Rm>` | `<Rm>` 可以为高寄存器。 |
| `CMN <Rn>, <Rm>` | `CMN <Rn>, <Rm>` | - |
| `CMP <Rn>, #<imm>` | `CMP <Rn>, #<imm>` | - |
| `CMP <Rn>, <Rm>` | `CMP <Rn>, <Rm>` | `<Rd>` 与 `<Rm>` 可以为高寄存器。 |
| `CPS<effect> <iflags>` | `CPS<effect> <iflags>` | - |
| `CPY <Rd>, <Rm>` | `MOV <Rd>, <Rm>` | - |
| `EOR <Rd>, <Rm>` | `EORS <Rd>, <Rd>, <Rm>` | - |
| `LDMIA <Rn>!, <registers>` | `LDMIA <Rn>, <registers>` | `<Rn>` 出现在 `<registers>` 中。 |
| `LDMIA <Rn>!, <registers>` | `LDMIA <Rn>!, <registers>` | 否则。 |
| `LDR <Rd>, [<Rn>, #<imm>]` | `LDR <Rd>, [<Rn>, #<imm>]` | `<Rn>` 可以为 SP。 |
| `LDR <Rd>, [<Rn>, <Rm>]` | `LDR <Rd>, [<Rn>, <Rm>]` | - |
| `LDR <Rd>, [PC, #<imm>]` | `LDR <Rd>, [PC, #<imm>]` | 尽可能优先使用 `<label>` 形式。 |
| `LDR <Rd>, <label>` | `LDR <Rd>, <label>` | 尽可能优先使用 `<label>` 形式。 |
| `LDRB <Rd>, [<Rn>, #<imm>]` | `LDRB <Rd>, [<Rn>, #<imm>]` | - |
| `LDRB <Rd>, [<Rn>, <Rm>]` | `LDRB <Rd>, [<Rn>, <Rm>]` | - |
| `LDRH <Rd>, [<Rn>, #<imm>]` | `LDRH <Rd>, [<Rn>, #<imm>]` | - |
| `LDRH <Rd>, [<Rn>, <Rm>]` | `LDRH <Rd>, [<Rn>, <Rm>]` | - |
| `LDRSB <Rd>, [<Rn>, <Rm>]` | `LDRSB <Rd>, [<Rn>, <Rm>]` | - |
| `LDRSH <Rd>, [<Rn>, <Rm>]` | `LDRSH <Rd>, [<Rn>, <Rm>]` | - |
| `LSL <Rd>, <Rm>, #<imm>` | `MOVS <Rd>, <Rm>` | `<imm>` == 0。 |
| `LSL <Rd>, <Rm>, #<imm>` | `LSLS <Rd>, <Rm>, #<imm>` | 否则。 |
| `LSL <Rd>, <Rs>` | `LSLS <Rd>, <Rd>, <Rs>` | - |
| `LSR <Rd>, <Rm>, #<imm>` | `LSRS <Rd>, <Rm>, #<imm>` | - |
| `LSR <Rd>, <Rs>` | `LSRS <Rd>, <Rd>, <Rs>` | - |
| `MOV <Rd>, #<imm>` | `MOVS <Rd>, #<imm>` | - |
| `MOV <Rd>, <Rm>` | `ADDS <Rd>, <Rm>, #0` | `<Rd>` 与 `<Rm>` 均为 R0-R7。 |
| `MOV <Rd>, <Rm>` | `MOV <Rd>, <Rm>` | 否则。 |
| `MUL <Rd>, <Rm>` | `MULS <Rd>, <Rm>, <Rd>` | - |
| `MVN <Rd>, <Rm>` | `MVNS <Rd>, <Rm>` | - |
| `NEG <Rd>, <Rm>` | `RSBS <Rd>, <Rm>, #0` | - |
| `ORR <Rd>, <Rm>` | `ORRS <Rd>, <Rd>, <Rm>` | - |
| `POP <registers>` | `POP <registers>` | `<registers>` 可以包含 PC。 |
| `PUSH <registers>` | `PUSH <registers>` | `<registers>` 可以包含 LR。 |
| `REV <Rd>, <Rn>` | `REV <Rd>, <Rn>` | - |
| `REV16 <Rd>, <Rn>` | `REV16 <Rd>, <Rn>` | - |
| `REVSH <Rd>, <Rn>` | `REVSH <Rd>, <Rn>` | - |
| `ROR <Rd>, <Rs>` | `RORS <Rd>, <Rd>, <Rs>` | - |
| `SBC <Rd>, <Rm>` | `SBCS <Rd>, <Rd>, <Rm>` | - |
| `STMIA <Rn>!, <registers>` | `STMIA <Rn>!, <registers>` | - |
| `STR <Rd>, [<Rn>, #<imm>]` | `STR <Rd>, [<Rn>, #<imm>]` | `<Rn>` 可以为 SP。 |
| `STR <Rd>, [<Rn>, <Rm>]` | `STR <Rd>, [<Rn>, <Rm>]` | - |
| `STRB <Rd>, [<Rn>, #<imm>]` | `STRB <Rd>, [<Rn>, #<imm>]` | - |
| `STRB <Rd>, [<Rn>, <Rm>]` | `STRB <Rd>, [<Rn>, <Rm>]` | - |
| `STRH <Rd>, [<Rn>, #<imm>]` | `STRH <Rd>, [<Rn>, #<imm>]` | - |
| `STRH <Rd>, [<Rn>, <Rm>]` | `STRH <Rd>, [<Rn>, <Rm>]` | - |
| `SUB <Rd>, <Rn>, #<imm>` | `SUBS <Rd>, <Rn>, #<imm>` | - |
| `SUB <Rd>, #<imm>` | `SUBS <Rd>, #<imm>` | - |
| `SUB <Rd>, <Rn>, <Rm>` | `SUBS <Rd>, <Rn>, <Rm>` | - |
| `SUB SP, #<imm>` | `SUB SP, SP, #<imm>` | - |
| `SWI <imm>` | `SVC <imm>` | - |
| `SXTB <Rd>, <Rm>` | `SXTB <Rd>, <Rm>` | - |
| `SXTH <Rd>, <Rm>` | `SXTH <Rd>, <Rm>` | - |
| `TST <Rn>, <Rm>` | `TST <Rn>, <Rm>` | - |
| `UXTB <Rd>, <Rm>` | `UXTB <Rd>, <Rm>` | - |
| `UXTH <Rd>, <Rm>` | `UXTH <Rd>, <Rm>` | - |

## 2. UAL 之前的伪指令 NOP

在 **UAL 之前**的汇编代码中，`NOP` 是一条伪指令，在 **Thumb** 代码中等价于 `MOV R8,R8`。

把 `NOP` 助记符按 **UAL** 汇编不会改变代码的功能，但会改变：

* 所选择的指令编码。
* 所生成的二进制代码能成功执行的体系结构变体，因为 **Thumb** 版本的 `NOP` 指令是在 **Armv6T2** 中引入的。

为避免 **Thumb** 代码发生变化，应在按 **UAL** 汇编之前，把汇编源文件中的 `NOP` 替换为 `MOV R8,R8`。

**注意：** **UAL 之前**的伪指令在 **Arm** 代码中不同，那里它等价于 `MOV R0,R0`。

## 3. UAL 之前的浮点指令助记符

表 D2-2 列出 **UAL 之前**浮点指令助记符的 **UAL** 等价形式。

表 D2-2 UAL 之前浮点指令助记符的 UAL 等价形式：

| UAL 之前的汇编助记符 | UAL 等价形式 | 参见 |
| --- | --- | --- |
| `FABSD`、`FABSS` | `VABS` | 第 A7-455 页的 `VABS` |
| `FADDD`、`FADDS` | `VADD` | 第 A7-456 页的 `VADD` |
| `FCMP`、`FCMPE`、`FCMPEZ`、`FCMPZ` | `VCMP{E}` | 第 A7-457 页的 `VCMP`、`VCMPE` |
| `FCONSTD`、`FCONSTS` | `VMOV` | 第 A7-478 页的 `VMOV`（立即数） |
| `FCPYD`、`FCPYS` | `VMOV` | 第 A7-479 页的 `VMOV`（寄存器） |
| `FDIVD`、`FDIVS` | `VDIV` | 第 A7-468 页的 `VDIV` |
| `FLDD` | `VLDR` | 第 A7-473 页的 `VLDR` |
| `FLDMD`、`FLDMS` | `VLDM`、`VPOP` | 第 A7-471 页的 `VLDM`、第 A7-491 页的 `VPOP` |
| `FLDMX` | `FLDMX` | 第 D2-775 页的 `FLDMX`、`FSTMX` |
| `FLDS` | `VLDR` | 第 A7-473 页的 `VLDR` |
| `FMACD`、`FMACS` | `VMLA` | 第 A7-476 页的 `VMLA`、`VMLS` |
| `FMDHR`、`FMDLR` | `VMOV` | 第 A7-480 页的 `VMOV`（Arm 内核寄存器到标量） |
| `FMDRR` | `VMOV` | 第 A7-484 页的 `VMOV`（两个 Arm 内核寄存器与双字寄存器之间） |
| `FMRDH`、`FMRDL` | `VMOV` | 第 A7-481 页的 `VMOV`（标量到 Arm 内核寄存器） |
| `FMRRD` | `VMOV` | 第 A7-484 页的 `VMOV`（两个 Arm 内核寄存器与双字寄存器之间） |
| `FMRRS` | `VMOV` | 第 A7-483 页的 `VMOV`（两个 Arm 内核寄存器与两个单精度寄存器之间） |
| `FMRS` | `VMOV` | 第 A7-482 页的 `VMOV`（Arm 内核寄存器与单精度寄存器之间） |
| `FMRX` | `VMRS` | 第 A7-485 页的 `VMRS` |
| `FMSCD`、`FMSCS` | `VNMLS` | 第 A7-489 页的 `VNMLA`、`VNMLS`、`VNMUL` |
| `FMSR` | `VMOV` | 第 A7-482 页的 `VMOV`（Arm 内核寄存器与单精度寄存器之间） |
| `FMSRR` | `VMOV` | 第 A7-483 页的 `VMOV`（两个 Arm 内核寄存器与两个单精度寄存器之间） |
| `FMSTAT` | `VMRS` | 第 A7-485 页的 `VMRS` |
| `FMULD`、`FMULS` | `VMUL` | 第 A7-487 页的 `VMUL` |
| `FMXR` | `VMSR` | 第 A7-486 页的 `VMSR` |
| `FNEGD`、`FNEGS` | `VNEG` | 第 A7-488 页的 `VNEG` |
| `FNMACD`、`FNMACS` | `VMLS` | 第 A7-476 页的 `VMLA`、`VMLS` |
| `FNMSCD`、`FNMSCS` | `VNMLA` | 第 A7-489 页的 `VNMLA`、`VNMLS`、`VNMUL` |
| `FNMULD`、`FNMULS` | `VNMUL` | 第 A7-489 页的 `VNMLA`、`VNMLS`、`VNMUL` |
| `FSHTOD`、`FSHTOS` | `VCVT` | 第 A7-463 页的 `VCVT`（浮点与定点之间） |
| `FSITOD`、`FSITOS` | `VCVT` | 第 A7-461 页的 `VCVT`、`VCVTR`（浮点与整数之间） |
| `FSLTOD`、`FSLTOS` | `VCVT` | 第 A7-463 页的 `VCVT`（浮点与定点之间） |
| `FSQRTD`、`FSQRTS` | `VSQRT` | 第 A7-498 页的 `VSQRT` |
| `FSTD` | `VSTR` | 第 A7-501 页的 `VSTR` |
| `FSTMD`、`FSTMS` | `VSTM`、`VPUSH` | 第 A7-499 页的 `VSTM`、第 A7-492 页的 `VPUSH` |
| `FSTMX` | `FSTMX` | 第 D2-775 页的 `FLDMX`、`FSTMX` |
| `FSTS` | `VSTR` | 第 A7-501 页的 `VSTR` |
| `FSUBD`、`FSUBS` | `VSUB` | 第 A7-503 页的 `VSUB` |
| `FTOSHD`、`FTOSHS` | `VCVT` | 第 A7-463 页的 `VCVT`（浮点与定点之间） |
| `FTOSI{Z}D`、`FTOSI{Z}S` | `VCVT{R}` | 第 A7-461 页的 `VCVT`、`VCVTR`（浮点与整数之间） |
| `FTOSL`、`FTOUH` | `VCVT` | 第 A7-463 页的 `VCVT`（浮点与定点之间） |
| `FTOUI{Z}D`、`FTOUI{Z}S` | `VCVT{R}` | 第 A7-461 页的 `VCVT`、`VCVTR`（浮点与整数之间） |
| `FTOULD`、`FTOULS`、`FUHTOD`、`FUHTOS` | `VCVT` | 第 A7-463 页的 `VCVT`（浮点与定点之间） |
| `FUITOD`、`FUITOS` | `VCVT` | 第 A7-461 页的 `VCVT`、`VCVTR`（浮点与整数之间） |
| `FULTOD`、`FULTOS` | `VCVT` | 第 A7-463 页的 `VCVT`（浮点与定点之间） |

### 3.1. FLDMX, FSTMX

`VLDM`、`VPOP`、`VPUSH` 与 `VSTM` 指令的编码 T1 含有一个 imm8 字段，其值设为要传送的双字寄存器数量的两倍。Arm 反对使用 imm8 取奇数值的这些编码，它们也没有 **UAL** 语法。

**UAL 之前**的助记符 `FLDMX` 与 `FSTMX` 生成的指令分别与 `FLDMD` 相同，只是 imm8 等于双字寄存器数量的两倍加一：

* `FLDMD` 生成 `VLDM.64` 或 `VPOP.64`。
* `FSTMD` 生成 `VSTM.64` 或 `VPUSH.64`。

除用于反汇编以及重新汇编反汇编出的代码之外，Arm 反对使用 `FLDMX` 与 `FSTMX`。
