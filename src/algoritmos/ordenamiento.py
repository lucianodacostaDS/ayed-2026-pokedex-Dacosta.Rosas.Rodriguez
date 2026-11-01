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
    """Ordenamiento por inserción. Devuelve una nueva secuencia, no usa sorted."""
    raise NotImplementedError
