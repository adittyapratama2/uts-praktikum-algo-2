kata = input("Masukkan sebuah kata: ")

posisi_awal = int(input("Masukkan posisi awal (indeks mulai dari 0): "))
panjang = int(input("Masukkan panjang substring: "))

substring = kata[posisi_awal:posisi_awal + panjang]

print(f"Substring dari kata '{kata}' mulai dari posisi {posisi_awal} dengan panjang {panjang} adalah: '{substring}'")