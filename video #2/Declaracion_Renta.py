#Solicitamos los datos
edad=input("¿Cuánto años tienes?:\n")
renta=int(input("¿Cuánto ganas al mes:?\n"))

#creamos la condición
if edad >= "18" and renta >= 1000:
  print("Tienes que tributar")
  if edad < "18" and renta < 1000:
    print("No tienes que tributar")
  if renta<=15000:
    print("Tienes que pagar el 5%")
  elif renta==15000 and renta<=25000:
    print("Tienes que pagar el 15%")
elif renta==25000 and renta<=35000:
  print("Tienes que pagar el 20%")
elif renta==35000 and renta<=60000:
  print("Tienes que pagar el 30%")
elif renta>60000:
  print("Tienes que pagar el 45%")