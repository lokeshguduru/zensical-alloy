# Container Install

```dockerfile
FROM python:3.13-slim
RUN pip install zensical zensical-alloy
WORKDIR /docs
CMD ["zensical", "build"]
```

## Notes

Long code samples should not clip copy actions.
