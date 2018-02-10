from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import RAMGO_SYSTEM.db_manager.db_manager as db

import ipdb

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/insert_product_view')
def insert_product_view():
    return render_template("insert_product.html")


@app.route('/insert_product', methods=["POST"])
def insert_product():
    db.DBManager().insert_product(nombre=request.form['nombre'].encode('ascii'),
                                  costo=request.form['costo'].encode('ascii'),
                                  precio=request.form['precio'].encode('ascii'),
                                  stock=request.form['cantidad'].encode('ascii'))
    return render_template("insert_product.html")


if __name__ == "__main__":
    app.run(debug=True)
