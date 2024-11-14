#Meminta pengguna untuk memasukan kata, posisi awal, dan panjang karakter
kata = input("Masukan Kata: ")
posisi_awal = int(input("Masukan posisi awal: "))
panjang_karakter = int(input("Masukan panjang karakter: "))

#Mengambil substring dari kata
substring = kata[posisi_awal: posisi_awal + panjang_karakter]

#Menampilkan substring yang diambil
print("substring:", substring)