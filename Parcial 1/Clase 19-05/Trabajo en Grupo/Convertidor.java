import java.util.Stack;
public class Convertidor {
    public static void decimalABinario(int numero) {

        Stack<Integer> pila = new Stack<>();

        while (numero > 0) {
            int residuo = numero % 2;
            pila.push(residuo);
            numero /= 2;
        }

        System.out.print("El número binario es: ");

        while (!pila.empty()) {
                System.out.print(pila.pop());
        }
    }

    public static void main(String[] args) {

        int decimal = 27;
        
        decimalABinario(decimal);
    }
}
