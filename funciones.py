
import random

#funciones que no reciben parametros y no devuelven resultados

def mostrar_bienvenida():
    #no hay parametros de entrada entre los parentesis
    print ("¡bienvenido a la funcion de bienvenida!")
    print ("por favor, selecciona una opcion del menú")
    print ("1. opcion 1")
    print ("1. opncion 2")
    print ("3. opcion 3")
    print ("4. salir")

    #para usar la funcion, simplemete la llamamos por su nombre seguido de parentesis
mostrar_bienvenida()


#funcion recibe parametros pero no devuelven resultados

def saludar_persona(nombre, edad):
    #recibe nombre y edad como parametros de entrada
    print (f"¡hola {nombre}, veo que tienes {edad} años!")
    #no tiene return, solo imprime en patnalla el mensaje

    saludar_persona("Estrella", 45)
    #Lo llamamos a la funcion con argumentos especificos



    #funciones que no reciben parametros y devueleven resultados

    def tirar_dado():
        #no recibe parametros de entrada
        numero_obtenido = random.randint (1, 6) #genera un numero aleatorio de 1y 6
        return numero_obtenido #devuleve el numero obtenido
    resultado = tirar_dado()#llamamos a la funcion y almacenamiento de resultado en una variable
    print (f"has tirado el dado y obtuviste: {resultado}")


#funciones que recibe parametros y devuelven resultados

def calcular_area_rectangulo(base, altura):
    #recibe los datos necesarios
    area= base*altura
    #devuleve el resultado del calculo
    return area

#para usarla:
mi_area = calcular_area_rectangulo(5, 10)
print (f"el area del rectangulo es: {mi_area}")