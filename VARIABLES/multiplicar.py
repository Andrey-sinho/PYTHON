def multiplicar_numeros():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    resultado = num1 * num2 * num3
    return resultado

resultado_multiplicacion = multiplicar_numeros()
print("El resultado de la multiplicación es:", resultado_multiplicacion)
