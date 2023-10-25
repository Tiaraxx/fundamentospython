'''
Ciclos o Bucle: Son una secuencia de instrucciones de codigo que 
se ejecuta repetidas veces hasta que
 la condicon asignada a dicho bucle deja de ser verdadera.
   En Python existen dos ciclos que son: For y While.

   Ciclo o Bucle For: Se utiliza cuando conocemos la cantidad de iteraciones que deseamos
   que se ejecuten. Se utiliza con coleccion(listas, tupla, diccionario o cadena).

   Sintaxis: For variable in [listas, diccionario,...]
'''

#Repetir la impresion de un elemento



# Mostrar los elementos del ciclo For usando una lista
 
for i in ["rojo", 7, 25.2, True]:
     print("Python")


for i in ["rojo", 7, 25.2, True]:
     print(i)   

# Utiliza el nombre de una coleccion en una variable
datos = ["azul", 7, 25.2, True]    

for i in datos:
     print(i)

# Recorrer el contenido de un diccionario mostrando solo clave

diccionario = {"Jose":46} 
for i in diccionario: 
     print(f"El resultado con la clave es: {i}") 

# Recorrer el contenido de un diccionario mostrando solo el valor
diccionario = {"Jose": 46, "Luis": 35, "Manuel": 25}        

for i in diccionario :
     print(f"El resultado del valor es:{diccionario[i]}")

     # print(f"{diccionario[i]}")

# Recorrer el contenido de un diccionario para mostrar la clave y el valor 

diccionario = {"Jose": 46, "Luis": 35, "Manuel": 25}        
for i in diccionario:
      print(f"{i} -> {diccionario[i]} ")

# Recorrer el contenido de un diccionario para mostrar la clave y el valor 
#usando el metodo Items

for clave, valor in diccionario.items():
     print(f"{clave} -> {valor}")

    
# Recorrer el contenido de una cadena de caracteres ( en vertical)

cadenaCaracteres = "Jose"

for i in cadenaCaracteres:
     print(f"{i}")



     cadenaCaracteres = "Jose"



# Recorrer el contenido de una cadena de caracteres (horizontal)

cadenaCaracteres = "Jose\n"

for i in cadenaCaracteres:
     print(f"{i}" ,end="")


# Impresion de numeros del 1 al 100

for i in range(1,10):
     
     print(i)
    

