def calcular_porcentaje(numero, porcentaje):
    return numero * (porcentaje / 100)

try:
    numero_ingresado = float(input("Ingresa un número: "))
    porcentaje_a_calcular = 20

    resultado_porcentaje = calcular_porcentaje(numero_ingresado, porcentaje_a_calcular)
    print("El 20% de", numero_ingresado, "es:", resultado_porcentaje)
except ValueError:
    print("Error: Por favor, ingresa un número válido.")
