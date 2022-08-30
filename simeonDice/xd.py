import random

AHORCADO = ["", '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''' , '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
#facil
paisesFacil = "colombia argentina alemania brasil belgica honduras"
marcaFacil = "iphone xiaomi samsung huawei motorola nokia"
animalesFacil = "perro gato pez paloma hamster"
videoFacil = "callofduty fortnite gta fifa minecraft"
#normal
paisesNormal = "afganistan uruguay andorra camboya georgia angola"
marcaNormal = "oneplus pocco realme oppo htc asus blackberry"
animalesNormal = "murcielago cangrejo erizo elefante jirafa"
videoNormal = "farcry finalfantasy pugb leagueoflegends mortalkombat"
#dificil
paisesDificil = "tayikistan santalucia nauru gambia bangladesh"
marcaDificil = "zte lanix lenovo sony vodafone caterpilla"
animalesDificil = "tapir lince anguila pezglobo ajolote"
videoDificil = "lifeisstrange detroitbecomehuman worldofwarcraft thief ninjagaiden"
#################################################################################################################################
def Consola(frase):
    vector = frase.split()
    palabraRandom = vector[random.randint(0,(len(vector)-1))]
    espacios = "_"*len(palabraRandom)
    espacios = list(espacios)
    for i in range(3):
        f = random.randint(0, len(palabraRandom) - 1)
        espacios.pop(f)
        letra = palabraRandom[f]
        espacios.insert(f, letra)
    pantalla = ""
    for i in espacios:
        pantalla = pantalla + i
    return  pantalla ,palabraRandom
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def juego(vectorPalabra,completacion,palabra):
    vidas = 0
    a = 1
    while a == 1:
        letra = input("Ingrese letra\n")
        palabraTrabajo = vectorPalabra
        for i in palabraTrabajo:
            try:
              palabraTrabajo.index(letra)
            except:
                vidas +=1
                break
            if letra == i:
                indice = palabraTrabajo.index(i)
                completacion.pop(indice)
                completacion.insert(indice, letra)
                palabraTrabajo.remove(letra)
                palabraTrabajo.insert(indice, "_")
                break
        if vidas!=0:
            print(AHORCADO[vidas])
            if vidas == 4:
                print("JUEGO TERMINADO")
                print(palabra)
                break
        pantalla = "".join(completacion)
        print(pantalla)
        final = "".join(palabra)
        if pantalla == final:
            print("Juego terminado\n")
            break
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
completacion = []
while True :
    print("AHORCADO\n")
    dificultad = input("Elija el nivel de dificultad (facil,normal,dificil)\n")
#////////////////////////////FACIL////////////////////////////////////////////////////////////////////////////////////////
    if dificultad == "facil"  :
      categoria  = input("Elija categoria(paises,celulares,animales,videojuegos)\n")
      if categoria == "paises":
          f = Consola(paisesFacil)
          string = f[0]
          palabra = f[1]
          print(string)
          completacion = list(string)
          vectorPalabra = list(palabra)
          juego(vectorPalabra,completacion,palabra)
      elif categoria == "celulares":
          f = Consola(marcaFacil)
          string = f[0]
          palabra = f[1]
          print(string)
          completacion = list(string)
          vectorPalabra = list(palabra)
          juego(vectorPalabra, completacion,palabra)
      elif categoria == "animales":
          f = Consola(animalesFacil)
          string = f[0]
          palabra = f[1]
          print(string)
          completacion = list(string)
          vectorPalabra = list(palabra)
          juego(vectorPalabra, completacion,palabra)
      elif categoria == "videojuegos":
          f = Consola(videoFacil)
          string = f[0]
          palabra = f[1]
          print(string)
          completacion = list(string)
          vectorPalabra = list(palabra)
          juego(vectorPalabra, completacion,palabra)
      else:
          print("categoria no valida")
# ////////////////////////////NORMAL////////////////////////////////////////////////////////////////////////////////////////
    elif dificultad == "normal":
        categoria = input("Elija categoria(paises,celulares,animales,videojuegos)\n")
        if categoria =="paises":
            f = Consola(paisesNormal)
            string = f[0]
            palabra = f[1]
            print(string)
            completacion = list(string)
            vectorPalabra = list(palabra)
            juego(vectorPalabra, completacion,palabra)
        elif categoria == "celulares":
            f = Consola(marcaNormal)
            string = f[0]
            palabra = f[1]
            print(string)
            completacion = list(string)
            vectorPalabra = list(palabra)
            juego(vectorPalabra, completacion,palabra)
        elif categoria == "animales":
            f = Consola(animalesNormal)
            string = f[0]
            palabra = f[1]
            print(string)
            completacion = list(string)
            vectorPalabra = list(palabra)
            juego(vectorPalabra, completacion,palabra)
        elif categoria == "videojuegos":
            f = Consola(videoNormal)
            string = f[0]
            palabra = f[1]
            print(string)
            completacion = list(string)
            vectorPalabra = list(palabra)
            juego(vectorPalabra, completacion,palabra)
        else:
            print("categoria no valida")
# ////////////////////////////////DIFICIL/////////////////////////////////////////////////////////////////////////////////
    elif dificultad == "dificil":
        categoria = input("Elija categoria(paises,celulares,animales,videojuegos)\n")
        if categoria == "paises":
            f = Consola(paisesDificil)
            string = f[0]
            palabra = f[1]
            print(string)
            completacion = list(string)
            vectorPalabra = list(palabra)
            juego(vectorPalabra, completacion,palabra)
        elif categoria == "celulares":
            f = Consola(marcaDificil)
            string = f[0]
            palabra = f[1]
            print(string)
            completacion = list(string)
            vectorPalabra = list(palabra)
            juego(vectorPalabra, completacion,palabra)
        elif categoria == "animales":
            f = Consola(animalesDificil)
            string = f[0]
            palabra = f[1]
            print(string)
            completacion = list(string)
            vectorPalabra = list(palabra)
            juego(vectorPalabra, completacion,palabra)
        elif categoria == "videojuegos":
            f = Consola(videoDificil)
            string = f[0]
            palabra = f[1]
            print(string)
            completacion = list(string)
            vectorPalabra = list(palabra)
            juego(vectorPalabra, completacion,palabra)
        else:
            print("categoria no valida")
    else:
        print("Error dificultad no indentificada\n")
