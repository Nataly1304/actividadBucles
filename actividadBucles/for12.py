""""
Elaborar un algoritmo que pida las 4 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio
"""

n = int(input("Ingrese la cantidad de estudiantes: "))
if n <= 0:
    print("La cantidad de estudiantes debe ser mayor que cero.")
else:
    notas_mas_altas = []
    notas_mas_bajas = []
    suma_notas = 0

    for i in range(n):
        print("Ingrese las 4 notas del estudiante", i + 1)
        notas = []

        for j in range(4):
            nota = float(input("Ingrese la nota {}: ".format(j + 1)))
            notas.append(nota)

        nota_maxima = max(notas)
        nota_minima = min(notas)

        notas_mas_altas.append(nota_maxima)
        notas_mas_bajas.append(nota_minima)
        suma_notas += sum(notas)

    nota_maxima_global = max(notas_mas_altas)
    nota_minima_global = min(notas_mas_bajas)
    promedio = suma_notas / (n * 4)

    print(f"La nota más alta es: {nota_maxima_global}")
    print(f"La nota más baja es: {nota_minima_global}")
    print(f"El promedio de las notas es: {promedio}")