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
