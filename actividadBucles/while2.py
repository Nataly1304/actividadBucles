""""
Sumar pares desde 0 hasta el número que indique el usuario.
"""
num = int(input("digite un número: "))

sumaPares = 0
contador = 0

while contador <= num:
    if contador % 2 == 0:
        sumaPares += contador
    contador += 1

print(f"La suma de los números pares desde 0 hasta {num} es: {sumaPares}")