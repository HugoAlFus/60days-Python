import json

PATH = "../../assets/example/"
FILE_PATH = "example_json.json"


def _read_json():
    with open(PATH + FILE_PATH, "r") as file:
        dates = json.load(file)
        return dates


def _print_json(json_dates):
    for key, value in json_dates.items():
        print(f"{key}: {value}")


dates = _read_json()
_print_json(dates)

key = input("Seleccione que clave quiere consultar: ")

if key in dates:
    print(f"{key}: {dates[key]}")
else:
    print("No se ha encontrado la clave introducida")
