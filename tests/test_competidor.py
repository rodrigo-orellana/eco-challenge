import unittest
import sys
import random
sys.path.append('challenge')

from competidor import Competidor
from mongoDB import BaseDatos
import os
import logging

user = os.environ.get("USER_MBD")
passw = os.environ.get("PASS_MBD")
ambiente = os.environ.get("AMBIENTE")
if ambiente != "localhost":
    logging.info("base de datos cloud"+str(ambiente))
    mongo = BaseDatos(
        "mongodb+srv://"+str(user)+":"+str(passw)+"@cluster0-qazzt.mongodb.net/desafio?retryWrites=true&w=majority", False)
else:
    logging.info("base de datos local")
    mongo = BaseDatos("mongodb://127.0.0.1:27017/MiBaseDatos", True)

# inyeccion de dependencia
competidor_data = Competidor(data_access=mongo)

class TestModel(unittest.TestCase):

    def setUp(self):
        self.prueba1 = competidor_data.create("Sebastian Test1"+str(random.uniform(1, 1000)), '2019-06-26',
                               "60","Masculino" , "Chile", "Santiago")
        self.prueba2 = competidor_data.create("Juan Test2"+str(random.uniform(1, 1000)), '2019-06-26',
                               "70","Masculino" , "España", "Madrid")

    def testTipoCreacion(self):
        self.assertIsNotNone(self.prueba1,
                              "Tipo de objeto competidor incorrecto.")
    def testTipoCreacion2(self):
        self.assertIsNotNone(self.prueba2,
                              "Tipo de objeto competidor incorrecto.")


if __name__ == '__main__':
    unittest.main()
