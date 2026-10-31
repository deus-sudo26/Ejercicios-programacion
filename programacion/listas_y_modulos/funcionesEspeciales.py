# def contar_positivos(lista):
#     numeros_postivos = 0
#     for i in range (0, len(lista),1):
#         if lista[i] > 0:
#             numeros_postivos += 1
#     print(f"cantidad positivos: {numeros_postivos}")
######################## NEGATIVOS CEROS Y POSITIVOS #############
# def contar_negativos(lista):
#     numeros_negativos = 0
#     for i in range (0, len(lista),1):
#         if lista[i] > 0:
#             numeros_negativos += 1
#     print(f"cantidad negativos: {numeros_negativos}")


#region DETERMINAR SIGNOS Y CONTARLOS 
def determinar_signo(numero: int) -> bool|None:
    bandera = None
    if numero > 0:
        bandera = True
    elif numero < 0:
        bandera = False
    return bandera

def contar_signos(lista,criterio:bool|None):
    contador = 0
    for i in range(0, len(lista),1):
        if determinar_signo(lista[i]) == criterio:
            contador += 1
    return contador

def calcular_positivos_negativos(lista):
    numeros_postivos = contar_signos(lista,True)
    numeros_negativos = contar_signos(lista,False)

    print(f"cantidad positivos: {numeros_postivos}")
    print(f"cantidad negativos: {numeros_negativos}")

#endregion



#REGION  PARES E IMPARES ########
def sumar_pares(lista):
    suma_pares = 0
    for i in range(0,len(lista),1):
        if determinar_paridad == True:
            suma_pares += lista[i]

    print(suma_pares)

def sumar_impares(lista):
    suma_impares = 0
    for i in range(1,len(lista),1):
        if lista[i] % 2 != 0:
            suma_impares += lista[i]

    print(suma_impares)

def determinar_paridad(numero)->bool:
    es_par = False
    if numero % 2 == 0:
        es_par = True
    return es_par
#ENDREGION