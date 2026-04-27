

# esto es un comentario de una sola linea

"""Esto es un comentario
de multiples lineas
de Python
"""

# Condicionales

"""
Simple: si()                         | if():
Dobles: si() Sino()                  | if(): elif():
Multiples: Switch                    | No existe 

""" 

# python trabaje con if simple
"""
Palabrareservada (condicion):
    SentenciaUno
    SentenciaDos

"""

if (True):
    print("Hola")
    print("Como estas")

if (False):
    print("bien")
    print("y usted")

# comparacion de numeros enteros en python
a=5
b=3
if(a>b):
    print("A es mayor que B")

# comparacion de datos booleanos en python
c= False
if (c== True):
    print("C es verdadero")

# comparacion de caracteres 
caracter = 'a'
if(caracter== 'b'):
    print("el caracter es :", caracter)

# comparacion de palabras en pyton
    palabra = "hola"
if(palabra == "chao"):
    print("la palabra es:", palabra)


#python trabaje con si doble
"""
Palabrareservada (condicion)
    SentenciaUno
    SentenciaDos
SiNo(condicion):
    SentenciaUno
    SentenciaUno
"""

nota = 4 

if(nota >= 4):
    print("Exelente")
elif(nota >= 2 and nota <= 3):
    print("Nesecita recuperar")
elif(nota < 2):
    print("Reprobo")
