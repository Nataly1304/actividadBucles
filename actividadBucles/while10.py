"""""
10.	Elaborar un algoritmo que pida las 3 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.
"""""

n = int(input("Ingrese la cantidad de estudiantes: "))

contador_estudiantes = 0

while contador_estudiantes < n:
    print("Estudiante", contador_estudiantes + 1)
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))

    nota_maxima = max(nota1, nota2, nota3)
    nota_minima = min(nota1, nota2, nota3)
    promedio = (nota1 + nota2 + nota3) / 3

    print("Nota más alta:", nota_maxima)
    print("Nota más baja:", nota_minima)
    print("Promedio:", promedio)
    print()

    contador_estudiantes += 1