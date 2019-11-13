## Herraminetas
El desarrollo del proyecto utiliza Python más: - Flask para la interfaz REST - Celery para gestionar los eventos - MySQL y MongoDB como bases de datos - Consul para la configuración distribuida

Más información sobre lenguajes y tecnologías usadas.
* **Lenguajes:** Los microservicios están construidos en Python3 virtualenv como entorno virtual para el desarollo local de los microservicios. Las APIs REST se construirán usarndo Flask. Este microframework es ligero y de facil uso. Ademas cuenta con gran cantidad de material de apoyo existente en la red. Esto se ejecutará en un entorno virtual con pyvenv.
* **Base de datos:** Se hace uso de una base de datos NoSQL [MongoDB](https://www.mongodb.com) para el almacenamiento información. Para la utilización de la BD en python se usa [pymongo](https://api.mongodb.com/python/current/).
* **Comunicación:** Para la comunicación de los microservicios se usará el broker [RabbitMQ](https://www.rabbitmq.com/).
* **Test:** Se realizar un desarrollo basado en pruebas con Unittest para Python. Además en cada actualización del repositorio de Github se ejecutan los tests de Unittest.
* **Servicios:** Cada microservicio generará log, para esto se usará logging y syslog para centralizar la información.