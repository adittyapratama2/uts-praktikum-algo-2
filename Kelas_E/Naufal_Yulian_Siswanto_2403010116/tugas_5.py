# meminta kata input dari pengguna
kata = input("asukan sebuah kata:")

# menerima input posisi awal dan pan jang karakter
posisi_awal = int(input("masukan posisi awal(indeks dimulai dari 0):"))
panjang = int(input("masukan panjang karekter yang ingin di ambil:"))

# masukan substring dengan posisi awal dan panjang karakter
substring = kata[posisi_awal:posisi_awal + panjang]

# menampilkan panjang
print("substring yang diambil:",substring)
