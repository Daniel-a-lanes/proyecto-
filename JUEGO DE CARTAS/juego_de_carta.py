import random

palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
valor_numerico = {str(i): i for i in range(2, 11)}
valor_numerico.update({'J':11, 'Q':12, 'K':13, 'A':14})

# Crear y mezclar baraja
baraja = [(valor, palo) for palo in palos for valor in valores]
random.shuffle(baraja)

# Repartir cartas en partes iguales
jugador1 = baraja[:9]
jugador2 = baraja[9:]

print("¡Empieza el juego de cartas!")

puntos_jugador1 = 0
puntos_jugador2 = 0
ronda = 1

while jugador1 and jugador2:
    print(f"\nRonda {ronda}:")
    carta1 = jugador1.pop(0)
    carta2 = jugador2.pop(0)
    print(f"Jugador 1 juega: {carta1[0]} de {carta1[1]}")
    print(f"Jugador 2 juega: {carta2[0]} de {carta2[1]}")

    val1 = valor_numerico[carta1[0]]
    val2 = valor_numerico[carta2[0]]

    if val1 > val2:
        puntos_jugador1 +=1
        print("Jugador 1 gana la ronda.")
    elif val2 > val1:
        puntos_jugador2 +=1
        print("Jugador 2 gana la ronda.")
    else:
        print("¡Empate en esta ronda!")

    ronda +=1

print("\n---Juego terminado Gracias por jugar---")
print(f"Puntos Jugador 1: {puntos_jugador1}")
print(f"Puntos Jugador 2: {puntos_jugador2}")

if puntos_jugador1 > puntos_jugador2:
    print("¡Jugador 1 gana el juego!")
elif puntos_jugador2 > puntos_jugador1:
    print("¡Jugador 2 gana el juego!")
else:
    print("¡El juego termina en empate!")
print("GAME OVER__DANIEL ALANES CACERES")
