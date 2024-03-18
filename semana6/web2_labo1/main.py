import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/eco', methods=['POST'])
def eco():
    return flask.request.form.get('eco', 'No hay eco')

if __name__ == '__main__':
    app.run()
