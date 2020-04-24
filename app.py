from flask import Flask, render_template
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def principal():
    nombre = "Desconocido"
    return render_template("principal.html",nombre=nombre)

@app.route('/<cadena>',methods=["GET","POST"])
def saludo(cadena):
    nombre = cadena
    return render_template("principal.html",nombre=nombre)

app.run(debug=True)