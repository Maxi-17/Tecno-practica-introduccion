#Paul
import random

min_num = 1
max_num = 50
numero_secreto = random.randint(min_num, max_num)
intentos = 0
max_intentos = 5

print(f"""
|❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖|\n ¡Bienvenido al Juego de Adivinanza!\n Intenta adivinar el númmero secreto\n entre {min_num} y {max_num}.\n|❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖|\n""")

while intentos < max_intentos:
        numero_jugador = int(input(f"Intento {intentos + 1} de {max_intentos}. Ingresa tu número: "))
        intentos += 1

        match numero_jugador:
          case _ if numero_jugador == numero_secreto:
            print("""\n\n❖❖❖❖¡Felicidades!\n¡Has ganado!❖❖❖❖""")
            break
          case _ if numero_jugador < numero_secreto:
            print("El número es mayor ↑↑")
          case _ if numero_jugador > numero_secreto:
            print("El número es menor ↓↓")

if intentos == max_intentos:
  print(f"""\n****Has perdido. El número secreto era {numero_secreto}****""")