def calcular_valor_total(valor_unitario, cantidad):
    valor_sin_iva = valor_unitario * cantidad
    iva = valor_sin_iva * 0.16
    valor_total = valor_sin_iva + iva
    return valor_total

try:
    valor_unitario = float(input("Ingresa el valor unitario del producto: "))
    cantidad_comprada = int(input("Ingresa la cantidad de productos comprados: "))

    valor_total_a_pagar = calcular_valor_total(valor_unitario, cantidad_comprada)
    print("El valor total a pagar, incluyendo el IVA, es:", valor_total_a_pagar)
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos.")
