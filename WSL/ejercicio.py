#calcular devengado
#sumar alimentacion y transoporte para suma al sueldo
#sumar pension y salud y restarselo al sueldo 
#si sueldo <2.000.000 se le paga subbsidio de alientacion 80.000 y transoprte 60.000
#si sueldo >=2.000.000 transporte = 0 y alimentacion = 0 
#pension = 0.4% del sueldo 
#salud =0.375%

def main():
    class Persona():
        def __init__(self):
            self.nombre = input("ingrese el nombre:  ")
            self.apellido = input("ingrese el apellido:  ")
            self.direccion = input("ingrese la direccion:  ")
            self.telefono = input("ingrese el telefono:  ")
        #una funcion dentro de una clase se llama metodo
        #si no tiene parametro, escribir "self"
        def mostrar(self):
            #toca escribir "self." antes del parametro
            print(f"mi nombre es: {self.nombre} {self.apellido}")

    #persona1 = Persona()
    #persona1.mostrar()

    #persona2 = Persona()
    #persona2.mostrar()

    class Empleado(Persona):
        def __init__(self):
            super().__init__()
            #poner __ despues del "self." bloquea los datos y no deja hacer modificaciones desade afuera
            self.sueldo = float(input("ingrese su sueldo:  "))
            self.alimentacion = 0
            self.transporte = 0
            self.pension = 0
            self.salud = 0
            self.devengado = 0
            self.deducciones = 0

        def mostrarEmpleado(self):
            super().mostrar()
            print(f"sueldo: {self.sueldo}")
            print(f"transporte: {self.transporte}")
            print(f"alimentacion: {self.alimentacion}")
            print(f"pension: {self.pension}")
            print(f"salud: {self.salud}")
            print(f"devengado: {self.devengado}")
            print(f"deducciones: {self.deducciones}")

    empleado1 = Empleado()
    #empleado1.sueldo = 4000000
    

    if empleado1.sueldo < 2000000:
        empleado1.alimentacion = 80000
        empleado1.transporte = 60000

    #calculando pension
    empleado1.pension = empleado1.sueldo*0.04
    #calculando salud
    empleado1.salud = empleado1.sueldo*0.0375
    empleado1.devengado = empleado1.sueldo + empleado1.alimentacion + empleado1.transporte
    empleado1.deducciones = empleado1.sueldo - empleado1.salud - empleado1.pension

    
    empleado1.mostrarEmpleado()
        



if __name__ == "__main__":
    main()