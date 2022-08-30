print("\nRecuerde, el programa tiene las siguientes limitantes :\n")
print("1.No admite valores decimales\n2.No admite valores negativos\n3.No admite valores mayores a 999.999.999\n")
try:
 numero = int(input("Ingrese el valor deseado\n"))
except :
    try :
     print("Error numero de tipo decimal no valido\n")
     numero = int(input("Ingrese nuevamente el valor \n"))
    except:
        print("Fin del programa, por favor vuelva a ejecutar\n")

while numero<=0 or numero>999999999:   #los try except ayudan a validar el error decimal, mientras que el ciclo evalua los rangos negativos y mayores al permitido
      if numero<=0:
        try:
         print("Error valor menor a  0 \n")
         numero = int(input("Ingrese nuevamente el valor\n"))
        except:
         print("Numero decimal invalido\n")
         numero = int(input("Ingrese nuevamente el valor\n"))
      else :
        try:
         print("Error valor fuera del rango permitido\n")
         numero = int(input("Ingrese nuevamente el valor\n"))
        except:
         print("Numero decimal invalido\n")
         numero = int(input("Ingrese nuevamente el valor\n"))


unidad = { '0': " ", '1' : "uno" , '2' : "dos" , '3' : "tres" , '4' : "cuatro" , '5' : "cinco" , '6' : "seis", '7' : "siete", '8' : "ocho" , '9' : "nueve"}
dece = { '0': " ", '2' : "veinte", '3':"treinta",'4':"cuarenta",'5':"cincuenta",'6':"sesenta",'7':"setenta",'8':"ochenta",'9':"noventa"}
cente = {'0' : " " , '1' : "ciento", '2':"docientos",'3':"trecientos",'4':"cuatrocientos",'5':"quinientos",'6':"seicientos",'7':"setecientos",'8':"ochocientos",'9':"novecientos"}
espe = { '10' : "diez", '11':"once",'12':"doce",'13':"trece",'14':"catorce",'15':"quince",'16':"dieciseis",'17':"diecisiete",'18':"dieciocho",'19':"diecinueve"}
cente_espe ={'1' : "cien"}
cadena = str(numero)
resultado = ""

if len(cadena) == 1 :                 #decidi realizar los condicionales por numero de caracter por caracter en vez de uno por uno
    valuni = cadena[0]
    resultado = unidad[valuni]
    print(resultado)
# ///////////////////////////////////////////
if len(cadena) == 2 :
    if cadena[0] == "1": #como el especifica que del 11-19 los nombres son especificos entonces evaluamos el resultado con dos condicionales
        valdece = cadena[0:]   #teniendo en cuenta la posicion del substring, en este caso si el primero es 1 es porque es 11-19
        resultado = espe[valdece]
        print(resultado)
    elif cadena[0] != "1":
        valdece = cadena[0]
        valuni  = cadena[1]
        if cadena[1] == "0":
          resultado = dece[valdece]
          print(resultado)
        else :
            resultado = dece[valdece] + " y " + unidad[valuni]
            print(resultado)
#/////////////////////////////////////////////////////////////////////////////
if len(cadena) == 3:
     if cadena == "100":
        print("cien")
     elif cadena[1] != "1" :
         valcente = cadena[0] # es lo mismo pero en este caso son las decenas, si el numero del medio es 1 significa que lo que sigue es 11-19
         valdece = cadena[1]
         valunid = cadena[2]
         if cadena[1] == "0":
             if cadena[2] == "0" or cadena[1] == "0":
                 resultado = cente[valcente] + " " + dece[valdece] + "  " + unidad[valunid]
                 print(resultado)
             else :
                 resultado = cente[valcente] + " " + dece[valdece] + " y " + unidad[valunid]
                 print(resultado)
         elif cadena[1] != "0":
             if cadena[2] == "0":
                 resultado = cente[valcente] + " " + dece[valdece]
                 print(resultado)
             else:
                 resultado = cente[valcente] + " " + dece[valdece] + " y " + unidad[valunid]
                 print(resultado)
     elif cadena[1] == "1":
         valcente = cadena[0]
         valdece = cadena[1:]
         resultado = cente[valcente]+" "+espe[valdece]
         print(resultado)
#///////////////////////////////////////////////////////////////////////
if len(cadena) == 4 :
        valunimil = cadena[0]
        valcente = cadena[1]
        valdece = cadena[2]
        valunid = cadena[3]
        if cadena[0] == "1":#si el primer numero es 1, osea mil
          if cadena[2] == "1":
            valdec = cadena[2:]
            resultado =  "mil" + cente[valcente] + " " + espe[valdec] #este bloque es si la posicion 2 es 1, entonces usa los numeros especiales 10-19
            print(resultado)
          elif cadena[2] != "1":
              if cadena[1] == "1" and cadena[2] == "0" and cadena[3] == "0":
                  resultado = " mil "+cente_espe[valcente]
                  print(resultado)
              elif cadena[3] == "0" or cadena[2] == "0":
                  resultado = "Mil" + cente[valcente] + " " + dece[valdece] + " " + unidad[
                      valunid]  # este bloque es si la decena es 0, entonces quita el y
                  print(resultado)
              else :
                  resultado = "Mil" + cente[valcente] + " " + dece[valdece] + " y " + unidad[valunid]
                  print(resultado)
        elif cadena[0] != "1" :#si el primer numero es diferente de 1, osea dosmil,tresmil.etc
           if cadena[2] == "1":
              valdec = cadena[2:]
              resultado = unidad[valunimil] + "mil" + cente[valcente] + " " + espe[valdec]
              print(resultado)
           elif cadena[2] != "1":
               if cadena[1] == "1" and cadena[2] == "0" and cadena[3] == "0":
                   resultado = unidad[valunimil] + " mil " + cente_espe[valcente]
                   print(resultado)
               elif cadena[3] == "0" or cadena[2] == "0":
                   resultado = unidad[valunimil] + "Mil" + cente[valcente] + " " + dece[valdece] + "  " + unidad[
                       valunid] #este bloque es si la posicion 2 es 0, entonces quita el y
                   print(resultado)
               else :
                   resultado = unidad[valunimil] + "Mil" + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                       valunid]
                   print(resultado)
#////////////////////////////////////////////////////////////////////////////////////////////////
if len(cadena) == 5:
    if cadena[0] == "1":#si son rangos de 10-19 mil
        valdecemil = cadena[0:2]
        valcente =cadena[2]
        valdece = cadena[3]
        valuni = cadena[4]
        if cadena[2] == "1" and cadena[3] == "0" and cadena[4] == "0":
            resultado = espe[valdecemil]+ " Mil " + cente_espe[valcente]
            print(resultado)
        elif cadena[3] == "1":
            valdece = cadena[3:]
            resultado = espe[valdecemil] + " Mil" + cente[valcente] + " " + espe[valdece]
            print(resultado)
        elif cadena[3] == "0" or cadena[4] == "0":
            resultado =espe[valdecemil] + " Mil" + cente[valcente] + " " + dece[valdece] + " " + unidad[valuni]
            print(resultado)
        else :
            resultado = espe[valdecemil]+ " Mil" + cente[valcente] + " " + dece[valdece] + " y "+ unidad[valuni]
            print(resultado)
    elif cadena[0] != "1":#si son diferentes de 10-19, osea 29 39 40 mil
        valdecemil = cadena[0]
        valunimil = cadena[1]
        valcente = cadena[2]
        valdece = cadena[3]
        valuni = cadena[4]
        if cadena[1] == "0":#si el segundo caracter es 0 osea 20 40 30 50 mil
            if cadena[2] == "1" and cadena[3] == "0" and cadena[4] == "0":
                resultado = dece[valdecemil] + " Mil " + cente_espe[valcente]
                print(resultado)
            elif cadena[3] == "1":
                valdece = cadena[3:]
                resultado = dece[valdecemil] + " Mil" + cente[valcente] + " " + espe[valdece]
                print(resultado)
            elif cadena[3] == "0" or cadena[4] == "0":
                resultado = dece[valdecemil] + "Mil" + cente[valcente] + " " + dece[valdece] + " " + unidad[valuni]
                print(resultado)
            else:
                resultado = dece[valdecemil] + "Mil" + cente[valcente] + " " + dece[valdece] + "  y  " + unidad[valuni]
                print(resultado)
        elif cadena[1] != "0": # si el segundo caracter es diferente de cero osea 34 52 37 24 mil
            if cadena[2] =="1" and cadena[3] =="0" and cadena[4] == "0":
                resultado = dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente_espe[valcente]
                print(resultado)
            elif cadena[3] == "1":
                valdece = cadena[3:]
                resultado = dece[valdecemil]+ " y " + unidad[valunimil] + " Mil"+ cente[valcente]+ " "+ espe[valdece]
                print(resultado)
            elif cadena[3] == "0" or cadena[4] == "0" :
                resultado = dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[valcente] + " "+ dece[valdece]+ " "+unidad[valuni]
                print(resultado)
            else:
                resultado = dece[valdecemil] + " y " + unidad[valunimil] + " Mil" + cente[valcente] + "  " + dece[
                    valdece] + " y " + unidad[valuni]
                print(resultado)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
if len(cadena) == 6 :
   if cadena[0] == "1": # si son valores de entre 100-199 mil
       valcentemil = cadena[0]
       valdecemil = cadena[1]
       valunimil = cadena[2]
       valcente = cadena[3]
       valdece = cadena[4]
       valunidad = cadena[5]
       if  cadena[1] == "0" and cadena[2] == "0": #si es 100 mil
             if cadena[4] == "1" :
                 valdece = cadena[4:]
                 resultado = "Cien Mil" + cente[valcente] + "  " + espe[valdece]
                 print(resultado)
             elif cadena[3] == "1" and cadena[4] == "0" and cadena[5] == "0":
                 resultado = "Cien Mil " + cente_espe[valcente]
                 print(resultado)
             elif cadena[4] == "0" or cadena[5] == "0":
                 resultado = "Cien Mil " + cente[valcente] + " " + dece[valdece] + "  " + unidad[valunidad]
                 print(resultado)
             else :
                  resultado = "Cien Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[valunidad]
                  print(resultado)
       elif cadena[1] != "0" or cadena[2] != "0": # si es entre 101-199 mil
            valcentemil = cadena[0]
            valdecemil = cadena[1]
            valunimil = cadena[2]
            valcente = cadena[3]
            valdece = cadena[4]
            valuni = cadena[5]
            if cadena[1] == "1":#si es entre 110-119 mil
                valdecemil = cadena[1:3]
                if cadena[3] == "1" and cadena[4] == "0" and cadena[5] == "0":
                    resultado = cente[valcentemil]+" "+espe[valdecemil]+" Mil"+cente_espe[valcente]
                    print(resultado)
                elif cadena[4] == "0" or cadena[5] == "0":
                    resultado =cente[valcentemil]+" "+espe[valdecemil]+" Mil"+ cente[valcente]+" "+dece[valdece]+" "+unidad[valuni]
                    print(resultado)
                elif cadena[4] == "1":
                    valdece = cadena[4:]
                    resultado = cente[valcentemil]+" "+espe[valdecemil]+" Mil"+cente[valcente]+" "+espe[valdece]
                    print(resultado)
                else:
                    resultado = cente[valcentemil]+ " "+espe[valdecemil]+" Mil"+cente[valcente]+" "+dece[valdece]+" y"+unidad[valuni]
                    print(resultado)
            elif cadena[1] == "0" or cadena[2] == "0": #si es valores por ejemplo 103 150 mil etc
                  if cadena[3] == "1" and cadena[4] == "0" and cadena[5] == "0":
                      resultado = cente[valcentemil] +" "+dece[valdecemil]+"  " + unidad[valunimil] + " Mil" + cente_espe[valcente]
                      print(resultado)
                  elif cadena[4] == "0" or cadena[5] == "0":
                      resultado = cente[valcentemil] +""+dece[valdecemil]+" " + unidad[valunimil] + " Mil" + cente[valcente] + " " + dece[
                          valdece] + "  " + unidad[valuni]
                      print(resultado)
                  elif cadena[4] == "1":
                      valdece = cadena[4:]
                      resultado = cente[valcentemil] +" "+dece[valdecemil]+ " " + unidad[valunimil]+ " Mil" + cente[valcente] + " " +espe[valdece]
                      print(resultado)
                  else:
                      resultado = cente[valcentemil] +" "+dece[valdecemil]+"  " + unidad[valunimil] + " Mil" + cente[valcente] + " " + dece[
                          valdece] + " y " + unidad[valuni]
                      print(resultado)
            else: # si son valores tipo 135 185 145 mil
                if cadena[3] == "1" and cadena[4] == "0" and cadena[5] == "0":
                    resultado = cente[valcentemil] + "  "+dece[valdecemil]+" y "+ unidad[valunimil] + " Mil" + cente_espe[valcente]
                    print(resultado)
                elif cadena[4] == "0" or cadena[5] == "0":
                    resultado = cente[valcentemil] +" "+ dece[valdecemil]+ " y " + unidad[valunimil] + " Mil" + cente[valcente] + " " + dece[
                        valdece] + "  " + unidad[valuni]
                    print(resultado)
                elif cadena[4] == "1":
                    valdece = cadena[4:]
                    resultado = cente[valcentemil] +" "+dece[valdecemil]+ " y " + unidad[valunimil] + " Mil" + cente[valcente] + " " + espe[
                        valdece]
                    print(resultado)
                else:
                    resultado = cente[valcentemil] +" "+dece[valdecemil]+" y "+ unidad[valunimil] + " Mil" + cente[valcente] + " " + dece[
                        valdece] + " y " + unidad[valuni]
                    print(resultado)
   elif cadena[0] != "1" : #si el rango es 200-999 mil
        valcentemil = cadena[0]
        valdecemil = cadena[1]
        valunimil = cadena[2]
        valcente = cadena[3]
        valdece = cadena[4]
        valuni = cadena[5]
        if cadena[1] == "0" and cadena[2] == "0":#si son valores por ejemplo 300 400 200 mil
            if cadena[4] == "1":
                valcente = cadena[3]
                valdece = cadena[4:]
                resultado = cente[valcentemil] + " Mil" + cente[valcente] + "  " + espe[valdece]
                print(resultado)
            elif cadena[3] == "1" and cadena[4] == "0" and cadena[5] == "0":
                resultado = cente[valcentemil] +" Mil " + cente_espe[valcente]
                print(resultado)
            elif cadena[4] == "0" or cadena[5] == "0":
                resultado = cente[valcentemil] +"  Mil " + cente[valcente] + " " + dece[valdece] + "  " + unidad[valuni]
                print(resultado)
            else:
                resultado =  cente[valcentemil] +"  Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[valuni]
                print(resultado)
        elif cadena[1] != "0" or cadena[2] != "0":
            valcentemil = cadena[0]
            valdecemil = cadena[1]
            valunimil = cadena[2]
            valcente = cadena[3]
            valdece = cadena[4]
            valuni = cadena[5]
            if cadena[1] == "1": #si son valores por ejemplo 319 415 613 mil
                valdecemil = cadena[1:3]
                if cadena[3] == "1" and cadena[4] == "0" and cadena[5] == "0":
                    resultado = cente[valcentemil] + " " + espe[valdecemil] + " Mil" + cente_espe[valcente]
                    print(resultado)
                elif cadena[4] == "0" or cadena[5] == "0":
                    resultado = cente[valcentemil] + " " + espe[valdecemil] + " Mil" + cente[valcente] + " " + dece[
                        valdece] + " " + unidad[valuni]
                    print(resultado)
                elif cadena[4] == "1":
                    valdece = cadena[4:]
                    resultado = cente[valcentemil] + " " + espe[valdecemil] + " Mil" + cente[valcente] + " " + espe[
                        valdece]
                    print(resultado)
                else:
                    resultado = cente[valcentemil] + " " + espe[valdecemil] + " Mil" + cente[valcente] + " " + dece[
                        valdece] + " y" + unidad[valuni]
                    print(resultado)
            elif cadena[1] == "0" or cadena[2] =="0": #si son valores tipo 405 320 540 mil
                if cadena[3] == "1" and cadena[4] == "0" and cadena[5] == "0":
                    resultado = cente[valcentemil]+" "+dece[valdecemil] + " "+unidad[valunimil]+ " Mil"+cente_espe[valcente]
                    print(resultado)
                elif cadena[4] == "0" or cadena[5] == "0":
                    resultado = cente[valcentemil]+" "+dece[valdecemil]+" "+ unidad[valunimil]+ " Mil" + cente[valcente] + " "+dece[valdece]+" "+unidad[valuni]
                    print(resultado)
                elif cadena[4] == "1":
                    valdece = cadena[4:]
                    resultado = cente[valcentemil]+" "+dece[valdecemil]+" " + unidad[valunimil]+ " Mil"+ cente[valcente]+ " "+espe[valdece]
                    print(resultado)
                else :
                    resultado = cente[valcentemil]+" "+dece[valdecemil] +" "+unidad[valunimil]+" Mil"+cente[valcente]+" "+dece[valdece]+ " Y "+unidad[valuni]
                    print(resultado)
            elif cadena[1] != "0" and cadena[2] != "0" : # si son valores 435 638 396 693 mil
                if cadena[3] == "1" and cadena[4] == "0" and cadena[5] == "0":
                    resultado = cente[valcentemil] + "  "+dece[valdecemil]+" y "+ unidad[valunimil] + " Mil" + cente_espe[valcente]
                    print(resultado)
                elif cadena[4] == "0" or cadena[5] == "0":
                    resultado = cente[valcentemil] +" "+ dece[valdecemil]+ " y " + unidad[valunimil] + " Mil" + cente[valcente] + " " + dece[
                        valdece] + "  " + unidad[valuni]
                    print(resultado)
                elif cadena[4] == "1":
                    valdece = cadena[4:]
                    resultado = cente[valcentemil] +" "+dece[valdecemil]+ " y " + unidad[valunimil] + " Mil" + cente[valcente] + " " + espe[
                        valdece]
                    print(resultado)
                else:
                    resultado = cente[valcentemil] +" "+dece[valdecemil]+" y "+ unidad[valunimil] + " Mil" + cente[valcente] + " " + dece[
                        valdece] + " y " + unidad[valuni]
                    print(resultado)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def excepciones(a): # funcion en la cual se almacenan los bloques de las excepciones de los cientos de miles y lo cientos
    resul = " "
    if len(a) == 7:
        if a[1] == "1":
            if a[2] =="0" and a[3] =="0":
                valcentemil = a[1]
                valcente=a[4]
                valdece = a[5]
                valuni = a[6]
                if a[4] == "1" and a[5] == "0" and a[6] == "0":
                    resul = cente_espe[valcentemil]+ " Mil " + cente_espe[valcente]
                    return resul
                elif a[5] == "1":
                    valdece = a[5:]
                    resul = cente_espe[valcentemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[5] == "0" or a[6] == "0":
                    resul = cente_espe[valcentemil] + " Mil " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente_espe[valcentemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[2] == "1":
                valcentemil = a[1]
                valdecemil = a[2:4]
                valcente = a[4]
                valdece = a[5]
                valuni = a[6]
                if a[4] == "1" and a[5] == "0" and a[6] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil]+" Mil " + cente_espe[valcente]
                    return resul
                elif a[5] == "1":
                    valdece = a[5:]
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[5] == "0" or a[6] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[2] == "0" or a[3]  == "0":
                valcentemil = a[1]
                valdecemil = a[2]
                valunimil = a[3]
                valcente = a[4]
                valdece = a[5]
                valuni = a[6]
                if a[4] == "1" and a[5] == "0" and a[6] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente_espe[valcente]
                    return resul
                elif a[5] == "1":
                    valdece = a[5:]
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + espe[
                        valdece]
                    return resul
                elif a[5] == "0" or a[6] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " y " + unidad[
                                valuni]
                    return resul
            else:
                valcentemil = a[1]
                valdecemil = a[2]
                valunimil = a[3]
                valcente = a[4]
                valdece = a[5]
                valuni = a[6]
                if a[4] == "1" and a[5] == "0" and a[6] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente_espe[
                        valcente]
                    return resul
                elif a[5] == "1":
                    valdece = a[5:]
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + espe[
                                valdece]
                    return resul
                elif a[5] == "0" or a[6] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil]  + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil]  + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " y " + unidad[
                                valuni]
                    return resul
        elif a[1] != "1":
            if a[2] =="0" and a[3] =="0":
                valcentemil = a[1]
                valcente=a[4]
                valdece = a[5]
                valuni = a[6]
                if a[4] == "1" and a[5] == "0" and a[6] == "0":
                    resul = cente[valcentemil]+ " Mil " + cente_espe[valcente]
                    return resul
                elif a[5] == "1":
                    valdece = a[5:]
                    resul = cente[valcentemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[5] == "0" or a[6] == "0":
                    resul = cente[valcentemil] + "  " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[2] == "1":
                valcentemil = a[1]
                valdecemil = a[2:4]
                valcente = a[4]
                valdece = a[5]
                valuni = a[6]
                if a[4] == "1" and a[5] == "0" and a[6] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil]+" Mil " + cente_espe[valcente]
                    return resul
                elif a[5] == "1":
                    valdece = a[5:]
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[5] == "0" or a[6] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[2] == "0" or a[3]  == "0":
                valcentemil = a[1]
                valdecemil = a[2]
                valunimil = a[3]
                valcente = a[4]
                valdece = a[5]
                valuni = a[6]
                if a[4] == "1" and a[5] == "0" and a[6] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente_espe[valcente]
                    return resul
                elif a[5] == "1":
                    valdece = a[5:]
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + espe[
                        valdece]
                    return resul
                elif a[5] == "0" or a[6] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " y " + unidad[
                                valuni]
                    return resul
            else:
                valcentemil = a[1]
                valdecemil = a[2]
                valunimil = a[3]
                valcente = a[4]
                valdece = a[5]
                valuni = a[6]
                if a[4] == "1" and a[5] == "0" and a[6] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + \
                            cente_espe[
                                valcente]
                    return resul
                elif a[5] == "1":
                    valdece = a[5:]
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + espe[
                                valdece]
                    return resul
                elif a[5] == "0" or a[6] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " y " + unidad[
                                valuni]
                    return resul
    elif len(a) == 8: #Bloque de excepciones para decenas de millon
        if a[2] == "1":
            if a[3] =="0" and a[4] =="0":
                valcentemil = a[2]
                valcente=a[5]
                valdece = a[6]
                valuni = a[7]
                if a[5] == "1" and a[6] == "0" and a[7] == "0":
                    resul = cente_espe[valcentemil]+ " Mil " + cente_espe[valcente]
                    return resul
                elif a[6] == "1":
                    valdece = a[6:]
                    resul = cente_espe[valcentemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[6] == "0" or a[7] == "0":
                    resul = cente_espe[valcentemil] + " Mil " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente_espe[valcentemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[3] == "1":
                valcentemil = a[2]
                valdecemil = a[3:5]
                valcente = a[5]
                valdece = a[6]
                valuni = a[7]
                if a[5] == "1" and a[6] == "0" and a[7] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil]+" Mil " + cente_espe[valcente]
                    return resul
                elif a[6] == "1":
                    valdece = a[6:]
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[6] == "0" or a[7] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[3] == "0" or a[4]  == "0":
                valcentemil = a[2]
                valdecemil = a[3]
                valunimil = a[4]
                valcente = a[5]
                valdece = a[6]
                valuni = a[7]
                if a[5] == "1" and a[6] == "0" and a[7] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente_espe[valcente]
                    return resul
                elif a[6] == "1":
                    valdece = a[6:]
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + espe[
                        valdece]
                    return resul
                elif a[6] == "0" or a[7] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " y " + unidad[
                                valuni]
                    return resul
            else:
                valcentemil = a[2]
                valdecemil = a[3]
                valunimil = a[4]
                valcente = a[5]
                valdece = a[6]
                valuni = a[7]
                if a[5] == "1" and a[6] == "0" and a[7] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente_espe[
                        valcente]
                    return resul
                elif a[6] == "1":
                    valdece = a[6:]
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + espe[
                                valdece]
                    return resul
                elif a[6] == "0" or a[7] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil]  + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil]  + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " y " + unidad[
                                valuni]
                    return resul
        elif a[2] != "1":
            if a[3] =="0" and a[4] =="0":
                valcentemil = a[2]
                valcente=a[5]
                valdece = a[6]
                valuni = a[7]
                if a[5] == "1" and a[6] == "0" and a[7] == "0":
                    resul = cente[valcentemil]+ " Mil " + cente_espe[valcente]
                    return resul
                elif a[6] == "1":
                    valdece = a[6:]
                    resul = cente[valcentemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[6] == "0" or a[7] == "0":
                    resul = cente[valcentemil] + " Mil " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[3] == "1":
                valcentemil = a[2]
                valdecemil = a[3:5]
                valcente = a[5]
                valdece = a[6]
                valuni = a[7]
                if a[5] == "1" and a[6] == "0" and a[7] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil]+" Mil " + cente_espe[valcente]
                    return resul
                elif a[6] == "1":
                    valdece = a[6:]
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[6] == "0" or a[7] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[3] == "0" or a[4]  == "0":
                valcentemil = a[2]
                valdecemil = a[3]
                valunimil = a[4]
                valcente = a[5]
                valdece = a[6]
                valuni = a[7]
                if a[5] == "1" and a[6] == "0" and a[7] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente_espe[valcente]
                    return resul
                elif a[6] == "1":
                    valdece = a[6:]
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + espe[
                        valdece]
                    return resul
                elif a[6] == "0" or a[7] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " y " + unidad[
                                valuni]
                    return resul
            else:
                valcentemil = a[2]
                valdecemil = a[3]
                valunimil = a[4]
                valcente = a[5]
                valdece = a[6]
                valuni = a[7]
                if a[5] == "1" and a[6] == "0" and a[7] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + \
                            cente_espe[
                                valcente]
                    return resul
                elif a[6] == "1":
                    valdece = a[6:]
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + espe[
                                valdece]
                    return resul
                elif a[6] == "0" or a[7] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " y " + unidad[
                                valuni]
                    return resul
    elif len(a) == 9:#si las excepciones son para cientos de millones
        if a[3] == "1":
            if a[4] =="0" and a[5] =="0":
                valcentemil = a[3]
                valcente=a[6]
                valdece = a[7]
                valuni = a[8]
                if a[6] == "1" and a[7] == "0" and a[8] == "0":
                    resul = cente_espe[valcentemil]+ " Mil " + cente_espe[valcente]
                    return resul
                elif a[7] == "1":
                    valdece = a[7:]
                    resul = cente_espe[valcentemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[7] == "0" or a[8] == "0":
                    resul = cente_espe[valcentemil] + " Mil " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente_espe[valcentemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[4] == "1":
                valcentemil = a[3]
                valdecemil = a[4:6]
                valcente = a[6]
                valdece = a[7]
                valuni = a[8]
                if a[6] == "1" and a[7] == "0" and a[8] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil]+" Mil " + cente_espe[valcente]
                    return resul
                elif a[7] == "1":
                    valdece = a[7:]
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[7] == "0" or a[8] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[4] == "0" or a[5]  == "0":
                valcentemil = a[3]
                valdecemil = a[4]
                valunimil = a[5]
                valcente = a[6]
                valdece = a[7]
                valuni = a[8]
                if a[6] == "1" and a[7] == "0" and a[8] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente_espe[valcente]
                    return resul
                elif a[7] == "1":
                    valdece = a[7:]
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + espe[
                        valdece]
                    return resul
                elif a[7] == "0" or a[8] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " y " + unidad[
                                valuni]
                    return resul
            else:
                valcentemil = a[3]
                valdecemil = a[4]
                valunimil = a[5]
                valcente = a[6]
                valdece = a[7]
                valuni = a[8]
                if a[6] == "1" and a[7] == "0" and a[8] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente_espe[
                        valcente]
                    return resul
                elif a[7] == "1":
                    valdece = a[7:]
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + espe[
                                valdece]
                    return resul
                elif a[7] == "0" or a[8] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil]  + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil]  + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " y " + unidad[
                                valuni]
                    return resul
        elif a[3] != "1":
            if a[4] == "0" and a[5] == "0":
                valcentemil = a[3]
                valcente = a[6]
                valdece = a[7]
                valuni = a[8]
                if a[6] == "1" and a[7] == "0" and a[8] == "0":
                    resul = cente[valcentemil] + " Mil " + cente_espe[valcente]
                    return resul
                elif a[7] == "1":
                    valdece = a[7:]
                    resul = cente[valcentemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[7] == "0" or a[8] == "0":
                    resul = cente[valcentemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[4] == "1":
                valcentemil = a[3]
                valdecemil = a[4:6]
                valcente = a[6]
                valdece = a[7]
                valuni = a[8]
                if a[6] == "1" and a[7] == "0" and a[8] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil]+" Mil " + cente_espe[valcente]
                    return resul
                elif a[7] == "1":
                    valdece = a[7:]
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + espe[valdece]
                    return resul
                elif a[7] == "0" or a[8] == "0":
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " "+ dece[valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil]+" "+espe[valdecemil] + " Mil " + cente[valcente] + " " + dece[valdece] + " y " + unidad[
                        valuni]
                    return resul
            elif a[4] == "0" or a[5]  == "0":
                valcentemil = a[3]
                valdecemil = a[4]
                valunimil = a[5]
                valcente = a[6]
                valdece = a[7]
                valuni = a[8]
                if a[6] == "1" and a[7] == "0" and a[8] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente_espe[valcente]
                    return resul
                elif a[7] == "1":
                    valdece = a[7:]
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + espe[
                        valdece]
                    return resul
                elif a[7] == "0" or a[8] == "0":
                    resul = cente[valcentemil] + " "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] +" "+dece[valdecemil]+" "+unidad[valuni] + " Mil " + cente[valcente] + " " + dece[
                        valdece] + " y " + unidad[
                                valuni]
                    return resul
            else:
                valcentemil = a[3]
                valdecemil = a[4]
                valunimil = a[5]
                valcente = a[6]
                valdece = a[7]
                valuni = a[8]
                if a[6] == "1" and a[7] == "0" and a[8] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + \
                            cente_espe[
                                valcente]
                    return resul
                elif a[7] == "1":
                    valdece = a[7:]
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + espe[
                                valdece]
                    return resul
                elif a[7] == "0" or a[8] == "0":
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " " + unidad[valuni]
                    return resul
                else:
                    resul = cente[valcentemil] + " " + dece[valdecemil] + " y " + unidad[valunimil] + " Mil " + cente[
                        valcente] + " " + dece[
                                valdece] + " y " + unidad[
                                valuni]
                    return resul

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////77
if len(cadena) == 7:
    if cadena[0] == "1":
        resultado = "Un Millon" + excepciones(cadena)
        print(resultado)
    elif cadena[0] !="1":
        valunimillon = cadena[0]
        resultado = unidad[valunimillon]+ " Millones  " + excepciones(cadena)
        print(resultado)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if len(cadena) == 8:
    if cadena[0] == "1":
        valdecemillon = cadena[0:2]
        resultado = espe[valdecemillon]+ " " + "Millones" + excepciones(cadena)
        print(resultado)
    elif cadena[0] != "1":
         if cadena[1] == "0":
             valdecemillon = cadena[0]
             resultado = dece[valdecemillon]+ " " + " Millones" + excepciones(cadena)
             print(resultado)
         else :
             valdecemillon = cadena[0]
             valunimillon = cadena[1]
             resultado = dece[valdecemillon]+" "+" y "+ unidad[valunimillon]+" " +" Millones" + excepciones(cadena)
             print(resultado)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
if len(cadena) == 9:
    if cadena[0] == "1":
        if cadena[1] == "0" and cadena[2] == "0":
            valcentemillon = cadena[0]
            resultado = cente_espe[valcentemillon] + " " + "Millones" + excepciones(cadena)
            print(resultado)
        elif cadena[1] == "1":
            valcentemillon  = cadena[0]
            valdecemillon = cadena[1:3]
            resultado = cente[valcentemillon] + " " + espe[valdecemillon] + " Millones" + excepciones(cadena)
            print(resultado)
        elif cadena[1] == "0" or cadena[2] == "0" :
            valcentemillon = cadena[0]
            valdecemillon = cadena[1]
            valunimillon = cadena[2]
            resultado = cente[valcentemillon]+ " " + dece[valdecemillon] + " " + unidad[valunimillon] + " Millones " + excepciones(cadena)
            print(resultado)
        else:
            valcentemillon = cadena[0]
            valdecemillon = cadena[1]
            valunimillon = cadena[2]
            resultado = cente[valcentemillon] + " " + dece[valdecemillon] + " y " + unidad[
                valunimillon] + " Millones " + excepciones(cadena)
            print(resultado)
    elif cadena[0] != "1":
        if cadena[1] == "0" and cadena[2] == "0":
            valcentemillon = cadena[0]
            resultado = cente[valcentemillon] + " " + "Millones" + excepciones(cadena)
            print(resultado)
        elif cadena[1] == "1":
            valcentemillon  = cadena[0]
            valdecemillon = cadena[1:3]
            resultado = cente[valcentemillon] + " " + espe[valdecemillon] + " Millones" + excepciones(cadena)
            print(resultado)
        elif cadena[1] == "0" or cadena[2] == "0" :
            valcentemillon = cadena[0]
            valdecemillon = cadena[1]
            valunimillon = cadena[2]
            resultado = cente[valcentemillon]+ " " + dece[valdecemillon] + " " + unidad[valunimillon] + " Millones " + excepciones(cadena)
            print(resultado)
        else:
            valcentemillon = cadena[0]
            valdecemillon = cadena[1]
            valunimillon = cadena[2]
            resultado = cente[valcentemillon] + " " + dece[valdecemillon] + " y " + unidad[
                valunimillon] + " Millones " + excepciones(cadena)
            print(resultado)

