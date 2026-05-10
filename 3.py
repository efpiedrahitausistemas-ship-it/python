# ---------------- FUNCIONES BÁSICAS ----------------

def sumar():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", a + b)
    except:
        print("Error: Entrada no válida")


def restar():
    try:
        a = float(input("Ingrese el minuendo: "))
        b = float(input("Ingrese el sustraendo: "))
        print("Resultado:", a - b)
    except:
        print("Error: Entrada no válida")


def multiplicar():
    try:
        a = float(input("Ingrese el primer factor: "))
        b = float(input("Ingrese el segundo factor: "))
        print("Resultado:", a * b)
    except:
        print("Error: Entrada no válida")


def dividir():
    try:
        a = float(input("Ingrese el dividendo: "))
        b = float(input("Ingrese el divisor: "))
        if b == 0:
            print("Error: No se puede dividir entre cero")
        else:
            print("Resultado:", a / b)
    except:
        print("Error: Entrada no válida")


# ---------------- FACTORIAL ----------------

def factorialCalculo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorialCalculo(n - 1)


def factorial():
    try:
        n = int(input("Ingrese un número entero positivo: "))
        if n < 0:
            print("Error: El número debe ser positivo")
        else:
            print("Resultado:", factorialCalculo(n))
    except:
        print("Error: Entrada no válida")


# ---------------- POTENCIA ----------------

def potenciaCalculo(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potenciaCalculo(base, exp - 1)


def potencia():
    try:
        base = float(input("Ingrese la base: "))
        exp = int(input("Ingrese el exponente (entero): "))
        print("Resultado:", potenciaCalculo(base, exp))
    except:
        print("Error: Entrada no válida")


# ---------------- MENÚ PRINCIPAL ----------------

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

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                sumar()
            elif opcion == 2:
                restar()
            elif opcion == 3:
                multiplicar()
            elif opcion == 4:
                dividir()
            elif opcion == 5:
                factorial()
            elif opcion == 6:
                potencia()
            elif opcion == 7:
                print("Saliendo del programa...")
            else:
                print("Opción inválida")
        except:
            print("Error: Debe ingresar un número")

# ---------------- EJECUCIÓN ----------------
calculadora()