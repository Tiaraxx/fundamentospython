'''
Las duplas son listas inmutables, es decir, no se pueden 
modificar despues de su creacion.
    -No permiten anadir, eliminar, mover elementos, entre otros (no append, 
    extend, remove ).
    -Si permiten extraer porcones, pero el resultado de la extracciones
    es una dupla nueva.
    -No permiten busqueda (no index)
    -Si permiten comprobar si un elemento se encuentra en la dupla.

    Ventajas o utilidad con respecto a las listas
    -Mas rapidas.
    -Menos espacio (Mayor optimizacion).
    -Foematean strings
    -Puede usarse como claves en un diccionario (las listas, no).
'''

miTupla = ("Yerman", 5,7,2023)

# Metodos para convertir de tupla a lista y viceversa
# Covertir una tupla en  lsita, se utiliza el metodo list
miTupla =("Yerman", 5,7,2023)
miLista=list(miTupla)
print(miLista)

# Covertir una lista en  tupla, se utiliza el metodo tuple
miLista =("Yerman", 5,7,2023)
miTupla=tuple(miLista)
print(miTupla)

# Comprobar si hay elementos dentro de la tupla con la instruccion IN
miTupla =("Yerman", 5,7,2023)
print("Yerman" in miTupla)


# Comprobar la cantidad de de veces que se repite un
#  elementos dentro de una tupla conel metodo COUNT
miTupla =("Yerman", 5,7,2023)
print (miTupla.count(5))

# Comprobar la longitud de la tupla con el metodo LEN
miTupla =("Yerman", 5,7,2023)
print(len(miTupla))

# Tupla unitaria, son tupla con un unico elemento, al final se coloca 
# una coma (,)
miTupla =("Yerman",)
print(len(miTupla))

# Si colocamos una tupla sin una coma (,) al final, cuenta el total de caractere
miTupla =("Yerman")
print(len(miTupla))

# Desempaquetado de tuplas 
miTupla =("Yerman", 5, 7,2023)
nombre, dia, mes, anio = miTupla
print(nombre, dia, mes, anio)




