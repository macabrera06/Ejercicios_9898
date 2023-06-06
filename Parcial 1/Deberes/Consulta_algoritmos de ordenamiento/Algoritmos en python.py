
#algoritmo de burbuja

def burbuja(elementos):
    Intercambio = True                      #Dejamos el boolean en true para acceder almenos una vez dentro del bucle
    while Intercambio:
        Intercambio = False                 #Cambiamos a false para que de hacer un intercambio cambie el valor y de no ser asi termine el bucle.
        for i in range(len(elementos) - 1):
            if elementos[i] >elementos[i+1]:
                elementos[i], elementos[i + 1] = elementos[i + 1], elementos[i] #intercambia posicion de las variables una con otra.
                Intercambio = True

#comprobamos que funcione
Lista = [5,4,9,3,2,7,11,6]
burbuja(Lista)
print(Lista)



#algoritmo de Quicksort:

def division(elementos, low, high):
    i = low - 1
    pivot = elementos[high]
  
    for j in range(low, high):
        if elementos[j] < pivot:
            i += 1
            # Intercambiar los elementos de la lista en [i+1] y [high]
            elementos[i], elementos[j] = elementos[j], elementos[i]
  
    # Intercambiar los elementos de la lista en [i+1] y [high]
    elementos[i+1], elementos[high] = elementos[high], elementos[i+1]
  
    return i+1
  
def quick_sort(elementos, low, high):
    if low < high:
        pi = division(elementos, low, high)
  
        quick_sort(elementos, low, pi-1)
        quick_sort(elementos, pi+1, high)

Lista = [5,4,9,3,2,7,11,6]
quick_sort(Lista, )
print(Lista)