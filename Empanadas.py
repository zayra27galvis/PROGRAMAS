print("EMPANADAS")
print(" ")
preparadas = int(input("Cantidad de empanadas preparadas: "))
vendidas = int(input("Cantidad de empanadas vendidas: "))
precio = float(input("Precio de cada empanada: "))
perdidas = preparadas - vendidas
valorPerdidas = perdidas * precio
print(" ")
print("REGISTRO DEL DIA")
print("Empanadas preparadas:", preparadas)
print("Empanadas vendidas:", vendidas)
print("Empanadas perdidas:",preparadas - vendidas)
print("Ganancias", vendidas * precio)
print("Valor de las perdidas: $", valorPerdidas)