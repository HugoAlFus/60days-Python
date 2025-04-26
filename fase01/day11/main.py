exchange_rates = {
    "EUR": 1.0,
    "USD": 1.09,
    "GBP": 0.86,
    "JPY": 145.5,
    "MXN": 18.47
}
amount = 0


def convert_current(from_currency, to_currency, amount):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Moneda no soportada")
    rate = amount / exchange_rates[from_currency]
    converted = rate * exchange_rates[to_currency]
    return converted


from_currency = input("Introduzca la moneda desde la que quiere convertir (EUR,USD,GBP,JPY,MXN): ").upper()
to_currency = input("Introduzca la moneda que a la que quiere convertir (EUR,USD,GBP,JPY,MXN): ").upper()

while not isinstance(amount, float):
    try:
        amount = float(input("Introduzca la cantidad de dinero a convertir: "))
    except ValueError:
        print("Por favor introduzca un número")

result = round(convert_current(from_currency, to_currency, amount), 2)

print(f"La conversion de {from_currency} a {to_currency} de la cantidad {amount} es {result}")
