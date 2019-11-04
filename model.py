import logging
from datetime import date

# Clase que representa Competidor


class Desafio:

    # Crear competidor
    def __init__(self, nombre,
                 fecha_ini, fecha_fin, pais="España", ciudad="Granada"):
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

    def __dict__(self):
        d = {
            "nombre": self.nombre,
            "fecha_ini": self.fecha_ini,
            "fecha_fin": self.fecha_fin,
            "pais": self.pais,
            "ciudad": self.ciudad,
        }

        return d


class Premio:

    # Crear un premio
    def __init__(self, patrocinador, tipo, fecha_cre, monto, descripcion):
        self.patrocinador = patrocinador
        self.tipo = tipo
        self.fecha_cre = fecha_cre
        self.monto = monto
        self.descripcion = descripcion


class Competidor:
    # Crear competidor
    def __init__(self, nombre, fecha_ins, edad, sexo, pais, ciudad):
        self.scores = []
        self.premios = []
        self.nombre = nombre
        self.fecha_ins = fecha_ins
        self.edad = edad
        self.sexo = sexo
        self.pais = pais
        self.ciudad = ciudad

    def aniadir_puntaje(self, nuevo_score):
        self.scores.append(nuevo_score)
        return 'Dato valido'


# Clase que representa la estructura de los datos score
class Score:

    # Crear un score
    def __init__(self, evento, puntaje, fecha_eve):
        self.evento = evento
        self.puntaje = puntaje
        self.fecha_eve = fecha_eve
