# Sync todo: dio_driver

文章：`docs/autosar/io/dio_driver/index.md` · 源：`AUTOSAR_CP_SWS_DIODriver.md`（R23-11 markdown，1321 行）·
生成：2026-10-24 · Issue：#52
（恢复 = 第一个仍为 `[ ]` 的条目；全部 `[x]` + TODO.md 行已更新 = 本次同步完成）

## 规则检查（STANDARD.md 展开）
- [x] 七章骨架齐全、编号 1–7 连续
- [x] 无禁止章节（源 ch.6 需求追踪 / ch.9 时序图 / ch.10 配置规范 / 附录 A 均合规省略）
- [x] front-matter title 为唯一 h1；正文无 `# `；无 `[SWS_Dio_xxxxx]` 需求编号残留
- [x] 微信页脚 `<section id="wechat">` + `<h4>`；nav 已注册
- [x] 第 3.1 节标题「输入文件和相关标准与规范」→「输入文件」
  - Note: STANDARD.md §1 canonical；站内 12 篇用「输入文件」，DIO 为变体
- [x] 第 4.2 节标题改为「汽车域的适用性」
  - Note: 先改为 STANDARD.md 原列的「适用于汽车领域」；用户评审 PR 时改定「汽车域的适用性」→ STANDARD.md §2 同步改定（commit 493ed12）
- [x] 第 7.5 节标题保持「调度函数」
  - Note: 曾按 STANDARD.md 原列改「周期函数」；用户定夺保留「调度函数」（站内 7 篇 vs BswM/CanNm 2 篇）→ STANDARD.md §2/§3 改定并记录决策（commit de11d8a）

## 内容差距（vs 源文档）
- [x] 第 1–7 章全部源内容已翻译 — 无缺口
  - Note: 15 条缩略语、2 份输入文件、2 个依赖模块、功能规格 7.1–7.7（含 MaskedWritePort/输出引脚回读）、5 个类型定义、9 个 API 函数（说明 + C 签名 + 需求正文）、开发错误表、回调/调度函数/期望接口
- [x] 第 6.7 节「安全事件」正文「无。」→「本模块不报告安全事件。」
  - Note: 源 *The module does not report security events.*，忠实译文
- [x] 第 7.4 节笔误「下层层」→「下层」

## 验证与收尾
- [x] Phase A 机械检查
  - Note: `mkdocs build --strict` exit 0、0 WARNING、0 ERROR；渲染后标题 `31-输入文件` / `42-汽车域的适用性` / `67-安全事件` / `75-调度函数` / `76-期望接口`；被改名标题无站内入链
- [x] Phase B 覆盖映射 + 忠实度抽查
  - Note: 源 §1–§8 全节 ↔ 文章 §1–§7 一一对应；禁章列为有意省略；SWS 为核对基准
- [x] 用户确认门（Step 7）
  - Note: 两项用词决策由用户在运行中给出（见决策记录）；确认门后修订生效
- [x] 更新 `docs/autosar/TODO.md` 行 + 最后更新
  - Note: DIO 行注记对齐完成；io 分区拆分；同类偏差（adc/icu/ocu/port/pwm 3.1·4.2，bswm/cannm/csm 调度函数）列入待办
- [x] 提交 + PR
  - Note: commit de11d8a + 493ed12 · PR #53 · Closes #52

## 决策记录（追加式）
- 2026-10-24 用户：*Scheduled functions* 定名「调度函数」（不改「周期函数」）→ STANDARD.md §2/§3、BswM/CanNm/Csm 待办
- 2026-10-24 用户：*Applicability to car domains* 定名「汽车域的适用性」（不用「适用于汽车领域」）→ STANDARD.md §2、9 篇变体文章待办

## 未纳入（有意跳过）
- 源 ch.6 Requirements Tracing / ch.9 Sequence diagrams / ch.10 Configuration specification / 附录 A — STANDARD.md 禁止章，合规省略
- port/pwm/adc/icu/ocu/bswm/cannm/csm 的同类用词偏差 — 非 DIO 范围，TODO.md 待办清单跟踪
