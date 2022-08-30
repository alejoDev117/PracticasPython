matriz = []
print(matriz)
f = int(input("Ingrese la cantidad de filas que desea\n"))
c = int(input("Ingrese la cantidad de columnas que desea\n"))

for i in range(f): #ya sabemos como crear matrices personalizadas
    matriz.append([0]*c)
for i in range(f):
    for j in range(c):# ya sabemos como agregar elementos a una matriz
      numero = int(input("ingrese el numero\n"))
      matriz[i][j] = numero
# ya sabemos como agregar elementos o modificar (ojo previamente deberian haber elementos asignados)
print(matriz)

numero = int(input("Ingrese numero \n"))
factorial = 1
print("El factorial de " + str(numero)+"!")
for i in range(1,numero + 1):
    factorial *= i

print(factorial)
