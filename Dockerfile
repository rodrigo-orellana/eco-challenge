FROM frolvlad/alpine-python3:latest
LABEL maintainer="Rodrigo Orellana"

# Con esta imagen ya tenemos instalado python3 en Alpine

# Carga archivo de requerimientos 
ADD ./requirements.txt /tmp/requirements.txt

# Instala requerimientos
RUN pip3 install -qr /tmp/requirements.txt

# sube ficheros fuente
ADD ./challenge opt/webapp/

# Indicamos el directorio de trabajo de la imagen
WORKDIR /opt/webapp

# Esto informa uso  del puerto 8989.
EXPOSE ${PORT}

#CMD python3 principal.py 

#Para que no se ejecute como root
#RUN useradd -m userapp
#USER userapp

#CMD gunicorn --workers=5 principal:app
CMD gunicorn --workers=5 --bind 0.0.0.0:${PORT} principal:app
