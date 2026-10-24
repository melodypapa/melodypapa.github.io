# Sync todo: Group io — IO 分区收尾

基准：R23-11 · 生成：2026-10-24 · 队列序 = 行序
（恢复 = 第一个仍为 `[ ]` 的行；全部 `[x]` = 批次完成）
步骤图例：① 源定位+差距分析 · ② 就地翻译/补齐 · ③ Phase A 机械检查 · ④ Phase B 证据 · ⑤ 用户确认门 · ⑥ TODO.md 行+提交

## Queue

- [x] dio_driver（SWS_DIODriver · R23-11 markdown · 2026-10-24 完成（含重开缩略语改排）· commit de11d8a/493ed12/e21067f · PR #53）
  - Note: 2026-10-24 完成 3.1/4.2/6.7/7.4 对齐（commit de11d8a/493ed12 · PR #53）；同日缩略语普查发现 §2 仍为 GFM 表格（行集 15:15 一致）→ 按 STANDARD.md §1 改排引用块
  - Note: 重开 2026-10-24 缩略语章格式 → 已完成 commit e21067f；早期按篇 todo 审计 trail 见 [dio_driver.md](dio_driver.md)
  - Note: 2026-10-24 复核（用户点名 dio）：源 ch.1–8 逐章对照无缺口，缩略语 15:15 同序，`gen_glossary/gen_api_list --check` 均 exit 0 → 不改动、不开重开；新版本 R25-11 源结构有别（7.1.2 扩写、7.6.3 Transient Faults 撤除），如跟进发布版需另起重开行
  - [x] Step 1 — 源定位 + 差距分析（源 §2 表 15 行；文行集 15:15；缺口 = 格式）
  - [x] Step 2 — 就地翻译/补齐（表格 → 15 条粗体术语+引用块，源序；英文全称加粗；导语"下表"→"以下"）
  - [x] Step 3 — Phase A 机械检查（表格行 0、术语行 15、源序一致、无 h1/需求号、strict build 0 WARNING）
  - [x] Step 4 — Phase B 覆盖映射 + 忠实度（15↔15 同序；内容沿用已核对译文，仅版式）
  - [x] Step 5 — 用户确认门（用户指示"run skill to find and fix it"为本轮授权；证据随报告呈现，PR #53 可否决）
  - [x] Step 6 — TODO.md 行 + 提交/PR（commit e21067f · PR #53）
- [x] port_driver（SWS_PortDriver · R23-11 markdown · 2026-10-24 完成 · commit ee486aa · PR #53 / issue #54）
  - Note: 缩略语章现为 GFM 表格 → 引用块（行集 7:7 已核对一致）；4.2「对汽车域的适用性」→「汽车域的适用性」
  - Note: 2026-10-24 Step 1 差距分析（issue #54）：新增缺口 = §1 缺源 ch.1 映射表（Driver/Port Pin/Channel Group 对照，2 行 4 列）；§4.2 用词、§2 格式如前；§7.6.3「可配置接口」与 STANDARD.md「可配置的接口」冲突（站内 5 篇用前者）→ 待用户决策；其余 §3/§5/§6/§7 与源逐条一致
  - Note: 用户决策（2026-10-24）：7.6.3 保留「可配置接口」，STANDARD.md §2 与决策记录同步改为该词
  - [x] Step 1 — 源定位 + 差距分析
  - [x] Step 2 — 就地翻译/补齐（§1 映射表补译；§2 表格 → 7 条粗体术语+引用块、源序；§4.2 → 汽车域的适用性）
  - [x] Step 3 — Phase A 机械检查（strict build exit 0 / 0 WARNING；7 章骨架；ch.2 表格 0 行、术语 7 条；无 h1/需求号/禁止章；glossary 重新生成后 --check 0、api --check 0）
  - [x] Step 4 — Phase B 覆盖映射 + 忠实度（源 ch.1–8 逐节映射；ch.6/9/10/A 有意省略；§1 表 4 列 2 行逐字译；ch.2 7:7 同序）
  - [x] Step 5 — 用户确认门（2026-10-24 用户确认：Phase A/B 证据 + TODO.md 行；7.6.3 决策保留「可配置接口」）
  - [x] Step 6 — TODO.md 行 + 提交/PR（commit ee486aa · PR #53 · Closes #54）
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
