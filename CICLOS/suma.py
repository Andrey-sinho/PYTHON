def calcular_suma_primeros_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = 20
suma_total = calcular_suma_primeros_naturales(n)

if suma_total == 210:
    print("El total es 210, la suma de los primeros", n, "números naturales.")
else:
    print("El total no es 210. La suma de los primeros", n, "números naturales es:", suma_total)
