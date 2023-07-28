def calcular_cuadrado(numero):
    return numero ** 2

try:
    numero_ingresado = float(input("Ingresa un número: "))
    resultado_cuadrado = calcular_cuadrado(numero_ingresado)
    print("El cuadrado de", numero_ingresado, "es:", resultado_cuadrado)
except ValueError:
    print("Error: Por favor, ingresa un número válido.")
