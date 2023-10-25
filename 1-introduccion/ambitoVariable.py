'''
El ambito de una variable es el area que ocupa dentro del programa donde 
esa variable es conocida (declarada) y de esa manera evitar cometer errores entre las variables 
'''



# Declarar variables dentro de una funcion
valor = 5 # Variable con ambito global

def miFuncion (n):
    dato = 3 # Variable con ambito local
    print(n * dato)
    print("En la funcion" ,dato)
    print("En la funcion" ,valor) # llamar una variable declarada fuera de la funcion

miFuncion (valor)
print(valor)

# Si se intenta llamar una variable que esta declarada dentro de una funcion desde fuera,
# diria que la variable no esta definida
# print ("Afuera de la funcion" ,dato)

# Si creamos dos funciones con el mismo nombre de variable, estas se concideran diferetes
#  porque estan declardas demtro de cada funcion
valor = 5

def miFuncion(n):
    dato = 3
    print(n * dato)
    print("Dentro de la funcion" ,dato)

def miFuncion2(n):
     dato = 13 
     print(n + dato)
     print("Dentro de la funcion" ,dato)


miFuncion(valor)
miFuncion2(valor)
miFuncion(valor)