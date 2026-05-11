import  time

print("""
░█▀▀░█▀█░█▀▀░█▀▀░█▀▀
░█░░░█░█░█▀▀░█▀▀░█▀▀
░▀▀▀░▀▀▀░▀░░░▀░░░▀▀▀

☕ CAFETERÍA INTEP ☕
━━━━━━━━━━━━━━━━━━━━
      BIENVENIDO
━━━━━━━━━━━━━━━━━━━━━
1.Pequeño
2.Mediano       
3.Grande
4.Salir
━━━━━━━━━━━━━━━━━━━━━       
""")

print("Que tamaño de cafe quieres el dia de hoy? ")

opcion = int(input("Ingrese el tamaño de cafe que desea: "))

if opcion == 1:
    print("Has elegido un cafe pequeño")
    multi = 2.0 * 0.10
    suma = 2.0 + multi
    print("El precio del cafe es: ", suma)

elif opcion ==2:
    print("Has elegido un cafe mediano")
    multi = 3.0 * 0.10
    suma = 3.0 + multi
    print("El precio del cafe es: " ,suma)

elif opcion == 3:
    print("Has elegido un cafe grande") 
    multi = 4.0 * 0.10
    suma = 4.0 + multi
    print("El precio del cafe es: ",suma)
elif opcion == 4:
    print("Gracias por venir") 

print("☕ Preparando tu café...\n")

barra = ""

for i in range(10):
    barra += "█"
    print(f"\r[{barra:<10}] {(i+1)*10}%", end="")
    time.sleep(0.5)
time.sleep(2)
print("\n✅ ¡Tu café está listo!")

print("¡Tu cafe esta listo! Disfrutalo ☕")
print(r"""
        ( (
         ) )
      ........
      |      |]
      \      /
       `----'
      """)

print("Gracias por su compra")

print(r"""
        \o/
         |
        / \
      """)