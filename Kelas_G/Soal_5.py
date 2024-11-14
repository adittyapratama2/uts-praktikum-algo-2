# Program untuk mengambil substring dari kata berdasarkan posisi awal dan panjang karakter

# Meminta input dari pengguna
kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal: "))
panjang = int(input("Masukkan panjang karakter: "))

# Mengambil substring sesuai posisi awal dan panjang karakter
substring = kata[posisi_awal:posisi_awal+panjang]

# Menampilkan hasil substring
print("Substring yang diambil:", substring)
