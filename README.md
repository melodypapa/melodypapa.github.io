# 米多papa的小屋

> A slow sparrow should make an early start. Learning a endless life.

本仓库是个人博客与知识库的源码，基于 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 构建，通过 GitHub Actions 自动部署到 GitHub Pages。

**在线访问：<https://melodypapa.github.io/>**

## 内容

站点内容以汽车嵌入式软件为主，也包括语言学习、教育等个人笔记：

| 栏目 | 简介 |
| --- | --- |
| [CP AUTOSAR](docs/autosar/index.md) | AUTOSAR CP 基础软件模块的原理与设计：通信、存储（NvM/Flash/EEP）、模式管理（EcuM/BswM）、I/O、系统服务、电源状态管理等 |
| [ARM Cortex](docs/cortex/index.md) | Cortex-M7 / Cortex-R52 处理器架构：MPU、异常模型、地址映射、多级缓存等 |
| [NXP](docs/nxp/index.md) | S32K5xx 与 S32G2 应用笔记：MPU 设计、双核休眠方案、ADC 功能安全、S32G2 各外设模块 |
| [EB Tresos](docs/eb_tresos/index.md) | EB tresos Studio 配置工具的使用与 Safety OS 集成 |
| [信息安全](docs/cybersecurity/index.md) | 汽车信息安全概念与术语 |
| [Automotive](docs/automotive/ethernet/frame_format/index.md) | 车载以太网帧格式 |
| [Linux](docs/linux/embedded_linux/index.md) | 嵌入式 Linux 概念 |
| [AUTOSAR 规范文档](docs/autosar_pdf/AUTOSAR_CP) | 内置的 AUTOSAR CP 规范 PDF（R22-11、R4.3.1），便于对照查阅 |
| [语言学习](docs/languages/index.md) | 德语（Berliner Platz）与法语课程笔记 |
| [教育](docs/education/index.md) | 数学与信息科学 |
| [博客](docs/blog/index.md) | 更新动态与技术随笔 |

## 本地开发

依赖：Python 3（pip）

```bash
# 安装依赖
pip install -r requirements.txt

# 本地预览（默认 http://127.0.0.1:8000）
mkdocs serve
```

构建站点到 `site/` 目录：

```bash
mkdocs build --strict
```

## MkDocs 使用

### 新增页面

1. 在 `docs/` 对应栏目下创建目录与页面，例如 `docs/nxp/s32g2/lpuart/index.md`
2. 在 `mkdocs.yml` 的 `nav` 中注册该页面——存在未收录的 Markdown 文件时，`mkdocs build --strict` 会因告警而构建失败
3. 推送到 `master` 后由 Actions 自动构建发布

### 写作规范

- **每个页面有且只有一个一级标题（`#`）**，否则右侧目录（TOC）会显示异常
- 通过 front-matter 设置页面标题：

  ```yaml
  ---
  title: 页面标题
  ---
  ```

### 可用的 Markdown 扩展

以下扩展已在 `mkdocs.yml` 的 `markdown_extensions` 中启用，写作时可直接使用：

- **提示框（admonition）**：支持 `note` / `tip` / `warning` / `danger` 等类型

  ```markdown
  !!! note "提示"
      这是一个 admonition 提示框。
  ```

- **Mermaid 图表**：直接书写 `mermaid` 代码块即可渲染（通过 CDN 引入 mermaid 10.9.1，配合 `docs/javascripts/mermaid-init.js` 初始化）

  ````markdown
  ```mermaid
  graph LR
      A[启动] --> B[初始化]
      B --> C[运行]
  ```
  ````

- **表格** 与 **任务列表**（`- [x]` 已完成）
- **代码复制按钮**：所有代码块右上角自动启用
- **标题锚点**：各级标题自动生成永久链接，便于页面内跳转与引用

## 部署

推送到 `master` 分支后，[GitHub Actions](.github/workflows/ci.yml) 会自动执行 `mkdocs build --strict` 并通过 artifact 方式发布到 GitHub Pages，无需手动操作。

## 目录结构

```
.
├── docs/               # 站点内容（Markdown 与静态资源）
│   ├── autosar/        # AUTOSAR CP 模块笔记
│   ├── autosar_pdf/    # AUTOSAR 规范 PDF
│   ├── cortex/         # ARM Cortex 架构笔记
│   ├── nxp/            # NXP 芯片应用笔记
│   ├── blog/           # 博客文章
│   └── ...
├── overrides/          # Material 主题定制（如侧边栏常用链接）
├── mkdocs.yml          # 站点配置与导航
└── requirements.txt    # Python 依赖（mkdocs-material）
```

## 联系

- GitHub：[melodypapa](https://github.com/melodypapa)
- 邮箱：melodypapa@outlook.com

---

Copyright &copy; melodypapa
