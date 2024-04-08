import flask
from model.Mensaje import Mensaje
import sirope

app = flask.Flask(__name__)
srp = sirope.Sirope()

@app.route('/')
def index():
    # return app.send_static_file('index.html')
    mensajes = srp.load_last(Mensaje, 10)

    return flask.render_template('index_template.html', mensajes=mensajes)

@app.route('/saludo', methods=['POST'])
def saludo():
    nombre = flask.request.form.get('name')
    mensaje = flask.request.form.get('mensaje')

    if not nombre:
        nombre = "Anónimo"

    if not mensaje:
        mensaje = "Mensaje vacío"

    data = Mensaje(nombre, mensaje)
    srp.save(data)

    return flask.redirect('/')

if __name__ == '__main__':
    app.run()
