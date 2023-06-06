public class QuickSort {
    public static void quicksort(int[] arr, int low, int high) {
        if (low < high) {
            int pivot = partition(arr, low, high); // Encuentra el índice del pivote
            quicksort(arr, low, pivot - 1); // Ordena recursivamente los elementos antes del pivote
            quicksort(arr, pivot + 1, high); // Ordena recursivamente los elementos después del pivote
        }
    }
    
    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high]; // Elige el último elemento como pivote
        int i = low - 1; // Índice del elemento más pequeño
        
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) { // Si el elemento actual es menor o igual al pivote
                i++; // Incrementa el índice del elemento más pequeño
                swap(arr, i, j); // Intercambia arr[i] y arr[j]
            }
        }
        
        swap(arr, i + 1, high); // Intercambia el pivote con el elemento en la posición correcta
        return i + 1; // Retorna la posición del pivote
    }
    
    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    // Ejemplo de uso:
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 7, 6, 3};
        quicksort(arr, 0, arr.length - 1); // Llama a la función quicksort para ordenar el arreglo
        
        for (int num : arr) {
            System.out.print(num + " "); // Imprime el arreglo ordenado
        }
    }
}


