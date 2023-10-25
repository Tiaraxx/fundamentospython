'''
Lambda : Es una funcion  anonima y se utiliza en python al momento de programar para
 abreviar la sixtaxist asi ahorrar tiempo. O sea nos permite resumir una funcion 
 normal en python  en una funcion lanmbda.

Todo lo que hacemos con una funcion lamnbda, lo podemos hacer co una funcion normal,
 pero no  todo lo que se puede hacer en una funcion normal  se puede hacer en un
   afuncion lambda.

Tambien son llamadas:
-on the go
-on demand
-online
'''

#FUNCION NORMAL

'''
def, se utiliza para crar objetos los cuales son definidos por cada usuario son
 sentencias para ejecutar con el nombre de la funcion y tiene referencia al 
 nombre o namespace local o global.
'''

def area_triangulo(base , altura):
    print((base*altura)/2)
triangulo1 = area_triangulo(5,7)
triangulo2 =area_triangulo(9,6)

print(triangulo1)
print(triangulo2)

#Funcion lambda.ejmeplo1
area_triangulo = lambda base,altura :(base*altura)/2

triangulo1 = area_triangulo(5,7)
triangulo2 =area_triangulo(9,6)
print(triangulo1)
print(triangulo2)

# Funcion Lambda. Ejemplo 2

al_cubo = lambda numero:pow(numero, 3)

# al_cubo = lambda numero:numero**3

print(al_cubo(5))

# Funcion Lambda. Ejemplo 3

destacar_valor = lambda comision:"¡{}! RD$".format(comision)
comision_jose = 5800

print(destacar_valor(comision_jose))

