# FastAPI In Containers - Docker

When deploying applications, a common approach is to build a Linux container
image. This page intentionally uses words like `Dockerfile` and long headings to
stress inline code and right-side navigation.

!!! tip "Jump to the Dockerfile"

    In a hurry? Jump to the `Dockerfile` below and come back for details later.

## Build a Docker Image

```dockerfile title="Dockerfile" linenums="1"
FROM python:3.13-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
```

## Start the Docker Container

```bash
docker build -t alloy-smoke .
docker run -p 80:80 alloy-smoke
```

## Deployment Concepts

Longer sections should not push the TOC into the article column.
