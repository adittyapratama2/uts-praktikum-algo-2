#mengambil karakter dari kata
kata = input("masukan kata")
posisi_awal = int(input("masukan posisi awal(mulai dari 0): "))
panjang = int(input("masukan panjang karakter yang ingin diambil: "))

substring = kata[posisi_awal:posisi_awal + panjang]

print("substring yang diambil:", substring)
