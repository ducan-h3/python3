print("Calculadora de sueldo y comisiones")

sueldo = float(input("Sueldo base: "))
venta1 = float(input("Venta 1: "))
venta2 = float(input("Venta 2: "))
venta3 = float(input("Venta 3: "))

comision = (venta1 + venta2 + venta3) * 0.10
total = sueldo + comision

print("Comisión:", comision)
print("Sueldo total:", total)
