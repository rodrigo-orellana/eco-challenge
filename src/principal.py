# encoding=utf8
from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from desafio import Desafio
from mongoDB import BaseDatos
import logging
import datetime
import os

app = Flask("ecochallenge")
api = Api(app)

logging.basicConfig(filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,  datefmt='%d-%b-%y %H:%M:%S')


# Si se trata de una prueba de travis debe de hacerlo en local


user = os.environ.get("USER_MBD")
passw = os.environ.get("PASS_MBD")
ambiente = os.environ.get("AMBIENTE")
if ambiente != "localhost":
    logging.info("base de datos cloud"+str(ambiente))
    mongo = BaseDatos(
        "mongodb+srv://"+str(user)+":"+str(passw)+"@cluster0-qazzt.mongodb.net/desafio?retryWrites=true&w=majority", False)
else:
    logging.info("base de datos local")
    mongo = BaseDatos("mongodb://127.0.0.1:27017/MiBaseDatos", True)
parser = reqparse.RequestParser()
parser.add_argument('nombre', type=str,
                    help='desafío no puede ser null', required=True)
parser.add_argument('fecha_ini', type=str, required=False)
parser.add_argument('fecha_fin', type=str, required=False)
parser.add_argument('pais', type=str, required=False)
parser.add_argument('ciudad', type=str, required=False)


def abortar_ruta_inexistente(ruta):
    if(False):  # Crear validación
        abort(404, message="Error 404. La ruta {} no existe".format(ruta))


class Principal(Resource):
    def get(self):
        return {'status': 'OK'}


class DesafioIndividual(Resource):
    def get(self, ruta):
        abortar_ruta_inexistente(ruta)
        logging.info("Obteniendo desafios de la base de datos.")
        return {ruta: mongo.getDesafio(ruta)}

    def put(self, ruta):
        args = parser.parse_args()
        desafio = Desafio(args['nombre'], args['fecha_ini'], args['fecha_fin'])
        exito = mongo.insertDesafio(desafio)
        if(not(exito)):
            mongo.updateDesafio(args['nombre'], desafio.__dict__())
        return mongo.getDesafio(ruta)

    def delete(self, ruta):
        mongo.removeDesafio(ruta)
        return '', 204


class Desafios(Resource):

    def get(self):
        return mongo.getDesafios()

    def post(self):
        args = parser.parse_args()
        desafio = Desafio(args['nombre'], args['fecha_ini'], args['fecha_fin'])
        ruta = args['nombre']
        mongo.insertDesafio(desafio)
        return mongo.getDesafio(ruta), 201

    def delete(self):
        mongo.removeDesafios()
        return '', 204


api.add_resource(Principal, '/', '/status')
api.add_resource(Desafios, '/desafios')
api.add_resource(DesafioIndividual, '/desafios/<string:ruta>')


if (__name__ == '__main__'):
    # Esto es para que pueda abrirse desde cualquier puerto y
    port = int(os.environ.get("PORT", 8989))
    app.run(host="0.0.0.0", port=port, debug=False)