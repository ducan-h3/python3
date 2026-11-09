meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

numero = int(input("Dime el número (entre 1 y 12) del mes: "))

print(f"El mes introducido ({numero}) es {meses[numero - 1]} con {dias[numero - 1]} días")
