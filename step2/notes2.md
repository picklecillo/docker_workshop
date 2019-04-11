# Estructura Dockerfile
```
FROM <> # Imagen base

ADD <> # Agrega un archivo
COPY <> # También acepta URLs

RUN <> # Ejecuta un comando dentro de la construcción de la imagen

ENV <> # Variable de ambiente

EXPOSE <> # Expone un puerto

CMD <> # cmd de entrada. puede pisarse
ENTRYPOINT <> # script de entrada
```

## CMD vs ENTRYPOINT
`ENTRYPOINT` sets the command and parameters that will be executed first when a container is run. Any command line arguments passed to `docker run <image>` will be appended to the entrypoint command, and will override all elements specified using `CMD`. For example, `docker run <image> bash` will add the command argument bash to the end of the entrypoint.

* [Docker ENTRYPOINT CMD Dockerfile best practices](https://medium.freecodecamp.org/docker-entrypoint-cmd-dockerfile-best-practices-abc591c30e21)

# Comandos
1. `docker run`: Levanta un contenedor a partir de una imagen local o remota.
2. `docker build`: Construye una imagen a partir de un `Dockerfile`.
3. `docker inspect <container_id>`: Permite ver toda la configuración del contenedor.
4. `docker logs <container_id>`

# Build custom Dockerfile

```bash
docker build -t hello_world_flask step2
docker run -p 5000:5000 --name hello_world_flask_container hello_world_flask
```
