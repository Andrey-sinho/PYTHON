def calcular_promedio(notas):
    return sum(notas) / len(notas)

try:
    notas_estudiante = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1} (de 0.0 a 5.0): "))
        if nota < 0.0 or nota > 5.0:
            print("Error: Por favor, ingresa una nota válida (entre 0.0 y 5.0).")
            exit()

        notas_estudiante.append(nota)

    promedio = calcular_promedio(notas_estudiante)

    if promedio >= 3.0:
        print("Aprobó. Su promedio es:", promedio)
    else:
        print("No aprobó. Su promedio es:", promedio)
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos para las notas.")
