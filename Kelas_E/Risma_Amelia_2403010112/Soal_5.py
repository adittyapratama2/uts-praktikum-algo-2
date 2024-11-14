# Masukan kata, posisi awal, dan panjang karakter
kata = str(input("Masukan Kata:"))+ " "
posisi_awal = int(input("Masukan Posisi Awal: "))
panjang_karakter = int(input("Masukan Panjang Karakter: "))
# kata yang diambil berdasarkan posisi awal dan panjang karakter 
substring = kata[posisi_awal:posisi_awal + panjang_karakter]
print(substring)