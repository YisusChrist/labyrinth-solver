#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file     laberinto.py
@date     03/09/2023
@version  1.0
@license  GNU General Public License v3.0
@url      https://github.com/yisuschrist/labyrinth-solver
@author   Alejandro Gonzalez Teruel (https://github.com/alejandrom1999)
@desc     Reto de programación. URL: https://aprendeconalf.es/docencia/python/retos/laberinto/

@requires  Python 3.6 o mayor

Instrucciones:

El laberinto se representará como una una lista de listas, donde cada lista es
una fila del laberinto y cada casilla se representará con un espacio ' ' si
hay paso o con la letra 'X' si hay un muro, tal y como se muestra a continuación:

Ejemplo salida: ['Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha',
'Arriba', 'Arriba', 'Derecha', 'Derecha', 'Abajo', 'Abajo', 'Abajo']
"""

from enum import Enum


class Direcciones(Enum):
    NULL = "Null"
    ARRIBA = "Arriba"
    ABAJO = "Abajo"
    DERECHA = "Derecha"
    IZQUIERDA = "Izquierda"


visitados = []


def print_laberinto(laberinto: list[str], casilla_actual) -> None:
    global visitados

    for i in visitados:
        laberinto[i[0]][i[1]] = " "

    laberinto[casilla_actual[0]][casilla_actual[1]] = "-"

    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            print(laberinto[i][j], end=" ")
        print()


def crear_tablero(filas: int, columnas: int) -> list:
    """
    Crea un tablero de laberinto de tamaño filas x columnas

    Args:
        filas (int): Número de filas del laberinto
        columnas (int): Número de columnas del laberinto

    Returns:
        list: Tablero de laberinto
    """
    laberinto = []

    """
    .............
    . E X X X X .
    .   X       .
    .   X   X   .
    .       X   .
    . X X X X S .
    .............
    """

    muro = (
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 1),
        (2, 1),
        (2, 3),
        (3, 3),
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 3),
    )

    for i in range(filas):
        laberinto.append([])
        for _ in range(columnas):
            laberinto[i].append(" ")

    for i in range(len(muro)):
        laberinto[muro[i][0]][muro[i][1]] = "X"

    laberinto[4][4] = "S"

    return laberinto


def instanciar_laberinto(laberinto: list[str]) -> (int, int):
    """
    Instancia el laberinto

    Args:
        laberinto (list): Tablero de laberinto

    Returns:
        (int, int): Coordenadas de la entrada y la salida
    """
    filas = columnas = len(laberinto)

    entrada = (0, 0)
    salida = (filas - 1, columnas - 1)

    return entrada, salida


def siguiente_casilla(laberinto: list[str], casilla_actual: tuple) -> (tuple, str):
    """
    Calcula la siguiente casilla a la que moverse

    Args:
        laberinto (list): Tablero de laberinto
        casilla_actual (tuple): Coordenadas de la casilla actual

    Returns:
        (tuple, str): Coordenadas de la casilla destino y dirección en la que
        moverse
    """
    global visitados

    for direccion in Direcciones:
        if direccion == Direcciones.NULL:
            continue

        destino = moverse(laberinto, casilla_actual, direccion)
        if destino is None:
            continue

        print_laberinto(laberinto, casilla_actual)

        visitados.append(destino)

        return destino, direccion.value

    return None, None


def buscar_solucion(laberinto: list[str], entrada: tuple, salida: tuple) -> list[str]:
    """
    Busca la solución al laberinto

    Args:
        laberinto (list): Tablero de laberinto
        entrada (tuple): Coordenadas de la entrada
        salida (tuple): Coordenadas de la salida

    Returns:
        list: Lista de direcciones para llegar a la salida
    """
    global visitados

    soluciones = []
    encontrado = False

    casilla_actual = entrada
    visitados.append(casilla_actual)
    while encontrado is False:
        casilla_actual, direct = siguiente_casilla(laberinto, casilla_actual)
        print(casilla_actual, " ", direct)
        input("\nContinuar? ")
        soluciones.append(direct)

        encontrado = es_solucion(casilla_actual, salida)

    return soluciones


def es_solucion(casilla_actual: tuple, salida: tuple) -> bool:
    """
    Comprueba si la casilla actual es la salida

    Args:
        casilla_actual (tuple): Coordenadas de la casilla actual
        salida (tuple): Coordenadas de la salida

    Returns:
        bool: True si la casilla actual es la salida, False en caso contrario
    """
    return casilla_actual == salida


def moverse(laberinto, casilla_actual, direccion) -> tuple:
    """
    Mueve el personaje en la dirección indicada

    Args:
        laberinto (list): Tablero de laberinto
        casilla_actual (tuple): Coordenadas de la casilla actual
        direccion (Direcciones): Dirección en la que moverse

    Returns:
        tuple: Coordenadas de la casilla destino
    """
    global visitados

    # Calcular la casilla destino
    match direccion:
        case Direcciones.ARRIBA:
            destino = (casilla_actual[0] - 1, casilla_actual[1])
        case Direcciones.ABAJO:
            destino = (casilla_actual[0] + 1, casilla_actual[1])
        case Direcciones.DERECHA:
            destino = (casilla_actual[0], casilla_actual[1] + 1)
        case Direcciones.IZQUIERDA:
            destino = (casilla_actual[0], casilla_actual[1] - 1)
        case _:
            destino = None

    try:
        laberinto[destino[0]][destino[1]]
    except IndexError:
        return None

    # Si la casilla destino está fuera del tablero
    if (destino[0] < 0 or destino[1] < 0) or (
        destino[0] >= len(laberinto) or destino[1] >= len(laberinto)
    ):
        return None

    # Si la casilla actual es un muro
    if laberinto[destino[0]][destino[1]] == "X":
        return None

    # Si la casilla destino ya ha sido visitada
    if destino in visitados:
        return None

    return destino


def main():
    laberinto = crear_tablero(filas=5, columnas=5)
    entrada, salida = instanciar_laberinto(laberinto)

    try:
        solucion = buscar_solucion(laberinto=laberinto, entrada=entrada, salida=salida)
        print(solucion)
    except KeyboardInterrupt:
        print("Programa interrumpido por el fede")
        exit()


if __name__ == "__main__":
    main()
