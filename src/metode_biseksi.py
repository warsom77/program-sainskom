import numpy as np

def f(x):
    return ((x * np.exp(-x)) + 1 ) 

def biseksi(a, b, e, N):
    i = 1
    iterasi = 0
    akar = 0
    keterangan = ""
    while(i <= N):
        fa = f(a)
        fb = f(b)

        if (fa * fb) > 0:
            break
        
        x = (a + b) / 2
        fx = f(x)
        keterangan = "berlawanan tanda" if (fx * fa) < 0 else ""
        print('|{:3}|{:=7.6f}|{:=7.6f}|{:=7.6f}|{:=10.6f}|{:=10.6f}|{:16}|'.format(i, a, b, x, fx, fa, keterangan))
        if (fx * fa) < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
            
        if abs(fx) < e:
            iterasi = i
            akar = x
            fakar = fx
            break
        
        i += 1
    
    print("\nPada iterasi ke ", iterasi, "diperoleh x = ", round(akar, 5), " dengan f(x) = ", round(fakar, 5))

print("======= METODE BISEKSI =======")
print("\nPersamaan: (x * e ^ -x) + 1 = 0")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
e = float(input("Masukkan toleransi error: "))
N = int(input("Masukkan iterasi maksimum: "))

print("\n|{:^3}|{:^9}|{:^9}|{:^9}|{:^10}|{:^10}|{:^16}|".format("i", "a", "b", "x", "f(x)", "f(a)", "Keterangan"))
print("==========================================================================")
biseksi(a, b, e, N)