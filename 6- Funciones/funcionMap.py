'''
La funcion map, apilca una funcion a cada elemento de una lista iterable
(listas, duplas, etc) devolviendo una lsita con los resultados.
Permite utilizar una funcion en lugar de una condicion.
'''
class Empleado: 
    def __init__ (self, nombre, cargo, salario):
        self.nombre = nombre 
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tieme un salario de RD${} pesos.".format(self.nombre, self.cargo, self.salario)

listaEmpleados =[
Empleado ("Juan", "Director", 175000),
Empleado ("Ana", "Presidente", 125000),
Empleado ("Antonio", "Administrador", 85000),
Empleado ("Sara", "Secretaria", 75000),
Empleado ("Mario", "Mantenimiento", 50000) ]


# Crear una funcion para realizar calculos de la comision

def calculo_comision(empleado):
        empleado.salario = empleado.salario
        return empleado

  
listaEmpleadoComision = map(calculo_comision, listaEmpleados)

for empleados in listaEmpleadoComision:
   print(empleado)

 
# Aplicar comision solo a los trabajadores con salario bajos

def calculo_comision (empleado):
    if(empleado.salario <= 50000):
        empleado.salario = empleado.salario *1.10
    return empleado

listaEmpleadosComision = map(calculo_comision, listaEmpleados)

#for empleado in listaEmpleadoComision:
print(f"El empleado {empleado} ha ganado RD$ de comision en este mes")
           



