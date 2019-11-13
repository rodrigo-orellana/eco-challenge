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
El desarrollo del proyecto utiliza Python3 virtualen con microframework Flask para la interfaz REST, base de datos NoSQL [MongoDB](https://www.mongodb.com). Para la utilización de la BD en python se usa [pymongo](https://api.mongodb.com/python/current/). 

Más información sobre lenguajes y tecnologías usadas en la [documentación](https://github.com/rodrigo-orellana/eco-challenge/blob/master/docs/arquitectura.md)  

## Historias de usuario
Las historias de usuario que representan los requisitos de este proyecto son las siguientes agrupados por microservicio:
* [Microservicio Desafío](https://github.com/rodrigo-orellana/eco-challenge/milestone/7)
* [MongMicroservicio CompetidoroDB](https://github.com/rodrigo-orellana/eco-challenge/milestone/6)

## Integración continua
El objetivo de implementar el proyecto con integración continua es realizar integraciones automáticas lo más a menudo posible para así poder detectar fallos cuanto antes. Este proyecto utiliza dos sistemas de CI:

**[Travis](https://travis-ci.org)** Permite instalar todas las dependencias y ejecutar los test (desarrollados con unitTest) de manera automatica en cada actualización realizada sobre nuestro repositorio github. Tambien permite comprobar el funcionamiento correcto de nuestros tests en diversas versiones de Python 
 Para habilitarlo se siguien los siguientes pasos:  
1. Subir los fuentes y los test en el repositorio.
2. Vincular nuestra cuenta de GitHub a Travis en el [sitio oficial](https://travis-ci.org)
3. Indicar a Travis el repositorio que queremos que Travis ejecute los test.
4. Crear y subir al repositorio el archivo de configuración [.travis.yml](https://github.com/rodrigo-orellana/eco-challenge/blob/master/.travis.yml) 
5. Crear archivo de dependencias [requirements.txt](https://github.com/rodrigo-orellana/eco-challenge/blob/master/requirements.txt)  

Travis ademas permite comprobar la compatibilidad del sistema que se está desarrollando en las versiones que se le especifique del lengueje de programación.  
Más información ver la [documentación](https://github.com/rodrigo-orellana/eco-challenge/blob/master/docs/integracion_continua.md)

**[CircleCI](https://circleci.com/)** Permite una rapida configuración. Primero se hace el emparejamiento con la  cuenta GitHub luego se crea el fichero de configuración yml.
 Para habilitarlo se siguien los siguientes pasos:  
1. Subir los fuentes y los test en el repositorio.
2. Vincular nuestra cuenta de GitHub a CircleCI en el [sitio oficial](https://circleci.com/)
3. Crear y subir al repositorio el archivo de configuración [.circleci/config.yml](https://github.com/rodrigo-orellana/eco-challenge/blob/master/.circleci/config.yml) 

## Herramienta de construcción
buildtool: Makefile  
Las herramientas de construcción se relacionan con lo que es necesario para construir todo un proyecto. Este proyecto utiliza [Make](https://es.wikipedia.org/wiki/Make). Esta herramienta de gestión de dependencias,permite en este caso instalar las dependencias del proyecto o gatillar la ejecucción de pruebas. Se crea el archivo [Makefile](https://github.com/rodrigo-orellana/eco-challenge/blob/master/Makefile) en el cual se indican las instrucciones a ejecutar por el programa make de acuerdo a los parametros que se le entreguen.  

Los objetivos configurados son los siguientes.  
*Instalación*  El siguente comando permite instalar todos los requisitos necesarios para la aplicación. 
~~~
make install
~~~
Esté comando ejecutará la siguiente instrucción, en donde recive como parametro [requirements.txt](https://github.com/rodrigo-orellana/eco-challenge/blob/master/requirements.txt)
~~~
pip install -r requirements.txt.
~~~

*Test* Tambien permite ejecutar los tests del proyecto con el siguiente comando.
~~~
make test
~~~
Esté comando ejecutará la siguiente instrucción
~~~
python -m unittest discover tests
~~~
Unitest será detallado en el punto siguiente. Discover permite indicar a unittest que busque los test, en este caso en el directorio "tests"

## TEST 
Para la automatización de los test se utiliza el framework de Python llamdo [Unittest](https://docs.python.org/3/library/unittest.html), el cual está inspirado en [JUnit](https://es.wikipedia.org/wiki/JUnit). Este framework permite hacer uso de varias funciones del tipo "assert" (afirmaciones) que evalua los casos de prueba entregados como parametro. Para la ejecucción de los test, se puede utilizar el programa make descrito en el punto anterior. La ejecucción de los test se realiza de la siguiente forma:
~~~
python -m unittest discover tests
~~~
Discover permite indicar a unittest que busque los test, en este caso en el directorio "tests" para más información dejo el siguiente [link](https://work.njae.me.uk/2018/04/05/testing/)


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
