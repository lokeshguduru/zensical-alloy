# MkDocs Variants

These fixtures use `mkdocs.yml`. They help check projects that move from
MkDocs-style configuration to Zensical with Alloy.

## Accent Color

Path: `examples/mkdocs-variants/accent-cyan`

```yaml
extra:
  alloy:
    accent_color: "oklch(0.62 0.16 218)"
    accent_color_dark: "oklch(0.72 0.14 218)"
    top_nav_accent: true
```

Check links, active states, chart colors, code actions, and accented top
navigation.

## Compact Layout

Path: `examples/mkdocs-variants/compact-layout`

```yaml
extra:
  alloy:
    content_width: "40rem"
    sidebar_width: "12rem"
    toc_width: "10rem"
```

Check clipping around code actions, long headings, and page actions.

## Deep Navigation

Path: `examples/mkdocs-variants/deep-nav`

```yaml
theme:
  features:
    - navigation.path
    - navigation.sections
    - navigation.tabs
```

Check nested sections, breadcrumbs, active sidebar states, and expand controls.

## No Search, No Repo

Path: `examples/mkdocs-variants/no-search-no-repo`

```yaml
plugins: []

theme:
  name: alloy
```

Check header spacing when search and repository controls are absent.

## System Fonts

Path: `examples/mkdocs-variants/system-fonts`

```yaml
theme:
  name: alloy
  font: false

extra:
  alloy:
    font_sans: "ui-sans-serif, system-ui, sans-serif"
    font_mono: "ui-monospace, SFMono-Regular, monospace"
```

## Minimal Features

Path: `examples/mkdocs-variants/minimal-features`

This fixture enables the theme with a small palette config. It catches
assumptions that only work with the full feature list.

## Suggested Ports

```bash
cd examples/mkdocs-variants/accent-cyan
../../.venv/bin/zensical serve -a 127.0.0.1:8771
```

```bash
cd examples/mkdocs-variants/deep-nav
../../.venv/bin/zensical serve -a 127.0.0.1:8772
```

```bash
cd examples/mkdocs-variants/no-search-no-repo
../../.venv/bin/zensical serve -a 127.0.0.1:8773
```
