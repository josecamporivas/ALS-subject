"""
Frecuencia de palabras en un archivo de texto

Dado un archivo de texto, leyendo su contendio
1º leer esei.txt
y simplemente separando por espacios,
2º str.split()
mostrar la frecuencia de cada palabra en el archivo.
3º utlizar un diccionario para almacenar las apariciones
"""
def frecuencia_palabras(nf: str):
    toret = {}
    with open(nf, "rt", encoding='utf-8') as f:
        for linea in f:
            palabras = linea.replace(".", "").replace(",", "").strip().lower().split(" ")
            for palabra in palabras:
                if palabra in toret:
                    toret[palabra] += 1
                else:
                    toret[palabra] = 1
    return toret

if __name__ == "__main__":
    dict_frec = frecuencia_palabras("esei.txt")
    for i in dict_frec:
        print(f"{i}: {dict_frec[i]}")
