# Meminta pengguna untuk memasukkan kata
kata = input("Masukkan kata: ")

# Meminta pengguna memasukkan posisi awal dan panjang karakter
posisi_awal = int(input("Masukkan posisi awal: "))
panjang_karakter = int(input("Masukkan panjang karakter: "))

# Mengambil substring berdasarkan posisi awal dan panjang karakter
substring = kata[posisi_awal: posisi_awal + panjang_karakter]

# Menampilkan hasil substring
print("Substring:", substring)

# penjelasan

#Program meminta input berupa kata, posisi awal, dan panjang karakter.

#Menggunakan slicing untuk mengambil substring dari kata sesuai posisi awal dan panjang yang dimasukkan.

#Menampilkan substring yang dihasilkan.

#FahmiZamzamZawahir_2403010132
