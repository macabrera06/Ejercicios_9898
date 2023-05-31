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
        self.elementos = []

    def encolar(self,elemento):
        self.elementos.append(elemento)
    
    def desencolar(self):
        if self.vacia():
            return self.elementos.pop(0)
    
    def vacia(self):
        return len(self.elementos) == 0
    
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