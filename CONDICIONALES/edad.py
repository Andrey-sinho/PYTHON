def verificar_edad(edad):
    if edad < 0 or edad > 100:
        return False
    return True

try:
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))

    if not verificar_edad(edad):
        print("Error: Por favor, ingresa una edad válida (entre 0 y 100 años).")
    else:
        if edad >= 18:
            print("Hola", nombre + ",", "Usted es mayor de edad.")
        else:
            print("Hola", nombre + ",", "Usted es menor de edad.")
except ValueError:
    print("Error: Por favor, ingresa un número entero válido para la edad.")
