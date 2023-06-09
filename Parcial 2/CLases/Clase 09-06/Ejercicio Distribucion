def distribution_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    count = [0] * range_val

    for num in arr:
        count[num - min_val] += 1

    output = []
    for i in range(range_val):
        output.extend([i + min_val] * count[i])

    return output

# Solicitar al usuario una lista de números
numbers = input("Ingresa una lista de números separados por espacios: ").split()
numbers = [int(num) for num in numbers]

# Ordenar la lista utilizando el algoritmo de Ordenación por Distribución
sorted_numbers = distribution_sort(numbers)

# Imprimir la lista ordenada
print("Lista ordenada:")
print(sorted_numbers)