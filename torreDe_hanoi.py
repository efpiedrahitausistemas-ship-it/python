import os

def limpiar_pantalla():
    # Limpia la consola para dar el efecto de animacion
    os.system('cls' if os.name == 'nt' else 'clear')

def dibujar_torres(torres, n):
    
    #Dibuja el estado actual de las torres en la consola
    limpiar_pantalla()
    print("\n"+"==="*15)
    print("Torre de Hanoi".center(45))
    print("==="*15+ "\n")


    # Ancho maximo que ocupara el disco mas grande mas un espacio de margen
    ancho_columna = n * 2 + 3 

    # Dubujar desde arriba hacia abajo
    for i in range(n -1, -1, -1):
        fila=""
        for poste in ['A', 'B', 'C']:
            if i < len (torres[poste]): #Arreglo de 3 postes
                tamaño_disco = torres[poste][i]
                #crear el dibujo del disco (===)
                disco_str = "[" + "=" * ((tamaño_disco * 2) -1)+ "]"
                #centar el disco dentro del acnho de la columna
                fila += disco_str.center(ancho_columna)
            else:
                # Si no hay disco en esa posición, dibujar un espacio vacío
                fila += "|".center(ancho_columna)
        print(fila)
# Dibujar la base y las etiquetas de los postes
    print("-" * (ancho_columna * 3))
    print("A".center(ancho_columna) + "B".center(ancho_columna) + "C".center(ancho_columna))
    print("\n"+"==="*15)


def jugar_hanoi(n):
    # FUncion principal que controle el flujo para iniciar el programa 
    # Inicializar el estado del juego: el poste A tiene los discos 3, 2, 1 (de mayor a menor) 
    torres = {'A': list(range( n, 0, -1)), 'B': [], 'C': []}
    movimientos = 0 # Variable local para contar el numero de movinientos realizados

    while len(torres['B']) < n:
        dibujar_torres(torres, n)
        print(f"Movimientos realizados: {movimientos}") 
        print("Intrucciones: Ingrese el poste de origen y el destino separado por un espacio")
        print("Ejemplo: A C  para mover disco superior a  A hacia B")
        print("Escribir Q para salir del juego\n")

        entrada = input("Ingrese su movimiento: ").strip().upper()

        if entrada == 'Q':
            print("Gracias por jugar la torre de Hanoi. ¡Hasta la próxima!")
            return 
        partes = entrada.split() # Dividir la entrada en partes para obtener el origen y destino
        if len(partes) != 2 or partes[0] not in torres or partes[1] not in torres:
            print("Entrada inválida. Por favor asegurate de usar las letras A, B, C")
            input("Presiona Enter para continuar...")
            continue
        origen, destino = partes[0], partes[1] # Obtener el poste de origen y destino 
        
        #validar el movimiento: el poste de origen no debe estar vacio y disco a mover debe
        #ser mas pequeño que el disco superior del poste de destino (si no esta vacio)
        if not torres[origen]:
            print(f"El poste {origen} esta vacio. No se puede mover un disco desde ahi.")
            input("Presiona Enter para continuar...")
            continue
        disco_a_mover = torres[origen][-1] # Obtener el disco superior del poste de origen

        if torres[destino] and torres[destino][-1] < disco_a_mover:
            print( f"no puedes colocar un disco mas grande sobre uno mas pequeño en el poste {destino}.")
            input("Presiona Enter para continuar...")
            continue

        #si el movimiento es valido, realizarlo quitar el disco del poste de origen y 
        #agregarlo al poste de destino 
        torres[origen].pop() # Quitar el disco del poste de origen
        torres[destino].append(disco_a_mover) # Agregar el disco al poste de destino
        movimientos += 1 # Incrementar el contador de movimientos



#pantalla final del juego
    dibujar_torres(torres, n)
    print(f"¡Felicidades! Has completado la torre de Hanoi en {movimientos} movimientos.")  
    input("Presiona Enter para salir...")
                  




if __name__=="__main__":
   #puedes cambiar este numero para jugar con mas o menos discos
   #(recomiendo no mas de 5 para mantener lo manejable)
   jugar_hanoi(3) #Iniciar el juego con 3 discos