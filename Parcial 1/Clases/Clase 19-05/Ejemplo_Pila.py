pila = []

pila.append(10) # Insertar elemento 10 en la pila
pila.append(20) # Insertar elemento 20 en la pila
pila.append(30) # Insertar elemento 30 en la pila

while len(pila) > 0:
    print(pila[-1], end=" ") # Imprimir elemento superior de la pila
    pila.pop() # Eliminar elemento superior de la pila