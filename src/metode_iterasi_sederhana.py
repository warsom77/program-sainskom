import numpy as np

def f(x):
    return x + np.exp(x)

def g(x):
    return -np.exp(x)

def iterasiSederhana(e, N, x0):
    i = 1
    while (i <= N):
        gx = g(x0)
        fx = abs(f(gx))
        if fx < e:
            print("\nAkar adalah x = ", round(gx, 5))
            break
        print('|{:=3}|{:=8.5f}|{:=8.5f}|{:=8.5f}|'.format(i, x0, gx, fx))
        x0 = gx
        i += 1

print("======= METODE ITERASI SEDERHANA =======")
print("\nPersamaan: x + e ^ x = 0")

e = float(input("Masukkan toleransi error: "))
N = int(input("Masukkan iterasi maksimum: "))
x0 = float(input("Masukkan tebakan awal: "))

print("\n|{:^3}|{:^8}|{:^8}|{:^8}|".format("i", "x", "g(x)", "f(x)"))
print("================================")
iterasiSederhana(e, N, x0)