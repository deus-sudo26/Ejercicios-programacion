# def sumar_numeros_1()
#     primer_numero = int(input("Ingrese el primer numero: "))
#     segundo_numero = int(input("Ingrese el segundo numero: "))
#     sume = primer_numero + segundo_numero
#     print(f"la suma de {primer_numero} + {segundo_numero} es: {sume}")

# def sumar_numeros_2(primer_numero, segundo_numero):
#     sume = primer_numero + segundo_numero
#     print(f"la suma de {primer_numero} + {segundo_numero} es: {sume}")
# ##################main###########

# # sumar_numeros_1() #llamada a la funcion
# sumar_numeros_2(10, 20) #llamada a la funcion

# primer_numero = int(input("Ingrese el primer numero: "))
# segundo_numero = int(input("Ingrese el segundo numero: "))
# sumar_numeros_2(primer_numero, segundo_numero) #llamada a la funcion

# def sumar_numeros_3(primer_numero, segundo_numero):
#     primer_numero = int(input("Ingrese el primer numero: "))
#     segundo_numero = int(input("Ingrese el segundo numero: "))
#     suma = primer_numero + segundo_numero
#     return suma
# resultado = sumar_numeros_3() #llamada a la funcion
# print(f"la suma es: {resultado}")

# def sumar_numeros_4(primer_numero, segundo_numero):
#     suma = primer_numero + segundo_numero
#     return suma
# resultado = sumar_numeros_4(10, 20) #llamada a la funcion
# print(f"la suma es: {resultado}")

#########################################################

#6 Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar. 
# def verificar_par(numero):
#     if numero % 2 == 0:
#         print(f"El número {numero} es par.")
#     else:
#         print(f"El número {numero} es impar.")
# print("Ingrese un número para verificar si es par o impar:")
# numero = int(input())
# verificar_par(numero)

##############################################################

#7Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario. 
# def verificar_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False

# print("Ingrese un número para verificar si es par o impar:")
# numero = int(input())
# resultado = verificar_par(numero)
# if resultado == True:
#     print(f"El número {numero} es par.")
# else:
#     print(f"El numero {numero} es impar.")


# def verificar_par(numero):
#     if numero % 2 == 0:
#         es_par = True
#     else:
#         es_par = False
#     return es_par

# print("Ingrese un número para verificar si es par o impar:")
# numero = int(input())
# resultado = verificar_par(numero)
# if resultado == True:
#     print(f"El número {numero} es par.")
# else:
#     print(f"El numero {numero} es impar.")

# def verificar_par(numero):
#     es_par = False   #determino de antemano que es falso hasta que
#     #se demuestre lo contrario
#     if numero % 2 == 0:
#         es_par = True
   
#     return es_par

# def verificar_par(numero):

#     return numero % 2 == 0

############################################################################

#9Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado. 
# def potenciar_numero(base,exponente):
#     potencia = base ** exponente
#     return potencia
# resultado = potenciar_numero(2,3)
# print(resultado)

# def potenciar_numero(base,exponente):
#     resultado = 1
#     for i in range(0,exponente,1):
#         resultado = base * resultado
#     return resultado
# solucion = potenciar_numero(2,3)
# print(solucion)
from math import pow
pow