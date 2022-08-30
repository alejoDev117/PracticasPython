import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5 import QtWidgets

class TrabajoGui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana.ui",self)
        self.buscar.clicked.connect(self.search)
        self.crear.clicked.connect(self.new)
        self.inversa.clicked.connect(self.inv)
#/////////////////////////////////////////////////////////////////////////
    def search(self):
        global matriz
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, options = options)
        if fileName:
            self.urlentrada.setText(str(fileName))
            archivo = open(fileName)
            texto = archivo.read()
            self.original.setText(str(texto))
            temporal = ""
            matriz = []
            vector2 = []
            filas = 1
            columnas = 0
            f = 0
            for i in texto:# meto todos los elementos en un vector
                if i !=" " and i != "\n":
                    try:
                     vector2.append(int(i))
                    except:
                        print("Error caracter no valido")
                        break
            for i in texto:#conteo de las columnas
                if i == " ":
                    columnas += 1
                if i == "\n":
                    break
            for i in texto:#conteo de las filas
                if i == "\n":
                    filas +=1
            print(columnas,filas)
            for i in range(filas): # Creacion de la matriz
                matriz.append([0]*(columnas))
            n = 0
            for i in range(filas):#matriz llena con elementos ya operativa :D
               for j in range(columnas):
                   matriz[i][j] = vector2[n]
                   n +=1

#/////////////////////////////////////////////////////////////////////
    def inv(self):
        a = np.linalg.inv(matriz)
        print(a)
#/////////////////////////////////////////////////////////////////
    def new(self):
        global nombreArchivo
        contenido = "Matriz Original\n"+(self.original.toPlainText())
        nombreArchivo = self.salida.text()
        archivoSalida = open(nombreArchivo,"wt")
        archivoSalida.write(contenido)
        archivoSalida.close()
#////////////////////////////////////////////////////////




if __name__== '__main__':
    nombreArchivo = ""
    vector2 =[]
    app = QApplication(sys.argv)
    GUI = TrabajoGui()
    GUI.show()
    sys.exit(app.exec_())