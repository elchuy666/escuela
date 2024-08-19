def isnertion_sort(A):
    for i in range(1,len(A)):
        j = i
        while j-1 >= 0 and A[j] < A[j-i]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
