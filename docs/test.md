## Test 
Para la automatización de los test se utiliza el framework de Python llamdo [Unittest](https://docs.python.org/3/library/unittest.html), el cual está inspirado en [JUnit](https://es.wikipedia.org/wiki/JUnit). Este framework permite hacer uso de varias funciones del tipo "assert" (afirmaciones) que evalua los casos de prueba entregados como parametro. Para la ejecucción de los test, se puede utilizar el programa make descrito en el punto anterior. La ejecucción de los test se realiza de la siguiente forma:
~~~
python -m unittest discover tests
~~~
Discover permite indicar a unittest que busque los scripts de test, en este caso en el directorio "tests" para más información dejo el siguiente [link](https://work.njae.me.uk/2018/04/05/testing/)
