#meminta input kata
kata = input("Masukkan kata: ")
posisi_awal = int((input("Masukan posisi awal: "))) - 1 #mengonversi posisi awal jadi dari 0
panjang_karakter = int((input("Masukan panjang karakter: ")))

#mengambil substring
substring = kata[posisi_awal:posisi_awal+panjang_karakter]
print("Substring: ", substring)