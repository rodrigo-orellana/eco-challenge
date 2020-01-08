from model import Desafio
from mongoDB import BaseDatos
import logging
import os

# Para el sistema de logs
logging.basicConfig(filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,  datefmt='%d-%b-%y %H:%M:%S')
#direccion = "mongodb://127.0.0.1:27017/MiBaseDatos"
mongo = BaseDatos("mongodb://127.0.0.1:27017/MiBaseDatos", True)

j1 = Desafio("Reciclaje2", '2019-06-26', '2020-06-26', "Chile", "Santiago")
j2 = Desafio("Bike2", '2019-08-26', '2020-06-26', "Chile", "Santiago")
j3 = Desafio("Limpia2", '2019-09-26', '2020-06-26', "Chile", "Santiago")

#mongo = BaseDatos(direccion, False)

mongo.insertDesafio(j1)
mongo.insertDesafio(j2)
mongo.insertDesafio(j3)

