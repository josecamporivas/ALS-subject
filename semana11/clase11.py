# Reflexión
# Notación (python): atributos (datos) y atributos llamables (métodos)

# Instrospección (reflexión "lectura"): preguntar a un objeto que métodos y atributos tiene
#     Tenemos:
#       __dict__: atributos del objeto
#       hasattr(obj, nombre: str): True/False
#       dir(obj): todos los miembros del objeto (atributos y métodos)
#       getattr(obj, nombre: str): devuelve el miembro del objeto que coincide con el nombre
#       callable(attr): True/False si un miembro es una función o no
# Reflexión "escritura": modificar los atributos y métodos de un objeto
#     Tenemos:
#       del obj.x: elimina el miembro (atributo o método) llamado x
#       __getattribute__: llamado SIEMPRE para cualquier miembro
#           método de la clase que se puede sobreescribir -> tiene que devolver siempre un callable (lambda)
#       __getattr__: llamado antes de devolver AttributeError

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

class Personaje:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    def di(self, msg):
        return f"{self.nombre}: {msg}"

class PersonajeSimpson(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __getattr__(self, item):
        if self.nombre.lower() == "homer" and item == "bebe":
            return lambda: "Slurp (le da un sorbo a la cerveza Duff)"

        raise AttributeError(f"{self.__class__} no tiene {item}")

    def __getattribute__(self, item):
        if item == "di" and self.nombre.lower() == "maggie":
            return lambda msg: f"{self.nombre}: Chup-chup"
        else:
            return super().__getattribute__(item)

def str_dir(obj) -> str:
    l_miembros = dir(obj)
    toret = ""
    for str_miembro in l_miembros:
        miembro = getattr(obj, str_miembro)
        if callable(miembro):
            toret += str_miembro + "()"
        else:
            toret += str_miembro + ": " + str(miembro) + "\n"

    return toret

if __name__ == "__main__":
    p0 = Punto(1,2)
    print(hasattr(p0, 'x'))
    print(hasattr(p0, 'distancia'))
    print(hasattr(p0, 'z'))

    p1 = Personaje('Piolin')
    print(p1.di("Hola hola hola"))

    p2 = PersonajeSimpson("Maggie")
    print(p2.di("Tengo hambre"))

    p3 = PersonajeSimpson("Homer")
    print(p3.bebe())
