from src.config import TEMA
from src.dominio.pokedex import Pokedex, cadena_evolucion
from src.algoritmos.busqueda import busqueda_binaria, busqueda_lineal
from src.algoritmos.ordenamiento import ordenar_insercion, ordenar_seleccion

# Funciones "clave": le dicen a los algoritmos qué mirar de cada Pokémon.
# El nombre se compara en minúsculas para que "pikachu" y "Pikachu" sean iguales.
POR_NOMBRE = lambda p: p.nombre.lower()
POR_HP = lambda p: p.hp

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def pedir_id():
    texto = input("Id del Pokémon: ").strip()
    try:
        return int(texto)
    except ValueError:
        print("Ingresá un número entero.")
        return None


def listar_catalogo(dex):
    print("\n--- Catálogo de Pokémon ---")
    dex.listar()


def ver_detalle(dex):
    id_pokemon = pedir_id()
    if id_pokemon is None:
        return
    pokemon = dex.buscar(id_pokemon)
    if pokemon is None:
        print(f"No existe un Pokémon con id {id_pokemon}.")
    else:
        print(pokemon.resumen())

def buscar_pokemon(dex):
    print("\n--- Buscar Pokémon ---")
    print("1. Buscar por ID (lineal)")
    print("2. Buscar por Nombre (lineal)")
    print("3. Buscar por Nombre (binaria)")
    criterio = input("> ").strip()

    if criterio == "1":
        id_pokemon = pedir_id()
        if id_pokemon is None:
            return
        resultado = busqueda_lineal(dex.pokemons, id_pokemon, lambda p: p.id)
    elif criterio == "2":
        nombre = input("Nombre del Pokémon: ").strip().capitalize()
        resultado = busqueda_lineal(dex.pokemons, nombre, lambda p: p.nombre)
    elif criterio == "3":
        nombre = input("Nombre del Pokémon: ").strip().lower()
        # La binaria solo funciona si la lista está ordenada por lo que se busca.
        # El catálogo está ordenado por id, así que primero se ordena una copia
        # por nombre (inserción). Así nunca da un falso "no encontrado".
        print("Ordenando el catálogo por nombre para usar búsqueda binaria...")
        ordenados = ordenar_insercion(dex.pokemons, POR_NOMBRE)
        resultado = busqueda_binaria(ordenados, nombre, POR_NOMBRE)
    else:
        print("Opción inválida.")
        return

    if resultado is None:
        print("No se encontró ningún Pokémon con ese criterio.")
    else:
        print("¡Encontrado!")
        print(resultado.resumen())

def ordenar_catalogo(dex):
    print("\n--- Ordenar catálogo ---")
    print("Ordenar por: 1. Nombre  2. HP")
    criterio = input("> ").strip()
    if criterio == "1":
        clave, nombre_criterio = POR_NOMBRE, "nombre"
    elif criterio == "2":
        clave, nombre_criterio = POR_HP, "hp"
    else:
        print("Opción inválida.")
        return

    print("Algoritmo: 1. Selección  2. Inserción")
    algoritmo = input("> ").strip()
    if algoritmo == "1":
        dex.pokemons = ordenar_seleccion(dex.pokemons, clave)
        nombre_algoritmo = "selección"
    elif algoritmo == "2":
        dex.pokemons = ordenar_insercion(dex.pokemons, clave)
        nombre_algoritmo = "inserción"
    else:
        print("Opción inválida.")
        return

    print(f"Catálogo ordenado por {nombre_criterio} ({nombre_algoritmo}):")
    dex.listar()


def mostrar_cadena_evolucion(dex):
    id_pokemon = pedir_id()
    if id_pokemon is None:
        return
    cadena = cadena_evolucion(dex, id_pokemon)
    if not cadena:
        print(f"No existe un Pokémon con id {id_pokemon}.")
        return
    nombres = []
    for id_en_cadena in cadena:
        nombres.append(dex.buscar(id_en_cadena).nombre)
    print(" → ".join(nombres))


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    dex = Pokedex()
    dex.cargar_datos_iniciales()

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            listar_catalogo(dex)
        elif opcion == "2":
            ver_detalle(dex)
        elif opcion == "3":
            buscar_pokemon(dex)
        elif opcion == "4":
            ordenar_catalogo(dex)
        elif opcion == "5":
            mostrar_cadena_evolucion(dex)
        elif opcion in {"6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
