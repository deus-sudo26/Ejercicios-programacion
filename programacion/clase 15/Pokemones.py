import os
from funciones_pokemones import *


nombres = [
    "Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Jigglypuff",
    "Gastly", "Abra", "Machop", "Geodude", "Dratini",
    "Vulpix", "Psyduck", "Oddish", "Haunter", "Raichu",
    "Hitmonlee", "Onix", "Sylveon", "Espeon", "Bagon",
    "Growlithe", "Poliwag", "Bellsprout", "Gengar", "Jolteon",
    "Makuhita", "Rhyhorn", "Togekiss", "Kadabra", "Gible",
    "Ponyta", "Vaporeon", "Chikorita", "Misdreavus", "Electabuzz",
    "Riolu", "Larvitar", "Clefairy", "Mewtwo", "Dragonair",
    "Magmar", "Totodile", "Treecko", "Duskull", "Luxray",
    "Machoke", "Golem", "Granbull", "Ralts", "Axew"
]

tipos = [
    "Electrico", "Fuego", "Agua", "Planta", "Hada",
    "Fantasma", "Psiquico", "Lucha", "Roca", "Dragon",
    "Fuego", "Agua", "Planta", "Fantasma", "Electrico",
    "Lucha", "Roca", "Hada", "Psiquico", "Dragon",
    "Fuego", "Agua", "Planta", "Fantasma", "Electrico",
    "Lucha", "Roca", "Hada", "Psiquico", "Dragon",
    "Fuego", "Agua", "Planta", "Fantasma", "Electrico",
    "Lucha", "Roca", "Hada", "Psiquico", "Dragon",
    "Fuego", "Agua", "Planta", "Fantasma", "Electrico",
    "Lucha", "Roca", "Hada", "Psiquico", "Dragon"
]

niveles = []

puntos_salud = [
    12, 10, 15, 17, 22,
    12, 10, 20, 24, 18,
    14, 19, 14, 17, 18,
    23, 30, 23, 22, 22,
    18, 13, 16, 24, 16,
    28, 27, 27, 15, 29,
    17, 24, 20, 18, 20,
    19, 26, 19, 35, 25,
    22, 21, 18, 21, 25,
    25, 32, 25, 16, 24
]

puntos_ataque = [
    14, 15, 12, 13, 11,
    16, 18, 22, 19, 23,
    17, 16, 12, 21, 20,
    30, 24, 20, 25, 29,
    21, 13, 15, 27, 22,
    24, 28, 24, 23, 32,
    23, 21, 18, 20, 24,
    26, 27, 13, 35, 27,
    26, 20, 22, 23, 28,
    27, 31, 25, 17, 30
]

puntos_defensa = [
    10, 11, 18, 16, 14,
    12, 9, 17, 28, 19,
    15, 15, 13, 16, 16,
    20, 32, 19, 18, 21,
    17, 14, 17, 20, 14,
    25, 30, 25, 14, 28,
    16, 22, 21, 17, 18,
    18, 26, 18, 27, 24,
    20, 19, 15, 24, 22,
    22, 35, 23, 13, 25
]
######################################################################
# Disponemos de los siguientes datos de los pokemones que capturo ASH:
# nombre, tipo, nivel, puntos_salud, puntos_ataque, puntos_defensa
# El nivel debera calcularse de acuerdo al promedio entre los puntos de at, salud y defe:
# 1 - 8 -> Nivel 1
# 9 - 15 -> Nivel 2
# 16 - 20 -> Nivel 3
# Mas de 20 -> 4

def main():
    asignar_nivel(niveles,puntos_salud,puntos_ataque,puntos_defensa)
    while True:
        lista_distintos_tipos = ["Hada","Roca","Fuego"]
        opciones_menu = ["Cargar", "Mostrar todos","Ordenar","Mostrar por nombre","Mostrar por tipo y nivel","Maximo ataque","Cantidad por tipo","Porcentaje tipos"]
        opcion = elegir_opcion(opciones_menu)



        match opcion:
            case 1:
                cargar_pokemon(nombres, tipos, puntos_salud, puntos_defensa, puntos_ataque, niveles)
            case 2:
                mostrar_pokemones(nombres, tipos, niveles, puntos_salud, puntos_defensa, puntos_ataque)
            case 3:
                ordenar_por_nivel(niveles, nombres, puntos_salud, puntos_ataque, puntos_defensa, tipos)
            case 4:
                nombre = "Pikachu"
                indice = buscar_por_nombre(nombres, nombre)
                if indice != -1:
                    mostrar_cabecera()
                    mostrar_un_pokemon(nombres, tipos,niveles, puntos_salud,puntos_ataque, puntos_defensa,indice)
                else:
                    print("Pokemon no encontrado.")
            case 5:
                buscar_por_tipo_nivel(nombres,tipos,puntos_salud,puntos_defensa,puntos_ataque,niveles,"Hada",3)

            case 6:
                mostrar_pokemones_mayor_ataque(nombres,tipos,niveles,puntos_salud,puntos_ataque,puntos_defensa)
            case 7:
                contar_pokemones_por_tipo(tipos,lista_distintos_tipos)
            case 8:
                mostrar_porcentaje_por_tipo(tipos, lista_distintos_tipos)
        os.system("pause")
        os.system("cls")

if __name__ == "__main__":
    main()