"""
Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio
"""
n = int(input("Ingrese la cantidad de notas: "))
if n <= 0:
    print("La cantidad de notas debe ser mayor que cero.")
else:
    sumaNotas = 0
    for i in range(n):
        nota = float(input("Ingrese la nota: ".format(i + 1)))
        sumaNotas += nota

    promedio = sumaNotas / n
    print(f"El promedio de las notas es: {promedio}")