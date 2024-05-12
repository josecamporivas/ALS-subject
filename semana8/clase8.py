from Waypoint import Waypoint
import csv
import json
import pickle

def escribir_texto(nf: str, w: Waypoint):
    t = str(w)
    """
    funcion open:
    1º parametro: nombre del archivo
    2º parametro: modo de apertura
        r -> read    t -> text
        w -> write   b -> binary
        a -> append
    """
    with open(nf, "wt", encoding='utf-8') as f:
        f.write(t)

def leer_archivo(nf: str):
    toret = []
    with open(nf, "rt") as f:
        for linea in f:
            toret.append(linea)

    print(str.join("\n", toret))

def csv_from_waypoint(w: Waypoint):
    return [w.nombre, w.lat, w.lon]

def escribir_archivo_csv(nf: str, l: list):
    with open(nf, "wt") as f:
        writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_NONNUMERIC, lineterminator="\n")
        writer.writerow(["nombre", "lat", "lon"])
        writer.writerows(l)


def leer_archivo_csv(nf: str):
    toret = []
    with open(nf, "rt") as f:
        reader = csv.DictReader(f, fieldnames=['nombre', 'lat', 'lon'], delimiter=";")
        for row in reader:
            toret.append(row)

    print(toret)

def json_from_waypoint(w: Waypoint):
    return {"nombre": w.nombre, "lat": w.lat, "lon": w.lon}

def escribir_json(nf: str, l: list):
    with open(nf, "wt") as f:
        json.dump(l, f)

def leer_json(nf: str):
    toret = []
    with open(nf, "rt") as f:
        toret = json.load(f)

    print(toret)

def archivo_pickle(nf: str, l: list):
    with open(nf, "wb") as f:
        pickle.dump(l, f)

    with open(nf, "rb") as f:
        toret = pickle.load(f)

    print(toret)

if __name__ == "__main__":
    null_island = Waypoint.el0_0()
    escribir_texto("waypoint.txt", null_island)
    leer_archivo("waypoint.txt")

    l = [csv_from_waypoint(null_island)]
    escribir_archivo_csv("waypoint.csv", l)
    leer_archivo_csv("waypoint.csv")

    l = [json_from_waypoint(null_island)]
    escribir_json("waypoint.json", l)
    leer_json("waypoint.json")

    archivo_pickle("waypoint.pkl", l)