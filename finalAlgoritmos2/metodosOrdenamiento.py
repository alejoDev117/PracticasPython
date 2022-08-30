from Funciones import  *
menu = """
Metodos de ordenamiento 
1.burbuja
2.seleccion
3.insercion
4.shell
5.Merge sort 
6.salida
<=>
"""
a = 0
conteo = 0
while True:
    lista = []
    decision = "si"
    while decision == "si":
        numero = int(input("Ingrese un numero \n"))
        lista.append(numero)
        decision = input("Desea ingresar otro numero(no repetido)?(si,no)\n")
    for i in lista:
       a = lista.count(i)
       if a >1:
           print("Error, Elementos de la lista repetidos\nVuelva a ingresar la lista\n")
           conteo +=1
           break
    if conteo == 0:
        break
    conteo = 0

salida = 0
while salida == 0 :
    decision = input(menu)
    if decision == '1' :
        burbuja(lista)
    elif decision == '2':
        seleccion(lista)
    elif decision == '3':
        insercion(lista)
    elif decision == '4':
        Shell(lista)
    elif decision == '5':
        vectorPrueba = []
        vectorPrueba.extend(lista)
        print("Ordenamiento por Merge Sort\n")
        mergeSort(vectorPrueba)
    elif decision == '6':
        salida = 1
