'''
Operadores logicos: Permite construir expresiones logicas, y se obtiene como
resultado boleanos (True | False).
Los operadores logicos son:
1-AND(Conjuncion): Se le conoce como multiplicacion logica. Sera verdadero cuando ambas
sean verdaderas.
2- OR(Disyuncion): Se le conoce como suma logica. Sera verdadera vuando una o ambas condiciones 
sean verdaderas.
3-NOT(Negacion): Si niegas u valor, sera lo contrario al valor existente.
La prioridad de los operadores logicos:
NOT
AND
OR

Ejemplo:
a= 10, b= 12, c= 13, d= 10
((a > b) or (a < c)) and ((a == c) or (a >= b))

Prioridad de los operadores en general
1- ()
2-**
3- * / mod not
4- + - and
5- > < == >= <= != or
'''
 
operador = 10 > 12
print(operador)

operador = 10 < 13
print(operador)

operador = 10 == 13
print(operador)

operador = 10 >= 12
print(operador)