nombre = input("Introduce nombre y apellidos: ")

iniciales = ""
es_inicial = True

for c in nombre:
    if es_inicial and c != " ":
        iniciales += c
        es_inicial = False
    elif c == " ":
        es_inicial = True

print(f"Las iniciales son: {iniciales}")
