# Zensical Alloy

A documentation theme for [Zensical](https://zensical.org). Alloy extends the
built-in Material theme, so search, instant navigation, code annotations,
footnotes, tabs, palette switching, and plugins keep working.

Alloy only changes the visual layer. It gives Material a quieter header, denser
navigation, calmer typography, and matching styles for common documentation
surfaces.

[![PyPI version](https://img.shields.io/pypi/v/zensical-alloy.svg?logo=pypi&label=PyPI&color=4c4c4c)](https://pypi.org/project/zensical-alloy/)
[![Python versions](https://img.shields.io/pypi/pyversions/zensical-alloy.svg?label=Python&color=4c4c4c)](https://pypi.org/project/zensical-alloy/)
[![MIT license](https://img.shields.io/badge/license-MIT-4c4c4c.svg)](LICENSE)

![Alloy kitchen sink, light scheme](https://raw.githubusercontent.com/lokesh-guduru/zensical-alloy/main/.github/assets/kitchen-sink-light.png)

## Install

```bash
pip install zensical-alloy
```

## Use

In `zensical.toml`:

```toml
[project.theme]
name = "alloy"

[project.extra.alloy]
accent_preset = "violet"
```

In `mkdocs.yml`:

```yaml
theme:
  name: alloy

extra:
  alloy:
    accent_preset: violet
```

## What Alloy Changes

- Header, search trigger, source link, and palette toggle.
- Left navigation, right table of contents, and footer links.
- Prose typography, headings, links, tables, and task lists.
- Code blocks, annotations, content tabs, callouts, and buttons.
- Mermaid diagrams and optional Apache ECharts blocks.
- Mobile drawer spacing and tap targets.

Alloy does not replace the Material runtime. The behavior stays upstream.

## Screenshots

| Light | Dark |
| --- | --- |
| ![Light scheme](https://raw.githubusercontent.com/lokesh-guduru/zensical-alloy/main/.github/assets/kitchen-sink-light.png) | ![Dark scheme](https://raw.githubusercontent.com/lokesh-guduru/zensical-alloy/main/.github/assets/kitchen-sink-dark.png) |

| Code | Callouts |
| --- | --- |
| ![Code blocks](https://raw.githubusercontent.com/lokesh-guduru/zensical-alloy/main/.github/assets/code-light.png) | ![Callouts](https://raw.githubusercontent.com/lokesh-guduru/zensical-alloy/main/.github/assets/callouts-light.png) |

| Mobile home | Mobile drawer |
| --- | --- |
| ![Home, phone viewport](https://raw.githubusercontent.com/lokesh-guduru/zensical-alloy/main/.github/assets/home-mobile.png) | ![Phone drawer open](https://raw.githubusercontent.com/lokesh-guduru/zensical-alloy/main/.github/assets/mobile-drawer.png) |

## Theme Knobs

All public options live under `[project.extra.alloy]`:

```toml
[project.extra.alloy]
accent_preset = "violet"       # orange, slate, cyan, violet
accent_color = "oklch(...)"    # optional light-mode override
accent_color_dark = "oklch(...)" # optional dark-mode override
radius = "0.625rem"
font_sans = "\"Inter\", ui-sans-serif, system-ui"
font_mono = "\"JetBrains Mono\", ui-monospace"
content_width = "46rem"
sidebar_width = "clamp(10rem, 18vw, 14.5rem)"
toc_width = "clamp(9rem, 15vw, 13rem)"
top_nav_accent = false
```

`accent_preset` uses Alloy's curated preset values. Material `palette.accent`
still accepts Material names such as `indigo`, `amber`, and `deep-purple`.

Use `alloy_layout: wide` in page front matter when one page needs wider content:

```yaml
---
title: System overview
alloy_layout: wide
---
```

See the [theming guide](examples/zensical-toml/docs/theming.md) for details.

## Compatibility

Alloy is tested with `zensical >= 0.0.40` on Python 3.10 through Python 3.13.

The compatibility notes in [MATERIAL_COMPAT.md](MATERIAL_COMPAT.md) list the
upstream Material selectors and variables that Alloy relies on.

## Local Development

```bash
python -m venv .venv
.venv/bin/pip install -e .
.venv/bin/python scripts/bundle-css.py --watch
```

In another terminal:

```bash
cd examples/zensical-toml
../../.venv/bin/zensical serve -a 127.0.0.1:8765
```

Open <http://127.0.0.1:8765>. The Kitchen Sink page is the main regression
target because it places the busiest surfaces on one page.

## Checks

Run the full local sweep:

```bash
./scripts/smoke.sh
```

That rebuilds the CSS bundle, checks cache-bust versions, and builds the
canonical docs, MkDocs compatibility example, variant fixtures, and real-world
shape fixtures.

## Contributing

Good changes are small and visible. Improve one component, add one focused
fixture, tighten the docs, or make light and dark mode more consistent.

Read the [contributing guide](examples/zensical-toml/docs/contributing.md) for
the workflow.

## License

[MIT](LICENSE)
