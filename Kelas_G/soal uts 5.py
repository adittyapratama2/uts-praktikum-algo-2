#NAMA : INSAN DZULFIQOR
#NIM : 2403010174
#KELAS : G
kata = input("Masukan kata :")
posisi_awal = int(input("Masukan posisi awal : "))
panjang_karakter = int(input("Masukan panjang karakter :"))

substring = kata[posisi_awal:posisi_awal+panjang_karakter]
print("Substring:",substring)