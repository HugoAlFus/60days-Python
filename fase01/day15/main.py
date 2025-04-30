number_choose = input("Indique que número que quiera multiplicar: ")

print(f"--Tabla de multiplicar del número {number_choose}")
for i in range(11):
    result = int(i) * float(number_choose)
    print(f"{number_choose} x {i} = {round(result, 2)}")
