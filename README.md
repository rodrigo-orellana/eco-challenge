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
Para la automatización de los test se utiliza el framework de Python llamdo [Unittest](https://docs.python.org/3/library/unittest.html), para más información puede consultar la [documentación](https://github.com/rodrigo-orellana/eco-challenge/blob/master/docs/buildtool.md)

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
