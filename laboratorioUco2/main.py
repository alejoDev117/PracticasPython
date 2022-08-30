from Funciones import *
cadena = input("Ingrese cadena de texto\n")

print("La Longitud de la cadena es :"+str(tamanoCadena(cadena)))

print("La cantidad de vocales de la cadena es : "+str(cantidadVocales(cadena)))

vectorDeVocales(cadena)

print("La cantidad de consonantes es :"+str(cantidadConsonantes(cadena)))

consonanteMasFrecuente(cadena)

print("La cantidad de espacios es :"+str(espacioCadena(cadena)))

print("La cantidad de palabras es : "+str(cantidadPalabras(cadena)))

palabraMasFrecuente(cadena)

print("El texto invertido es :"+str(invertirMayusMinus(cadena)))

buscadorDePalabras(cadena)
