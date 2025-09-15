from app_spending import app
from flask import render_template

@app.route("/")
def index():
    datos=[
        {"Date":"12/09/25", "Transaction": "Compra", "Amount": "129.90"},
        {"Date":"13/09/25", "Transaction": "Compra", "Amount": "29.90"},
        {"Date":"14/09/25", "Transaction": "Compra", "Amount": "9.90"}

    ]
    return render_template("index.html", data = datos)

@app.route("/new")
def new():
    return render_template("new.html")