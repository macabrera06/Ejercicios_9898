import java.util.Arrays;

public class RadixSort {
    public static void radixSort(int[] arr) {
        int max = getMax(arr); // Obtiene el valor máximo en el arreglo

        // Realiza el ordenamiento para cada dígito, comenzando desde el dígito menos significativo
        for (int exp = 1; max / exp > 0; exp *= 10) {
            countingSort(arr, exp);
        }
    }

    public static void countingSort(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10];

        // Cuenta la frecuencia de ocurrencia de cada dígito en la posición "exp"
        for (int i = 0; i < n; i++) {
            int index = arr[i] / exp % 10;
            count[index]++;
        }

        // Calcula las posiciones finales de cada dígito
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        // Construye el arreglo de salida en orden
        for (int i = n - 1; i >= 0; i--) {
            int index = arr[i] / exp % 10;
            output[count[index] - 1] = arr[i];
            count[index]--;
        }

        // Copia el arreglo de salida al arreglo original
        System.arraycopy(output, 0, arr, 0, n);
    }

    public static int getMax(int[] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }

    // Ejemplo de uso:
    public static void main(String[] args) {
        int[] arr = {170, 45, 75, 90, 802, 24, 2, 66};
        radixSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
