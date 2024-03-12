# LISTAS NUMERICAS:
# 1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros:
# [1,2,3,4,5,6,7,8,9,10].
# 2. Crea una nueva lista con los números pares de la lista anterior en orden inverso
# 3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por
# consola.
# 4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
# compresión).
# 5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
# 6. Haz lo mismo con el número más alto
# 7. Suma todos los elementos de la lista con y sin un bucle.
# 8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
# el punto 2. 

#creamos la lista con los numeros proporcionados
numeros= [1,2,3,4,5,6,7,8,9,10]

lista_num2= []#creamos la lista para numeros pares
#creamos un bucle for para agregar los numeros pares a la lista
for i in range(0,11):
    if i % 2 == 0: #comprobamos que es par
         lista_num2.insert(0,i)#Usamos el comando "insert" para agregar en la lista y hacerlo a la inversa
lista_par = lista_num2  #almacenamos en lista_par

#creamos un bucle para potenciar los numeros pares
for num in lista_par:
    potencia= num **2
    
#creamos un bucle usando los bucles anteriores en una sola linea
potencia_pares = [num **2 for num in range(len(numeros), 0, -1) if num %2==0] 

Min_potencia = potencia_pares[0]#creamos una lista para almacenar el minimo sin usar el comando min()
Max_potencia = potencia_pares[0]# creamos otra lista para el maximo sin usar el comando max()

#Creamos un bucle para sacar el minimo y el maximo
for num in potencia_pares:
  if num< Min_potencia:
      Min_potencia = num
  elif num > Max_potencia:
      Max_potencia = num
#usamos el comando "sum" para hacer la suma de datos de la lista
sumtotal= sum(potencia_pares)#guardamos en la variable "sumTotal"

#Mostramos los resultados
print(f"Lista numeros: {numeros}")
print(f"Lista numeros pares inversos: {lista_par}")
print(f"Lista numeros pares ponteciados en orden inverso: {potencia_pares}")
print(f"El minimo de la lista de potencia es: {Min_potencia}")
print(f"El maximo de la lista de potencia es: {Max_potencia}")
print(f"La suma de la lista de numeros potenciados: {sumtotal}")
print(f"lsita numeros {numeros} el 8 está en la posicion numeros[7]")
print(f"lsita numeros {lista_num2} el 8 está en la posicion lista_num2[1]")


    

        
        
