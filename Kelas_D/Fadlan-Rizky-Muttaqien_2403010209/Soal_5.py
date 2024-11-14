# Fadlan Rizky Muttaqien
# 2403010209
# Meminta input kata dari pengguna
kata = input("Masukkan kata: ")

# Meminta input posisi awal (indeks mulai) dan panjang karakter
posisi_awal = int(input("Masukkan posisi awal: "))
panjang_karakter = int(input("Masukkan panjang karakter: "))

# Mengambil substring sesuai dengan posisi awal dan panjang karakter
substring = kata[posisi_awal : posisi_awal + panjang_karakter]

# Menampilkan substring yang diambil
print("Substring:", substring)
