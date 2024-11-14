# Meminta input dari pengguna
kata = input("Masukkan sebuah kata: ")
posisi_awal = int(input("Masukkan posisi awal (indeks mulai dari 0): "))
panjang_karakter = int(input("Masukkan panjang karakter yang ingin diambil: "))

# Mengambil substring sesuai dengan posisi awal dan panjang karakter
substring = kata[posisi_awal:posisi_awal + panjang_karakter]

# Menampilkan hasil
print("Substring yang diambil:", substring)