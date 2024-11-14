#Meminta input kata dari pengguna
kata = input("Masukkan kata anda: ")

#Meminta input posisi awal dimulai dari 0 dan panjang karakternya
posisi_awal = int(input("Masukkan posisi awal anda: "))
panjang_karakter = int(input("Masukkan panjang karakter anda: "))

#Mengambil substring dari kata berdasarkan posisi awal dan panjang karakter
substring = kata[posisi_awal:posisi_awal + panjang_karakter]

#Menampilkan substring yang diambilnya
print("Hasil Substring:", substring)