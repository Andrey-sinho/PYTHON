def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def determinar_estado_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

try:
    peso_kg = float(input("Ingrese su peso en Kg: "))
    estatura_metros = float(input("Ingrese su estatura en metros: "))

    if peso_kg <= 0 or estatura_metros <= 0:
        print("Error: Por favor, ingrese valores positivos para peso y estatura.")
    else:
        imc = calcular_imc(peso_kg, estatura_metros)
        estado_imc = determinar_estado_imc(imc)

        print("Su IMC es:", imc)
        print("Estado de su IMC:", estado_imc)
except ValueError:
    print("Error: Por favor, ingrese valores numéricos válidos para peso y estatura.")
