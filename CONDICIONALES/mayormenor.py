def encontrar_mayor_menor(num1, num2):
    if num1 > num2:
        return num1, num2
    else:
        return num2, num1

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    mayor, menor = encontrar_mayor_menor(num1, num2)
    print("El número mayor es:", mayor)
    print("El número menor es:", menor)
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos.")
