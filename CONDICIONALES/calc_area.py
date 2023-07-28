import math

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) * altura) / 2

def menu():
    print("Menú de opciones:")
    print("1. Calcular área de un cuadrado")
    print("2. Calcular área de un rectángulo")
    print("3. Calcular área de un triángulo")
    print("4. Calcular área de un círculo")
    print("5. Calcular área de un rombo")
    print("6. Calcular área de un trapecio")
    print("7. Salir")

while True:
    menu()
    opcion = input("Ingresa el número de la opción que deseas calcular: ")

    if opcion == "1":
        lado_cuadrado = float(input("Ingresa la longitud del lado del cuadrado: "))
        area = calcular_area_cuadrado(lado_cuadrado)
        print("El área del cuadrado es:", area)
    elif opcion == "2":
        base_rectangulo = float(input("Ingresa la base del rectángulo: "))
        altura_rectangulo = float(input("Ingresa la altura del rectángulo: "))
        area = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
        print("El área del rectángulo es:", area)
    elif opcion == "3":
        base_triangulo = float(input("Ingresa la base del triángulo: "))
        altura_triangulo = float(input("Ingresa la altura del triángulo: "))
        area = calcular_area_triangulo(base_triangulo, altura_triangulo)
        print("El área del triángulo es:", area)
    elif opcion == "4":
        radio_circulo = float(input("Ingresa el radio del círculo: "))
        area = calcular_area_circulo(radio_circulo)
        print("El área del círculo es:", area)
    elif opcion == "5":
        diagonal_mayor_rombo = float(input("Ingresa la diagonal mayor del rombo: "))
        diagonal_menor_rombo = float(input("Ingresa la diagonal menor del rombo: "))
        area = calcular_area_rombo(diagonal_mayor_rombo, diagonal_menor_rombo)
        print("El área del rombo es:", area)
    elif opcion == "6":
        base_mayor_trapecio = float(input("Ingresa la base mayor del trapecio: "))
        base_menor_trapecio = float(input("Ingresa la base menor del trapecio: "))
        altura_trapecio = float(input("Ingresa la altura del trapecio: "))
        area = calcular_area_trapecio(base_mayor_trapecio, base_menor_trapecio, altura_trapecio)
        print("El área del trapecio es:", area)
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, ingresa un número del 1 al 7.")
