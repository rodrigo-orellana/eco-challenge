import unittest
import sys
import random
sys.path.append('challenge')

from desafio import Desafio
from mongoDB import BaseDatos
import os
import logging

user = os.environ.get("USER_MBD")
passw = os.environ.get("PASS_MBD")
ambiente = os.environ.get("AMBIENTE")
if ambiente != "localhost":
    logging.info("base de datos cloud"+str(ambiente))
    mongo = BaseDatos(
        "mongodb+srv://"+str(user)+":"+str(passw)+"@cluster0-qazzt.mongodb.net/desafio?retryWrites=true&w=majority", False, "desafio")
else:
    logging.info("base de datos local")
    mongo = BaseDatos("mongodb://127.0.0.1:27017/MiBaseDatos", True, "desafio")

# inyeccion de dependencia
desafio_data = Desafio(data_access=mongo)

class TestModel(unittest.TestCase):

    def setUp(self):
        self.prueba1 = desafio_data.create("Reciclaje"+str(random.uniform(1, 1000)), '2019-06-26',
                               '2020-06-26', "Chile", "Santiago")
        self.prueba2 = desafio_data.create("Reciclaje2"+str(random.uniform(1, 1000)), '2020-06-26',
                               '2021-06-26', "Chile", "Santiago")

    def testTipoCreacion(self):
        self.assertIsNotNone(self.prueba1,
                              "Tipo de objeto desafio incorrecto.")
    def testTipoCreacion2(self):
        self.assertIsNotNone(self.prueba2,
                              "Tipo de objeto desafio incorrecto.")


if __name__ == '__main__':
    unittest.main()
