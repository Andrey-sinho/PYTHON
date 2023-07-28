def calcular_salario(salario_diario, dias_trabajados):
    salario_bruto = salario_diario * dias_trabajados
    descuento_pension = salario_bruto * 0.10
    descuento_salud = salario_bruto * 0.15
    salario_neto = salario_bruto - descuento_pension - descuento_salud
    return salario_neto

try:
    salario_diario = float(input("Ingresa el salario diario del empleado: "))
    dias_trabajados = int(input("Ingresa el número de días trabajados: "))

    salario_a_pagar = calcular_salario(salario_diario, dias_trabajados)
    print("El salario a pagar al empleado es:", salario_a_pagar)
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos.")
