# Nama: Muhamad Rif'atul Akbar
# NIM: 2403010091
# Kelas: D(TI) 2024

print("Mengambil Karakter dari Kata")
Kata = str(input("Masukkan kata: "))
Posisi_awal = int(input("Masukkan posisi awal yang ingin dipilih (hitungnya dari 0): "))
Panjang_karakter = int(input("Masukkan panjang karakternya: "))
substring = Kata[Posisi_awal:Posisi_awal+Panjang_karakter]
print("substring: ",substring)