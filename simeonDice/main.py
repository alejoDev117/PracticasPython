import time
import pygame, sys, random

# colores apagados
negro = [0, 0, 0]
rojoApagado = [153, 0, 0]
amarilloApagado = [204, 204, 0]
verdeApagado = [0, 153, 0]
azulApagado = [0, 0, 153]
# colores encendidos
rojoEncendido = [255, 0, 0]
amarilloEncendido = [255, 255, 0]
verdeEncendido = [0, 255, 0]
azulEncendido = [0, 0, 255]

pygame.init()


def juego():
    diccionarioColor = {"verde": [0, 255, 0], "rojo": [255, 0, 0], "amarillo": [255, 255, 0], "azul": [0, 0, 255]}
    diccionarioposicion = {"verde": (200, 150, 100, 120), "rojo": (100, 30, 100, 120), "amarillo": (200, 30, 100, 120),
                           "azul": (100, 150, 100, 120)}
    diccionarioSonido = {"verde": sonidoLa, "rojo": sonidoSol, "azul": sondioMi, "amarillo": sonidoRe}
    colores = ["verde", "amarillo", "rojo", "azul"]
    colorRandom = random.choice(colores)
    listaGlobal.append(colorRandom)
    for i in listaGlobal:
        nuevoColor = diccionarioColor[i]
        posicion = diccionarioposicion[i]
        sonidito = diccionarioSonido[i]
        pygame.draw.rect(pantalla, nuevoColor, posicion)
        sonidito.play()
    print(listaGlobal)


pantalla = pygame.display.set_mode((400, 400))
relojito = pygame.time.Clock()
# Sonidos////////////////////////////////////
sonidoLa = pygame.mixer.Sound("la.ogg")
sonidoSol = pygame.mixer.Sound("sol.ogg")
sondioMi = pygame.mixer.Sound("mi.ogg")
sonidoRe = pygame.mixer.Sound("re.ogg")
listaGlobal = []
listaBotones = []
# Botones////////////////////////////
rojo = pygame.Rect(15, 300, 80, 50)
verde = pygame.Rect(110, 300, 80, 50)
azul = pygame.Rect(205, 300, 80, 50)
amarillo = pygame.Rect(300, 300, 80, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rojo.collidepoint(pygame.mouse.get_pos()):
                listaBotones.append("rojo")
            elif amarillo.collidepoint(pygame.mouse.get_pos()):
                listaBotones.append("amarillo")
            elif verde.collidepoint(pygame.mouse.get_pos()):
                listaBotones.append("verde")
            elif azul.collidepoint(pygame.mouse.get_pos()):
                listaBotones.append("azul")
    print("este son bontones")
    print(listaBotones)
    pantalla.fill(negro)
    pygame.draw.rect(pantalla, rojoApagado, (100, 30, 100, 120))
    pygame.draw.rect(pantalla, amarilloApagado, (200, 30, 100, 120))
    pygame.draw.rect(pantalla, azulApagado, (100, 150, 100, 120))
    pygame.draw.rect(pantalla, verdeApagado, (200, 150, 100, 120))
    pygame.draw.rect(pantalla, rojoEncendido, rojo, 0)
    pygame.draw.rect(pantalla, verdeEncendido, verde, 0)
    pygame.draw.rect(pantalla, azulEncendido, azul, 0)
    pygame.draw.rect(pantalla, amarilloEncendido, amarillo, 0)
    if listaBotones == listaGlobal:
        juego()
        listaBotones = []
    pygame.display.flip()
    relojito.tick(0.5)
