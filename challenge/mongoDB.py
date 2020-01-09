#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import pymongo
#ObjectIds are small, likely unique, fast to generate, and ordered. ObjectId values are 12 bytes in length
from bson.objectid import ObjectId
"""
from desafio import Desafio
import os
"""


class BaseDatos:
    def __init__(self, direccion, prueba=False):
        logging.info("MONGO:Tratando de conectar con la base de datos.")
        MONGODB_URI = direccion
        client = pymongo.MongoClient(MONGODB_URI, connectTimeoutMS=40000)
        db = client["desafio"]
       
        if (not prueba):
            self.desafio = db.desafio
        else:
            self.desafio = db.prueba
        logging.info("MONGO:Conexión completada con éxito.")
        


    # CRUD*******************************************************************************
    def insert(self, element):
        _id = self.desafio.insert_one(element.copy()).inserted_id
        return str(_id)


    def get(self, key, value):
        # None if no object is found:
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
