# Path Parameters

```python
@app.get("/users/{user_id}/projects/{project_id}")
def read_project(user_id: int, project_id: str):
    return {"user_id": user_id, "project_id": project_id}
```

## Validation

| Input | Result |
| --- | --- |
| `123` | accepted |
| `abc` | validation error |

!!! warning "Order matters"

    Specific routes should appear before parameterized routes.
