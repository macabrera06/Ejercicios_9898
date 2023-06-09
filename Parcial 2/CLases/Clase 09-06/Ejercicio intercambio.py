"""
Ejercicio de práctica:

Implementaremos el algoritmo de ordenación por intercambio en Python utilizando
una función llamada exchange_sort. Además, solicitaremos al usuario que ingrese
una lista de números y ordenaremos esa lista utilizando el algoritmo de intercambio.
"""


def binario(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

# Ejemplo de uso

numero = input("Ingresa una lista de números separados por espacios: ").split()
numero = [int(num) for num in numero]

binario(numero)

print("Lista ordenada:")
print(numero)



