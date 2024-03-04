diccionario_parseo = {
    "Ene": "01",
    "Feb": "02",
    "Mar": "03",
    "Abr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Ago": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dic": "12"
}

def parsear_fecha(fecha: str):
    fecha = fecha.split(" ")
    return fecha[2] + "-" + diccionario_parseo.get(fecha[1]) + "-" + fecha[0]

print(parsear_fecha("12 Feb 2015"))