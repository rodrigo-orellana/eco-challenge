import unittest
import sys
sys.path.append("src")
from competidor import Competidor


class TestModel(unittest.TestCase):

    def setUp(self):
        self.prueba1 = Competidor("Sebastian Piñera", '2019-06-26',
                               "60","Masculino" , "Chile", "Santiago")
        self.prueba2 = Competidor("Juan Carlos", '2019-06-26',
                               "70","Masculino" , "España", "Madrid")

    def testTipoCreacion(self):
        self.assertIsInstance(self.prueba1, Competidor,
                              "Tipo de objeto jugador incorrecto.")

    def testUnicidad(self):
        self.assertIsNot(self.prueba1, self.prueba2,
                         "Dos objetos con los mismos atributos no pueden ser el mismo.")

if __name__ == '__main__':
    unittest.main()
