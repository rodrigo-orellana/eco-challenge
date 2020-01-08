#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 2019
"""
# Clase que representa Competidor


class Competidor:
    # Crear competidor
    def __init__(self, nombre, fecha_ins, edad, sexo, pais, ciudad):
        self.scores = []
        self.premios = []
        self.nombre = nombre
        self.fecha_ins = fecha_ins
        self.edad = edad
        self.sexo = sexo
        self.pais = pais
        self.ciudad = ciudad

    def aniadir_puntaje(self, nuevo_score):
        self.scores.append(nuevo_score)
        return 'Dato valido'

    def get_edad(self):
        return self.edad

    def get_fecha_sexo(self):
        return self.sexo

    def get_pais(self):
        return self.pais

    def get_ciudad(self):
        return self.ciudad

    def update_edad(self, edad_new):
        self.edad = edad_new

    def update_sexo(self, sexo_new):
        self.sexo = sexo_new

    def update_pais(self, pais_new):
        self.pais = pais_new

    def update_ciudad(self, ciudad_new):
        self.ciudad = ciudad_new
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
