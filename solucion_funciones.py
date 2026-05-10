
import math

#operacion de la suma
def suma(numero_uno, numero_dos):
   suma = numero_uno + numero_dos

   return suma





#operacion de la resta
def resta(numero_uno, numero_dos):
   

    resta = numero_uno - numero_dos
    return resta




#operacion de la multiplicacion
def multiplicacion(numero_uno, numero_dos):
    
   multiplicacion= numero_uno * numero_dos

   return multiplicacion






#operacion de la divivcion
def division(numero_uno, numero_dos):  
     
   division = numero_uno / numero_dos
   return division




#operacion factorial

def factorial(n):
   
   factorial = math.factorial(6)
   return factorial


#operacion potencia
def potencia(numero_uno, numero_dos):
   potencia = numero_uno** numero_dos


print("*" * 40)
print(" BIENVENIDO A LA CALCULADORA ".center(40, "*"))
print("*" * 40)


#----------------MENÚ-----------------


def calculadora():
    opcion = 0

    while opcion != 7:
        print("""
╔══════════════════════════════╗
║       CALCULADORA 🧮         ║
╠══════════════════════════════╣
║ 1. Sumar                    ║
║ 2. Restar                   ║
║ 3. Multiplicar              ║
║ 4. Dividir                  ║
║ 5. Factorial                ║
║ 6. Potencia                 ║
║ 7. Salir                    ║
╚══════════════════════════════╝
""")    

















calculadora()
