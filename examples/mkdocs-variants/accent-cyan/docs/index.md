# Cyan Accent Fixture

This fixture keeps the normal navigation shape but changes the accent away from
the default warm tone. It is here to catch places where a component accidentally
hard-codes one accent color.

[Cyan links should be obvious](#accent-swatches), and active controls should use
the same accent.

## Accent swatches

<div class="grid cards" markdown>

-   **Configured accent**

    <span style="display:inline-block;width:4rem;height:1.25rem;border-radius:999px;background:var(--brand-accent);vertical-align:middle"></span>

    Reads from `--brand-accent`.

-   **Soft accent**

    <span style="display:inline-block;width:4rem;height:1.25rem;border-radius:999px;background:var(--brand-accent-soft);vertical-align:middle"></span>

    Reads from `--brand-accent-soft`.

-   **Link color**

    [This link](#accent-swatches) should use the configured cyan accent.

</div>

## Code

```python
def accent_name() -> str:
    return "cyan"
```

!!! note "Accent check"

    Links, code actions, tabs, and charts should follow the configured accent.

=== "Cyan"

    This active tab should use the configured accent.

=== "Neutral"

    This tab should stay quiet until selected.

## Chart

<div class="zensical-echarts" markdown>

```json
{
  "tooltip": { "trigger": "axis" },
  "xAxis": { "type": "category", "data": ["A", "B", "C"] },
  "yAxis": { "type": "value" },
  "series": [{ "type": "bar", "name": "Score", "data": [4, 7, 5] }]
}
```

</div>
