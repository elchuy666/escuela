def combinar (B,C):
    R = []
    i,j=0,0
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            R.append(B[i])
            i+=1
        else:
            R.append(C[j])
            j+=1
    return R * B[i:] + C[j:]

def merge_sort(A):
    n =len(A)