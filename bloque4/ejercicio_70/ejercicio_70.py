cadena = input("Escribe una cadena de texto: ")
apariciones = {}

for caracter in cadena:
    if caracter in apariciones:
        apariciones[caracter] += 1
    else:
        apariciones[caracter] = 1

for clave, valor in apariciones.items():
    print(f"'{clave}' -> {valor}")
