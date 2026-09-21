# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID  | Entrega | Acción (pasos en el CLI)                                            | Datos                                | Resultado esperado                                                                   | Resultado     | Notas |
| --- | ------- | ------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------ | ------------- | ----- |
| P01 | E1      | Ejecutar `py -3 -m src.main` y elegir la opción 1 (Listar catálogo) | catálogo cargado a mano (12 Pokémon) | lista no vacía con los 12 Pokémon, sin errores                                       | `no corrido`  |       |
| P02 | E1      | Elegir la opción 2 (Ver detalle) e ingresar el id -1                | id = -1                              | mensaje claro de que no existe ese Pokémon; el menú vuelve a mostrarse               | `no corrido`  |       |
| P03 | E2      | Elegir la opción 5 (Operación recursiva) e ingresar el id 172       | Pichu (172), cadena 172 → 25 → 26    | muestra la cadena Pichu → Pikachu → Raichu (ids 172, 25, 26)                         | `no corrido`  |       |
| P04 | E2      | Elegir la opción 5 (Operación recursiva) e ingresar el id 6         | Charizard (6), última evolución      | muestra solo Charizard (caso base)                                                   | `no corrido`  |       |
| P05 | E3      | Agregar a la colección principal hasta el tope                      | equipo de 6 / equivalente            | el séptimo falla con excepción propia                                                | `no corrido`. |       |
| P06 | E3      | Desapilar historial vacío                                           | pila vacía                           | excepción propia, menú sigue                                                         | `no corrido`. |       |
| P07 | E3      | Desencolar cola vacía                                               | cola vacía                           | excepción propia, menú sigue                                                         | `no corrido`. |       |
| P08 | E3      | Listar colección con el iterador                                    | 2+ ítems                             | el orden coincide con las inserciones                                                | `no corrido`. |       |
| P09 | E4      | Búsqueda lineal de un nombre que existe                             |                                      | lo encuentra                                                                         | `no corrido`. |       |
| P10 | E4      | Búsqueda lineal de un nombre que no existe                          |                                      | no encontrado, sin traceback                                                         | `no corrido`. |       |
| P11 | E4      | Búsqueda binaria con catálogo desordenado                           |                                      | avisa o reordena; no da un falso hit                                                 | `no corrido`. |       |
| P12 | E4      | Ordenar por un criterio y después por otro                          |                                      | el orden cambia                                                                      | `no corrido`. |       |
| P13 | E5      | Guardar texto (`.txt`), salir, volver a entrar                      |                                      | los datos siguen                                                                     | `no corrido`. |       |
| P14 | E5      | Guardar binario y modificar un registro por id                      |                                      | al recargar, ese campo cambió                                                        | `no corrido`. |       |
| P15 | E5      | Abrir un binario truncado o con magia mala                          | archivo basura                       | excepción de archivo inválido                                                        | `no corrido`. |       |
| P16 | E2      | Elegir la opción 2 (Ver detalle) e ingresar el id 25                | Pikachu (25)                         | muestra los datos de Pikachu: nombre, tipo, ataque, hp y velocidad                   | `no corrido`  |       |
| P17 | E2      | Elegir la opción 2 (Ver detalle) e ingresar el id 999               | id = 999 (no está en el catálogo)    | mensaje claro de que no existe; el programa no se corta y el menú vuelve a mostrarse | `no corrido`  |       |
| P18 | E2      | En el menú principal escribir `9z` y apretar Enter                  | opción = `9z`                        | muestra "Opción inválida." y vuelve a mostrar el menú                                | `no corrido`  |       |
| P19 | E2      | En el menú principal apretar Enter sin escribir nada                | opción vacía                         | no falla; muestra "Opción inválida." y vuelve a preguntar                            | `no corrido`  |       |
