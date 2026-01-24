# AGENTS.md

This file provides guidance for agentic coding agents working with this Jekyll-based static site repository.

## Project Overview

This is a multilingual technical documentation blog (Jekyll + GitHub Pages) focused on automotive software engineering, embedded systems, and processor architecture. Content is published in English, German, and Chinese.

## Development Commands

### Local Development
```bash
# Start development server (requires restart after _config.yml changes)
npm run serve
# or
bundle exec jekyll serve

# Install dependencies
bundle install

# Build static site
bundle exec jekyll build
```

### Validation
```bash
# No automated testing framework - validate through Jekyll build
bundle exec jekyll build --verbose
```

## Content Structure & Conventions

### File Organization
- **Blog posts**: `_posts/YYYY-MM-DD-title.md` (require Jekyll front matter)
- **Documentation sections**: Organized in topical directories with `index.md` navigation
- **Assets**: Images stored alongside referencing markdown files (~380 images total)

### Jekyll Front Matter Requirements
All markdown files must include minimum front matter:
```yaml
---
layout: post
title: Post Title
---
```

For documentation pages:
```yaml
---
layout: default
title: Page Title
---
```

## Code Style Guidelines

### Markdown Formatting
- Use GitHub-flavored markdown syntax
- Include proper alt text for images
- Use relative paths for image references from file location
- Follow existing heading hierarchy (no skipped levels)

### Content Standards
- Technical accuracy is paramount
- Use consistent terminology across languages
- Include code examples with proper syntax highlighting
- Reference official specifications (AUTOSAR, ARM, Infineon)

### Multilingual Considerations
- Language determined by directory structure and file naming
- Chinese characters used in site title and content
- Maintain consistency in technical terminology across languages

## File Naming Conventions

### Blog Posts
- Format: `YYYY-MM-DD-descriptive-title.md`
- Use lowercase with hyphens for separation
- Include date prefix for chronological ordering

### Documentation
- Use descriptive directory names (e.g., `autosar/`, `cortex/`, `automotive/`)
- Each section has `index.md` for navigation/overview
- Subdirectories follow hierarchical organization

## Configuration Management

### Critical Files
- **`_config.yml`**: Jekyll site configuration (requires server restart after changes)
- **`Gemfile.lock`**: Ruby dependencies (GitHub Pages compatible)
- **`.vscode/settings.json`**: Spell check configuration for EN/DE/FR

### Spell Check
The project uses cSpell with:
- Languages: English, German (de-DE), French
- Custom dictionary includes technical terms (AUTOSAR, ARM, embedded systems)
- Technical terms automatically added to `.vscode/settings.json`

## Architecture Notes

### Jekyll Configuration
- **Theme**: Minima (Jekyll default)
- **Plugins**: `jekyll-feed` for RSS generation
- **GitHub Pages**: Uses `github-pages` gem (version 225)
- **Compatibility**: Configured for GitHub Pages deployment

### Content Organization Pattern
Each documentation section follows:
```
section/
├── index.md (navigation/overview)
├── subsection1/
│   └── topic.md
└── subsection2/
    └── topic.md
```

## Development Workflow

### Before Making Changes
1. Read existing files in target section to understand conventions
2. Check for similar content patterns to follow
3. Verify image paths and references

### Content Creation
1. Follow established directory structure
2. Include proper Jekyll front matter
3. Use relative image paths
4. Test with `bundle exec jekyll build`

### Validation
- No automated testing framework
- Manual validation through Jekyll build process
- Check for broken links and image references
- Verify multilingual consistency

## Important Reminders

- **Server Restart**: Required after modifying `_config.yml`
- **Image References**: Use relative paths from markdown file location
- **Front Matter**: Mandatory for all markdown files
- **Multilingual**: Maintain technical term consistency across languages
- **GitHub Pages**: Ensure compatibility with github-pages gem constraints

## Common Tasks

### Adding New Blog Post
1. Create file in `_posts/` with proper naming convention
2. Include required front matter with layout and title
3. Add content following markdown conventions
4. Test build locally

### Creating New Documentation Section
1. Create new directory with descriptive name
2. Add `index.md` with navigation/overview
3. Organize content in hierarchical subdirectories
4. Follow existing patterns for consistency

### Updating Existing Content
1. Read file to understand current structure
2. Maintain existing formatting and style
3. Update image references if needed
4. Validate changes with Jekyll build