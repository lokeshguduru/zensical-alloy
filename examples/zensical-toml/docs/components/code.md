# Code Blocks

Inline `code` should read like code without breaking the paragraph rhythm.

## Fenced Block

```python
from zensical import Site

def build(config: dict) -> Site:
    """Render a static site from a Zensical config."""
    return Site.from_config(config).build()
```

## Filename

```ts title="lib/theme.ts"
export type Theme = {
  scheme: "default" | "slate"
  primary: string
  accent: string
}

export function applyTheme(theme: Theme): void {
  document.body.dataset.mdColorScheme = theme.scheme
}
```

## Line Numbers

```rust linenums="1"
fn fibonacci(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => fibonacci(n - 1) + fibonacci(n - 2),
    }
}
```
