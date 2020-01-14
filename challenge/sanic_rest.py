# encoding=utf8
# importacion librerías sanic
from sanic import Sanic, response
from sanic.response import json

from desafio import Desafio
from mongoDB import BaseDatos
import logging
import datetime
import os

app = Sanic('__name__')

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
        "mongodb+srv://"+str(user)+":"+str(passw)+"@cluster0-qazzt.mongodb.net/desafio?retryWrites=true&w=majority", False, "desafio")
else:
    logging.info("base de datos local")
    mongo = BaseDatos("mongodb://127.0.0.1:27017/MiBaseDatos", True, "desafio")
# inyeccion de dependencia
desafio_data = Desafio(data_access=mongo)


@app.route('/', methods=['GET'])
# se indica ejecucción asincrona
def status(self):
    return json({ "running": True })

@app.route('/desafios/<ruta>', methods=['GET'])
# se indica ejecucción asincrona
async def get(request,ruta):
    logging.info("Obteniendo desafios de la base de datos. ruta:"+ruta)
    desafio = desafio_data.search_by_name(ruta)
    if desafio == None:
        return json({ "Encontrado": False })
    else:
        return json(desafio)

        

@app.route('/desafios/<ruta>', methods=['DELETE'])
# se indica ejecucción asincrona
async def delete(request,ruta):
    desafio_data.remove(ruta)
    response.text('', status=204)


@app.route('/desafios', methods=['POST'])
# se indica ejecucción asincrona
async def post(request):
    args = request.json
    id = desafio_data.create(args['nombre'],args['fecha_ini'],args['fecha_fin'],args['pais'],args['ciudad'])
    if id != None:
        return json({ "id_": id })
    


if (__name__ == '__main__'):
    # Esto es para que pueda abrirse desde cualquier puerto
    port = int(os.environ.get("PORT", 8989))
    # ejecutamos la aplicación parametro worker=4 asincronos
    app.run(host="0.0.0.0", port=port, debug=False, workers=4)
