'''
Las pilas (stacks), no existen en Python pero se pueden simular utilizando las listas con sus metodos
.append() y .pop para simular la entrada y salida de datos de la pila. Utiliza la estructura de 
datos LIFO (Last In First Out) 
'''
# Agregar elementos al final de la pila
pila = [1,2,3]

pila.append(4)

print(pila)

# Sacar elementos al final de la pila
pila = [1,2,3]

pila.pop()

print(pila)

# Sacar elementos al final de la pila y almacenarlo en una variable 
pila = [1,2,3]
variablePop = pila.pop()

print(f"Sacando el elemento {variablePop} de la pila")

print(pila)