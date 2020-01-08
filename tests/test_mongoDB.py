import sys
sys.path.append("../")

import unittest
from desafio import Desafio
from mongoDB import BaseDatos
import pymongo

class TestModel(unittest.TestCase):
	#Definimos datos de prueba
    def setUp(self):
        self.mongo = BaseDatos("mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/desafio?retryWrites=true&w=majority",True)
		#BaseDatos("mongodb://127.0.0.1:27017/MiBaseDatos",True)
        self.mongo.removeDesafios()
        self.prueba = Desafio("Ejemplo", '2019-06-26',
                               '2020-06-26', "Chile", "Santiago")

    def test1UpdateDesafio(self):
        self.mongo.insertDesafio(self.prueba)
        self.assertEqual(self.mongo.getSize(), 1, "El número de documentos dentro de la base de datos debería ser 1 en este punto.")
        updates= {'pais':'Ejemplo_Update'}
        self.mongo.updateDesafio("Ejemplo",updates)
        self.assertEqual(self.mongo.getDesafio("Ejemplo")['pais'],'Ejemplo_Update',"El Nombre de la entrada de ejemplo no se ha actualizado correctamente")
        self.mongo.removeDesafio("Ejemplo")
		
	#Valida que los elementos se almacenen correctamente en la BD
    def test2Tipo(self):
        self.mongo.insertDesafio(self.prueba)
        self.assertIsInstance(self.mongo.getDesafio("Ejemplo"),dict,"El elemento sacado desde la base de datos no es un diccionario.")
        self.mongo.removeDesafio("Ejemplo")
        self.assertEqual(self.mongo.getSize(), 0, "La base de datos debería de estar vacía en este punto.")		
	
	#Valida que los elementos se obtengas completos del la BD
    def test3GetDesafio(self):
        diccionario = self.prueba.__dict__()
        self.mongo.insertDesafio(self.prueba)
        self.assertEqual(self.mongo.getDesafio("Ejemplo"),diccionario,"El Desafio Ejemplo no se ha obtenido correctamente de la base de datos.")
        self.mongo.removeDesafio("Ejemplo")
        self.assertEqual(self.mongo.getSize(), 0, "La base de datos debería de estar vacía en este punto.")		

    def test4GetDesafioInsertRemoveAllSize(self):
        prueba2 = Desafio("Ejemplo2", '2019-06-26',
                               '2020-06-26', "Chile", "Santiago")
        self.mongo.insertDesafio(self.prueba)
        self.mongo.insertDesafio(prueba2)
        self.assertEqual(self.mongo.getSize(),2,"Se esperaban un total de 2 documentos en la BD.")
        salida=self.mongo.getDesafios()
        self.assertEqual(salida["Ejemplo"],self.prueba.__dict__(),"El primer ejemplo no se ha insertado correctamente.")
        self.assertEqual(salida["Ejemplo2"],prueba2.__dict__(),"El segundo ejemplo no se ha insertado correctamente")
        self.mongo.removeDesafios()
        self.assertEqual(self.mongo.getSize(),0,"No se han eliminó todos los documentos de la BD.")

    def test5RemoveDesafio(self):
        self.mongo.insertDesafio(self.prueba)
        self.assertEqual(self.mongo.getSize(), 1, "El número de documentos dentro de la base de datos debería ser 1 en este punto.")
        self.mongo.removeDesafio("Ejemplo")
        self.assertEqual(self.mongo.getSize(), 0, "La base de datos debería de estar vacía en este punto.")

    def test6InsertarDosIguales(self):
        self.mongo.insertDesafio(self.prueba)
        self.assertEqual(self.mongo.getSize(), 1, "El número de documentos dentro de la base de datos debería ser 1 en este punto.")
        self.mongo.insertDesafio(self.prueba)
        self.assertEqual(self.mongo.getSize(), 1, "El número de documentos dentro de la base de datos debería seguir siendo 1 en este punto.")
        self.mongo.removeDesafios()
        self.assertEqual(self.mongo.getSize(), 0, "La base de datos debería de estar vacía en este punto.")


if __name__ == '__main__':
    unittest.main()
