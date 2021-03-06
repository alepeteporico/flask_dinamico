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

@app.route('/potencia/<int:base>/<int:exponente>',methods=["GET","POST"])
def calculadora(base,exponente):
    base= base
    exponente= exponente
    if exponente==0:
        resultado=1

    elif exponente>0:
        resultado=base**exponente

    elif exponente<0:
        resultado=1/base**exponente
    return render_template("calculadora.html",base=base,exponente=exponente,resultado=resultado)

@app.route('/cuenta/<palabra>/<letra>',methods=["GET","POST"])
def cuenta_letras(palabra,letra):
    palabra=palabra
    letra=letra
    if type(letra)==str:
        num=palabra.count(letra)
    else:
        abort(404)
    return render_template("letras.html",palabra=palabra,letra=letra,num=num)

app.run(debug=True)