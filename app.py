from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dataset")
def dataset():
    return render_template("dataset.html")

@app.route("/problematica")
def problematica():
    return render_template("problematica.html")
