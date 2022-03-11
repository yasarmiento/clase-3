from library import *

def main ():
    #aplicacion de los diccionarios
    """
    persona = {
        "nombre": "Yair",
        "apellido": "Sarmiento",
        "edad": 20
    }
    """
    persona = {
        "datospersonales":{
        "nombre": "Yair",
        "apellido": "Sarmiento",
        "edad": 20
        },
        "salarial": {
            "salario": 2000000,
            "subtransporte": 50000,
            "subalimentacion": 60000
        }
    }

    
    #print (persona["nombre"]+ " " + persona["apellido"] )
    #persona ["nombre"] = "Andres"
    #print (f"{persona['nombre']} {persona['apellido']}" )

    print (persona["datospersonales"])
    print (f"nombre: {persona['datospersonales']['nombre']}  {persona['datospersonales']['apellido']} ")
    print (f"salario: {persona['salarial']['salario']}")
    


if __name__ == "__main__":  
    main()