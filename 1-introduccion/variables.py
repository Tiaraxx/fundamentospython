# para los comentarios de una linea se utiliza el signo de #
'''
para los comentarios de varias lineas en Python
 se utilizan triple comillas simples
'''
# En Python, no se declara los tipos de datos

# Declarar y asignar valores a una variable
numero = 10 # Variable con valor entero (int)
real = 25.2 # Variable con valor decimal (float)
doble = 25.457456 # Variable con valor decimal alto (double)
nombre = "Jose" # Variable con cadena de caracteres | strings (str)
valor = True # Variable con datos booleanos (bool)

#Imprimir valores en pantalla
print(numero)
print (real)
print(doble)
print(nombre)
print(valor)

# Mostrar el tipo de dato de una variable 
print(type(numero))
print(type(real))
print(type(doble))
print(type(nombre))
print(type(valor))

# Calculos con variables 
num1 = 10
num2 = 6.7

suma = num1 + num2

print("El resultado de la suma es",suma)

# Jerarquia de operadores
# Sin especificar la jerarquia, primero se multiplica num2(6.7) por 10, luego se divide entre 6 y al final se suma el valor de num1 (10)
resultado = (num1 + num2) * 10 / 6



# Si especificamos la jerarquia, primero se calcula lo que esta dentro de parentesis (num1 + num2), o sea, 10 mas 6.7 y el resultado de la suma se multiplica por 10 y luego se divide entre 6
resultado = (num1 + num2) * 10 / 6

print ("El resultado del calculo es" ,resultado)

# Tipado dinamico en Python: Permite que el tipo de una variable sea cambiado en cualquier momento en la ejecuciondel programa
valor = 8
print(valor)

valor = "infotep"
print(valor)