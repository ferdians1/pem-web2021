import random

def nilaimax():
    a = int(input('masukan bilangan ke-1: '))
    b = int(input('masukan bilangan ke-2: '))
    c = int(input('masukan bilangan ke-3: '))
 
    # menentukan nilai bilangan
    if a > b and a > c:
        maks = a
    else:
        if b > a and b > c:
            maks = b
        else:
            maks = c
 
    # cetak nilai bilangan
    print('Bilangan Terbesar adalah:  %d' % maks) 