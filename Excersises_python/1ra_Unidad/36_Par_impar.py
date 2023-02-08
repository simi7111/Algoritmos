#Este programa determina si un numero es par o impar
import os
os.system('cls')
number=input("Dame un numero: ")
if '.' in number:
    number=float(number)
    if number & 1 == 0:
            print("El número es par")
    else:
            print("El número es impar")
elif '.' not in number:
    number=int(number)
    if number & 1 == 0:
        print("El número es par")
    else:
        print("El número es impar")



if number & 1 == 0:
    print("El número es par")
else:
    print("El número es impar")


    

