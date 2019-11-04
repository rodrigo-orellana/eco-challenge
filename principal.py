from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from model import Jugador
from mongoDB import BaseDatos
import logging
import datetime
import os

app = Flask("hito2")
api = Api(app)

# Para el sistema de logs
logging.basicConfig(filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,  datefmt='%d-%b-%y %H:%M:%S')

# Esto sera con flask sin el microframework de RestFul
# @app.route("/")

# Si se trata de una prueba de travis debe de hacerlo en local

if('TRAVIS' in os.environ):
    print('TRAVIS')
    mongo = BaseDatos("mongodb://127.0.0.1:27017/MiBaseDatos", True)
elif('MLAB' in os.environ):
    print('MLAB')
    # rodrigoesteban/r0k4FCFHDNGJKnlh
    mongo = BaseDatos("mongodb://rodrigoesteban:" + os.environ.get('MLABPASS') +
                      "@ds026018.mlab.com:26018/jugadores", True)
else:
    print('else')
    #mongo = BaseDatos("mongodb://127.0.0.1:27017/MiBaseDatos", False)
    mongo = BaseDatos(
        "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/sample_airbnb?retryWrites=true&w=majority", False)


# nombre,fecha_fin, fecha_ini, pais="España", ciudad="Granada")
parser = reqparse.RequestParser()
parser.add_argument('desafio', type=str,
                    help='desafío no puede ser null', required=True)
parser.add_argument('fecha_ini', type=datetime, required=True)
parser.add_argument('fecha_fin', type=datetime, required=True)
parser.add_argument('pais', type=str, required=False)
parser.add_argument('ciudad', type=str, required=False)


def abortar_ruta_inexistente(ruta):
    if(False):  # Crear vaidación
        abort(404, message="Error 404. La ruta {} no existe".format(ruta))


"""     for j in mongo.jugadores.find():
        if(ruta == j['Nick']):
            return
    abort(404, message="Error 404. La ruta {} no existe".format(ruta))
 """


class Principal(Resource):
    def get(self):
        return {'status': 'OK'}


class Desafios(Resource):
    def get(self, ruta):
        abortar_ruta_inexistente(ruta)
        logging.info("Obteniendo desafios de la base de datos.")
        return {ruta: mongo.getJugador(ruta)}

    def put(self, ruta):
        args = parser.parse_args()
        jugador = Jugador(args['Nick'], args['Nombre'], args['Apellidos'], args['Edad'],
                          args['Videojuegos'], args['Competitivo'])
        exito = mongo.insertJugador(jugador)
        if(not(exito)):
            mongo.updateJugador(args['Nick'], jugador.__dict__())
        return mongo.getJugador(ruta)

    def delete(self, ruta):
        mongo.removeJugador(ruta)
        return '', 204


class Jugadores(Resource):

    def get(self):
        return mongo.getJugadores()

    def post(self):
        args = parser.parse_args()
        jugador = Jugador(args['Nick'], args['Nombre'], args['Apellidos'], args['Edad'],
                          args['Videojuegos'], args['Competitivo'])
        ruta = args['Nick']
        mongo.insertJugador(jugador)
        return mongo.getJugador(ruta), 201

    def delete(self):
        mongo.removeJugadores()
        return '', 204


api.add_resource(Principal, '/', '/status')
api.add_resource(Jugadores, '/jugadores')
api.add_resource(JugadorIndividual, '/jugadores/<string:ruta>')


if (__name__ == '__main__'):
    # Esto es para que pueda abrirse desde cualquier puerto y
    #  direccion(de esta forma en heroku no nos da error).
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)
    # app.run(debug=True)
