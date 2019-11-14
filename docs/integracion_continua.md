## Integración continua
**[Travis](https://travis-ci.org)** Se utiliza Travis-CI para la implementación de la integración continua. Los siguientes son los pasos para su configuración:
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

**[CircleCI](https://circleci.com/)** Permite una rapida configuración. Primero se hace el emparejamiento con la  cuenta GitHub luego se crea el fichero de configuración yml.
 Para habilitarlo se siguien los siguientes pasos:  
1. Subir los fuentes y los test en el repositorio.
2. Vincular nuestra cuenta de GitHub a CircleCI en el [sitio oficial](https://circleci.com/)
3. Crear y subir al repositorio el archivo de configuración [.circleci/config.yml](https://github.com/rodrigo-orellana/eco-challenge/blob/master/.circleci/config.yml) 
El archivo de configuración posee la siguiente estructura (propuesta por CircleCI al enlazar el repositorio) en donde agregamos nuestros comandos para creación de entorno virtual para python, y los "make" para la instalación y los test
~~~
version: 2
jobs:
  build:
    docker:
      - image: circleci/python:3.7
    steps:
      - checkout
      - run:
          name: virtualiza python3
          command: python3 -m venv venv
      - run:
          name: Dependencias del proyecto
          command: |
            . venv/bin/activate 
            make install
      - run:
          name: Test unittest
          command: |
            . venv/bin/activate 
            make test
~~~ 

resultado de CircleCI del ultimo despliegue:  
[![CircleCI](https://circleci.com/gh/rodrigo-orellana/eco-challenge.svg?style=svg)](https://circleci.com/gh/rodrigo-orellana/eco-challenge)  