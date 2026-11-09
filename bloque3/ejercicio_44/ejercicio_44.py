cadena = input("Introduce una frase:  ")

contador = 0
if len(cadena) > 0:
    contador = 1
    for c in cadena:
        if c == " ":
            contador += 1

print(f"La frase tiene {contador} palabras.")
