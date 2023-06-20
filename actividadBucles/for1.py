""""
Suma de los n primeros números, solicite al usuario el numero de elementos a sumar
"""""

n = int(input("digite el número de elementos a sumar: "))

if n <= 0:
    print("El número de elementos debe ser mayor que cero.")
else:
    suma = 0
    for n in range(1, n + 1):
        suma += n

    print(f"La suma de los primeros:{n} números es:{suma}")
    