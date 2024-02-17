# MAYUSCULA O MINUSCULA (BONUS*):
# Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es
# una mayúscula o una minúscula.

#solicitamos la letra
letra= input("introduce una letra:\n")

#Creamos una condicion y verificamos si es mayuscula o minúscula
if letra.islower():
    print("La letra:",letra,"es Minúscula")
elif letra.isupper():
     print("La letra:",letra,"es Mayuscula")