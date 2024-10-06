r, c, N = map(int, input().split())  # input ukuran hutan dan jumlah gerakan
emas_petak = []

# Masukkan grid ke dalam list
for i in range(r):
    matrix = list(map(int, input().split()))
    emas_petak.append(matrix)

arah_gerakan = input()  # input arah gerakan

x, y = 0, 0
total_emas = emas_petak[x][y]  # emas awal di posisi (0, 0)
emas_petak[x][y] = 0  # emas diambil, set menjadi 0
gerakan = 1 

for langkah in arah_gerakan:
    if langkah == 'R':  # Gerakan ke kanan
        if y + 1 < c:  # cek apakah masih di dalam batas kolom
            y += 1
            total_emas += emas_petak[x][y] + 3  # tambahkan emas di petak + bonus
            emas_petak[x][y] = 0  # emas di petak baru diambil
        else:
            gerakan = 0  # keluar dari batas
            break
    elif langkah == 'L':  # Gerakan ke kiri
        if y - 1 >= 0:  # cek apakah masih di dalam batas kolom
            y -= 1
            total_emas += emas_petak[x][y] - 2  # kurangi emas di petak
            emas_petak[x][y] = 0  # emas di petak baru diambil
        else:
            gerakan = 0  # keluar dari batas
            break
    elif langkah == 'D':  # Gerakan ke bawah
        if x + 1 < r:  # cek apakah masih di dalam batas baris
            x += 1
            total_emas += emas_petak[x][y] - 2  # kurangi emas di petak
            emas_petak[x][y] = 0  # emas di petak baru diambil
        else:
            gerakan = 0  # keluar dari batas
            break
    elif langkah == 'U':  # Gerakan ke atas
        if x - 1 >= 0:  # cek apakah masih di dalam batas baris
            x -= 1
            total_emas += emas_petak[x][y] + 3  # tambahkan emas di petak + bonus
            emas_petak[x][y] = 0  # emas di petak baru diambil
        else:
            gerakan = 0  # keluar dari batas
            break

print(langkah, x, y, total_emas)

if gerakan:
    print(total_emas)
else:
    print("gerakanmu salah bung!")
