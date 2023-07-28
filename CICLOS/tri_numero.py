def mostrar_triangulo_rectangulo(num_filas):
    for i in range(1, num_filas + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

try:
    num_filas_triangulo = int(input("Ingrese el número de filas del triángulo: "))

    if num_filas_triangulo <= 0:
        print("Error: Por favor, ingrese un número entero positivo.")
    else:
        mostrar_triangulo_rectangulo(num_filas_triangulo)
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
