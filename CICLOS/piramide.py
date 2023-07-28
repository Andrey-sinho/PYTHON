def mostrar_piramide_con_numeros(num_filas):
    numero = 1
    for i in range(1, num_filas + 1):
        for j in range(1, num_filas - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(numero, end=" ")
            numero += 1
        print()

try:
    num_filas_piramide = int(input("Ingrese el número de filas de la pirámide: "))

    if num_filas_piramide <= 0:
        print("Error: Por favor, ingrese un número entero positivo.")
    else:
        mostrar_piramide_con_numeros(num_filas_piramide)
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
