"""
Leer números enteros del teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
"""

suma = 0
numero = int(input("Ingrese un número entero (0 para finalizar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número entero (0 para finalizar): "))

print("La sumatoria de los números ingresados es:", suma)