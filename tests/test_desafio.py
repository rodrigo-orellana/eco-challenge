import unittest
import sys
sys.path.append('challenge')
from unittest.mock import MagicMock
from desafio import Desafio

import os
import logging


class TestModel(unittest.TestCase):

    def setUp(self):
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

        # Create a sample id:
        self.sample_id = '000000000000000000000000'
  
    def test_create_ok(self):
        """ Test if a new desafio is inserted on list """
        # Configure the mock for returning an id on insert, and None on get:
        self.mock.insert.return_value = self.sample_id
        self.mock.get.return_value = None

        id = self.desafio.create(
            self.sample_desafio["nombre"], self.sample_desafio["fecha_ini"], 
            self.sample_desafio["fecha_fin"], self.sample_desafio["pais"], 
            self.sample_desafio["ciudad"]
        )

        # Ensure that mock had been called with correct arguments:
        self.mock.insert.assert_called_with(self.sample_desafio)
        self.mock.get.assert_called_with(key='nombre', value=self.sample_desafio['nombre'])
        self.assertEqual(id, self.sample_id)

        
    def test_search_by_name(self):
        """ Test the search for existing and non-existing desafio by name """
        # Existing desafio:
        self.sample_desafio['_id'] = self.sample_id
        self.mock.get.return_value = self.sample_desafio

        res_found = self.desafio.search_by_name(self.sample_desafio["nombre"])
        self.assertEqual(res_found, self.sample_desafio)
        self.mock.get.assert_called_with(key='nombre', value=self.sample_desafio['nombre'])

        # Non-existing desafio:
        self.mock.get.return_value = None        
        
        res_not_found = self.desafio.search_by_name("Non-existing desafio")
        self.assertEqual(res_not_found, None)
        self.mock.get.assert_called_with(key='nombre', value="Non-existing desafio")

if __name__ == '__main__':
    unittest.main()
