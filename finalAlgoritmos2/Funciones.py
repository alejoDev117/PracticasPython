import time
from animaciones import *
#/////////////////////////////////////////////////////////////////////////////////////////
def burbuja(vector1):
    contadorIntercambios = 0
    contadorComparaciones = 0
    vectorPrueba = []
    vectorPrueba.extend(vector1)
    print("Ordenamiento por burbuja\n")
    print(vector1)
    for i in range(len(vectorPrueba)):
        for j in range(len(vectorPrueba) - 1):
            contadorComparaciones +=1
            if vectorPrueba[j] > vectorPrueba[j + 1]:
                anterior = vectorPrueba[j]
                posterior = vectorPrueba[j+1]
                time.sleep(1)
                animacionBurbuja(vectorPrueba,anterior,posterior,j,j+1)
                aux = vectorPrueba[j]
                vectorPrueba[j] = vectorPrueba[j + 1]
                vectorPrueba[j + 1] = aux
                time.sleep(1)
                animacionBurbuja(vectorPrueba,anterior,posterior,j,j+1)
                aux = 0
                contadorIntercambios +=1
    print(vectorPrueba)
    print("Estabilidad : Si")
    print("Total comparaciones : "+str(contadorComparaciones))
    print("Total intercambios : "+str(contadorIntercambios))
    vectorPrueba =[]
#////////////////////////////////////////////////////////////////////////////////////
def seleccion(lista):
    contadorIntercambios = 0
    contadorComparaciones = 0
    vectorPrueba = []
    vectorPrueba.extend(lista)
    print("Ordenamiento por seleccion\n")
    print(lista)
    for i in range(len(vectorPrueba)):
        minimo = i
        auxiliar = minimo
        for j in range(i, len(vectorPrueba)):
            if (vectorPrueba[j] < vectorPrueba[minimo]):
                minimo = j
            contadorComparaciones += 1
        time.sleep(1)
        animacionSeleccion(vectorPrueba,auxiliar,minimo)
        if (minimo != i):
            aux = vectorPrueba[i]
            vectorPrueba[i] = vectorPrueba[minimo]
            vectorPrueba[minimo] = aux
            contadorIntercambios +=1
    print(vectorPrueba)
    print("Estabilidad : No")
    print("Total comparaciones : " + str(contadorComparaciones))
    print("Total intercambios : " + str(contadorIntercambios))
    vectorPrueba = []
#/////////////////////////////////////////////////////////////////////////////////////
def insercion(lista):
    contadorIntercambios = 0
    contadorComparaciones = 0
    vectorPrueba = []
    vectorPrueba.extend(lista)
    print("Ordenamiento por inserccion\n")
    print(vectorPrueba)
    for i in range(len(vectorPrueba)):
        time.sleep(1)
        animacionInsercion(vectorPrueba, i)
        for j in range(i, 0, -1):
            contadorComparaciones +=1
            if (vectorPrueba[j - 1] > vectorPrueba[j]):
                aux = vectorPrueba[j]
                vectorPrueba[j] = vectorPrueba[j - 1]
                vectorPrueba[j - 1] = aux
                contadorIntercambios += 1
    print(vectorPrueba)
    print("Estabilidad : Si")
    print("Total comparaciones : " + str(contadorComparaciones))
    print("Total intercambios : " + str(contadorIntercambios))
    vectorPrueba = []
#/////////////////////////////////////////////////////////////////////////////////////////////////////////
def Shell(lista):
    contadorIntercambios = 0
    contadorComparaciones = 0
    vectorPrueba = []
    vectorPrueba.extend(lista)
    print("Ordenamiento por Shell\n")
    print(vectorPrueba)
    mitad = len(vectorPrueba) // 2
    while mitad > 0:
        for i in range(mitad, len(vectorPrueba)):
            temp = vectorPrueba[i]
            j = i
            primero = temp
            segundo = vectorPrueba[j-mitad]
            time.sleep(1)
            animacionShell(vectorPrueba, mitad, primero,segundo)
            contadorComparaciones += 1
            while j>=mitad and vectorPrueba[j-mitad] > temp:
                vectorPrueba[j] = vectorPrueba[j-mitad]
                j = j-mitad
                contadorIntercambios +=1
            vectorPrueba[j] = temp
        mitad = mitad//2
    print(vectorPrueba)
    print("Estabilidad : No")
    print("Total comparaciones : " + str(contadorComparaciones))
    print("Total intercambios : " + str(contadorIntercambios))
    vectorPrueba = []
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
string = ""
def mergeSort(lista):
    if len(lista) == 1:
        return lista
    elif len(lista) > 1:
        mitad = len(lista) // 2
        primeraMitad = lista[:mitad]
        segundaMitad = lista[mitad:]
        time.sleep(1)
        animacionMergeSort(primeraMitad, segundaMitad , lista ,string,0)
        mergeSort(primeraMitad)
        mergeSort(segundaMitad)
        i = 0
        j = 0
        k = 0
        while i < len(primeraMitad) and j < len(segundaMitad):
            if primeraMitad[i] < segundaMitad[j]:
                lista[k] = primeraMitad[i]
                i += 1
            else:
                lista[k] = segundaMitad[j]
                j += 1
            k += 1
        while i < len(primeraMitad):
            lista[k] = primeraMitad[i]
            i +=1
            k +=1
        while j < len(segundaMitad):
            lista[k] = segundaMitad[j]
            j +=1
            k +=1
        time.sleep(1)
        animacionMergeSort(primeraMitad,segundaMitad, lista ,string,1)
    return lista

