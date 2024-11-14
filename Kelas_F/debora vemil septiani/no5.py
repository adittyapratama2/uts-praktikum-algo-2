kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal: "))
panjang_karakter = int(input("Masukkan panjang karakter: "))
substring = kata[posisi_awal:posisi_awal + panjang_karakter]
print("Substring:", substring)
