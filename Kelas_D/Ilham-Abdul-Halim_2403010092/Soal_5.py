# Ilham Abdul Halim
# 2403010092

def ambil_substring(kata, posisi_awal, panjang):
    # Mengambil substring sesuai dengan posisi awal dan panjang yang diberikan
    return kata[posisi_awal:posisi_awal + panjang]

# Meminta input dari pengguna
kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal: "))
panjang = int(input("Masukkan panjang karakter: "))

# Menampilkan substring yang diambil berdasarkan posisi awal dan panjang karakter
substring = ambil_substring(kata, posisi_awal, panjang)
print("Substring:",substring)