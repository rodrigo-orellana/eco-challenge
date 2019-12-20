FROM frolvlad/alpine-python3:latest
LABEL maintainer="Rodrigo Orellana"

# Con esta imagen se supone que ya tenemos instalado python3 en Alpine

#Indicamos el directorio de trabajo de la imagen:
WORKDIR ~/ecochallenge/


#Copiamos los directorios necesarios para que funcione el servicio web.
COPY ./principal.py  principal.py
COPY ./mongoDB.py  mongoDB.py
COPY ./desafio.py  model.py
COPY ./competidor.py competidor.py
COPY ./requirements.txt requirements.txt

# Esto servirá para abrir el puerto 8989
EXPOSE 8989

# Instalamos las dependecias del servicio (Flask, Flask_restful, pymongo y gunicorn)
RUN pip3 install -r requirements.txt
# Ejecutamos el servicio
CMD gunicorn --workers=5 principal:app
