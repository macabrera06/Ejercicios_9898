public class ShellSort {
    public static void shellSort(int[] arr) {
        int n = arr.length;
        int gap = n / 2; // Establece el tamaño inicial del gap

        while (gap > 0) {
            for (int i = gap; i < n; i++) {
                int temp = arr[i];
                int j = i;

                // Desplaza los elementos que son mayores que temp hacia la derecha
                while (j >= gap && arr[j - gap] > temp) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }

                arr[j] = temp;
            }

            gap /= 2; // Reduce el tamaño del gap
        }
    }

    // Ejemplo de uso:
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 7, 6, 3};
        shellSort(arr);

        for (int num : arr) {
            System.out.print(num + " "); // Imprime el arreglo ordenado
        }
    }
}
