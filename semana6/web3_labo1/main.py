import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/conversor', methods=['POST'])
def conversor():
    try:
        grados = float(flask.request.form.get('temperatura'))
    except Exception:
        return 'Error: el valor ingresado no es un número.'
    resultado = (grados * 9 / 5) + 32
    return f'{grados} grados Celsius son {resultado} grados Fahrenheit.'

if __name__ == '__main__':
    app.run()
