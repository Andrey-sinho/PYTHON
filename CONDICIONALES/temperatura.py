def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_a_kelvin(fahrenheit):
    celsius = fahrenheit_a_celsius(fahrenheit)
    kelvin = celsius_a_kelvin(celsius)
    return kelvin

def kelvin_a_fahrenheit(kelvin):
    celsius = kelvin_a_celsius(kelvin)
    fahrenheit = celsius_a_fahrenheit(celsius)
    return fahrenheit

def menu():
    print("Menú de opciones:")
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Convertir de Celsius a Kelvin")
    print("4. Convertir de Kelvin a Celsius")
    print("5. Convertir de Fahrenheit a Kelvin")
    print("6. Convertir de Kelvin a Fahrenheit")
    print("7. Salir")

while True:
    menu()
    opcion = input("Ingresa el número de la opción que deseas realizar: ")

    if opcion == "1":
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print("La temperatura en Fahrenheit es:", fahrenheit, "°F")
    elif opcion == "2":
        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print("La temperatura en Celsius es:", celsius, "°C")
    elif opcion == "3":
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        kelvin = celsius_a_kelvin(celsius)
        print("La temperatura en Kelvin es:", kelvin, "K")
    elif opcion == "4":
        kelvin = float(input("Ingresa la temperatura en Kelvin: "))
        celsius = kelvin_a_celsius(kelvin)
        print("La temperatura en Celsius es:", celsius, "°C")
    elif opcion == "5":
        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
        kelvin = fahrenheit_a_kelvin(fahrenheit)
        print("La temperatura en Kelvin es:", kelvin, "K")
    elif opcion == "6":
        kelvin = float(input("Ingresa la temperatura en Kelvin: "))
        fahrenheit = kelvin_a_fahrenheit(kelvin)
        print("La temperatura en Fahrenheit es:", fahrenheit, "°F")
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, ingresa un número del 1 al 7.")
