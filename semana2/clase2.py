# Funciones
def nombre_function():
    print('Hola mundo')
    pass  # Marca el final de la función, no es necesario ponerlo

nombre_function()  # Devuelve None

def suma(a, b):
    return a + b

print(suma(2, 3))  # 5

# Paso de parámetros: se pasa la referencia por copia (por valor). Es definitiva, excepto los tipos básicos, todos
# los pasos son por referencia
def dobla(a):
    a *= 2

x = 2
dobla(x)
print(x)  # 2

# Cadenas de caracteres
nombre = "ALS"
print(nombre[1:])  # LS
print(nombre[::-1])  # SLA

# Listas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[1::2])  # [2, 4, 6, 8, 10]

lista[3:6] = [40, 50, 60]
print(lista)  # [1, 2, 3, 40, 50, 60, 7, 8, 9, 10]

lista_heterogenea = ["ALS", 4.5, True]
print(lista_heterogenea)  # ['ALS', 4.5, True]
lista_heterogenea.append(5)
print(lista_heterogenea)  # ['ALS', 4.5, True, 5]
lista_heterogenea.pop()
print(lista_heterogenea)  # ['ALS', 4.5, True]

# Matrices: listas bidimensionales
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][2])  # 6

# Tuplas: listas inmutables
tupla = (5,)  # Tupla con un valor, se pone la coma para que no interprete como un entero
tupla_2 = (1, 2, 3, 4, 5)

# Diccionarios
diccionario = {'nombre': 'ALS', 'edad': 22}
print(diccionario['nombre'])  # ALS
print(diccionario.get('edad'))  # 22

if not diccionario.get('apellido'):
    print('No tiene apellido')
else:
    print(diccionario['apellido'])

