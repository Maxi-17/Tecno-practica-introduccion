#Versión de Maxi:

import random

num_secreto = random.randint(1, 17)
print ()
print('****** Se bienvenido al juego Adivina el Número! ******')
print ()

limite_super = int(input('Elegi el rango en el que vas a adivinar el numero  (minimo 2 ;)  ): '))
print ()
if limite_super < 2:
    limite_super = 2  
num_secreto = random.randint(1, limite_super)

# Cantidad de intentos a eleccion del usuario
max_intentos = int(input('Cuántos intentos quieres tener? (mínimo 1, máximo 10): '))
print ()
if max_intentos < 1:
    max_intentos = 1
if max_intentos > 10:
    max_intentos = 10

intentos = 0
acertado = False

# Logica del juego
while intentos < max_intentos:
    print('Intento', intentos + 1, 'de', max_intentos)
    print ()
    num_jugador = int(input(f'Ingresa un número entre 1 y {limite_super}: '))
    print ()

    if num_jugador == num_secreto:
        print('Felicidadess! Adivinaste el número!!', num_secreto)
        print ()
        acertado = True
        intentos = max_intentos  
    else:
        if num_jugador < num_secreto:
            print('El número secreto es MAYOr')
            print ()
        else:
            print('El numero secreto es MENOR')
            print ()
        intentos = intentos + 1

# Se verifica si perdio
if not acertado:
    print('Perdon, no adivinaste el numero  :( )')
    print ()
    print('El número secreto era', num_secreto)

