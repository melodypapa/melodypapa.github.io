<section id="title">Cortex-M7 指令集</section>

# 1. 指令集总结

处理器实现了一个版本的 **Thumb** 指令集。 表 **3-1** 列出了支持的指令。

| Mnemonic      | Operands                    | Brief description                                                   | Flags   | Page                 |
| ------------- | --------------------------- | ------------------------------------------------------------------- | ------- | -------------------- |
| ADC, ADCS     | {Rd,} Rn, Op2               | Add with Carry                                                      | N,Z,C,V | page 3-44            |
| ADD, ADDS     | {Rd,} Rn, Op2               | Add                                                                 | N,Z,C,V | page 3-44            |
| ADD, ADDW     | {Rd,} Rn, #imm12            | Add                                                                 | -       | page 3-44            |
| ADR           | Rd, label                   | Address to Register                                                 | -       | page 3-25            |
| AND, ANDS     | {Rd,} Rn, Op2               | Logical AND                                                         | N,Z,C   | page 3-47            |
| ASR, ASRS     | Rd, Rm, <Rs\|#n>            | Arithmetic Shift Right                                              | N,Z,C   | page 3-49            |
| B             | label                       | Branch                                                              | -       | page 3-128           |
| BFC           | Rd, #lsb, #width            | Bit Field Clear                                                     | -       | page 3-124           |
| BFI           | Rd, Rn, #lsb, #width        | Bit Field Insert                                                    | -       | page 3-124           |
| BIC, BICS     | {Rd,} Rn, Op2               | Bit Clear                                                           | N,Z,C   | page 3-47            |
| BKPT          | #imm8                       | Breakpoint                                                          | -       | page 3-173           |
| BL            | label                       | Branch with Link                                                    | -       | page 3-128           |
| BLX           | Rm                          | Branch indirect with Link and Exchange                              | -       | page 3-128           |
| BX            | Rm                          | Branch indirect and Exchange                                        | -       | page 3-128           |
| CBNZ          | Rn, label                   | Compare and Branch if Non Zero                                      | -       | page 3-130           |
| CBZ           | Rn, label                   | Compare and Branch if Zero                                          | -       | page 3-130           |
| CLREX         | -                           | Clear Exclusive                                                     | -       | page 3-41            |
| CLZ           | Rd, Rm                      | Count Leading Zeros                                                 | -       | page 3-51            |
| CMN           | Rn, Op2                     | Compare Negative                                                    | N,Z,C,V | page 3-52            |
| CMP           | Rn, Op2                     | Compare                                                             | N,Z,C,V | page 3-52            |
| CPS           | Rd, Rn                      | Change Processor State                                              | -       | page 3-174           |
| CPY           | Rd, Rn                      | Copy                                                                | -       | page 3-17            |
| DMB           | {opt}                       | Data Memory Barrier                                                 | -       | page 3-175           |
| DSB           | {opt}                       | Data Synchronization Barrier                                        | -       | page 3-176           |
| EOR, EORS     | {Rd,} Rn, Op2               | Exclusive OR                                                        | N,Z,C   | page 3-47            |
| ISB           | {opt}                       | Instruction Synchronization Barrier                                 | -       | page 3-177           |
| IT            | -                           | If-Then condition block                                             | -       | page 3-131           |
| LDM           | Rn{!}, reglist              | Load Multiple registers                                             | -       | page 3-34            |
| LDMDB, LDMEA  | Rn{!}, reglist              | Load Multiple, decrement before                                     | -       | page 3-34            |
| LDMIA, LDMFD  | Rn{!}, reglist              | Load Multiple registers, increment after                            | -       | page 3-34            |
| LDR, LDRT     | Rt, [Rn, #offset]           | Load Register with word (immediate offset, unprivileged)            | -       | page 3-26, page 3-31 |
| LDRH, LDRHT   | Rt, [Rn, #offset]           | Load Register with Halfword (immediate offset, unprivileged)        | -       | page 3-26, page 3-31 |
| LDRSH, LDRSHT | Rt, [Rn, #offset]           | Load Register with Signed Halfword (immediate offset, unprivileged) | -       | page 3-26, page 3-31 |
| LDRB, LDRBT   | Rt, [Rn, #offset]           | Load Register with byte (immediate offset, unprivileged)            | -       | page 3-26, page 3-31 |
| LDRSB, LDRSBT | Rt, [Rn, #offset]           | Load Register with Signed Byte (immediate offset, unprivileged)     | -       | page 3-26, page 3-31 |
| LDR           | Rt, [Rn, Rm {, LSL #shift}] | Load Register with word (register offset)                           | -       | page 3-29            |
| LDRH          | Rt, [Rn, Rm {, LSL #shift}] | Load Register with Halfword (register offset)                       | -       | page 3-29            |
| LDRSH         | Rt, [Rn, Rm {, LSL #shift}] | Load Register with Signed Halfword (register offset)                | -       | page 3-29            |
| LDRB          | Rt, [Rn, Rm {, LSL #shift}] | Load Register with Byte (register offset)                           | -       | page 3-29            |
| LDRSB         | Rt, [Rn, Rm {, LSL #shift}] | Load Register with Signed Byte (register offset)                    | -       | page 3-29            |
| LDR           | Rt, label                   | Load Register with word (literal)                                   | -       | page 3-32            |
| LDRH          | Rt, label                   | Load Register with Halfword (literal)                               | -       | page 3-32            |
| LDRB          | Rt, label                   | Load Register with Byte (literal)                                   | -       | page 3-32            |
| LDRD          | Rt, Rt2, [Rn, #offset]      | Load Register Dual with two bytes (immediate offset)                | -       | page 3-26            |
| LDRD          | Rt, Rt2, label              | Load Register Dual with two bytes (PCrelative)                      | -       | page 3-32            |
| LDREX         | Rt, [Rn, #offset]           | Load Register Exclusive                                             | -       | page 3-39            |
| LDREXB        | Rt, [Rn]                    | Load Register Exclusive with Byte                                   | -       | page 3-39            |
| LDREXH        | Rt, [Rn]                    | Load Register Exclusive with Halfword                               | -       | page 3-39            |
| LDRSB         | Rt, label                   | Load Register with Signed Byte (PC-relative)                        | -       | page 3-32            |
| LDRSH         | Rt, label                   | Load Register with Signed Halfword (PC-relative)                    | -       | page 3-32            |
| LSL, LSLS     | Rd, Rm, <Rs\| #n>           | Logical Shift Left                                                  | N,Z,C   | page 3-49            |
| LSR, LSRS     | Rd, Rm, <Rs\| #n>           | Logical Shift Right                                                 | N,Z,C   | page 3-49            |
| MLA           | Rd, Rn, Rm, Ra              | Multiply with Accumulate, 32-bit result                             | N,Z     | page 3-83            |
| MLS           | Rd, Rn, Rm, Ra              | Multiply and Subtract, 32-bit result                                | -       | page 3-83            |
| MOV, MOVS     | Rd, Op2                     | Move                                                                | N,Z,C   | page 3-53            |
| MOV, MOVS     | Rd, Rm                      | Move (register)                                                     | N,Z     | page 3-53            |
| MOVT          | Rd, #imm16                  | Move Top                                                            | -       | page 3-55            |
| MOVW          | Rd, #imm16                  | Move 16-bit constant                                                | N,Z,C   | page 3-53            |
| MRS           | Rd, spec_reg                | Move from Special Register to general register                      | -       | page 3-178           |
| MSR           | spec_reg, Rn                | Move from general register to Special Register                      | -       | page 3-179           |
| MUL, MULS     | {Rd,} Rn, Rm                | Multiply, 32-bit result                                             | N,Z     | page 3-83            |
| MVN, MVNS     | Rd, Op2                     | Move NOT                                                            | N,Z,C   | page 3-53            |
| NEG           | {Rd,} Rm                    | Negate                                                              | -       | page 3-180           |
| NOP           | -                           | No Operation                                                        | -       | page 3-181           |
| ORN, ORNS     | {Rd,} Rn, Op2               | Logical OR NOT                                                      | N,Z,C   | page 3-47            |
| ORR, ORRS     | {Rd,} Rn, Op2               | Logical OR                                                          | N,Z,C   | page 3-47            |
| PKHTB, PKHBT  | {Rd,} Rn, Rm, {, Op2}       | Pack Halfword                                                       | -       | page 3-117           |
| PLD           | [Rn {, #offset}]            | Preload Data                                                        | -       | page 3-36            |
| POP           | reglist                     | Pop registers from stack                                            | -       | page 3-37            |
| PUSH          | reglist                     | Push registers onto stack                                           | -       | page 3-37            |
| QADD          | {Rd,} Rn, Rm                | Saturating double and Add                                           | Q       | page 3-107           |
| QADD16        | {Rd,} Rn, Rm                | Saturating Add 16                                                   | -       | page 3-107           |
| QADD8         | {Rd,} Rn, Rm                | Saturating Add 8                                                    | -       | page 3-107           |
| QASX          | {Rd,} Rn, Rm                | Saturating Add and Subtract with Exchange                           | -       | page 3-109           |
| QDADD         | {Rd,} Rn, Rm                | Saturating Double and Add                                           | Q       | page 3-111           |
| QDSUB         | {Rd,} Rn, Rm                | Saturating Double and Subtract                                      | Q       | page 3-111           |
| QSAX          | {Rd,} Rn, Rm                | Saturating Subtract and Add with Exchange                           | -       | page 3-109           |

QSUB {Rd,} Rn, Rm Saturating Subtract Q page 3-107
QSUB16 {Rd,} Rn, Rm Saturating Subtract 16 - page 3-107
QSUB8 {Rd,} Rn, Rm Saturating Subtract 8 - page 3-107
RBIT Rd, Rn Reverse Bits - page 3-56
REV Rd, Rn Reverse byte order in a word - page 3-56
REV16 Rd, Rn Reverse byte order in each halfword - page 3-56
REVSH Rd, Rn Reverse byte order in bottom halfword and
sign extend
- page 3-56
ROR, RORS Rd, Rm, <Rs|#n> Rotate Right N,Z,C page 3-49
RRX, RRXS Rd, Rm Rotate Right with Extend N,Z,C page 3-49
RSB, RSBS {Rd,} Rn, Op2 Reverse Subtract N,Z,C,V page 3-44
SADD16 {Rd,} Rn, Rm Signed Add 16 GE page 3-57
SADD8 {Rd,} Rn, Rm Signed Add 8 GE page 3-57
SASX {Rd,} Rn, Rm Signed Add and Subtract with Exchange GE page 3-65
SBC, SBCS {Rd,} Rn, Op2 Subtract with Carry N,Z,C,V page 3-44
SBFX Rd, Rn, #lsb, #width Signed Bit Field Extract - page 3-125
SDIV {Rd,} Rn, Rm Signed Divide - page 3-103
SEL {Rd,} Rn, Rm Select bytes GE page 3-77
SEV - Send Event - page 3-182
SHADD16 {Rd,} Rn, Rm Signed Halving Add 16 - page 3-59
SHADD8 {Rd,} Rn, Rm Signed Halving Add 8 - page 3-59
SHASX {Rd,} Rn, Rm Signed Halving Add and Subtract with
Exchange
- page 3-60
SHSAX {Rd,} Rn, Rm Signed Halving Subtract and Add with
Exchange
- page 3-60
SHSUB16 {Rd,} Rn, Rm Signed Halving Subtract 16 - page 3-62
SHSUB8 {Rd,} Rn, Rm Signed Halving Subtract 8 - page 3-62
SMLABB,
SMLABT, SMLATB,
SMLATT
Rd, Rn, Rm, Ra Signed Multiply Accumulate halfwords Q page 3-87
SMLAD, SMLADX Rd, Rn, Rm, Ra Signed Multiply Accumulate Dual Q page 3-89
SMLAL RdLo, RdHi, Rn, Rm Signed Multiply with Accumulate Long
(32 × 32 + 64), 64-bit result
- page 3-102
SMLALBB,
SMLALBT,
SMLALTB,
SMLALTT
RdLo, RdHi, Rn, Rm Signed Multiply Accumulate Long,
halfwords
- page 3-91