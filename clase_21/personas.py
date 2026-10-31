from datos_personas_con_puntos import*
#region mostrar
def mostrar_lista_personas(lista_personas: list[dict]):
    for persona in lista_personas:
        print(f"{persona["nombre"]} - {persona["edad"]} - {persona["soltero"]} - {persona["hobbies"]} - {persona["email"]} - {persona["puntos"]}")
    pass
def mostrar_hobbies(lista_hobbies):
    for hobbie in lista_hobbies:
        print(f"{hobbie} - ", end = "")
def mostrar_hobbies_v2(lista_hobbies):
    mensaje = ""
    for hobbie in lista_hobbies:
        mensaje += f"{hobbie} - "
    return mensaje
def mostrar_lista_personas_v2(lista_personas: list[dict]):
    for persona in lista_personas:
        print(f"{persona["nombre"]:<15}{persona["edad"]:<5}{persona["soltero"]:<15}", end = "")
        if len(persona["hobbies"]) != 0:
            mensaje = mostrar_hobbies(persona["hobbies"])
            print(mensaje, end = "")
        else:
            print(f"- Sin Hobbies - ", end = "")
        print() 

def mostrar_una_persona(persona):
        print(f"{persona["nombre"]:<15}{persona["edad"]:<5}{persona["soltero"]:<15}", end = "")
        if len(persona["hobbies"]) != 0:
            mensaje = mostrar_hobbies(persona["hobbies"])
            print(mensaje, end = "")
        else:
            print(f"- Sin Hobbies - ", end = "")
        print() 
#endregion

def mostrar_buscado(lista_de_personas:list[dict], buscado:str):
    for persona in lista_de_personas:
        if persona["nombre"] == buscado:
            mostrar_una_persona(persona)

def mostrar_por_edad(lista_de_personas, edad):
    for persona in lista_de_personas:
        if persona["edad"] == edad:
            mostrar_una_persona(persona)

def filtrar_por_clave(lista_personas:list[dict], clave:str, valor:any):
    lista_filtrada = []
    for persona in lista_personas:
        if persona[clave] == valor:
            lista_filtrada.append(persona)
    return lista_filtrada

def mostrar_por_clave(lista_personas:list[dict], clave:str, valor:any):
    for persona in lista_personas:
        if persona[clave] == valor:
            mostrar_una_persona(persona)

def mostrar_por_clave_v2(lista_personas:list[dict], clave:str, valor:any):
    lista_filtrada = filtrar_por_clave(lista_personas,clave,valor)
    print(lista_filtrada)

def obtener_promedio_filtrado(lista_personas,clave_promedio, clave_filtro, valor_filtro):
    lista_filtrada = filtrar_por_clave(lista_personas,clave_filtro,valor_filtro)
    suma = 0
    for persona in lista_filtrada:
        suma += persona[clave_promedio]
    promedio = suma/len(lista_filtrada)
    return promedio

def buscar_maximo(lista_personas,clave):
    maximo = lista_personas[0][clave]
    for persona in lista_personas:
        if persona[clave] > maximo:
            maximo = persona[clave]
    return maximo
def mostrar_maximo_por_clave(lista_personas,clave):
    maximo = buscar_maximo(lista_personas,clave)
    mostrar_por_clave(lista_personas,clave,maximo)


def recopilar_hobbies(lista_personas):
    hobbies = []
    lista_filtrada = []
    for persona in lista_personas:
        for hobbie in persona['hobbies']:
            hobbies.append(hobbie)
    for hobbie in hobbies:
        bandera = False
        for h in lista_filtrada:
            if hobbie == h:
                bandera = True
                break
        if bandera == False:
            lista_filtrada.append(hobbie)

    return lista_filtrada

