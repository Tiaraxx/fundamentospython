'''
Las colas (queue), no existen en Python, pero se pueden simular utilizando las listas 
con sus metodos .append() y .pop para simular la entrada y salida de datos de la fila o cola.
Utilizando la estructura FIFO (First In First Out).
'''


# La manera normal es importando la coleccion
from collections import deque

cola = ["Jose", "Miguel", "Faury", "Albiery"]

print(cola)

# Agregar elementos al final de la cola/fila
cola = ["Jose", "Miguel", "Faury", "Albiery"]

cola.append("Joendry")
cola.append("Yerman")

print(cola)

# Sacar elementos al final de la cola/fila
cola = ["Jose", "Miguel", "Faury", "Albiery"]

# Para sacar el primer elemento debemos colocar el indice 0
variable = cola.pop(0)

print(f"Atiende a {variable}")

print(f"Luego, siguen {cola}")

