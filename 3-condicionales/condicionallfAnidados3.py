nombre = input("Digite su nombre:")
apellido = input("Digite su apellido:")
educacion = input("Digite su nivel academico:")

if educacion == "Barchiller" or educacion == "barchiller":
   edad = int(input(f"{nombre}{apellido} udted ya es barchiller.\nPor favor, introduzca su edad: "))
   if edad >= 16:

    print(f"{nombre} Usted reune las condiciones para realixar el curso tecnico en el INFOTEP")

   else: 
    print(f"{nombre}, Usted no tiene la edad minima para estudiar en el INFOTEP")

else:
   print(f"{nombre}, Usted aun no es barchiller, por lo tanto no puede realizar los cursos en el INFOTEP")    