print("Tabla de multiplicar")

numero = int(input("Introduce un número: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
