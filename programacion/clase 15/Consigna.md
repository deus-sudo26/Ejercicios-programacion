# Trabajo práctico: Sistema de gestión de Pokémon

**Programación I — Desarrollo progresivo por clases**

## Situación problemática

Ash Ketchum tiene una colección de 50 Pokémon. Necesita un programa de consola para consultar sus características, buscar Pokémon, conocer estadísticas de su colección, incorporar nuevos ejemplares y ordenarlos según su nivel.

Los datos se encuentran en **listas paralelas**: `nombres`, `tipos`, `niveles`, `puntos_salud`, `puntos_ataque` y `puntos_defensa`. Cada posición de las seis listas corresponde al mismo Pokémon. La lista de niveles comienza vacía.

## Etapa 1. Visualización

1. Crear una función que muestre una cabecera con los nombres de los campos.
2. Crear una función que reciba los datos de un Pokémon y los muestre en una fila.
3. Mostrar todos los Pokémon recorriendo las listas paralelas.
4. Mostrar únicamente los Pokémon de un tipo solicitado.

## Etapa 2. Cálculo de niveles

1. Desarrollar una función que calcule el promedio de una lista de puntajes.
2. Crear una función que determine el nivel a partir del promedio de salud, ataque y defensa.
3. Completar la lista `niveles` de los 50 Pokémon utilizando las funciones anteriores.

| Promedio | Nivel |
|---|---|
| Menor que 9 | 1 |
| Desde 9 y menor que 16 | 2 |
| Desde 16 hasta 20 inclusive | 3 |
| Mayor que 20 | 4 |

## Etapa 3. Búsquedas

1. **Por nombre:** buscar un Pokémon y devolver su índice; devolver `-1` si no existe. Mostrar sus datos desde el programa principal.
2. **Por tipo:** mostrar todos los Pokémon de un tipo indicado.
3. **Por nivel:** mostrar todos los Pokémon del nivel solicitado.
4. **Por rango de ataque:** mostrar los Pokémon cuyo ataque se encuentre entre dos valores, incluyendo los límites.
5. **Por tipo y nivel:** mostrar los Pokémon que cumplan ambas condiciones.
6. **Mayor ataque:** devolver el índice del primer Pokémon que tenga el ataque máximo.
7. **Menor salud:** devolver el índice del primer Pokémon que tenga la salud mínima.

## Etapa 4. Estadísticas

1. Contar los Pokémon de cada tipo disponible.
2. Mostrar el porcentaje que representa cada tipo sobre el total.
3. Contar los Pokémon de cada nivel (1 a 4).
4. Determinar el tipo más frecuente. Ante empate, considerar el primero de la lista de tipos disponibles.
5. Calcular el promedio de ataque de los Pokémon de un tipo solicitado. Si no existen coincidencias, informar la situación.

## Etapa 5. Incorporación de Pokémon

Crear `cargar_pokemon()` para que solicite directamente el nombre, tipo, puntos de salud, ataque y defensa de un Pokémon. Calcular el promedio de sus tres puntajes, determinar el nivel y agregar los seis datos a sus respectivas listas utilizando `append()`.

**En esta etapa no se solicitan validaciones.** Se supondrá que el usuario ingresa los datos con el formato esperado.

## Etapa 6. Ordenamiento por nivel

Implementar **burbujeo tradicional** para ordenar los Pokémon por nivel de mayor a menor. Comparar elementos vecinos e intercambiarlos cuando corresponda. Cada intercambio deberá realizarse también en las otras cinco listas para conservar la relación entre los datos.

No utilizar `sort()` ni `sorted()`.

## Etapa 7. Integración

Organizar el sistema en tres archivos:

- `data_storage.py`: datos iniciales.
- `pokemones.py`: funciones desarrolladas.
- `main.py`: menú principal con `while` y `match`.

El menú deberá ofrecer las funciones anteriores y permitir realizar operaciones hasta seleccionar **Salir**.

## Condiciones de trabajo

- Utilizar listas paralelas, funciones y estructuras de control.
- No utilizar clases ni programación orientada a objetos.
- No utilizar `max()`, `min()`, `sum()`, `sort()` ni `sorted()` para resolver los algoritmos solicitados.
- Evitar variables globales dentro de las funciones: trabajar con parámetros y valores de retorno.
- Reutilizar las funciones desarrolladas en las etapas anteriores.
- No incorporar validaciones de entrada en esta versión.
- Cada etapa deberá funcionar antes de avanzar a la siguiente.
