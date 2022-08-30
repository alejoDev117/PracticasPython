def ingresoDatos():
    d = "si"
    lista = []
    while d == "si":
        n = float(input("Ingrese dato numerico\n"))
        lista.append(n)
        d = input("Desea ingresar otro dato?\nsi--no\n")
    return lista
#/////////////////////////////////////////////////////////
def promedio(a):
    suma = 0
    for i in a :
        suma = suma + i
    pro = suma / len(a)
    return pro
#//////////////////////////////////////////////////////////////
def mayorMenor(a):
    for r in range(1,len(a)):
        for p in range(len(a)-r):
            if a[p]<a[p+1]:
                temp = a[p]
                a[p] = a[p+1]
                a[p+1] = temp
    return a
#/////////////////////////////////////////////////////////////////////
def menorMayor(a):
    for r in range(1,len(a)):
        for p in range(len(a)-r):
            if a[p]>a[p+1]:
                temp = a[p]
                a[p] = a[p+1]
                a[p+1] = temp
    return a
#/////////////////////////////////////////////////////////////////////////
def producto(a):
    multi = 1
    for i in a:
        multi = multi * i
    return multi
