import math

print("*" * 40)
print(" BIENVENIDO A LA CALCULADORA ".center(40, "*"))
print("*" * 40)

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

print ("Hola elige una opcion del menu")

#Operaciones que va a realizar la calculadora de acuerdo a la opcion dada por el usuario

try:
   opcion = int(input("selecciona la operacion que quieres realizar: "))

   if opcion ==1: 
      print("vas a sumar")  
      suma_uno= int(input("ingresa el primer numero: "))
      suma_dos= int(input("ingresa el segundo numero: "))
      suma = suma_uno + suma_dos
      print("El resultado de la suma es: ", suma)
   elif opcion == 2:
      print("vas a restar")
      resta_uno= int(input("ingresa el primer numero: "))
      resta_dos= int(input("ingresa el segundo numero: "))
      resta = resta_uno - resta_dos
      print("El resultado de la resta es: ", resta)
   elif opcion == 3:
      print("vas a multiplicar")
      multi_uno= int(input("ingresa el primer numero: "))
      multi_dos= int(input("ingresa el segundo numero: "))
      multi = multi_uno * multi_dos
      print("El resultado de la nultiplicacion es: ", multiplicacion)
   elif opcion == 4:
      print("vas a dividir")                 
      division_uno= int(input("ingresa el primer numero: "))
      division_dos= int(input("ingresa el segundo numero: "))
      division = division_uno / division_dos
      print("El resultado de la division es: ", division)
   elif opcion == 5:
      print("vas a calcular el factorial")
      factorial_n= int(input("ingresa el numero para calcular su factorial: "))
      factorial = math.factorial(factorial_n)
      print("El resultado del factorial es: ", factorial)
   elif opcion == 6:
      print("vas a calcular la potencia")
      potencia_uno= int(input("ingresa el primer numero: "))
      potencia_dos= int(input("ingresa el segundo numero: "))
      potencia = potencia_uno ** potencia_dos
      print("El resultado de la potencia es: ", potencia)
   elif opcion == 7:
      print("ejecutando la salida el programa......")
   else:
      print("opcion invalida, elige bine la opcion del menu")
except:
   print("Error: numero no valido")

