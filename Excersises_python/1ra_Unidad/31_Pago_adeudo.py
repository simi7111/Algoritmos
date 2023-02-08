#Este programa verifica si se pago un adeudo
import os
os.system("cls")
print("Tu adeudo es de $500 pesos")
pago=input("¿Cuanto deseas pagar?")
if '.' in pago:
        pago=float(pago)
else:
        pago=int(pago)

if pago==500 or pago ==500.0:
    print("El pago quedo liquidado")
elif pago>500:
    sobra=pago-500
    print("Tu pago quedo liquidado, tu cambio es de ",sobra)
else:
    falta=500-pago
    print("No es suficiente para liquidar, faltan",falta,"para liquidar")