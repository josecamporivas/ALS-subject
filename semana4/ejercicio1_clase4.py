"""
Crea la clase Tripleta, que almacena los valores x, y, z.
Proporciona un inicializador, propiedades de solo lectura y un método __str__() que devuelve los valores
de forma textual con el formato <x>, <y>, <z>.

Añade a la clase anterior el método to_tuple() que devuelve una tupla con los valores de la tripleta.
"""


class Tripleta:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    def to_tuple(self):
        return self.__x, self.__y, self.__z  # Devuelve una tupla con los valores de la tripleta

    def __str__(self):
        return f"<{self.__x}>, <{self.__y}>, <{self.__z}>"


if __name__ == "__main__":
    tripleta = Tripleta(1, 2, 3)
    print(str(tripleta))
    print(tripleta.to_tuple())
