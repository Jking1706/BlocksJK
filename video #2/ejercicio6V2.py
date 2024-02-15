# BECAS PARA ESTUDIANTES (BONUS*):
# El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.
# Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que
# pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.

#solicitamos los datos requeridos
print("""El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Responde las siguientes preguntas.""")
name=input("introduce tu nombre:\n")
edad= int(input("¿Cuántos años tienes?\n:"))
nota= int(input("¿Cuál es tu promedio?\n:"))

#Creamos una condición para comprobar su edad y sus notas

if (edad>=17)and(edad<=21) and (nota>=8):
    print("Cumples los requisitos para recibir la beca. ¡Felicidades!",name.title())
else:
    print("No cumples los requisitos para recibir la beca. :( \n Otro dia será, buena suerte",name.title())