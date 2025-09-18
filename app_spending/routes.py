
from app_spending import app
from flask import render_template, request, redirect
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
    ident = []
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
               
           
"""            
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    reg = []
    if request.method == "GET":
        with open("data/movimientos.csv", "r", encoding="utf-8") as r:
        
            csvReader = csv.reader(r, delimiter=",", quotechar='"' )
            for i in csvReader:
                if i[0] == str(id):
                    reg = i
        return render_template("update.html", datos = reg)
    elif request.method == "POST":
        with open("data/movimientos.csv", "a", encoding="utf-8") as r:
            csvReader = csv.reader(r, delimiter=",", quotechar='"' )
            for i in csvReader:
                if i[0] == id:
                    i[1] = request.form[1]
                    i[2] = request.form[2]
                    i[3] = request.form[3]
                    writer = csv.writer(r) 
                    writer.writerow([i[0],i[1],i[2], i[3]])       

        return render_template("update.html", datos = reg)
"""
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    reg = []
    if request.method == "GET":
        # Abrimos el CSV en modo lectura
        with open("data/movimientos.csv", "r", encoding="utf-8") as r:
            csvReader = csv.reader(r, delimiter=",", quotechar='"')
            for i in csvReader:
                if i[0] == str(id):  # buscamos por ID
                    reg = i
        return render_template("update.html", datos=reg)

    elif request.method == "POST":
        filas = []
        # Primero leemos todas las filas del CSV
        with open("data/movimientos.csv", "r", encoding="utf-8") as r:
            csvReader = csv.reader(r, delimiter=",", quotechar='"')
            for i in csvReader:
                if i[0] == str(id):  # si es el registro a actualizar
                    # remplazamos los valores con los del formulario
                    i[1] = request.form["Date"]
                    i[2] = request.form["Transaction"]
                    i[3] = request.form["Amount"]
                    reg = i
                filas.append(i)  

        
        if validacion(request.form) == True:
            with open("data/movimientos.csv", "w", newline="", encoding="utf-8") as w:
                writer = csv.writer(w, delimiter=",", quotechar='"')
                writer.writerows(filas)
        else:
            return render_template("update.html", datos = reg, error = validacion(request.form))    

        return redirect("/")


    
        

@app.route("/delete/<int:id>",  methods=["GET", "POST"])
def delete(id):
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