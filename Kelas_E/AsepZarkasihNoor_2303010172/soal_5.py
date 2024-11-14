# Nama: Asep Zarkasih Noor
# NIM: 2303010172
# Deskripsi: Program Mengambil Karakter dari Kata

# Meminta pengguna memasukkan kata dan parameter substring
kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal: "))
panjang_karakter = int(input("Masukkan panjang karakter: "))

# Mengambil substring berdasarkan posisi awal dan panjang karakter
substring = kata[posisi_awal:posisi_awal + panjang_karakter]

# Menampilkan hasil substring
print("Substring:", substring)
