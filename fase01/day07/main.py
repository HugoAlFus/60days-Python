import random

print("Vas a tener que adivinar un número entre el 1 y el 10 (enteros)")
is_correct = False

while not is_correct:
    player = 0
    machine = random.randint(1, 10)
    while player < 1 or player > 10:
        player = input("Introduzca el número que crea que es: ")
        if player.isdigit():
            player = int(player)
            if player < 1 or player > 10:
                print("Por favor ingrese un número que sea valido (1,10)")
        else:
            player = 0
            print("Por favor introduzca números enteros")

    if player == machine:
        is_correct = True
    else:
        print("No se ha acertado el número")
        print(f"Número maquina: {machine} - Tú número: {player}")
