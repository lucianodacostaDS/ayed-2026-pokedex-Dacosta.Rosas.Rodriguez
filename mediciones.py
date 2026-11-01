import time
import random
import copy
from src.dominio.pokedex import Pokedex
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion

def medir_tiempo(funcion_busqueda, coleccion, clave, obtener_clave, repeticiones=1000):
    inicio = time.perf_counter()
    for _ in range(repeticiones):
        funcion_busqueda(coleccion, clave, obtener_clave)
    fin = time.perf_counter()

    return (fin - inicio) / repeticiones

def medir_ordenamiento(funcion_orden, coleccion, clave, repeticiones=5):
    # Las funciones devuelven una copia ordenada, así que cada repetición
    # arranca con la colección desordenada.
    inicio = time.perf_counter()
    for _ in range(repeticiones):
        funcion_orden(coleccion, clave)
    fin = time.perf_counter()

    return (fin - inicio) / repeticiones

def main():
    print("=== INICIANDO MEDICIONES DE RENDIMIENTO ===")

    dex = Pokedex()
    dex.cargar_datos_iniciales()
    coleccion_original = dex.pokemons

    coleccion_agrandada = copy.deepcopy(coleccion_original * 1000)

    clave_buscar = -1
    obtener_id = lambda p: p.id

    print(f"Tamaño colección original: {len(coleccion_original)} elementos.")
    print(f"Tamaño colección agrandada: {len(coleccion_agrandada)} elementos.")
    print("-" * 50)

    print("Midiendo Búsqueda Lineal (peor caso)...")

    tiempo_lineal_orig = medir_tiempo(busqueda_lineal, coleccion_original, clave_buscar, obtener_id, repeticiones=10000)
    print(f"Lineal (Original) : {tiempo_lineal_orig:.8f} segundos")

    tiempo_lineal_agrandada = medir_tiempo(busqueda_lineal, coleccion_agrandada, clave_buscar, obtener_id, repeticiones=10000)
    print(f"Lineal (Agrandada): {tiempo_lineal_agrandada:.8f} segundos")

    print("-" * 50)
    print("Midiendo Búsqueda Binaria (peor caso)...")

    # La binaria necesita la colección ordenada por id. El catálogo original
    # ya lo está; la agrandada se arma repitiendo cada Pokémon 1000 veces
    # seguidas, así queda ordenada por id sin usar sorted().
    agrandada_ordenada = [p for p in coleccion_original for _ in range(1000)]

    tiempo_binaria_orig = medir_tiempo(busqueda_binaria, coleccion_original, clave_buscar, obtener_id, repeticiones=10000)
    print(f"Binaria (Original) : {tiempo_binaria_orig:.8f} segundos")

    tiempo_binaria_agrandada = medir_tiempo(busqueda_binaria, agrandada_ordenada, clave_buscar, obtener_id, repeticiones=10000)
    print(f"Binaria (Agrandada): {tiempo_binaria_agrandada:.8f} segundos")

    print("-" * 50)
    print("Midiendo ordenamientos por nombre...")

    # Los ordenamientos son O(n²): con 12000 tardarían minutos, por eso se
    # miden con 12, 120 y 1200 Pokémon (el catálogo repetido x1, x10 y x100).
    por_nombre = lambda p: p.nombre.lower()
    for factor in (1, 10, 100):
        datos = coleccion_original * factor
        t_sel = medir_ordenamiento(ordenar_seleccion, datos, por_nombre)
        t_ins = medir_ordenamiento(ordenar_insercion, datos, por_nombre)
        print(f"n = {len(datos):5d} | Selección: {t_sel:.8f} s | Inserción: {t_ins:.8f} s")

    print("-" * 50)
    print("¡Mediciones terminadas!")

if __name__ == "__main__":
    main()
