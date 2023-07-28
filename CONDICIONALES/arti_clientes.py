def calcular_total_a_pagar(cantidad, precio_unitario):
    if cantidad <= 5:
        total_a_pagar = cantidad * precio_unitario
    elif cantidad < 10:
        descuento = 0.05  # 5% de descuento
        total_a_pagar = cantidad * precio_unitario * (1 - descuento)
    else:
        descuento = 0.08  # 8% de descuento
        total_a_pagar = cantidad * precio_unitario * (1 - descuento)
    return total_a_pagar

try:
    cantidad_articulos = int(input("Ingrese la cantidad de artículos comprados: "))
    precio_unitario_original = float(input("Ingrese el precio unitario original: "))

    if cantidad_articulos < 0 or precio_unitario_original < 0:
        print("Error: Por favor, ingrese valores no negativos.")
    else:
        total_a_pagar = calcular_total_a_pagar(cantidad_articulos, precio_unitario_original)
        print("El valor total a pagar es:", "$" + str(total_a_pagar))
except ValueError:
    print("Error: Por favor, ingrese valores numéricos válidos.")
