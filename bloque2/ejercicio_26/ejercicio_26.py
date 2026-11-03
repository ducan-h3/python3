print("Números pares entre dos números")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

for numero in range(num1, num2 + 1, 2):
    print(numero)
