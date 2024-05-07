"""
Clase Struct:
Se trata de un diccionario (dict), pero que además de permitir el acceso a los miembros a través de ['miembro'],
permite el acceso "directo"
s1 = Struct()
s1.add('x', 42)
print(s1.x)
"""
class Struct:
    def __init__(self):
        ...

    def add(self, key, value):
        self.__dict__[key] = value

# ESTO MÉTODOS SON PARA QUE FUNCIONE CON LLAVES []
    # def __getitem__(self, item):
    #     return self.__dict__[item]
    #
    # def __setitem__(self, key, value):
    #     self.__dict__[key] = value

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        raise AttributeError(f"{self.__class__} no tiene {item}")

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __str__(self):
        return str(self.__dict__)

if __name__ == "__main__":
    s1 = Struct()
    s1.add('x', 42)
    print(s1.x)
    print(s1)
    s1.y = 3.14
    print(s1)
    print(s1.y)
    try:
        print(s1.z)
    except AttributeError as e:
        print(e)

    # print(s1['x'])
    # print(s1['y'])
