import random

options = ["👊", "✋", "✌️"]
victories_player = 0
victories_machine = 0


def _choose_option():
    option = 0
    while option < 1 or option > 3:
        option = input(
            """--Elija que quiere sacar--\n1.Piedra\n2.Papel\n3.Tijeras\n""")
        if option.isdigit():
            option = int(option)
            if option < 1 or option > 4:
                print("Por favor ingrese un número que sea valido (1,3)")
        else:
            option = 0
            print("Por favor indique números enteros")
    return option


def _check_winner():
    if player == machine:
        print(f"Empate\nJugador {player} vs Maquina {machine}")
    elif (player == options[0] and machine == options[2]) or (player == options[1] and machine == options[0]) or (
            player == options[2] and machine == options[1]):
        print(f"Ha ganado el jugador\nJugador {player} vs Maquina {machine}")
        return True
    else:
        print(f"Ha ganado la maquina\nJugador {player} vs Maquina {machine}")
        return False


while victories_player < 4 or victories_machine < 4:
    player = options[_choose_option() - 1]
    machine = random.choice(options)

    who_win = _check_winner()
    if who_win:
        victories_player += 1
    else:
        victories_machine += 1
