from Funciones import *
print("Menu de Inicio\n")
print("1.Ingresar valores\n2.Promedio\n3.Ordenar de Mayor a Menor\n4.Ordenar de Menor a Mayor\n5.Calcular el producto\n6.salir\n")

arreglo = ingresoDatos()

print("Menu de Inicio\n")
print("1.Ingresar valores\n2.Promedio\n3.Ordenar de Mayor a Menor\n4.Ordenar de Menor a Mayor\n5.Calcular el producto\n6.salir\n")
opcion = input("Escoja una opción\n")

while True:
    if opcion == "1":
        arreglo = ingresoDatos()
        print("Menu de Inicio\n")
        print("1.Ingresar valores\n2.Promedio\n3.Ordenar de Mayor a Menor\n4.Ordenar de Menor a Mayor\n5.Calcular el producto\n6.salir\n")
        opcion = input("Escoja una opción\n")

    if opcion == "2":
        prom = promedio(arreglo)
        print("El promedio de datos es :"+str(prom))
    elif opcion == "3":
        mayor = mayorMenor(arreglo)
        print("El vector ordenado de Mayor a Menor es:\n")
        print(mayor)
    elif opcion =="4":
        menor = menorMayor(arreglo)
        print("El vector ordenado de Menor a Mayor es : \n")
        print(menor)
    elif opcion =="5":
        produc = producto(arreglo)
        print("El producto es :"+str(produc))
    elif opcion == "6":
        break
    print("Menu de Inicio\n")
    print("1.Ingresar valores\n2.Promedio\n3.Ordenar de Mayor a Menor\n4.Ordenar de Menor a Mayor\n5.Calcular el producto\n6.salir\n")
    opcion = input("Escoja una opción\n")

print("Fin del Programa")
