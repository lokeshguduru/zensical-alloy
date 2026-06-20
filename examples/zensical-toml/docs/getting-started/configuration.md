# Configuration

Alloy inherits Material's configuration and adds a small set of options for the
visual layer.

## Palette

Use normal palette settings when you want to stay close to Material config.
These are Material named accents, so multi-word names use hyphens, such as
`deep-purple`.

```toml
[[project.theme.palette]]
scheme = "default"
primary = "white"
accent = "orange"

[[project.theme.palette]]
scheme = "slate"
primary = "black"
accent = "orange"
```

Use Alloy's curated presets when you want direct accent control:

```toml
[project.extra.alloy]
accent_preset = "cyan"
```

Or set optional exact-color overrides:

```toml
[project.extra.alloy]
accent_color = "#5b5ef7"
accent_color_dark = "#8f91ff"
```

## Fonts

```toml
[project.extra.alloy]
font_sans = "\"Geist\", \"Inter\", ui-sans-serif, system-ui"
font_mono = "\"Geist Mono\", ui-monospace, monospace"
```

## Layout

Use layout options for dense navigation or wide code samples:

```toml
[project.extra.alloy]
content_width = "46rem"
sidebar_width = "clamp(10rem, 18vw, 14.5rem)"
toc_width = "clamp(9rem, 15vw, 13rem)"
```

## Features

All Material and Zensical feature flags remain available. Start with the flags
your project already uses and add more only when needed.

```toml
[project.theme]
name = "alloy"
features = [
  "content.code.copy",
  "content.code.annotate",
  "content.tabs.link",
  "navigation.footer",
  "navigation.path",
  "navigation.tabs",
  "search.highlight",
]
```

See [Theming](../theming.md) for the full Alloy option list.
