# Contributing

Alloy should stay small, readable, and easy to update. Good changes usually
improve one surface at a time.

## Good First Fixes

- Polish an existing component.
- Add a focused example to the Kitchen Sink page.
- Improve light and dark mode parity.
- Tighten setup docs where the path is unclear.
- Add a visual regression case for a real layout bug.

## Local Checks

Build the main example:

```bash
cd examples/zensical-toml
../../.venv/bin/zensical build
```

When a change touches shared theme assets, build the MkDocs-compatible example:

```bash
cd examples/mkdocs-yml
../../.venv/bin/zensical build
```

For the full local sweep, run this from the repo root:

```bash
./scripts/smoke.sh
```

That command builds the canonical docs, MkDocs compatibility example, variant
fixtures, and real-world shape fixtures.

## Style Guide

- Prefer tokens over hard-coded colors.
- Keep component CSS scoped to the surface it styles.
- Avoid template overrides unless CSS cannot solve the problem cleanly.
- Add comments only where the reason is not obvious from the code.
- Keep examples realistic enough to catch bugs.
- Write docs in plain language.

## Feature Boundaries

Alloy should focus on theme behavior. If a feature needs custom syntax,
persistent data, or its own release rhythm, it probably belongs in a Zensical
extension instead of the theme.
