print("Este programa pide números hasta introducir un 0.")
print("Al finalizar, mostrará la suma y la media de los números.")

suma = 0
contador = 0

numero = int(input("Introduce un número: "))

while numero != 0:
    suma = suma + numero
    contador = contador + 1

    numero = int(input("Introduce otro número: "))

if contador > 0:
    media = suma / contador

    print("La suma es:", suma)
    print("La media es:", media)
else:
    print("No has introducido ningún número")

