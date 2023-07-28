def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            next_term = fib[-1] + fib[-2]
            fib.append(next_term)
        return fib

def suma_fibonacci(serie_fibonacci):
    return sum(serie_fibonacci)

try:
    n = int(input("Ingrese el número de términos de Fibonacci a mostrar: "))

    serie_fibonacci = fibonacci(n)
    suma = suma_fibonacci(serie_fibonacci)

    print("Los primeros", n, "términos de la serie de Fibonacci son:", serie_fibonacci)
    print("La suma de los primeros", n, "términos de la serie de Fibonacci es:", suma)
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
