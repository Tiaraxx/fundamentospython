'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra 
y muestre por pantalla el numero de veces que aparece el numero de veces
que aparece una letra en la frase
'''


frase = input("Escriba una frase:") 
letra = input("Escribe una letra:")

contador = 0

for i in frase:
   if i == letra:
      contador += 1

print(f"La letra {letra} aparece {contador} veces en la frase {frase}.")

    
