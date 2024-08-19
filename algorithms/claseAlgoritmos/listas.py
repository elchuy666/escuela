import numpy as np
import math as meth
import matplotlib as plot

#las listas si importan el orden

misCachorros = [["Camilo", 10.8, 1], ["Milo", 8.3, 2], ["elPP", 12.3, 3]]

#cuando dices que una variable es igual a otra, haces una referencia

var1 = 1
var2 = var1

var2 = 10 

# vector por escalar

# investigar multiplicacion de matrices

matriz1 = [[1,2],
          [3,4],]

matriz2 = [[2,1],
          [1,5],]

def getC_fila_cola(matriz1, matriz2, fila, columna):
    aux =0
    for i in range(len(matriz1)):
        aux += matriz1[fila][i] * matriz2[i][columna]
    return aux

print(getC_fila_cola(matriz1, matriz2, 1, 1))

def multiplicar_matrices(matriz1, matriz2):
    fila = 1
    lista =[]
    for i in range(len(matriz1)):
        lista.append(getC_fila_cola(matriz1, matriz2, fila, i))
    print(lista)

multiplicar_matrices(matriz1, matriz2)