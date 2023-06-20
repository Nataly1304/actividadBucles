"""
Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo
"""
primer_numero = int(input("digite el primer número: "))
segundo_numero = int(input("digite el segundo número: "))
while primer_numero >= segundo_numero:
    print("Error: el primer número debe ser menor que el segundo.")
    primer_numero = int(input("Ingrese el primer número: "))
    segundo_numero = int(input("Ingrese el segundo número: "))
numero_actual = primer_numero
while numero_actual <= segundo_numero:
    print(numero_actual)
    numero_actual += 1