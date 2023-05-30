"""
UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE
DEPARTAMENTO DE CIENCIAS DE LA COMPUTACION
ESTRUCTURA DE DATOS

Nombre: Miguel Cabrera
NRC: 9898
Fecha de entrega: 30-05-2023

Tarea sobre Listas, Pilas y Colas
"""


#EJERCICIO 1: Verificar si una lista está ordenada de forma ascendente

def ordenadaCorrectamente(lista):     

    for i in range(len(lista) - 1):                                # Si el bucle se completa sin retornar False, la lista está ordenada.

        if lista[i] > lista[i + 1]:
            return False
    return True     


#Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
print(ordenadaCorrectamente(mi_lista))



#EJERCICIO 2: Implementar una pila utilizando una lista


class Pila:
    def __init__(self):
        self.items = []  # Almacenamos los elementos de la pila
    
    def vacia(self):
        return len(self.items) == 0  # Verifica si la pila está vacía
    
    def insertar(self, elemento):
        self.items.append(elemento)  # Añade un elemento al final de la lista
    
    def eliminar(self):
        if self.vacia():
            return None  # Si la pila está vacía, retorna None
        return self.items.pop()  # Retira el elemento del final de la lista y lo retorna

# Ejemplo de uso:
pila = Pila()
pila.insertar(1)
pila.insertar(2)
pila.insertar(3)

while not pila.vacia():
    numero = pila.eliminar()
    print(numero)  


#EJERCICIO 3: Verificar si una palabra es un palíndromo utilizando una pila


# Utilizamos la clase pila del ejercicio 2

def es_palindromo(palabra):
    pila = Pila()
    for letra in palabra:
        pila.insertar(letra)  # Apila cada letra de la palabra
    
    palabra_invertida = ""
    while not pila.vacia():
        letra = pila.eliminar()  # Elimina cada letra de la pila
        palabra_invertida += letra  # Concatena las letras para formar la palabra invertida
    
    return palabra == palabra_invertida  # Compara la palabra original con la invertida

# Ejemplo de uso:
palabra = "oso"
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")

palabra = "palabrita"
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")




#EJERCICIO 4:  Implementar una cola utilizando una lista

class Cola:
    def __init__(self):
        self.items = []  # Lista para almacenar los elementos de la cola
    
    def vacia(self):
        return len(self.items) == 0  # Verifica si la cola está vacía
    
    def insertar(self, elemento):
        self.items.append(elemento)  # Añade un elemento al final de la lista
    
    def eliminar(self):
        if self.vacia():
            return None  # Si la cola está vacía, retorna None
        return self.items.pop(0)  # Retira el elemento del inicio de la lista y lo retorna

# Ejemplo de uso:
cola = Cola()
cola.insertar(1)
cola.insertar(2)
cola.insertar(3)

while not cola.vacia():
    elemento = cola.eliminar()
    print(elemento)  




#EJERCICIO 5: Verificar si una lista es simétrica

def es_simetrica(lista):
    pila = Pila()
    longitud = len(lista)
    mitad = longitud // 2

    # Apila los elementos de la primera mitad de la lista
    for i in range(mitad):
        pila.insertar(lista[i])

    # Compara los elementos de la segunda mitad de la lista con los desapilados
    # de la pila en orden inverso
    for i in range(mitad, longitud):
        elemento_pila = pila.eliminar()

        if elemento_pila != lista[i]:
            return False

    return True

# Ejemplo de uso:
lista3 = [1, 2, 3, 2, 1]
if es_simetrica(lista3):
    print("La lista es simétrica.")
else:
    print("La lista no es simétrica.")

lista4 = [1, 2, 3, 4, 5]
if es_simetrica(lista4):
    print("La lista es simétrica.")
else:
    print("La lista no es simétrica.")
