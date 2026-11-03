print("Comprobar si es vocal")

letra = input("Introduce una letra: ")

while letra != " ":

    if letra in "aeiou":
        print("VOCAL")
    else:
        print("NO VOCAL")

    letra = input("Introduce otra letra: ")

print("Fin")
