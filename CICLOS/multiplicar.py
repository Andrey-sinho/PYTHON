try:
    numero_entero = int(input("Ingrese un número entero para mostrar su tabla de multiplicar: "))

    print("Tabla de multiplicar del", numero_entero)
    for i in range(1, 11):
        resultado = numero_entero * i
        print(numero_entero, "x", i, "=", resultado)
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
