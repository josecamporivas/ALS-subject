# Conjuntos: colecciones de objetos desordenados que no se repiten
conj = set()
conj2 = {1, 2, 3}

if 1 in conj2:
    print("El 1 está en el conjunto")

conj3 = {1, 2, 3, 4, 5}

print(conj2 | conj3)  # Unión
print(conj2 & conj3)  # Intersección
print(conj2 - conj3)  # Diferencia
print(conj3 > conj2)  # Subconjunto
