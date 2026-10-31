# # 1 #

# for numero in range (0,10,1):
#     print(numero + 1)

# 2 #

# for numero in range(10, 0, -1):
#     print(numero)

# 3 #
# i = int(input("ingresa un numero: "))
# for numero in range(i):
#     print(numero)

# 4 #
# numero = int(input("ingresa un numero: "))
# for i in range(0,11,1):
#     multiplicacion = numero * i
#     print(numero ,"*",i,"=",multiplicacion)


# 5 #
# for numero in range(0,11,1):
#     if numero % 3 == 0:
#         print (numero)

# 6 #
# acumulador = 0
# for i in range(0,11,1):
#     numero = int(input("ingrese un numero: "))
#     if numero == 0:
#         break
#     acumulador += numero

# promedio = acumulador / i
# print(f"""
# La suma total de los numero ingresados es {acumulador}
# Y el promedio es: {promedio}
# """)

# 7 #
# for i in range (1,11,1):
#     if i == 5:
#         continue
#     print(i)

# 8 #
# suma = 0
# for i in range(0,10):
#     numero = int(input("ingresa un numero:"))
#     if 50 < numero < 100:
#         continue
#     suma += numero
# print(suma)






# 9 #
# for i in range(0,50):
#     if i % 2 == 0:
#         print(i)




# preguntar por la palabra reservada "end="

# 10 #
# numero = int(input("ingresa un numero:"))
# for i in range(1,numero):
#     for j in range(1,i + 1):
#         print(j, end="")
#     print()

# 11 #
for i in range (1, 13, 1):
    for j in range(1, 13, 1):
        print(i,j)
