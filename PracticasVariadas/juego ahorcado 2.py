import random
import os
'''
Alejandro Gómez Orjuela
Juan Esteban Cadavid Narvaez 
Alejandro Castaño Acosta 
'''

#Elegir dificultad
eleccion = input("Ingrese la dificultad que desea: facil, medio o dificil\n")
eleccion = eleccion.lower()
print("Tienes 6 vidas")

if eleccion == "facil":
    facil = ["PERRO", "GATO", "CARRO", "MOTO", "OSO", "CAMA"]
    palabra = list(random.choice(facil))


if eleccion == "medio":
    medio = ["BICICLETA", "URBANIZACION", "VENTANAS", "ALGORITMOS", "TELEVISOR"]
    palabra = list(random.choice(medio))

if eleccion == "dificil":
    dificil = ["EUROESCEPTICISMO", "ATICISMO", "RESILIENCIA", "NEFELIBATA", "ZURUMBATICO"]
    palabra = list(random.choice(dificil))

horca = ["          !=====N",
         "                N",
         "                N",
         "                N",
         "                N",
         "                N",
         "                N",
         "      __________N"]

ahorcado = ["          !=====N",
         "          O     N",
         "        / | \   N",
         "        \ | /   N",
         "         / \    N",
         "        /   \   N",
         "       _\   /_  N",
         "     ___________N" ]

Letras_t = []       #Todas las letras usadas
fallos = 1

resultado = []      #Guiones

for i in range(len(palabra)):
    resultado.append("_")

while True:

    os.system("cls")

    print("----------El ahorcado-------------")

    for i in range(fallos):
        print(ahorcado[i])
    for i in range((len(horca)-fallos)):
        print(horca[i+fallos])

    print()

    #Resultados

    print("     ", end=" ")
    for i in resultado:
        print(i, end=" ")

    print()
    print()

    #comprobante de si gano o perdio

    if resultado == palabra:
        print("-------Victoria--------")
        break

    if fallos > 6:
        print("La palabra era:","".join(palabra))
        print("--------Derrota--------")
        break

    #Ingresar letra

    while True:
        letra_sin_f = input("Ingresa una letra:\n")
        letra_u = letra_sin_f.upper()
        if len(letra_u) != 1:
            print("Introduce una letra animal")
        elif letra_u in Letras_t:
            print("Esa letra ya fue introducida")
        elif letra_u not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            print("Deberias probar introduciendo una letra")
        else:
            Letras_t.append(letra_u)
            break

    #Comprobar letras

    for i in range(len(palabra)):
        if palabra[i] == letra_u:
            resultado[i] = letra_u

    if letra_u not in palabra:
        fallos += 1

    print()
    print()