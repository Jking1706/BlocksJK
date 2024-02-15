# Crea un script que acepte un string de 5 caracteres y devuelva otro string con todos los caracteres
# duplicados. Si el input es ‘sbc56’, el output deberá ser ‘ssbbcc5566’

#solicitamos el texto en pantalla
texto= input(" Introduce una cadena de texto con 5 o más carecteres: ")

#Ahora vamos a verificar el contenido
if len(texto) >= 5: 
      #Vamos a dublicar y a concatenar con join y un bucle de for
 resultado = "".join(caracteres *2 for caracteres in texto)
 print(f"Su texto lo hemos duplicado:  {resultado}")# mostramos el resultado
else:
     print("Error, El texto ingresado tiene menos de 5 caracteres")#mostramos un error si ingresan menos caracteres


