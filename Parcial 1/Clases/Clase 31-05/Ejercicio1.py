"""
UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE 
DEPARTAMENTO DE CIENCIAS COMPUTACIONALES
ESTRUCTURA DE DATOS 

MIGUEL CABRERA 
31/05/2023
9898

"""



#Ejercicio 1: Escribe un programa que permita crear una lista de nombres y luego muestre los nombres en orden alfabético.

def ordenAlfabetico(Lista):
    lista.sort() #El metodo sort ordena de mayor a menor los elementos de una lista
    return lista

lista= []

while True:
    nombre = input("Ingrese un nombre o presione enter para terminar de ingresar valores. : ")
    if nombre == "":
        break
    lista.append(nombre) # Ingresa el nombre dentro de la lista



print(ordenAlfabetico(lista))



