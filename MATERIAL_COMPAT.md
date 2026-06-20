# Material / Zensical compatibility

Alloy is a skin on top of Material via Zensical's `extends: material`
chain. This file pins which upstream versions Alloy is tested against
and records the upstream selector or behavior changes that have required
a fix.

## Supported versions

| Component       | Minimum tested  | Maximum tested  |
| --------------- | --------------- | --------------- |
| `zensical`      | `0.0.40`        | `0.0.40`        |
| Python          | `3.10`          | `3.13`          |

Alloy's `pyproject.toml` requires `zensical>=0.0.40`. Newer Zensical
versions should work unchanged unless they ship breaking selector changes
in Material's bundled CSS, which we track below.

## Upstream surfaces Alloy depends on

Alloy targets these Material selectors and CSS variables directly. Any
upstream refactor that renames or moves one of these is a Material
breaking change that requires an Alloy update.

### CSS variables

- `--md-default-bg-color`, `--md-default-bg-color--light`,
  `--md-default-bg-color--lighter`, `--md-default-bg-color--lightest`
- `--md-default-fg-color`, `--md-default-fg-color--light`,
  `--md-default-fg-color--lighter`, `--md-default-fg-color--lightest`
- `--md-primary-bg-color`, `--md-primary-fg-color`,
  `--md-primary-fg-color--light`, `--md-primary-fg-color--dark`
- `--md-accent-fg-color`, `--md-accent-fg-color--transparent`,
  `--md-accent-bg-color`
- `--md-typeset-color`, `--md-typeset-a-color`
- `--md-code-bg-color`, `--md-code-fg-color`
- `--md-footer-bg-color`, `--md-footer-fg-color`,
  `--md-footer-bg-color--dark`, `--md-footer-fg-color--light`,
  `--md-footer-fg-color--lighter`
- `--md-mermaid-*` (font, edge, node, label, sequence-actor, loop-line)

### Class selectors

- Layout: `.md-grid`, `.md-main__inner`, `.md-container`, `.md-content`,
  `.md-content__inner`, `.md-content__inner::before`
- Header: `.md-header`, `.md-header__inner`, `.md-header__button`,
  `.md-header__brand`, `.md-header__title`, `.md-header__topic`,
  `.md-header__source`, `.md-header--shadow`, `.md-header--lifted`,
  `.md-header__button.md-logo`, `.md-header[hidden]`
- Sidebar: `.md-sidebar`, `.md-sidebar--primary`, `.md-sidebar--secondary`,
  `.md-sidebar__scrollwrap`, `.md-sidebar__inner`,
  `.md-sidebar-button`, `[data-md-toggle=drawer]:checked ~ .md-container .md-sidebar--primary`
- Nav: `.md-nav`, `.md-nav__list`, `.md-nav__item`, `.md-nav__link`,
  `.md-nav__title`, `.md-nav__icon`, `.md-nav__source`,
  `.md-nav__container`, `.md-nav__item--section`, `.md-nav__item--nested`,
  `.md-nav__item--active`, `.md-nav__toggle:checked`,
  `.md-nav__link--active`, `.md-toggle--indeterminate`
- TOC: `.md-nav--secondary`
- Tabs (nav): `.md-tabs`, `.md-tabs__list`, `.md-tabs__item`,
  `.md-tabs__link`, `.md-tabs__item--active`, `.md-tabs__link--active`
- Code: `.md-typeset .highlight`, `.md-typeset .highlight .highlighttable`,
  `.md-typeset .highlight .linenos`, `.md-typeset .highlight .code`,
  `.md-typeset .highlight code > span[id^="__span"]`,
  `.md-typeset .highlight .hll`, `.md-typeset .highlight span.filename`,
  `.md-typeset .highlight .md-clipboard`,
  `.md-typeset .highlight [data-md-component="clipboard"]`,
  `.md-typeset .highlight .md-code__nav`,
  `.md-typeset .highlight .md-code__button`
- Tabbed content: `.md-typeset .tabbed-set`, `.tabbed-labels`,
  `.tabbed-labels--linked`, `.tabbed-content`, `.tabbed-block`,
  `.tabbed-control`, `.js .md-typeset .tabbed-labels:before`,
  `.md-typeset .tabbed-set > input.focus-visible ~ .tabbed-labels:before`,
  `.md-content__inner > .tabbed-set .tabbed-labels:after`
- Callouts: `.md-typeset .admonition`, `.md-typeset details`,
  `.md-typeset .admonition > .admonition-title`,
  `.md-typeset details > summary`
- Buttons: `.md-typeset .md-button`, `.md-typeset .md-button--primary`,
  `.md-content__button`, `.md-content__button--copy-markdown`,
  `.md-content__button--copied`
- Search: `.md-search__form`, `.md-search__input`, `.md-search__output`,
  `.md-search__icon`, `.md-search-result__item`,
  `.md-search-result__link`, `.md-search-result__teaser`
- Footer: `.md-footer`, `.md-footer__inner`, `.md-footer-meta`,
  `.md-footer-meta__inner`, `.md-footer__link`,
  `.md-footer__link--prev`, `.md-footer__link--next`,
  `.md-footer__button`, `.md-footer__title`, `.md-footer__direction`,
  `.md-copyright`, `.md-social`, `.md-social__link`
- Runtime: `.md-progress`, `.md-top`, `.md-dialog`, `.md-dialog__inner`,
  `.md-banner`, `.md-banner__button`, `.md-consent`, `.md-consent__inner`,
  `.md-overlay`, `.md-skip`
- Content actions: `.md-content__button`, `[data-md-component=header]`,
  `[data-md-component=logo]`, `[data-md-component=clipboard]`,
  `[data-md-color-scheme=default]`, `[data-md-color-scheme=slate]`,
  `[data-md-color-primary]`, `[data-md-color-accent]`
- Tabs (page action): `.md-content__button`,
  `.md-typeset .md-content__button:hover`

### JavaScript surfaces

- `document$` Observable for instant-nav lifecycle (used by
  `sidebar-scroll.js`, `echarts.js`, and `copy-markdown.js`)
- `document.body[data-md-color-scheme]` attribute mutation
  (used by `echarts.js` for live recolor)
- `data-md-component="clipboard"` for code-block copy buttons
- `.js` class on `<html>` (added by Material's runtime; used in the
  tabbed-labels indicator suppression)

## Compatibility lessons for downstream CSS

Adopters often ship `extra_css/custom.css` files written against Material's
default token semantics. Two semantics matter:

- `--md-default-*` are **neutral surfaces**: body bg, prose fg. Alloy
  remaps these to its own `--background` / `--foreground` tokens. Safe
  because the meaning matches.
- `--md-primary-*` are **branded surfaces**: Material's header background
  and tab bar use them. Alloy paints those surfaces directly via component
  CSS, so we intentionally **do not** remap `--md-primary-*`. Downstream
  CSS that uses `--md-primary-fg-color` as a branded background color (a
  common Material idiom) sees Material's saturated brand value, not our
  prose foreground, which is what those rules expected.

If your `custom.css` from a Material project does any of the following,
it will continue to work under Alloy without changes:

```css
.testimonial { background-color: var(--md-primary-fg-color); }
.hero-band   { background: var(--md-primary-fg-color); color: var(--md-primary-bg-color); }
```

If your CSS hard-codes Material's hex values (e.g. `#009688`), bind the
brand color to a CSS variable instead so swapping themes is one-line.

## Known upstream-fragile spots

These rules are most likely to break on a Material refactor. Audit them
first when bumping `zensical`:

1. **Content tabs indicator suppression** (`tabs.css`). Material's
   `.js .md-typeset .tabbed-labels:before` selector draws the default
   underline, the focus-visible input selector recolors it, and mobile
   `.tabbed-labels:after` selectors reserve extra scroll padding. Alloy
   matches those selector shapes and relies on load order. If Material
   changes the indicator selector shape, this is the first thing to verify.
2. **Header transform scoping** (`header.css`). Alloy resets `transform`
   via `.md-header--alloy:not([hidden])` so Material's autohide can apply.
   If Material moves autohide from `[hidden]` to a class, update the
   selector.
3. **Mobile drawer positioning** (`responsive.css`). Material's mobile
   drawer uses `position: fixed; top: .4rem; height: calc(100% - .8rem)`.
   Alloy overrides `top` and `height` to push the drawer below the
   header. If Material restructures the drawer geometry, the override
   needs revisiting.
4. **Per-line code span overflow** (`code.css`). Alloy sets
   `width: max-content; min-width: 100%; max-width: none` on `<code>` and
   each line `<span>` so `<pre>`'s `scrollWidth` reflects content width
   and the in-block horizontal scroll engages. If Material changes the
   per-line wrapper element or its display, the fix needs to follow.
5. **Tabbed labels link underline** (`tabs.css`). The `content.tabs.link`
   feature wraps labels in `<a>`. Alloy suppresses the inherited prose link
   underline. If Material changes that wrapping element type, update the
   selector.
6. **Section-label hide rule** (`sidebar.css`). Scoped to
   `body:has(.md-tabs)` + desktop breakpoint. If Material renders
   `.md-tabs` even when the feature is off (or vice versa), the section
   labels will hide / un-hide incorrectly.
7. **Nested nav disclosure chevrons** (`sidebar.css`). Material emits two
   different structures depending on `navigation.indexes`: indexed rows use
   `.md-nav__container > label.md-nav__link`, while non-indexed nested
   rows use `li.md-nav__item--nested > label.md-nav__link >
   .md-nav__icon`. Alloy styles both paths explicitly so sections remain
   visibly expandable. Avoid using `.md-nav__item--active` as an open-state
   fallback here; it makes the current branch look unclickable because the
   checkbox can no longer collapse it. For non-indexed rows, Alloy draws the
   chevron as a mask on `.md-nav__icon` itself and suppresses Material's
   pseudo-elements, since upstream active-row transforms can otherwise keep
   the visual arrow rotated after collapse.

## Update playbook

When bumping the `zensical` dependency:

1. Read Material's CHANGELOG for renames or removed classes / variables in
   the lists above.
2. Run `./scripts/smoke.sh` and visually inspect the kitchen sink in
   both schemes against pre-bump screenshots.
3. Open the seven "upstream-fragile spots" above and confirm each rule
   still matches.
4. If the upstream version delivers new features (palette options,
   new feature flags), assess whether Alloy needs to opt in or override.
5. Update the "Supported versions" table at the top of this file.
6. Bump Alloy's own version via `./scripts/bump-version.py`.

## Reporting incompatibilities

If you hit a Material feature that Alloy breaks unintentionally, open an
issue at <https://github.com/lokeshguduru/zensical-alloy/issues> with the
minimal reproducer and which upstream selector or feature is affected.
The fixes are almost always small once the selector battle is identified.
