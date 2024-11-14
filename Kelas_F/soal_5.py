def ambil_substring(kata, posisi_awal, panjang):
    
    return kata[posisi_awal:posisi_awal + panjang]

kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal: "))
panjang = int(input("Masukkan panjang karakter: "))

substring = ambil_substring(kata, posisi_awal, panjang)

print("Substring:", substring)