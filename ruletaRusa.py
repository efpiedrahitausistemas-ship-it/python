'''
Reto de Programación Simulador de Probabilidades: Ruleta Rusa

1.Descripcion del Problema
se requiere desarrollar un problema en Python que simule un sistema de azar basado en un revolver
 de 6 recamaras. El programa debe gestionar eventos aleatorio, pausas de ejecucion para mejorar la 
 experencia de usuario y control del flujo basado en condiciones de victoria o derrota

2. Requerimiento tecnicos:

El algoritmo debe cumplir con los siguientes requisitos:

*Inicializacion: Definir una recamara ganadora (bala) de forma
 aleatoria entre 1 y 6 (random)

*Bucle de juego:El usuario debe interctuar manaualmente (while)
para girar el tambor y disparar (time)

*Mecanica de azar: En cada turno, la posicion de la recamara que queda al frente 
al percutor debe ser aleatoria, simulando el giro del tambor 

*Condicion de derrota: Si  la recamara seleccionada coincide con la de la
bala, el programa termina inmediatamente (if)

*Condicion de Victoria: El jugador gana si logra sobrevivir a 5 intentos
( ya que el sexto intento seria fatal). (else)
'''
import random,time

print ("="*50) 
print ("Bienvenido al simulador de la Ruleta Rusa")
print ("="*50)

input("Poner Bala en el Tambor (Presionar Enter)")
bala = random.randint(1, 6)
time.sleep(0.5)

disparos = 0 

while True: 
    input("Girar el Tambor (Presionar enter)")
    recamara = random.randint(1, 6)


    input("Apuntar y Disparar(Presionar enter)")
    time.sleep (1)

    if recamara == bala:
        print("¡Bang! Has perdido. La bala estaba en la recamra \ Numero", bala)
        break
    else:
        disparos +=1
        print("Has sobrevivido a este intento")
        print ("intento de disparos:", disparos)

    if disparos == 5:
        print("¡Felicidades! Has ganado al sobrevivir a 5 intentos.")
        break

print ("="*50) 
print ("Fin del juego - Gracias por jugar")
print ("="*50)