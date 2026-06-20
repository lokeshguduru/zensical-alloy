# First Steps

Create a small application:

```python title="main.py" linenums="1"
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    return {"items": [{"name": "Alloy"}], "q": q}
```

!!! tip "Interactive docs"

    Framework docs often mix prose, code, and callouts in quick succession.

## Run it

```bash
uvicorn main:app --reload
```
