# Soal 5: Mengambil Karakter dari Kata
kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal: ")) - 1
panjang_karakter = int(input("Masukkan panjang karakter: "))
substring = kata[posisi_awal:posisi_awal + panjang_karakter]
print(f"Substring: {substring}")

#Jerry Hilman Firmansyah 2203010512
#program ini dapat menampilkan substring dari kata yang dimasukan oleh penguna
#menggunakan 3 buah inputan berupa 1 string dan 2 integer
#program ini juga menggunakan 1 buah string untuk menampilkan substring
