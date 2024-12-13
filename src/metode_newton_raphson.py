import numpy as np

def f(x):
    return x - np.exp(-x)

def fturunan(x):
    return 1 + np.exp(-x)

def newtonRaphson(e, N, x0):
    i = 1
    while(i <= N):
        fx = f(x0)
        f1x = fturunan(x0)
        xn = x0 - (fx / f1x)
        error = abs(xn - x0)
        if (error < e):
            print('|{:=3}|{:=8.5f}|{:=8.5f}|{:=8.5f}|{:=8.5f}'.format(i, x0, fx, f1x, error))
            print("\nAkar terletak di x = ", round(x0, 5))
            break
        else:
            print('|{:=3}|{:=8.5f}|{:=8.5f}|{:=8.5f}|{:=8.5f}'.format(i, x0, fx, f1x, error))
        x0 = xn
        i += 1
        
print("======= METODE NEWTON RAPHSON =======")
print("\nPersamaan: x - e ^ -x = 0")

e = float(input("Masukkan toleransi error: "))
N = int(input("Masukkan iterasi maksimum: "))
x0 = float(input("Masukkan tebakan awal: "))

print("\n|{:^3}|{:^8}|{:^8}|{:^8}|{:^8}".format("i", "x", "f(x)", "f'(x)", "Error"))
print("========================================")
newtonRaphson(e, N, x0)