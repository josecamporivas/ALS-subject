from datetime import datetime

class Mensaje:
    def __init__(self, nombre: str, mensaje: str):
        self.__nombre = nombre
        self.__mensaje = mensaje
        self.__hora = datetime.now().strftime('%H:%M:%S')

    @property
    def nombre(self):
        return self.__nombre

    @property
    def mensaje(self):
        return self.__mensaje

    @property
    def hora(self):
        return self.__hora

    def __str__(self):
        return f"{self.nombre} ({self.hora}): {self.mensaje}"