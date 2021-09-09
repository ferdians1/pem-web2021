from kasus1 import *
from Sorting import *

def main():
    n=int(input("inputkan panjang list:"))
    InputListKuy(n)
    TampilkanListKuy()
    L=getListdariGlobal()
    print("sort3")
    LL=sort3(L,"asc")
    print(LL)
    print("sort4")
    print(Sort4(L,"desc",2))
    print("sort2")
    LL=Sort2(L,"desc")
    print(LL)
    print(Sort2(L,"desc"))
    print("sort1")
    print(Sort1(L,"asc"))
    #TukarElemenTetangga()
    JumlahkanElemenListDiriSendiridanTetangga()
    #print("pisah")
    #JumlahkanElemenTetangga()

if __name__ == '__main__':
    main()
    
