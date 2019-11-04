import logging
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 2019
"""
# Clase que representa Competidor


class Desafio:

    # Crear competidor
    def __init__(self, nombre,
                 fecha_fin, fecha_ini, pais="España", ciudad="Granada"):
        self.premios = []
        self.competidores = []
        self.nombre = nombre
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin
        self.pais = pais
        self.ciudad = ciudad
# TODO: obtent ranking, calcular ganadores
# Duda: preio acá o en usuario?

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
        return True  # {ruta: mongo.getJugador(ruta)}


class Premio:

    # Crear un premio
    def __init__(self, patrocinador, tipo, fecha_cre, monto, descripcion):
        self.patrocinador = patrocinador
        self.tipo = tipo
        self.fecha_cre = fecha_cre
        self.monto = monto
        self.descripcion = descripcion
