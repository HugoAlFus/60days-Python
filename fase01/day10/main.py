from datetime import datetime
from dateutil.relativedelta import relativedelta

is_correct = False
birthday_validate = None
while not is_correct:
    birthday_input = input("Por favor indique su fecha de nacimiento con le siguiente formato (dd/mm/yyyy):\n")
    try:
        birthday_validate = datetime.strptime(birthday_input, "%d/%m/%Y")
        is_correct = True
    except ValueError:
        print("Por favor introduzca un valor válido")

today = datetime.now()

age = relativedelta(today, birthday_validate)
days = today.timetuple().tm_yday - birthday_validate.timetuple().tm_yday

print(f"Tienes {age.years} años, {age.months} meses y {days} días.")
