# LOG-IN:
# Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
# Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
# indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
# contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
# Cambia el script para que no distinga entre mayúsculas y minúsculas.
# (Pista: Necesitarás in If Statement anidado)

#solicitamos usuario y contraseña
name= input("Hola, Introduce tu nombre de usuario:\n")
contraseña= input("Hola, Introduce tu contraseña:\n")
contraseña_almacenada= "Blocks1"

#Creamos una condicion anidada
if contraseña== contraseña_almacenada:
    print("Bienvenido "+name.title())
    #si no se cumple dirá que intente otra vez
else:
    contraseña= input("Error, la contraseña es incorrecta, intenta otra vez:\n")
    #si esta vez es correcta dirá bienvenido
    if contraseña== contraseña_almacenada:
     print("Bienvenido "+name.title())
     #si no, no hay más intentos
    else:
        print("Error. Contraseña incorrecta, no hay más intento. intenta otro día")
