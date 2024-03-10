# 3. Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
# de la palabra introducida empezando por la última. 

#solicitamos la palabra
palabra= input("Introduce una palabra: ")
reverse= ""
#creamos un bucle de for
for i in range(len(palabra)-1,-1,-1):#con el -1 inicia desde el final, con paso de -1
    reverse+= palabra[i]
    if len(reverse)==len(palabra):#creamos una condición para mostrar solo el nombre al revés
     print(reverse)