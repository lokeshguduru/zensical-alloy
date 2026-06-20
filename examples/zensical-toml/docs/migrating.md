# Migrating From Material

Alloy extends Material. Most projects can switch themes with one config change
and keep their existing Markdown, plugins, and feature flags.

## Switch The Theme

In `zensical.toml`:

```toml
[project.theme]
name = "alloy"
```

In `mkdocs.yml`:

```yaml
theme:
  name: alloy
```

Add `zensical-alloy` to your project dependencies and rebuild.

## Behavior Alloy Preserves

Alloy does not replace the Material runtime. These features continue to use
upstream behavior:

- Search index, scoring, highlighting, and keyboard shortcut.
- Instant navigation and prefetching.
- Code annotations, code copy, and code selection.
- Footnote tooltips and content tooltips.
- Tabbed content, including linked tabs.
- Palette toggle and color-scheme persistence.
- MkDocs and Zensical plugins.
- Python Markdown and `pymdownx` extensions.
- MkDocs compatibility through `mkdocs.yml`.

If a Material feature is not called out below, assume it still works.

## Visual Changes

Alloy restyles these surfaces:

- Header and search trigger.
- Source link and palette toggle.
- Left navigation and right TOC.
- Typography and page spacing.
- Code blocks and code action buttons.
- Callouts, tables, content tabs, buttons, and task lists.
- Mermaid diagrams and ECharts blocks.
- Footer links and mobile drawer.

The goal is a calmer, denser interface while keeping the same authoring model.

## Defaults To Notice

### Header Autohide

Alloy keeps the header pinned by default. If you want Material's hide-on-scroll
behavior, enable `header.autohide`:

```toml
[project.theme]
features = ["header.autohide"]
```

### Top Navigation

`navigation.tabs` works normally. Alloy uses a neutral active state by default.
Set `top_nav_accent = true` if the active top tab should use the accent color.

```toml
[project.extra.alloy]
top_nav_accent = true
```

### Sidebar Section Labels

When `navigation.tabs` is enabled, Alloy hides duplicate top-level labels in the
desktop sidebar because the tab bar already names the section. When tabs are
off, the labels remain visible.

### Sidebar Expand Controls

Section chevrons expand and collapse in place. Section links still navigate when
clicked directly.

### Mobile TOC Button

Alloy hides Material's floating mobile TOC button. The page outline and
back-to-top control cover the same use case in a calmer way. You can restore it
with project CSS if your docs need it.

## Color Differences

Alloy maps Material `palette.accent` names into OKLCH tokens. This keeps prose
contrast consistent across light and dark mode while still accepting Material
names such as `indigo`, `amber`, and `deep-purple`.

If exact brand color is more important than automatic contrast tuning, set the
optional accent overrides directly:

```toml
[project.extra.alloy]
accent_color = "#5b5ef7"
accent_color_dark = "#8f91ff"
```

## Suggested Feature List

Start with the features your project already uses. This example shows a common
documentation setup:

```toml
[project.theme]
features = [
  "content.action.edit",
  "content.action.view",
  "content.code.annotate",
  "content.code.copy",
  "content.code.select",
  "content.footnote.tooltips",
  "content.tabs.link",
  "content.tooltips",
  "navigation.footer",
  "navigation.path",
  "navigation.sections",
  "navigation.tabs",
  "navigation.top",
  "search.highlight",
]

[project.extra.alloy]
accent_preset = "orange"
radius = "0.625rem"
```

## Roll Back

Change `name = "alloy"` back to `name = "material"` and rebuild. Alloy does not
modify your Markdown content, plugin pipeline, or extension configuration.
