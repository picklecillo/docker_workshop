# Amononamiento del proyecto

## Docker-compose
```
...
services:
  web:
    build:
      context: ./app
      dockerfile: ../docker/web/Dockerfile
...
```

## Dockerfile
```
...
COPY . /app
WORKDIR /app
...
```