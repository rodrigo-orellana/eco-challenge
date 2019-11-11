![Eco Challenge](docs/images/eco.jpeg "Eco Challenge")
***
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)[![Build Status](https://travis-ci.org/rodrigo-orellana/eco-challenge.svg?branch=master)](https://travis-ci.org/rodrigo-orellana/eco-challenge)
Proyecto CC: Proyecto de curso CC asociado a la sustentabilidad ecológica
***
## Descripción del proyecto 
Este proyecto tiene por objetivo incentivar el tipo de vida sustentable con el medio ambiente generando conciencia y acciones pro ecología. Este sistema permitirá a los **organizadores** crear *Desafíos* ecológicos en los cuales de asociarán distintas *metas* las cuales entregarán *puntajes* a los **participantes** que se inscriban en el desafío. Tambien se podrán crear *eventos* en los cuales los usuarios que participen podran sumar puntaje. El sistema tendrá **Auspiciadores** los cuales podrán subir al sistema información asociada a *premios* o *descuentos* a los cuales las personas que cumplan el desafío podrán acceder.

## Arquitectura
La aplicación será desarrollada siguiendo una arquitectura de [microservicios](https://en.wikipedia.org/wiki/Microservices) debido a que a pesar que una solución monolitica sería mas simple de implementar, en el tiempo al requerir escabilidad crecen funcionalidad se vuelven complejas de mantener y desplegar. Las arquitecturas basadas en microservicios permiten un crecimiento escalable simple y logicamente aislado. Las peticiones de información o de ingreso de esta serán recibidas por un API Gateway. Dicho Gateway enrutará las peticiones al microservicio que corresponda. 
Se construirán los siguientes microservicios:
1. Desafíos: Entidad que representa el desafío
2. Competidores: Entidad que representa a los usuarios que participan en el desafío
4. Auspiciadores: Entidad de representa a los auspiciadores que entregarán premios en en desafío

![Arquitectura](docs/images/arquitectura2.png "Arquitectura")

## Herraminetas
* **Lenguajes:** Los microservicios están construidos en Python3 virtualenv como entorno virtual para el desarollo local de los microservicios. Las APIs REST se construirán usarndo Flask. Este microframework es ligero y de facil uso. Ademas cuenta con gran cantidad de material de apoyo existente en la red. Esto se ejecutará en un entorno virtual con pyvenv.
* **Base de datos:** Se hace uso de una base de datos NoSQL [MongoDB](https://www.mongodb.com) para el almacenamiento información. Para la utilización de la BD en python se usa [pymongo](https://api.mongodb.com/python/current/).
* **Comunicación:** Para la comunicación de los microservicios se usará el broker [RabbitMQ](https://www.rabbitmq.com/).
* **Test:** Se realizar un desarrollo basado en pruebas con Unittest para Python. Además en cada actualización del repositorio de Github se ejecutan los tests de Unittest.
* **Servicios:** Cada microservicio generará log, para esto se usará logging y syslog para centralizar la información.

## Historias de usuario
Las historias de usuario que representan los requisitos de este proyecto son las siguientes agrupados por microservicio:
* [Microservicio Desafío](https://github.com/rodrigo-orellana/eco-challenge/milestone/7)
* [MongMicroservicio CompetidoroDB](https://github.com/rodrigo-orellana/eco-challenge/milestone/6)

## Integración continua
El objetivo de implementar el proyecto con integración continua es realizar integraciones automáticas lo más a menudo posible para así poder detectar fallos cuanto antes. En este proyecto se usa [Travis](https://travis-ci.org) que permite instalar todas las dependencias y ejecutar los test (desarrollados con unitTest) de manera automatica en cada actualización realizada sobre nuestro repositorio github. Tambien permite comprobar el funcionamiento correcto de nuestros tests en diversas versiones de Python 
 Para habilitarlo se siguien los siguientes pasos:  
1. Subir los fuentes y los test en el repositorio.
2. Vincular nuestra cuenta de GitHub a Travis en el [sitio oficial](https://travis-ci.org)
3. Indicar a Travis el repositorio que queremos que Travis ejecute los test.
4. Crear y subir al repositorio el archivo de configuración [.travis.yml](https://github.com/rodrigo-orellana/eco-challenge/blob/master/.travis.yml) 
5. Crear archivo de dependencias [requirements.txt](https://github.com/rodrigo-orellana/eco-challenge/blob/master/requirements.txt)  

Travis ademas permite comprobar la compatibilidad del sistema que se está desarrollando en las versiones que se le especifique del lengueje de programación.  
Más información ver la [documentación](https://github.com/rodrigo-orellana/eco-challenge/docs/integracion_continua.md)

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
