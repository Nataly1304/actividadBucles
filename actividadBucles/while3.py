""""
Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay
"""
n = int(input("digite un número: "))

sumaImpares = 0
contador = 1
cantidadImpares = 0

while contador <= n:
    if contador % 2 != 0:
        sumaImpares += contador
        cantidadImpares += 1
    contador += 1

print(f"La suma de los números impares desde 1 hasta {n} es: {sumaImpares}")
print(f"Cantidad de números impares: {cantidadImpares}")