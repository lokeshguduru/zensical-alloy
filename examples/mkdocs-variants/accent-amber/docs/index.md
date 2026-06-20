# Amber accent

This fixture verifies that Alloy maps Material's named palette accent
**without overriding the adopter's choice**. The config only sets
`accent: amber` in the palette &mdash; no `accent_color`, no `accent_preset`.

## What to look for

- **Light scheme** &mdash; this [link](https://example.com) should render
  as a darker mustard yellow that clears WCAG AA against the white
  background.
- **Dark scheme** &mdash; toggle the palette in the header. The same link
  should now render as a bright neon yellow that clears AA against the
  dark background.

If you see orange instead of yellow, the warm-bucket split in
`tokens.css` regressed.

## Other prose

Inline `code` and **bold** sit at the accent-adjacent neutral. A
secondary [link with longer text](https://example.com) and a third
[short link](https://example.com) sit further down the paragraph so the
hue is comparable in context.

```python
def hello(name: str) -> str:
    """Smoke that the code block keeps its neutral palette."""
    return f"hello, {name}"
```

!!! note "Note"
    Callouts should keep their semantic accent (blue for note) and not pick
    up the amber link color.

!!! tip "Tip"
    The active content tab pill below picks up the amber accent.

=== "First"

    First tab content.

=== "Second"

    Second tab content. The active tab pill is amber per scheme.

=== "Third"

    Third tab content.
