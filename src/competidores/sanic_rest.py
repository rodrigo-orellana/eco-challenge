# encoding=utf8
# importacion librerías sanic
from sanic import Sanic, response
from sanic.response import json

from competidor import Competidor
from mongoDB import BaseDatos
import logging
import datetime
import os

app = Sanic('__name__')

logging.basicConfig(filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,  datefmt='%d-%b-%y %H:%M:%S')
logging.info("inicio microservicio competidor")
# Si se trata de una prueba de travis debe de hacerlo en local
user = os.environ.get("USER_MBD")
passw = os.environ.get("PASS_MBD")
ambiente = os.environ.get("AMBIENTE")
if ambiente != "localhost":
    logging.info("base de datos cloud"+str(ambiente))
    mongo = BaseDatos(
        "mongodb+srv://"+str(user)+":"+str(passw)+"@cluster0-qazzt.mongodb.net/desafio?retryWrites=true&w=majority", False, "competidor")
else:
    logging.info("base de datos local")
    mongo = BaseDatos("mongodb://127.0.0.1:27017/MiBaseDatos", True, "competidor")
# inyeccion de dependencia
competidor_data = Competidor(data_access=mongo)


@app.route('/', methods=['GET'])
def status(self):
    return json({ "running_competidor": True })

@app.route('/competidor/<ruta>', methods=['GET'])
# se indica ejecucción asincrona
async def get(request,ruta):
    logging.info("Obteniendo competidor de la base de datos. ruta:"+ruta)
    competidor = competidor_data.search_by_name(ruta)
    if competidor == None:
        return json({ "Encontrado": False })
    else:
        return json(competidor)

        

@app.route('/competidor/<ruta>', methods=['DELETE'])
# se indica ejecucción asincrona
async def delete(request,ruta):
    competidor_data.remove(ruta)
    response.text('', status=204)


@app.route('/competidor', methods=['POST'])
# se indica ejecucción asincrona
async def post(request):
    args = request.json
    id = competidor_data.create(args['nombre'],args['fecha_ins'],args['edad'],args['sexo'],args['pais'],args['ciudad'])
    if id != None:
        return json({ "id_": id })
    


if (__name__ == '__main__'):
    # Esto es para que pueda abrirse desde cualquier puerto
    #port = int(os.environ.get("PORT", 7777))
    port = 8988
    # ejecutamos la aplicación parametro worker=4 asincronos
    app.run(host="0.0.0.0", port=port, debug=False, workers=4)
