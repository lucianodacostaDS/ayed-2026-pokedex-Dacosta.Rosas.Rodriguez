"""Catálogo manual de Pokémon para la Entrega 1."""

CATALOGO = [
    {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno"}, #{} Diccionario que contiene 3 datos str""
    {"id": 2, "nombre": "Ivysaur", "tipo": "Planta/Veneno"},
    {"id": 3, "nombre": "Venusaur", "tipo": "Planta/Veneno"},
    {"id": 4, "nombre": "Charmander", "tipo": "Fuego"},
    {"id": 5, "nombre": "Charmeleon", "tipo": "Fuego"},
    {"id": 6, "nombre": "Charizard", "tipo": "Fuego/Volador"},
    {"id": 7, "nombre": "Squirtle", "tipo": "Agua"},
    {"id": 8, "nombre": "Wartortle", "tipo": "Agua"},
    {"id": 9, "nombre": "Blastoise", "tipo": "Agua"},
    {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico"},
] #CATALOGO es una lista donde agregamos todos los pokemon


def listar_catalogo():#Funcion
    """Muestra todos los Pokémon guardados en el catálogo."""
    print("\n--- Catálogo de Pokémon ---")

    for pokemon in CATALOGO: #Recorre cada pokemon de la lista (CATALOGO)
        print(pokemon["id"], "-", pokemon["nombre"], "-", pokemon["tipo"])