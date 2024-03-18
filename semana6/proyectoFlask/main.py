# Hola mundo con Flask

import flask

app = flask.Flask(__name__)

@app.route("/")
def main():
    return app.send_static_file("index.html")

@app.route("/saludo", methods=["POST"])
def saludo():
    NOMBRE_POR_DEFECTO = "Anónimo"

    nombre = flask.request.form.get("nombre", NOMBRE_POR_DEFECTO).strip()
    if not nombre:
        nombre = NOMBRE_POR_DEFECTO

    return f"Hola {nombre}"


if __name__ == "__main__":
    app.run()

"""
$flask run    # Ejecutar la app
$flask routes # Ver las rutas de la app

"""