
from app_spending import app
from flask import render_template, request
import csv
from datetime import date
num = 1
last_num = 0
@app.route("/")
def index():
    datos=[]
    with open("data/movimientos.csv", "r", encoding="utf-8") as f:
        csvReader = csv.reader(f, delimiter=",", quotechar='"')
        for i in csvReader:
            datos.append(i)
    return render_template("index.html", data = datos)

@app.route("/new", methods=["GET", "POST"])
def new():
    render = render_template("new.html")
    ident = [0]
    with open("data/movimientos.csv", "r", encoding="utf-8") as f:
        csvReader = csv.reader(f, delimiter=",", quotechar='"')
        
        for i in csvReader:
            ident.append(i[0])

   
    
    if request.method == "GET":
        return render_template("new.html")
    else:
        with open("data/movimientos.csv", "a", newline="", encoding="utf-8") as f:
           
               
           
            
            writer = csv.writer(f)
            if validacion(request.form) == True:
                
                writer.writerow([(int(ident[-1]) +1 or 0),request.form["Date"],request.form["Transaction"], request.form["Amount"]])
                
            else:
               render = render_template("new.html", error = validacion(request.form))    
    return render
@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")

def validacion(datosFormulario):
    errores = []
    hoy = str(date.today())
    if datosFormulario["Date"] > hoy:
        errores.append("la fecha no puede ser en el futuro")
    if datosFormulario["Transaction"] == "":
        errores.append("Debe agregar un concepto de transaccion")
    if datosFormulario["Amount"]== "" or datosFormulario["Amount"] == 0:
        errores.append("Introduzca una cantidad valida")        

    if errores == []:
        return True 
    else:
        return errores