import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication
from Funciones import *

class claseGui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui",self)
        self.uno.clicked.connect(self.escribir)
        self.dos.clicked.connect(self.escribir)
        self.tres.clicked.connect(self.escribir)
        self.cuatro.clicked.connect(self.escribir)
        self.cinco.clicked.connect(self.escribir)
        self.seis.clicked.connect(self.escribir)
        self.siete.clicked.connect(self.escribir)
        self.ocho.clicked.connect(self.escribir)
        self.nueve.clicked.connect(self.escribir)
        self.cero.clicked.connect(self.escribir)
        self.punto.clicked.connect(self.escribir)
        self.suma.clicked.connect(self.sum)
        self.menos.clicked.connect(self.res)
        self.multiplicacion.clicked.connect(self.mul)
        self.division.clicked.connect(self.di)
        self.igual.clicked.connect(self.resultado)
        self.borrar.clicked.connect(self.delet)
        self.seno.clicked.connect(self.sen)
        self.coseno.clicked.connect(self.cos)
        self.tangente.clicked.connect(self.tan)
        self.inversen.clicked.connect(self.inversaSeno)
        self.invercos.clicked.connect(self.inversaCoseno)
        self.invertan.clicked.connect(self.inversaTangen)



#escribir ///////////////////////////////////////
    def escribir(self):
        global cadena
        sender = self.sender()
        cadena = cadena + sender.text()
        self.pantalla.setText(cadena)

#borrar ////////////////////////////////////////
    def delet(self):
        global cadena
        valor = ""
        for i in cadena[0:len(cadena)-1]:
            valor = valor + i
        self.pantalla.setText(str(valor))
        cadena = valor
#operaciones comunes /////////////////////////////////////////////
    def sum(self):
        global cifra
        global sender
        global cadena
        sender = "+"
        cifra = cadena
        self.pantalla.setText("")
        cadena =""
    def res(self):
        global cifra
        global sender
        global cadena
        sender = "-"
        cifra = cadena
        self.pantalla.setText("")
        cadena = ""
    def mul(self):
        global cifra
        global sender
        global cadena
        sender = "*"
        cifra = cadena
        self.pantalla.setText("")
        cadena = ""
    def di(self):
        global cifra
        global sender
        global cadena
        sender = "%"
        cifra = cadena
        print(cifra)
        self.pantalla.setText("")
        cadena = ""
# el igual /////////////////////////////////////////////////////////////////////////
    def resultado(self):
        global cifra
        global  cadena
        a = float(cifra)
        b = float(cadena)
        if  sender == "+":
             resultado = suma(a,b)
             self.pantalla.setText(str(resultado))
             cifra =""
             cadena =""
        elif sender =="-":
            resultado = resta(a,b)
            self.pantalla.setText(str(resultado))
            cifra = ""
            cadena = ""
        elif sender =="*":
            resultado = multi(a,b)
            self.pantalla.setText(str(resultado))
            cifra = ""
            cadena = ""
        if sender == "%":
            resultado = divi(cifra,cadena)
            self.pantalla.setText(str(resultado))
            cifra = ""
            cadena = ""
#funciones trigonometricas ////////////////////////////////////////////////////////
    def sen(self):
        global cadena
        self.pantalla.setText("")
        a = float(cadena)
        resultado = seno(a)
        self.pantalla.setText(str(resultado))
        cadena =""
    def cos(self):
        global cadena
        self.pantalla.setText("")
        a = float(cadena)
        resultado = coseno(a)
        self.pantalla.setText(str(resultado))
        cadena =""
    def tan(self):
        global cadena
        self.pantalla.setText("")
        a = float(cadena)
        resultado = tangente(a)
        self.pantalla.setText(str(resultado))
        cadena =""
#funciones inversas////////////////////////////////////////////////////
    def inversaSeno(self):
        global cadena
        a = float(cadena)
        resultado = senoInver(a)
        self.pantalla.setText(str(resultado))
        cadena =""
    def inversaCoseno(self):
        global cadena
        a = float(cadena)
        resultado =  coseInver(a)
        print(resultado)
        self.pantalla.setText(str(resultado))
        cadena = ""
    def inversaTangen(self):
        global cadena
        a = float(cadena)
        resultado = tanInver(a)
        print(resultado)
        self.pantalla.setText(str(resultado))
        cadena = ""

if __name__=='__main__':
    cadena = ""
    cifra = ""
    sender = ""
    app = QApplication(sys.argv)
    GUI = claseGui()
    GUI.show()
    sys.exit(app.exec_())
