# EL MAYOR DE CUATRO:
# Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
# pantalla.

#solicitamos los numeros uno por uno con input y los convertimos en float
numero=float(input("Intoducir el primer numero:\n"))
numero_1=float(input("Intoducir el segundo numero:\n"))
numero_2=float(input("Intoducir el tercero numero:\n"))
numero_3=float(input("Intoducir el cuarto numero:\n"))

#Utilizamos la función max()
mayor= max(numero,numero_1,numero_2,numero_3)

#Mostramos los resultados
print("El valor más alto es: ",int(mayor))