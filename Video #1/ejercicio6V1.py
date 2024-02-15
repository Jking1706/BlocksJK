#Vamos a hacer un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total
#de la cuenta.

#definimos el menu y sus precios
menu={
     "Ensalada mixta": 12,
    "Sopa de pescado": 10,
    "Dorada al horno": 18,
    "Arroz al curry": 14,
    "Lasaña de carne": 15,
    "Brownie de chocolate": 8,
    "Helado": 6,
    "Refrescos": 5.5,
    "Café": 3.5
}
#el total de la cuenta
cuenta_Total= 0

#leemos la cantidad de cada elemento
for alimento, precio in menu.items():#hacemos un bucle que ira mencionado cada alimento del menu anterior
    cantidad= int(input(f"Cuántos platos de {alimento} has consumido:  "))#cada uno se irá almacenado en cantidad
    cuenta_Total += cantidad * precio#multiplicamos cantidad con el precio del alimento y almacenamos en cuenta_total
    #que también irá acumulando el total de cada producto
    #se mostrara el total de cada alimento consumido
    print(f"El total de la cuenta es: {cuenta_Total} Euro")

