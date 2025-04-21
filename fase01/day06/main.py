text = input("Introduzca una palabra o frase para comprobar si es palíndromo:\n").replace(" ", "")

if len(text) % 2 != 0:
    half = len(text) // 2
    part_1 = text[:half].lower()
    part_2 = text[1 + half:].lower()
    inverted = part_2[::-1]

    if part_1 == inverted:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
else:
    print("No es un palíndromo")
