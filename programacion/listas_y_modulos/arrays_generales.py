from inputs import *
from validate import  *
from funcionesEspeciales import *

def ingresar_datos_en_lista(lista, cantidad, mensaje, mensaje_error, minimo, maximo, reintentos):
    for _ in range(0,cantidad,1):
        numero = pedir_numero_validado(mensaje, mensaje_error, minimo, maximo, reintentos)
        lista.append(numero)


# def calcular_positivos_negativos(lista):
#     numeros_postivos = 0
#     numeros_negativos = 0

#     for i in range (0, len(lista),1):
#         if lista[i] > 0:
#             numeros_postivos += 1
#         elif lista[1] < 0: #para no contar el 0 con el else.
#             numeros_negativos += 1
#     print(f"cantidad positivos: {numeros_postivos}")
#     print(f"cantidad negativos: {numeros_negativos}")

def calcular_positivos_negativos_v2(lista):
    numeros_postivos = contar_signos(lista,True)
    numeros_negativos = contar_signos(lista,False)

    print(f"cantidad positivos: {numeros_postivos}")
    print(f"cantidad negativos: {numeros_negativos}")

def sumar_pares(lista):
    suma_pares = 0
    for i in range(0,len(lista),1):
        if determinar_paridad(lista[i]) == True:
            suma_pares += lista[i]
