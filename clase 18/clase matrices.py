
matriz_a= [[1,2,3] ,
           [4,5,6],
           [7,8,9]]

matriz_b = [[9,8,7],
            [6,5,4],
            [3,2,1]]

matriz_resultado = [[0,0,0],  #hacerlo asi o crear una funcion que me cree una matriz
                    [0,0,0],
                    [0,0,0]]

# for i in range(len(matriz_a)):
#     fila = []
#     for j in range(len(matriz_a[i])):
#         suma = matriz_a[i][j] + matriz_b[i][j]
#         fila.append(suma)
#     matriz_resultado.append(fila)
resultado = []
x = matriz_a
y = matriz_b

for i in range(len(x)):
    if len(x[i]) == len(y):
        filas =[]
        for j in range(len(y[0])):
            filas.append(0)
        resultado.append(filas)


for i in range(len(x)):
    for j in range(len(y[i])):
        for k in range(len(x)):
            resultado[i][j]+= matriz_a[i][k]*matriz_b[k][j]

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()
mostrar_matriz(resultado)        
#Matriz RESULTANTE con el mismo numero de FILAS que la primera y mismas COLUMNAS que la segunda.

