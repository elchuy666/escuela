#solucion recursiva

def busqueda(A, principio,final,x):
    if final > principio: 
        medio = (final + principio)//2

        if A[medio] == x: return medio
        
        elif A[medio]>x:return busqueda(A,principio,medio-1,x)
        else: return busqueda(A,medio+1,final,x)
    else: return -1

#solucion iterativa jsjsjs

# def busqueda2(A,x):
#     inicio = 0
#     final = len(A) - 1
#     medio = 0
#     while inicio <= final:
#         medio = (final - inicio)//2
#         if A[medio] < x: inicio = medio +1
#         elif A[medio]>x: final = medio - 1
#         else: return medio
#     return -1