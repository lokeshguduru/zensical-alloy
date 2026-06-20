# Workers

```yaml
services:
  api:
    image: alloy-smoke
    deploy:
      replicas: 3
```

!!! note "Worker count"

    The best worker count depends on workload, CPU, and memory.
