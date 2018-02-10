from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/insert_product')
def insert_product():
    return render_template("insert_product.html")


@app.route('/bootstrap')
def bootstrap():
    return render_template("bootstrap_example.html")


if __name__ == "__main__":
    app.run(debug=True)
