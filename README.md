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
1. Desafíos: Entidad que representa el desafío
2. Competidores: Entidad que representa a los usuarios que participan en el desafío
4. Auspiciadores: Entidad de representa a los auspiciadores que entregarán premios en en desafío

![Arquitectura](docs/images/arquitectura2.png "Arquitectura")

## Lenguaje
Los microservicios serán construidos en Python. Se ha elegido este lenguaje debido a lo simplificado, de rapido desarrollo y elegante. Ademas ofrece muchas librerías que puden resultar utilies en el desarrollo del proyecto

## Framework
Para Las APIs REST se usará Flask. Este microframework es ligero y de facil uso. Ademas cuenta con gran cantidad de material de apoyo existente en la red y ofrece facilidad de implementar scripts.
 
## Base de datos
Los microservicios utilizarán una base de datos MySQL para gestionar su información. Para la utilización de Mysql en python se utilizará el ORM SQLAlchemy. 

## Configuración distribuida
Como servicio de configuración distribuida se usará Consul que almacenará pares clave-valor y registrará los servicios.
 
## Servicios 
Cada microservicio generará log, para esto se usará logging y syslog para centralizar la información.



