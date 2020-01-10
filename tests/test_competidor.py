import unittest
import sys
sys.path.append('challenge')
from unittest.mock import MagicMock
from competidor import Competidor

import os
import logging


class TestModel(unittest.TestCase):

    def setUp(self):
        #  uso de MOCK para simular conexion BD
        self.mock = MagicMock()
        # crea instancia
        self.competidor = Competidor(data_access=self.mock)

        # asigna datos:
        self.sample_competidor = dict(
            nombre="Juan_test0001",
            fecha_ins='2019-06-26',
            edad="38",
            sexo="MASCULINO",
            pais="Chile",
            ciudad="Santiago" 
        )

        # Create a sample id:
        self.sample_id = '000000000000000000000000'
  
    def test_create_ok(self):
        """ Test if a new competidor is inserted on list """
        # Configure the mock for returning an id on insert, and None on get:
        self.mock.insert.return_value = self.sample_id
        self.mock.get.return_value = None

        id = self.competidor.create(
            self.sample_competidor["nombre"], self.sample_competidor["fecha_ins"], 
            self.sample_competidor["edad"], self.sample_competidor["sexo"], 
            self.sample_competidor["pais"], self.sample_competidor["ciudad"]
        )

        # Ensure that mock had been called with correct arguments:
        self.mock.insert.assert_called_with(self.sample_competidor)
        self.mock.get.assert_called_with(key='nombre', value=self.sample_competidor['nombre'])
        self.assertEqual(id, self.sample_id)

        
    def test_search_by_name(self):
        """ Test the search for existing and non-existing competidor by name """
        # Existing competidor:
        self.sample_competidor['_id'] = self.sample_id
        self.mock.get.return_value = self.sample_competidor

        res_found = self.competidor.search_by_name(self.sample_competidor["nombre"])
        self.assertEqual(res_found, self.sample_competidor)
        self.mock.get.assert_called_with(key='nombre', value=self.sample_competidor['nombre'])

        # Non-existing competidor:
        self.mock.get.return_value = None        
        
        res_not_found = self.competidor.search_by_name("Non-existing competidor")
        self.assertEqual(res_not_found, None)
        self.mock.get.assert_called_with(key='nombre', value="Non-existing competidor")

if __name__ == '__main__':
    unittest.main()

     
