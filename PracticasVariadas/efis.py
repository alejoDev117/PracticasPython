#creador de contraseñas random
import random
respuesta = ""
lista = []
respuesta = input("Quieres crear una contraseña?\n")
numero = 0
while (respuesta == "si"):
    caracteres = "abcdefghijklmnñopqrstuvxyz012345679@%$&"
    contraseña = ""
    for i in range(8):
        cantidad = len(caracteres)
        numero = random.randint(0, cantidad-1)
        contraseña = contraseña + caracteres[numero]
    print("Su contraseña es: "+ contraseña)
    lista.append(contraseña)
    respuesta = input("Quieres otra contraseña?\n")
print("La lista de contraseñas es:\n")
print(lista)
