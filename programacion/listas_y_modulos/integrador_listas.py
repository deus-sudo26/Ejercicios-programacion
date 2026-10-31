from inputs import *
from validate import  *
from funcionesEspeciales import *


###opcion 2  #######################################

def determinar_signo(numero: int) -> bool|None:
    bandera = None
    if numero > 0:
        bandera = True
    elif numero < 0:
        bandera = False
    return bandera


###############################################
# print(sumar_pares(lista))


# def buscar_mayor_impar(lista):
#     impar_mayor = lista[0]
#     for i in range (0,len(lista),1):
#         if lista[i] % 2 != 0 :
#             if impar_mayor < lista[i]:
#                 impar_mayor = lista[i]
#     return impar_mayor
# print(buscar_mayor_impar(lista))

# def mostrar_numeros_lista(lista):
#     print(lista)

# def mostrar_numeros_lista(lista):
#     for i in range (1,len(lista),1):
#         print(lista[i])

# print(mostrar_numeros_lista(lista))

# def listar_pares(lista):
#     for i in range (1,len(lista),1):
#         if lista[i] % 2 == 0 :
#            print(lista[i])

# print(listar_pares(lista))

lista = [1,-2,3,4,7,6,8,-5]

# def mostrar_posicion_impar(lista):
#     for i in range(1,len(lista),1):
#         if len(lista) % 2 != 0:
#             print(lista[i])

# print(mostrar_posicion_impar(lista))

# def solicitar_entero() -> int:
#     numero = int(input("Ingrese un numero entero: "))
#     return numero

# def validar_entero(numero: int, min_valor: int, max_valor: int) -> bool:
#     return min_valor <= numero <= max_valor

# def agregar_elemento_lista(lista: list, elemento: int) -> None:
#     lista.append(elemento)

# def cargar_lista(cantidad_elementos: int, limite_inferior: int, limite_superior: int) -> list:
#     lista = []
#     while len(lista) < cantidad_elementos:
#         numero = solicitar_entero()
#         if validar_entero(numero, limite_inferior, limite_superior):
#             agregar_elemento_lista(lista, numero)
#         else:
#             print(f"El numero {numero} no esta dentro del rango permitido ({limite_inferior}-{limite_superior}).")
#     return lista