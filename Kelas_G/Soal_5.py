# Meminta pengguna untuk memasukkan sebuah kata
kata = input("Masukkan sebuah kata: ")

# Meminta pengguna untuk memasukkan posisi awal dan panjang
posisi_awal = int(input("Masukkan posisi awal (0 untuk karakter pertama): "))
panjang = int(input("Masukkan panjang substring yang ingin diambil: "))

# Mengambil substring sesuai dengan posisi awal dan panjang
substring = kata[posisi_awal:posisi_awal + panjang]

# Menampilkan substring yang diambil
print("Substring yang diambil:", substring)