import time
import random
import copy
from src.dominio.pokedex import Pokedex
from src.algoritmos.busqueda import busqueda_lineal

def medir_tiempo(funcion_busqueda, coleccion, clave, obtener_clave, repeticiones=1000):
    inicio = time.perf_counter()
    for _ in range(repeticiones):
        funcion_busqueda(coleccion, clave, obtener_clave)
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
    print("¡Mediciones terminadas!")

if __name__ == "__main__":
    main()