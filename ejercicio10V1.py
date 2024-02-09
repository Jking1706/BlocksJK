#CALCULADORA DE AHORROS

#solicitamos unos datos al usuario
name= input("¿Cuál es tu nombre?")
print(f"Hola {name}")

pago_horas= float(input("¿Cuánto te pagan por hora?: "))
hora_trabajo= float(input("¿Cuántas horas has trabajado?: "))

#sacamos la ganancia semanal y anual
salario_semanal= (pago_horas * hora_trabajo)
ganancia_anual= salario_semanal * 52
#mostramos
print(f"Hey {name}, Tienes una ganacia anual de: {int(ganancia_anual)} $")

#solicitamos sus gastos semanales
gastos_semanal = float(input(f"Hey {name}, ¿Cuánto gastas semanalmente?\nIntroduce la cantidad: "))
#sacamos los anuales
gasto_anual= (gastos_semanal * 52)
#restamos los gastos anuales a las ganancias anuales
resultado= ganancia_anual- gasto_anual
#mostramos

print(f"hey {name}, te quedan: {int(resultado)} Euros")
#Problema:
# ¿Si el usuario decidiese trabajar a tiempo parcial (25 horas semanales) y decidiese reducir sus
# gastos a 3/4 de lo que gastaba antes, tendría suficiente dinero para sus gastos?
# (Pista: tan solo necesitas cambiar los valores de las variables de ‘horas trabajadas por semana’ y
# ‘gastos semanales’)
horas_semanales_trabajadas= 25
gastos_semanal= gastos_semanal * 3//4

#Calculamos su nuevo salario semanal
salario_semanal= pago_horas * horas_semanales_trabajadas
#Salario anual
ganancia_anual= salario_semanal * 52
#Calculamos los nuevos gastos
gasto_anual= gastos_semanal * 52
#Calculamos los nuevos ahorros anuales
resultado= ganancia_anual - gasto_anual
#mostramos los resultados
print("\nCon trabajo a tiempo parcial y gastos reducidos:")
print(f"Los gastos anuales de {name} son: {int(gasto_anual)} euros")
print(f"Los ahorros anuales de {name} son: {int(resultado)} euros")