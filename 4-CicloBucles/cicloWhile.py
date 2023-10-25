'''
Ciclo o bucle while, se utiliza cuando no conocemos la cantidad de interaciones que se ejecutaran.
 Se utiliza con colecciones (listas, tuplas, conjunto, diccionario o cadena)
'''

# Importar el modulo math para la raiz cuadrada 
import math

numero = int(input("Introduzca un numero: "))

while numero < 0:
      print("El numero no puede ser negativo, inteten de nuevo!")
  
      numero = int(input("Introduzca un numero: "))

print(f"La raiz cuadratica de {numero} es:{(math.sqrt(numero)):.2f}")

# Imprimir contenido varias veces

variable = 1

while variable <= 100:
      print(variable)
      variable = variable + 1

