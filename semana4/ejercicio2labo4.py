class Prestamo:
    def __init__(self, importe: float, interes: float, num_cuotas: int):
        self.__importe = importe
        self.__interes = interes
        self.__num_cuotas = num_cuotas
        self.__cuota = (importe + (importe * interes/100)) / num_cuotas

    @property
    def num_cuotas(self) -> int:
        return self.__num_cuotas

    @property
    def cuota(self) -> float:
        return self.__cuota

    def paga_cuota(self):
        self.__num_cuotas -= 1
        self.__importe -= self.__cuota

    def amortiza(self, x: float):
        self.__importe -= x
        self.__cuota = (self.__importe + (self.__importe * self.__interes/100)) / self.__num_cuotas


prestamo = Prestamo(1000, 10, 10)
print(prestamo.num_cuotas)
print(prestamo.cuota)
prestamo.paga_cuota()
print(prestamo.num_cuotas)
print(prestamo.cuota)
prestamo.amortiza(100)
print(prestamo.num_cuotas)
print(prestamo.cuota)
