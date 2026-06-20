# Projects

## `projects.create`

```python
project = client.projects.create(name="Docs", visibility="private")
```

## `projects.list`

```python
projects = client.projects.list(limit=20)
```

## Response

| Field | Type |
| --- | --- |
| `id` | `str` |
| `name` | `str` |
| `created_at` | `datetime` |
