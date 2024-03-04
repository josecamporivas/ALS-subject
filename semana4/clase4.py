import math

class Punto:
    def __init__(self, x, y):
        self.__x = x  # Atributo privado (porque tiene __ al inicio)
        self.__y = y  # Atributo privado también

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def distancia(self, a, b):
        return math.sqrt((self.x - a)**2 + (self.y - b)**2)

    def __str__(self):
        return f"({self.x}, {self.y})"

if __name__ == "__main__":
    p = Punto(1, 2)
    print(str(p))
    p.x = 3
    p.y = 4
    print(str(p))
    print(p.distancia(0, 0))
