# Charts

Use `.zensical-echarts` when a page needs a small chart. Write a normal JSON
ECharts option inside the block. Alloy loads Apache ECharts, applies the current
theme colors, and keeps the chart in sync when the reader switches light or dark
mode.

<div class="zensical-echarts" markdown>

```json
{
  "title": { "text": "Weekly activity" },
  "tooltip": { "trigger": "axis" },
  "legend": { "top": 24 },
  "grid": { "left": 36, "right": 18, "top": 58, "bottom": 32 },
  "xAxis": {
    "type": "category",
    "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  },
  "yAxis": { "type": "value" },
  "series": [
    {
      "name": "Builds",
      "type": "bar",
      "data": [12, 18, 16, 24, 32, 28, 36],
      "itemStyle": { "borderRadius": [6, 6, 0, 0] }
    },
    {
      "name": "Deploys",
      "type": "line",
      "smooth": true,
      "data": [8, 10, 11, 16, 21, 18, 25]
    }
  ]
}
```

</div>

## Guidance

- Keep data small enough to read in the Markdown source.
- Use plain JSON. The block stays portable and easy to review.
- Set `window.zensicalAlloyEChartsSrc` before Alloy's chart script runs if your
  site must load ECharts from an approved internal URL.

## Line trend

<div class="zensical-echarts" markdown>

```json
{
  "title": { "text": "Traffic trend" },
  "tooltip": { "trigger": "axis" },
  "grid": { "left": 36, "right": 18, "top": 44, "bottom": 32 },
  "xAxis": {
    "type": "category",
    "boundaryGap": false,
    "data": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
  },
  "yAxis": { "type": "value" },
  "series": [
    {
      "name": "Visits",
      "type": "line",
      "smooth": true,
      "symbolSize": 7,
      "areaStyle": { "opacity": 0.12 },
      "data": [120, 180, 150, 220, 260, 310]
    }
  ]
}
```

</div>

## Composition

<div class="zensical-echarts" markdown>

```json
{
  "title": { "text": "Surface coverage" },
  "tooltip": { "trigger": "item" },
  "legend": {
    "bottom": 0,
    "itemWidth": 10,
    "itemHeight": 10
  },
  "series": [
    {
      "name": "Surface coverage",
      "type": "pie",
      "radius": ["48%", "72%"],
      "center": ["50%", "44%"],
      "avoidLabelOverlap": true,
      "label": { "show": false },
      "data": [
        { "value": 38, "name": "Code" },
        { "value": 24, "name": "Docs" },
        { "value": 18, "name": "Charts" },
        { "value": 20, "name": "Callouts" }
      ]
    }
  ]
}
```

</div>

## Empty data

Empty series render as a quiet state instead of a blank panel. This helps pages
that generate charts from optional data.

<div class="zensical-echarts" markdown>

```json
{
  "title": { "text": "No runs yet" },
  "xAxis": { "type": "category", "data": [] },
  "yAxis": { "type": "value" },
  "series": [
    { "name": "Runs", "type": "bar", "data": [] }
  ]
}
```

</div>
