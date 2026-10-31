
# ######### FUNCIONES ########
#region 1
def get_int(mensaje:str)-> int|None:
    numero = int(input(mensaje))
    return numero

def elegir_opcion(lista)-> int:
    for i in range(0,len(lista),1):
        print(f"{i+1}. {lista[i]}")
    opcion = get_int("selecciona una opcion: ")
    return opcion

# def calcular_promedio(lista_puntajes: list):
#     suma = 0
#     for i in range(0, len(lista_puntajes), 1):
#         suma += lista_puntajes[i]

#     promedio = suma / len(lista_puntajes)
#     return promedio

# def calcular_nivel(promedio: float):
#       if promedio > 20:
#             nivel = 4
#       elif promedio >= 16:
#             nivel = 3
#       elif promedio >= 9:
#             nivel = 2
#       else:
#             nivel = 1

#       niveles.append(nivel)

# def asignar_nivel(niveles: list, salud, ataque, defensa):
#     for i in range(0, len(salud), 1):
#         promedio = calcular_promedio([salud[i], ataque[i], defensa[i]])
#         nivel = calcular_nivel(promedio)
#         niveles.append(nivel)
                            
# def mostrar_cabecera():
#     print(f"{0:15}{1:15}{2:15}{3:10}{4:10}{5:10}".format("Nombre", "Tipo", "Nivel", "Pt Salud", "Pt Ataque", "Pt Defensa"))
        
# def mostrar_un_pokemon(nombres, tipos, niveles, salud, ataque, defensa):
#     print(f"{nombres:15}{tipos:15}{niveles:10}{salud:10}{ataque:10}{defensa:10}")

# def mostrar_pokemones(nombres, tipos, niveles, salud, ataque, defensa):
#     mostrar_cabecera()    
#     for i in range(0, len(nombres), 1):
#         mostrar_un_pokemon(nombres[i], tipos[i], niveles[i], salud[i], ataque[i], defensa[i])

# def mostrar_pokemones_tipo(nombres, tipos, niveles, salud, ataque, defensa, tipo_buscado):
#     mostrar_cabecera()
#     for i in range(0, len(nombres), 1):
#         if tipos[i] == tipo_buscado:
#             mostrar_un_pokemon(nombres[i], tipos[i], niveles[i], salud[i], ataque[i], defensa[i])
             
#             # print(f"{nombres[i]:15}{tipos[i]:15}{niveles[i]:10}{salud[i]:10}{ataque[i]:10}{defensa[i]:10}")
#endregion

#region 1. visualizacion
def mostrar_cabecera():
    print("{0:15}{1:15}{2:15}{3:10}{4:10}{5:10}".format("Nombre", "Tipo", "Nivel" , "Pt Salud", "Pt Ataque", "Pt Defensa"))

def mostrar_pokemones_tipo(nombres, tipos, niveles, salud, ataque, defensa, tipo_buscado):
    mostrar_cabecera()    
    for i in range(0, len(nombres), 1):
        if tipos[i] == tipo_buscado:
            mostrar_un_pokemon(nombres[i], tipos[i], niveles[i], salud[i], ataque[i], defensa[i])

def mostrar_un_pokemon(nombre, tipo, nivel, salud, ataque, defensa, indice):
    print(f"{nombre[indice]:15}{tipo[indice]:15}{nivel[indice]:10}{salud[indice]:10}{ataque[indice]:10}{defensa[indice]:10}")

def mostrar_pokemones(nombres, tipos, niveles, salud, ataque, defensa):
    mostrar_cabecera()
    for i in range(0, len(nombres), 1):
        mostrar_un_pokemon(nombres, tipos, niveles, salud, ataque, defensa,i)

#endregion
#region 2.region calculo niveles
def calcular_promedio(lista_puntajes: list):
    suma = 0
    for i in range(0, len(lista_puntajes), 1):
        suma += lista_puntajes[i]

    promedio = suma / len(lista_puntajes)
    return promedio

def calcular_nivel(promedio: float):
    if promedio > 20:
        nivel = 4
    elif promedio >= 16:
        nivel = 3
    elif promedio >= 9:
        nivel = 2
    else:
        nivel = 1
    return nivel


def asignar_nivel(niveles: list, salud, ataque, defensa):
    for i in range(0, len(salud), 1):
        guardar_nivel_en_lista(niveles, salud, ataque, defensa, i)

def guardar_nivel_en_lista(niveles: int, salud, ataque, defensa, i):
    promedio = calcular_promedio([salud[i], ataque[i], defensa[i]])
    nivel = calcular_nivel(promedio)
    niveles.append(nivel)

#endregion busqueda


#region 3. busquedas

def mostrar_pokemones_criterio(nombres, tipos, niveles, salud, ataque, defensa, lista_criterio, tipo_buscado):
    mostrar_cabecera()
    for i in range(0,len(lista_criterio),1):
        if lista_criterio[i] == tipo_buscado:
            mostrar_un_pokemon(nombres, tipos, niveles, salud, ataque, defensa,i)


def mostrar_pokemones_tipo(nombres, tipos, niveles, salud, ataque, defensa, tipo_buscado):
    mostrar_cabecera()
    for i in range(0,len(nombres,1)):
        if tipos[i] == tipo_buscado:
            mostrar_un_pokemon(nombres[i], tipos[i], niveles[i], salud[i], ataque[i], defensa[i])

# buscar_por_nombre() devuelve el indice del pokemon o -1
def buscar_por_nombre(nombres, nombre):
    indice = -1
    for i in range(0,len(nombres,1)):
        if nombres[i] == nombre:
            indice = i
            break
    return indice

# Buscar por tipo y nivel , muestra pokemon que cumple ambas condiciones

def buscar_por_tipo_nivel(nombres, tipos, niveles, salud, ataque, defensa, tipo_buscado, nivel_buscado):
    mostrar_cabecera()
    for i in range(0,len(nombres,1)):
        if tipos[i] == tipo_buscado and niveles[i] == nivel_buscado:
            mostrar_un_pokemon(nombres[i], tipos[i], niveles[i], salud[i], ataque[i], defensa[i])
    
#endregion


#region 4. estadisticas
def buscar_maximo(lista):
    maximo = lista[0]
    for i in range(0,len(lista),1):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

def mostrar_pokemones_mayor_ataque(nombres, tipos, niveles, salud, ataque, defensa):
    maximo = buscar_maximo(ataque)
    print(f"maximo ataque es {maximo}")
    mostrar_pokemones_criterio(nombres,tipos,niveles,salud,ataque,defensa,ataque,maximo)

def contar_pokemon_por_tipo(tipos,tipo_buscado):
    contador_tipo = 0
    for i in range(0,len(tipos)):
        if tipos[i] == tipo_buscado:
            contador_tipo += tipos[i]

    return contador_tipo
def contar_pokemones_por_tipo(tipos, lista_distintos_tipos):
    contadores_tipo = []

    for i in range(0,len(lista_distintos_tipos)):
        contador = 0
        for j in range(0,len(tipos)):
            if lista_distintos_tipos[i] == tipos[j]:
                contador += 1
        contadores_tipo.append(contador)
    return contadores_tipo

def mostrar_cantidad_por_tipo(tipos, lista_distintos_tipos):
    contadores_tipo = contar_pokemones_por_tipo(tipos, lista_distintos_tipos)
    for i in range(0,len(lista_distintos_tipos)):
        print(f"cantidad de {lista_distintos_tipos[i]: {contadores_tipo[i]}}")

def mostrar_porcentaje_por_tipo(tipos, lista_distintos_tipos):
    contadores_tipo = contar_pokemones_por_tipo(tipos, lista_distintos_tipos)
    total_pokemones = len(tipos)
    for i in range(0,len(lista_distintos_tipos)):
        porcentaje = (contadores_tipo[i] * 100) / total_pokemones
    print(f"Tipo {lista_distintos_tipos[i]}:{porcentaje:.2f}%")
#endregion

#region 5. carga de pokemon
def cargar_pokemon(nombres: list, tipos: list, puntos_salud: list, puntos_defensa: list, puntos_ataque: list, niveles: list): # verificar que puede retornar
    nombre = input("Ingrese nombre: ")  ### aca tendriamos que poner una funcion para ingresar datos
    tipo = input("Ingrese tipo: ")  #### aca tambien pero con categoria 
    salud = int(input("Ingrese puntos de salud"))   ##
    defensa = int(input("Ingrese puntos de defensa"))   ##
    ataque = int(input("Ingrese puntos de ataque"))   ###

    # promedio = calcular_promedio([salud[i], ataque[i], defensa[i]])
    #nivel = calcular_nivel(promedio)
   # niveles.append(nivel)
    # Si esta todo bien

    nombres.append(nombre)
    tipos.append(tipo)
    puntos_salud.append(salud)
    puntos_defensa.append(defensa)
    puntos_ataque.append(ataque)
#endregion

#region 6. ordenamiento
def ordenar_por_nivel(nombres, niveles):
    for i in range(0,len(niveles) - 1, 1):
        for j in range(i + 1, len(niveles), 1):
            if niveles [i] > niveles [j]:
                auxiliar = niveles[i]
                niveles[i] = niveles[j]
                niveles[j] = auxiliar

######################################################################
# Disponemos de los siguientes datos de los pokemones que capturo ASH:
# nombre, tipo, nivel, puntos_salud, puntos_ataque, puntos_defensa
# El nivel debera calcularse de acuerdo al promedio entre los puntos de at, salud y defe:
# 1 - 8 -> Nivel 1
# 9 - 15 -> Nivel 2
# 16 - 20 -> Nivel 3
# Mas de 20 -> 4


# asignar_nivel(niveles, puntos_salud, puntos_ataque, puntos_defensa)
# mostrar_pokemones(nombres, tipos, niveles, puntos_salud, puntos_ataque, puntos_defensa)
# print()
# mostrar_pokemones_tipo(nombres, tipos, niveles, puntos_salud, puntos_ataque, puntos_defensa, "Fuego")



# print(calcular_promedio(puntos_salud))
