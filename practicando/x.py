#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
#imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el 
#número introducido

nombre = input("Escribe tu nombre:")

num = int(input("Dijite un numero entero:"))

print((nombre + "\n") * int(num))


bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))