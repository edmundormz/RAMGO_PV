from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import RAMGO_SYSTEM.db_manager.db_manager as db

import ipdb


app = Flask(__name__)
Bootstrap(app)

current_product_id = 0

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


@app.route('/consult_product_view')
def consult_product_view():
    return render_template("consult_product_view.html")


@app.route('/consult_product', methods=["POST"])
def consult_product():
    product_details = db.DBManager().consular_producto(nombre_producto=request.form['nombre'].encode('ascii'))
    return render_template("consult_product.html",
                           id_producto=product_details[0],
                           nombre=product_details[1],
                           costo=product_details[2],
                           precio=product_details[3],
                           cantidad=product_details[4])


@app.route('/modify_product_view', methods=["POST"])
def modify_product_view():
    updated_product = db.DBManager().modify_product(id_producto=request.form['id_producto'].encode('ascii'),
                                                    nombre=request.form['nombre'].encode('ascii'),
                                                    costo=request.form['costo'].encode('ascii'),
                                                    precio=request.form['precio'].encode('ascii'),
                                                    stock=request.form['cantidad'].encode('ascii'))
    return render_template("modify_product_view.html",
                           id_producto=updated_product[0],
                           nombre=updated_product[1],
                           costo=updated_product[2],
                           precio=updated_product[3],
                           cantidad=updated_product[4])



# @app.route('/modify_product', methods=["POST"])
# def modify_product():
#     pass


if __name__ == "__main__":
    app.run(debug=True)
