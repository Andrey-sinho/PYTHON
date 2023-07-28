def calcular_raiz_cuadrada(numero):
    if numero < 0:
        return None 

    
    aproximacion = numero / 2

   
    for _ in range(100):  
        aproximacion = 0.5 * (aproximacion + numero / aproximacion)

    return aproximacion

try:
    numero_ingresado = float(input("Ingresa un número para calcular su raíz cuadrada: "))

    raiz_cuadrada = calcular_raiz_cuadrada(numero_ingresado)
    if raiz_cuadrada is not None:
        print("La raíz cuadrada de", numero_ingresado, "es:", raiz_cuadrada)
    else:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
except ValueError:
    print("Error: Por favor, ingresa un número válido.")
