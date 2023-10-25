'''
los diccionarios, se colocan dentro de llaves {}, se guardan desordenados y tienen dos elementos
por posicion: clave y valor. Ademas, no pueden existri claves duplicadas. Tambien, aceptan diferentes
tipos de datos.
'''
# Diccionario vacio
diccionario = {}

print(diccionario)

# Agregar y mostrar los valores de un diccionario 
estudiantes = {"Nombre": "Yohan", "Edad":18, "Tecnico":["Linux", "Python", "Git & Github"]}

print(estudiantes)

# Mostrar valores especificos de un diccionario 
estudiantes = {"Nombre": "Yohan", "Edad":18, "Tecnico":["Linux", "Python", "Git & Github"]}

print(estudiantes["Tecnico"])

# Mostrar valores especificos de un diccionario Con multiple datos
estudiantes = {"Nombre": "Yohan", "Edad":18, "Tecnico":["Linux", "Python", "Git & Github"]}

print(estudiantes["Tecnico"][1])

# Mostrar valores especificos de un diccionario con el constructor dict
estudiantes = dict(Nombre="Yohan", Edad=18, Tecnico=["Linux", "Python", "Git & Github"])

print(estudiantes)

# Verificar tipo de dato
print(type(estudiantes))

# Agregar elementos  a un diccionario
estudiantes = {"Nombre": "Yohan", "Edad":18, "Tecnico":["Linux", "Python", "Git & Github"]}

estudiantes["Tanda"] = "Tarde"

print(estudiantes)

# Modificar valores de un diccionario

estudiantes = {"Nombre": "Yohan", "Edad":18, "Tecnico":["Linux", "Python",
 "Git & Github"], "Tanda":"Tarde"}

estudiantes["Tecnico"] = "HTML, CSS, JavaScript"

print(estudiantes)

# Eliminar valores de un diccionario
estudiantes = {"Nombre": "Yohan", "Edad":18, "Tecnico":["Linux", "Python",
 "Git & Github"], "Tanda":"Tarde"}

del(estudiantes["Tecnico"])
 
print(estudiantes)

# Agregar elementos con diferentes tipos de datos en un diccionario (con listas)
estudiantes = {"Milton":[20,5.12],"Maria":[21,4.11],"Jose Miguel":[28,5.6]}

print(estudiantes)

# Agregar elementos con diferentes tipos de datos en un diccionario (con otro diccionario)
estudiantes = {"Milton":{"Edad":18,"Estatura":5.6},"Esmeralda":{"edad":28, "estatura":3.6}, 
"Maria":[18,4.10]}

print(estudiantes)

# Buscar elementos que no existen en un diccionario con el metodo get()
estudiantes = {254658:"Massiel", 254659:"Yerman", 254660:"Smailyn", 254661:"Laura"}


print(estudiantes.get(254657, "el valor introducido NO existe"))

# Realizar busquedas directas en un diccionario
estudiantes = {254658:"Massiel", 254659:"Yerman", 254660:"Smailyn", 254661:"Laura"}

print(254658 in estudiantes)

# Mostrar todas las claves en un diccionario con el metodo keys()
estudiantes = {254658:"Massiel", 254659:"Yerman", 254660:"Smailyn", 254661:"Laura"}

print(estudiantes.keys())

# Mostrar todos los valores en un diccionario con el metodo values()
estudiantes = {254658:"Massiel", 254659:"Yerman", 254660:"Smailyn", 254661:"Laura"}

print(estudiantes.values())

# Mostrar todas las claves y los valores en un diccionario con el metodo items()
estudiantes = {254658:"Massiel", 254659:"Yerman", 254660:"Smailyn", 254661:"Laura"}

print(estudiantes.items())

# Mostrar cuantos elementos tengo en un diccionario usando el metodo len()
estudiantes = {254658:"Massiel", 254659:"Yerman", 254660:"Smailyn", 254661:"Laura"}

print(len(estudiantes))

# eliminar todos los elementos en un diccionario usando el metodo clear()
estudiantes = {254658:"Massiel", 254659:"Yerman", 254660:"Smailyn", 254661:"Laura"}

estudiantes.clear()

print(estudiantes)


