'''
El operador ternario, es una herramienta muy potente utilizada
por muchos lenguajes de programacion. Es igual a if...else, o sea,
tenemos la comdicion a evaluar, el codigo a ejecutar si se cumple
la condicion y el codigo si la condicion no se cumple.

Sintaxis: [codigo si es cumple] if [condicion] else
[codigo si no se cumple]
'''

a = 100
b = 16

print("Resultado es verdadero") if a > b else print('Resultado es falso')
'''
elaborar un programa que pida al ususario un numero y es par lo eleve al cubo y
 si no es par lo eleve al cuadrado
'''


numero = int(input("Digite un numero: "))

elevarPotencia = numero**3 if (numero%2) == 0 else numero**2 

print(f"El resultado es: {elevarPotencia}")


'''
Elabora un programa que pida a do usuarios el nombre y la edad, 
imprima el nombre del mayor
'''

nombre1 = input("Introduzca el nombre del primer usuario:")

edad1 = input("Introduzca la edad del primer usuario:")

nombre2 = input("Introduzca el nombre del sugundo usuario:")

edad2 = input("Introduzca la edad del segundo usuario:")

print(f"{nombre1}, es mayor.") if edad1 > edad2 else print(f"{nombre2},es mayor.")


nombre1 = input("Introduzca el nombre del primer usuario:")

edad1 = int(input("Introduzca la edad del primer usuario:"))

nombre2 = input("Introduzca el nombre del sugundo usuario:")

edad2 = int(input("Introduzca la edad del segundo usuario:"))

print(f"{nombre1}, es mayor.") if edad1 > edad2 else print(f"{nombre2},es mayor.")






