#Este programa evalua si una contrseña ingresada por el usuario es correctas o no
import os
os.system("cls")
key_c='key'
key=input("Introduce la contraseña: ")
if key_c==key:
    print("Contraseña correcta, acceso permitido")
else:
    print("Contraseña incorrecta, acceso denegado")