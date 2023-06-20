"""""
Sumar pares desde 0 hasta el número que indique el usuario
"""""
numero = int(input("Ingrese un número: "))

sumaPares = 0
for i in range(0, numero + 1, 2):
    sumaPares += i

print(f"La suma de los números pares desde 0 hasta:{numero} es:{sumaPares}")