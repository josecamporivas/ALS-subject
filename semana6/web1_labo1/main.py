from datetime import datetime

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "La fecha y hora actual es " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")


if __name__ == '__main__':
    app.run()
