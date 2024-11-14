#Putri Fadilla Maulidia_2403010217
#Mengambil Karakter dari Kata

#input
kata=str(input("Masukkan kata:"))
posisi_awal=int(input("Masukkan posisi awal:"))
panjang_karakter=int(input("Masukkan panjang karakter:"))

#mengambil substring
substring=kata[posisi_awal:posisi_awal+panjang_karakter]

#output
print(f"substring:{substring}")