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
            self.__sueldo = float(input("ingrese su sueldo:  "))
            self.alimentacion = 0
            self.transporte = 0
            self.pension = 0

        def mostrarEmpleado(self):
            super().mostrar()
            print(f"sueldo: {self.__sueldo}")
            print(f"transporte: {self.transporte}")
            print(f"alimentacion: {self.alimentacion}")
            print(f": {self.pension}")

    empleado1 = Empleado()
    empleado1.sueldo = 4000000
    empleado1.mostrarEmpleado()



if __name__ == "__main__":
    main()