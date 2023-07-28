def calcular_porcentaje(numero, porcentaje):
    return numero * (porcentaje / 100)

try:
    numero_ingresado = float(input("Ingresa un número: "))

    porcentaje_30 = calcular_porcentaje(numero_ingresado, 30)
    porcentaje_60 = calcular_porcentaje(numero_ingresado, 60)
    porcentaje_90 = calcular_porcentaje(numero_ingresado, 90)

    print("El 30% de", numero_ingresado, "es:", porcentaje_30)
    print("El 60% de", numero_ingresado, "es:", porcentaje_60)
    print("El 90% de", numero_ingresado, "es:", porcentaje_90)

except ValueError:
    print("Error: Por favor, ingresa un número válido.")
