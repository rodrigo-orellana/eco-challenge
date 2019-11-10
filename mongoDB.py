#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import pymongo
from desafio import Desafio

import os


class BaseDatos:
    def __init__(self, direccion, prueba=False):
        logging.info("MONGO:Tratando de conectar con la base de datos.")
        MONGODB_URI = direccion
        client = pymongo.MongoClient(MONGODB_URI, connectTimeoutMS=40000)
        if ('MLAB' in os.environ):
            db = client["desafio"]
        else:
            db = client["desafio"]
        if (not prueba):
            self.desafio = db.desafio
        else:
            # self.desafio = db.desafio
            self.desafio = db.desafio
        logging.info("MONGO:Conexión completada con éxito.")

    def insertDesafio(self, desafio):
        entrada = desafio.__dict__()
        if(self.desafio.find_one({"nombre": entrada['nombre']})):
            logging.warning(
                "MONGO:Desafio %s ya existente, no se ha podido insertar.", entrada['nombre'])
            return False
        else:
            self.desafio.insert_one(entrada)
            logging.info(
                "MONGO:Desafio %s insertado en la base de datos.", entrada['nombre'])
            return True

    def getDesafio(self, nombre):
        desafio = self.desafio.find_one({"nombre": nombre})
        del desafio['nombre']
        logging.info(
            "MONGO:Desafio %s devuelto por la base de datos.", nombre)
        return nombre

    def getDesafios(self):
        salida = {}
        for j in self.desafio.find():
            del j['_id']
            salida[j['nombre']] = j
        logging.info("MONGO:Todos los Desafios de la base de datos devueltos.")
        return salida

    def insertDesafio(self, desafio):
        entrada = desafio.__dict__()
        if(self.desafio.find_one({"Nombre": entrada['nombre']})):
            logging.warning(
                "MONGO:Desafio %s ya existente, no se ha podido insertar en la base de datos.", entrada['nombre'])
            return False
        else:
            self.desafio.insert_one(entrada)
            logging.info(
                "MONGO:Desafio %s insertado en la base de datos.", entrada['nombre'])
            return True

    def removeDesafio(self, nombre):
        logging.info(
            "MONGO:Desafio %s eliminado de la base de datos.", nombre)
        self.desafio.delete_one({"Nombre": nombre})

    def mostrarDesafios(self):
        cursor = self.desafio.find()
        for j in cursor:
            print(j['nombre'], ' - ', j['fecha_ini'], ' - ', j['fecha_fin'])

    def removeDesafios(self):
        for j in self.desafio.find():
            self.removeDesafio(j['nombre'])
        logging.info("MONGO:Base de datos de Desafio vaciada por completo.")

    def getSize(self):
        return self.desafio.count_documents({})


"""
    def updateDEsafio(self, jugador_nick, updates):
        try:
            jugador = self.getJugador(jugador_nick)
            self.jugadores.update_one({'Nick': jugador['Nick']}, {
                                      '$set': updates}, upsert=False)
        except:
            print("hola")
            logging.warning(
                "MONGO:Oops!! Se pretende actualizar una entrada inexistente.")

    def getJugadores(self):
        salida = {}
        for j in self.jugadores.find():
            del j['_id']
            salida[j['Nick']] = j
        logging.info(
            "MONGO:Todos los jugadores de la base de datos devueltos.")
        return salida
"""
