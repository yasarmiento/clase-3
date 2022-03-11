def listas ():
    lista1 = []
    lista2 = list()

    listaconelementos = [30, 2000000,"Ing sistemas", "Yair Sarmietno", "estudiante", True, ["semestre 9", 2020] ]

    #aumentar el valor de un dato
    #listaconelementos[1]=listaconelementos[1]+200000

    #print(listaconelementos[1])

    #utilizando ciclo for
    print("mostrando elementos con ciclo for")
    for i in range(len(listaconelementos)):
        print (listaconelementos[i])
    
    
    print("")
    print("")
    print("")
    #utilizando ciclo while
    print("mostrando elementos con ciclo while")
    j=0
    while j < (len(listaconelementos)):
        print (listaconelementos[j])
        j+=1
    #ultimo numero de la lista => print (listaconelementos[-1])
    #mostrar con rangos print (listaconelementos[0:3])
    #mostrar con rangos y saltando (pares) print (listaconelementos[0:3:2])
    #mostrar con rangos y saltando (impares) print (listaconelementos[1:3:2])
    #una lista dentro de otra print (listaconelementos[-1][3])
    #agregar un elemento a la lista al final
    #listaconelementos.append(["sede Riohacha", "Mieguel Soto"])
    #agregar un elemento a la lista en la posicion x
    listaconelementos.insert(2, ["sede Riohacha", "Mieguel Soto"])
    print(listaconelementos)
    #eliminar elementos de una lista segun su posicio en el arreglo
    # listaconelementos.pop(2)
    del listaconelementos[2]
    #borra un elemento en especifico de la lista
    listaconelementos.remove("Ing sistemas")
    print(listaconelementos)


def main ():
    listas ()

if __name__ == "__main__":  
    main()