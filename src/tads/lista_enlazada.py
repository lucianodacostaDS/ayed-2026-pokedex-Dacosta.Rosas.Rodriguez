from src.tads.nodo import Nodo

class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""

    def __init__(self):
        self.cabeza= None
        self.cantidad= 0

    def esta_vacia(self):
        if self.cabeza is None:
            return True
        else:
            return False

    def tamanio(self):
        return self.cantidad

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cantidad += 1
            return

        aux = self.cabeza
        self.cabeza = nuevo_nodo
        nuevo_nodo.siguiente = aux       
        self.cantidad += 1    

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
    
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cantidad += 1
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        self.cantidad += 1  

    def insertar_ordenado(self, dato, clave):
        raise NotImplementedError

    def eliminar(self, dato):
        raise NotImplementedError

    def buscar(self, dato):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
