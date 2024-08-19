import random

def quick_sort(A):
    if len(A) < 2:
        n = random.choice(A) 
        grande=[a for a in A if a>n]
        iguales =[a for a in A if a==n]
        chico=[a for a in A if a<n]
    grande = quick_sort(grande)
    chico = quick_sort(chico)

    return chico + iguales + grande


def quick_sort2 (A):
    pivote = random.choice(A)
    chicos,iguales,grandes = [], [], []
    for a in A:
        if a > pivote: grandes.append(a)
        elif a < pivote: chicos.append(a)
        else: iguales.append(a)
    chicos = quick_sort2(chicos)
    grandes = quick_sort2(grandes)
    return chicos + iguales + grandes  