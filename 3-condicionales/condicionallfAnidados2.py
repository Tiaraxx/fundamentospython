nombre = input("Digite su nombre:")
apellido = input("Digite su apellido:")
educacion = input("Digite su nivel academico:")
edad = int(input("Digite su edad:"))

if (educacion == "Barchiller" or educacion == "barchiller") and edad >= 16:
       
  print(f"{nombre}, usted es  barchiller y es {edad} años de edad, por lo que puede realizar cursos tecnicos en el INFPTEP")

  print(f"{nombre} Usted reune las condiciones para realixar el curso tecnico en el INFOTEP") 
  
else: 
   
 print(f"{nombre}, Usted aun no es barchiller o no tiene la edad suficiente para estudiar los cursos de INFOTEP")    