# Meminta pengguna untuk memasukkan kata, posisi awal, dan panjang karakter
kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal: "))
panjang_karakter = int(input("Masukkan panjang karakter: "))

# Mengambil substring sesuai dengan posisi awal dan panjang karakter
substring = kata[posisi_awal:posisi_awal + panjang_karakter]

# Menampilkan hasil substring
print("Substring:", substring)
