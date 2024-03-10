#  2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 

contraseñaAlmacenada="karma"#contraseña guardada
contraseña=input("Introduce la contraseña: ")#solicitamos una contraseña
#creamos un bucle de while
while contraseña!=contraseñaAlmacenada:# si la contraseña es diferente a la contraseñaAlmacenada 
    #iniciará el bucle
    
    contraseña=input("Introduce la contraseña: ")#volvemos a hacer la pregunta
    #creamos un condicional
    if contraseña== contraseñaAlmacenada:
        print("Bienvenido.")
    if contraseña!= contraseñaAlmacenada:
        print("contraseña incorrecta, intenta otra vez.")
        