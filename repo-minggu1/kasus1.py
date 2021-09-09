L= 0


def InputListKuy(n):
    '''Ini adalah prosedur untuk menginputkan list, tidak ada return disini'''
    # kamus
    global L # untuk merujuk ke variabel global harus di tambah keyword global
    L=[]
    i=0

    #algoritma
    while i < n:
        elem = int(input("inputkan elemen indeks ke-"+str(i)+":"))
        L.append(elem) # isi elemen L yang ada di global
        i+=1

def TampilkanListKuy():
    '''ini adalah prosedur untuk menampil list yang ada di global variabel'''
    global L
    print("List L",L)    

def JumlahkanElemenListDiriSendiridanTetangga():
    '''ini adalah prosedur untuk menjumlahkan setiap elemen list dengan dirinya sendiri dan tetangganya!!'''
    #kamus
    global L
    #algoritma
    for i in range(len(L)):
        for j in range(len(L)):
            print("L_",i,"+L_",j,"=",L[i]+L[j],end=" ")
            print() #tambahkan untuk baris baru
        print() # ketika loop yang paling dalam dengan pencacah j selesai, maka di pindah di baris baru


def JumlahkanElemenTetangga():
    '''Ini adalah prosedur untuk menjumlahkan setiap elemen list dengan list tetangganya!'''
    global L
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            print("L_",i,"+L_",j,"=",L[i]+L[j],end=" ")
            print() #tambahan untuk baris baru
        print()

def TukarElemen(a,b):
    temp=a
    a = b
    b = temp
    return a,b

def TukarElemenTetangga():
    global L
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            print("sebelum tukar L_",i,"=",L[i],",L_",j,"=",L[j],end=" ")
            L[i],L[j] = TukarElemen(L[i],L[j])
            print("sesudah tukar L_",i,"=",L[i],",L_",j,"=",L[j],end=" ")
            print()
        print()
    print(L)
        
def getListdariGlobal():
    global L
    return L