"""
Elabore un algoritmo que permita ingresar n número de temperaturas y escriba la temperatura más alta, la más baja y la temperatura promedio.
"""

n = int(input("Ingrese la cantidad de temperaturas a ingresar: "))

contador = 0
suma_temperaturas = 0
temperatura_maxima = float('-inf')
temperatura_minima = float('inf')

while contador < n:
    temperatura = float(input("Ingrese una temperatura: "))
    suma_temperaturas += temperatura

    if temperatura > temperatura_maxima:
        temperatura_maxima = temperatura

    if temperatura < temperatura_minima:
        temperatura_minima = temperatura

    contador += 1

promedio_temperaturas = suma_temperaturas / n

print("La temperatura más alta es:", temperatura_maxima)
print("La temperatura más baja es:", temperatura_minima)
print("La temperatura promedio es:", promedio_temperaturas)