# Architecture

Alloy is a visual layer on top of Zensical's Material theme. It does not fork
the engine or replace the runtime behavior.

## Alloy Owns

- Design tokens for color, radius, spacing, and type.
- Template partials for the header, search trigger, page actions, and TOC.
- Component CSS for navigation, code, callouts, tables, tabs, charts, and the
  footer.
- Small runtime scripts for sidebar behavior, Markdown copy, and chart
  hydration.

## Zensical Owns

- Markdown parsing and page rendering.
- Navigation, search, palette switching, and instant navigation.
- Code annotations, footnotes, content tabs, and tooltips.
- Compatibility for `zensical.toml` and `mkdocs.yml`.

## Project Layout

```text
zensical_alloy/
  main.html
  mkdocs_theme.yml
  assets/
    stylesheets/zensical-alloy/
    javascripts/zensical-alloy/
  partials/
```

- `mkdocs_theme.yml` declares the parent theme and default features.
- `main.html` loads the theme CSS and small runtime scripts.
- `tokens.css` defines semantic colors, spacing, and sizing.
- `components/` keeps each visual surface in a focused CSS file.
- `partials/` contains template overrides where the markup needs help.

## Design Rule

Keep visual behavior in the theme. Move larger features into extensions when
they need custom syntax, persistent configuration, or a separate release cycle.

That boundary keeps Alloy easy to update when Zensical or Material changes.
