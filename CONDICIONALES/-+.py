def determinar_signo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"

try:
    numero_ingresado = float(input("Ingresa un número: "))

    resultado = determinar_signo(numero_ingresado)
    print("El número es:", resultado)
except ValueError:
    print("Error: Por favor, ingresa un número válido.")
