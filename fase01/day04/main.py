import random
import string


def _ask_character(text):
    response = ""
    while response != "s" and response != "n":
        response = input(text).lower()
        if response != "s" and response != "n":
            print("Por favor introduzca un valor válido (s/n)")
    return response == "s"


list_character = list(string.ascii_letters)
list_numbers = list()
list_simbols = list()
if _ask_character("¿Quiere introducir números en su contraseña?\n"):
    list_numbers = list(string.digits)
if _ask_character("¿Quiere introducir simbolos en su contraseña?\n"):
    list_simbols = list("!@#$&?¿*%")

list_character_total = list_character + list_numbers + list_simbols
size = 20

password = "".join(random.choice(list_character_total) for _ in range(size))
print(f"Su contraseña es {password}")