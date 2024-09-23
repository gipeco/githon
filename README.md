# Piedra, Papel, Tijera

Este juego es para aprender a programar en Python, tiene algunas cosas que talvez no esten bien, pero estoy aprendiendo este maravilloso lenguaje.

Librerias

```
import random
from time import sleep
from tqdm import tqdm
import os
```

Python 3.8
for GIPECO

## Version 0.0.0

Primera version para aprender

## Version 0.0.1

Con ayuda de chatgtp se realizaron los siguientes cambios

1. Manejo de entradas inválidas:
   • En arma_player_sel(), si el jugador ingresa un número que no está entre 1 y 3, se llama recursivamente a la función. Esto podría llevar a un error de RecursionError si el jugador sigue ingresando opciones inválidas. Usa un bucle while en su lugar:

```
    def arma_player_sel():
    global arma_player
    while True:
        print("1", armas[0])
        print("2", armas[1])
        print("3", armas[2])
        player = int(input("Escoge una opción 1-2-3? "))
        if player in [1, 2, 3]:
            arma_player = armas[player - 1]
            print("Tu eliges:", arma_player)
            break
        else:
            print("Opción no válida, intenta de nuevo.")
```

2. Uso de sleep() en lugar de tqdm:
   • Has comentado el uso de tqdm. Si quieres darle un toque de suspenso, puedes usar un bucle for con sleep() en lugar de comentarlo.
   • Por ejemplo:

```
    for _ in range(3):
    sleep(1)
    print("PC está pensando...")
```

3. Simplicidad en el reinicio del juego:
   • Al reiniciar el juego, no es necesario llamar a todas las funciones en una sola línea. Simplemente puedes volver a llamar a game() y permitir que el flujo normal del programa continúe.
   • Cambia esto:

````
print("Game Restart!!!")
game()
arma_player_sel()
arma_pc_sel()
logica()
volver()```
````
