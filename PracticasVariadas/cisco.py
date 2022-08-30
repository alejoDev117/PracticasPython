#Converter de binario a decimal y bisceversa
def binarioDecimal(binario):
    suma = 0
    cantidad = len(binario)-1
    for i in binario:
        a = int(i)
        suma = suma + a * (2**(cantidad))
        cantidad -=1
    return  suma
def octalDecimal(octal):
    suma = 0
    cantidad = len(octal) - 1
    for i in octal:
        a = int(i)
        suma = suma + a * (8 ** (cantidad))
        cantidad -= 1
    return suma
def hexaDecimal(hexa):
    diccionario = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    suma = 0
    cantidad = len(hexa) - 1
    for i in hexa:
        a = diccionario[i]
        suma = suma + a * (16 ** (cantidad))
        cantidad -= 1
    return suma

def decimalBinario(decimal):
    lista = []
    residuo = 0
    cociente = 0
    while True:
        residuo =  decimal // 2
        cociente = decimal % 2
        lista.append(cociente)
        if residuo < 2 :
            lista.append(residuo)
            break
        a = residuo // 2
        cociente = residuo % 2
        lista.append(cociente)
        if a < 2 :# revisar porque no con todos los numeros funciona, creo que no sirve con primos
            break
        decimal = a
    suma = ""
    for i in range(1,len(lista)+1):
        suma = suma + str(lista[-i])
    return suma
def decimalOctal(decimal):
       a =  oct(decimal)
       a = str(a)
       b = a.replace('0o','')
       return  b
def decimalHexa(decimal):
    a = hex(decimal)
    a = str(a)
    b = a.replace('0x','')
    return b


while True:
 print("Convertidor\n")
 print("1.Pasar de binario a decimal\n2.Pasar de decimal a cualquier sistema\n3.Pasar de octal a decimal\n4.Pasar de hexadecimal a decimal\n5.Salir")
 decision = input("Ingrese la opcion que desea \n")
 if decision == "1":
     bi = input("Ingrese numero binario\n")
     a = binarioDecimal(bi)
     print("Resultado: "+str(a))
 elif decision == "2":
      tal = input("1.decimal a binario\n2.decimal a octal\n3.decimal a hexadecimal\n")
      if tal == "1":
          bi = int(input("Ingrese numero \n"))
          a = decimalBinario(bi)
          print("Resultado: " + str(a))
      elif tal == "2":
          bi = int(input("Ingrese numero\n"))
          a = decimalOctal(bi)
          print("Resultado: " + str(a))
      elif tal == "3":
          bi = int(input("Ingrese numero\n"))
          a = decimalHexa(bi)
          print("Resultado: " + str(a))
 elif decision == "3":
     bi = input("Ingrese el numero octal\n")
     a = octalDecimal(bi)
     print("Resultado: "+str(a))
 elif decision == "4":
     bi = input("Ingrese el numero hexadecimal\n")
     a = hexaDecimal(bi)
     print("Resultado: " + str(a))
 elif decision == "5":
     break

print("Fin del programa :)")