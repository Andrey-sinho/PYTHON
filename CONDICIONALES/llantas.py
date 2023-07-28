def calcular_valor_compra(num_llantas):
    if num_llantas < 6:
        precio_unitario = 240000
    elif num_llantas <= 7:
        precio_unitario = 221000
    else:
        precio_unitario = 180000

    valor_compra = num_llantas * precio_unitario
    return valor_compra

try:
    num_llantas_compradas = int(input("Ingrese el número de llantas compradas: "))

    if num_llantas_compradas < 0:
        print("Error: Por favor, ingrese un número válido de llantas.")
    else:
        valor_a_pagar = calcular_valor_compra(num_llantas_compradas)
        print("El valor a pagar es:", valor_a_pagar)
except ValueError:
    print("Error: Por favor, ingrese un número entero válido para el número de llantas.")