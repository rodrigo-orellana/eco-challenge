![Eco Challenge](docs/images/eco.jpeg "Eco Challenge")
***
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
Proyecto CC: Proyecto de curso CC asociado a la sustentabilidad ecológica
***
## Descripción del proyecto 
Este proyecto tiene por objetivo incentivar el tipo de vida sustentable con el medio ambiente generando conciencia y acciones pro ecología. Este sistema permitirá a los **organizadores** crear *Desafíos* ecológicos en los cuales de asociarán distintas *metas* las cuales entregarán *puntajes* a los **participantes** que se inscriban en el desafío. Tambien se podrán crear *eventos* en los cuales los usuarios que participen podran sumar puntaje. El sistema tendrá **Auspiciadores** los cuales podrán subir al sistema información asociada a *premios* o *descuentos* a los cuales las personas que cumplan el desafío podrán acceder.

## Alcance
El alcance del proyecto es la construcción del backend del sistema. Para esta versión solo podrá estar activo un desafío en un período de tiempo.

## Arquitectura
La aplicación será desarrollada siguiendo una arquitectura de [microservicios](https://en.wikipedia.org/wiki/Microservices) debido a que a pesar que una solución monolitica sería mas simple de implementar, en el tiempo al requerir escabilidad crecen funcionalidad se vuelven complejas de mantener y desplegar. Las arquitecturas basadas en microservicios permiten un crecimiento escalable simple y logicamente aislado. Las peticiones de información o de ingreso de esta serán recibidas por un API Gateway REST utilizando JSON. Dicho Gateway enrutará las peticiones al microservicio que corresponda. 
Se construirán los siguientes microservicios:
1. Desafíos: Crea/consulta Desafíos con sus respectivas metas
2. Score: Corresponde a la entidad encargada de administrar los puntajes de los participantes. Este microservicios expondrá una interfaz en la cual se informará nuevos puntajes a asignar a un usuario. Tambien se podrá consultar el puntaje acomulado en el desafío en curso.
3. Premio: Microservicio encargado de la gestión de premios
4. Resultados: Microservicio encargado de una vez finalizado el desafío generar los resultados

<center>docs/images/backend.png</center>

## Lenguaje
Los microservicios serán construidos en Python. Se ha elegido este lenguaje debido a lo simplificado, de rapido desarrollo y elegante. Ademas ofrece muchas librerías que puden resultar utilies en el desarrollo del proyecto

## Framework
Para Las APIs REST se usará Flask. Este microframework es ligero y de facil uso. Ademas cuenta con gran cantidad de material de apoyo existente en la red y ofrece facilidad de implementar scripts.
 
## Base de datos
EL microservicio resultados utilizará una base de datos MySQL para gestionar y consultar mejor los datos de tipo DATE. El resto de los servicios usará una BD MongoDB. Para la utilización de Mysql en python se utilizará el ORM SQLAlchemy. Para MongoDB se utilizará MongoEngine.

## Configuración distribuida
Como servicio de configuración distribuida se usará Consul que almacenará pares clave-valor y registrará los servicios.

## Comunicación
Los microservicios se comunicarán mediante envío de mensajes REST JSON.
 
## Test
Para el desarrollo basado en test se aplicarán distintas pruebas en cada microservicio usando [PyTest](https://docs.pytest.org/en/latest/). 
 
## Servicios 
Cada microservicio generará log, para esto se usará logging y syslog para centralizar la información.


