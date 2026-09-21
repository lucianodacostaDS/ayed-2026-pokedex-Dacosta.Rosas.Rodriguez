from src.dominio.pokemon import Pokemon


class Pokedex:
    def __init__(self):
        self.pokemons = []
        self.evoluciones = {}

    def cargar_datos_iniciales(self):
        self.pokemons.append(Pokemon(1, "Bulbasaur", "Planta/Veneno", 49, 45, 45))
        self.pokemons.append(Pokemon(2, "Ivysaur", "Planta/Veneno", 62, 60, 60))
        self.pokemons.append(Pokemon(3, "Venusaur", "Planta/Veneno", 82, 80, 80))
        self.pokemons.append(Pokemon(4, "Charmander", "Fuego", 52, 39, 65))
        self.pokemons.append(Pokemon(5, "Charmeleon", "Fuego", 64, 58, 80))
        self.pokemons.append(Pokemon(6, "Charizard", "Fuego/Volador", 84, 78, 100))
        self.pokemons.append(Pokemon(7, "Squirtle", "Agua", 48, 44, 43))
        self.pokemons.append(Pokemon(8, "Wartortle", "Agua", 63, 59, 58))
        self.pokemons.append(Pokemon(9, "Blastoise", "Agua", 83, 79, 78))
        self.pokemons.append(Pokemon(25, "Pikachu", "Electrico", 55, 35, 90))
        self.pokemons.append(Pokemon(26, "Raichu", "Electrico", 90, 60, 110))
        self.pokemons.append(Pokemon(172, "Pichu", "Electrico", 40, 20, 60))

        # id de un Pokémon -> id de su evolución siguiente (filas de evoluciones.txt)
        self.evoluciones = {
            1: 2,
            2: 3,
            4: 5,
            5: 6,
            7: 8,
            8: 9,
            172: 25,
            25: 26,
        }

    def listar(self):
        for pokemon in self.pokemons:
            print(pokemon.resumen())

    def buscar(self, id_pokemon):
        for pokemon in self.pokemons:
            if pokemon.id == id_pokemon:
                return pokemon
        return None

    def siguiente_evolucion(self, id_pokemon):
        return self.evoluciones.get(id_pokemon)


def cadena_evolucion(pokedex, id_pokemon):
    pokemon = pokedex.buscar(id_pokemon)
    if pokemon is None:
        return []
    siguiente = pokedex.siguiente_evolucion(id_pokemon)
    if siguiente is None:
        return [id_pokemon]
    return [id_pokemon] + cadena_evolucion(pokedex, siguiente)