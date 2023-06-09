# implementaremos la busqueda binaria en python. La busqueda binaria es un algoritmo eficiente para encontrar
# un elemento especifico en una lista ordenada.

def ordenamientoBinario(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def bubble_sot(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Ejemplo de uso

lista = [1,5,8,6,2,7,9,8,2,6,2,1,6,6,5]
target = 4

bubble_sot(lista)
print(lista)

resultado = ordenamientoBinario(lista,target)

if resultado != -1:
    print("El elemento", target, "se encuentra en la posición", resultado)
else:
    print("El elemento", target, "no se encontró en el arreglo.")


