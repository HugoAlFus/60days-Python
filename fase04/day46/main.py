import pandas as pd

dates = [
    {"Nombre": "Ana", "Departamento": "Ventas", "Edad": 28, "Salario": 35000},
    {"Nombre": "Luis", "Departamento": "Marketing", "Edad": 34, "Salario": 42000},
    {"Nombre": "Carlos", "Departamento": "Ventas", "Edad": 25, "Salario": 30000},
    {"Nombre": "Laura", "Departamento": "IT", "Edad": 30, "Salario": 50000},
    {"Nombre": "Marta", "Departamento": "Marketing", "Edad": 29, "Salario": 39000},
    {"Nombre": "Pedro", "Departamento": "IT", "Edad": 40, "Salario": 52000},
    {"Nombre": "Sara", "Departamento": "Ventas", "Edad": 35, "Salario": 41000},
    {"Nombre": "Diego", "Departamento": "Marketing", "Edad": 31, "Salario": 43000},
]

df = pd.DataFrame(dates)

print(f"Datos actuales:\n{df}")
print("------------------------------------------")

older_30 = df[df["Edad"] > 30]
print(f"Empleados que son mayores que de 30 años:\n{older_30}")
print("------------------------------------------")

it_employee = df[df["Departamento"] == "IT"]
print(f"Empleados del departamento de IT\n{it_employee}")
print("------------------------------------------")

avg_salary = round(df.groupby("Departamento")["Salario"].mean(), 2)
print(f"Salario promedio por departamento:\n{avg_salary}")
print("------------------------------------------")

max_age_department = df.groupby("Departamento")["Edad"].max()
print(f"La edad máxima de cada departamento es:\n{max_age_department}")
print("------------------------------------------")

df["Impuestos"] = df["Salario"] * 0.3
df["Salario Neto"] = df["Salario"] - df["Impuestos"]
print(f"Tablas de impuestos (30% del salario) y salario neto (Salario - Impuestos) han sifo agregadas:\n{df}")
print("------------------------------------------")

print(f"Estadisticas generales:\n{df.describe()}")