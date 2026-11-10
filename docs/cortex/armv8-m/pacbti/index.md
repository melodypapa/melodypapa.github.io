---
title: "指针认证与分支目标识别扩展（Pointer authentication and branch target identification Extension）"
---

本章规定可选的 **Armv8.1-M** 指针认证扩展与分支目标识别扩展规则。

## 1. 实现 PAC 与 BTI

**PACBTI** 扩展是 **OPTIONAL** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

若实现了 **PACBTI** 扩展，`ID_ISAR5.PACBTI` 将读出为非零值。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

**PAC** 与 **BTI** 特性可以针对每个安全状态与特权级别独立启用或禁用。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

### 1.1 指针认证

**PAC** 可按如下方式启用或禁用：

- `CONTROL.PAC_EN`，用于特权模式。
- `CONTROL.UPAC_EN`，用于非特权模式。

伪代码函数 `PACEnabled()` 描述了这一点。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

在特权模式下，`CONTROL.PAC_EN` 与 `CONTROL.UPAC_EN` 可以使用 `MSR` 与 `MRS` 指令访问。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

在非特权模式下，`CONTROL.UPAC_EN` 可以使用 `MRS` 指令读取。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

指针认证使用四个 128 位密钥：

| | Non-secure 状态 | Secure 状态 |
| --- | --- | --- |
| 特权 | `PAC_KEY_P_NS` | `PAC_KEY_P_S` |
| 非特权 | `PAC_KEY_U_NS` | `PAC_KEY_U_S` |

特权软件可以通过 `MSR` 与 `MRS` 指令访问这些密钥，其中：

- 寄存器值 `PAC_KEY_P_3`:`PAC_KEY_P_2`:`PAC_KEY_P_1`:`PAC_KEY_P_0` 拼接构成 `PAC_KEY_P`。
- 寄存器值 `PAC_KEY_U_3`:`PAC_KEY_U_2`:`PAC_KEY_U_1`:`PAC_KEY_U_0` 拼接构成 `PAC_KEY_U`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

对于**指针认证**指令，加密值的生成方式是 **IMPLEMENTATION DEFINED** 的，可以是以下之一：

- **QARMA** 算法的 5 轮变体，称为 **QARMA5**，如 *The QARMA Block Cipher Family*（Roberto Avanzi，Qualcomm Product Security Initiative）所述，此时 `ID_ISAR5.PACBTI` 的值为 `0b0001`。
- 一种 **IMPLEMENTATION DEFINED** 算法，此时 `ID_ISAR5.PACBTI` 的值为 `0b0010`。
- **QARMA** 算法的 3 轮变体，称为 **QARMA3**，如 *The QARMA Block Cipher Family*（Roberto Avanzi，Qualcomm Product Security Initiative）所述，此时 `ID_ISAR5.PACBTI` 的值为 `0b0100`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

当使用 **IMPLEMENTATION DEFINED** 算法时，适用以下规则：

- 该算法必须使用与 `ComputePAC()` 函数相同的输入参数。
- 在以下情况下，该算法必须给出相同的结果：
  - 传入该算法的参数（寄存器中的值与密钥）相同。
  - **PE** 执行于相同的安全与特权级别。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

允许 **IMPLEMENTATION DEFINED** 算法依据 **PE** 的安全与特权级别施加额外的密码学轮次。在不同安全与特权级别使用相同的输入参数与密钥值，可能产生不同的结果。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

以下函数描述了 **PACBTI** 扩展所支持的 **QARMA** 算法：

- `ComputePAC()`
- `PACCellInvShuffle()`
- `PACCellShuffle()`
- `PACInvSub()`
- `PACMult()`
- `PACSubQ3()`
- `PACSubQ5()`
- `RotCell()`
- `TweakCellInvRot()`
- `TweakCellRot()`
- `TweakInvShuffle()`
- `TweakShuffle()`

**Arm** 建议指针认证使用 **QARMA** 算法族。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

**PAC** 由 `PACBTI`、`PAC` 与 `PACG` 指令生成。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

伪代码函数 `ComputePAC()` 的输入参数为：

- 32 位指针/地址/数据的最高位零扩展到 64 位。
- 32 位**修饰符**（modifier）的最高位零扩展到 64 位。
- 128 位密码学密钥。

伪代码函数 `CreatePAC()` 描述了这一点。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

若 **PAC** 认证指令未能验证 **PAC**，则产生 **INVSTATE UsageFault**。若用于生成 **PAC** 的任一输入参数在验证 **PAC** 之前被修改，即三个通用寄存器之一或密码学密钥被修改，则会产生该错误。`AUT`、`BXAUT` 与 `AUTG` 指令认证 **PAC**。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

当 `PACEnabled()` 为 **FALSE** 时：

- **PAC** 生成指令不创建 **PAC**，也不更新任何寄存器。这些指令提供的其他功能不受影响。
- **PAC** 认证指令不验证 **PAC**，也不产生 **INVSTATE UsageFault**。这些指令提供的其他功能不受影响。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

密码学算法的输出是 32 位 **PAC**，因此不同的输入参数与密钥组合有可能产生完全相同的 **PAC**。这类**密码学碰撞**（cryptographic collision）无法被 **PAC** 认证指令检测到，也不会产生 **INVSTATE UsageFault**。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

**PACBTI** 扩展不区分特权 **Thread** 模式执行与 **Handler** 模式执行。例如，在 **Handler** 模式下完成认证的指针，可以在特权 **Thread** 模式下通过验证，而不产生 **INVSTATE UsageFault**。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

对于以下两对指令之间可以执行的指令数量，没有架构上的限制：

- 生成 **PAC** 的指令与验证 **PAC** 的指令之间。例如 `PAC` 与 `AUT`。
- 验证 **PAC** 的指令与返回指令之间。例如 `AUT` 与 `BX`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

**Arm** 建议：在指针通过认证之后与对该指针的任何后续引用之间，不应将未保护的指针保存到内存再恢复。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

下面是使用 **PAC** 的示例。

```arm
 1   LDR   R4, =func1             // Load function address.
 2   BLX   R4                      // Call function which is protected by PAC-AUT.
 3 ret1:
 4   MOV   R1, #AA                 // #AA value stored in R1 register.
 5   MOV   R2, #BB                 // #BB value stored in R2 register.
 6   LDR   R4, =func2
 7   BLX   R4                      // Call function which is protected by PAC-AUT.
 8 ret2:
 9   AUTG  R0, R1, R2              // Validate R0, R1, and R2 registers. If any of the
10                                 // values or the secret key have changed, then an
11                                 // INVSTATE UsageFault is generated.
12                                 // Not supported on legacy implementations.
13   ...
14 func1:
15   PAC   R12, LR, SP             // Computes the cryptographic code using LR, SP, and
16                                 // a secret key, then stores it in R12.
17                                 // This instruction works on legacy implementations.
18   PUSH  {R4-R6, R12, LR}        // Stack LR if it needs to be used before the AUT.
19   ...                           // Function body.
20   POP   {R4-R6, R12, LR}        // Restore the value of LR before authenticating.
21   AUT   R12, LR, SP             // Computes PAC using LR, SP, and a secret key, and
22                                 // then compares it against the value in R12.
23                                 // If the two values match then the LR is validated,
24                                 // otherwise an INVSTATE UsageFault is generated.
25                                 // This instruction works on legacy implementations.
26   BX    LR                      // Return to 'ret1'.
27 func2:
28   PAC   R12, LR, SP             // Calculate PAC for LR.
29   ...
30   PACG  R0, R1, R2              // Calculate PAC where desired value is in R1 (#AA).
31                                 // The modifier value is in R2 (#BB).
32                                 // Computed PAC is stored in R0 register.
33                                 // Not supported on legacy implementations.
34   ...                           // Function body.
35   BXAUT R12, LR, SP             // Validate LR and branch to LR ('ret2').
36                                 // Not supported on legacy implementations.
```

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

参见：

- 第 B3.4 节《专用 CONTROL 寄存器》（Special-purpose CONTROL register）。

### 1.2 分支目标识别

**BTI** 可按如下方式启用或禁用：

- `CONTROL.BTI_EN`，用于特权模式。
- `CONTROL.UBTI_EN`，用于非特权模式。

伪代码函数 `BTIEnabled()` 描述了这一点。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

在特权模式下，`CONTROL.BTI_EN` 与 `CONTROL.UBTI_EN` 可以使用 `MSR` 与 `MRS` 指令访问。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

在非特权模式下，`CONTROL.UBTI_EN` 可以使用 `MRS` 指令读取。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

当针对目标安全与特权状态启用了 **BTI** 时，任何将 `EPSR.B` 或 `LO_BRANCH_INFO.BTI` 置 1 的指令都称为 **BTI 置位指令**（**BTI setting** instruction）。`BTIEnabled()` 描述了这一点。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

任何将 `EPSR.B` 清 0 的指令都称为 **BTI 清零指令**（**BTI clearing** instruction）。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

异常进入时，`EPSR.B` 被自动压栈并清 0；异常返回时被恢复。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

`EPSR.B` 不作为 **FNC_RETURN** 栈帧的一部分被压栈并清 0。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

若针对目标安全状态与特权级别启用了 **BTI**，则在执行以下任一 **BTI 置位指令**时，`EPSR.B` 被置 1：

- `BLX`。
- `BLXNS`。
- 当持有分支地址的寄存器不是 **LR** 时：
  - `BX`。
  - `BXNS`。
- 当地址被加载到 **PC** 时：
  - `LDR`（寄存器）。
  - `LDR`（字面量）。
- 当地址被加载到 **PC** 且基地址寄存器不是 **SP**，或者基地址寄存器是 **SP** 但不发生 **SP** 回写时：
  - `LDR`（立即数）。
  - `LDM`、`LDMIA`、`LDMFD`。
  - `LDMDB`、`LDMEA`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

在执行以下任一 **BTI 置位指令**时，`LO_BRANCH_INFO.BTI` 位被置 1：

- `BFLX`。
- 当持有分支地址的寄存器不是 **LR** 时：
  - `BFX`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

当 **BTI 置位**的 **Branch Future** 分支被采用时，若以下全部条件成立，则 `EPSR.B` 被置 1：

- `BTIEnabled()` 为 **TRUE**。
- `LO_BRANCH_INFO.BTI` 被置 1。
- `LO_BRANCH_INFO.VALID` 被置 1。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

伪代码函数 `HandleLO()`、`GetInstrExecState()` 与 `InstructionAdvance()` 展示了 **BTI 置位**的 **Branch Future** 指令如何将 `EPSR.B` 置 1。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

任何不是 **BTI 置位**、且将 `LO_BRANCH_INFO.VALID` 位置 1 的指令，也必须将 `LO_BRANCH_INFO.BTI` 位清 0。例如 `LE` 与 `LETP` 指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

`BXAUT` 指令不是 **BTI 置位指令**，无论使用哪个寄存器作为分支目标。通过 `AUT` 或 `AUTG` 指令后接 `BX` 指令，可以实现带 **BTI 置位**的等价行为。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

`POP`（单寄存器）是 `LDR`（立即数）的别名，`POP`（多寄存器）是 `LDM`、`LDMIA`、`LDMFD` 的别名，它们都不是 **BTI 置位指令**。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

对于从 Non-secure 状态到 Secure 状态的转换，若 `SG` 指令被 **BTI 置位**分支作为目标，则由与该分支特权级别相关联的 `CONTROL_NS.BTI_EN` 与 `CONTROL_NS.UBTI_EN` 位决定 `EPSR.B` 是否被置位。

`SG` 指令是 **BTI 清零**的，因此若 `EPSR.B` 已置位，即使 **BTI** 未启用，它也会被清零。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI && S。

对于从 Secure 状态到 Non-secure 状态的转换，若该转换由 **BTI 置位**分支引起，例如 `BXNS`，则将检查与目标 Non-secure 状态特权级别相关联的 `CONTROL_NS.BTI_EN` 与 `CONTROL_NS.UBTI_EN` 位，以决定 `EPSR.B` 是否被置位。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI && S。

以下指令是 **BTI 清零**的：

- `BTI`。
- `SG`。
- `PACBTI`。

若 `EPSR.B` 已置位，即使 **BTI** 未启用，**BTI 清零指令**也会将其清 0。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

当 `EPSR.B` 置位时，下一条执行的指令必须是 **BTI 清零指令**或 `BKPT` 指令，否则会产生 **INVSTATE UsageFault**。

若下一条指令是 **BTI 清零指令**，则 `EPSR.B` 被清零。若下一条指令是 `BKPT` 指令，则 `EPSR.B` 不被清零并保持置位，且不产生 **INVSTATE UsageFault**。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

当需要 **PAC** 功能但不希望使用 `PACBTI` 创建**着陆垫**（landing pad）时，可以使用 `PAC` 或 `PACG` 指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。

下面是使用 **BTI** 的示例。

```arm
 1   // Current Security state is Non-secure
 2   LDR    R4, =testBti        // Load function address.
 3   LDR    R3, =ret1
 4   BLX    R4                  // BTI is enabled for Non-secure state, set EPSR.B.
 5 ret1:
 6   BTI                        // BTI clearing instruction.
 7   LDR    R4, =funcTestBti
 8   BLX    R4                  // Set EPSR.B.
 9 ret2:
10   LDR    R4, =nscBti
11   BLX    R4                  // Target address is in NSC region, set EPSR.B.
12 end:
13   ...
14   // Function in Non-secure state.
15 testBti:
16   BTI                        // BTI clearing instruction, valid entry point.
17   ...                        // LR not used for return, so PAC-AUT is not required.
18   ...                        // But using LR would be recommended in this scenario.
19   BX     R3                  // Branch to 'ret1'. LR is not used, so the branch
20                              // target must be a BTI clearing instruction.
21   // Function in Non-secure state.
22 funcTestBti:
23   PACBTI R12, LR, SP         // BTI clearing instruction, valid entry point.
24   ...                        // Stacking and unstacking R12, LR, and SP is safe
25                              // as any corruption will be detected by BXAUT.
26   BXAUT  R12, LR, SP         // Validate LR and return to 'ret2', address in LR.
27                              // The combined authenticate and branch instruction
28                              // is not backwards compatible with legacy software.
29   // Function in Non-secure state.
30 leafFunc:
31   BTI                        // Since BTI is enabled, a BTI clearing instruction
32   ...                        // is required.
33   BX     leafRet             // Does not set BTI, uses FNC_RETURN.
34   ...
35   // Secure and Non-secure callable region.
36 nscBti:
37   SG                         // Clear BTI, regardless of the Secure BTI settings.
38   B      secure              // Call Secure function.
39   ...
40   // Function in Secure state.
41 secure:
42   PAC    R12, LR, SP         // BTI clearing PAC is not required.
43   ...
44   LDR    R6, =leafFunc
45   BLXNS  R6                  // Call Non-secure function.
46                              // Instruction implicitly checks BTI settings for the
47                              // current privilege state in CONTROL_NS.
48 leafRet:
49   ...                        // BTI clearing instruction not required.
50   AUT    R12, LR, SP         // Validate LR.
51   ...                        // Stacking and unstacking LR and SP is not safe.
52   ...                        // Corruption of the registers will not be detected.
53   BXNS   LR                  // Branch to 'end'. Does not set BTI.
```

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PACBTI。
