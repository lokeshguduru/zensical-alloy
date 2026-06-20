# Deployments

## `deployments.create`

```python
deployment = client.deployments.create(project_id="proj_123", branch="main")
```

!!! warning "Idempotency"

    Retry deployment creation with an idempotency key in production clients.
