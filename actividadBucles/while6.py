"""
Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio
"""
n = int(input("escriba la cantidad de notas a capturar: "))

suma_notas = 0
contador = 0

while contador < n:
    nota = float(input("Ingrese la nota: "))
    suma_notas += nota
    contador += 1

promedio = suma_notas / n

print(f"El promedio de las {n}notas es: {promedio}")