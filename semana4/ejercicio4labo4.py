class Aparato:
    def __init__(self, nombre: str, precio_hora: float):
        self.__nombre = nombre
        self.__precio_hora = precio_hora

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def precio_hora(self) -> float:
        return self.__precio_hora


class Televisor(Aparato):
    def __init__(self, precio_hora: float):
        super().__init__("Televisor", precio_hora)


class Decodificador(Aparato):
    def __init__(self, precio_hora: float):
        super().__init__("Decodificador", precio_hora)


class Detalle:
    def __init__(self, aparato: Aparato, horas: int):
        self.__aparato = aparato
        self.__horas = horas

    def calcula_total(self) -> float:
        return self.__aparato.precio_hora * self.__horas

    def __str__(self):
        return f"{self.__aparato.nombre}: {self.__horas}h * {self.__aparato.precio_hora}€/hora = {self.calcula_total()}€"


class Factura:
    def __init__(self):
        self.__detalles = []

    def add_detalle(self, detalle: Detalle):
        self.__detalles.append(detalle)

    def calcula_total(self) -> float:
        total = 0
        for detalle in self.__detalles:
            total += detalle.calcula_total()
        return total

    def __str__(self):
        detalles = "\n\t".join([str(detalle) for detalle in self.__detalles])
        return f"Factura:\n\t{detalles}\nTotal: {self.calcula_total()}€"

televisor = Televisor(10)
decodificador = Decodificador(5)
detalle1 = Detalle(televisor, 3)
detalle2 = Detalle(decodificador, 2)
factura = Factura()
factura.add_detalle(detalle1)
factura.add_detalle(detalle2)
print(str(factura))
