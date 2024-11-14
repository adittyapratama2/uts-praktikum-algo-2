#Kandar_Maulana
#2403010119
#E_Informatika

# Meminta input dari pengguna
kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal: "))
panjang_karakter = int(input("Masukkan panjang karakter: "))

# Mengambil substring berdasarkan posisi awal dan panjang karakter
if 0 <= posisi_awal < len(kata):
    substring = kata[posisi_awal:posisi_awal + panjang_karakter]
    print(f"Substring: '{substring}'")
else:
    print("Posisi awal tidak valid.")