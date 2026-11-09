notas = []

for iterador in range(0,5):
        nota = int(input("introduce una nota: "))
        if nota >= 0 and nota <= 10:
                notas.append(nota)

print("notas introduidas: ", notas)
media = sum(notas)/len(notas)
print(f"nota media {media}")
print(f"nota minima {min(notas)}")
maximo = -1
for nota in notas:
        if nota > maximo:
                maximo = nota

print(f"nota maxima: {maximo}")
