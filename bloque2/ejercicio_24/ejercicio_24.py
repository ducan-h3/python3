print("Este programa cuenta cuántos números son mayores, menores o iguales a 0")

cantidad = int(input("¿Cuántos números vas a introducir? "))

mayores = 0
menores = 0
iguales = 0

for i in range(cantidad):
    numero = float(input("Introduce un número: "))

    if numero > 0:
        mayores = mayores + 1
    elif numero < 0:
        menores = menores + 1
    else:
        iguales = iguales + 1

print("Números mayores que 0:", mayores)
print("Números menores que 0:", menores)
print("Números iguales a 0:", iguales)
