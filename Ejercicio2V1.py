#Tasa de cambio de euro a dolar
Euro =float(1.2)
#Textos de inicio explicativos
text="           Casa de Cambio     \nTasa de cambio: 10%\n"
text1= "Precio del Euro = {} $".format(Euro)
print(text + " " +text1+"")#mostramos los textos
cantidad = input("Introducir la cantidad que desea convertir en dolares: ")#solicitamos la cantidad a convertir
cambio_dolares=(int(cantidad)*Euro)#la operación para el cambio de euro a dolar 
descuento = (10/100)*cambio_dolares#la tasa de descuento por el cambio(lo que cobra la casa por converción)
resultado = cambio_dolares-descuento#los dolares iniciales menos el pago de la casa de cambio

text2="El total del cambio es: {: .0f} $\n".format(cambio_dolares)
text3= "La casa se queda con: {:.0f} $\nEl resultado total es: {:.0f} $".format(descuento,resultado)
print(text2+ "" + text3)
#utlicé format para que en los {} agregue los valores de las variables
#{: .0f}: agregará los valores despues del punto y como es 0 no los colocará

