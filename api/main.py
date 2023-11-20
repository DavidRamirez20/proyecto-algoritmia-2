from flask import Flask, render_template, request
import math

app = Flask(__name__)

class Engranaje:

   def __init__(self, modulo, dientes, material):
      self.modulo = modulo
      self.dientes = dientes
      self.material = material
      self.resultado = []

   def modelado(self):
      a = round(self.modulo,2)
      d = round(self.modulo * 1.25,2)
      Ht = round(a + d,2)
      R = round(d - a,2)
      r = round(0.20 * self.modulo,2)
      Pc = round(math.pi * self.modulo,2)
      e = round(0.49 * Pc,2)
      v = round(0.51 * Pc,2)
      dp = round(self.modulo * self.dientes,2)
      de = round(dp + (2*a),2)
      di = round(dp - (2*d),2)
      Dp = round(self.modulo * (2 * self.dientes),2)
      De = round(Dp + (2 * self.modulo),2)
      Di = round(Dp - (2*d),2)
      
      self.resultado = [a,d,Ht,R,r,Pc,e,v,dp,de,di,Dp,De,Di]
      result = self.resultado
      print(result)
      return result
   
gear = Engranaje(0, 0, 'X')
resultado = Engranaje.modelado(gear) 

@app.route("/")
def index():
   return render_template("index.html",gear=gear,resultado=resultado)

@app.route("/calc-gear", methods=["GET", "POST"])
def calc_gear():
   if request.method == "GET":
      return render_template("index.html")
   elif request.method == "POST":
      print(request.form)
      modulo = float(request.form["input1"])
      dientes = float(request.form["input2"])
      material = request.form["input3"]
      
      gear = Engranaje(modulo, dientes, material)
      resultado = Engranaje.modelado(gear)
      print(resultado)
      
      return render_template('index.html', gear=gear, resultado=resultado)

if __name__=="__main__":
   app.run(debug=True)