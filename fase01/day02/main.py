operation = 0
while operation < 1 or operation > 4:
    operation = input("""--Seleccione una de estas operaciones--\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n""")
    if operation.isdigit():
        operation = int(operation)
        if operation < 1 or operation > 4:
            print("Por favor ingrese un número que sea valido (1,4)")
    else:
        operation = 0
        print("Por favor indique números enteros")


def _check_number(number):
    while not number.isdigit():
        number = input("Por favor introduzca un valor válido: ")
    return int(number)


number_1 = input("Indique el primer número que quiere usar: ")
number_1 = _check_number(number_1)
number_2 = input("Indique el segundo número que quiere usar: ")
number_2 = _check_number(number_2)

match operation:
    case 1:
        total = number_1 + number_2
        print(f"Suma: {number_1} + {number_2} = {total}")
    case 2:
        total = number_1 - number_2
        print(f"Resta: {number_1} - {number_2} = {total}")
    case 3:
        total = number_1 * number_2
        print(f"Multiplicación: {number_1} x {number_2} = {total}")
    case 4:
        total = number_1 / number_2
        print(f"División: {number_1} / {number_2} = {total}")
