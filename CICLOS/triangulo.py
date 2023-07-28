def mostrar_triangulo(num_filas):
    for i in range(1, num_filas + 1):
        print(" " * (num_filas - i) + "*" * (2 * i - 1))

try:
    num_filas_triangulo = int(input("Ingrese el número de filas del triángulo: "))

    if num_filas_triangulo <= 0:
        print("Error: Por favor, ingrese un número entero positivo.")
    else:
        mostrar_triangulo(num_filas_triangulo)
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
