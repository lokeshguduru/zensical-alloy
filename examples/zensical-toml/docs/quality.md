# Quality

Use this checklist before changing shared theme behavior or a visible surface.

## Build Checks

Build the canonical example:

```bash
cd examples/zensical-toml
../../.venv/bin/zensical build
```

Run the full local sweep from the repo root:

```bash
./scripts/smoke.sh
```

The smoke script checks cache-bust versions and builds the canonical docs,
MkDocs compatibility example, variant fixtures, and real-world shape fixtures.

## Version Guard

Theme assets use cache-bust query strings. Keep them in sync with the package
version:

```bash
./scripts/bump-version.py --check
```

When changing shipped CSS, JavaScript, templates, or package metadata, bump them
together:

```bash
./scripts/bump-version.py 0.2.1
```

## Navigation

- Top navigation remains balanced with and without search or repository links.
- Section links navigate to index pages when index pages exist.
- Section chevrons expand in place.
- Active sidebar items stay visible while scrolling.

## Visual Surfaces

- Code actions do not overlap code text.
- Code line numbers and code text stay aligned.
- Annotation popovers escape code blocks.
- Callouts align icon, title, content, and chevron.
- Charts keep tooltips inside the chart layer.
- Tables, tabs, grids, and footer controls stay compact.

## Manual Pages To Check

- Home
- Installation
- Configuration
- Code blocks
- Callouts
- Charts
- Kitchen Sink

Check each page in light and dark mode. Also check a phone-width viewport.

## Fixture Coverage

The fixture matrix covers common project shapes:

- `accent-cyan`: custom `extra.alloy` accent colors.
- `compact-layout`: narrower content, sidebar, and TOC widths.
- `deep-nav`: nested section navigation and section index rows.
- `no-search-no-repo`: header without search or repository controls.
- `system-fonts`: remote fonts disabled.
- `minimal-features`: theme enabled without the larger feature list.
- `fastapi-style`: tutorial and reference docs.
- `sdk-reference`: generated API reference density.
- `product-handbook`: long prose, tasks, charts, and runbooks.

## Release Readiness

- README and docs use the same package name and theme name.
- Package version matches CSS and JavaScript cache-bust strings.
- `repo_url` points to the project repository.
- Example copy is clear and current.
