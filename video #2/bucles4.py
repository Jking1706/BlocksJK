# Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
# pantalla el número de veces que aparece la letra en la frase.
#solicitamos una frase
 
frase=input("Introduce una frase: ")
#Solicitamos una letra
letra=input("Introduce una letra: ")
numletra= 0
frase1= ""
#creamos un bucle
for i in range(0,len(frase)):
    frase1= frase[i]#Frase1 toma cada letra de la frase 1 por una
    if frase1 == letra:#condicional si frase1 es igual a la letra
        numletra += 1# el numletra va sumando 1
        print("------------Resultado----------------")   

print(f"Letra introducida: {letra}")
print(f"El numero de letras en la frase es: {numletra}")