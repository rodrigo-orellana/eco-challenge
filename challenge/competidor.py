#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 2019
"""
# Clase que representa Competidor


class Competidor:
    # Method init
    def __init__(self, data_access):
        # inyeccion de dependencia
        self.data_access = data_access
 
    #CRUD ***************************************************************************************
    def search_by_name(self, nombre):
        return self.data_access.get(key='nombre', value=nombre)

    def create(self, nombre, fecha_ins, edad, sexo, pais, ciudad):
        if self.search_by_name(nombre) == None:
            item = dict(
                nombre=nombre,
                fecha_ins=fecha_ins,
                edad=edad,
                sexo=sexo,
                pais=pais,
                ciudad=ciudad
            )
            _id = self.data_access.insert(item)
            return _id
        else:
            raise ValueError("El competidor ya existe")

    def search_by_id(self, id):
        res = self.data_access.get(key='_id', value=id)
        if res == None:
            raise LookupError("Registro no encontrado")
        return res


    def remove(self, id):
        self.search_by_id(id)
        self.data_access.delete(id)
    

    def modify(self, id, new_values):
        event = self.search_by_id(id)
        for key in new_values.keys():
            if key not in event.keys():
                raise KeyError("No existe registro " + str(key))
            if key == "_id":
                raise KeyError("Error al modificar")
        self.data_access.update(id, new_values)


# Clase que representa la estructura de los datos score
class Score:

    # Crear un score
    def __init__(self, evento, puntaje, fecha_eve):
        self.evento = evento
        self.puntaje = puntaje
        self.fecha_eve = fecha_eve


class Premio:

    # Crear un premio
    def __init__(self, patrocinador, tipo, fecha_cre, monto, descripcion):
        self.patrocinador = patrocinador
        self.tipo = tipo
        self.fecha_cre = fecha_cre
        self.monto = monto
        self.descripcion = descripcion
        # if nuevo_score is None:
        # self.premios.append(nuevo_premio)
        # return 'Dato valido'
