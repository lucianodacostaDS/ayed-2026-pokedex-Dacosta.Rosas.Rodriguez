def ordenar_seleccion(coleccion, clave):
    copia_lista = coleccion[:]

    for i in range(len(copia_lista)):
        min_index = i
        for j in range(i + 1, len(copia_lista)):
            if clave(copia_lista[j]) < clave(copia_lista[min_index]):
                min_index = j
        copia_lista[i], copia_lista[min_index] = copia_lista[min_index], copia_lista[i]
    return copia_lista


def ordenar_insercion(coleccion, clave):
    """Ordenamiento por inserción. Devuelve una nueva secuencia, no usa sorted.

    Como ordenar cartas en la mano: toma cada elemento y lo corre hacia la
    izquierda hasta dejarlo detrás del primero que no sea más grande que él.
    La parte de la izquierda siempre queda ordenada.
    """
    copia_lista = coleccion[:]

    for i in range(1, len(copia_lista)):
        actual = copia_lista[i]          # el elemento que voy a ubicar
        j = i - 1                        # empiezo a comparar con el de su izquierda

        # Mientras el de la izquierda sea MÁS GRANDE, lo corro un lugar a la derecha.
        # Uso > (y no >=) para no pasar por encima de uno igual: eso lo hace estable.
        while j >= 0 and clave(copia_lista[j]) > clave(actual):
            copia_lista[j + 1] = copia_lista[j]
            j -= 1

        copia_lista[j + 1] = actual      # lo dejo en el hueco que quedó
    return copia_lista
