# Meminta input kata dari pengguna
kata = input("Masukkan kata: ")

# Meminta input posisi awal dan panjang substring
posisi_awal = int(input("Masukkan posisi awal (indeks mulai dari 0): "))
panjang = int(input("Masukkan panjang karakter yang ingin diambil: "))

# Mengambil substring sesuai dengan posisi awal dan panjang
substring = kata[posisi_awal : posisi_awal + panjang]

# Menampilkan hasil substring
print("Substring yang diambil:", substring)
