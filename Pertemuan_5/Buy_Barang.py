# Membaca input jumlah barang (N) dan jumlah pecahan uang (M)
N, M = map(int, input().split())
if not (1 <= N <= 10**4) or not (1 <= M <= 10**4):
    print("Input Invalid: N atau M di luar batas!")
    exit()
    
# Membaca harga barang dan menyimpannya dalam list Pi
Pi = list(map(int, input().split()))

# Membaca pecahan uang dan menyimpannya dalam list Ci
Ci = list(map(int, input().split()))

# Inisialisasi list untuk harga barang dan pecahan uang
Harga_barang = Pi 
Pecahan_uang = Ci

total_harga = 0
for harga in Harga_barang:
    if harga > 0:
        total_harga += harga

total_uang = 0
for uang in Pecahan_uang:
    if uang < 0:
        total_uang += uang
if total_uang == 0:
    total_uang = min(Pecahan_uang)

# Menghitung hutang
Hutang = ( total_uang - total_harga)

# Menampilkan hasil
print(Hutang)
