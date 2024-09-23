# Este juego es para aprender a programar en Python, tiene algunas cosas que talvez no esten bien, pero estoy aprendiendo este maravilloso lenjuage.
# Python 3.8

import random
from time import sleep
from tqdm import tqdm
import os


# Variables del Juego
armas = ["Piedra", "Papel", "Tijera"]
arma_player = ""
arma_pc = ""

# Arranca el Juego
def game():
    print(r"""
    
  _______  __  .___________. __    __    ______   .__   __. 
 /  _____||  | |           ||  |  |  |  /  __  \  |  \ |  | 
|  |  __  |  | `---|  |----`|  |__|  | |  |  |  | |   \|  | 
|  | |_ | |  |     |  |     |   __   | |  |  |  | |  . `  | 
|  |__| | |  |     |  |     |  |  |  | |  `--'  | |  |\   | 
 \______| |__|     |__|     |__|  |__|  \______/  |__| \__| 
                                                            
  _______      ___      .___  ___.  _______ 
 /  _____|    /   \     |   \/   | |   ____|
|  |  __     /  ^  \    |  \  /  | |  |__   
|  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  |__| |  /  _____  \  |  |  |  | |  |____ 
 \______| /__/     \__\ |__|  |__| |_______|
                                            

""")
    print("PIEDRA, PAPEL O TIJERA")
    print("VERSION 0.0.1")
    print("FOR GIPECO")
    print()


game()
# Elección de Armas
# ------- Jugador elige un arma -------
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


arma_player_sel()
for _ in range(3):
    sleep(1)
    print("PC está pensando...")

# ------- PC elije un arma -------

# Caracteristica de tiempo para darle un poco más de suspenso


def arma_pc_sel():
    global arma_pc
    # for i in tqdm(range(50)):
    sleep(0.01)
    # Metodo 1 (escoge un arma de un random de 1-3) version 0.1
    """
    arma = random.randrange(0, 3)
    if arma == 0:
        arma_pc = "Piedra"
    elif arma == 1:
        arma_pc = "Papel"
    elif arma == 2:
        arma_pc = "Tijera"
    print("PC elige: ", arma_pc)
    """

    # Metodo 2 (Escoge un arma de un array de armas)
    arma_pc = random.choice(armas)
    print("PC elige: ", arma_pc)
    print()
    return arma_pc


arma_pc_sel()

# Comprobacion de armas

print(arma_player, " VRS ", arma_pc)
print()
# Mecanica del Juego

# Si player Gana


def logica():
    if arma_player == armas[1] and arma_pc == armas[0]:
        print("Ganaste!, Papel envuelve a Piedra. :) ")
        print()
    elif arma_player == armas[2] and arma_pc == armas[1]:
        print("Ganaste!, Tijera corta Papel. :) ")
        print()
    elif arma_player == armas[0] and arma_pc == armas[2]:
        print("Ganaste!, Piedra destruye a Tijera. :) ")
        print()
    # Si Player pierde
    elif arma_player == armas[1] and arma_pc == armas[2]:
        print("Perdiste!, Tijera corta Papel. :( ")
        print()
    elif arma_player == armas[2] and arma_pc == armas[0]:
        print("Perdiste!, Piedra destruye a Tijera. :( ")
        print()
    elif arma_player == armas[0] and arma_pc == armas[1]:
        print("Perdiste!, Papel envuelve a Piedra. :( ")
        print()
    elif arma_player == arma_pc:
        print("Empate: :)", arma_player, "es igual a", arma_pc)
        print()
    return


logica()

# Volver a empezar el juego


def volver():
    jugarNow = str(input("QUIERES VOLVER A JUGAR? S/N "))
    if jugarNow == "s" or jugarNow == "S" or jugarNow == "Si" or jugarNow == "SI" or jugarNow == "si":
        print("Game Restart !!!")
        game()
        arma_player_sel()
        arma_pc_sel()
        logica()
        volver()
    elif jugarNow == "n" or jugarNow == "N" or jugarNow == "No" or jugarNow == "NO" or jugarNow == "no":
        exit()
    else:
        print("DEBE SELECIONAR SI O NO")
        volver()


volver()
