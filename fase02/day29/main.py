import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")

file_ventas = "../../assets/example/otros/ventas.csv"
file_productos = "../../assets/example/otros/productos.csv"
file_poblacion = "../../assets/example/otros/poblacion.csv"


def _get_data(file_csv):
    dates = []
    with open(file_csv, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(";")
            dates.append(parts)
        return dates


def _obtain_information(data, index):
    values = []
    for i, linea in enumerate(data):
        if i == 0:
            continue
        values.append(linea[index])
    return values


dates = _get_data(file_ventas)
values_x = _obtain_information(dates, 0)
values_y = _obtain_information(dates, 1)

plt.plot(values_x, values_y)
plt.xlabel(dates[0][0])
plt.ylabel(dates[0][1])
plt.title("Titulo")
plt.grid()

plt.show()
