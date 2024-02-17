# RELACION ENTRE NÚMEROS:
# Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
# de los otros dos. 

#solicitamos los numeros
numero=int(input("Intoducir el primer numero:\n"))
numero_1=int(input("Intoducir el segundo numero:\n"))
numero_2=int(input("Intoducir el tercero numero:\n"))


#creamos una condicion que ira sumando los numeros anteriores y comparando
if numero== numero_1+numero_2:
    print("el numero",numero,"es la suma de los otros dos numeros introducidos")
elif numero_1 == numero + numero_2:
    print("el numero",numero_1,"es la suma de los otros dos numeros introducidos")
elif numero_2==numero+numero_1:
    print("el numero",numero_2,"es la suma de los otros dos numeros introducidos")
else:
    print("Ninguno de los numeros anteriores es la suma entre ellos")
    