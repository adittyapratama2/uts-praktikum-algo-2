kata = input("masukan sebuah kata: ")

posisi_awal = int(input("masukan posisi awal(dimulai dari 0):"))
panjang_karakter = int(input("masukan panjang karakter yang ingin diambil:"))

subtring = kata[posisi_awal : posisi_awal + panjang_karakter]

print("subtring yang diambil adalah:", subtring)
