def Sort1(A,ket):
    #kamus lokal
    i = 0
    n = len(A)

    #algoritma
    for i in range(n):
        min_idx = i
        for j in range(i+i, len(A)):
            if A[min_idx] > A[j] and ket=="asc":
                min_idx = j
            if A[min_idx] < A[j] and ket=="desc":
                min_idx = j
            A[i], A[min_idx]= A[min_idx],A[i]

        return A


def Sort2(A,ket):
    #kamus lokal
    i = 0
    n = len(A)
    newA = []

    #algoritma
    for i in range(n):
        if A[i]%2==1:
            newA.append(A[i])

        for i in range(len(newA)):
            min_idx = i
        for j in range(i+i, len(newA)):
            if newA[min_idx] > newA[j] and ket=="asc":
                min_idx = j
            if newA[min_idx] < newA[j] and ket=="desc":
                min_idx = j
            newA[i], newA[min_idx]= newA[min_idx],newA[i]

        return newA


def sort3(A,ket):
    #kamus lokal
    n=len(A)
    temp = 0

    #algoritma
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j>=0 and temp < A[j] and ket=="asc":
            A[j+1] = A[j]
            j = j-1
        while j>=0 and temp > A[j] and ket=="desc":
            A[j+1] = A[j]
            j = j-1
        A[j-1]=temp
    return A


def Sort4(A,ket,prio):
    # kamus lokal 
    n = len(A)
    temp = 0
    newA=[]

    #algoritma
    for i in range(n):
        if A[i]%prio==0:
            newA.append(A[i])

    n = len(newA)

    for i in range(1,n):
        temp = newA[i]
        j = i-1
        while j>=0 and temp > newA[j] and ket=="asc":
            newA[j+1] = newA[j]
            j = j-1
        while j>=0 and temp > newA[j] and ket=="desc":
            newA[j+1] = newA[j]
            j = j-1
        newA[j+1]=temp
    return newA


        