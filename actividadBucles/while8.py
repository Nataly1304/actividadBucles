"""""
Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero
"""

numero = int(input("Ingrese un número entero mayor que cero: "))

while numero <= 0:
    numero = int(input("El número ingresado no es válido. Ingrese un número entero mayor que cero: "))

print("Los divisores del número", numero, "son:")

divisor = 1
while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
    divisor += 1