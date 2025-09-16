"""
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


@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")
"""


from app_spending import app
from flask import render_template, request, redirect
import csv
from datetime import date

@app.route("/")
def index():
    datos=[]
    #llamada al archivo csv
    fichero = open('data/movimientos.csv','r')
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    for items in csvReader:
        datos.append(items)
    """
    datos=[
        {'fecha':'01/09/2025','concepto':'Salario','monto':1500},
        {'fecha':'05/09/2025','concepto':'Ropa','monto':-150},
        {'fecha':'10/09/2025','concepto':'Supermercado','monto':-200}
    ]
    """
    return render_template("index.html",data = datos,titulo="Lista")


@app.route("/new",methods=["GET","POST"])
def new():
    if request.method == "POST":
        if validacion(request.form):
            pass
        mifichero = open("data/movimientos.csv", "a",newline="")
        lectura = csv.writer(mifichero,delimiter=",",quotechar=" ")
        mifichero.close()
        return redirect("/")
    else:
        return render_template("new.html",titulo="Nuevo",tipoAccion="Registro",tipoBoton="Guardar")


@app.route("/delete")
def delete():
    return render_template("delete.html",titulo="Borrar")

@app.route("/update")
def update():
    return render_template("update.html",titulo="Actualizar",tipoAccion="Actualización",tipoBoton="Editar")


def validacion(datosFormulario):
    errores = []
    hoy = str(date.today())
    if datosFormulario["Date"] > hoy:
        errores.append("la fecha no puede ser en el futuro")
    if datosFormulario["Transaction"] == "":
        errores.append("Debe agregar un concepto de transaccion")
    if datosFormulario["Amount"]== "" or datosFormulario["Amount"] == 0:
        errores.append("Introduzca una cantidad valida")        