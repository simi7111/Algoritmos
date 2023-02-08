#Este programa pide datos al usuario (calle, nombre, numero, colonia) y los concatena
import os
os.system("cls")
name=input("¿Cual es tu nombre ?")
lastname=input("¿Cual es tu apellido? ")
street=input("¿En que calle vives?")
h_number=input("¿Cual es tu numero de casa?")
colonia=input("¿Cual es tu colonia?")
print(name,lastname,"vive en el",h_number,"de la calle",street,"colonia",colonia)