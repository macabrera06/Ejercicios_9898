
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



# Algoritmo de Quicksort:

def quicksort(elementos):
    if len(elementos) <= 1:  # Si la lista tiene 1 elemento o menos, está ordenada
        return elementos
    else:
        pivot = elementos[0]  # Selecciona el primer elemento como pivote
        less = [x for x in elementos[1:] if x <= pivot]  # Crea una lista con los elementos menores o iguales al pivote
        greater = [x for x in elementos[1:] if x > pivot]  # Crea una lista con los elementos mayores al pivote
        return quicksort(less) + [pivot] + quicksort(greater)  # Aplica Quicksort recursivamente en las sublistas

# Ejemplo de uso:
numeros = [5, 2, 9, 1, 7, 6, 3]
numeros2 = quicksort(numeros)  # Ordena la lista utilizando Quicksort
print(numeros2)  # Imprime la lista ordenada

#algoritmo shellsort

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Establece el tamaño inicial del gap

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Desplaza los elementos que son mayores que temp hacia la derecha
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2  # Reduce el tamaño del gap

# Ejemplo de uso:
arr = [5, 2, 9, 1, 7, 6, 3]
shell_sort(arr)
print(arr)



#algoritmo de ratix

def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Cuenta la frecuencia de ocurrencia de cada dígito en la posición "exp"
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Calcula las posiciones finales de cada dígito
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construye el arreglo de salida en orden
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copia el arreglo de salida al arreglo original
    for i in range(n):
        arr[i] = output[i]


def radixSort(arr):
    max_value = max(arr)  # Encuentra el valor máximo en el arreglo

    # Realiza el ordenamiento para cada dígito, comenzando desde el dígito menos significativo
    exp = 1
    while max_value // exp > 0:
        countingSort(arr, exp)
        exp *= 10


# Ejemplo de uso:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
print(arr)









