def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

try:
    numero = int(input("Ingrese un número para calcular su factorial: "))

    if numero < 0:
        print("Error: Por favor, ingrese un número entero no negativo.")
    else:
        factorial_numero = calcular_factorial(numero)
        print("El factorial de", numero, "es:", factorial_numero)
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
