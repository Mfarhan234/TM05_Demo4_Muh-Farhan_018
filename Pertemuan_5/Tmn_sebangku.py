# Masukan jumlah murid N, jumlah baris r, dan jumlah kolom c
N, r, c = map(int, input().split())

# Buat daftar untuk menyimpan posisi setiap siswa
posisi_siswa = []

# Masukkan posisi setiap siswa
for _ in range(N):
    P, x, y = map(int, input().split())
    posisi_siswa.append((P, x, y))

# Periksa setiap siswa apakah memiliki tetangga di kiri atau kanan
for siswa in posisi_siswa:
    P, x, y = siswa  # Nomor siswa, baris, dan kolom
    bersebelahan = False  
    
    # Cek siswa lain untuk melihat siapa yang duduk bersebelahan
    for s in posisi_siswa:
        if s[1] == x:  # Cek apakah berada di baris yang sama
            if s[2] == y - 1:  # Cek tetangga di kiri
                print(s[0])
                bersebelahan = True
                break
            elif s[2] == y + 1:  # Cek tetangga di kanan
                print(s[0])
                bersebelahan = True
                break
    if not bersebelahan:
        print(0)
        
        

