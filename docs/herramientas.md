## Herraminetas
El desarrollo del proyecto utiliza Python más: Flask para la interfaz REST, MongoDB como bases de datos
* **Lenguajes:** Los microservicios están construidos en Python3 venv como entorno virtual para el desarollo y ejecucción de los microservicios. Las APIs REST se construirán usarndo Flask. Este microframework es ligero y de facil uso. Ademas cuenta con gran cantidad de material de apoyo existente en la red.
* **Base de datos:** Se hace uso de una base de datos NoSQL [MongoDB](https://www.mongodb.com) para el almacenamiento información. Para la utilización de la BD en python se usa [pymongo](https://api.mongodb.com/python/current/).
* **Test:** Se realizar un desarrollo basado en pruebas con Unittest para Python. Además en cada actualización del repositorio de Github se ejecutan los tests de Unittest.
* **Servicios:** Cada microservicio generará log, para esto se usa logging.