def ordenar_ascendente(num1, num2, num3):
    return sorted([num1, num2, num3])

def ordenar_descendente(num1, num2, num3):
    return sorted([num1, num2, num3], reverse=True)

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    numeros_ascendente = ordenar_ascendente(num1, num2, num3)
    numeros_descendente = ordenar_descendente(num1, num2, num3)

    print("Números en orden ascendente:", numeros_ascendente)
    print("Números en orden descendente:", numeros_descendente)
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos.")
