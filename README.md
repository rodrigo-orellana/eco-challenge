![Eco Challenge](docs/images/eco.jpeg "Eco Challenge")
***
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)[![Build Status](https://travis-ci.org/rodrigo-orellana/eco-challenge.svg?branch=master)](https://travis-ci.org/rodrigo-orellana/eco-challenge)[![CircleCI](https://circleci.com/gh/rodrigo-orellana/eco-challenge.svg?style=svg)](https://circleci.com/gh/rodrigo-orellana/eco-challenge)  
Proyecto CC: Proyecto de curso CC asociado a la sustentabilidad ecológica
***
## Descripción del proyecto 
Este proyecto tiene por objetivo incentivar el tipo de vida sustentable con el medio ambiente generando conciencia y acciones pro ecología. Este sistema permitirá a los **organizadores** crear *Desafíos* ecológicos en los cuales de asociarán distintas *metas* las cuales entregarán *puntajes* a los **participantes** que se inscriban en el desafío. Tambien se podrán crear *eventos* en los cuales los usuarios que participen podran sumar puntaje. El sistema tendrá **Auspiciadores** los cuales podrán subir al sistema información asociada a *premios* o *descuentos* a los cuales las personas que cumplan el desafío podrán acceder.

## Arquitectura
La aplicación será desarrollada siguiendo una arquitectura de [microservicios](https://en.wikipedia.org/wiki/Microservices) 
Puedes ver la [documentación](https://github.com/rodrigo-orellana/eco-challenge/blob/master/docs/arquitectura.md) para más información

## Herraminetas
El desarrollo del proyecto utiliza Python3 venv con microframework Flask para la interfaz REST, base de datos NoSQL [MongoDB](https://www.mongodb.com). Para la utilización de la BD en python se usa [pymongo](https://api.mongodb.com/python/current/). 

Más información sobre lenguajes y tecnologías usadas en la [documentación](https://github.com/rodrigo-orellana/eco-challenge/blob/master/docs/herramientas.md)  

## Historias de usuario
Las historias de usuario que representan los requisitos de este proyecto son las siguientes agrupados por microservicio:
* [Microservicio Desafío](https://github.com/rodrigo-orellana/eco-challenge/milestone/7)
* [MongMicroservicio CompetidoroDB](https://github.com/rodrigo-orellana/eco-challenge/milestone/6)

## Integración continua
El objetivo implementa integración continua con Travis-CI y CircleCI . Más información ver la [documentación](https://github.com/rodrigo-orellana/eco-challenge/blob/master/docs/integracion_continua.md)

## Herramienta de construcción
buildtool: Makefile  
Este proyecto implementa un makefile como herramienta builtool, para más información puede consultar la [documentación](https://github.com/rodrigo-orellana/eco-challenge/blob/master/docs/buildtool.md)

## Test 
Para la automatización de los test se utiliza el framework de Python llamdo [Unittest](https://docs.python.org/3/library/unittest.html), para más información puede consultar la [documentación](https://github.com/rodrigo-orellana/eco-challenge/blob/master/docs/test.md)

## Virtualización sobre Docker
El concepto de [Docker](https://www.docker.com/) nace de la intención de poder administrar mejor los recursos de hardware (capacidad de computo), al virtualizar se crean pequeños ordenadores virtuales en los que se  distrubuyen los recursos, ademas de aislar las aplicaciones de otras que estén en el mismo servidor en distintas máquinas virtuales. En el caso de Docker, permite crear ambientes vittuales simplificados de pequeño tamaño, los que luego al desplegarse asegura que las pruebas realizadas en local se comportarán identicamente en el servidor de destino, al poseer una configuración que es exactamente la misma localmente y en la nube.  

Para la elección de la imagen de docker del proyecto creado en python se evalaron las siguientes caracteristicas:  
* **Imagen lijera:** La ventaja de una imágen pequeña apunta la rápides de extraer de la red y más rápidas de cargar en la memoria al iniciar el contenedor  
* **Actualizaciones de seguridad:** Conviene que la imagen esté bien mantenida, de modo que obtenga actualizaciones de seguridad para el sistema operativo base de manera oportuna.   

Las opciones analizadas
* **Alpine:** Esta imagen posee muchas recomandaciones en la comunidad de desarrolladores, debido a que tiene un pequeño peso (cercano a los 5 MB), aun siendo full distribución Linux.  
* **Ubuntu 18.04 (tag:18.04):** Esta versión 2018 de ubuntu tendrá actualizaciones de seguridad hasta el 2023. peso de 64 MB.  
* **Python:** El Docker oficial de Python, con buena aceptación en la comunidad pero con un elevado peso cercano a los 193MB (tag slim-buster). ofrece la ultima versión de Python.
* **jfloff/alpine-python** Imágen basada en Alpine, incluye python3-dev. el tag "latest-slim" tiene un peso de 83 MB incluyendo python.

De las opciones analizadas se opta por [jfloff/alpine-python](https://hub.docker.com/r/jfloff/alpine-python) el cual ademas de ligero, incluye python3.  

**Manos a la obra:** seguimos los siguientes pasos para la creación de nuestra imagen Docker de proyecto:  
Instalar Docker cliente -> Descargar Imagen -> instalar Python3 -> instalas pip3 -> Copiar fuentes proyecto -> instalar modulos python -> exponer los puertos -> Hacer ejecutable el Docker -> Crear Imagen Docker del proyecto
El siguiente es el Dockerfile del proyecto *debidamente comentado*:
~~~
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

# resuelve error de creación de imagen. instala gcc
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
# Instala las dependecias del servicio 
RUN pip install -r requirements.txt

# abrir el puerto 8989
EXPOSE 8989
# Comandos para ejecutar el servicio
# ENTRYPOINT indica que CMD se ejecuta sobre python
ENTRYPOINT ["python3"]
# ejecuta la app
CMD ["principal.py"]
~~~
creamos nuesta imagen:
~~~
docker build -t ecochallenge:3.0 .
~~~
ecochallenge es el nombre de la imagen y el 3.0 es el tag
Luego la ejecutamos
~~~
docker run -it -d -p 8989:8989 ecochallenge
~~~
Nuesta aplicación corre en el puerto 8989, se mapea desde el 8989.
La imagen creada
~~~
*docker images*
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
ecochallenge              3.0                 f4a8f83b9aa2        26 minutes ago      204MB

*docker ps*
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    
06ef3833dced        ecochallenge        "python3 principal.py"   15 minutes ago      Up 15 minutes       0.0.0.0:8989->8989/tcp   
~~~
Y desplegamos la imagen en hub docker, con *docker login* y luego:
~~~
docker tag f4a8f83b9aa2 rodrigoorellana/ecochallenge:3.0
docker push rodrigoorellana/ecochallenge
~~~
Acceso APP WEB
~~~
Contenedor: https://hub.docker.com/r/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Contenedor en Heroku: https:/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.herokuapp.com/news


http://localhost:8989                        -> indica status de la aplicación
https://ecochallenge.herokuapp.com/desafios  -> lista desafios de la BD
~~~

## Despliegue
[Despliegue:](https://ecochallenge.herokuapp.com/)  
El despliegue del servicio web se realiza en [Heroku](https://www.heroku.com), que nos ofrece una plataforma como un servicio ([PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service)) en la nube. Esto nos permite tener a nuestra disposición un servidor en el que poder desplegar nuestro proyecto en la nube de forma gratuita, vinculando nuestra cuenta de github permite realizar el despligue de nuestro servicio automaticamente una vez finalizas correctamente nuestro set de pruebas de TRAVIS. Heroku utiliza nuestro archivo de rependencias [requirements.txt](https://github.com/rodrigo-orellana/eco-challenge/blob/master/requirements.txt) para nuestra aplicación, de la siguiente manera:  
~~~
pip install -r requirements.txt
~~~
Ademas el indicamos en el archivo [runtime.txt](https://github.com/rodrigo-orellana/eco-challenge/blob/master/runtime.txt) la versión de python a utilizar (3.7.3). Finalmente le indicamos en el archivo [Procfile](https://github.com/rodrigo-orellana/eco-challenge/blob/master/Procfile) el comando que será ejecutado al iniciar la aplicación, en este caso indicamos nuestro web server
 ~~~
 web: gunicorn principal:app
 ~~~

## Arquitectura en capas de microservicios
La arquitectura de este microservicio está compuesta por tres capas:

**servicio:** interfaz de acceso al microservicio: principal.py
**negocio:** ejecuta subrutinas y acciones de los usuarios: desafio.py
**BD:** ejecuta comunicación con BD: mongoDB.py