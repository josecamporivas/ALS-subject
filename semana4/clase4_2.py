class Waypoint:
    NULL_ISLAND = None  # Atributo de clase (estático)

    @staticmethod
    def el0_0():  # Método estático
        if Waypoint.NULL_ISLAND is None:
            Waypoint.NULL_ISLAND = Waypoint(0, 0, "NULL ISLAND")
        return Waypoint.NULL_ISLAND

    def __init__(self, lat: float, lon: float, nombre: str):
        self.__lat = lat
        self.__lon = lon
        self.__nombre = nombre

    @property
    def lat(self) -> float:
        return self.__lat

    @property
    def lon(self) -> float:
        return self.__lon

    @property
    def nombre(self) -> str:
        return self.__nombre

    def __str__(self):
        return f"{self.__nombre}: {self.__lat}ºN, {str(self.__lon)}ºO"

class Cuadrante:
    def __init__(self, coord1: Waypoint, coord2: Waypoint):
        self.__coord1 = coord1
        self.__coord2 = coord2

    @property
    def coord1(self):
        return self.__coord1

    @property
    def coord2(self):
        return self.__coord2

    def __str__(self):
        return f"[{self.__coord1}] - [{self.__coord2}]"

class Alto(Waypoint):
    def __init__(self, lat: float, lon: float, nombre: str, altitud: float):
        super().__init__(lat, lon, "Alto de " + nombre)
        self.__altitud = altitud

    @property
    def altitud(self) -> float:
        return self.__altitud

    def __str__(self):
        return f"{super().__str__()} a {self.__altitud}m"


if __name__ == "__main__":
    w = Waypoint(42.344686, -7.8556442, "Cafeteria politécnico")
    print(str(w))

    cuadrante = Cuadrante(w, Waypoint.el0_0())
    print(str(cuadrante))
