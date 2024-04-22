# Herencia dinámica
# Python usa una herencia basada en prototipos o por delegación (no estoy muy seguro de que sea por delegación)

class A:
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.__y = y

    @property
    def y(self):
        return self.__y

a = A(10)
b = B(10, 20)

print(a.x)
# print(a.y) # AttributeError: 'A' object has no attribute 'y'
print(b.x)
print(b.y)

print(a.__class__)
print(b.__class__)
print(b.__class__.__bases__)

class Programador:
    def __init__(self, nombre, sueldo):
        self.__nombre = nombre
        self.__sueldo = sueldo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def sueldo(self):
        return self.__sueldo

    def __str__(self):
        return f"Programador {self.nombre}: {self.sueldo}€"

class ProgramadorJunior(Programador):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre, sueldo)

    def asciende(self):
        self._Programador__sueldo = 1700
        self.__class__ = ProgramadorSenior   # Importante: cambia la clase del objeto

    def __str__(self):
        return f"Programador {self.nombre}: {self.sueldo}€ (junior)"

class ProgramadorSenior(Programador):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre, sueldo)

    def desciende(self):
        self._Programador__sueldo = 1100
        self.__class__ = ProgramadorJunior

    def __str__(self):
        return f"Programador {self.nombre}: {self.sueldo}€ (senior)"

p1 = ProgramadorJunior("Erik", 1100)
p2 = ProgramadorSenior("Juan", 1700)

print("Programadores antes:")
print(p1)
print(p2)
# p1.__class__ = ProgramadorSenior
# p1.sueldo = 1700

print("Programadores después:")
p1.asciende()
print(p1)

p2.desciende()
print(p2)
