def bubble_sot(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


lista = [1,2,3,4,5,6,4,8,9,1,0,8,7,4,5]

bubble_sot(lista)

print(lista)