from validate import *
def get_int(mensaje:str)-> int|None:
    numero = int(input(mensaje))
    return numero

def get_float(mensaje:str)-> float|None:
    numero = float(input(mensaje))
    return numero

def get_string(mensaje:str)-> str|None:
    cadena = input(mensaje)
    return cadena

def pedir_numero_validado(mensaje,mensaje_error,minimo,maximo,reintentos):
    numero = get_int(mensaje)
    validate_int(mensaje,mensaje_error,minimo,maximo,reintentos)
