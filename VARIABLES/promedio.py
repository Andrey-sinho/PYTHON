def calcular_promedio(numeros):
    total_numeros = len(numeros)
    suma_numeros = sum(numeros)
    promedio = suma_numeros / total_numeros
    return promedio

try:
    numeros = []
    for i in range(5):
        numero = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(numero)

    promedio_numeros = calcular_promedio(numeros)
    print("El promedio de los números ingresados es:", promedio_numeros)
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos.")
