print("Calculadora de calificación final de Algoritmos")

p1 = float(input("Calificación parcial 1: "))
p2 = float(input("Calificación parcial 2: "))
p3 = float(input("Calificación parcial 3: "))
examen = float(input("Calificación examen final: "))
trabajo = float(input("Calificación trabajo final: "))

promedio_parciales = (p1 + p2 + p3) / 3
calificacion_final = (promedio_parciales * 0.55) + (examen * 0.30) + (trabajo * 0.15)

print("Calificación final:", calificacion_final)
