#ejercicios 11 y 12

# contador_divisiores = 0

# numero = int(input("ingrese un numero: "))

# for i in range (1,numero + 1 , 1):
#     if numero % i  == 0:
#         print(i)
#         contador_divisiores += 1
# print(contador_divisiores)

#ejercicio 12
#ingresar un numero, determinar si es primo o no 
# contador_divisores = 0
# numero = int(input("ingresa un numero: "))

# for i in range(1,numero,1):
#     if numero %  i == 0:
#         contador_divisores += 1
# if contador_divisores == 2:
#     print("es primo")
# else:
#     print("no es primo")

#     contador_divisores = 0
# numero = int(input("ingresa un numero: "))

# for i in range(2,numero):
#     if numero %  i == 0:
#         contador_divisores += 1
# if numero != 1 and contador_divisores == 0:
#     print("es primo")
# else:
#     print("no es primo")
# bandera_primo = True
# numero = int(input("ingresa un numero: "))

# for i in range(2,numero,1):
#     if numero %  i == 0:
#         bandera_primo = False
# if numero != 1 and bandera_primo == True:
#     print("es primo")
# else:
#     print("no es primo")

# 13

# numero = int(input("ingrese un numero:"))
# contador_divisores = 0

# contador_primos = 0
# for i in range(1,numero + 1 ,1):
#     for j in range(1, i + 1 ,1):
#         if i % j == 0:
#             contador_divisores += 1
#     if contador_divisores == 2:
#         print(f"{i} es primo")
#         contador_primos += 1
#     contador_divisores = 0 # tengo que reiniciar el contador de divisores para el siguiente numero
# print(f"la cantidad de numeros primos es: {contador_primos}")


# numero = int(input("ingrese un numero:"))
# contador_divisores = 0

# contador_primos = 0
# for i in range(2,numero + 1 ,1):
#     bandera_primo = True
#     for j in range(2, i ,1):
#         if i % j == 0:
#             bandera_primo = False
#             break
#     if bandera_primo == True:
#         print(f"{i} es primo")
#         contador_primos += 1
#     # tengo que reiniciar el contador de divisores para el siguiente numero
# print(f"la cantidad de numeros primos es: {contador_primos}")

def es_primo(numero):
    numero = int(input("ingrese un numero:"))
    contador_divisores = 0
    contador_primos = 0
    for i in range(2,numero + 1 ,1):
        bandera_primo = True
        for j in range(2, i ,1):
            if i % j == 0:
                bandera_primo = False
                break
        if bandera_primo == True:
            print(f"{i} es primo")
            contador_primos += 1
    # tengo que reiniciar el contador de divisores para el siguiente numero
    print(f"la cantidad de numeros primos es: {contador_primos}")

es_primo(10)