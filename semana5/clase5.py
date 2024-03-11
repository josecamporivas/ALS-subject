import unittest
import math


class Punto:
    def __init__(self, x=0, y=0):
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
        return math.sqrt((self.x - a) ** 2 + (self.y - b) ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __gt__(self, other):  # Sobrecarga del operador >
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
        return hash((self.x, self.y))  # Se retorna el hash de una tupla con los valores de x y y

    def a_lista(self):
        return [self.x, self.y]

    def __add__(self, other):
        if isinstance(other, Punto):
            return Punto(self.x + other.x, self.y + other.y)

        if isinstance(other, int):
            return Punto(self.x + other, self.y + other)

    def __radd__(self, other):
        if isinstance(other, Punto):
            return Punto(self.x + other.x, self.y + other.y)

        if isinstance(other, int):
            return Punto(self.x + other, self.y + other)


class TestPunto(unittest.TestCase):
    def setUp(self):
        self.p0 = Punto()
        self.p1 = Punto(1, 2)
        self.p2 = Punto(3, 4)

    def test_init(self):
        self.assertEqual(0, self.p0.x)
        self.assertEqual(0, self.p0.y)

    def test_init_params(self):
        self.assertEqual(1, self.p1.x)
        self.assertEqual(2, self.p1.y)

    def test_a_lista(self):
        self.assertEqual([1, 2], self.p1.a_lista())

    def test_corchetes(self):
        self.assertEqual(1, self.p1[0])
        self.assertEqual(2, self.p1[1])

    def test_suma(self):
        self.assertEqual(Punto(4, 6), self.p1 + self.p2)
        self.assertEqual(Punto(4, 5), self.p1 + 3)

    def test_suma_inversa(self):
        self.assertEqual(Punto(4, 6), self.p2 + self.p1)
        self.assertEqual(Punto(4, 5), 3 + self.p1)

    def test_getitem_error(self):
        self.assertEqual(1, self.p1[0])
        self.assertEqual(2, self.p1[1])

        self.assertRaises(IndexError, lambda: self.p1[2])

if __name__ == "__main__":
    unittest.main()
