from flask import Flask, render_template, request, redirect, url_for
import os

from utils.handshake import handshake

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

    print("handshaking")
    # temporary
    username = os.environ.get("BYU_USERNAME")
    password = os.environ.get("BYU_PASSWORD")
    # print("here", username, password, query)
    result = handshake(username, password, query, True)
    print("res", result)
    print("finished handshake")
    print("ja", result.jobs_applied)
    # We'll want it to go to an intermediate page
    # return redirect(url_for("done"), jobs_applied=result.jobs_applied, job_query=query)
    return render_template(
        "done.html", jobs_applied=result.jobs_applied, job_query=query
    )


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
