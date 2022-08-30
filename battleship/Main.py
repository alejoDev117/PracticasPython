import time
from Funciones import *
from ventanas import *
import pygame
"""
Editado por :
Juan Esteban Cadavid Narváez
Alejandro Gómez Orjuela
"""
pygame.init()
SonidoBienvenida = pygame.mixer.Sound("Bienvenidos-a-la-grieta-del-invocador.ogg")
subditos = pygame.mixer.Sound("se-han-generado-subditos.ogg")
def jugar():
    disparos_restantes_j1 = DISPAROS_INICIALES
    disparos_restantes_j2 = DISPAROS_INICIALES
    cantidad_barcos = 10
    matriz_j1, matriz_j2 = obtener_matriz_inicial(), obtener_matriz_inicial()
    matriz_j1 = colocar_e_imprimir_barcos(
        matriz_j1, cantidad_barcos, JUGADOR_1)
    subditos.play()
    matriz_j2 = colocar_e_imprimir_barcos(
        matriz_j2, cantidad_barcos, JUGADOR_2)
    turno_actual = JUGADOR_1
    print("===============")
    while True:
        print(f"Turno de {turno_actual}")
        time.sleep(1)
        disparos_restantes = disparos_restantes_j2
        if turno_actual == JUGADOR_1:
            disparos_restantes = disparos_restantes_j1
        matriz_oponente = matriz_j1
        if turno_actual == JUGADOR_1:
            matriz_oponente = matriz_j2
        imprimir_matriz(matriz_oponente, False,
                        oponente_de_jugador(turno_actual))
        x, y = solicitar_coordenadas(turno_actual)
        acertado = disparar(x, y, matriz_oponente)
        if turno_actual == JUGADOR_1:
            disparos_restantes_j1 -= 1
        else:
            disparos_restantes_j2 -= 1

        imprimir_matriz(matriz_oponente, False,
                        oponente_de_jugador(turno_actual))
        if acertado:
            print("Disparo acertado")
            time.sleep(1)
            if todos_los_barcos_hundidos(matriz_oponente):
                indicar_victoria(turno_actual)
                imprimir_matrices_con_barcos(matriz_j1, matriz_j2)
                break
        else:
            print("Disparo fallado")
            time.sleep(1)
            if disparos_restantes-1 <= 0:
                indicar_fracaso(turno_actual)
                imprimir_matrices_con_barcos(matriz_j1, matriz_j2)
                break
            turno_actual = oponente_de_jugador(turno_actual)

def mostrar_menu():
    eleccion = ""
    while eleccion != "3":
        menu = """
1. Jugar
2. Instrucciones
3. Salir
Elige: """
        eleccion = input(menu)
        if eleccion == "1":
            SonidoBienvenida.play()#Esta tambien la agregué
            jugar()
        elif eleccion == "2":
            acerca_de()

mostrar_menu()