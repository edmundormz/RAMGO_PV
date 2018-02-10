from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/insert')
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)