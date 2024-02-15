#Vamos a crea un script que reciba como input un número de tarjeta de crédito e imprima por pantalla todos
#los caracteres en forma de asterisco salvo los últimos cuatro.

# solicitamos el numero de su tarjeta
digitos_tarjeta= input("introduzca los numero de su tarjerta: \n")

#ocultamos los primeros digitos con (*) y dejamos los ultimos 4
ocultar = "*" * (len(digitos_tarjeta) -4) + digitos_tarjeta[-4:]#según la longitud de la tarjeta se restaran 4 y se colocarán
#(*) dejando solo los ultimos 4 digitos
#Mostramos el resultado de ocultar los digitos
print(f"Hemos ocultado los primeros digitos de su tarjeta el resultado es: \n {ocultar}")
