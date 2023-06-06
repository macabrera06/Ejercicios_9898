"""
UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE 
DEPARTAMENTO DE CIENCIAS COMPUTACIONALES
ESTRUCTURA DE DATOS 

MIGUEL CABRERA 
31/05/2023
9898

"""

# Ejercicio 2: Implementa una Pila utilizando una estructura de datos adecuada y realiza las operaciones de apilar y desapilar

class Pila:
    def __init__(self):
        self.elementos = [] #Aqui estamos asignado que dentro de la pila usaremos una lista para guardar los elementos

    def apilar(self, elemento):
        self.elementos.append(elemento)  #con esta funcion appened podemos agregar elementos a la lista de la pila

    def desapilar(self):
        if not self.vacia():   #Verificamos que la pila tenga datos dentro de su lista
            return self.elementos.pop() #Eliminamos el elemneto de la ultima posicion de la lista
    
    def vacia(self):
        return len(self.elementos) == 0  #Verifica si tiene elementos al contavilizar y comparar si es igual a 0


# Realizamos las operacion apilar y desapilar

pila = Pila()

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)

pila.desapilar()
print(pila.elementos)

pila.apilar(4)
print(pila.elementos)