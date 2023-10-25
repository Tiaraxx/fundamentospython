'''
Los conjuntos o sets, son colecciones donde los elementos se agregan de forma 
desordenada y no pueden existir elementos duplicados. Se utilizan llaves {}.
Dentro de los conjuntos no se pueden agregar otras colecciones.
'''

# Mostrar un conjunto vacio
conjunto = set() #set(), indica que es un conjunto, pero solo si esta vacio
conjunto = {}
print(conjunto)

# Agregar elementos a los conjuntos
conjunto = {"Jose", 2.8, 3, "Miguel"}
conjunto.add(2023) # Se pueden agregar todos los valores que se deseen
conjunto.add(2004)
print(conjunto)

# Agregar elementos a los conjuntos e ignorar los que estan repetidos
conjunto = {"Juan", 2.8, 3, "Juan", "Pedro"}
conjunto.add(3) # No aceptara valores duplicados
print(conjunto)

# Eliminar elementos de un conjunto con metodo discard()
conjunto = {"Juan", 2.8, 3, "Juan", "Pedro"}
conjunto.discard("Pedro")
print(conjunto)

# Vaciar conjunto
conjunto = {"Juan", 2.8, 3, "Juan", "Pedro"}
conjunto.clear()
print(conjunto)

# Buscar un elemento dentro del conjunto
conjunto = {"Juan", 2.8, 3, "Juan", "Pedro"}
print("Juan" in conjunto) # O print("Juan" not in conjunto) 

# Comprobar si ambos conjunto  son iguales
conjunto1 = {1,8.5,3,8}
conjunto2 = {3,1,8.5,8}

print(conjunto1 == conjunto2)

# Conocer la cantidad de elemento que posee un conjunto
conjunto1 = {1,8.5,3,8,9}
conjunto2 = {3,1,8.5,8,9}

print(len(conjunto1))

# Union de dos conjuntos: Muestra los elementos que estan en ambos conjuntos,  sin los duplicados
conjunto1 = {1,8.5,3,8,"Juan"}
conjunto2 = {"Juan", 3,1,8.5,8,"Joendry"}

unionConjunto = conjunto1 | conjunto2

print(unionConjunto)

# Interseccion de dos conjuntos: Muestra los elementos en ambos conjuntos
conjunto1 = {1,8.5,3,8,"Joendry",}
conjunto2 = {"Joendry",8.5,8,}

interseccionConjuntos = conjunto1 & conjunto2
print(interseccionConjuntos)

# Diferencia de dos conjuntos: Muestra los elementos que estan en conjunto1 pero no
# en conjunto2, o viceversa
conjunto1 = {1,8.5,3,8,"Joendry",}
conjunto2 = {"Joendry",8.5,8,}

diferenciaConjuntos = conjunto2 - conjunto1

print(diferenciaConjuntos)

# Diferencia simetrica de dos conjuntos: Muestra los elementos que solo estan en conjunto1 pero no
# en conjunto2, pero no en ambos.
conjunto1 = {1,8.5,3,}
conjunto2 = {"Joendry",8.5,9,}

dsimetricaConjuntos = conjunto1 ^ conjunto2

print(dsimetricaConjuntos)

# Determinar si un conjunto es subconjunto de otro conjunto
conjunto1 = {1,8.5,3,}
conjunto2 = {10,8.5,9,}

subconjunto = {1,3,8.5,9,10}

print(conjunto1.issubset(subconjunto))

# Determinar si un conjunto es superconjunto de otro conjunto
conjunto1 = {1,8.5,3,}
conjunto2 = {10,8.5,9,4}

superconjunto = {1,3,8.5,9,10}

print(superconjunto.issuperset(conjunto2))