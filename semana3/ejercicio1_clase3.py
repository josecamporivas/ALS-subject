"""
Crea un programa que pida una cadena de caracteres y distinga entre vocales y consonantes.
Mostrará las vocales y las consonantes empleadas en orden alfabético, y en cuanto a las vocales,
el número de veces que aparece cada una.

Ejemplo:
Dame un texto: Hola, mundo!
Vocales: aou
Consonantes: dhlmn
a: 1 veces
o: 2 veces
u: 1 veces
i: 1 veces
e: 1 veces
"""

def pide_cadena() -> str:
    return input("Dame un texto: ")


def distingue_vocales_consonantes(cadena: str):
    vocales = set("aeiou")

    vocales_apariciones = []
    consonantes_apariciones = []

    for letra in cadena:
        if letra.isalpha():
            if letra in vocales:
                vocales_apariciones.append(letra)
            else:
                consonantes_apariciones.append(letra)

    print(f"Vocales: {"".join(sorted(vocales_apariciones))}")
    print(f"Consonantes: {"".join(sorted(consonantes_apariciones))}")

    for letra in vocales:
        print(f"{letra}: {vocales_apariciones.count(letra)} veces")

cadena = pide_cadena()
distingue_vocales_consonantes(cadena.lower())

print("hooa", end="")
