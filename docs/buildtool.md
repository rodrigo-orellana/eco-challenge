## Herramienta de construcción
buildtool: Makefile  
Las herramientas de construcción se relacionan con lo que es necesario para construir todo un proyecto. Este proyecto utiliza [Make](https://es.wikipedia.org/wiki/Make). Esta herramienta de gestión de dependencias,permite en este caso instalar las dependencias del proyecto o gatillar la ejecucción de pruebas. Se crea el archivo [Makefile](https://github.com/rodrigo-orellana/eco-challenge/blob/master/Makefile) en el cual se indican las instrucciones a ejecutar por el programa make de acuerdo a los parametros que se le entreguen.  

Los objetivos configurados son los siguientes.  
*Instalación*  El siguente comando permite instalar todos los requisitos necesarios para la aplicación (dependencias). 
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
