""""
Digite un número, si el numero supera a 10, multiplique los 10 primeros números, si no, súmelos
"""

num = int(input("Ingrese un número: "))

if num > 10:
    resultado = 1
    for i in range(1, 11):
        resultado *= num
    print(f"El resultado de la multiplicación de los 10 primeros números es: {resultado}")
else:
    resultado = 0
    for i in range(1, 11):
        resultado += num
    print(f"El resultado de la suma de los 10 primeros números es: {resultado}")