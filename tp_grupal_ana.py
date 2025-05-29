# Versión Ana
import random

num_max = 99
num_min = 1
numero_random = random.randint(num_min,num_max)
intentos = 1
max_intentos = 5

print('''
               #####################################################
               ¡Bienvenido/a al juego de adivinar el número secreto!
               #####################################################
     '''
               )

print(numero_random)
while intentos <= max_intentos:
    intentos = intentos + 1
    num_ingresado = int(input(f"Por favor, ingrese un número del {num_min} al {num_max}: " ))
    if num_ingresado == numero_random  and num_ingresado >= num_min and num_ingresado <= num_max:
        print(f"¡Felicitaciones! adivinaste el número secreto: {numero_random}")
        break
    elif num_ingresado > numero_random  and num_ingresado >= num_min and num_ingresado <= num_max:
        print(f"El número secreto es menor al que ingresaste. Te quedan {max_intentos-intentos+1} intentos.")
    elif num_ingresado < numero_random  and num_ingresado >= num_min and num_ingresado <= num_max:
        print(f"El número secreto es mayor al que ingresaste. Te quedan {max_intentos-intentos+1} intentos.")
    elif  num_ingresado <= num_min and num_ingresado >= num_max:
        print(f"El número que ingresaste no es correcto. Te quedan {max_intentos-intentos+1} intentos.")
else:
    print(f"¡Perdiste!, el número secreto era {numero_random}")