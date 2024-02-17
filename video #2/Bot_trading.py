# BOT DE TRADING:
# Un bot de trading está programado para realizar ciertas acciones con respecto a un producto
# financiero. Crea un script de manera que dado un precio introducido por el usuario, si el precio del
# producto está por debajo de 100 dólares, el bot imprima por pantalla la orden de comprar. Si está
# entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. Si el precio está
# estrictamente por encima de 150 el bot deberá imprimir la orden de vender

#Solicitamos el precio al usuario
precio_usuario=int(input("Ingresa el precio de tus acciones:\n"))

#creamos una condición  
#si el precio es menor a 100 recomienda comprar
if precio_usuario<100:
    print("Deberias comprar")
    #Si el precio es mayor o igual a 100 y menor o igual a 150 recomienda esperar
elif (precio_usuario>=100) and (precio_usuario<=150):
    print("deberias esperar")
    #si el precio es mayor a 150 recomienda vender
elif precio_usuario>150:
    print("Deberias vender")