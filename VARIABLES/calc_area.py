def calcular_area_cuadrado(lado):
    return lado ** 2

try:
    lado_cuadrado = float(input("Ingresa la longitud de un lado del cuadrado: "))

    area_cuadrado = calcular_area_cuadrado(lado_cuadrado)
    print("El área del cuadrado es:", area_cuadrado)
except ValueError:
    print("Error: Por favor, ingresa un número válido para la longitud del lado.")
