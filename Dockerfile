# Esta es la imagen base del proyecto
#ya tiene instalado python3
FROM jfloff/alpine-python:latest-slim
# Especifica el autor.
MAINTAINER Rodrigo Orellana

# Indicamos el directorio de trabajo de la imagen:
WORKDIR ~/ecochallenge/

#Copiamos los archivos necesarios para que funcione el servicio web.
COPY ./principal.py  principal.py
COPY ./mongoDB.py  mongoDB.py
COPY ./desafio.py  desafio.py
COPY ./competidor.py  competidor.py
COPY ./requirements.txt requirements.txt

# Instalan los packetes gcc y musl-dev necesario para nuestra instalación
# Se agregar a los paquetes de manera virtual
# no a los globales pues solo es usada en la creación.
# Luego los podemos quitar, así nuestra imagen solo posee lo necesario
# Y la mantenemos de bajo tamaño
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
# Instala las dependecias del servicio 
RUN pip install -r requirements.txt

# Quitamos los paquetes gcc y musl-dev 
RUN apk del .build-deps
# abrir el puerto 8989
EXPOSE 8989
# Comandos para ejecutar el servicio
# ENTRYPOINT indica que CMD se ejecuta sobre python
ENTRYPOINT ["python3"]
# ejecuta la app
CMD ["principal.py"]
