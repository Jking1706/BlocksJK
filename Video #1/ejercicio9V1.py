#Operaciones Aritméticas
resultado = (15*3)/ (2**4)
print(f"El resultado de la operación anterior es: {resultado}" )

#Leer un numero entero positivo
n = int(input("Introduce un entero positivo:\n"))

#Operación entero positivo
resultado_op= (n ** 2) + (n * 2) + 1
print(f"El resultado de la operación es: {resultado_op}")

#Solicitamos dos numeros enteros

ent= int(input("introducir un numero Entero:\n"))
ent1= int(input("introducir otro numero Entero:\n"))

if ent1!= 0 :#creamos una condición si se cumple se ejecuta lo siguiente
    
#Calculamos el conciente y el entero
 conciente = ent // ent1 # División entera
 resto = ent % ent1 #el resto de la división
 
 #Mostramos los resultados
 print(f"Los numeros introducidos son {ent} y {ent1}")
 print(f"El Concientes es: {conciente}")
 print(f"El resto es: {resto}")
 
else:# si ent1 = 0 dirá que es un error
    if ent1== 0 : 
        print("Error, no se puede dividir por ( 0 )")