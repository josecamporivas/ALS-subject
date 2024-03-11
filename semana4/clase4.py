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

    def __gt__(self, other):   # Sobrecarga del operador >
        return self.distancia(0, 0) > other.distancia(0, 0)

    def __eq__(self, other):  # Sobrecarga del operador ==
        return self.distancia(0, 0) == other.distancia(0, 0)

    def __ne__(self, other):  # Sobrecarga del operador !=
        return self.distancia(0, 0) != other.distancia(0, 0)

    def __lt__(self, other):  # Sobrecarga del operador <
        return self.distancia(0, 0) < other.distancia(0, 0)

    def __ge__(self, other):  # Sobrecarga del operador >=
        return self.distancia(0, 0) >= other.distancia(0, 0)

    def __le__(self, other):  # Sobrecarga del operador <=
        return self.distancia(0, 0) <= other.distancia(0, 0)

    def __len__(self):  # Sobrecarga del operador len()
        return 2

    def __getitem__(self, index):  # Sobrecarga del operador []
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError("Index out of range")

    def __setitem__(self, index, value):  # Sobrecarga del operador []
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")

    def __hash__(self):  # Sobrecarga del operador hash()
        return hash((self.x, self.y))   # Se retorna el hash de una tupla con los valores de x y y




if __name__ == "__main__":
    p = Punto(1, 2)
    print(str(p))
    p.x = 3
    p.y = 4
    print(str(p))
    print(p.distancia(0, 0))

    p1 = Punto(1, 2)
    p2 = Punto(3, 4)
    print(p1 > p2)
    print(p1 == p2)
    print(p1 != p2)
    print(p1 < p2)
    print(p1 >= p2)
    print(p1 <= p2)
