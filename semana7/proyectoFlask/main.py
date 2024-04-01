import flask
from datetime import datetime

app = flask.Flask(__name__)

@app.route("/")
def main():
    return app.send_static_file("index.html")

@app.route("/saludo", methods=["POST"])
def saludo():
    NOMBRE_DEFAULT = "desconocido"
    nombre = flask.request.form.get("nombre", NOMBRE_DEFAULT)
    if not nombre:
        nombre = NOMBRE_DEFAULT

    hora = datetime.now()
    valores = {
        "nombre_persona": nombre,
        "hora": [hora.hour, hora.minute, hora.second]
    }

    return flask.render_template("respuesta.html", **valores)

@app.route("/saludo/<nombre>")
def saludo_nombre(nombre):
    return f"Hola, {nombre}"

if __name__ == "__main__":
    app.run(debug=False)
