def mostrar_patron_z(num_filas):
    for i in range(1, num_filas + 1):
        for j in range(1, num_filas + 1):
            if i == 1 or i == num_filas or j == num_filas - i + 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

try:
    num_filas_patron_z = int(input("Ingrese el número de filas del patrón Z: "))

    if num_filas_patron_z <= 0:
        print("Error: Por favor, ingrese un número entero positivo.")
    else:
        mostrar_patron_z(num_filas_patron_z)
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
