import random

print(f'Juego de adivinar un numero')
secreto = random.randint(1, 100)

for i in range(1, 11):
  print(f"Intentos restantes: {11 - i}")
  num = int(input("Introduce un número (1-100): "))

  if num == secreto:
    print(f"¡Acertaste en {i} intentos!")
    break
  print("Es mayor.\n" if num < secreto else "Es menor.\n")
else:
  print(f"Agotaste los intentos. El número era: {secreto}")

