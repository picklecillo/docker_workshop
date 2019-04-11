# Docker

**En mi máquina sí funciona!**

## Pq es bkn?

![Docker vs VM](docker_vs_vm.jpg)

## Conceptos

* **Docker**: The key benefit of Docker is that it allows users to package an application with all of its dependencies into a standardized unit for software development. Unlike virtual machines, containers do not have the high overhead and hence enable more efficient usage of the underlying system and resources.
* **VM**: Isolation at great cost.
* **Container**: This gives developers the ability to create predictable environments that are isolated from rest of the applications and can be run anywhere.
* **Imagen**: A Docker image is built up from a series of **layers**. 

---
	
**Container vs imagen**: The major difference between a container and an image is the top writable layer. All writes to the container that add new or modify existing data are stored in this writable layer. When the container is deleted, the writable layer is also deleted. The underlying image remains unchanged.

---

* **Layer**: Each layer represents an instruction in the image’s Dockerfile. Each layer except the very last one is read-only.	
	Each layer is only a set of differences from the layer before it. The 	layers are stacked on top of each other. When you create a new 	container, you add a new writable layer on top of the underlying 	layers. This layer is often called the “container layer”.
* **asdf**:	

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
docker create --name hello_world alpine:latest ls
docker start --attach --interactive hello_world
```
Run -> creates a container and starts it

***

# Ejemplo Dockerfile

```bash
docker build --tag=hello_world_img step1/
docker images
docker run hello_world_img
```

