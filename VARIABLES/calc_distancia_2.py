def transformar_distancia(distancia_metros):
    distancia_kilometros = distancia_metros / 1000
    distancia_centimetros = distancia_metros * 100
    distancia_milimetros = distancia_metros * 1000
    return distancia_kilometros, distancia_centimetros, distancia_milimetros

try:
    distancia_metros = float(input("Ingresa la distancia en metros: "))

    if distancia_metros < 0:
        print("Error: Por favor, ingresa una distancia no negativa.")
    else:
        distancia_kilometros, distancia_centimetros, distancia_milimetros = transformar_distancia(distancia_metros)
        print("La distancia en kilómetros es:", distancia_kilometros, "km.")
        print("La distancia en centímetros es:", distancia_centimetros, "cm.")
        print("La distancia en milímetros es:", distancia_milimetros, "mm.")
except ValueError:
    print("Error: Por favor, ingresa un número válido para la distancia.")
