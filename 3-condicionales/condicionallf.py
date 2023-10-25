# Condicional IF simple (if)
num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("Intoduzca el segundo numero: "))

if num1 > num2:
    print("El valor de la variable num1 es mayor que el valor de la variable num2")

    estadoCivil = "Casado"

    if estadoCivil == "Casado" :
       print("No se si felicitarlo o darle el pesame.")

       # Condicional IF doble (if... else)
num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("Intoduzca el segundo numero: "))

if num1 > num2:
    print("El valor de la variable num1 es mayor que el valor de la variable num2")

else:
     print("El valor de la variable num2 es mayor que el valor de la variable num1")


 # Condicional IF multiple (if...elif....else)
num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("Intoduzca el segundo numero: "))

if num1 > num2:
    print("El valor de la variable num1 es mayor que el valor de la variable num2")

elif num2 > num1:
    print("El valor de la variable num2 es mayor que el valor de la variable num1")

else: 
    print("Los valores de las variables num1 ynum2 son iguales")


    