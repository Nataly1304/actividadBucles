"""
Digite un número, si el numero supera a 10, multiplique los 10 primeros números, sino, súmelos
"""
numero = int(input("Ingrese un número: "))
resultado = 1 
if numero > 10:
    contador = 1
    while contador <= 10:
        resultado *= contador
        contador += 1
else:
    contador = 1
    suma = 0
    while contador <= numero:
        suma += contador
        contador += 1

if numero > 10:
    print(f"El resultado de la multiplicación de los 10 primeros números es: {resultado}")
else:
    print(f"La suma de los números del 1 al {numero} es: {suma}")