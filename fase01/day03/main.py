conversion = 0
while conversion < 1 or conversion > 2:
    conversion = input("""--Selecciona el tipo de conversion--\n1.Celsius a Fahrenheit\n2.Fahrenheit a Celsius\n""")
    if conversion.isdigit():
        conversion = float(conversion)
        if conversion < 1 or conversion > 2:
            print("Por favor ingrese un número que sea valido (1,2)")
    else:
        conversion = 0
        print("Por favor indique números enteros")


def _enter_degrees():
    degrees = 0
    while not isinstance(degrees, float):
        try:
            degrees = float(input("Introduzca los grados que desea convertir: "))
        except ValueError:
            print("Por favor introduza cun valor valido")

    return degrees


degrees = _enter_degrees()

match conversion:
    case 1:
        result = (degrees * (9 / 5)) + 32
        print(f"El resultado de la conversion de {degrees}ºC Celsius a Fahrenheit es: {result} ºF")
    case 2:
        result = (degrees - 32) * (5 / 9)
        print(f"El resultado de la conversion de {degrees}ºF Fahrenheit a Celsius es: {result} ºC")
