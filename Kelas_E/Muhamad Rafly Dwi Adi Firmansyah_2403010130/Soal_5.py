#Nama:Muhamad Rafly Dwi Adi Firmansyah
#NIM:2403010130
#Kelas:TI-E-24

print("------Mengambil Karakter dari Kata------")
print(" ")
kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal (mulai dari 0): "))
panjang = int(input("Masukkan panjang karakter yang ingin diambil: "))

substring = kata[posisi_awal:posisi_awal + panjang]

print("Substring yang diambil:", substring)