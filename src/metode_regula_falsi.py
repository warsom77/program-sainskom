import numpy as np

def f(x):
    return ((x * np.exp(-x)) + 1 )

def regulaFalsi(a, b, e, N):
    i = 1
    fa = f(a)
    fb = f(b)
    while(i <= N):
        x = (fb*a - fa*b) / (fb - fa)
        fx = f(x)
        error = abs(fx)
        if (error < e):
            print('|{:3}|{:=9.6f}|{:=9.6f}|{:=9.6f}|{:=9.6f}|{:=9.6f}|{:=9.6f}|'.format(i, a, b, x, fx, fa, fb))
            print("\nAkar persamaan diperoleh di x = ", round(x, 5), " dengan kesalahan = {:.6f}".format(error))
            break
        else:
            print('|{:3}|{:=9.6f}|{:=9.6f}|{:=9.6f}|{:=9.6f}|{:=9.6f}|{:=9.6f}|'.format(i, a, b, x, fx, fa, fb))
        if(fx*fa < 0):
            b = x
            fb = fx
        else:
            a = x
            fa = fx
            
        i += 1

print("======= METODE REGULA FALSI =======")
print("\nPersamaan: (x * e ^ -x) + 1 = 0")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
e = float(input("Masukkan toleransi error: "))
N = int(input("Masukkan iterasi maksimum: "))

print("\n|{:^3}|{:^9}|{:^9}|{:^9}|{:^9}|{:^9}|{:^9}|".format("i", "a", "b", "x", "f(x)", "f(a)", "f(b)"))
print("=================================================================")
regulaFalsi(a, b, e, N)