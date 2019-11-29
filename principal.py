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

if('TRAVIS' in os.environ):
    print('TRAVIS')
    mongo = BaseDatos("mongodb://127.0.0.1:27017/MiBaseDatos", True)
else:
    print('else')
    user = os.environ.get("USER_MBD")
    passw = os.environ.get("PASS_MBD")
    mongo = BaseDatos(
        "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/desafio?retryWrites=true&w=majority", False)

# nombre,fecha_fin, fecha_ini, pais="España", ciudad="Granada")
parser = reqparse.RequestParser()
parser.add_argument('nombre', type=str,
                    help='desafío no puede ser null', required=True)
parser.add_argument('fecha_ini', type=datetime, required=True)
parser.add_argument('fecha_fin', type=datetime, required=True)
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
        desafio = Desafio(args['Nombre'], args['Fecha_ini'], args['Fecha_fin'])
        exito = mongo.insertDesafio(desafio)
        if(not(exito)):
            mongo.updateDesafio(args['Nombre'], desafio.__dict__())
        return mongo.getDesafio(ruta)

    def delete(self, ruta):
        mongo.removeDesafio(ruta)
        return '', 204


class Desafios(Resource):

    def get(self):
        return mongo.getDesafios()

    def post(self):
        args = parser.parse_args()
        desafio = Desafio(args['Nombre'], args['Fecha_ini'], args['Fecha_fin'])
        ruta = args['Nombre']
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
    #  direccion(de esta forma en heroku no nos da error).
    port = int(os.environ.get("PORT", 8989))
    app.run(host="0.0.0.0", port=port, debug=False)
