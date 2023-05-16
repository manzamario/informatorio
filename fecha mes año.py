fecha_nacimiento = input("Ingresa tu fecha de nacimiento en formato dd/mm/aaaa: ")

# Se separa la fecha en tres componentes (día, mes y año) utilizando la función split()
dia, mes, anio = fecha_nacimiento.split('/')

# Se convierten los componentes a enteros para realizar la operación de cálculo de la edad
dia = int(dia)
mes = int(mes)
anio = int(anio)

# Se calcula la edad en años utilizando la fecha actual y la fecha de nacimiento ingresada
from datetime import date
hoy = date.today()
edad = hoy.year - anio - ((hoy.month, hoy.day) < (mes, dia))

# Se muestra la edad en años en pantalla
print("Tu edad es:", edad, "años.")
