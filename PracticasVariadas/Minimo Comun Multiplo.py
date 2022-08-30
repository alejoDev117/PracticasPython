# Decir el minimo comun multiplo de tres numeros y tal
n1 = int(input())
n2 = int(input("\n"))
n3 = int(input("\n"))
# variables
a = 0
b = 0
c = 0
multi = 1
# vectores
lista1 = []
lista2 = []
lista3 = []
x = 1
mcm = 0
while x != 0 :
    a = n1 * multi
    b = n2 * multi
    c = n3 * multi
    lista1.append(a)
    lista2.append(b)
    lista3.append(c)
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                for k in range(len(lista3)):
                    if lista2[j] == lista3[k]:
                        mcm = lista3[k]
                        x = 0
    multi += 1
print(mcm)