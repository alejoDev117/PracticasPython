import random
import time
from ventanas import  *
import pygame

FILAS = 6
COLUMNAS = 8
MAR = " "
SUBMARINO = "○"  # Ocupa una celda
DESTRUCTOR = "●"  # Ocupa dos celdas
DESTRUCTOR_VERTICAL = "◻"  # Ocupa tres celdas
MAMADISIMO = "🔲" # Ocupa cuatro celdas
DISPARO_FALLADO = "ø"
DISPARO_ACERTADO = "X"
DISPAROS_INICIALES = 10000000000000000000000000
CANTIDAD_BARCOS_INICIALES = 8
JUGADOR_1 = "J1"
JUGADOR_2 = "J2"


def obtener_matriz_inicial():
    matriz = []
    for y in range(FILAS):
        matriz.append([])
        for x in range(COLUMNAS):
            matriz[y].append(MAR)
    return matriz


def incrementar_letra(letra):
    return chr(ord(letra)+1)


def imprimir_separador_horizontal():
    for _ in range(COLUMNAS+1):
        print("+---", end="")
    print("+")


def imprimir_fila_de_numeros():
    print("|   ", end="")
    for x in range(COLUMNAS):
        print(f"| {x+1} ", end="")
    print("|")

def es_mar(x, y, matriz):
    return matriz[y][x] == MAR


def coordenada_en_rango(x, y):
    return x >= 0 and x <= COLUMNAS-1 and y >= 0 and y <= FILAS-1


def colocar_e_imprimir_barcos(matriz, cantidad_barcos, jugador):
    barcos_una_celda = cantidad_barcos//2
    barcos_dos_celdas_verticales = cantidad_barcos//4
    barcos_tres_celdas_horizontales = cantidad_barcos//3
    barcos_cuatro_celdas_vertical = cantidad_barcos//9
    if jugador == JUGADOR_1:
        print("Imprimiendo barcos del jugador 1 ")
        time.sleep(1)
    else:
        print("Imprimiendo barcos del jugador 2 ")
        time.sleep(1)
    print(f"Barcos de una celda: {barcos_una_celda}")
    time.sleep(1)
    print(f"Barcos verticales de dos celdas: {barcos_dos_celdas_verticales}")
    time.sleep(1)
    print(f"Barcos horizontales de tres celdas: {barcos_tres_celdas_horizontales}")
    time.sleep(1)
    print(f"Barcos verticales de cuatro celdas: {barcos_cuatro_celdas_vertical}")
    time.sleep(1)
    print(f"Total: {barcos_una_celda + barcos_dos_celdas_verticales + barcos_tres_celdas_horizontales + barcos_cuatro_celdas_vertical}")
    time.sleep(1)
    matriz = colocar_barcos_de_tres_celdas_horizontal(barcos_tres_celdas_horizontales, DESTRUCTOR, matriz)
    matriz = colocar_barcos_de_dos_celdas_vertical(barcos_dos_celdas_verticales, DESTRUCTOR_VERTICAL, matriz)
    matriz = colocar_barcos_de_una_celda(barcos_una_celda, SUBMARINO, matriz)
    matriz = colocar_barcos_de_cuatro_celdas_vertical(barcos_cuatro_celdas_vertical,MAMADISIMO,matriz)
    return matriz


def obtener_x_aleatoria():
    return random.randint(0, COLUMNAS-1)


def obtener_y_aleatoria():
    return random.randint(0, FILAS-1)


def colocar_barcos_de_una_celda(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        if es_mar(x, y, matriz):
            matriz[y][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz


def colocar_barcos_de_tres_celdas_horizontal(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        x2 = x+2
        x1 = x+1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and es_mar(x, y, matriz) and es_mar(x2, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x2] = tipo_barco
            matriz[y][x1] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz


def colocar_barcos_de_dos_celdas_vertical(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        y2 = y+1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y2) and es_mar(x, y, matriz) and es_mar(x, y2, matriz):
            matriz[y][x] = tipo_barco
            matriz[y2][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz

def colocar_barcos_de_cuatro_celdas_vertical(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        y2 = y+3
        y1 = y+2
        y3 = y +1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y2) and es_mar(x, y, matriz) and es_mar(x, y2, matriz):
            matriz[y][x] = tipo_barco
            matriz[y2][x] = tipo_barco
            matriz[y1][x] = tipo_barco
            matriz[y3][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz


def imprimir_disparos_restantes(disparos_restantes, jugador):
    print(f"Disparos restantes de {jugador}: {disparos_restantes}")


def imprimir_matriz(matriz, deberia_mostrar_barcos, jugador):
    print(f"Este es el mar del jugador {jugador}: ")
    time.sleep(1)
    letra = "A"
    for y in range(FILAS):
        imprimir_separador_horizontal()
        print(f"| {letra} ", end="")
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            valor_real = celda
            if not deberia_mostrar_barcos and valor_real != MAR and valor_real != DISPARO_FALLADO and valor_real != DISPARO_ACERTADO:
                valor_real = " "
            print(f"| {valor_real} ", end="")
        letra = incrementar_letra(letra)
        print("|",)  # Salto de línea
    imprimir_separador_horizontal()
    imprimir_fila_de_numeros()
    imprimir_separador_horizontal()


def solicitar_coordenadas(jugador):
    print(f"Solicitando coordenadas de disparo al jugador {jugador}")
    y = None
    x = None
    while True:
        letra_fila = input(
            "Ingresa la letra de la fila tal y como aparece en el tablero: ")
        if len(letra_fila) != 1:
            print("Debes ingresar únicamente una letra")
            continue
        y = ord(letra_fila) - 65
        if coordenada_en_rango(0, y):
            break
        else:
            print("Fila inválida")
    while True:
        try:
            x = int(input("Ingresa el número de columna: "))
            if coordenada_en_rango(x-1, 0):
                x = x-1  # Queremos el índice, así que restamos un 1 siempre
                break
            else:
                print("Columna inválida")
        except:
            print("Ingresa un número válido")

    return x, y


def disparar(x, y, matriz) -> bool:
    if es_mar(x, y, matriz):
        matriz[y][x] = DISPARO_FALLADO
        return False
    elif matriz[y][x] == DISPARO_FALLADO or matriz[y][x] == DISPARO_ACERTADO:
        return False
    else:
        matriz[y][x] = DISPARO_ACERTADO
        return True


def oponente_de_jugador(jugador):
    if jugador == JUGADOR_1:
        return JUGADOR_2
    else:
        return JUGADOR_1


def todos_los_barcos_hundidos(matriz):
    for y in range(FILAS):
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            # Si no es mar o un disparo, significa que todavía hay un barco por ahí
            if celda != MAR and celda != DISPARO_ACERTADO and celda != DISPARO_FALLADO:
                return False
    # Acabamos de recorrer toda la matriz y no regresamos en la línea anterior. Entonces todos los barcos han sido hundidos
    return True


def indicar_victoria(jugador):
    if jugador == "J1":
        ventanaJugador1()
    else:
        ventanaJugador2()



def indicar_fracaso(jugador):
    print(
        f"Fin del juego\nEl jugador {jugador} pierde. Se han acabado sus disparos")


def imprimir_matrices_con_barcos(matriz_j1, matriz_j2):
    time.sleep(1)
    print("Mostrando ubicación de los barcos de ambos jugadores:")
    time.sleep(1)
    imprimir_matriz(matriz_j1, True, JUGADOR_1)
    imprimir_matriz(matriz_j2, True, JUGADOR_2)

def acerca_de():
    print("Instrucciones: \n 1. Hay cuatro barcos\n 2. Si aciertas sigues jugando\n 3. Si aciertas X aparece este simbolo\n 4. Si fallas ø aparece este simbolo  ")