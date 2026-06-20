# Settings

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `debug` | `bool` | `false` | Enable verbose logs |
| `workers` | `int` | `1` | Number of worker processes |
| `root_path` | `str` | `""` | Path prefix behind a proxy |

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
    workers: int = 1
```
