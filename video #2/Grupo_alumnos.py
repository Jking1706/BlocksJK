# GRUPOS DE ALUMNOS:
# En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos
# lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la
# M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y
# R hasta la Z se les ha asignado al grupo A también, el resto están en el B.
# Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por
# pantalla el grupo que le corresponde a ese alumno.

import re#Importamos un modulo llamado re

#Solicitamos el nombre y su genero
sexo=input("¿Eres Chico | Chica ?:\n")
sexo=sexo.lower()
Name=input("¿Cuál es tu nombre?:\n").capitalize()#capitalize borra y escribe nuevamente el contenido con la primera letra en mayuscula
#creamos el condicional
if sexo=="chico":
    if re.match(r"[A-HR-Z]", Name):#re.match ayuda a buscar desde la primera letra de cada string
        print("Eres del Grupo 'A' ")
    else:
        print("Estas en el grupo 'B' ")
if sexo=="chica":
    if re.match(r"[E-M]",Name):
        print("Eres del Grupo 'A' ")
    else:
        print("Estas en el grupo 'B' ")
        