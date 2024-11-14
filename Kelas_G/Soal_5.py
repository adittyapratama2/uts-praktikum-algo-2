#NAMA : MUHAMMAD DARIS RIF'AN RAMADHAN
#NIM  : 2403010164
# Meminta pengguna untuk memasukkan kata
kata = input("Masukkan sebuah kata: ")

# Meminta pengguna memasukkan posisi awal dan panjang karakter
posisi_awal = int(input("Masukkan posisi awal (dimulai dari 0): "))
panjang_karakter = int(input("Masukkan panjang karakter yang ingin diambil: "))

# Mengambil substring sesuai posisi awal dan panjang karakter
substring = kata[posisi_awal: posisi_awal + panjang_karakter]

# Menampilkan hasil substring
print("Substring yang diambil adalah:", substring)