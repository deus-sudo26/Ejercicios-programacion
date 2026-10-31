from inputs import *
def validate_int(numero,mensaje,mensaje_error,minimo,maximo,reintentos)-> int|None:
    intentos = 0
    while minimo > numero or numero > maximo:
        print(mensaje_error)
        numero = int(input(mensaje))
        intentos += 1
        if intentos == reintentos:
            break
    return numero

def validate_float(numero,mensaje,mensaje_error,minimo,maximo,reintentos)-> float|None:
    intentos = 0
    while minimo > numero or numero > maximo:
        print(mensaje_error)
        numero = float(input(mensaje))
        intentos += 1
        if intentos == reintentos:
            break
    return numero
