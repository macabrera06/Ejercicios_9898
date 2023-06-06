

public class Burbuja {
    public static void burbuja(int[] elementos) {
        int n = elementos.length;
        // Iterar a través del arreglo n - 1 veces
        for (int i = 0; i < n - 1; i++) {
            // Iterar a través de los elementos no ordenados
            for (int j = 0; j < n - i - 1; j++) {
                // Comparar elementos adyacentes y realizar un intercambio si es necesario
                if (elementos[j] > elementos[j + 1]) {
                    int temp = elementos[j];
                    elementos[j] = elementos[j + 1];
                    elementos[j + 1] = temp;
                }
            }
        }
    }

    // Ejemplo de uso
    public static void main(String[] args) {
        int[] numeros = {64, 34, 25, 12, 22, 11, 90};
        burbuja(numeros);                           // Ordenar el arreglo utilizando el método burbuja
        System.out.println("Arreglo ordenado:"); // Imprimir el arreglo ordenado
        for (int i = 0; i < numeros.length; i++) {
            System.out.print(numeros[i] + " ");
        }
    }
}

