#Este programa compara un numero y verfica si es mayor o menor a 0
import os 
os.system("cls")
number=input("Dame un numero: ")
if '.' in number:
    number=float(number)
    if type(number) == float :
        if number>0:
            print("El numero",number,"mayor a 0")
        elif number==0:
            print("El numero es 0")
        else:
            print("El numero",number,"menor a 0")
else:
    number=int(number)
    if type(number) == int :
        if number>0:
            print("El numero",number,"es mayor a 0")
        elif number==0:
            print("El numero es 0")
        else:
            print("El numero",number,"menor a 0")
