## Integración continua
Se utiliza Travis-CI para la implementación de la integración continua. Los siguientes son los pasos para su configuración:
1. Subir los fuentes y los test en el repositorio.
2. Vincular nuestra cuenta de GitHub a Travis en el [sitio oficial](https://travis-ci.org)
3. Indicar a Travis el repositorio que queremos que Travis ejecute los test.
4. Crear y subir al repositorio el archivo de configuración [.travis.yml](https://github.com/rodrigo-orellana/eco-challenge/blob/master/.travis.yml):  
5. Crear archivo de dependencias [requirements.txt]  (https://github.com/rodrigo-orellana/eco-challenge/blob/master/requirements.txt)  
~~~
language: python
python:
  - "3.7.3"
# command to install dependencies
install:
  - pip install -r requirements.txt
# Services for Travis
services: mongodb
#Variables de entorno
env:
  - TRAVIS=yes
# command to run tests
script:
  - python -m unittest discover tests
~~~  

Aqui se indicar el lenguaje y versión. Luego se indica como realizar la instalación de las despendencias. Por último ejecuta los test. Luego en cada actualización de codigo se ejecutarán los test de manera automatica. El siguiente indicador entrega información del resultado de Travis del ultimo despliegue:  
[![Build Status](https://travis-ci.org/rodrigo-orellana/eco-challenge.svg?branch=master)](https://travis-ci.org/rodrigo-orellana/eco-challenge)  

