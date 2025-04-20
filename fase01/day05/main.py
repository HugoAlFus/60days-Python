text = input("Introduzca el texto que quiere contar sus palabras:\n")
list_words = text.split()
count = len(list_words)
print(f"El texto que introduciste tiene un total de {count} palabras")
