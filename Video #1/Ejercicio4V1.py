#Texto de inicio
text= "Introducir el numero de cada tipo de RBM que has vendido"
serie_1= int(input("¿Cuántos RBM Serie 1 has vendido? \n"))#\n: es para que al terminar haga un salto de linea
Serie_plus= int( input("¿Cuántos RMB Serie plus has vendido? \n") )
todoterreno= int(input("¿Cuánto RBM todoterreno has vendido? \n"))
#precio de los carros
precio_serie1= 20000
precio_plus= 35000
precio_todoterreno= 60000

#la comision que gana el vendedor
comision=precio_serie1 * (3.0 / 100)
comision1 =precio_plus* (5.0 / 100)
comision2= precio_todoterreno * (0.7/100)

#multiplicamos la comision con el numero de tipos de carros vendidos
resultado_1 = comision * serie_1
resultado_plus =comision1 * Serie_plus
resultado_tdterreno= comision2 * todoterreno

#escribimos los autos vendidos y sus ganancias en cada tipo de auto
text= "Numero de carros RBM vendidos de los tipos\n Serie 1: {:.0f} su ganancia es de: {:.0f} \n".format(serie_1,resultado_1)
text1= "Serie Plus: {:.0f} su ganancia es de: {:.0f}\n".format(Serie_plus,resultado_plus)
text2= "Todoterreno: {:.0f} su ganancia es de: {:.0f}".format(todoterreno,resultado_tdterreno)
print(text+text1+text2)#mostramos en pantalla los textos anteriores en pantalla

