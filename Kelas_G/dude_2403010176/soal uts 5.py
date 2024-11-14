#NAMA : DUDE DWI BUDIANTO
#NIM : 2403010176
#KELAS : G
# MENGAMBIL KARAKTER DARI KATA
kata = input("Masukan kata :")
posisi_awal = int(input("Masukan posisi awal : "))
panjang_karakter = int(input("Masukan panjang karakter :"))

substring = kata[posisi_awal:posisi_awal+panjang_karakter]
print("Substring:",substring)