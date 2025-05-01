PATH = "../../assets/example/"
file = input("Indique que fichero quiere abrir, tiene que estar en 'assets/example': ")


def _open_file():
    with open(PATH + file, "r") as read_file:
        content = read_file.read()
    return content


def _write_file():
    new_content = input("Introduzca el texto que quiere añadir: ")
    with open(PATH + file, "a") as write_file:
        write_file.write(new_content)


try:
    print(f"El contenido del fichero es el siguiente:\n{_open_file()}")
    _write_file()
    print(f"El contenido del fichero modificado es el siguiente:\n{_open_file()}")
except OSError:
    print("Se ha introducido un ficheo erroneo, se saldra del programa")
