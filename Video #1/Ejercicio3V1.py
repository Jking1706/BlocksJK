
text = "Introducir los minutos|segundos|centésimas de los siguientes atletas:\n"

#Datos de hannah
Hannah_Neise = "Hannah Neise"
print(text + " " + Hannah_Neise)#mostramos en pantalla nombre y texto
min_h = int(input("Minutos:\n"))
seg_h = int(input("Segundos:\n"))
cente_h = int(input("Centésimas:\n"))

#datos de jackie
Jackie_Narracott = "Jackie Narracott"
print(Jackie_Narracott + ": \n")#mostramos nombre
min_j = int(input("Minutos:\n"))
seg_j = int(input("Segundos:\n"))
cente_j = int(input("Centésimas:\n"))

# datos de kimberley
Kimberley_Bos = "Kimberley Bos"
print(Kimberley_Bos + ": \n")#mostramos nombre
min_k = int(input("Minutos:\n"))
seg_k = int(input("Segundos:\n"))
cente_k = int(input("Centésimas:\n"))

# Convertimos los tiempos a segundos
Tiempo_H = (min_h * 60 + seg_h + cente_h / 100)
Tiempo_J = (min_j * 60 + seg_j + cente_j / 100)
Tiempo_K = (min_k * 60 + seg_k + cente_k / 100)

# Calculamos la velocidad media (suponiendo una pista de 100 metros)
metros_pista = 100
Velocidad_H = metros_pista / Tiempo_H
Velocidad_J = metros_pista / Tiempo_J
Velocidad_K = metros_pista / Tiempo_K

# Mostramos los resultados
print("\nResultados:")
print(Hannah_Neise + " - Velocidad media: {:.2f} Metros por segundo".format(Velocidad_H))
print(Jackie_Narracott + " - Velocidad media: {:.2f} Metros por segundo".format(Velocidad_J))
print(Kimberley_Bos + " - Velocidad media: {:.2f} Metros por segundo".format(Velocidad_K))
#utlicé format para que en los {} agregue los valores de las variables
#{: .2f}: agregará los valores despues del punto y como es 2 colocará dos numeros despues del (.)
# f indica que el dato es flotante
