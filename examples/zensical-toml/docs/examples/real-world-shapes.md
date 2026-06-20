# Real-World Shapes

These fixtures mimic common documentation sites. They are synthetic, but they
use realistic page structure and density.

## Framework Tutorial

Path: `examples/real-world-smoke/fastapi-style`

Includes tutorial pages, deployment pages, Dockerfile examples, dense code
blocks, reference tables, and multiple top-level sections.

```bash
cd examples/real-world-smoke/fastapi-style
../../.venv/bin/zensical serve -a 127.0.0.1:8781
```

Check code block action alignment, right TOC behavior, inline code inside
callouts, and nested sections.

## SDK Reference

Path: `examples/real-world-smoke/sdk-reference`

Includes class signatures, method signatures, nested resources, parameter
tables, repetitive headings, and code-heavy pages.

```bash
cd examples/real-world-smoke/sdk-reference
../../.venv/bin/zensical serve -a 127.0.0.1:8782
```

Check left navigation density, right TOC truncation, table rhythm, line height,
and copy controls.

## Product Handbook

Path: `examples/real-world-smoke/product-handbook`

Includes decision records, runbooks, task lists, charts, content tabs, and
operational tables.

```bash
cd examples/real-world-smoke/product-handbook
../../.venv/bin/zensical serve -a 127.0.0.1:8783
```

Check long-form reading rhythm, charts in both color schemes, task list styling,
tabs, and tables near prose.

## Why Local Fixtures

External docs change. Local fixtures keep the test inputs stable while the theme
evolves.
