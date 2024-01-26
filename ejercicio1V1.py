text1 = ("estas usando python")#La variable text1 almacena un texto

name = input("¿Cual es tu nombre?")#aquí preguntamos y almacenamos lo que escriban en la variable (name)

print("Hola, " + name + ", " + text1)#mostramos en pantalla un texto más el nombre introducido más otro texto
print("Hola, ".upper() + name.upper() + ", " + text1.upper())#hacemos lo mismo pero con todo en mayusculas (upper)
print("Hola, ".lower() + name.lower() + ", " + text1.lower())#hacemos lo mismo pero con minusculas (lower)
print("Hola, " + name.title()+ ", " + text1)#aquí lo dejamos normal solo cambiamos la letra inicial del (name)
print("Hola, " + (name.replace("."," ")) + ", " + text1)#aquí remplazamos un (.) por un espacio
