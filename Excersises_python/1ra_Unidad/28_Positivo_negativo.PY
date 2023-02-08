#Este programa devuelve si un numero es positivo o negativo
import os 
os.system("cls")
number=input("Dame un numero: ")
if '.' in number:
    number=float(number)
    if type(number) == float :
        if number>0:
            print("El numero",number," es positivo")
        elif number==0:
            print("El numero es 0")
        else:
            print("El numero",number,"es negativo")
else:
    number=int(number)
    if type(number) == int :
        if number>0:
            print("El numero",number," es positivo")
        elif number==0:
            print("El numero es 0")
        else:
            print("El numero",number,"es negativo")
