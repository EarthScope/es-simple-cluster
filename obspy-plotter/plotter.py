from flask import Flask, send_file, redirect, request, render_template, flash
from mpl_plotter import Plotter
from urllib.parse import urlencode

app = Flask(__name__)
app.secret_key = b'3)\xe2z\x1f\xcd\xd3\x1c\xb5\x04\\j\xe6\x0b02'

plotter = Plotter()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/plot")
def plot():
    request_args = {}
    for arg in ('net', 'sta', 'loc', 'cha', 'start', 'end'):
        arg_value = request.args.get(arg)
        if arg_value:
            request_args[arg] = arg_value
        else:
            flash("Missing %s" % arg)
            return render_template('index.html')
    png = plotter.plot_from_query(**request_args)
    return send_file(png, mimetype='image/png')
    

    