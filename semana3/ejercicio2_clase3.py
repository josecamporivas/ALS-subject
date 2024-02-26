"""
Pedimos una cantidad a devolver
Contamos con monedas infinitas de cada tipo.
    tipo_monedas = [100, 50, 20, 10, 5, 2, 1]

EJEMPLO:
A devolver: 37
20: 1
10: 1
5: 1
2: 1
"""

def pide_cantidad() -> int:
    return int(input("A devolver: "))

def devuelve_cambio(cantidad: int) -> dict:
    tipo_monedas = [100, 50, 20, 10, 5, 2, 1]
    cambio = {}

    for moneda in tipo_monedas:
        if cantidad >= moneda:
            cambio[moneda] = cantidad // moneda
            cantidad = cantidad % moneda
    return cambio

cantidad = pide_cantidad()
result = devuelve_cambio(cantidad)

for moneda, cantidad in result.items():
    print(f"{moneda}: {cantidad}")

