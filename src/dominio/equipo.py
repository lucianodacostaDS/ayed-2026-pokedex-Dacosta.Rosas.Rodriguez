from src.excepciones import ColeccionLlenaError


class Equipo:
    TOPE = 6

    def __init__(self):
        self.pokemons = []

    def agregar(self, pokemon):
        if len(self.pokemons) >= self.TOPE:
            raise ColeccionLlenaError(f"El equipo ya tiene {self.TOPE} Pokémon.")
        self.pokemons.append(pokemon)

    def listar(self):
        for pokemon in self.pokemons:
            print(pokemon.resumen())