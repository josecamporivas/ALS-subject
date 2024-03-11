"""
Un almacén guarda piezas de fontanería (con un valor común que es el coste), en concreto tuberías (longitud),
tuercas (ancho), y codos (ángulo). Es necesario llevar un servicio de inventario que permita el alta, baja
y modificación de piezas.

Crea la jerarquía de herencia necesaria para las piezas, y para la clase Inventario,
reescribe los métodos necesarios, de tal forma que se comporte como una lista de piezas.

"""

class Pieza:
    def __init__(self, coste: float, nombre: str):
        self.__coste = coste
        self.__nombre = nombre

    @property
    def coste(self):
        return self.__coste

    @property
    def nombre(self):
        return self.__nombre

    @coste.setter
    def coste(self, value):
        self.__coste = value


class Tuberia(Pieza):
    def __init__(self, coste: float, longitud: float):
        super().__init__(coste, "Tuberia")
        self.__longitud = longitud

    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self, value):
        self.__longitud = value

    def __str__(self):
        return f"{self.nombre}: {self.longitud} ángulo x {self.coste}€"

class Tuerca(Pieza):
    def __init__(self, coste: float, ancho: float):
        super().__init__(coste, "Tuerca")
        self.__ancho = ancho

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, value):
        self.__ancho = value

    def __str__(self):
        return f"{self.nombre}: {self.ancho} ancho  x {self.coste}€"

class Codo(Pieza):
    def __init__(self, coste: float, angulo: float):
        super().__init__(coste, "Todo")
        self.__angulo = angulo

    @property
    def angulo(self):
        return self.__angulo

    @angulo.setter
    def angulo(self, value):
        self.__angulo = value

    def __str__(self):
        return f"{self.nombre}: {self.angulo} ángulo x {self.coste}€"

class Inventario:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.__lista = items

    def __len__(self):
        return len(self.__lista)

    def __getitem__(self, index: int):
        return self.__lista[index]

    def __delitem__(self, key):
        return self.__lista.pop(key)

    def __str__(self):
        toret = "Inventario\n"
        for i in self.__lista:
            toret += "\t" + str(i) + "\n"
        return toret


if __name__ == "__main__":
    tub1 = Tuberia(12.5, 10)
    tuer1 = Tuerca(5, 10)
    cod1 = Codo(7, 25.5)

    inventario = Inventario([tub1, tuer1, cod1])
    print(inventario)

    inventario[0].longitud = 20
    print(inventario)



