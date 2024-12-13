import numpy as np
import math

def f(x):
    return math.cos(x)

def hitung_perbedaan_terbagi(xi, yi, n):
    ST = np.zeros((n, n), dtype=float)
    
    for i in range(n):
        ST[0][i] = (yi[i+1] - yi[i]) / (xi[i+1] - xi[i])
    
    for tingkat in range(1, n):
        for i in range(n - tingkat):
            ST[tingkat][i] = (ST[tingkat-1][i+1] - ST[tingkat-1][i]) / (xi[i+tingkat+1] - xi[i])
    
    return ST

def taksir_derajat_polinom(ST, xi, x, n):
    hasil = np.zeros(n, dtype=float)
    hasil[0] = 1 + ST[0][0] * (x - xi[0])  
    
    for derajat in range(1, n):
        suku = ST[derajat][0]
        for k in range(derajat + 1): 
            suku *= (x - xi[k])
        hasil[derajat] = hasil[derajat - 1] + suku
    
    return hasil

print("======= METODE POLINOM NEWTON =======\n")
print("Persamaan: f(x) = cos(x)")

# Input data
n = int(input("Masukkan banyak derajat polinom: "))
a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
x = float(input("Masukkan x yang ingin ditaksir: "))

# Inisialisasi xi dan yi
xi = np.linspace(a, b, n + 1)
yi = np.array([f(x) for x in xi])

# Hitung tabel perbedaan terbagi
ST = hitung_perbedaan_terbagi(xi, yi, n)

# Hitung nilai taksiran polinomial
derajat = taksir_derajat_polinom(ST, xi, x, n)

# Output hasil
print("\nTabel xi:", xi)
print("Tabel yi:", yi)
print("\nTabel Perbedaan Terbagi (ST):\n", ST)
print("\nHasil Taksiran untuk Derajat Polinom:")
for i, nilai in enumerate(derajat, start=1):
    print(f"Derajat {i}: {nilai}")