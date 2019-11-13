#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging


class Desafio:

    # Crear competidor
    def __init__(self, nombre,
                 fecha_ini, fecha_fin, pais="ESPAÑA", ciudad="GRANADA"):
        self.premios = []
        self.competidores = []
        self.nombre = nombre
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin
        self.pais = pais
        self.ciudad = ciudad
# TODO: obtent ranking, calcular ganadores
# Duda diseño: premio acá o en usuario?

    def __dict__(self):
        d = {
            "nombre": self.nombre,
            "fecha_ini": self.fecha_ini,
            "fecha_fin": self.fecha_fin,
            "pais": self.pais,
            "ciudad": self.ciudad
        }

        return d

    def aniadir_premio(self, nuevo_premio):
        if nuevo_premio is None:
            return 'Dato no valido'
        else:
            self.premios.append(nuevo_premio)
            return 'Dato valido'

    def cerrar_desafio():
        return True

    def get(self, ruta):
        logging.info("mensaje de log.")
        # {ruta: mongo.getJugador(ruta)}
        return True

    def get_fecha_fin(self):
        return self.fecha_fin

    def get_fecha_ini(self):
        return self.fecha_ini

    def get_pais(self):
        return self.pais

    def get_ciudad(self):
        return self.ciudad

    def update_fecha_fin(self, fecha_fin_new):
        self.fecha_fin = fecha_fin_new

    def update_fecha_ini(self, fecha_ini_new):
        self.fecha_ini = fecha_ini_new

    def update_pais(self, pais_new):
        self.pais = pais_new

    def update_ciudad(self, ciudad_new):
        self.ciudad = ciudad_new


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
