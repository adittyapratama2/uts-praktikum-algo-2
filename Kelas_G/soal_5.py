print("\n--- Mengambil Karakter dari Kata ---\n")

kata = input("Masukkan kata : ")
posisi_awal = int(input("Masukkan posisi awal : ")) - 1
panjang_karakter = int(input("Masukkan panjang karakter : "))

substring = kata[posisi_awal : posisi_awal + panjang_karakter]

print("Substring :", substring)