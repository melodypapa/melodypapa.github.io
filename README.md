# 米多papa的小屋

> A slow sparrow should make an early start. Learning a endless life.

This repository contains the source of my personal blog and knowledge base, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and deployed automatically to GitHub Pages via GitHub Actions.

**Visit online: <https://melodypapa.github.io/>**

## Content

The site focuses on automotive embedded software, along with personal notes on languages and education:

| Section | Description |
| --- | --- |
| [CP AUTOSAR](docs/autosar/index.md) | Principles and design of AUTOSAR CP basic software modules: communication, memory (NvM/Flash/EEP), mode management (EcuM/BswM), I/O, system services, power state management, and more |
| [ARM Cortex](docs/cortex/index.md) | Cortex-M7 / Cortex-R52 processor architecture: MPU, exception model, address map, multilevel cache, etc. |
| [NXP](docs/nxp/index.md) | Application notes for S32K5xx and S32G2: MPU design, dual-core sleep design, ADC functional safety, S32G2 peripheral modules |
| [EB Tresos](docs/eb_tresos/index.md) | Using the EB tresos Studio configuration tool and Safety OS integration |
| [Cybersecurity](docs/cybersecurity/index.md) | Automotive cybersecurity concepts and terminology |
| [Automotive](docs/automotive/ethernet/frame_format/index.md) | Automotive Ethernet frame format |
| [Linux](docs/linux/embedded_linux/index.md) | Embedded Linux concepts |
| [AUTOSAR Specifications](docs/autosar_pdf/AUTOSAR_CP) | Bundled AUTOSAR CP specification PDFs (R22-11, R4.3.1) for quick reference |
| [Languages](docs/languages/index.md) | German (Berliner Platz) and French course notes |
| [Education](docs/education/index.md) | Mathematics and computer science |
| [Blog](docs/blog/index.md) | Updates and technical essays |

## Local Development

Prerequisite: Python 3 (pip)

```bash
# Install dependencies
pip install -r requirements.txt

# Live preview (default http://127.0.0.1:8000)
mkdocs serve
```

Build the site into the `site/` directory:

```bash
mkdocs build --strict
```

## MkDocs Usage

### Adding a Page

1. Create a directory and page under the matching section in `docs/`, e.g. `docs/nxp/s32g2/lpuart/index.md`
2. Register the page in the `nav` section of `mkdocs.yml` — if any Markdown file is left unregistered, `mkdocs build --strict` fails with a warning
3. Push to `master` and Actions builds and publishes automatically

### Writing Conventions

- **Every page must have exactly one level-1 heading (`#`)**, otherwise the right-hand table of contents (TOC) breaks
- Set the page title via front matter:

  ```yaml
  ---
  title: Page Title
  ---
  ```

### Available Markdown Extensions

The following extensions are enabled under `markdown_extensions` in `mkdocs.yml` and can be used directly:

- **Admonitions**: supports `note` / `tip` / `warning` / `danger` and more

  ```markdown
  !!! note "Tip"
      This is an admonition block.
  ```

- **Mermaid diagrams**: simply write a `mermaid` code block (mermaid 10.9.1 loaded from CDN, initialized by `docs/javascripts/mermaid-init.js`)

  ````markdown
  ```mermaid
  graph LR
      A[Start] --> B[Init]
      B --> C[Run]
  ```
  ````

- **Tables** and **task lists** (`- [x]` done)
- **Copy-to-clipboard buttons**: enabled automatically on all code blocks
- **Heading anchors**: every heading gets a permanent link for in-page jumps and references

## Deployment

After pushing to `master`, [GitHub Actions](.github/workflows/ci.yml) automatically runs `mkdocs build --strict` and publishes the result to GitHub Pages — no manual steps required.

## Repository Layout

```
.
├── docs/               # Site content (Markdown and static assets)
│   ├── autosar/        # AUTOSAR CP module notes
│   ├── autosar_pdf/    # AUTOSAR specification PDFs
│   ├── cortex/         # ARM Cortex architecture notes
│   ├── nxp/            # NXP chip application notes
│   ├── blog/           # Blog posts
│   └── ...
├── overrides/          # Material theme customizations (e.g. sidebar quick links)
├── mkdocs.yml          # Site configuration and navigation
└── requirements.txt    # Python dependencies (mkdocs-material)
```

## Contact

- GitHub: [melodypapa](https://github.com/melodypapa)
- Email: melodypapa@outlook.com

---

Copyright &copy; melodypapa
