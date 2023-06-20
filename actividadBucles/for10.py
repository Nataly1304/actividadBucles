"""
Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero
"""

numero = int(input("Ingrese un número entero mayor que cero: "))
if numero <= 0:
    print("El número debe ser mayor que cero.")
else:
    print(f"Los divisores de : {numero} son:")
    for n in range(1, numero + 1):
        if numero % n == 0:
            print(n)