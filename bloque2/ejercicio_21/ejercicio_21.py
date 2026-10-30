print(f'calculo de factorial')

numero = int(input(f'Introduce un numero; '))
factorial = 1
incremento = 1

while incremento <= numero:
  factorial = factorial * incremento
  incremento += 1


print(f'el factorial es: {factorial}')
