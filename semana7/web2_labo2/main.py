import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/factura", methods=["POST"])
def crear_factura():
    data_emisor_cliente = get_data_form_emisor_cliente()
    lines_data = get_data_form_lines()
    iva = flask.request.form.get("iva")
    if not iva.isdigit():
        iva = 21
    importe_bruto = sum([line.get("total") for line in lines_data])
    importe_total = importe_bruto * int(100 + iva) / 100

    return flask.render_template("factura.html", **data_emisor_cliente, lines=lines_data, iva=iva, importe_bruto=importe_bruto, importe_total=importe_total)


def get_data_form_emisor_cliente() -> dict:
    data = {
        "emisor": {},
        "cliente": {}
    }
    for key in flask.request.form:
        if key.endswith("emisor"):
            data["emisor"][key] = flask.request.form.get(key)
        elif key.endswith("cliente"):
            data["cliente"][key] = flask.request.form.get(key)

    return data

def get_data_form_lines() -> list:
    lines = []
    index_line = 1
    while flask.request.form.get(f"concepto_{index_line}") is not None:
        data_line = {
            "concepto": flask.request.form.get(f"concepto_{index_line}"),
            "cantidad": flask.request.form.get(f"cantidad_{index_line}"),
            "precio": flask.request.form.get(f"precio_{index_line}")
        }
        if data_line.get("cantidad").isdigit() and data_line.get("precio").isdigit():
            data_line["total"] = int(data_line.get("cantidad")) * int(data_line.get("precio"))
        else:
            data_line["total"] = 0
        lines.append(data_line)
        index_line += 1

    return lines


if __name__ == "__main__":
    app.run()
