print(f'introduce una cadena de texto')
cadena = input("Cadena: ")
while True:
    caracter = input("Carácter: ")
    if len(caracter) == 1:
        break

contador = 0
for c in cadena:
    if c == caracter:
        contador += 1

print(f"Aparece {contador} veces")

