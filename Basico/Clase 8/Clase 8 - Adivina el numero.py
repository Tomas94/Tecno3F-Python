import random
numero_secreto = random.randint(1,50)

#Un contados para el while
contador = 0
numero = -1

while contador < 5 and numero_secreto != numero:
    numero = int(input("Ingrese un numero entre 1 y 50: "))    #Pido al jugador que elija un numero 
    
    if numero < numero_secreto:                                 #Si el numero que dice el jugador es menor al secreto
        print("el numero a adivinar es mayor.")
        contador += 1
    elif numero > numero_secreto:                               #Si el numero que dice el jugador es mayor al secreto
        print("el numero a adivinar es menor.")
        contador += 1
    
   
#Acá se llega cuando falló 5 veces o adivino el numero, dependiendo el caso imprime
if contador == 5:
    print(f"Lo lamento, fallaste, el numero era {numero_secreto}")
else:
    print(f"Adivinaste el numero, era: {numero_secreto}")