nombreArchivo = input("Ingrese el nombre que desea para el archivo\n")
archivo = open(nombreArchivo+".txt",'a+')
archivo.close()
encabezados = ["ID","Nombre","Apellido","Telefono","Direccion","Mail","Edad"]
for i in encabezados:
    archivo = open(nombreArchivo+".txt",'a+')
    archivo.write(i+" | ")
archivo.write("\n")
archivo.close()
decision = "si"
while decision == "si":
    for i in encabezados:
        datos = input("Ingrese su "+i+" porfavor\n")
        archivo = open(nombreArchivo + ".txt", 'a+')
        archivo.write(datos+" | ")
    archivo.write("\n")
    archivo.close()
    decision = input("Desea ingresar otro usuario?(si-no)\n")
#///////////////////////////////////////////////////////////
def cantidadPalabras():
    archivo = open(nombreArchivo + ".txt", 'r')
    linea = archivo.readlines()
    cantidadPalabras = 0
    for i in linea:
        string = i
        lista = string.split()
        for j in lista:
            if j != "|" or j != "":
                cantidadPalabras += 1
    archivo.close()
    print("La cantidad de palabras(incluyendo numeros) es : " + str(cantidadPalabras))
#/////////////////////////////////////////////
def cantidadLineas():
    cantidadLineas = int(input("Ingrese la cantidad de lineas que desea imprimir\n"))
    conteo = 0
    archivo = open(nombreArchivo + ".txt", 'r')
    linea = archivo.readlines()
    try:
        while conteo <= cantidadLineas:
             print(linea[conteo])
             conteo += 1
    except:
        if  conteo == cantidadLineas:
            pass
        else:
            print("Error linea de registro fuera de rango\n")
    archivo.close()
#/////////////////////////////////////////////////////
def busqueda():
    matrizBusqueda = []
    archivo = open(nombreArchivo + ".txt", 'r')
    linea = archivo.readlines()
    for i in linea:
        vector = i
        vector = vector.split()
        matrizBusqueda.append(vector)
    busquedaId = input("Ingrese ID que desea buscar\n")
    for i in range(len(matrizBusqueda)):
        if busquedaId == matrizBusqueda[i][0]:
            print("Se encuentra en la fila :" + str(i))
            break
    else:
        print("Error, Registro no encontrado\n")
    archivo.close()
archivo = open(nombreArchivo + ".txt", 'r')
total = archivo.readlines()
archivo.close()
menu = """
   ///Gestor de archivos///
   
1.cantidad de palabras
2.cantidad de lineas de registro(total:"""+str(len(total))+""")
3.busqueda de registro mediante ID
4.salir
"""
salir = 0
while salir == 0:
    decision = input(menu)
    if decision == "1":
        cantidadPalabras()
    elif decision == "2":
        cantidadLineas()
    elif decision == "3":
        busqueda()
    elif decision == "4":
        salir = 1
