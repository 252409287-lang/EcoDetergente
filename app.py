
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/investigacion")
def investigacion():
    return render_template("investigacion.html")

@app.route("/elaboracion")
def elaboracion():
    return render_template("elaboracion.html")

@app.route("/producto")
def producto():
    return render_template("producto.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

@app.route("/comparativa")
def comparativa():
    return render_template("comparativa.html")


if __name__ == "__main__":
    app.run(debug=True)
