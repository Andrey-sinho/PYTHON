def calcular_pulsaciones(edad, genero):
    if genero == 1:  # Género femenino
        pulsaciones = (220 - edad) / 10
    elif genero == 2:  # Género masculino
        pulsaciones = (210 - edad) / 10
    else:
        pulsaciones = None
    return pulsaciones

try:
    edad = int(input("Ingrese su edad: "))
    genero = int(input("Ingrese su género (1 para femenino, 2 para masculino): "))

    if edad <= 0 or (genero != 1 and genero != 2):
        print("Error: Por favor, ingrese una edad válida y elija un género válido.")
    else:
        pulsaciones_por_10_segundos = calcular_pulsaciones(edad, genero)
        if pulsaciones_por_10_segundos is not None:
            print("El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es:", pulsaciones_por_10_segundos)
        else:
            print("Error: Género no válido. Por favor, elija 1 para femenino o 2 para masculino.")
except ValueError:
    print("Error: Por favor, ingrese valores numéricos enteros válidos para la edad y el género.")
