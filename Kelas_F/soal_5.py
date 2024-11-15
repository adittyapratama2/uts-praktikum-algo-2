#imanuel tanu senjaya 2403010143
# Program untuk mengambil substring dari kata berdasarkan posisi awal dan panjang karakter

# Meminta input kata dari pengguna
kata = input("Masukkan kata: ")

# Meminta input posisi awal dan panjang karakter
posisi_awal = int(input("Masukkan posisi awal: "))
panjang_karakter = int(input("Masukkan panjang karakter: "))

# Mengambil substring menggunakan slicing
substring = kata[posisi_awal:posisi_awal + panjang_karakter]

# Menampilkan hasil substring
print(f"Substring: {substring}")
