#region PAPELERA
# for i in range(dimension):
#     fila =[]
#     for j in range(dimension):
#         valor = int(input(f"ingresa un numero entre 1 y {dimension**2}: "))
#         while valor < 0 or valor > (dimension**2)+1:
#             print("error,ingrese otro numero: ")
#             valor = int(input(f"ingresa un numero entre 1 y {dimension**2}: "))
#         fila.append(valor)
        
#     matriz.append(fila)
#endregion
import random
#region MOSTRAR

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()
#endregion

#region VALIDAR

def validar_repetido_matriz(matriz,numero):
    repetido = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                repetido = True
    return repetido

def validar_repetido_fila(fila,numero):
    repetido = False
    for i in range (len(fila)):
        if fila[i] == numero:
            repetido = True
    return repetido

def determinar_magico_filas(matriz,constante):
    es_magico = True
    for i in range(len(matriz)):
        suma_fila = 0
        for j in range(len(matriz[0])):
            suma_fila += matriz[i][j]
        if suma_fila != constante:
            es_magico = False
            break
    return es_magico

def determinar_magico_columnas(matriz,constante):
    es_magico = True
    for i in range(len(matriz[0])):
        suma_columna = 0
        for j in range(len(matriz)):
            suma_columna += matriz[j][i]
        if suma_columna != constante:
            es_magico = False
            break
    return es_magico

def determinar_magico_diagonal(matriz,constante):
    es_magico = True
    suma_diagonal = 0
    for i in range(len(matriz)):
        suma_diagonal += matriz[i][i]
    if suma_diagonal != constante:
        es_magico = False
    return es_magico

def determinar_magico_diagonal_inversa(matriz,constante): #la fila aumenta pero la columna disminuye
    es_magico = True
    suma_diagonal = 0
    for i in range(len(matriz)):
        j = len(matriz) - 1 - i
        suma_diagonal += matriz[i][j]
    if suma_diagonal != constante:
        es_magico = False
    return es_magico    
  
#endregion
#region PEDIR y CALCULO
def pedir_dimensiones():
    dimension = input("Ingresa las dimensiones de la matriz,si quieres que sea aleatoria escribe x: ")
    if dimension == "x":
        dimension = random.randint(1,9)
    else:
        dimension = int(dimension)
    return dimension
def determinar_constante(dimension):
    constante = (dimension*(dimension**2 + 1))/2
    return constante

def crear_cuadrado_magico_mostrar():
    dimension = pedir_dimensiones()
    matriz = []
    for i in range(dimension):
        fila =[]
        for j in range(dimension):
            while True:
                valor = int(input(f"ingrese un numero entre 1 y {dimension**2}: "))
                if valor > 0 and valor < (dimension**2)+1 and validar_repetido_matriz(matriz,valor) == False and validar_repetido_fila(fila,valor) == False:
                    print("valor cargado...")
                    fila.append(valor)
                    break
        matriz.append(fila)

    constante = determinar_constante(dimension)
    if determinar_magico_columnas(matriz,constante) and determinar_magico_filas(matriz,constante) and determinar_magico_diagonal(matriz,constante) and determinar_magico_diagonal_inversa(matriz,constante):
        print("La matriz es un cuadrado magico.")
        print(f"La constante magica es {constante}")
    else:
        print("La matriz no es un cuadrado magico.")
        print(f"La constante magica es {constante}")
    mostrar_matriz(matriz)

def main():
    crear_cuadrado_magico_mostrar()

if __name__ == "__main__":
    main()