# CONTRASEÑA SEGURA:
    
# Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
# especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,

# comprueba si es una contraseña segura e indícarlo por pantalla
contraseña= input("Introduce una contraseña:\n")
#Vamos a solicitar un modulo llamado re
import re
#Creamos una condicion para verificar si tiene vocal en minúscula y los dos símbolos (*,#)
if re.match(r".*[aeiou].*[#*].*[#*].*", contraseña):
    print("Es una contraseña segura")#si se cumple la condición mostrará ese texto
else:
    print("No es una contraseña segura")#si no se mostrará este