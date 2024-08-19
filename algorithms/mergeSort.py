#divide y venceras
def mergeSort(A):
    if len(A) <= 1:
        return A
    
    medio = len(A)//2
    midIzquierda = A[:medio]
    midDerecha = A[medio:]
    sortedIzquierda = mergeSort(midIzquierda)
    sortedDerecha = mergeSort(midDerecha)

    return merge(sortedIzquierda, sortedDerecha)


def merge(izquierda, derecha):
    resultado = []
    i=j=0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i+=1
        else:
            resultado.append(derecha[j])
            j+=1    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

noOrdenado = [3, 7, 6, -10, 15, 23.5, 55, -13]
ordenado = mergeSort(noOrdenado)

print(ordenado)