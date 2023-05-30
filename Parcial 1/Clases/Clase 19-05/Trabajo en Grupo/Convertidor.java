/* UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE
    DEPARTAMENTO DE CIENCIAS DE LAS COMPITACION
    ESTRUCTURA DE DATOS

    MIGUEL CABRERA, PAUL JARAMILLO Y GABRIEL REVELO
    9898
    19/05/2023

    EJERCICIOS DE PILAS

    2. CONVERTIR UN NUMERO DECIMAL A BINARIO
*/ 

import java.util.Stack;

public class Convertidor {

    public static void decimalABinario(int numero) {
        // Se crea una instancia de la clase Stack para almacenar los residuos
        Stack<Integer> pila = new Stack<>();

        // Se realiza la conversión del número decimal a binario mediante divisiones sucesivas
        while (numero > 0) {
            int residuo = numero % 2;
            // El residuo se agrega a la pila
            pila.push(residuo);
            // El número se divide por 2 para continuar con la siguiente división
            numero /= 2;
        }

        // Se imprime el mensaje inicial
        System.out.print("El número binario es: ");

        // Se desapila y se imprime cada elemento hasta que la pila esté vacía
        while (!pila.empty()) {
            System.out.print(pila.pop());
        }
    }

    public static void main(String[] args) {
        // Se define el número decimal a convertir
        int decimal = 27;

        // Se llama al método decimalABinario pasando el número decimal como argumento
        decimalABinario(decimal);
    }
}

