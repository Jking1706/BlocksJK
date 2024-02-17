# EL TRIÁNGULO:
# En una obra es necesario construir para el tejado de una casa una estructura triangular con tres
# piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir
# este estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo
# con esas piezas.
# (Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para
# todas las posibles combinaciones)

#Solicitamos las longitudes
print("Por favor ingresar las largura de las piezas")
longitud=int(input("introducir la longitud de la primera pieza:\n"))
longitud_1=int(input("introducir la longitud de la segunda pieza:\n"))
longitud_2=int(input("introducir la longitud de la tercera pieza:\n"))

#creamos una condicion y vamos sumando y mirando si es mayor a uno de los 3 
if (longitud+longitud_1>longitud_2)and(longitud+longitud_2>longitud_1)and(longitud_1+longitud_2>longitud):
    print("Se puede contruir con esas medidas de las piezas")#si es así mostrará esto
else:
    print("No se puede contruir con esas medidas")#si no esto