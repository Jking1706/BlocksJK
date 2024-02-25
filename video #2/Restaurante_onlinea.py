# RESTAURANTE ONLINE:

#Solicitamos el
hamburguesa = input("¿Qué tipo de hamburguesa quieres? clásica|vegana:\n")

#creamos la lista de los ingredientes de ambas hamburguesas 
clásica = ("""Los ingredientes extras de la hamburguesa clásica son: 
        • Queso
        • Idiazabal
        • Bacon
        • Huevo
        """)
vegana = ("""Los ingredientes extras de la hamburguesa vegana son:
        • Tofu
        • Cebolla caramelizada"""
        )

#Creamos un condicional anidado para que el usuario elija la hamburguesa que quiere
if hamburguesa.lower() == "clasica":
            ingredientes = input(clásica)
            if ingredientes.lower() == "queso":
                print("Has elegido la hamburguesa clásica con queso")
            if ingredientes.lower() == "idiazabal":
                print("Has elegido la hamburguesa clásica con idiazabal")
            if ingredientes.lower() == "bacon":
                print("Has elegido la hamburguesa clásica con queso")
            if ingredientes.lower() == "huevo":
                print("Has elegido la hamburguesa clásica con huevo")

elif hamburguesa.lower() == "vegana":
            ingredientes = input(vegana)
            if ingredientes.lower() == "tofu":
                print("Has elegido la hamburguesa vegana con tofu")
            if ingredientes.lower() == "cebolla caramelizada":
                print("Has elegido la hamburguesa vegana con cebolla caramelizada")
else:
  print("El ingrediente que seleccionaste no está en nuestra lista o lo escribiste mal")