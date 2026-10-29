def busqueda_lineal(coleccion, clave, obtener_clave):
    for item in coleccion:
        if obtener_clave(item) == clave:
            return item
    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """La colección tiene que estar ordenada por obtener_clave."""
    raise NotImplementedError
