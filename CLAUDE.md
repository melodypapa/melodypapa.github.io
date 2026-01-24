# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based static site for a technical documentation blog, hosted on GitHub Pages. The site contains multilingual content (English, German, Chinese) focused on automotive software engineering, embedded systems, and processor architecture.

## Development Commands

### Install Dependencies
```bash
bundle install
```

### Local Development Server
```bash
npm run serve
# or
bundle exec jekyll serve
```
The site will be available at `http://localhost:4000`. Note that changes to `_config.yml` require restarting the server.

### Build Static Site
```bash
bundle exec jekyll build
```
Builds the site to `_site/` directory.

## Content Structure

### Blog Posts
- Location: `_posts/`
- Naming convention: `YYYY-MM-DD-title.md`
- All posts require Jekyll front matter with at minimum:
  ```yaml
  ---
  layout: post
  title: Post Title
  ---
  ```

### Documentation Sections
The site is organized into topical directories, each with an `index.md` for navigation:

- **`autosar/`** - AUTOSAR specifications and implementation guides (CAN, Ethernet, LIN, memory, diagnostics)
- **`cortex/`** - ARM Cortex processor documentation (M7, R52+ architectures, memory systems, programming models)
- **`automotive/`** - General automotive engineering topics
- **`cybersecurity/`** - Security-related documentation
- **`eb_tresos/`** - EB tresos configuration tool documentation
- **`nxp/`** - NXP processor documentation
- **`linux/`** - Linux-related content
- **`education/`** - Educational materials (mathematics, computer science)
- **`languages/`** - Language learning materials (primarily German)

### Assets
- Images are stored alongside the markdown files that reference them
- The site contains ~380 images supporting the documentation

## Configuration

### Site Configuration
- **File**: `_config.yml`
- **Theme**: Minima (Jekyll default theme)
- **Plugins**: `jekyll-feed` for RSS generation
- **GitHub Pages compatibility**: Uses `github-pages` gem (version 225)

### Spell Check
The project uses cSpell with support for:
- English, German (de-DE), and French
- Custom dictionary includes technical terms (AUTOSAR, ARM, embedded systems terminology)

## Architecture Notes

### Jekyll Theme Customization
- Custom styles: `_sass/` directory for SCSS extensions
- Theme: Uses Minima with potential customizations
- Layouts: Can override Minima layouts in `_layouts/` if present

### Multilingual Content
- Content is published in multiple languages without formal i18n framework
- Language is determined by content directory and file naming
- Chinese characters are used in site title and some content

### Content Organization Pattern
Each major documentation section follows this pattern:
- Directory with descriptive name
- `index.md` at root of section for navigation/overview
- Hierarchical subdirectories for detailed topics
- Markdown files with Jekyll front matter

## Important Notes

- No automated testing framework - content validation is manual through Jekyll build
- No CI/CD pipeline - deployment happens via GitHub Pages
- When modifying `_config.yml`, always restart the Jekyll server
- Image references should use relative paths from the markdown file location
