print("Calculadora de descuento del 15%")

total_compra = float(input("Introduce el total de la compra: "))

descuento = total_compra * 0.15
total_final = total_compra - descuento

print("Descuento aplicado:", descuento)
print("Total a pagar:", total_final)
