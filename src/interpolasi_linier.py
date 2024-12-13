def sample(n):
    i = 0
    while(i < n):
        x[i] = float(input(f"Masukkan sample x ke-{i+1}: "))
        fx[i] = float(input(f"Masukkan sample f(x) ke-{i+1}: "))
        i += 1
    
    i = 0
    print("\nTABEL SAMPLE")
    print("|{:^5}|{:^6}|".format("x", "f(x)"))
    print("==============")
    while(i < n):
        print('|{:=5}|{:=6}|'.format(x[i], fx[i]))
        i += 1
        
def interpolasiLinier(a, n):
    for i in range(n):
        if a > x[i] and a < x[i+1]:
            x0 = x[i]
            x1 = x[i+1]
            fx0 = fx[i]
            fx1 = fx[i+1]
            break
        
    fa = fx0 + (fx1-fx0)/(x1-x0)*(a-x0)
    print("\nTABEL HASIL")
    print("|{:^5}|{:^6}|{:^6}|{:^7}|{:^7}|{:^6}|".format("x", "x0", "x1", "f(x0)", "f(x1)", "f(x)"))
    print("============================================")
    print('|{:=5}|{:=6}|{:=6}|{:=7}|{:=7}|{:=6}|'.format(a, x0, x1, fx0, fx1, fa))
    print(f"\nNilai f(x) dari x = {a} adalah {fa}")
            

print("======= METODE INTERPOLASI LINIER =======")

n = int(input("\nMasukkan banyak sample: "))
x = [0] * n
fx = [0] * n
a = float(input("Masukkan nilai x yang ingin dicari: "))

sample(n)
interpolasiLinier(a, n)