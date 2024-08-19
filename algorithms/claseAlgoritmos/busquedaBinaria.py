#iterativa

def busqueda(A, len, e):
    a = 0
    b = len - 1
    while a!=b:
        m = (a+b)/2
        if A[a] == e:
            1
        else:
            if e < A[a]:
                b = m
            else:
                a = m
    return 0


#recursiva

def busquedaRec(A, a, b, e):
    if a==b:
        if e == A[a]:
            return 1
        else:
            return 0
    m = (a+b)/2

    if e < m:
        busqueda(A, a, m, e)
    else:
        busqueda(A, m, b, e)
