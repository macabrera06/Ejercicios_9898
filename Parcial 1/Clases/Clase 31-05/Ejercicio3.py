"""
UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE 
DEPARTAMENTO DE CIENCIAS COMPUTACIONALES
ESTRUCTURA DE DATOS 

MIGUEL CABRERA 
31/05/2023
9898

"""


# Ejercicio 3: Crea una Cola que permita almacenar números enteros y realiza las operaciones de encolar y desencolar.

class Cola:
    def __init__(self):
        self.elementos = []  #Aqui asiganamos que la cola guardara sus datos dentro de una lista

    def encolar(self,elemento):
        self.elementos.append(elemento) #aqui ingresamos los valores que desee el usuario en la lista en la ultima posicion
    
    def desencolar(self):
        if self.vacia():        #Verificamos que la lisat dentro de la cola tenga datos para poder continuar
            return self.elementos.pop(0)  #aqui eliminamos el valor de la lista de la primera posicion 0.
    
    def vacia(self):
        return len(self.elementos) == 0 #Verifica si tiene elementos al contavilizar y comparar si es igual a 0
    
#Realizamos operaciones

cola = Cola()

cola.encolar(1)
cola.encolar(5)
cola.encolar(4)
cola.encolar(3)

cola.desencolar()
print(cola.elementos)

cola.encolar(10)
print(cola.elementos)

