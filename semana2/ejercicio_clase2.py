"""
EJERCICIO LISTAS: Un profesor tiene 3 notas por cada alumno: primer parcial, segundo parcial y proyecto.
Crea un programa que pregunte por las 3 notas de un número indeterminado de alumnos (para terminar, cadena vacía).
Al final, muestra: las notas de cada alumno y las medias.
Crea dos funciones:
fn1: def pide_notas_alumnos() -> una lista (alumnos) de diccionarios (notas):
                                    {
                                        'nombre': '',
                                        'parcial1': 10,
                                        'parcial2': 10,
                                        'proyecto': 10
                                    }
fn2: muestra notas alumnos(alumnos)
"""
def pide_notas_alumnos() -> list:
    toret = []
    while True:
        nombre = input("Nombre del alumno: ")
        if not nombre:
            break
        parcial1 = float(input("Nota primer parcial: "))
        parcial2 = float(input("Nota segundo parcial: "))
        proyecto = float(input("Nota proyecto: "))
        toret.append({
            'nombre': nombre,
            'parcial1': parcial1,
            'parcial2': parcial2,
            'proyecto': proyecto
        })
    return toret

def muestra_notas_alumnos(alumnos: list):
    for alumno in alumnos:
        print(f"{alumno['nombre']}: {alumno['parcial1']}, {alumno['parcial2']}, {alumno['proyecto']}")
        print(f"Media: {((alumno['parcial1'] + alumno['parcial2'] + alumno['proyecto']) / 3):.2f}")

alumnos = pide_notas_alumnos()
print()
muestra_notas_alumnos(alumnos)