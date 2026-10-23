# Sync todo: Group io — IO 分区收尾

基准：R23-11 · 生成：2026-10-24 · 队列序 = 行序
（恢复 = 第一个仍为 `[ ]` 的行；全部 `[x]` = 批次完成）
步骤图例：① 源定位+差距分析 · ② 就地翻译/补齐 · ③ Phase A 机械检查 · ④ Phase B 证据 · ⑤ 用户确认门 · ⑥ TODO.md 行+提交

## Queue

- [x] dio_driver（SWS_DIODriver · R23-11 markdown · 2026-10-24 完成（含重开缩略语改排）· commit de11d8a/493ed12/e21067f · PR #53）
  - Note: 2026-10-24 完成 3.1/4.2/6.7/7.4 对齐（commit de11d8a/493ed12 · PR #53）；同日缩略语普查发现 §2 仍为 GFM 表格（行集 15:15 一致）→ 按 STANDARD.md §1 改排引用块
  - Note: 重开 2026-10-24 缩略语章格式 → 已完成 commit e21067f；早期按篇 todo 审计 trail 见 [dio_driver.md](dio_driver.md)
  - [x] Step 1 — 源定位 + 差距分析（源 §2 表 15 行；文行集 15:15；缺口 = 格式）
  - [x] Step 2 — 就地翻译/补齐（表格 → 15 条粗体术语+引用块，源序；英文全称加粗；导语"下表"→"以下"）
  - [x] Step 3 — Phase A 机械检查（表格行 0、术语行 15、源序一致、无 h1/需求号、strict build 0 WARNING）
  - [x] Step 4 — Phase B 覆盖映射 + 忠实度（15↔15 同序；内容沿用已核对译文，仅版式）
  - [x] Step 5 — 用户确认门（用户指示"run skill to find and fix it"为本轮授权；证据随报告呈现，PR #53 可否决）
  - [x] Step 6 — TODO.md 行 + 提交/PR（commit e21067f · PR #53）
- [ ] port_driver（SWS_PortDriver · R23-11 markdown · ✅ 仅余对齐）
  - Note: 缩略语章现为 GFM 表格 → 引用块（行集 7:7 已核对一致）；4.2「对汽车域的适用性」→「汽车域的适用性」
  - [ ] Step 1 — 源定位 + 差距分析
  - [ ] Step 2 — 就地翻译/补齐（缩略语改排 + 4.2 标题）
  - [ ] Step 3 — Phase A 机械检查（strict build 0 WARNING）
  - [ ] Step 4 — Phase B 覆盖映射 + 忠实度
  - [ ] Step 5 — 用户确认门
  - [ ] Step 6 — TODO.md 行 + 提交/PR（hash 记入本行）
- [ ] pwm_driver（SWS_PWMDriver · R23-11 markdown · ✅ 仅余对齐）
  - Note: 缩略语章表格 → 引用块（行集 13:13 已核对一致）；4.2「对汽车域的适用性」→「汽车域的适用性」
  - [ ] Step 1 — 源定位 + 差距分析
  - [ ] Step 2 — 就地翻译/补齐
  - [ ] Step 3 — Phase A 机械检查
  - [ ] Step 4 — Phase B 覆盖映射 + 忠实度
  - [ ] Step 5 — 用户确认门
  - [ ] Step 6 — TODO.md 行 + 提交/PR
- [ ] ocu_driver（SWS_OCUDriver · R23-11 markdown · ✅ 对齐 + 行集）
  - Note: 缩略语章表格 → 引用块，补回 MCU 行（源 14 行 → 文 13 条），清理"Term definition:"伪行；3.1「输入文档与相关标准和规范」→「输入文件」
  - [ ] Step 1 — 源定位 + 差距分析
  - [ ] Step 2 — 就地翻译/补齐
  - [ ] Step 3 — Phase A 机械检查
  - [ ] Step 4 — Phase B 覆盖映射 + 忠实度
  - [ ] Step 5 — 用户确认门
  - [ ] Step 6 — TODO.md 行 + 提交/PR
- [ ] icu_driver（SWS_ICUDriver · R23-11 markdown · 🔶 对齐）
  - Note: 删禁止章「时序图」；4.2「适用车型域」→「汽车域的适用性」；缩略语行集 12:12 已核对一致
  - [ ] Step 1 — 源定位 + 差距分析
  - [ ] Step 2 — 就地翻译/补齐
  - [ ] Step 3 — Phase A 机械检查
  - [ ] Step 4 — Phase B 覆盖映射 + 忠实度
  - [ ] Step 5 — 用户确认门
  - [ ] Step 6 — TODO.md 行 + 提交/PR
- [ ] adc_driver（SWS_ADCDriver · R23-11 markdown · ✅ 对齐 + 深补）
  - Note: 缩略语行集修复 — 源 18 行 → 文 16 条：补回 API/HW/SW、恢复 DEM→DET 源序、Conversion Mode 合回一条、术语行带别名（ADC Result Buffer (…,…))；4.2「适用车型域」→「汽车域的适用性」；深补（eval-2 实测缺口）：API 章约 78 个 SWS 需求正文未译、§3.1 陈旧 13 项清单换 R23-11 两项、§7.4.1 Background 未译
  - [ ] Step 1 — 源定位 + 差距分析
  - [ ] Step 2 — 就地翻译/补齐
  - [ ] Step 3 — Phase A 机械检查
  - [ ] Step 4 — Phase B 覆盖映射 + 忠实度
  - [ ] Step 5 — 用户确认门
  - [ ] Step 6 — TODO.md 行 + 提交/PR
- [ ] iohwab（SWS_IOHardwareAbstraction · R23-11 markdown · ⚠️ 补齐）
  - Note: 缺「约束和假设」章；删禁止章「时序图」；3.1 已是「输入文件」
  - [ ] Step 1 — 源定位 + 差距分析
  - [ ] Step 2 — 就地翻译/补齐
  - [ ] Step 3 — Phase A 机械检查
  - [ ] Step 4 — Phase B 覆盖映射 + 忠实度
  - [ ] Step 5 — 用户确认门
  - [ ] Step 6 — TODO.md 行 + 提交/PR

## Not queued（有意跳过）
- （无 — IO 分区 7 篇 SWS 全部入队）
