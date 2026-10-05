#Trabajo autonomo 2 
import random
print("Bienvenido al juego, empezemos...")
print("Piedra, Papel o Tijera")

opciones = ["piedra", "papel", "tijera"]
jugador = input("Elige piedra, papel o tijera: ")
computadora = random.choice(opciones)
print("La computadora eligió:", computadora)
if jugador == computadora:
    print("Empate")

elif jugador == "piedra" and computadora == "tijera":
    print("Ganaste")

elif jugador == "papel" and computadora == "piedra":
    print("Ganaste")

elif jugador == "tijera" and computadora == "papel":
    print("Ganaste")

else:
    print("Perdiste")
import random

continuar = "si"

while continuar == "si":

    print("Piedra, Papel o Tijera")

    opciones = ["piedra", "papel", "tijera"]

    jugador = input("Elige piedra, papel o tijera: ")

    computadora = random.choice(opciones)

    print("La computadora eligió:", computadora)

    if jugador == computadora:
        print("Empate")

    elif jugador == "piedra" and computadora == "tijera":
        print("Ganaste")

    elif jugador == "papel" and computadora == "piedra":
        print("Ganaste")

    elif jugador == "tijera" and computadora == "papel":
        print("Ganaste")

    else:
        print("Perdiste")

    continuar = input("¿Deseas continuar? si/no: ")

print("Gracias por jugar")