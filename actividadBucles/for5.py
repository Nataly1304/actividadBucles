"""
Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay
"""

n = int(input("Ingrese un número: "))

sumaImpares = 0
contadorImpares = 0

for i in range(1, n + 1, 2):
    sumaImpares += i
    contadorImpares += 1

print(f"La suma de los números impares desde 1 hasta: {n }es: {sumaImpares}")
print(f"La cantidad de números impares desde 1 hasta: {n} es: {contadorImpares}")