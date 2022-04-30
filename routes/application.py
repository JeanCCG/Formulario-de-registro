from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def login():
    name = request.form.get("nombre")
    apellido =  request.form.get("apellido")
    celular =  request.form.get("celular")
    email =  request.form.get("email")
    fecha =  request.form.get("fecha")
    return render_template(
        "session.html", 
        nombre=name,
        apellido=apellido, 
        celular=celular,
        email=email,
        fecha=fecha,
        )
@app.route("/<string:name>")
def session(name):
    return render_template(
        "session.html", 
        nombre=name,
        )

@app.route("/users")
def names():
    #Query a DB for users.
    name_list = ["Jose", "Pedro", "Maria", "Luis"]
    return render_template(
        "list.html",
        nombres=name_list,
        )