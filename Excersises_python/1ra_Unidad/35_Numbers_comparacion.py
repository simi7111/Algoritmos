#Este programa compara dos numeros
import os
os.system("cls")
num1=int(input("Dame el primer numero "))
num2=int(input("Dame el segundo numero "))
if num2>num1:
    print(num2,"es mayor que",num1)
elif num1>num2:
    print(num1,"es mayor que",num2)
