"""
Elabore un algoritmo que pregunte cuántas temperaturas se van a introducir, pida esas temperaturas, y escriba la temperatura más alta, la más baja y la temperatura promedio.
"""

cantidadTemperaturas = int(input("Ingrese la cantidad de temperaturas: "))
if cantidadTemperaturas <= 0:
    print("La cantidad de temperaturas debe ser mayor que cero.")
else:
    temperaturaMaxima = float('-inf')  
    temperaturaMinima = float('inf')  
    sumaTemperaturas = 0

    for i in range(cantidadTemperaturas):
        temperatura = float(input("Ingrese la temperatura: ".format(i + 1)))

        if temperatura > temperaturaMaxima:
            ttemperaturaMaxima = temperatura

        if temperatura < temperaturaMinima:
            ttemperaturaMinima = temperatura

        sumaTemperaturas += temperatura

    ttemperaturaPromedio = sumaTemperaturas / cantidadTemperaturas

    print(f"Temperatura máxima:  {temperaturaMaxima}")
    print(f"Temperatura mínima:  {temperaturaMinima}")
    print(f"Temperatura promedio: {sumaTemperaturas}")