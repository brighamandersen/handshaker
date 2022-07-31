from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/<name>")
def hello(name):
    print("name", name)
    print()
    print()
    if name is None:
        return "<h1>Make sure to provide a name in the URL</h1>"
    return render_template("hello.html", name=name)
