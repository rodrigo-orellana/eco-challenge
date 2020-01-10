#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

# TODO: obtent ranking, calcular ganadores
# Duda diseño: premio acá o en usuario?

class Desafio:

    # init desafio
    def __init__(self, data_access):
        # inyeccion de dependencia
        self.data_access = data_access

  
    #CRUD ***************************************************************************************
    def search_by_name(self, nombre):
        return self.data_access.get(key='nombre', value=nombre)

    def create(self, nombre, fecha_ini, fecha_fin, pais="ESPAÑA", ciudad="GRANADA"):
        if self.search_by_name(nombre) == None:
            item = dict(
                nombre=nombre,
                fecha_ini=fecha_ini,
                fecha_fin=fecha_fin,
                pais=pais,
                ciudad=ciudad
            )
            _id = self.data_access.insert(item)
            return _id
        else:
            raise ValueError("Ya existe el registro que se intenta crear")
    
    def modify(self, id, new_values):
        event = self.search_by_id(id)
        for key in new_values.keys():
            if key not in event.keys():
                raise KeyError("No existe registro con campo" + str(key))
            if key == "_id":
                raise KeyError("Campo _id no es modificable")
        
        self.data_access.update(id, new_values)

    def search_by_id(self, id):
        res = self.data_access.get(key='_id', value=id)
        if res == None:
            raise LookupError("No existe registro con ese ID")

        return res

    def remove(self, id):
        self.search_by_id(id)
        self.data_access.delete(id)
    


""" 
class Premio:

    # Crear un premio
    def __init__(self, patrocinador, tipo, fecha_cre, monto, descripcion):
        self.patrocinador = patrocinador
        self.tipo = tipo
        self.fecha_cre = fecha_cre
        self.monto = monto
        self.descripcion = descripcion
 """
