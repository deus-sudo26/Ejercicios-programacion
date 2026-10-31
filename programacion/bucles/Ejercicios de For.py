#1
'''
for i in range(1,11,1):
  print(i)
#2
for i in range(10,0,-1):
  print(i)

#3
numero = int(input("ingresa tu numero: "))
for i in range(1,numero + 1,1):
  print(i)

#4
numero = int(input("ingresa el numero de la tabla a verificar"))
for i in range (0,11,1):
  print(f"{numero} * {i} = {numero*i}")
#5
for i in range(1,10+1,1):
  if i % 3 == 0:
    print(i)
'''
'''
#6
contador = 0
suma = 0
for i in range(0,10,1):
  numero = int(input("ingresa tus numeros: "))
  if numero == 0:
    break
  contador += 1
  suma += numero
promedio = suma / contador
print(f"el promedio es {promedio} y la suma de los numeros es {suma}")
'''
'''
#7
for i in range(1,10+1,1):
  numero = int(input("ingress un numero"))
  if numero == 5 :
    continue
  print(numero)
'''
#8
'''
suma = 0
for i in range (1,10+1,1):
  numero = int(input("ingresa un numero: "))
  if  numero <= 50 or numero >= 100:
    suma += numero
print(suma)
'''
#9
'''
for i in range(1,50+1,1):
  if i % 2 == 0:
    print(i)
for i in range(2,50+1,2):
  print(i)
'''
#11
'''
numero = int(input("ingresa un numero: "))
cantidad_divisores = 0
for i in range(1,numero+1,1):
  if numero % i ==0:
    print(i)
    cantidad_divisores += 1
print(f"cantidad de divisores : {cantidad_divisores}")
'''
#12
'''
numero = int(input("ingresa un numero: "))
cantidad_divisores = 0
for i in range (1,numero+1,1):
  if numero % i == 0:
    cantidad_divisores += 1
if cantidad_divisores == 2:
  print(f"{numero} es primo.")
else:
  print(f"{numero} no es primo")
'''
'''
numero = int(input("ingresa un numero: "))
es_primo = True
for i in range (2,numero,1):
  if numero % i == 0:
    es_primo = False
    break
    
if es_primo == True and numero > 1:
  print(f"{numero} es primo.")
else:
  print(f"{numero} no es primo")
  '''
#13
numero = int(input("ingresa un numero: "))
es_primo = True
cantidad_primos = 0

for i in range(2,numero + 1,1):
  for j in range(2,i,1):
    if i % j == 0:
      es_primo = False
  if es_primo == True:
    print(i)
    cantidad_primos += 1
  es_primo = True

print("cantidad de primos",cantidad_primos)
  