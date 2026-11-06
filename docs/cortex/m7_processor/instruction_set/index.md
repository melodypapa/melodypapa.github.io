---
title: "Cortex-M7 指令集"
---




## 1. 指令集总结

处理器实现了一个版本的 **Thumb** 指令集。 表 **3-1** 列出了支持的指令。

| 助记符 | 操作数 | 简要说明 | 标志位 |
| --- | --- | --- | --- |
| ADC, ADCS | {Rd,} Rn, Op2 | 带进位加法 | N,Z,C,V |
| ADD, ADDS | {Rd,} Rn, Op2 | 加法 | N,Z,C,V |
| ADD, ADDW | {Rd,} Rn, #imm12 | 加法 | - |
| ADR | Rd, label | 将地址加载到寄存器 | - |
| AND, ANDS | {Rd,} Rn, Op2 | 按位与 | N,Z,C |
| ASR, ASRS | Rd, Rm, <Rs\|#n> | 算术右移 | N,Z,C |
| B | label | 分支 | - |
| BFC | Rd, #lsb, #width | 位段清零 | - |
| BFI | Rd, Rn, #lsb, #width | 位段插入 | - |
| BIC, BICS | {Rd,} Rn, Op2 | 位清零 | N,Z,C |
| BKPT | #imm8 | 断点 | - |
| BL | label | 带链接的分支 | - |
| BLX | Rm | 带链接与交换的间接分支 | - |
| BX | Rm | 间接分支与交换 | - |
| CBNZ | Rn, label | 比较结果非零则分支 | - |
| CBZ | Rn, label | 比较结果为零则分支 | - |
| CLREX | - | 清除独占 | - |
| CLZ | Rd, Rm | 统计前导零个数 | - |
| CMN | Rn, Op2 | 比较取负 | N,Z,C,V |
| CMP | Rn, Op2 | 比较 | N,Z,C,V |
| CPS | Rd, Rn | 更改处理器状态 | - |
| CPY | Rd, Rn | 复制 | - |
| DMB | {opt} | 数据内存屏障 | - |
| DSB | {opt} | 数据同步屏障 | - |
| EOR, EORS | {Rd,} Rn, Op2 | 按位异或 | N,Z,C |
| ISB | {opt} | 指令同步屏障 | - |
| IT | - | If-Then 条件块 | - |
| LDM | Rn{!}, reglist | 加载多个寄存器 | - |
| LDMDB, LDMEA | Rn{!}, reglist | 加载多个寄存器，先减 | - |
| LDMIA, LDMFD | Rn{!}, reglist | 加载多个寄存器，后增 | - |
| LDR, LDRT | Rt, [Rn, #offset] | 以字加载寄存器（立即数偏移，非特权） | - |
| LDRH, LDRHT | Rt, [Rn, #offset] | 以半字加载寄存器（立即数偏移，非特权） | - |
| LDRSH, LDRSHT | Rt, [Rn, #offset] | 以有符号半字加载寄存器（立即数偏移，非特权） | - |
| LDRB, LDRBT | Rt, [Rn, #offset] | 以字节加载寄存器（立即数偏移，非特权） | - |
| LDRSB, LDRSBT | Rt, [Rn, #offset] | 以有符号字节加载寄存器（立即数偏移，非特权） | - |
| LDR | Rt, [Rn, Rm {, LSL #shift}] | 以字加载寄存器（寄存器偏移） | - |
| LDRH | Rt, [Rn, Rm {, LSL #shift}] | 以半字加载寄存器（寄存器偏移） | - |
| LDRSH | Rt, [Rn, Rm {, LSL #shift}] | 以有符号半字加载寄存器（寄存器偏移） | - |
| LDRB | Rt, [Rn, Rm {, LSL #shift}] | 以字节加载寄存器（寄存器偏移） | - |
| LDRSB | Rt, [Rn, Rm {, LSL #shift}] | 以有符号字节加载寄存器（寄存器偏移） | - |
| LDR | Rt, label | 以字加载寄存器（字面量） | - |
| LDRH | Rt, label | 以半字加载寄存器（字面量） | - |
| LDRB | Rt, label | 以字节加载寄存器（字面量） | - |
| LDRD | Rt, Rt2, [Rn, #offset] | 以双字加载寄存器（立即数偏移） | - |
| LDRD | Rt, Rt2, label | 以双字加载寄存器（PC 相对） | - |
| LDREX | Rt, [Rn, #offset] | 独占加载寄存器 | - |
| LDREXB | Rt, [Rn] | 以字节独占加载寄存器 | - |
| LDREXH | Rt, [Rn] | 以半字独占加载寄存器 | - |
| LDRSB | Rt, label | 以有符号字节加载寄存器（PC 相对） | - |
| LDRSH | Rt, label | 以有符号半字加载寄存器（PC 相对） | - |
| LSL, LSLS | Rd, Rm, <Rs\| #n> | 逻辑左移 | N,Z,C |
| LSR, LSRS | Rd, Rm, <Rs\| #n> | 逻辑右移 | N,Z,C |
| MLA | Rd, Rn, Rm, Ra | 带累加的乘法，32 位结果 | N,Z |
| MLS | Rd, Rn, Rm, Ra | 乘减，32 位结果 | - |
| MOV, MOVS | Rd, Op2 | 移动 | N,Z,C |
| MOV, MOVS | Rd, Rm | 移动（寄存器） | N,Z |
| MOVT | Rd, #imm16 | 移动高半字 | - |
| MOVW | Rd, #imm16 | 移动 16 位常量 | N,Z,C |
| MRS | Rd, spec_reg | 从特殊寄存器移动到通用寄存器 | - |
| MSR | spec_reg, Rn | 从通用寄存器移动到特殊寄存器 | - |
| MUL, MULS | {Rd,} Rn, Rm | 乘法，32 位结果 | N,Z |
| MVN, MVNS | Rd, Op2 | 按位取反 | N,Z,C |
| NEG | {Rd,} Rm | 取负 | - |
| NOP | - | 空操作 | - |
| ORN, ORNS | {Rd,} Rn, Op2 | 按位或非 | N,Z,C |
| ORR, ORRS | {Rd,} Rn, Op2 | 按位或 | N,Z,C |
| PKHTB, PKHBT | {Rd,} Rn, Rm, {, Op2} | 打包半字 | - |
| PLD | [Rn {, #offset}] | 预加载数据 | - |
| POP | reglist | 从栈弹出寄存器 | - |
| PUSH | reglist | 将寄存器压入栈 | - |
| QADD | {Rd,} Rn, Rm | 饱和加法 | Q |
| QADD16 | {Rd,} Rn, Rm | 饱和 16 位加法 | - |
| QADD8 | {Rd,} Rn, Rm | 饱和 8 位加法 | - |
| QASX | {Rd,} Rn, Rm | 带交换的饱和加减 | - |
| QDADD | {Rd,} Rn, Rm | 饱和加倍加法 | Q |
| QDSUB | {Rd,} Rn, Rm | 饱和加倍减法 | Q |
| QSAX | {Rd,} Rn, Rm | 带交换的饱和减加 | - |
| QSUB | {Rd,} Rn, Rm | 饱和减法 | Q |
| QSUB16 | {Rd,} Rn, Rm | 饱和 16 位减法 | - |
| QSUB8 | {Rd,} Rn, Rm | 饱和 8 位减法 | - |
| RBIT | Rd, Rn | 位反转 | - |
| REV | Rd, Rn | 字内字节序反转 | - |
| REV16 | Rd, Rn | 各半字内字节序反转 | - |
| REVSH | Rd, Rn | 低半字字节序反转并符号扩展 | - |
| ROR, RORS | Rd, Rm, <Rs\|#n> | 循环右移 | N,Z,C |
| RRX, RRXS | Rd, Rm | 带扩展的循环右移 | N,Z,C |
| RSB, RSBS | {Rd,} Rn, Op2 | 逆向减法 | N,Z,C,V |
| SADD16 | {Rd,} Rn, Rm | 有符号 16 位加法 | GE |
| SADD8 | {Rd,} Rn, Rm | 有符号 8 位加法 | GE |
| SASX | {Rd,} Rn, Rm | 带交换的有符号加减 | GE |
| SBC, SBCS | {Rd,} Rn, Op2 | 带借位减法 | N,Z,C,V |
| SBFX | Rd, Rn, #lsb, #width | 有符号位段提取 | - |
| SDIV | {Rd,} Rn, Rm | 有符号除法 | - |
| SEL | {Rd,} Rn, Rm | 选择字节 | GE |
| SEV | - | 发送事件 | - |
| SHADD16 | {Rd,} Rn, Rm | 有符号减半 16 位加法 | - |
| SHADD8 | {Rd,} Rn, Rm | 有符号减半 8 位加法 | - |
| SHASX | {Rd,} Rn, Rm | 带交换的有符号减半加减 | - |
| SHSAX | {Rd,} Rn, Rm | 带交换的有符号减半减加 | - |
| SHSUB16 | {Rd,} Rn, Rm | 有符号减半 16 位减法 | - |
| SHSUB8 | {Rd,} Rn, Rm | 有符号减半 8 位减法 | - |
| SMLABB, SMLABT, SMLATB, SMLATT | Rd, Rn, Rm, Ra | 半字有符号乘累加 | Q |
| SMLAD, SMLADX | Rd, Rn, Rm, Ra | 双路有符号乘累加 | Q |
| SMLAL | RdLo, RdHi, Rn, Rm | 有符号长乘累加（32 × 32 + 64），64 位结果 | - |
| SMLALBB, SMLALBT, SMLALTB, SMLALTT | RdLo, RdHi, Rn, Rm | 半字有符号长乘累加 | - |
| SMLAWB, SMLAWT | Rd, Rn, Rm, Ra | 半字有符号乘累加（字 × 半字） | Q |
| SMLSD, SMLSDX | Rd, Rn, Rm, Ra | 双路有符号乘减 | Q |
| SMLSLD, SMLSLDX | RdLo, RdHi, Rn, Rm | 双路有符号长乘减 | - |
| SMMLA, SMMLAR | Rd, Rn, Rm, Ra | 有符号最高字乘累加 | - |
| SMMLS, SMMLSR | Rd, Rn, Rm, Ra | 有符号最高字乘减 | - |
| SMMUL, SMMULR | {Rd,} Rn, Rm | 有符号最高字乘法 | - |
| SMUAD, SMUADX | {Rd,} Rn, Rm | 双路有符号乘加 | Q |
| SMULBB, SMULBT, SMULTB, SMULTT | {Rd,} Rn, Rm | 半字有符号乘法 | - |
| SMULWB, SMULWT | {Rd,} Rn, Rm | 字 × 半字有符号乘法 | - |
| SMUSD, SMUSDX | {Rd,} Rn, Rm | 双路有符号乘减 | - |
| SSAT | Rd, #imm, Rn {, shift} | 有符号饱和 | C,Q |
| SSAT16 | Rd, #imm, Rn | 16 位有符号饱和 | Q |
| SSUB16 | {Rd,} Rn, Rm | 有符号 16 位减法 | GE |
| SSUB8 | {Rd,} Rn, Rm | 有符号 8 位减法 | GE |
| STM, STMIA, STMEA | Rn{!}, reglist | 存储多个寄存器 | - |
| STR, STRT | Rt, [Rn, #offset] | 以字存储寄存器（立即数偏移，非特权） | - |
| STRB, STRBT | Rt, [Rn, #offset] | 以字节存储寄存器（立即数偏移，非特权） | - |
| STRD | Rt, Rt2, [Rn, #offset] | 以双字存储寄存器（立即数偏移） | - |
| STRH | Rt, [Rn, #offset] | 以半字存储寄存器（立即数偏移） | - |
| SUB, SUBS | {Rd,} Rn, Op2 | 减法 | N,Z,C,V |
| SUB, SUBW | {Rd,} Rn, #imm12 | 减法 | - |
| SVC | #imm24 | 主管调用 | - |
| SXTB | Rd, Rm {, rotation} | 有符号字节扩展 | - |
| SXTB16 | {Rd,} Rm {, rotation} | 有符号字节 16 扩展 | - |
| SXTAB | {Rd,} Rn, Rm {, rotation} | 有符号字节扩展并相加 | - |
| SXTAB16 | {Rd,} Rn, Rm {, rotation} | 有符号字节 16 扩展并相加 | - |
| SXTAH | {Rd,} Rn, Rm {, rotation} | 有符号半字扩展并相加 | - |
| SXTH | Rd, Rm {, rotation} | 有符号半字扩展 | - |
| TBB | [Rn, Rm] | 表分支（字节） | - |
| TBH | [Rn, Rm, LSL #1] | 表分支（半字） | - |
| TEQ | Rn, Op2 | 测试等价 | N,Z,C |
| TST | Rn, Op2 | 测试 | N,Z,C |
| UADD16 | {Rd,} Rn, Rm | 无符号 16 位加法 | GE |
| UADD8 | {Rd,} Rn, Rm | 无符号 8 位加法 | GE |
| UASX | {Rd,} Rn, Rm | 带交换的无符号加减 | GE |
| UBFX | Rd, Rn, #lsb, #width | 无符号位段提取 | - |
| UDF | #imm16 | 永久未定义 | - |
| UDIV | {Rd,} Rn, Rm | 无符号除法 | - |
| UHADD16 | {Rd,} Rn, Rm | 无符号减半 16 位加法 | - |
| UHADD8 | {Rd,} Rn, Rm | 无符号减半 8 位加法 | - |
| UHASX | {Rd,} Rn, Rm | 带交换的无符号减半加减 | - |
| UHSAX | {Rd,} Rn, Rm | 带交换的无符号减半减加 | - |
| UHSUB16 | {Rd,} Rn, Rm | 无符号减半 16 位减法 | - |
| UHSUB8 | {Rd,} Rn, Rm | 无符号减半 8 位减法 | - |
| UMAAL | RdLo, RdHi, Rn, Rm | 无符号长乘累加累加 | - |
| UMLAL | RdLo, RdHi, Rn, Rm | 无符号长乘累加（32 × 32 + 64），64 位结果 | - |
| UMULL | RdLo, RdHi, Rn, Rm | 无符号长乘法，64 位结果 | - |
| UQADD16 | {Rd,} Rn, Rm | 无符号饱和 16 位加法 | - |
| UQADD8 | {Rd,} Rn, Rm | 无符号饱和 8 位加法 | - |
| UQASX | {Rd,} Rn, Rm | 带交换的无符号饱和加减 | - |
| UQSAX | {Rd,} Rn, Rm | 带交换的无符号饱和减加 | - |
| UQSUB16 | {Rd,} Rn, Rm | 无符号饱和 16 位减法 | - |
| UQSUB8 | {Rd,} Rn, Rm | 无符号饱和 8 位减法 | - |
| USAD8 | {Rd,} Rn, Rm | 无符号绝对差之和 | - |
| USADA8 | Rd, Rn, Rm, Ra | 无符号绝对差之和并累加 | - |
| USAT | Rd, #imm, Rn {, shift} | 无符号饱和 | C,Q |
| USAT16 | Rd, #imm, Rn | 16 位无符号饱和 | Q |
| USUB16 | {Rd,} Rn, Rm | 无符号 16 位减法 | GE |
| USUB8 | {Rd,} Rn, Rm | 无符号 8 位减法 | GE |
| UXTAB | {Rd,} Rn, Rm {, rotation} | 无符号字节扩展并相加 | - |
| UXTAB16 | {Rd,} Rn, Rm {, rotation} | 无符号字节 16 扩展并相加 | - |
| UXTAH | {Rd,} Rn, Rm {, rotation} | 无符号半字扩展并相加 | - |
| UXTB | Rd, Rm {, rotation} | 无符号字节扩展 | - |
| UXTB16 | {Rd,} Rm {, rotation} | 无符号字节 16 扩展 | - |
| UXTH | Rd, Rm {, rotation} | 无符号半字扩展 | - |
| VABS | Sd, Sm | 浮点绝对值 | - |
| VADD | Sd, Sn, Sm | 浮点加法 | - |
| VCMP, VCMPE | Sd, Sm | 浮点比较 | N,Z,C,V |
| VCVT, VCVTR | Sd, Sm | 浮点与整数转换 | - |
| VDIV | Sd, Sn, Sm | 浮点除法 | - |
| VFMA, VFMS | Sd, Sn, Sm | 浮点融合乘累加 | - |
| VLDM | Rn{!}, reglist | 浮点加载多个寄存器 | - |
| VLDR | Sd, [Rn, #offset] | 浮点加载寄存器 | - |
| VMLA, VMLS | Sd, Sn, Sm | 浮点乘累加 | - |
| VMOV | Sd, Sm | 浮点寄存器之间复制 | - |
| VMRS | Rt, FPSCR | 从浮点特殊寄存器移至内核寄存器 | N,Z,C,V |
| VMSR | FPSCR, Rt | 从内核寄存器移至浮点特殊寄存器 | - |
| VMUL | Sd, Sn, Sm | 浮点乘法 | - |
| VNEG | Sd, Sm | 浮点取负 | - |
| VNMLA, VNMLS, VNMUL | Sd, Sn, Sm | 浮点乘法并取负 | - |
| VPOP | reglist | 浮点出栈 | - |
| VPUSH | reglist | 浮点入栈 | - |
| VSQRT | Sd, Sm | 浮点平方根 | - |
| VSTM | Rn{!}, reglist | 浮点存储多个寄存器 | - |
| VSTR | Sd, [Rn, #offset] | 浮点存储寄存器 | - |
| VSUB | Sd, Sn, Sm | 浮点减法 | - |
| WFE | - | 等待事件 | - |
| WFI | - | 等待中断 | - |
| YIELD | - | 让出执行 | - |

![](arm_instruction_set_format.png)
