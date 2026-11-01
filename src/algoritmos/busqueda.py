def busqueda_lineal(coleccion, clave, obtener_clave):
    for item in coleccion:
        if obtener_clave(item) == clave:
            return item
    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):

    izquierda = 0
    derecha = len(coleccion_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        item_medio = coleccion_ordenada[medio]
        clave_medio = obtener_clave(item_medio)

        if clave_medio == clave:
            return item_medio
        elif clave_medio < clave:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None