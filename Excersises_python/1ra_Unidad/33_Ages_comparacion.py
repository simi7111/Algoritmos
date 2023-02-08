#Este programa compara dos edades
import os
os.system("cls")
age1=int(input("Dame la primera edad: "))
age2=int(input("Dame la segunda edad: "))
if age2>age1:
    dif=age2-age1
    print(age2,"es mayor que",age1,"por",dif,"años.")
elif age1>age2:
    dif=age1-age2
    print(age1,"es mayor que",age2,"por",dif,"años.")
