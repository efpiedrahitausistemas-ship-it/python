'''
Reto de Programacion #1: Piedra, Papel o Tijera

1.Descrpcion del problema:
se solicita desarrollar un programa interactivo en Python que
permita a un usario enfrentarse contra la computadora en el Clasico 
juego de Piedra, Papel o Tijera 
El programa debe ser capaz de procesar la entrada del usario,
generar una respuesta aleatoria y determinar un ganador basada en las reglas
tradicionales.

2.Requerimiento tecnicos:
El algoritmo debe estructurarse de la siguiente manera:

*Entrada de Datos: solicitar al usuario su eleccion. El programa debe ser capaz de reconocer 
la entrada sin importar si se escribe en mayusculas o minisculas.

*Logica de comparacion:
Implementar las condiciones necesarias para evaluar.

1.Empate: Ambaas elecciones son iguales
2.Victoria: El usuario vence a la pc.
(Piedra vence Tijeras, tijera vence Papel, Papel vence piedra)
3.Derrota:La pc vence al usario

*Control de flujo: el juego debe repetirse indefinidamente dentro de 
un bucle hasta que el usario decida escribir la palabra(salida)
'''


import random


opciones = ["piedra", "papel", "tijera"]

# Encabezado decorativo
print("*" * 40)
print(" PIEDRA, PAPEL O TIJERA ".center(40, "*"))
print("*" * 40)

# Bucle infinito
while True:
    # Entrada del usuario
    usuario = input("Elige (Piedra, Papel, Tijera) o escribe 'Salir': ").lower()

    # Salir del juego
    if usuario == "salir":
        print("Gracias por jugar ")
        break

    # Validar entrada
    if usuario not in opciones:
        print("Opción inválida, intenta de nuevo.")
        continue

    # Elección de la computadora
    pc = random.choice(opciones)

    print("Tú elegiste:", usuario)
    print("La computadora eligió:", pc)

    # Lógica del juego
    if usuario == pc:
        print("Resultado: ¡Empate!")
    elif (usuario == "piedra" and pc == "tijera") or \
         (usuario == "tijera" and pc == "papel") or \
         (usuario == "papel" and pc == "piedra"):
        print("Resultado: ¡Ganaste!")
    else:
        print("Resultado: Perdiste")