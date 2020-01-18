import unittest
# agregamos la ruta donde estan los fuentes del proyecto
import sys
#sys.path.append('challenge')
sys.path.append('src/desafios')

# se agrega MagicMock para simular pruebas con independencia de la BD
from unittest.mock import MagicMock
from desafio import Desafio

import os
import logging


class TestDesafio(unittest.TestCase):

    def setUp(self):
        """DATOS DE PRUEBA """
        #  uso de MOCK para simular conexion BD
        self.mock = MagicMock()
        # crea instancia
        self.desafio = Desafio(data_access=self.mock)

        # asigna datos:
        self.sample_desafio = dict(
            nombre="Reciclaje_test0001",
            fecha_ini='2019-06-26',
            fecha_fin='2019-06-26',
            pais="Chile",
            ciudad="Santiago", 
        )

        # crea un id simulando respuesta de BD
        self.sample_id = '5dfeb37bd6910141030af17e'

        # asigna datos:
        self.sample_desafio = dict(
            nombre="Reciclaje_test0002",
            fecha_ini='2019-06-26',
            fecha_fin='2019-06-26',
            pais="Chile",
            ciudad="Santiago", 
        )

        # crea un id simulando respuesta de BD
        self.sample_id = '1dfeb37bd6910141030af17e'
    # TEST de creación de objeto en BD
    def test_insert(self):
        # Indicamos al mock que devolver en un get
        self.mock.get.return_value = None
        # Indicamos al mock que devolver en un insert
        self.mock.insert.return_value = self.sample_id
        # probando insert
        id_insert_test = self.desafio.create(
            self.sample_desafio["nombre"], self.sample_desafio["fecha_ini"], 
            self.sample_desafio["fecha_fin"], self.sample_desafio["pais"], 
            self.sample_desafio["ciudad"]
        )

        # validando insert
        self.mock.insert.assert_called_with(self.sample_desafio)
        # validando get
        self.mock.get.assert_called_with(key='nombre', value=self.sample_desafio['nombre'])
        # el id debe ser el insertado
        self.assertEqual(id_insert_test, self.sample_id)
    #Validamos que no inserte duplicados
    def test_duplicado(self):
        # Indicamos al mock que devolver en un get
        self.mock.get.return_value = self.sample_id
        self.search_by_name = "Reciclaje_test0001"
        # Indicamos al mock que devolver en un insert
        self.mock.insert.return_value = self.sample_id
        # insertando el duplicado
        with self.assertRaises(ValueError):
            # esto fallará con raise
            id_insert_test = self.desafio.create(
                self.sample_desafio["nombre"], self.sample_desafio["fecha_ini"], 
                self.sample_desafio["fecha_fin"], self.sample_desafio["pais"], 
                self.sample_desafio["ciudad"]
            )
        # validando que no ejecutó el insert
        self.mock.insert.assert_not_called()

    # TEST de busqueda de objetos
    def test_metodos_search(self):
        # Prepadando prueba, inicio de valores:
        self.sample_desafio['_id'] = self.sample_id
        self.mock.get.return_value = self.sample_desafio
        # Ejecucción de prueba: search_by_name
        objeto_encontrado = self.desafio.search_by_name(self.sample_desafio["nombre"])
        self.assertEqual(objeto_encontrado, self.sample_desafio)
        self.mock.get.assert_called_with(key='nombre', value=self.sample_desafio['nombre'])

        # Prueba de valor no encontrado
        self.mock.get.return_value = None        
        
        test_found = self.desafio.search_by_name("__ESTE_VALOR_NO_EXISTE__")
        self.assertEqual(test_found, None)
        self.mock.get.assert_called_with(key='nombre', value="__ESTE_VALOR_NO_EXISTE__")

if __name__ == '__main__':
    unittest.main()
