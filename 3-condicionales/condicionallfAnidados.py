edad = int(input("Digite la edad:"))
educacion = input("Digite su nivel academico: ")

if educacion == "Barchiller" or educacion == "barchiller":
 if edad >= 16:
     print("Usted reune las condiciones para realixar el curso tecnico en el INFOTEP")

 else: 
    print("Usted no tiene la edad minima para estudiar en el INFOTEP")

else:
   print("Usted aun no es barchiller, por lo tanto no puede realizar los cursos en el INFOTEP")    