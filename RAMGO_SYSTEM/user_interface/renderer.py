from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from RAMGO_SYSTEM.db_manager import db_manager
import unicodedata
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
    email = request.form['email'].encode('ascii')
    return render_template("insert_product.html")


@app.route('/bootstrap')
def bootstrap():
    return render_template("bootstrap_example.html")


if __name__ == "__main__":
    app.run(debug=True)
