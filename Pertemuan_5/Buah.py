# Membaca input
N, K = map(int, input().split())

if not(1 <= N <= 10**5) or not(1 <= K <= 10**12):
    print("Input Invalid")
    exit()
    
harga_buah = list(map(int, input().split()))

for harga in harga_buah :
    if not(1 <= harga <= 10**12):
        print("Input Invalid")
        exit()
        
jumlah_buah_dibeli = 0   
# Cek setiap harga buah apakah bisa dibeli
for harga in harga_buah:
    if K >= harga: # Jika uang cukup untuk membeli buah ini
        jumlah_buah_dibeli += 1# Hitung buah yang bisa dibeli

print(jumlah_buah_dibeli)