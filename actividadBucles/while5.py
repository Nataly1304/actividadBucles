""""
Crear un programa que permita al usuario ingresar los valores totales de n facturas (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
"""""

totalVentas = 0
montoFactura = float(input("Ingrese el monto de la factura (0 para finalizar): "))

while montoFactura != 0:
    totalVentas += montoFactura
    montoFactura = float(input("Ingrese el monto de la factura (0 para finalizar): "))

if totalVentas > 1000:
    descuento = totalVentas * 0.1
    totalPagar = totalVentas - descuento
else:
    descuento = 0
    totalPagar = totalVentas

print(f"Total de ventas: {totalVentas}")
print(f"Descuento aplicado: {descuento}")
print(f"Total a pagar: {totalPagar}")