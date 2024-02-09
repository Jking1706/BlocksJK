#CALCULADORA DE AHORROS

#solicitamos unos datos al usuario
name= input("¿Cuál es tu nombre?")
print(f"Hola {name}")

pago_horas= float(input("¿Cuánto te pagan por hora?: "))
hora_trabajo= float(input("¿Cuántas horas has trabajado?: "))

#sacamos la ganancia semanal y anual
semana= hora_trabajo * 21
salario_semanal= (pago_horas * semana)
ganancia_anual= salario_semanal * 52
#mostramos
print(f"Hey {name}, Tienes una ganacia anual de: {int(ganancia_anual)} $")

#solicitamos sus gastos semanales
gastos_semanal = float(input(f"Hey {name}, ¿Cuánto gastas semanalmente?\nIntroduce la cantidad: "))
#sacamos los anuales
gasto_anual = gastos_semanal * 52
#restamos los gastos anuales a las ganancias anuales
resultado= ganancia_anual- gasto_anual
#mostramos

print(f"hey {name}, te quedan: {resultado}")
