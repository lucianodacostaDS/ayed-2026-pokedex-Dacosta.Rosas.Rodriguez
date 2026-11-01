from src.tads.lista_enlazada import ListaEnlazada

lista2 = ListaEnlazada()
lista2.insertar_al_final("Bulbasaur")
lista2.insertar_al_final("Charmander")
lista2.insertar_al_final("Squirtle")
print(lista2.cabeza.dato)                        # Bulbasaur
print(lista2.cabeza.siguiente.siguiente.dato)    # Squirtle
print(lista2.tamanio())                          # 3