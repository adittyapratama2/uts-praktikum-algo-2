kata = input("Masukan sebuah kata: ")
posisi_awal = int(input("masukan posisi awal: "))
panjang_karakter = int(input("masukan panjang karakter: "))
substring = kata[posisi_awal: posisi_awal + panjang_karakter]
print("substring yang diambil adalah :",substring)