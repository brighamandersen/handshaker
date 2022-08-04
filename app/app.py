from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/apply", methods=["POST"])
def apply():
    username = request.form["username"]
    password = request.form["password"]
    query = request.form["query"]
    print("here", username, password, query)
    return None


@app.route("/done")
def done():
    return render_template("done.html")


@app.route("/hello/<name>")
def hello(name):
    print("name", name)
    print()
    print()
    if name is None:
        return "<h1>Make sure to provide a name in the URL</h1>"
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
