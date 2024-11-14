# soal no 5
kata = input("Masukkan sebuah kata:")
posisi_awal = int(input("masukkan posisi awal:"))
panjang_karakter = int(input("masukkan panjang karakter yang ingin diambil:"))
substring = kata[posisi_awal+panjang_karakter]
print (f"substring yang diambil dari posisi {posisi_awal} dengan panjang {panjang_karakter} adalah: {substring}")