
       #Reordenando Numeros
       
       
numero = input("Introduce un numero de mas de una cifra \n")#solicitamos un numero de más de una cifra
for cifra in numero:#la variable cifra irá tomando el valor de cada numero de la cifra introducida (bucle for)
    # se mostrara cada numero en pantalla
 print(cifra)
 
 #solicitamos un numero de minimo 4 cifras y lo convertimos en un entero
number1= int(input("Introduce un numero de miinimo 4 cifras\n"))
numberInvers=int(str(number1)[::-1])#convertimos el numero introducido en una cadena luego
#tomamos toda esa cadena con [::-1] iniciamos desde el ultimo numero al terminar lo convierte en un entero nuevamente
# y lo mostramos en pantalla
print(f"a continuación se escribirán el numero ingresado pero inverso: {numberInvers}")
