def calcular_distancia_recorrida(velocidad, tiempo):
    distancia = velocidad * tiempo
    return distancia

try:
    velocidad_kmph = float(input("Ingresa la velocidad en kilómetros por hora (Km/h): "))
    tiempo_horas = float(input("Ingresa el tiempo en horas: "))

    distancia_recorrida = calcular_distancia_recorrida(velocidad_kmph, tiempo_horas)
    print("La distancia recorrida es:", distancia_recorrida, "kilómetros.")
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos para la velocidad y el tiempo.")
