# Meminta input dari pengguna
kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal: "))
panjang_karakter = int(input("Masukkan panjang karakter: "))

# Mengambil substring berdasarkan posisi_awal dan panjang_karakter
substring = kata[posisi_awal:posisi_awal + panjang_karakter]

# Menampilkan hasil substring
print("Substring:", substring)
