import unittest
# agregamos la ruta donde estan los fuentes del proyecto
import sys
#sys.path.append('challenge')
sys.path.append('src/competidores')

# se agrega MagicMock para simular pruebas con independencia de la BD
from unittest.mock import MagicMock
from competidor import Competidor

import os
import logging


class TestCompetidor(unittest.TestCase):

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

        # crea un id simulando respuesta de BD
        self.sample_id = '5dfeb37bd6910141030af17e'
  
    # TEST de creación de objeto en BD
    def test_insert(self):
        # Indicamos al mock que devolver en un get
        self.mock.get.return_value = None
        # Indicamos al mock que devolver en un insert
        self.mock.insert.return_value = self.sample_id    
        # probando insert
        id_insert_test = self.competidor.create(
            self.sample_competidor["nombre"], self.sample_competidor["fecha_ins"], 
            self.sample_competidor["edad"], self.sample_competidor["sexo"], 
            self.sample_competidor["pais"], self.sample_competidor["ciudad"]
        )
        # validando insert
        self.mock.insert.assert_called_with(self.sample_competidor)
        # probando get
        self.mock.get.assert_called_with(key='nombre', value=self.sample_competidor['nombre'])
        # chequeo de insetado vs resultado get
        self.assertEqual(id_insert_test, self.sample_id)
    def test_duplicado(self):
        # Indicamos al mock que devolver en un get
        self.mock.get.return_value = self.sample_id
        self.search_by_name = "Juan_test0001"
        # Indicamos al mock que devolver en un insert
        self.mock.insert.return_value = self.sample_id
        # insertando el duplicado
        with self.assertRaises(ValueError):
            # esto fallará con raise
            id_insert_test = self.competidor.create(
                self.sample_competidor["nombre"], self.sample_competidor["fecha_ins"], 
                self.sample_competidor["edad"], self.sample_competidor["sexo"], 
                self.sample_competidor["pais"], self.sample_competidor["ciudad"]
            )
        # validando que no ejecutó el insert
        self.mock.insert.assert_not_called()
    # TEST de busqueda de objetos
    def test_metodos_search(self):
        # Prepadando prueba, inicio de valores:
        self.sample_competidor['_id'] = self.sample_id
        self.mock.get.return_value = self.sample_competidor
        # Ejecucción de prueba: search_by_name
        objeto_encontrado = self.competidor.search_by_name(self.sample_competidor["nombre"])
        self.assertEqual(objeto_encontrado, self.sample_competidor)
        self.mock.get.assert_called_with(key='nombre', value=self.sample_competidor['nombre'])

        # Prueba de valor no encontrado
        self.mock.get.return_value = None        
        
        test_found = self.competidor.search_by_name("__ESTE_VALOR_NO_EXISTE__")
        self.assertEqual(test_found, None)
        self.mock.get.assert_called_with(key='nombre', value="__ESTE_VALOR_NO_EXISTE__")

if __name__ == '__main__':
    unittest.main()

     
