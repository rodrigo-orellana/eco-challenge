import unittest
import sys
sys.path.append('challenge')
import Desafio


class TestModel(unittest.TestCase):

    def setUp(self):
        self.prueba1 = Desafio("Reciclaje", '2019-06-26',
                               '2020-06-26', "Chile", "Santiago")
        self.prueba2 = Desafio("Reciclaje", '2019-06-26',
                               '2020-06-26', "Chile", "Santiago")

    def testTipoCreacion(self):
        self.assertIsInstance(self.prueba1, Desafio,
                              "Tipo de objeto jugador incorrecto.")

    def testUnicidad(self):
        self.assertIsNot(self.prueba1, self.prueba2,
                         "Dos objetos con los mismos atributos no pueden ser el mismo.")

if __name__ == '__main__':
    unittest.main()
