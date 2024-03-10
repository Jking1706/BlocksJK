# LISTAS DE CARACTERES:
# 1. Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas
# de caracteres: manzana, plátano, cereza, pera, higo, frambuesa y fresa.
# 2. Usa la función len() para imprimir la longitud de la lista frutas.
# 3. Accede al objeto numero 3 de la lista e imprímelo or consola.
# 4. Modifica el segundo objeto de la lista y cambiado a mora.
# 5. Añade el string mango al final de la lista.
# 6. Usa el método insert() y añade el string “uva“ año comienzo de la lista.
# 7. Usa un bucle para recorrer la lista e imprimir cada fruta por la consola
# 8. Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable
# llamada “ultima_fruta“.
# 9. Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola
# 10. Modifica el script para que imprima también la longitud de cada nombre de fruta por consola
# 11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que
# tengan más de 5 caracteres
# 12. Usa el método remove() para borrar el string “cereza“ de la lista.
# # 13. Usa el método clear() para vaciar la lista. 



#Creamos una lista
fruta= ["manzana", "platano", "cereza", "pera", "higo", "frambuesa", "fresa"]
print(len(fruta))#numero de frutas en la lista
print(fruta[3])#mostramos la fruta en la posición 3 de la lista
fruta[3]= "mora"#cambiamos "pera" por "mora" en la lista
fruta.append("mango")#agregamos a la lista "mango"
fruta.insert(0,"uva")

#Creamos un bucle for 
for i in range(0,len(fruta)):
    fruta1= fruta[i]
    print(fruta1)
print("-----------------------------")
ultima_fruta= fruta.pop()#ELIMINAMOS LA ULTIMA FRUTA 

#Creamos un bucle for    
for j in fruta:
    print(j)
print("-----------------------------")

#Creamos un bucle for 
for k in range(0,len(fruta)):
    numberfrut=len(fruta[k])#mostramos la longitud de cada fruta
    print(numberfrut)
print("-----------------------------")

#Creamos un bucle for 
for j in fruta:
    if len(j)>5:#creamos un condicional 
        #mostrar solo el nombre de las frutas mayor a 5 caracteres
        print(j)
fruta.remove("cereza")#removemos "cereza" de la lista

print("-----------------------------")
print(fruta)#mostramos la lista sin "cereza"
print("-----------------------------")
print(fruta.clear())#mostramos la lista vacía
print("-----------------------------")
