import numpy as np

def table(a, b, N):
    h = (b-a) / N
    i = 0
    hasil = 0
    hasily = 0
    while(i <= N and a < b):
        x = a + i * h
        y1 = (x + (np.exp(1)**x))
        y2 = ((x+1) + (np.exp(1)**(x+1)))
        
        if y1 == 0:
            hasil = x
        elif (y1*y2) < 0:
            if abs(y1) < abs(y2):
                hasil = x
                hasily = y1
            else:
                hasil = x+1
        print('|{:3}|{:=8.5f}|{:=8.5f}|'.format(i, x, y1))
        i += 1
    
    if a > b:
        print("\nBatas bawah tidak boleh lebih besar dari batas atas")
    else:
        print("\nPenyelesaian terdekat dengan nol pada x = ", round(hasil, 2), " dengan f(x) =  ", round(hasily, 5))

print("======= METODE TABLE =======")
print("\nPersamaan: x + e ^ x = 0")

a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
N = int(input("Masukkan jumlah pembagian: "))

print("\n|{:^3}|{:^8}|{:^8}|".format("i", "x", "f(x)"))
print("=======================")
table(a, b, N)