# PAR O IMPAR:
# Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa
# potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)

#Solicitamos un numero
numero= int(input("Introduce un numero:\n"))
potencia= int(input("Introduce la potencia:\n"))


#Hacemos la potenciación
potencia1= numero ** potencia

#creamos una condición para verificar si es par o impar
if potencia1 % 2 == 0:
    print("Este numero",numero,"elevado a",potencia,"=" ,potencia1," es par")
else:
      print("Este numero",numero,"elevado a",potencia,"=" ,potencia1," es impar")