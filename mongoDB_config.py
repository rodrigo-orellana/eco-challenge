from model import Desafio
from mongoDB import BaseDatos
import logging
import os

# Para el sistema de logs
logging.basicConfig(filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,  datefmt='%d-%b-%y %H:%M:%S')


if(__name__ == "__main__"):
    # direccion = "mongodb://127.0.0.1:27017/MiBaseDatos"
    #direccion = "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/MiBaseDatos?retryWrites=true&w=majority"
    #direccion = "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/MiBaseDatos?ssl=true&ssl_cert_reqs=CERT_NONE"
    #direccion = "mongodb://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net:27017"
    direccion = "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/desafio?retryWrites=true&w=majority"

j1 = Desafio("Reciclaje", '2019-06-26', '2020-06-26', "Chile", "Santiago")
j2 = Desafio("Bike", '2019-08-26', '2020-06-26', "Chile", "Santiago")
j3 = Desafio("Limpia", '2019-09-26', '2020-06-26', "Chile", "Santiago")

mongo = BaseDatos(direccion, False)

mongo.insertDesafio(j1)
mongo.insertDesafio(j2)
mongo.insertDesafio(j3)
