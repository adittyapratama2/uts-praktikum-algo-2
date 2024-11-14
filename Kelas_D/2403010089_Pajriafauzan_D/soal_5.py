#Mengambil Karakter dari Kata

kata = input("masukan sebuah kata: ")

posisi_awal = int(input("masukan posisi awal (index mulai dari 0):"))
panjang = int(input("masukan panjang substring: "))

substring = kata[posisi_awal:posisi_awal + panjang]

print(f"substring dari kata '{kata}' mulai dari posisi {posisi_awal} dengan panjang {panjang} adalah: '{substring}'")