public class Listas {
    public class Nodo {
        int valor;
        Nodo siguiente;
    
        public Nodo(int valor) {
            this.valor = valor;
            this.siguiente = null;
        }
    }
    
    public class ListaEnlazada {
        Nodo cabeza;
        int tamaño;
    
        public ListaEnlazada() {
            this.cabeza = null;
            this.tamaño = 0;
        }
    
        public void agregar(int valor) {
            Nodo nuevoNodo = new Nodo(valor);
            if (cabeza == null) {
                cabeza = nuevoNodo;
            } else {
                Nodo nodoActual = cabeza;
                while (nodoActual.siguiente != null) {
                    nodoActual = nodoActual.siguiente;
                }
                nodoActual.siguiente = nuevoNodo;
            }
            tamaño++;
        }
    
        public void imprimir() {
            Nodo nodoActual = cabeza;
            while (nodoActual != null) {
                System.out.print(nodoActual.valor + " ");
                nodoActual = nodoActual.siguiente;
            }
            System.out.println();
        }
    }
}
