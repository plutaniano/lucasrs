#! /usr/bin/env python3

from flask import Flask, render_template

HOST = "0.0.0.0"
PORT = 8000

app = Flask(__name__, static_url_path="/static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cv")
def resume():
    return render_template("cv.html")


if __name__ == "__main__":
    app.run(HOST, PORT, debug=True)
