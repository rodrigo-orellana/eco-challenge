# Esta es la imagen base del proyecto 
FROM ubuntu:latest
LABEL maintainer="rodrigoesteban@correo.ugr.es"
# Indicamos el directorio de trabajo de la imagen:
WORKDIR ~/ecochallenge/

#Copiamos los archivos necesarios para que funcione el servicio web.
COPY ./principal.py  principal.py
COPY ./mongoDB.py  mongoDB.py
COPY ./desafio.py  desafio.py
COPY ./competidor.py  competidor.py
COPY ./requirements.txt requirements.txt

# Actualizamos la imagen, instalamos pip y lo actualizamos
# uso el parametro -y porque la construcción no es interactiva.
RUN apt-get update \
  && apt-get install -y python3-pip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

#Instala dependencias del proyecto
RUN pip install -r requirements.txt

EXPOSE 8989
# Comandos para ejecutar el servicio
# ENTRYPOINT indica que CMD se ejecuta sobre python
ENTRYPOINT ["python3"]
# ejecuta la app puerto 8989.
CMD gunicorn -b :8989 principal:app
