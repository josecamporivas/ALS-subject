datos = """Microsoft, 1, Apple, 2, Google, 3, Yahoo, 4\n
1, 2015-01-09, 120, 34, 256, 78, 93, 222, 5\n
2, 2015-01-09, 900, 346, 730, 456, 33, 345, 234\n
3, 2015-01-09, 934, 922, 866, 444, 235, 999, 789\n
4, 2015-01-09, 45, 56, 78, 23, 44, 90, 9\n
"""

datos_parseados = {}

lista_datos = datos.split("\n")

empresas = lista_datos[0].split(", ")

for i in range(0, len(empresas) - 1, 2):
    datos_parseados[empresas[i + 1]] = {
        "nombre": empresas[i]
    }

for i in range(1, len(lista_datos)):
    if lista_datos[i] != "":
        datos = lista_datos[i].split(", ")
        datos_parseados[datos[0]]["fecha"] = datos[1]
        datos_parseados[datos[0]]["datos"] = datos[2:]

for k, v in datos_parseados.items():
    print(f"{v['nombre']} ({k}): {v['fecha']}")
    print(f"  ".join(v['datos']))