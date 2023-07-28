def determinar_par_o_impar(numero):
    if numero == 0:
        return "cero"
    elif numero % 2 == 0:
        return "par"
    else:
        return "impar"

try:
    numero_ingresado = int(input("Ingresa un número: "))

    resultado = determinar_par_o_impar(numero_ingresado)
    print("El número es:", resultado)
except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")
