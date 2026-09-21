from src.config import TEMA
from src.dominio.pokedex import Pokedex, cadena_evolucion

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
        elif opcion == "5":
            mostrar_cadena_evolucion(dex)
        elif opcion in {"3", "4", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
