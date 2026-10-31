import random
#region MOSTRAR

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print("---" * len(matriz) * 3)
        for j in range(len(matriz[0])):
            print(f"| {matriz[i][j]:^5}" ,end=" ")
        print("|")
    print("---" * len(matriz) * 3)
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
"""GUIAS PARA EL MOVIMIENTO ENTRE MATRIZ
   0 1 2
0 [1,2,3]
1 [4,5,6]
2 [7,8,9]
"""
def determinar_magico_diagonal_inversa(matriz,constante):
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
#endregion

#region CREACION
def crear_cuadrado_magico_mostrar():
    dimension = pedir_dimensiones()
    automatico = input("Quieres que sea automatico? ingresa si o no: ")
    bandera = False
    while bandera == False:
        matriz = []
        for i in range(dimension):
            fila =[]
            for j in range(dimension):
                while True:
                    if automatico == "no":
                        valor = int(input(f"ingrese un numero entre 1 y {dimension**2}: "))
                    else:
                        valor = random.randint(1, dimension**2)
                    if valor > 0 and valor < (dimension**2)+1 and validar_repetido_matriz(matriz,valor) == False and validar_repetido_fila(fila,valor) == False:
                        if automatico == "no":
                            print("valor cargado...")
                        fila.append(valor)
                        break
            matriz.append(fila)

        constante = determinar_constante(dimension)
        if determinar_magico_columnas(matriz,constante) and determinar_magico_filas(matriz,constante) and determinar_magico_diagonal(matriz,constante) and determinar_magico_diagonal_inversa(matriz,constante):
            print("La matriz es un cuadrado magico.")
            print(f"La constante magica es {constante}")
            bandera = True

        else:
            if automatico == "no":
                print("La matriz no es un cuadrado magico.")
                print(f"La constante magica es {constante}")
        if bandera == True or automatico == "no":
            mostrar_matriz(matriz)
#endregion
def main():
    crear_cuadrado_magico_mostrar()

if __name__ == "__main__":
    main()