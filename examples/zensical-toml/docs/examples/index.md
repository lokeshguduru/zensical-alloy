# Examples

Alloy ships source examples under `examples/`. They are used for local testing
and for showing common project shapes.

## Fixture Groups

| Group | Purpose |
| --- | --- |
| `examples/zensical-toml/` | Main Zensical docs site |
| `examples/mkdocs-yml/` | Minimal MkDocs-compatible setup |
| `examples/mkdocs-variants/` | Config compatibility and edge cases |
| `examples/real-world-smoke/` | Realistic documentation shapes |

## Run Everything

```bash
./scripts/smoke.sh
```

The smoke script builds each fixture and reports build failures.

## Serve One Fixture

```bash
cd examples/real-world-smoke/fastapi-style
../../.venv/bin/zensical serve -a 127.0.0.1:8771
```

Open <http://127.0.0.1:8771>. Use a different port when comparing multiple
fixtures side by side.

## What To Check

- Header balance when search or repository controls are missing.
- Left navigation with nested sections.
- Right TOC on long pages.
- Code block action alignment.
- Callouts, tables, tabs, and charts using the same visual language.
- Custom accent colors flowing through the theme.
