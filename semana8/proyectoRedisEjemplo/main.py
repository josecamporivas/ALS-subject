import flask
from model.Mensaje import Mensaje
from model.User import User
import sirope
import flask_login
import json


def create_app():
    lmanager = flask_login.login_manager.LoginManager()
    flapp = flask.Flask(__name__)
    sirp = sirope.Sirope()

    flapp.config.from_file("cfg/config.json", load=json.load)
    lmanager.init_app(flapp)
    return flapp, sirp, lmanager

app, srp, lm = create_app()

@lm.user_loader
def load_user(id: str) -> User:
    return User.find(srp, id)

@lm.unauthorized_handler
def unauthorized():
    flask.flash("Unauthorized")
    return flask.redirect('/')

@app.route('/')
def index():
    # return app.send_static_file('index.html')
    mensajes = srp.load_last(Mensaje, 10)

    return flask.render_template('index_template.html', mensajes=mensajes)

@app.route('/saludo', methods=['POST'])
def saludo():
    # nombre = flask.request.form.get('name')
    email = flask.request.form.get('email', "").strip()
    password = flask.request.form.get('password', "").strip()
    mensaje = flask.request.form.get('mensaje')

    # if not nombre:
    #     nombre = "Anónimo"

    usr = User.find(srp, email)

    if usr:
        if not usr.compara_password(password):
            flask.flash("usuario no reconocido")
            return flask.redirect('/')
    else:
        usr = User(email, password)
        srp.save(usr)

    flask_login.login_user(usr)

    if not mensaje:
        mensaje = "Mensaje vacío"

    data = Mensaje(usr.email, mensaje)
    srp.save(data)

    flask_login.logout_user()
    return flask.redirect('/')

if __name__ == '__main__':
    app.run()

# $ pip install flask-login
# python -c "import uuid; print(uuid.uuid4())"
# TODO: ver Blueprints para el proyecto