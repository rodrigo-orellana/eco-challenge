FROM sanicframework/sanic:LTS
#FROM frolvlad/alpine-python3:latest
# instrucción informativa
LABEL maintainer="Rodrigo Orellana"

# Con esta imagen ya tenemos instalado python3 en Alpine

# Carga archivo de requerimientos 
#ADD ./requirements.txt /tmp/requirements.txt

# Instala requerimientos
#RUN pip install -r /tmp/requirements.txt

# Instalar python3
# Atualizar pip e instalar las dependencias. No usamos el requirements.txt porque
# contiene módulos que no son necesarios en el contenedor. Además indicamos que no use la caché.
RUN python3 -m pip install --no-cache-dir --upgrade pip \
    && python3 -m pip install --no-cache-dir dnspython \
    pymongo

# sube ficheros fuente
ADD ./src/desafios /opt/webapp/

# Indicamos el directorio de trabajo de la imagen
WORKDIR /opt/webapp

# Esto informa uso  del puerto 8989.
EXPOSE ${PORT}

# Ejecuta comando para levantar webapp
#CMD gunicorn --workers=5 --bind 0.0.0.0:${PORT} wsgi:app
CMD python3 sanic_rest.py
