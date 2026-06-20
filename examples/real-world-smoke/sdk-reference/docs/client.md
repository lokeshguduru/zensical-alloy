# Client

## `AlloyClient`

```python linenums="1"
class AlloyClient:
    def __init__(self, token: str, *, base_url: str | None = None) -> None:
        self.token = token
        self.base_url = base_url or "https://api.example.test"

    def list_projects(self, *, limit: int = 50) -> list[dict[str, object]]:
        return []
```

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `token` | `str` | yes | API token |
| `base_url` | `str` | no | Override endpoint |

!!! note "Generated pages"

    Generated references often create many headings. The TOC should stay calm.
