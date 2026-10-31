#ejercicio 1
def ingresar_int()-> int:
    numero = int(input("ingresa un numero: "))
    return numero
#ejercicio 2
def ingresar_float()-> float:
    numero = float(input("ingrese un numero: "))
    return numero
#ejercicio 3 
def ingresar_string()-> str:
    cadena = input("ingresa algun caracter: ")
    return cadena

# 4 Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.  

def area_rectangulo (base,altura):
    area = base * altura
    return area

# print("Calcular area de un rectangulo")
# base = int(input("ingresa la base: "))
# altura = int(input("ingresa la altura: "))
# resultado = area_rectangulo(base,altura)
# print(f"el area es {resultado}")

#5 Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área. 
from math import pi
def area_circulo (radio):
    area = pi * radio ** 2
    return area
radio = int(input("ingrese el radio del circulo: "))
print(f"el area del circulo es {area_circulo(radio)}")

#6
def definir_paridad(numero:int):
    es_par = True
    if numero % 2 != 0:
        es_par = False
    if es_par:
        print(f"el numero {numero} es par.")
    else:
        print(f"el numero {numero} es impar.")

#7 
