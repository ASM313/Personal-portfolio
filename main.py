from distutils.log import debug
from flask import Flask, redirect, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True)
