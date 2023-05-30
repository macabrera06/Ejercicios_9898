import java.util.Stack;

    public class Ejemplo_Pila {
    public static void main(String[] args) {

    Stack<Integer> pila = new Stack<>();

    pila.push(10); // Insertar elemento 10 en la pila
    pila.push(20); // Insertar elemento 20 en la pila
    pila.push(30); // Insertar elemento 30 en la pila

    while (!pila.empty()) {
        System.out.print(pila.peek() + " "); // Imprimir elemento superior de la pila
        pila.pop(); // Eliminar elemento superior de la pila
        }
    }
}