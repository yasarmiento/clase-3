def main():
    #se crea el objeto 
    class Persona():
        nombre = "Yair"
        apellido = "sarmiento"
        direccion = "Km 5"
        telefono = "3004005060"
        #una funcion dentro de una clase se llama metodo
        #si no tiene parametro, escribir "self"
        def mostrar(self):
            #toca escribir "self." antes del parametro
            print(f"mi nombre es: {self.nombre} {self.apellido}")
    
    persona1 = Persona () #crear una instancia de la clase 
    print(persona1.nombre)

    

if __name__ == "__main__":
    main()