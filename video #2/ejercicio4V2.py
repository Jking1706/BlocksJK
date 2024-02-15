# DIVISION:
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
# divisor es cero el programa debe mostrar un error.

#solicitamos el primer numero
numero= int(input("introducir un numero:\n"))
#solicitamos el segundo numero
numero1= int(input("introducir otro numero:\n"))
#creamos una condición para comprobar si el segundo numero es mayor a 0
if numero1 > 0: 
    division= numero / numero1
    print(f"Su resultado es: {division}")
else:
     numero1 == 0
     print("Error, no puedo dividir por cero")
