# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Pokédex
- Por qué lo elegimos:

Elegimos la Pokédex porque es un tema conocido y fácil de entender.
Nos permite representar cada Pokémon mediante datos simples.
Cada Pokémon puede tener un número, un nombre y un tipo.
También permite aplicar más adelante búsquedas y ordenamientos.
Las evoluciones servirán para trabajar con recursión.
El equipo Pokémon permitirá practicar las estructuras de datos de la materia.

## 2. Modelo

Un ítem del catálogo representa un Pokémon y se modela con la clase `Pokemon` (`src/dominio/pokemon.py`).
Cada `Pokemon` guarda su id, nombre, tipo, ataque, hp y velocidad.
El catálogo es la clase `Pokedex` (`src/dominio/pokedex.py`): guarda los objetos `Pokemon` en una lista de Python y las evoluciones en un diccionario (id de un Pokémon → id de su evolución siguiente).
Los datos se cargan a mano en `cargar_datos_iniciales()`, con filas reales de `data/pokedex.txt` y `data/evoluciones.txt`. Esos archivos se leerán recién en E5.
El equipo (clase `Equipo`, máximo 6 Pokémon) es la colección principal. La pila y la cola se implementarán en E3.

Mutable e inmutable en nuestro modelo:

| Objeto | Tipo en Python | ¿Mutable? | Por qué |
| --- | --- | --- | --- |
| `Pokemon` | objeto de una clase propia | Sí | sus atributos se pueden reasignar (por ejemplo, el hp) |
| `self.pokemons` | `list` | Sí | se pueden agregar y quitar Pokémon |
| `self.evoluciones` | `dict` | Sí | se pueden agregar o cambiar relaciones |
| id, ataque, hp, velocidad | `int` | No | un número no cambia: reasignar el atributo lo hace apuntar a otro valor |
| nombre, tipo | `str` | No | un texto no se modifica internamente |

Por convención, el id de un Pokémon no se modifica una vez creado.

## 3. Recursión (E2)

- Función: `cadena_evolucion(pokedex, id_pokemon)` en `src/dominio/pokedex.py`. Devuelve la lista de ids de la cadena de evoluciones hacia adelante.
- Caso base: hay dos. Si el Pokémon no existe, devuelve `[]`. Si no tiene evolución siguiente, devuelve `[id_pokemon]`.
- Caso recursivo: `[id_pokemon] + cadena_evolucion(pokedex, siguiente)`, donde `siguiente` es el id de su evolución.
- Traza de un ejemplo real del dataset: Pichu (172). Según `evoluciones.txt`, 172 → 25 → 26.

```text
Llamada 1: cadena_evolucion(172) → existe, siguiente = 25
           → devuelve [172] + cadena_evolucion(25)
Llamada 2: cadena_evolucion(25)  → existe, siguiente = 26
           → devuelve [25] + cadena_evolucion(26)
Llamada 3: cadena_evolucion(26)  → existe, NO tiene siguiente (caso base)
           → devuelve [26]

Se desapila:
  la llamada 2 devuelve [25] + [26] = [25, 26]
  la llamada 1 devuelve [172] + [25, 26] = [172, 25, 26]

Resultado: [172, 25, 26] → Pichu → Pikachu → Raichu
```

Con un Pokémon sin evolución siguiente, por ejemplo Charizard (6), hay una sola llamada: `cadena_evolucion(6)` cae en el caso base y devuelve `[6]`. Con un id que no existe, por ejemplo 999, devuelve `[]`.

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | agregar, eliminar, buscar, recorrer, longitud | La cantidad de nodos internos siempre coincide con el tamaño reportado. |
| Pila | apilar (push), desapilar (pop), tope (peek), esta_vacia | El último elemento en entrar es el primero en salir (LIFO). |
| Cola | encolar (enqueue), desencolar (dequeue), frente (front), esta_vacia | El primer elemento en entrar es el primero en salir (FIFO). |

**Dónde se usa cada uno en el dominio:**
*   **ListaEnlazada:** Se utilizará para manejar el equipo Pokémon (colección principal), permitiendo agregar y quitar Pokémon dinámicamente.
*   **Pila:** Se utilizará para el historial de acciones (por ejemplo, para poder "deshacer" la última búsqueda o captura).
*   **Cola:** Se utilizará para gestionar turnos de combate o una cola de espera de acciones.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Búsqueda Lineal | O(n) | O(1) | Recorre el arreglo elemento por elemento hasta encontrar la clave. No usa memoria extra. |
| Búsqueda Binaria | O(log n) | O(1) | Divide el espacio de búsqueda a la mitad en cada paso. Requiere que el arreglo esté ordenado. |
| Ordenamiento (Selección/Inserción) | O(n²) | O(1) | Utilizan dos bucles anidados para comparar e insertar. No requieren memoria auxiliar. |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
| Búsqueda Lineal (peor caso: clave no encontrada) | 12 | 0.00000450 |
| Búsqueda Lineal (peor caso: clave no encontrada) | 12000 | 0.00042487 |

**Análisis de los resultados:** Los datos empíricos confirman la teoría. Al multiplicar el tamaño de la colección por 1000 (de 12 a 12000), el tiempo de ejecución de la búsqueda lineal aumentó drásticamente, demostrando su comportamiento lineal O(n). La búsqueda binaria, al ser O(log n), se espera que casi no sufra variaciones con este aumento de tamaño (se completará en la próxima entrega con las mediciones de mi compañero).

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
