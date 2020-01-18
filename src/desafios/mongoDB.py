#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import pymongo
from bson.objectid import ObjectId

"""
Administración de BD MONGODB.
Esta capa es reemplazable por otra tecnología
"""

class BaseDatos:
    def __init__(self, direccion, prueba=False, collection="desafio"):
        logging.info("MONGO:Tratando de conectar con la base de datos.")
        MONGODB_URI = direccion
        client = pymongo.MongoClient(MONGODB_URI, connectTimeoutMS=40000)
        db = client[collection]
       
        if (not prueba):
            self.desafio = db.desafio
        else:
            self.desafio = db.prueba
        logging.info("MONGO:Conexión completada con éxito.")

    # METODOS CRUD*******************************************************************************
    def insert(self, element):
        _id = self.desafio.insert_one(element.copy()).inserted_id
        return str(_id)

    def get(self, key, value):
        if key == '_id':
            out = self.desafio.find_one({'_id': ObjectId(value)})
        else:
            out = self.desafio.find_one({key: value})

        if out != None:
            out['_id'] = str(out['_id'])
        return out

    def update(self, _id, new_values):
        _new_values = {'$set': new_values}
        self.desafio.update_one({"_id": ObjectId(_id)}, _new_values)

    def delete(self, _id):
        self.desafio.delete_one({"_id": ObjectId(_id)})

    def getSize(self):
        return self.desafio.count_documents({})
