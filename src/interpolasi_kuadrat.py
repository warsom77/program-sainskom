import numpy as np

def f(i, x, y):
    matriksA[i][0] = pow(x, 2)
    matriksA[i][1] = x
    matriksA[i][2] = 1
    matriksB[i][0] = y
    
def ln(xCari, matriksX):
    return matriksX[0][0] * pow(xCari, 2) + matriksX[1][0] * xCari + matriksX[2][0]

print("======= METODE INTERPOLASI KUADRAT =======")
print("\nPersamaan:")
print("============================")
print("| (ax1 ^ 2) + bx1 + c = y1 |")
print("| (ax2 ^ 2) + bx2 + c = y2 |")
print("| (ax3 ^ 2) + bx3 + c = y3 |")
print("============================")

n = int(input("\nMasukkan banyak persamaan: "))
matriksA = np.full((n, 3), 0, dtype=float)
matriksB = np.full((n, 1), 0, dtype=float)
for i in range(n):
    x = float(input(f"Masukkan nilai x{i+1}: "))
    y = float(input(f"Masukkan nilai y{i+1}: "))
    f(i, x, y)
    
xCari = float(input("Masukkan nilai x yang ingin dicari: "))
    
matriksAInverse = np.linalg.inv(matriksA)

print("\nMatriks A =")
print(matriksA)
print("\nMatriks B =")
print(matriksB)
print("\nMatriks A Inverse =")
print(matriksAInverse)

matriksX = np.full((n, 1), 0, dtype=float)
matriksX = np.dot(matriksAInverse, matriksB)
print("\nMatriks X =")
print(matriksX)

result = ln(xCari, matriksX)
print(f"\nHasil dari ln({xCari}) = {round(result, 4)}")