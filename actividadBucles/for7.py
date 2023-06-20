""""
Algoritmo que pregunte al usuario que tabla de multiplicar quiere ver, debe generar la tabla de multiplicar desde cero hasta 10.
"""
tablaMulti = int(input("Ingrese la tabla de multiplicar que desea ver: "))

print("Tabla de multiplicar del", tablaMulti, ":")

for i in range(11):
    resultado = tablaMulti * i
    print(tablaMulti, "x", i, "=", resultado)