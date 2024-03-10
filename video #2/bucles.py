# 1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una
# estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
# centro de la estructura.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

num=int(input("Introducir un numero mayor a 0: "))# solicitamos un numero
#Creamos un bucle de for
for i in range(0,num+1):
    if i>0:#si i es mayor a 0 
        print("*" * i)
    else:
        print("No es un numero o es menor a 0")
        


    
    