# program-sainskom
Repository untuk menyimpan program tugas akhir mata kuliah Sains Komputasi

# Penjelasan Tentang program
## 1. LU Decomposition
Program ini mengimplementasikan metode Dekomposisi LU, yaitu sebuah teknik matematis untuk memecah matriks persegi menjadi tiga matriks: P (matriks permutasi), L (matriks segitiga bawah), dan U (matriks segitiga atas).
[LU_Decomposition.py](https://github.com/warsom77/program-sainskom/blob/main/src/Lu_Decomposition.py)

### Fungsi-fungsi Utama:
1. `mult_matrix(M, N)`: Melakukan perkalian matriks
2. `pivot_matrix(M)`: Membuat matriks pivot untuk mengoptimalkan perhitungan
3. `lu_decomposition(A)`: Melakukan dekomposisi LU pada matriks input

### Proses Kerja:
- Mengambil matriks input A
- Membuat matriks P untuk menukar baris jika diperlukan
- Menghitung matriks L dan U berdasarkan algoritma Doolittle
- Menampilkan matriks A, P, L, dan U

### Contoh yang Digunakan:
Matriks persegi 4x4: `[[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]]`


## 2. Markov Chain
Program ini mensimulasikan Rantai Markov sederhana dengan tiga keadaan: Tidur, Makan Es Krim, dan Lari.
[Markov_Chain.py](https://github.com/warsom77/program-sainskom/blob/main/src/Markov_Chain.py)

### Konsep Utama:
1. Terdapat tiga keadaan: Sleep (Tidur), Icecream (Makan Es Krim), Run (Lari)
2. Matriks transisi menentukan probabilitas perpindahan antar keadaan
3. Fungsi `activity_forecast(days)` mensimulasikan aktivitas selama sejumlah hari

### Proses Simulasi:
- Memulai dari keadaan awal "Tidur"
- Menggunakan matriks transisi untuk menentukan aktivitas berikutnya
- Menghitung probabilitas perpindahan antar keadaan
- Melakukan 10.000 simulasi untuk 2 hari
- Menghitung probabilitas akhir berada di keadaan "Lari"

### Matriks Transisi:
```
[[0.2, 0.6, 0.2],  # Dari Tidur
 [0.1, 0.6, 0.3],  # Dari Lari
 [0.2, 0.7, 0.1]]  # Dari Es Krim
```


## 3. Monte Carlo
Program ini menggunakan metode Monte Carlo untuk mengestimasi nilai Pi dengan mensampel titik-titik acak dalam persegi.
[Monte_Carlo.py](https://github.com/warsom77/program-sainskom/blob/main/src/Monte_Carlo.py)

### Proses Utama:
1. Generate titik-titik acak dalam persegi berukuran 2x2 yang terpusat di (0,0)
2. Menghitung berapa banyak titik yang berada di dalam lingkaran unit
3. Membandingkan rasio titik dalam lingkaran terhadap total titik
4. Menggunakan rasio tersebut untuk mengestimasi nilai Pi

### Langkah Simulasi:
- Input jumlah total titik acak dari pengguna
- Hasilkan titik `x` dan `y` secara acak antara -1 dan 1
- Hitung apakah titik berada di dalam lingkaran unit `(x² + y² ≤ 1)`
- Buat visualisasi titik-titik menggunakan matplotlib
- Tampilkan perbandingan estimasi Pi dengan nilai sebenarnya

### Visualisasi:
- Titik merah: di dalam lingkaran
- Titik biru: di luar lingkaran
- Lingkaran hijau: batas lingkaran unit
- Garis hitam: pembagi kuadran

Setiap program ini mendemonstrasikan teknik komputasi berbeda:
- Dekomposisi Matriks
- Rantai Markov
- Simulasi Monte Carlo

Metode-metode ini umum digunakan dalam berbagai bidang seperti matemátika, fisika, statistik, dan pemodelan komputasi.
Program ini mengadaptasi kode dari [jfaraudo/MonteCarlo-example](https://github.com/jfaraudo/MonteCarlo-example).


## 4. Metode Tabel 
Program ini memecahkan persamaan `𝑥 + 𝑒^𝑥 = 0` menggunakan Metode Tabel. Metode ini membuat tabel nilai fungsi `𝑓(𝑥)` dalam interval tertentu dan mencari akar berdasarkan perubahan tanda `𝑓(𝑥)`.
[metode_table.py](https://github.com/warsom77/program-sainskom/blob/main/src/metode_table.py)

### Fungsi-fungsi Utama:
1. `fungsi(x)`: Menghitung nilai fungsi `𝑓(𝑥)` untuk setiap titik `𝑥`.
2. `tabel_nilai(a, b, N)`: Membuat tabel nilai `𝑓(𝑥)` dalam interval `[𝑎, 𝑏]` dengan pembagian interval sebanyak `𝑁`.
3. `cari_akar(a, b, N)`: Mencari akar persamaan berdasarkan perubahan tanda `𝑓(𝑥)` di tabel.

### Proses Kerja:
- Meminta input batas bawah `(𝑎)`, batas atas `(𝑏)`, dan jumlah pembagian interval `(𝑁)`.
- Menghitung nilai `𝑓(𝑥)` di setiap titik dalam interval.
- Mencari akar berdasarkan perubahan tanda fungsi `𝑓(𝑥)`.
- Menampilkan tabel nilai `𝑥` dan `𝑓(𝑥)`, serta akar terdekat dengan nol.

### Contoh yang Digunakan:
Interval: [−1, 0], Pembagian Interval: 10.


## 5. Metode Bisection (Biseksi) 
Program ini menggunakan Metode Bisection untuk mencari akar persamaan non-linear `𝑓(𝑥) = 0`. Metode ini membagi interval `[𝑎, 𝑏]` menjadi dua bagian dan memilih subinterval yang mengandung akar berdasarkan perubahan tanda `𝑓(𝑥)` di kedua ujung interval.
[metode_biseksi.py](https://github.com/warsom77/program-sainskom/blob/main/src/metode_biseksi.py)

### Fungsi-fungsi Utama:
1. `fungsi(x)`: Menghitung nilai fungsi `𝑓(𝑥)`.
2. `bisection(a, b, e, N)`: Melakukan iterasi bisection untuk mencari akar persamaan.
3. `tabel_iterasi(a, b, x, fx, fa)`: Menampilkan tabel iterasi yang berisi nilai `𝑎, 𝑏, 𝑥, 𝑓(𝑥),` dan `keterangan` perubahan tanda.

### Proses Kerja:
- Meminta input batas bawah `(𝑎)`, batas atas `(𝑏)`, toleransi error `(𝑒)`, dan jumlah iterasi maksimum `(𝑁)`.
- Menghitung nilai fungsi `𝑓(𝑥)` di titik tengah interval.
- Memeriksa perubahan tanda pada interval dan memilih subinterval yang mengandung akar.
- Menampilkan tabel iterasi dan hasil akhir akar yang ditemukan.

### Contoh yang Digunakan:
Interval: [-1, 0], Toleransi Error: 0.001, Iterasi Maksimum: 10.


## 6. Metode Regula Falsi
Program ini menggunakan Metode Regula Falsi untuk mencari akar persamaan `𝑓(𝑥) = 0`. Metode ini menggunakan garis lurus (sekant) untuk memperkirakan akar persamaan.
[metode_regula_falsi.py](https://github.com/warsom77/program-sainskom/blob/main/src/metode_regula_falsi.py)

### Fungsi-fungsi Utama:
1. `fungsi(x)`: Menghitung nilai fungsi `𝑓(𝑥)`.
2. `regula_falsi(a, b, e, N)`: Melakukan iterasi menggunakan metode Regula Falsi untuk mencari akar.
3. `tabel_iterasi(a, b, x, fx, fa, fb)`: Menampilkan tabel iterasi yang berisi nilai `𝑎, 𝑏, 𝑥, 𝑓(𝑥), 𝑓(𝑎),` dan `𝑓(𝑏)`.

### Proses Kerja:
- Meminta input batas bawah `(𝑎)`, batas atas `(𝑏)`, toleransi error `(𝑒)`, dan jumlah iterasi maksimum `(𝑁)`.
- Menghitung nilai fungsi pada titik `𝑎` dan `𝑏`.
- Menghitung nilai `𝑥` menggunakan rumus Regula Falsi dan memeriksa perubahan tanda.
- Menampilkan tabel iterasi dan hasil akhir akar yang ditemukan.

### Contoh yang Digunakan:
Interval: [0, -1], Toleransi Error: 0.0001, Iterasi Maksimum: 20.


## 7. Metode Iterasi Sederhana
Program ini menggunakan Metode Iterasi Sederhana untuk memecahkan persamaan `𝑥 + 𝑒^𝑥 = 0` dengan cara mengubah bentuk persamaan menjadi `𝑥 = 𝑔(𝑥)` dan menghitung solusi iteratif hingga mencapai toleransi error tertentu.
[metode_iterasi_sederhana.py](https://github.com/warsom77/program-sainskom/blob/main/src/metode_iterasi_sederhana.py)

### Fungsi-fungsi Utama:
1. `fungsi(x)`: Menghitung nilai fungsi `𝑓(𝑥)`.
2. `iterasi_sederhana(e, N, x0)`: Melakukan iterasi sederhana untuk mencari akar persamaan.
3. `tabel_iterasi(i, x, gx, fx)`: Menampilkan tabel iterasi yang berisi nilai `𝑥, 𝑔(𝑥),` dan `𝑓(𝑥)`.

### Proses Kerja:
- Meminta input toleransi error `(𝜖)`, jumlah iterasi maksimum `(𝑁)`, dan tebakan awal `(𝑥0)`.
- Menghitung nilai `𝑔(𝑥)` dan `𝑓(𝑥)` pada setiap iterasi.
- Menampilkan tabel iterasi dan nilai akar jika konvergen.

### Contoh yang Digunakan:
Toleransi Error: 0.0001, Iterasi Maksimum: 10, Tebakan Awal: −1.


## 8. Metode Newton-Raphson
Program ini menggunakan Metode Newton-Raphson untuk menemukan akar persamaan `𝑓(𝑥) = 0` dengan pendekatan iteratif menggunakan turunan pertama dari fungsi.
[metode_newton_raphson.py](https://github.com/warsom77/program-sainskom/blob/main/src/metode_newton_raphson.py)

### Fungsi-fungsi Utama:
1. `fungsi(x)`: Menghitung nilai fungsi `𝑓(𝑥)`.
2. `turunan_fungsi(x)`: Menghitung turunan pertama dari fungsi `𝑓(𝑥)`.
3. `newton_raphson(e, N, x0)`: Melakukan iterasi menggunakan rumus Newton-Raphson untuk mencari akar.

### Proses Kerja:
- Meminta input toleransi error `(𝑒)`, jumlah iterasi maksimum `(𝑁)`, dan tebakan awal `(𝑥0)`.
- Menghitung fungsi dan turunannya pada setiap iterasi.
- Menampilkan tabel iterasi dan hasil akhir akar yang ditemukan.

### Contoh yang Digunakan:
Toleransi Error: 0.00001, Iterasi Maksimum: 10, Tebakan Awal: 0.


## 9. Metode Interpolasi Linier
Program ini menggunakan Metode Interpolasi Linier untuk memperkirakan nilai `𝑓(𝑥)` pada titik tertentu berdasarkan dua titik sampel terdekat.
[interpolasi_linier.py](https://github.com/warsom77/program-sainskom/blob/main/src/interpolasi_linier.py)

### Fungsi-fungsi Utama:
1. `interpolasi_linier(x0, x1, fx0, fx1, a)`: Menghitung nilai interpolasi linier `𝑓(𝑎)`.
2. `tabel_sampel(xi, fxi)`: Menampilkan tabel sampel yang berisi nilai `𝑥` dan `𝑓(𝑥)`.

### Proses Kerja:
- Meminta input jumlah sampel `𝑛 `dan nilai `𝑥𝑖` serta `𝑓(𝑥𝑖)` untuk setiap titik data.
- Menampilkan tabel sampel dan menghitung interpolasi linier berdasarkan dua titik terdekat.

### Contoh yang Digunakan:
Sampel: 2 titik, Interpolasi pada 𝑎 = 45.


## 10. Metode Interpolasi Kuadrat
Program ini menggunakan Metode Interpolasi Kuadrat untuk menentukan nilai `𝑓(𝑥)` pada titik tertentu berdasarkan tiga persamaan kuadrat.
[interpolasi_kuadrat.py](https://github.com/warsom77/program-sainskom/blob/main/src/interpolasi_kuadrat.py)

### Fungsi-fungsi Utama:
1. `interpolasi_kuadrat(xi, yi)`: Menghitung nilai interpolasi kuadrat menggunakan metode matriks.
2. `matriks_A(xi)`: Membuat matriks `A` berdasarkan koefisien persamaan kuadrat.
3. `matriks_B(yi)`: Membuat matriks `B` berdasarkan nilai `𝑦`.

### Proses Kerja:
- Meminta input jumlah persamaan `(𝑛 ≥ 3)`, dan nilai `𝑥𝑖` dan `𝑦𝑖` untuk setiap persamaan.
- Membentuk Matriks `A` dan `B`, menghitung Matriks `X`, dan menentukan nilai interpolasi.

### Contoh yang Digunakan:
Persamaan kuadrat: 3 titik data, Interpolasi pada 𝑎 = 9.2.

## 11. Polinom Newton 
Program ini menggunakan Metode Polinom Newton untuk interpolasi berdasarkan sejumlah titik data `𝑥𝑖` dan `𝑦𝑖`.
[polinom_newton.py](https://github.com/warsom77/program-sainskom/blob/main/src/polinom_newton.py)

### Fungsi-fungsi Utama:
1. `polinom_newton(xi, yi, a)`: Menghitung nilai interpolasi menggunakan polinom Newton.

### Proses Kerja:
- Meminta input titik data `𝑥𝑖` dan `𝑦𝑖` untuk setiap persamaan.
- Menghitung nilai interpolasi berdasarkan polinom Newton pada titik tertentu.

### Contoh yang Digunakan:
Interpolasi pada 𝑎 = 2.5, dengan titik data (x,y).


## 12. Metode Iterasi Jacobi
Program ini mengimplementasikan Metode Iterasi Jacobi, sebuah algoritma untuk menyelesaikan sistem persamaan linear berbentuk `Ax=b`. Berikut adalah penjelasan detail tentang kode ini:
[Metode_Iterasi_Jacobi.py](https://github.com/warsom77/program-sainskom/blob/main/src/Metode_Iterasi_Jacobi.py)

### Fungsi jacobi:
Fungsi ini menyelesaikan sistem persamaan linear menggunakan metode iterasi Jacobi.

### Parameter:
`A`: Matriks koefisien (harus berbentuk matriks persegi).
`b`: Vektor konstanta.
`N`: Jumlah iterasi (default: 25).
`x`: Vektor tebakan awal untuk solusi (default: None, yang berarti akan diisi dengan nol).

### Langkah-langkah Algoritma:
- Ekstraksi diagonal dari matriks A: Elemen diagonal dari A disimpan dalam vektor D.
- Matriks A dikurangi elemen diagonalnya menjadi matriks residu R.

### Iterasi Jacobi:
Pada setiap iterasi, solusi diperbarui menggunakan rumus: `x=b−R⋅x/D` Proses ini dilakukan sebanyak `N` kali.

### Hasil:
Fungsi mengembalikan vektor solusi `x`.


## 13. Matriks
Program ini menunjukkan berbagai operasi pada matriks menggunakan pustaka NumPy. 
[Matriks.py](https://github.com/warsom77/program-sainskom/blob/main/src/Matriks.py)
### Berikut operasi-operasinya:
### - Operasi Penjumlahan dan Pengurangan Matriks
#### Matriks:
```
A = [4, 5, 6], 
    [7, 8, 9]
B = [1, 2, 3],
    [1, 2, 3]
```

#### Operasi:
- Penjumlahan: `A+B`
- Pengurangan: `A−B` 

#### Hasil:
Penjumlahan dan pengurangan dilakukan elemen-per-elemen karena kedua matriks memiliki dimensi yang sama (2x3).

### - Perkalian Matriks
#### Matriks:
```
A = [1, 2], 
    [3, 4],
    [5, 6]  # 3x2
B = [10, 12, 12],
    [13, 14, 15]  # 2x3
```

#### Operasi:
Perkalian matriks: `A⋅BA⋅B` menggunakan `A @ B` atau `np.matmul(A, B)`.

#### Hasil:
Matriks hasil berukuran 3×3, mengikuti aturan dimensi: (3×2).(2×3)=(3×3)

### - Transpose Matriks
#### Matriks:
```
A = [1, 2], 
    [3, 4],
    [5, 6]
```

#### Operasi:
Transpose matriks ATAT menggunakan `A.transpose()`.

#### Hasil:
Matriks diubah dari 3×2 menjadi 2×3.

### - Determinan Matriks
#### Matriks:
```
A = [5, 0, 1],
    [3, 2, 2],
    [1, 4, 2]
B = [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
```

#### Operasi:
Determinan matriks AA dan BB menggunakan `np.linalg.det(A)`.

#### Hasil:
- Determinan A valid karena A adalah matriks persegi.
- Determinan B valid tetapi hasilnya 0 (karena B singular).

### - Invers Matriks
#### Matriks:
```
A = [5, 0, 1],
    [3, 2, 2],
    [1, 4, 2]  # invertible
B = [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]  # singular
```

#### Operasi:
- Invers matriks A menggunakan `np.linalg.inv(A)`.
- Invers matriks B menghasilkan error karena B singular (determinan = 0).

### - Verifikasi Invers
#### Operasi:
Memverifikasi `A*A^−1` dan `A^−1*A`, yang seharusnya menghasilkan matriks identitas.

#### Hasil:
Diperoleh matriks identitas II dengan elemen diagonal bernilai 1.


## 14. Eliminasi Gauss
Program ini adalah program Python untuk melakukan eliminasi Gauss. Berikut adalah ringkasan kodenya:
[Eliminasi_Gauss.py](https://github.com/warsom77/program-sainskom/blob/main/src/Eliminasi_Gauss.py)

### Fungsi utama: 
`gaussElim(a, b)`: Fungsi ini menerima dua parameter yaiut `a`(matriks koefisien) dan `b`(vektor konstanta).

#### Proses:
- `Eliminasi maju (Forward Elimination)`: Mengubah matriks menjadi bentuk segitiga atas dengan operasi baris elementer.
- `Substitusi balik (Backward Substitution)`: Menghitung nilai variabel dari atas ke bawah menggunakan matriks segitiga atas.

### Input awal:
```
Matriks a adalah:
[ 1.0,  1.0,  1.0],
[ 1.0, -1.0, -1.0],
[ 1.0, -2.0,  3.0]

Vektor b adalah [1.0, 1.0, -5.0].
```

### Output:
- Setelah eliminasi dan substitusi, nilai dari variabel disimpan dalam x.
- Skrip juga mencetak matriks a setelah diubah, vektor hasil x, dan hasil cek kesalahan numerik dengan menghitung perbedaan [a]{x} - b.


### Fitur tambahan:
- Bagian untuk menghitung determinan matriks ada, tetapi dikomentari.
- Menggunakan fungsi dari pustaka numpy untuk operasi matriks dan vektor.