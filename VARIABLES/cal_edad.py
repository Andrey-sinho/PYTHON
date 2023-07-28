def calcular_edad(year_nacimiento, year_actual):
    edad = year_actual - year_nacimiento
    return edad

try:
    year_nacimiento = int(input("Ingresa tu año de nacimiento: "))
    year_actual = int(input("Ingresa el año actual: "))

    if year_actual >= year_nacimiento:
        edad_persona = calcular_edad(year_nacimiento, year_actual)
        print("Tu edad es:", edad_persona, "años.")
    else:
        print("Error: El año de nacimiento debe ser anterior al año actual.")
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos para el año de nacimiento y el año actual.")
