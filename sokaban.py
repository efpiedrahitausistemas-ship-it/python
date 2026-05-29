import os


# Mapas del juego
mapas = [

    [
        list("########"),
        list("#      #"),
        list("# $$   #"),
        list("# ..@  #"),
        list("#      #"),
        list("########")
    ],

    [
        list("########"),
        list("#   .  #"),
        list("#   $  #"),
        list("#   $  #"),
        list("# . @  #"),
        list("#      #"),
        list("########")
    ],

    [
        list("#########"),
        list("#   .   #"),
        list("#   $   #"),
        list("# $$@   #"),
        list("#   .   #"),
        list("#       #"),
        list("#########")
    ],

    [
        list("#########"),
        list("#   .   #"),
        list("# $$ $  #"),
        list("#   @   #"),
        list("#   .   #"),
        list("#       #"),
        list("#########")
    ],

    [
        list("##########"),
        list("# .   .  #"),
        list("# $$ $$  #"),
        list("#    @   #"),
        list("#        #"),
        list("##########")
    ]
]


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def dibujar_mapa(mapa):

    limpiar_pantalla()

    print("Bienvenido al juego de sokaban. Espero se divierta")
    print("Controles para el juego")
    print("W - Arriba")
    print("A - Izquierda")
    print("S - Abajo")
    print("D - Derecha")
    print("Q - Salir del juego")
    print()

    for fila in mapa:
        print("".join(fila))


# Encontramos al jugador en el mapa
def encontrar_jugador(mapa):

    for i, fila in enumerate(mapa):

        for j, celda in enumerate(fila):

            if celda == '@':
                return i, j

    return None, None


# Movimiento del jugador
def mover_jugador(mapa, direccion):

    i, j = encontrar_jugador(mapa)

    if i is None:
        return mapa


    di, dj = 0, 0

    if direccion == 'W':
        di = -1

    elif direccion == 'S':
        di = 1

    elif direccion == 'A':
        dj = -1

    elif direccion == 'D':
        dj = 1

    else:
        return mapa


    nueva_i = i + di
    nueva_j = j + dj


    # no salir del limite del mapa
    if nueva_i < 0 or nueva_i >= len(mapa):
        return mapa

    if nueva_j < 0 or nueva_j >= len(mapa[0]):
        return mapa


    # movimiento normal
    if mapa[nueva_i][nueva_j] in [' ', '.']:

        mapa[i][j] = ' '
        mapa[nueva_i][nueva_j] = '@'


    # Movimiento de la caja
    elif mapa[nueva_i][nueva_j] == '$':

        sigiente_i = nueva_i + di
        sigiente_j = nueva_j + dj


        if sigiente_i < 0 or sigiente_i >= len(mapa):
            return mapa

        if sigiente_j < 0 or sigiente_j >= len(mapa[0]):
            return mapa


        # Espacio para la caja
        if mapa[sigiente_i][sigiente_j] in [' ', '.']:

            mapa[sigiente_i][sigiente_j] = '$'
            mapa[nueva_i][nueva_j] = '@'
            mapa[i][j] = ' '


    return mapa


# verificar si gano
def nivel_completado(mapa):

    for fila in mapa:

        for celda in fila:

            if celda == '.':
                return False

    return True


# juego
nivel_actual = 0

while nivel_actual < len(mapas):

    dibujar_mapa(mapas[nivel_actual])

    movimiento = input("movimientos: ").upper()

    if movimiento == 'Q':
        break

    mapas[nivel_actual] = mover_jugador(mapas[nivel_actual], movimiento)

    if nivel_completado(mapas[nivel_actual]):

        print("Nivel completado")

        input("Presione ENTER para continuar")

        nivel_actual += 1


print("Juego terminado")