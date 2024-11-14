# Meminta pengguna untuk memasukkan sebuah kata
kata = input("Masukkan sebuah kata: ")

# Meminta pengguna untuk memasukkan posisi awal dan panjang karakter
posisi_awal = int(input("Masukkan posisi awal (0 untuk karakter pertama): "))
panjang_karakter = int(input("Masukkan panjang karakter yang ingin diambil: "))

# Mengambil substring sesuai dengan posisi awal dan panjang karakter
substring = kata[posisi_awal:posisi_awal + panjang_karakter]

# Menampilkan hasil
print("Substring yang diambil:", substring)