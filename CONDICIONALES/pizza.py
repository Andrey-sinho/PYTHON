def calcular_precio_pizza(tamano, num_ingredientes):
    precios = {1: 15000, 2: 24000, 3: 36000}
    precio_base = precios.get(tamano, "Tamaño no válido")

    if precio_base != "Tamaño no válido":
        precio_total = precio_base + (num_ingredientes * 4000)
        return precio_total
    else:
        return "Tamaño no válido"

try:
    print("Tamaños de pizza disponibles:")
    print("1 - Pequeña")
    print("2 - Mediana")
    print("3 - Grande")

    tamano_pizza = int(input("Ingrese el número correspondiente al tamaño de la pizza: "))
    num_ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales: "))

    precio = calcular_precio_pizza(tamano_pizza, num_ingredientes_adicionales)
    if precio != "Tamaño no válido":
        print("El precio total a pagar es:", "$" + str(precio))
    else:
        print("Error: Tamaño de pizza no válido. Por favor, elija un número válido de la lista.")
except ValueError:
    print("Error: Por favor, ingrese números enteros válidos.")
