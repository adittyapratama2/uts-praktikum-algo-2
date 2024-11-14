# Meminta input kata dari user
kata = input("Masukkan kata: ")

# Meminta input posisi awal (dimulai dari 0) dan panjang karakter
posisi_awal = int(input("Masukkan posisi awal: "))
panjang_karakter = int(input("Masukkan panjang karakter: "))

# Mengambil substring dari kata berdasarkan posisi awal dan panjang karakter
substring = kata[posisi_awal:posisi_awal + panjang_karakter]

# Menampilkan substring yang diambil
print("Substring:", substring)

#Nama_Rendra_Adie_Permana
#NIM_2403010111