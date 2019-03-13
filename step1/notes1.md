# Docker

## Conceptos

* **Docker**: The key benefit of Docker is that it allows users to package an application with all of its dependencies into a standardized unit for software development. Unlike virtual machines, containers do not have the high overhead and hence enable more efficient usage of the underlying system and resources.
* **VM**: Isolation at great cost.
* **Container**: This gives developers the ability to create predictable environments that are isolated from rest of the applications and can be run anywhere.
* **Imagen**:
* **Contenedor**:

***

# Cómo levantar con docker

## Hola mundo
```bash
docker run hello-world
```

## Terminal
```bash
docker run -it alpine sh
```

## Crear un contenedor
```bash
docker create --name hello_world alpine:latest sh
docker start --attach --interactive hello_world /bin/bash
```
Run -> creates a container and starts it

***

# Ejemplo Dockerfile

```bash
docker build --tag=hello_world_img step1/
docker images
docker run hello_world_img
```

