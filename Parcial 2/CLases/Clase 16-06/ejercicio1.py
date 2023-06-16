"""

Ejercicio 1: Búsqueda lineal en una lista de números

Descripción: Implementar un programa que realice una búsqueda lineal en una lista de
números enteros. El programa debe solicitar al usuario un número objetivo y buscar ese
número en la lista. Si el número se encuentra en la lista, se debe imprimir su posición. En
caso contrario, se debe imprimir un mensaje indicando que el número no está presente.

"""

def Busqueda(lista, objetivo):

    i = 0
    encontrado = False

    while not encontrado:
        if objetivo == lista[i]:
            encontrado = True
        else:
            if i != len(lista) -1:
                i = i+1
            else:
                break
    
    if encontrado == True:
        return "El numero se encontre en en la lista en la posicion: " + str(i)
    else:
        if encontrado == False:
            return "El objetivo no se encontro dentro de la lista"
            
    

objetivo = int(input("Ingrese el numero deseado a buscar: "))

lista = [1,2,3,5,7,11,13,17]

print(Busqueda(lista, objetivo))
