# Estructura Dockerfile
```
FROM <> # Imagen base

ADD <> # Agrega un archivo
COPY <> # También acepta URLs

RUN <> # Ejecuta un comando dentro de la construcción de la imagen

ENV <> # Variable de ambiente

EXPOSE <> # Expone un puerto

CMD <> # ????
ENTRYPOINT <> # script de entrada
```

# Comandos
1. `docker run`: Levanta un contenedor a partir de una imagen local o remota.
2. `docker build`: Construye una imagen a partir de un `Dockerfile`.

# Build custom Dockerfile

```bash
docker build -t hello_world_flask step2
docker run -p 5000:5000 --name hello_world_flask_container hello_world_flask
```

