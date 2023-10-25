'''
Las colecciones en Python son estructuras de datos que permiten agrupar multiples
 objestos o valores de diferentes tipos de datos bajo mismo nombre. En Python, existen tres
colecciones basicas que son 

1- Listas
2- Tuplas
3- Diccionario
Listas: son una estructura de datos que nos permiten almacenar gran cantidad 
de valores identificado por indices(equivalentes a los array en otros 
lenguajes de programacion.)
- En Python, las listas pueden guardar diferentes tipos de valores(en otros
lenguaje no ocurre esto con los array)
- Se pueden expandir dinamicamente anadiendo nuevos elememtos(otra novedad 
respeto a los array en otros lenguejes.)

Sintaxis: nombrelista=[elem1, elem2, elem3,.....]
'''

# Mostrar una lista vacia 
miLista=[]
print()

# Mostrar toda la lista
miLista=["Esmeralda", "Milton", "Maria", "Faury", "Massiel", "Laura"]
print(miLista[:])

# Acceder a un elemento no existente: Se crea una 
# excepcion o error (indice fuera de rango)
miLista=["Esmeralda", "Milton", "Maria", "Faury", "Massiel", "Laura"]
print(miLista[5])

# Colocar indice negativo: Leera de derecha a izquierda empezando
# por el indice 1
miLista=["Esmeralda", "Milton", "Maria", "Faury", "Massiel"]
print(miLista[-1])

# Seleccionar una porcion de la lista, o sea, 
# mostrar parte de los elemtos de la lista
miLista=["Esmeralda", "Milton", "Maria", "Faury", "Massiel", "Laura"]
print(miLista[0:6])

# Agregar elementos al final de una lista con la instruccion append
miLista=["Esmeralda", "Milton", "Maria", "Faury", "Massiel", "Laura"]
miLista.append("Jose")
print(miLista[:])

# Agregar elementos en cualquier lugar de una lsita con ;a instruccion insert,
# utilizando dos parametros (indice, elemento)
miLista=["Esmeralda", "Milton", "Maria", "Faury", "Massiel", "Laura"]
miLista.insert(2,"Jose")
print(miLista[:])

# Agregar varios elementos a una lista con la instruccion extend, se utiliza
# dos parametros (indice, elemeto)
miLista=["Esmeralda", "Milton", "Maria", "Faury", "Massiel", "Laura"]
miLista.extend(["Tiara", "Jose", "Yerman","Albiery"])
print(miLista[:])

# Conocer el indice correspondiente a un elemento con la instruccion indix
miLista=["Esmeralda", "Milton", "Maria", "Faury", "Massiel", "Laura"]
miLista.extend(["Tiara", "Jose", "Yerman","Albiery"])
print(miLista[:])
print(miLista.index("Jose"))
