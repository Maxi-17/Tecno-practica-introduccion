import random
numero_random = random.randint (1,50) #elije el numero random que es verdadero
intentos_realizados = 0
max_intentos = 5
print(numero_random)
acierto = False
#presentamos el juego
print ("bienvenido al juego: Adivina el numero!")
print ("Tenes 5 intentos, diviertete")
#ciclo con 5 intentos (o eso intentamos)
while intentos_realizados < max_intentos and not acierto:
    intentos_restantes = max_intentos - intentos_realizados #variable que da los intentos que le quedan al usuario
    numero_de_intentos = intentos_realizados + 1   #variable que ingresa el usuario
    intento = int(input(f"intento {numero_de_intentos} (te quedan {intentos_restantes} intentos): Ingrese un numero entre 1 y 50:"))
    intentos_realizados +=1
    if intento == numero_random: #condicion, si intento (la variable) es mayor, igual o menor a el numero random
        acierto = True
        print ("Felicidades, elegiste el número" , numero_random, "Eres el ganador")
    elif intento > numero_random:
        print ("Tu numero es mayor")
    else:
        print ("Tu número es menor")
    if not acierto and intentos_realizados < max_intentos: #condicion si no hay acierto y quedan intentos
      print (f"Todavia te quedan {intentos_restantes - 1} intentos")
if not acierto: #condicion si no hay acierto y no quedan intentos
    print(f"Lo siento, te quedaste sin intentos. El número era {numero_random}. ¡Mejor suerte la próxima!")