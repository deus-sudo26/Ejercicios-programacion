# def calcular_factorial (numero):
#     if numero != 0:
#         resultado = numero * (numero - 1)
#     return resultado

# print(calcular_factorial(5))
# resultado = 1
# for i in range(1,6):
#     resultado *= i 
# print(resultado)

# def calcular_factorial (numero):
    
#     if numero == 0:
#         resultado = 1
#     else:
#         resultado = numero * calcular_factorial(numero - 1)
        
#     return resultado

# print(calcular_factorial(5))

#Realizar una función recursiva que calcule la suma de los primeros números naturales: 
# def sumar_numeros(numero: int)->int:
#     if numero <= 1:
#         return numero
#     else:
#         return numero + sumar_numeros(numero-1)


# numero = int(input("ingresa numero: "))
# print(sumar_numeros(numero))

#Realizar una función recursiva que calcule la potencia de un número: 
# def potenciar_numero(numero: int,potencia: int)->int:
#     if potencia == 0:
#         return 1
#     else: 
#         return numero * potenciar_numero(numero,potencia -1)

# numero = int(input("base: "))
# potencia = int(input("potencia: "))
# print(potenciar_numero(numero,potencia))


#Realizar una función recursiva que permita realizar la suma de los dígitos de un número: 

# def sumar_digitos(numero: int)->int:
#     if numero == 0:
#         return numero
#     else: 
#         return numero % 10 + sumar_digitos(numero // 10)

# numero = int(input("numero: "))
# print(sumar_digitos(numero))


#Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo: 
def calcular_fibonacci(numero: int)-> int:
    if numero <= 1:
        return numero
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
numero = int(input("numero: "))
print(calcular_fibonacci(numero))
