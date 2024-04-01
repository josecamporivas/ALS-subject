# ListaTopN

# Guarda los n elementos mayores
# P. ej. si n = 3 y la lista es [1, 2, 3, 4, 5], la lista resultante es [5, 4, 3]

class ListaTopN:
    def __init__(self, n):
        self.__n = n
        self.__lista = []

    @property
    def n(self):
        return self.__n

    @property
    def lista(self):
        return list(self.__lista)

    def inserta(self, elemento):
        # Precondiciones
        assert isinstance(elemento, (int, float)), "El elemento debe ser un número"

        self.__lista.append(elemento)
        self.__lista.sort(reverse=True)
        self.__lista = self.__lista[:self.__n]

        # Post-condiciones
        assert len(self.__lista) <= self.__n, "La lista no puede tener más de n elementos"
        if __debug__:
            for i in range(1, len(self.__lista)):
                assert self.__lista[i - 1] >= self.__lista[i], "La lista no está ordenada"

    def __str__(self):
        return str.join(", ", map(str, self.__lista))


if __name__ == "__main__":
    l = ListaTopN(3)
    l.inserta(1)
    l.inserta(2)
    l.inserta(3)
    l.inserta(4)
    l.inserta(5)
    print(l)
