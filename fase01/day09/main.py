import time

input("Presione ENTER para iniciar el cronómetro")
start = time.time()

print("--------------------------------------------")

input("Presione ENTER para finalizar el cronómetro")
finish = time.time()

print(f"Tiempo transcurrido {round(finish - start, 2)} segundos")
