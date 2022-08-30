import time
from os import system
#/////////////////////////////////////////////////////////////////////////////////////////////
def animacionBurbuja(vector,ante,poste,pos1,pos2):
    string = ""
    index = 0
    for i in vector:
        #/////APROXIMA DECIMALES A ENTEROS/////////
        b = i
        if isinstance(i, float):
            b = int(b)
        #///////SOLO IMPRIME MAXIMO 30 ASTERISCOS/////
        if b>30:
            a = "*" * 30
        else:
            a = "*" * b
        #/////PONE LAS FLECHAS EN LA POSICION QUE ESTA COMPARANDO//////
        if (i == ante or i == poste) and (index == pos1 or index == pos2):
            string += str(i) + "-" + a +"  "+"<==" + "\n"
        else :
            string += str(i) + "-" + a + "\n"
        a = ""
        index += 1
    system("cls")
    print(string)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
def animacionSeleccion(vector,auxiliar,minimo):
   string = ""
   index = vector.index(vector[minimo])
   for j  in range(auxiliar,index+1):
       time.sleep(1)
       for i in vector:
           # /////APROXIMA DECIMALES A ENTEROS/////////
           b = i
           if isinstance(i, float):
               b = int(b)
           # ///////SOLO IMPRIME MAXIMO 30 ASTERISCOS/////
           if b > 30:
               a = "*" * 30
           else:
               a = "*" * b
           # /////PONE LAS FLECHAS EN LA POSICION QUE ESTA COMPARANDO//////
           if i == vector[auxiliar]:
                string += str(i) + "-" + a + "  " + "<==" + "\n"
           elif i == vector[j]:
               string += str(i) + "-" + a + "  " + "<==" + "\n"
           else:
               string += str(i) + "-" + a + "\n"
       system("cls")
       print(string)
       string = ""
       print("Recorriendo...\n")
   if auxiliar != minimo :
       print("Minimo " + str(vector[minimo]))
       print("Intercambia " + str(vector[auxiliar]) + " con " + str(vector[minimo]) + "\n")
   time.sleep(1)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def animacionInsercion(vector,inicial):
    string = ""
    for j in range(inicial,0-1, -1):
        time.sleep(1)
        for i in vector:
            # /////APROXIMA DECIMALES A ENTEROS/////////
            b = i
            if isinstance(i, float):
                b = int(b)
            # ///////SOLO IMPRIME MAXIMO 30 ASTERISCOS/////
            if b > 30:
                a = "*" * 30
            else:
                a = "*" * b
            # /////PONE LAS FLECHAS EN LA POSICION QUE ESTA COMPARANDO//////
            if i == vector[inicial] :
                string += str(i) + "-" + a + "  " + "<==PIVOTE" + "\n"
            elif i == vector[j]:
                string += str(i) + "-" + a + "  " + "<==" + "\n"
            else:
                string += str(i) + "-" + a + "\n"
        system("cls")
        print(string)
        string = ""
    print("Cambiando...\n")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def animacionShell(lista,mitad,primer,segundo):
    string = ""
    time.sleep(1)
    for i in lista:
        # /////APROXIMA DECIMALES A ENTEROS/////////
        b = i
        if isinstance(i, float):
            b = int(b)
        # ///////SOLO IMPRIME MAXIMO 30 ASTERISCOS/////
        if b > 30:
            a = "*" * 30
        else:
            a = "*" * b
        # /////PONE LAS FLECHAS EN LA POSICION QUE ESTA COMPARANDO//////
        if i == primer or i == segundo:
            string += str(i) + "-" + a + "  " + "<==" + "\n"
        else:
            string += str(i) + "-" + a + "\n"
        a = ""
    system("cls")
    print(string)
    print("De "+str(mitad)+" En "+str(mitad))
    print(" Es "+str(segundo)+" mayor/menor que "+str(primer)+"\n")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def animacionMergeSort(primerParte,segundaParte,lista,string,imprenta):
   if imprenta == 0:
       print(lista)
       time.sleep(2)
       string = str(primerParte) +"  "+str(segundaParte)+"\n"
       system("cls")
       print(string)
       print("\n")
   elif imprenta == 1:
       time.sleep(1)
       system("cls")
       print("Compara y Une "+ str(primerParte) + " Con "+str(segundaParte))
       print(lista)
       print("\n")
