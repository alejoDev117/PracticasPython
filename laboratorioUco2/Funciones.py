def tamanoCadena(a):
    resul = len(a) #Cantidad de caracteres del string
    return  resul
#///////////////////////////////////////////////////////////////////////////////
def espacioCadena(a):
    a = a.count("")  #Cantidad de espacios de la cadena de caracteres
    return  a
#////////////////////////////////////////////////////////////////
def cantidadVocales(a):
    resul = 0 #cantidad de vocales
    b = a.lower()
    vocalA = b.count("a")
    vocalA2 = b.count("á")
    vocalE = b.count("e")
    vocalE2 = b.count("é")
    vocalI = b.count("i")
    vocalI2 = b.count("í")
    vocalO = b.count("o")
    vocalO2 = b.count("ó")
    vocalU = b.count("u")
    vocalU2 = b.count("ú")
    resul = vocalA + vocalA2 + vocalE + vocalE2 + vocalI + vocalI2 + vocalO + vocalO2 + vocalU + vocalU2
    return  resul
#////////////////////////////////////////////////////////////////////////////////
def vectorDeVocales(a):#en un vector la cantidad de vocales del texto
     vectorA =[]
     vectorE =[]
     vectorI =[]
     vectorO =[]
     vectorU =[]
     for i in a:
         if i =="a" or i =="á" or i =="A" or i =="Á":
             vectorA.append(i)
         elif i =="e" or i=="é" or i =="E" or i =="É":
             vectorE.append(i)
         elif i =="i" or i =="í" or i =="I" or i =="Í":
             vectorI.append(i)
         elif i =="o" or i =="ó" or i =="O" or i =="Ó":
             vectorO.append(i)
         elif i =="u" or i =="ú" or i =="U" or i =="Ú":
             vectorU.append(i)
     print("Las vocales a del texto :"+str(vectorA))
     print("Las vocales e del texto :"+str(vectorE))
     print("Las vocales i del texto :"+str(vectorI))
     print("Las vocales o del texto :"+str(vectorO))
     print("Las vocales u del texto :"+str(vectorU))
#////////////////////////////////////////////////////////////
def cantidadConsonantes(a):
    resul = 0
    b = a.lower() #cantidad de consonantes
    for i in b:
     if i in "bcdfghjklmnñpqrstvxyz":
        resul = resul + 1
    return resul
#//////////////////////////////////////////////////////////////////////////
def cantidadPalabras(a):#cantidad de palabras
    cantidad = a.split()
    resul = len(cantidad)
    return resul
#/////////////////////////////////////////////////////////////////////////////
def soloConsonantes(a):#Imprime solo las consonantes
    resul = ""
    for i in a:
        if i in "bcdfghjklmnñpqrstvxyzBCDFGHJKLMNÑPQRSTVXYZ":
            resul = resul+i
    return resul
#//////////////////////////////////////////////////////////////////////////////////
def invertirMayusMinus(a):#Invierte el texto
    b = a.swapcase()
    return b
#///////////////////////////////////////////////////////////////////////////////////
from collections import Counter
def palabraMasFrecuente(a): # la palabra mas frecuente
    palabra = a.split()
    contador = Counter(palabra)
    frecuente = contador.most_common()[0][0]
    print("La palabra mas frecuente es : "+frecuente)
#///////////////////////////////////////////////////////////////////////
def consonanteMasFrecuente(a):
    lista =[]
    for i in a:
        if i in "bcdfghjklmnñpqrstvxyzBCDFGHJKLMNÑPQRSTVXYZ":
            lista.append(i)
    contador = Counter(lista)
    frecuente = contador.most_common()[0][0]
    print("La consonante mas frecuente es :"+frecuente)
#//////////////////////////////////////////////////////////////////////////////////
def buscadorDePalabras(a):
    while True :
        lista = a.split()
        frecuencia = {}
        for i in lista:
            if i in frecuencia:
                frecuencia[i] += 1
            else:
                frecuencia[i] = 1
        buscar = input("Ingrese palabra que desea buscar \nSi desea salir presione 1")
        print("la palabra " + buscar + " se repite :" + str(frecuencia[buscar]))
        if buscar == 1:
            break
